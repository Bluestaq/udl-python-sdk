# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from datetime import datetime
from typing_extensions import Literal

import httpx

from ...types import airfieldstatus_create_params
from .history import (
    HistoryResource,
    AsyncHistoryResource,
    HistoryResourceWithRawResponse,
    AsyncHistoryResourceWithRawResponse,
    HistoryResourceWithStreamingResponse,
    AsyncHistoryResourceWithStreamingResponse,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.airfieldstatus_list_response import AirfieldstatusListResponse

__all__ = ["AirfieldstatusResource", "AsyncAirfieldstatusResource"]


class AirfieldstatusResource(SyncAPIResource):
    @cached_property
    def history(self) -> HistoryResource:
        return HistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> AirfieldstatusResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/rsivilli-bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AirfieldstatusResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AirfieldstatusResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/rsivilli-bluestaq/udl-python-sdk#with_streaming_response
        """
        return AirfieldstatusResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        id_airfield: str,
        source: str,
        id: str | NotGiven = NOT_GIVEN,
        alt_airfield_id: str | NotGiven = NOT_GIVEN,
        approved_by: str | NotGiven = NOT_GIVEN,
        approved_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        arff_cat: str | NotGiven = NOT_GIVEN,
        cargo_mog: int | NotGiven = NOT_GIVEN,
        fleet_service_mog: int | NotGiven = NOT_GIVEN,
        fuel_mog: int | NotGiven = NOT_GIVEN,
        fuel_qtys: Iterable[float] | NotGiven = NOT_GIVEN,
        fuel_types: List[str] | NotGiven = NOT_GIVEN,
        gse_time: int | NotGiven = NOT_GIVEN,
        med_cap: str | NotGiven = NOT_GIVEN,
        message: str | NotGiven = NOT_GIVEN,
        mhe_qtys: Iterable[int] | NotGiven = NOT_GIVEN,
        mhe_types: List[str] | NotGiven = NOT_GIVEN,
        mx_mog: int | NotGiven = NOT_GIVEN,
        narrow_parking_mog: int | NotGiven = NOT_GIVEN,
        narrow_working_mog: int | NotGiven = NOT_GIVEN,
        num_cog: int | NotGiven = NOT_GIVEN,
        operating_mog: int | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        passenger_service_mog: int | NotGiven = NOT_GIVEN,
        pri_freq: float | NotGiven = NOT_GIVEN,
        pri_rwy_num: str | NotGiven = NOT_GIVEN,
        reviewed_by: str | NotGiven = NOT_GIVEN,
        reviewed_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        rwy_cond_reading: int | NotGiven = NOT_GIVEN,
        rwy_friction_factor: int | NotGiven = NOT_GIVEN,
        rwy_markings: List[str] | NotGiven = NOT_GIVEN,
        slot_types_req: List[str] | NotGiven = NOT_GIVEN,
        survey_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        wide_parking_mog: int | NotGiven = NOT_GIVEN,
        wide_working_mog: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single airfield status record as a POST body and
        ingest into the database. This operation is not intended to be used for
        automated feeds into UDL. Data providers should contact the UDL team for
        specific role assignments and for instructions on setting up a permanent feed
        through an alternate mechanism.

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

          id_airfield: Unique identifier of the Airfield for which this status is referencing.

          source: Source of the data.

          id: Unique identifier of the record, auto-generated by the system.

          alt_airfield_id: Alternate airfield identifier provided by the source.

          approved_by: The name of the person who approved the airfield survey review.

          approved_date: The date that survey review changes were approved for this airfield, in ISO 8601
              UTC format with millisecond precision.

          arff_cat: The category of aircraft rescue and fire fighting (ARFF) services that are
              currently available at the airfield. Entries should include the code (FAA or
              ICAO) and the category.

          cargo_mog: Maximum on ground (MOG) number of high-reach/wide-body cargo aircraft that can
              be serviced simultaneously based on spacing and manpower at the time of status.

          fleet_service_mog: Maximum on ground (MOG) number of fleet aircraft that can be serviced
              simultaneously based on spacing and manpower at the time of status.

          fuel_mog: Maximum on ground (MOG) number of aircraft that can be simultaneously refueled
              based on spacing and manpower at the time of status.

          fuel_qtys: Array of quantities for each fuel type at the airfield, in kilograms. The values
              in this array must correspond to the position index in fuelTypes. This array
              must be the same length as fuelTypes.

          fuel_types: Array of fuel types available at the airfield. This array must be the same
              length as fuelQtys.

          gse_time: The expected time to receive ground support equipment (e.g. power units, air
              units, cables, hoses, etc.), in minutes.

          med_cap: The level of medical support and capabilities available at the airfield.

          message: Description of the current status of the airfield.

          mhe_qtys: Array of quantities for each material handling equipment types at the airfield.
              The values in this array must correspond to the position index in mheTypes. This
              array must be the same length as mheTypes.

          mhe_types: Array of material handling equipment types at the airfield. This array must be
              the same length as mheQtys.

          mx_mog: Maximum on ground (MOG) number of aircraft that can be simultaneously ground
              handled for standard maintenance based on spacing and manpower at the time of
              status.

          narrow_parking_mog: Maximum on ground (MOG) number of parking narrow-body aircraft based on spacing
              and manpower at the time of status.

          narrow_working_mog: Maximum on ground (MOG) number of working narrow-body aircraft based on spacing
              and manpower at the time of status.

          num_cog: The number of aircraft that are currently on ground (COG) at the airfield.

          operating_mog: Maximum on ground (MOG) number of aircraft due to items not directly related to
              the airfield infrastructure or aircraft servicing capability based on spacing
              and manpower at the time of status.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          passenger_service_mog: Maximum on ground (MOG) number of high-reach/wide-body passenger aircraft that
              can be serviced simultaneously based on spacing and manpower at the time of
              status.

          pri_freq: The primary frequency which the airfield is currently operating, in megahertz.

          pri_rwy_num: The number or ID of primary runway at the airfield.

          reviewed_by: The name of the person who reviewed the airfield survey.

          reviewed_date: The date the airfield survey was reviewed, in ISO 8601 UTC format with
              millisecond precision.

          rwy_cond_reading: The primary runway condition reading value used for determining runway braking
              action, from 0 to 26. A value of 0 indicates braking action is poor or
              non-existent, where a value of 26 indicates braking action is good.

          rwy_friction_factor: The primary runway friction factor which is dependent on the surface friction
              between the tires of the aircraft and the runway surface, from 0 to 100. A lower
              number indicates less friction and less braking response.

          rwy_markings: Array of markings currently on the primary runway.

          slot_types_req: Array of slot types that an airfield requires a particular aircraft provide in
              order to consume a slot at this location.

          survey_date: The date the airfield survey was performed, in ISO 8601 UTC format with
              millisecond precision.

          wide_parking_mog: Maximum on ground (MOG) number of parking wide-body aircraft based on spacing
              and manpower at the time of status. Additional information about this field as
              it pertains to specific aircraft type may be available in an associated
              SiteOperations record.

          wide_working_mog: Maximum on ground (MOG) number of working wide-body aircraft based on spacing
              and manpower at the time of status. Additional information about this field as
              it pertains to specific aircraft type may be available in an associated
              SiteOperations record.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/udl/airfieldstatus",
            body=maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "id_airfield": id_airfield,
                    "source": source,
                    "id": id,
                    "alt_airfield_id": alt_airfield_id,
                    "approved_by": approved_by,
                    "approved_date": approved_date,
                    "arff_cat": arff_cat,
                    "cargo_mog": cargo_mog,
                    "fleet_service_mog": fleet_service_mog,
                    "fuel_mog": fuel_mog,
                    "fuel_qtys": fuel_qtys,
                    "fuel_types": fuel_types,
                    "gse_time": gse_time,
                    "med_cap": med_cap,
                    "message": message,
                    "mhe_qtys": mhe_qtys,
                    "mhe_types": mhe_types,
                    "mx_mog": mx_mog,
                    "narrow_parking_mog": narrow_parking_mog,
                    "narrow_working_mog": narrow_working_mog,
                    "num_cog": num_cog,
                    "operating_mog": operating_mog,
                    "origin": origin,
                    "passenger_service_mog": passenger_service_mog,
                    "pri_freq": pri_freq,
                    "pri_rwy_num": pri_rwy_num,
                    "reviewed_by": reviewed_by,
                    "reviewed_date": reviewed_date,
                    "rwy_cond_reading": rwy_cond_reading,
                    "rwy_friction_factor": rwy_friction_factor,
                    "rwy_markings": rwy_markings,
                    "slot_types_req": slot_types_req,
                    "survey_date": survey_date,
                    "wide_parking_mog": wide_parking_mog,
                    "wide_working_mog": wide_working_mog,
                },
                airfieldstatus_create_params.AirfieldstatusCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AirfieldstatusListResponse:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.
        """
        return self._get(
            "/udl/airfieldstatus",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AirfieldstatusListResponse,
        )

    def count(
        self,
        *,
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
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return self._get(
            "/udl/airfieldstatus/count",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
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
            "/udl/airfieldstatus/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncAirfieldstatusResource(AsyncAPIResource):
    @cached_property
    def history(self) -> AsyncHistoryResource:
        return AsyncHistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAirfieldstatusResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/rsivilli-bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncAirfieldstatusResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAirfieldstatusResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/rsivilli-bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncAirfieldstatusResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        id_airfield: str,
        source: str,
        id: str | NotGiven = NOT_GIVEN,
        alt_airfield_id: str | NotGiven = NOT_GIVEN,
        approved_by: str | NotGiven = NOT_GIVEN,
        approved_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        arff_cat: str | NotGiven = NOT_GIVEN,
        cargo_mog: int | NotGiven = NOT_GIVEN,
        fleet_service_mog: int | NotGiven = NOT_GIVEN,
        fuel_mog: int | NotGiven = NOT_GIVEN,
        fuel_qtys: Iterable[float] | NotGiven = NOT_GIVEN,
        fuel_types: List[str] | NotGiven = NOT_GIVEN,
        gse_time: int | NotGiven = NOT_GIVEN,
        med_cap: str | NotGiven = NOT_GIVEN,
        message: str | NotGiven = NOT_GIVEN,
        mhe_qtys: Iterable[int] | NotGiven = NOT_GIVEN,
        mhe_types: List[str] | NotGiven = NOT_GIVEN,
        mx_mog: int | NotGiven = NOT_GIVEN,
        narrow_parking_mog: int | NotGiven = NOT_GIVEN,
        narrow_working_mog: int | NotGiven = NOT_GIVEN,
        num_cog: int | NotGiven = NOT_GIVEN,
        operating_mog: int | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        passenger_service_mog: int | NotGiven = NOT_GIVEN,
        pri_freq: float | NotGiven = NOT_GIVEN,
        pri_rwy_num: str | NotGiven = NOT_GIVEN,
        reviewed_by: str | NotGiven = NOT_GIVEN,
        reviewed_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        rwy_cond_reading: int | NotGiven = NOT_GIVEN,
        rwy_friction_factor: int | NotGiven = NOT_GIVEN,
        rwy_markings: List[str] | NotGiven = NOT_GIVEN,
        slot_types_req: List[str] | NotGiven = NOT_GIVEN,
        survey_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        wide_parking_mog: int | NotGiven = NOT_GIVEN,
        wide_working_mog: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single airfield status record as a POST body and
        ingest into the database. This operation is not intended to be used for
        automated feeds into UDL. Data providers should contact the UDL team for
        specific role assignments and for instructions on setting up a permanent feed
        through an alternate mechanism.

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

          id_airfield: Unique identifier of the Airfield for which this status is referencing.

          source: Source of the data.

          id: Unique identifier of the record, auto-generated by the system.

          alt_airfield_id: Alternate airfield identifier provided by the source.

          approved_by: The name of the person who approved the airfield survey review.

          approved_date: The date that survey review changes were approved for this airfield, in ISO 8601
              UTC format with millisecond precision.

          arff_cat: The category of aircraft rescue and fire fighting (ARFF) services that are
              currently available at the airfield. Entries should include the code (FAA or
              ICAO) and the category.

          cargo_mog: Maximum on ground (MOG) number of high-reach/wide-body cargo aircraft that can
              be serviced simultaneously based on spacing and manpower at the time of status.

          fleet_service_mog: Maximum on ground (MOG) number of fleet aircraft that can be serviced
              simultaneously based on spacing and manpower at the time of status.

          fuel_mog: Maximum on ground (MOG) number of aircraft that can be simultaneously refueled
              based on spacing and manpower at the time of status.

          fuel_qtys: Array of quantities for each fuel type at the airfield, in kilograms. The values
              in this array must correspond to the position index in fuelTypes. This array
              must be the same length as fuelTypes.

          fuel_types: Array of fuel types available at the airfield. This array must be the same
              length as fuelQtys.

          gse_time: The expected time to receive ground support equipment (e.g. power units, air
              units, cables, hoses, etc.), in minutes.

          med_cap: The level of medical support and capabilities available at the airfield.

          message: Description of the current status of the airfield.

          mhe_qtys: Array of quantities for each material handling equipment types at the airfield.
              The values in this array must correspond to the position index in mheTypes. This
              array must be the same length as mheTypes.

          mhe_types: Array of material handling equipment types at the airfield. This array must be
              the same length as mheQtys.

          mx_mog: Maximum on ground (MOG) number of aircraft that can be simultaneously ground
              handled for standard maintenance based on spacing and manpower at the time of
              status.

          narrow_parking_mog: Maximum on ground (MOG) number of parking narrow-body aircraft based on spacing
              and manpower at the time of status.

          narrow_working_mog: Maximum on ground (MOG) number of working narrow-body aircraft based on spacing
              and manpower at the time of status.

          num_cog: The number of aircraft that are currently on ground (COG) at the airfield.

          operating_mog: Maximum on ground (MOG) number of aircraft due to items not directly related to
              the airfield infrastructure or aircraft servicing capability based on spacing
              and manpower at the time of status.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          passenger_service_mog: Maximum on ground (MOG) number of high-reach/wide-body passenger aircraft that
              can be serviced simultaneously based on spacing and manpower at the time of
              status.

          pri_freq: The primary frequency which the airfield is currently operating, in megahertz.

          pri_rwy_num: The number or ID of primary runway at the airfield.

          reviewed_by: The name of the person who reviewed the airfield survey.

          reviewed_date: The date the airfield survey was reviewed, in ISO 8601 UTC format with
              millisecond precision.

          rwy_cond_reading: The primary runway condition reading value used for determining runway braking
              action, from 0 to 26. A value of 0 indicates braking action is poor or
              non-existent, where a value of 26 indicates braking action is good.

          rwy_friction_factor: The primary runway friction factor which is dependent on the surface friction
              between the tires of the aircraft and the runway surface, from 0 to 100. A lower
              number indicates less friction and less braking response.

          rwy_markings: Array of markings currently on the primary runway.

          slot_types_req: Array of slot types that an airfield requires a particular aircraft provide in
              order to consume a slot at this location.

          survey_date: The date the airfield survey was performed, in ISO 8601 UTC format with
              millisecond precision.

          wide_parking_mog: Maximum on ground (MOG) number of parking wide-body aircraft based on spacing
              and manpower at the time of status. Additional information about this field as
              it pertains to specific aircraft type may be available in an associated
              SiteOperations record.

          wide_working_mog: Maximum on ground (MOG) number of working wide-body aircraft based on spacing
              and manpower at the time of status. Additional information about this field as
              it pertains to specific aircraft type may be available in an associated
              SiteOperations record.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/udl/airfieldstatus",
            body=await async_maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "id_airfield": id_airfield,
                    "source": source,
                    "id": id,
                    "alt_airfield_id": alt_airfield_id,
                    "approved_by": approved_by,
                    "approved_date": approved_date,
                    "arff_cat": arff_cat,
                    "cargo_mog": cargo_mog,
                    "fleet_service_mog": fleet_service_mog,
                    "fuel_mog": fuel_mog,
                    "fuel_qtys": fuel_qtys,
                    "fuel_types": fuel_types,
                    "gse_time": gse_time,
                    "med_cap": med_cap,
                    "message": message,
                    "mhe_qtys": mhe_qtys,
                    "mhe_types": mhe_types,
                    "mx_mog": mx_mog,
                    "narrow_parking_mog": narrow_parking_mog,
                    "narrow_working_mog": narrow_working_mog,
                    "num_cog": num_cog,
                    "operating_mog": operating_mog,
                    "origin": origin,
                    "passenger_service_mog": passenger_service_mog,
                    "pri_freq": pri_freq,
                    "pri_rwy_num": pri_rwy_num,
                    "reviewed_by": reviewed_by,
                    "reviewed_date": reviewed_date,
                    "rwy_cond_reading": rwy_cond_reading,
                    "rwy_friction_factor": rwy_friction_factor,
                    "rwy_markings": rwy_markings,
                    "slot_types_req": slot_types_req,
                    "survey_date": survey_date,
                    "wide_parking_mog": wide_parking_mog,
                    "wide_working_mog": wide_working_mog,
                },
                airfieldstatus_create_params.AirfieldstatusCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AirfieldstatusListResponse:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.
        """
        return await self._get(
            "/udl/airfieldstatus",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AirfieldstatusListResponse,
        )

    async def count(
        self,
        *,
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
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return await self._get(
            "/udl/airfieldstatus/count",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
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
            "/udl/airfieldstatus/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AirfieldstatusResourceWithRawResponse:
    def __init__(self, airfieldstatus: AirfieldstatusResource) -> None:
        self._airfieldstatus = airfieldstatus

        self.create = to_raw_response_wrapper(
            airfieldstatus.create,
        )
        self.list = to_raw_response_wrapper(
            airfieldstatus.list,
        )
        self.count = to_raw_response_wrapper(
            airfieldstatus.count,
        )
        self.queryhelp = to_raw_response_wrapper(
            airfieldstatus.queryhelp,
        )

    @cached_property
    def history(self) -> HistoryResourceWithRawResponse:
        return HistoryResourceWithRawResponse(self._airfieldstatus.history)


class AsyncAirfieldstatusResourceWithRawResponse:
    def __init__(self, airfieldstatus: AsyncAirfieldstatusResource) -> None:
        self._airfieldstatus = airfieldstatus

        self.create = async_to_raw_response_wrapper(
            airfieldstatus.create,
        )
        self.list = async_to_raw_response_wrapper(
            airfieldstatus.list,
        )
        self.count = async_to_raw_response_wrapper(
            airfieldstatus.count,
        )
        self.queryhelp = async_to_raw_response_wrapper(
            airfieldstatus.queryhelp,
        )

    @cached_property
    def history(self) -> AsyncHistoryResourceWithRawResponse:
        return AsyncHistoryResourceWithRawResponse(self._airfieldstatus.history)


class AirfieldstatusResourceWithStreamingResponse:
    def __init__(self, airfieldstatus: AirfieldstatusResource) -> None:
        self._airfieldstatus = airfieldstatus

        self.create = to_streamed_response_wrapper(
            airfieldstatus.create,
        )
        self.list = to_streamed_response_wrapper(
            airfieldstatus.list,
        )
        self.count = to_streamed_response_wrapper(
            airfieldstatus.count,
        )
        self.queryhelp = to_streamed_response_wrapper(
            airfieldstatus.queryhelp,
        )

    @cached_property
    def history(self) -> HistoryResourceWithStreamingResponse:
        return HistoryResourceWithStreamingResponse(self._airfieldstatus.history)


class AsyncAirfieldstatusResourceWithStreamingResponse:
    def __init__(self, airfieldstatus: AsyncAirfieldstatusResource) -> None:
        self._airfieldstatus = airfieldstatus

        self.create = async_to_streamed_response_wrapper(
            airfieldstatus.create,
        )
        self.list = async_to_streamed_response_wrapper(
            airfieldstatus.list,
        )
        self.count = async_to_streamed_response_wrapper(
            airfieldstatus.count,
        )
        self.queryhelp = async_to_streamed_response_wrapper(
            airfieldstatus.queryhelp,
        )

    @cached_property
    def history(self) -> AsyncHistoryResourceWithStreamingResponse:
        return AsyncHistoryResourceWithStreamingResponse(self._airfieldstatus.history)
