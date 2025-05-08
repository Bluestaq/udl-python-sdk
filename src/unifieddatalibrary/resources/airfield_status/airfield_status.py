# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from datetime import datetime
from typing_extensions import Literal

import httpx

from ...types import (
    airfield_status_list_params,
    airfield_status_count_params,
    airfield_status_tuple_params,
    airfield_status_create_params,
    airfield_status_update_params,
    airfield_status_retrieve_params,
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
from ...types.airfieldstatus_full import AirfieldstatusFull
from ...types.airfieldstatus_abridged import AirfieldstatusAbridged
from ...types.airfield_status_tuple_response import AirfieldStatusTupleResponse

__all__ = ["AirfieldStatusResource", "AsyncAirfieldStatusResource"]


class AirfieldStatusResource(SyncAPIResource):
    @cached_property
    def history(self) -> HistoryResource:
        return HistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> AirfieldStatusResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AirfieldStatusResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AirfieldStatusResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AirfieldStatusResourceWithStreamingResponse(self)

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
                airfield_status_create_params.AirfieldStatusCreateParams,
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
    ) -> AirfieldstatusFull:
        """
        Service operation to get a single airfield status record by its unique ID passed
        as a path parameter.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/udl/airfieldstatus/{id}",
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
                    airfield_status_retrieve_params.AirfieldStatusRetrieveParams,
                ),
            ),
            cast_to=AirfieldstatusFull,
        )

    def update(
        self,
        path_id: str,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        id_airfield: str,
        source: str,
        body_id: str | NotGiven = NOT_GIVEN,
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
        """Service operation to update a single airfield status record.

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

          id_airfield: Unique identifier of the Airfield for which this status is referencing.

          source: Source of the data.

          body_id: Unique identifier of the record, auto-generated by the system.

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
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            f"/udl/airfieldstatus/{path_id}",
            body=maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "id_airfield": id_airfield,
                    "source": source,
                    "body_id": body_id,
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
                airfield_status_update_params.AirfieldStatusUpdateParams,
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
    ) -> SyncOffsetPage[AirfieldstatusAbridged]:
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
            "/udl/airfieldstatus",
            page=SyncOffsetPage[AirfieldstatusAbridged],
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
                    airfield_status_list_params.AirfieldStatusListParams,
                ),
            ),
            model=AirfieldstatusAbridged,
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
        Service operation to delete a Status object specified by the passed ID path
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
            f"/udl/airfieldstatus/{id}",
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
            "/udl/airfieldstatus/count",
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
                    airfield_status_count_params.AirfieldStatusCountParams,
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
            "/udl/airfieldstatus/queryhelp",
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
    ) -> AirfieldStatusTupleResponse:
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
            "/udl/airfieldstatus/tuple",
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
                    airfield_status_tuple_params.AirfieldStatusTupleParams,
                ),
            ),
            cast_to=AirfieldStatusTupleResponse,
        )


class AsyncAirfieldStatusResource(AsyncAPIResource):
    @cached_property
    def history(self) -> AsyncHistoryResource:
        return AsyncHistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAirfieldStatusResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncAirfieldStatusResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAirfieldStatusResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncAirfieldStatusResourceWithStreamingResponse(self)

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
                airfield_status_create_params.AirfieldStatusCreateParams,
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
    ) -> AirfieldstatusFull:
        """
        Service operation to get a single airfield status record by its unique ID passed
        as a path parameter.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/udl/airfieldstatus/{id}",
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
                    airfield_status_retrieve_params.AirfieldStatusRetrieveParams,
                ),
            ),
            cast_to=AirfieldstatusFull,
        )

    async def update(
        self,
        path_id: str,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        id_airfield: str,
        source: str,
        body_id: str | NotGiven = NOT_GIVEN,
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
        """Service operation to update a single airfield status record.

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

          id_airfield: Unique identifier of the Airfield for which this status is referencing.

          source: Source of the data.

          body_id: Unique identifier of the record, auto-generated by the system.

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
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            f"/udl/airfieldstatus/{path_id}",
            body=await async_maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "id_airfield": id_airfield,
                    "source": source,
                    "body_id": body_id,
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
                airfield_status_update_params.AirfieldStatusUpdateParams,
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
    ) -> AsyncPaginator[AirfieldstatusAbridged, AsyncOffsetPage[AirfieldstatusAbridged]]:
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
            "/udl/airfieldstatus",
            page=AsyncOffsetPage[AirfieldstatusAbridged],
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
                    airfield_status_list_params.AirfieldStatusListParams,
                ),
            ),
            model=AirfieldstatusAbridged,
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
        Service operation to delete a Status object specified by the passed ID path
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
            f"/udl/airfieldstatus/{id}",
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
            "/udl/airfieldstatus/count",
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
                    airfield_status_count_params.AirfieldStatusCountParams,
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
            "/udl/airfieldstatus/queryhelp",
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
    ) -> AirfieldStatusTupleResponse:
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
            "/udl/airfieldstatus/tuple",
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
                    airfield_status_tuple_params.AirfieldStatusTupleParams,
                ),
            ),
            cast_to=AirfieldStatusTupleResponse,
        )


class AirfieldStatusResourceWithRawResponse:
    def __init__(self, airfield_status: AirfieldStatusResource) -> None:
        self._airfield_status = airfield_status

        self.create = to_raw_response_wrapper(
            airfield_status.create,
        )
        self.retrieve = to_raw_response_wrapper(
            airfield_status.retrieve,
        )
        self.update = to_raw_response_wrapper(
            airfield_status.update,
        )
        self.list = to_raw_response_wrapper(
            airfield_status.list,
        )
        self.delete = to_raw_response_wrapper(
            airfield_status.delete,
        )
        self.count = to_raw_response_wrapper(
            airfield_status.count,
        )
        self.queryhelp = to_raw_response_wrapper(
            airfield_status.queryhelp,
        )
        self.tuple = to_raw_response_wrapper(
            airfield_status.tuple,
        )

    @cached_property
    def history(self) -> HistoryResourceWithRawResponse:
        return HistoryResourceWithRawResponse(self._airfield_status.history)


class AsyncAirfieldStatusResourceWithRawResponse:
    def __init__(self, airfield_status: AsyncAirfieldStatusResource) -> None:
        self._airfield_status = airfield_status

        self.create = async_to_raw_response_wrapper(
            airfield_status.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            airfield_status.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            airfield_status.update,
        )
        self.list = async_to_raw_response_wrapper(
            airfield_status.list,
        )
        self.delete = async_to_raw_response_wrapper(
            airfield_status.delete,
        )
        self.count = async_to_raw_response_wrapper(
            airfield_status.count,
        )
        self.queryhelp = async_to_raw_response_wrapper(
            airfield_status.queryhelp,
        )
        self.tuple = async_to_raw_response_wrapper(
            airfield_status.tuple,
        )

    @cached_property
    def history(self) -> AsyncHistoryResourceWithRawResponse:
        return AsyncHistoryResourceWithRawResponse(self._airfield_status.history)


class AirfieldStatusResourceWithStreamingResponse:
    def __init__(self, airfield_status: AirfieldStatusResource) -> None:
        self._airfield_status = airfield_status

        self.create = to_streamed_response_wrapper(
            airfield_status.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            airfield_status.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            airfield_status.update,
        )
        self.list = to_streamed_response_wrapper(
            airfield_status.list,
        )
        self.delete = to_streamed_response_wrapper(
            airfield_status.delete,
        )
        self.count = to_streamed_response_wrapper(
            airfield_status.count,
        )
        self.queryhelp = to_streamed_response_wrapper(
            airfield_status.queryhelp,
        )
        self.tuple = to_streamed_response_wrapper(
            airfield_status.tuple,
        )

    @cached_property
    def history(self) -> HistoryResourceWithStreamingResponse:
        return HistoryResourceWithStreamingResponse(self._airfield_status.history)


class AsyncAirfieldStatusResourceWithStreamingResponse:
    def __init__(self, airfield_status: AsyncAirfieldStatusResource) -> None:
        self._airfield_status = airfield_status

        self.create = async_to_streamed_response_wrapper(
            airfield_status.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            airfield_status.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            airfield_status.update,
        )
        self.list = async_to_streamed_response_wrapper(
            airfield_status.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            airfield_status.delete,
        )
        self.count = async_to_streamed_response_wrapper(
            airfield_status.count,
        )
        self.queryhelp = async_to_streamed_response_wrapper(
            airfield_status.queryhelp,
        )
        self.tuple = async_to_streamed_response_wrapper(
            airfield_status.tuple,
        )

    @cached_property
    def history(self) -> AsyncHistoryResourceWithStreamingResponse:
        return AsyncHistoryResourceWithStreamingResponse(self._airfield_status.history)
