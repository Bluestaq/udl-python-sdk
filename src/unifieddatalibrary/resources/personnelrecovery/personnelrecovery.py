# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime
from typing_extensions import Literal

import httpx

from ...types import (
    personnelrecovery_get_params,
    personnelrecovery_list_params,
    personnelrecovery_count_params,
    personnelrecovery_tuple_params,
    personnelrecovery_create_params,
    personnelrecovery_create_bulk_params,
    personnelrecovery_file_create_params,
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
from ...types.personnel_recovery_full_l import PersonnelRecoveryFullL
from ...types.personnelrecovery_list_response import PersonnelrecoveryListResponse
from ...types.personnelrecovery_tuple_response import PersonnelrecoveryTupleResponse

__all__ = ["PersonnelrecoveryResource", "AsyncPersonnelrecoveryResource"]


class PersonnelrecoveryResource(SyncAPIResource):
    @cached_property
    def history(self) -> HistoryResource:
        return HistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> PersonnelrecoveryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return PersonnelrecoveryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PersonnelrecoveryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return PersonnelrecoveryResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        msg_time: Union[str, datetime],
        pickup_lat: float,
        pickup_lon: float,
        source: str,
        type: str,
        id: str | NotGiven = NOT_GIVEN,
        auth_method: str | NotGiven = NOT_GIVEN,
        auth_status: str | NotGiven = NOT_GIVEN,
        beacon_ind: bool | NotGiven = NOT_GIVEN,
        call_sign: str | NotGiven = NOT_GIVEN,
        comm_eq1: str | NotGiven = NOT_GIVEN,
        comm_eq2: str | NotGiven = NOT_GIVEN,
        comm_eq3: str | NotGiven = NOT_GIVEN,
        execution_info: personnelrecovery_create_params.ExecutionInfo | NotGiven = NOT_GIVEN,
        identity: str | NotGiven = NOT_GIVEN,
        id_weather_report: str | NotGiven = NOT_GIVEN,
        mil_class: str | NotGiven = NOT_GIVEN,
        nat_alliance: int | NotGiven = NOT_GIVEN,
        nat_alliance1: int | NotGiven = NOT_GIVEN,
        num_ambulatory: int | NotGiven = NOT_GIVEN,
        num_ambulatory_injured: int | NotGiven = NOT_GIVEN,
        num_non_ambulatory: int | NotGiven = NOT_GIVEN,
        num_persons: int | NotGiven = NOT_GIVEN,
        objective_area_info: personnelrecovery_create_params.ObjectiveAreaInfo | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        pickup_alt: float | NotGiven = NOT_GIVEN,
        recov_id: str | NotGiven = NOT_GIVEN,
        rx_freq: float | NotGiven = NOT_GIVEN,
        survivor_messages: str | NotGiven = NOT_GIVEN,
        survivor_radio: str | NotGiven = NOT_GIVEN,
        term_ind: bool | NotGiven = NOT_GIVEN,
        text_msg: str | NotGiven = NOT_GIVEN,
        tx_freq: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single Personnel Recovery object as a POST body and
        ingest into the database. Requires a specific role, please contact the UDL team
        to gain access.

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

          msg_time: Time stamp of the original personnel recovery message, in ISO 8601 UTC format.

          pickup_lat: WGS-84 latitude of the pickup location, in degrees. -90 to 90 degrees (negative
              values south of equator).

          pickup_lon: WGS-84 longitude of the pickup location, in degrees. -180 to 180 degrees
              (negative values west of Prime Meridian).

          source: Source of the data.

          type: Specifies the type of incident resulting in a recovery or evacuation mission.
              Intended as, but not constrained to, MIL-STD-6016 J6.1 Emergency Type (e.g. NO
              STATEMENT, DOWN AIRCRAFT, MAN IN WATER, DITCHING, BAILOUT, DISTRESSED VEHICLE,
              GROUND INCIDENT, MEDICAL, ISOLATED PERSONS, etc.).

          id: Unique identifier of the record, auto-generated by the system.

          auth_method: Mechanism used to verify the survivors identity.

          auth_status: The confirmation status of the isolated personnel identity. Intended as, but not
              constrained to, MIL-STD-6016 J6.1 Authentication Status, Isolated Personnel (NO
              STATEMENT, AUTHENTICATED, NOT AUTHENTICATED, AUTHENTICATED UNDER DURESS, NOT
              APPLICABLE):

              AUTHENTICATED: Confirmed Friend

              NOT AUTHENTICATED: Unconfirmed status

              AUTHENTICATED UNDER DURESS: Authentication comprised by hostiles.

              NOT APPLICABLE: Authentication not required.

          beacon_ind: Flag indicating whether a radio identifier is reported.

          call_sign: The call sign of the personnel to be recovered.

          comm_eq1: Survivor communications equipment. Intended as, but not constrained to,
              MIL-STD-6016 J6.1 Communications Equipment, Isolated Personnel (NO STATEMENT,
              SURVIVAL RADIO, RADIO BEACON, EPLRS, SIGNAL MIRROR, SMOKE FLARE, IR SIGNALLING
              DEVICE, SIGNALLING PANEL, FRIENDLY FORCE TRACKER, GPS BEACON, LL PHONE, TACTICAL
              RADIO LOS, TACTICAL RADIO BLOS).

          comm_eq2: Survivor communications equipment. Intended as, but not constrained to,
              MIL-STD-6016 J6.1 Communications Equipment, Isolated Personnel (NO STATEMENT,
              SURVIVAL RADIO, RADIO BEACON, EPLRS, SIGNAL MIRROR, SMOKE FLARE, IR SIGNALLING
              DEVICE, SIGNALLING PANEL, FRIENDLY FORCE TRACKER, GPS BEACON, LL PHONE, TACTICAL
              RADIO LOS, TACTICAL RADIO BLOS).

          comm_eq3: Survivor communications equipment. Intended as, but not constrained to,
              MIL-STD-6016 J6.1 Communications Equipment, Isolated Personnel (NO STATEMENT,
              SURVIVAL RADIO, RADIO BEACON, EPLRS, SIGNAL MIRROR, SMOKE FLARE, IR SIGNALLING
              DEVICE, SIGNALLING PANEL, FRIENDLY FORCE TRACKER, GPS BEACON, LL PHONE, TACTICAL
              RADIO LOS, TACTICAL RADIO BLOS).

          identity: The survivor service identity (UNKNOWN MILITARY, UNKNOWN CIVILIAN, FRIEND
              MILITARY, FRIEND CIVIILIAN, NEUTRAL MILITARY, NEUTRAL CIVILIAN, HOSTILE
              MILITARY, HOSTILE CIVILIAN).

          id_weather_report: Unique identifier of a weather report associated with this recovery.

          mil_class: The military classification of the personnel to be recovered. Intended as, but
              not constrained to, MIL-STD-6016 J6.1 Isolated Personnel Classification (NO
              STATEMENT, MILITARY, GOVERNMENT CIVILIAN, GOVERNMENT CONTRACTOR, CIVILIAN,
              MULTIPLE CLASSIFICATIONS).

          nat_alliance: The country of origin or political entity of an isolated person subject to
              rescue or evacuation. If natAlliance is set to 126, then natAlliance1 must be
              non 0. If natAlliance is any number other than 126, then natAlliance1 will be
              set to 0 regardless. Defined in MIL-STD-6016 J6.1 Nationality/Alliance isolated
              person(s).

          nat_alliance1: Extended country of origin or political entity of an isolated person subject to
              rescue or evacuation. Specify an entry here only if natAlliance is 126. Defined
              in MIL-STD-6016 J6.1 Nationality/Alliance isolated person(s), 1.

          num_ambulatory: Number of ambulatory personnel requiring recovery.

          num_ambulatory_injured: Number of injured, but ambulatory, personnel requiring recovery.

          num_non_ambulatory: Number of littered personnel requiring recovery.

          num_persons: The count of persons requiring recovery.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          pickup_alt: Altitude relative to WGS-84 ellipsoid, in meters. Positive values indicate a
              point height above ellipsoid, and negative values indicate a point eight below
              ellipsoid.

          recov_id: UUID identifying the Personnel Recovery mission, which should remain the same on
              subsequent posts related to the same recovery mission.

          rx_freq: Receive voice frequency in 5Hz increments. This field will auto populate with
              the txFreq value if the post element is null.

          survivor_messages: Preloaded message conveying the situation confronting the isolated person(s).
              Intended as, but not constrained to, MIL-STD-6016 J6.1 Survivor Radio Messages
              (e.g. INJURED CANT MOVE NO KNOWN HOSTILES, INJURED CANT MOVE HOSTILES NEARBY,
              UNINJURED CANT MOVE HOSTILES NEARBY, UNINJURED NO KNOWN HOSTILES, INJURED
              LIMITED MOBILITY).

          survivor_radio: Survivor radio equipment. Intended as, but not constrained to, MIL-STD-6016 J6.1
              Survivor Radio Type (NO STATEMENT, PRQ7SEL, PRC90, PRC112, PRC112B B1, PRC112C,
              PRC112D, PRC148 MBITR, PRC148 JEM, PRC149, PRC152, ACRPLB, OTHER).

          term_ind: Flag indicating the cancellation of this recovery.

          text_msg: Additional specific messages received from survivor.

          tx_freq: Transmit voice frequency in 5Hz increments.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/udl/personnelrecovery",
            body=maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "msg_time": msg_time,
                    "pickup_lat": pickup_lat,
                    "pickup_lon": pickup_lon,
                    "source": source,
                    "type": type,
                    "id": id,
                    "auth_method": auth_method,
                    "auth_status": auth_status,
                    "beacon_ind": beacon_ind,
                    "call_sign": call_sign,
                    "comm_eq1": comm_eq1,
                    "comm_eq2": comm_eq2,
                    "comm_eq3": comm_eq3,
                    "execution_info": execution_info,
                    "identity": identity,
                    "id_weather_report": id_weather_report,
                    "mil_class": mil_class,
                    "nat_alliance": nat_alliance,
                    "nat_alliance1": nat_alliance1,
                    "num_ambulatory": num_ambulatory,
                    "num_ambulatory_injured": num_ambulatory_injured,
                    "num_non_ambulatory": num_non_ambulatory,
                    "num_persons": num_persons,
                    "objective_area_info": objective_area_info,
                    "origin": origin,
                    "pickup_alt": pickup_alt,
                    "recov_id": recov_id,
                    "rx_freq": rx_freq,
                    "survivor_messages": survivor_messages,
                    "survivor_radio": survivor_radio,
                    "term_ind": term_ind,
                    "text_msg": text_msg,
                    "tx_freq": tx_freq,
                },
                personnelrecovery_create_params.PersonnelrecoveryCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        *,
        msg_time: Union[str, datetime],
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncOffsetPage[PersonnelrecoveryListResponse]:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          msg_time: Time stamp of the original personnel recovery message, in ISO 8601 UTC format.
              (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/personnelrecovery",
            page=SyncOffsetPage[PersonnelrecoveryListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "msg_time": msg_time,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    personnelrecovery_list_params.PersonnelrecoveryListParams,
                ),
            ),
            model=PersonnelrecoveryListResponse,
        )

    def count(
        self,
        *,
        msg_time: Union[str, datetime],
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
          msg_time: Time stamp of the original personnel recovery message, in ISO 8601 UTC format.
              (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return self._get(
            "/udl/personnelrecovery/count",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "msg_time": msg_time,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    personnelrecovery_count_params.PersonnelrecoveryCountParams,
                ),
            ),
            cast_to=str,
        )

    def create_bulk(
        self,
        *,
        body: Iterable[personnelrecovery_create_bulk_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation intended for initial integration only, to take a list of
        Personnel Recovery records as a POST body and ingest into the database. Requires
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
            "/udl/personnelrecovery/createBulk",
            body=maybe_transform(body, Iterable[personnelrecovery_create_bulk_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def file_create(
        self,
        *,
        body: Iterable[personnelrecovery_file_create_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a list of Personnel Recovery records as a POST body
        and ingest into the database. Requires a specific role, please contact the UDL
        team to gain access. This operation is intended to be used for automated feeds
        into UDL.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/filedrop/udl-personnelrecovery",
            body=maybe_transform(body, Iterable[personnelrecovery_file_create_params.Body]),
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
    ) -> PersonnelRecoveryFullL:
        """
        Service operation to get a single PersonnelRecovery by its unique ID passed as a
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
            f"/udl/personnelrecovery/{id}",
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
                    personnelrecovery_get_params.PersonnelrecoveryGetParams,
                ),
            ),
            cast_to=PersonnelRecoveryFullL,
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
            "/udl/personnelrecovery/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def tuple(
        self,
        *,
        columns: str,
        msg_time: Union[str, datetime],
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PersonnelrecoveryTupleResponse:
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

          msg_time: Time stamp of the original personnel recovery message, in ISO 8601 UTC format.
              (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/udl/personnelrecovery/tuple",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "columns": columns,
                        "msg_time": msg_time,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    personnelrecovery_tuple_params.PersonnelrecoveryTupleParams,
                ),
            ),
            cast_to=PersonnelrecoveryTupleResponse,
        )


class AsyncPersonnelrecoveryResource(AsyncAPIResource):
    @cached_property
    def history(self) -> AsyncHistoryResource:
        return AsyncHistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPersonnelrecoveryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncPersonnelrecoveryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPersonnelrecoveryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncPersonnelrecoveryResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        msg_time: Union[str, datetime],
        pickup_lat: float,
        pickup_lon: float,
        source: str,
        type: str,
        id: str | NotGiven = NOT_GIVEN,
        auth_method: str | NotGiven = NOT_GIVEN,
        auth_status: str | NotGiven = NOT_GIVEN,
        beacon_ind: bool | NotGiven = NOT_GIVEN,
        call_sign: str | NotGiven = NOT_GIVEN,
        comm_eq1: str | NotGiven = NOT_GIVEN,
        comm_eq2: str | NotGiven = NOT_GIVEN,
        comm_eq3: str | NotGiven = NOT_GIVEN,
        execution_info: personnelrecovery_create_params.ExecutionInfo | NotGiven = NOT_GIVEN,
        identity: str | NotGiven = NOT_GIVEN,
        id_weather_report: str | NotGiven = NOT_GIVEN,
        mil_class: str | NotGiven = NOT_GIVEN,
        nat_alliance: int | NotGiven = NOT_GIVEN,
        nat_alliance1: int | NotGiven = NOT_GIVEN,
        num_ambulatory: int | NotGiven = NOT_GIVEN,
        num_ambulatory_injured: int | NotGiven = NOT_GIVEN,
        num_non_ambulatory: int | NotGiven = NOT_GIVEN,
        num_persons: int | NotGiven = NOT_GIVEN,
        objective_area_info: personnelrecovery_create_params.ObjectiveAreaInfo | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        pickup_alt: float | NotGiven = NOT_GIVEN,
        recov_id: str | NotGiven = NOT_GIVEN,
        rx_freq: float | NotGiven = NOT_GIVEN,
        survivor_messages: str | NotGiven = NOT_GIVEN,
        survivor_radio: str | NotGiven = NOT_GIVEN,
        term_ind: bool | NotGiven = NOT_GIVEN,
        text_msg: str | NotGiven = NOT_GIVEN,
        tx_freq: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single Personnel Recovery object as a POST body and
        ingest into the database. Requires a specific role, please contact the UDL team
        to gain access.

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

          msg_time: Time stamp of the original personnel recovery message, in ISO 8601 UTC format.

          pickup_lat: WGS-84 latitude of the pickup location, in degrees. -90 to 90 degrees (negative
              values south of equator).

          pickup_lon: WGS-84 longitude of the pickup location, in degrees. -180 to 180 degrees
              (negative values west of Prime Meridian).

          source: Source of the data.

          type: Specifies the type of incident resulting in a recovery or evacuation mission.
              Intended as, but not constrained to, MIL-STD-6016 J6.1 Emergency Type (e.g. NO
              STATEMENT, DOWN AIRCRAFT, MAN IN WATER, DITCHING, BAILOUT, DISTRESSED VEHICLE,
              GROUND INCIDENT, MEDICAL, ISOLATED PERSONS, etc.).

          id: Unique identifier of the record, auto-generated by the system.

          auth_method: Mechanism used to verify the survivors identity.

          auth_status: The confirmation status of the isolated personnel identity. Intended as, but not
              constrained to, MIL-STD-6016 J6.1 Authentication Status, Isolated Personnel (NO
              STATEMENT, AUTHENTICATED, NOT AUTHENTICATED, AUTHENTICATED UNDER DURESS, NOT
              APPLICABLE):

              AUTHENTICATED: Confirmed Friend

              NOT AUTHENTICATED: Unconfirmed status

              AUTHENTICATED UNDER DURESS: Authentication comprised by hostiles.

              NOT APPLICABLE: Authentication not required.

          beacon_ind: Flag indicating whether a radio identifier is reported.

          call_sign: The call sign of the personnel to be recovered.

          comm_eq1: Survivor communications equipment. Intended as, but not constrained to,
              MIL-STD-6016 J6.1 Communications Equipment, Isolated Personnel (NO STATEMENT,
              SURVIVAL RADIO, RADIO BEACON, EPLRS, SIGNAL MIRROR, SMOKE FLARE, IR SIGNALLING
              DEVICE, SIGNALLING PANEL, FRIENDLY FORCE TRACKER, GPS BEACON, LL PHONE, TACTICAL
              RADIO LOS, TACTICAL RADIO BLOS).

          comm_eq2: Survivor communications equipment. Intended as, but not constrained to,
              MIL-STD-6016 J6.1 Communications Equipment, Isolated Personnel (NO STATEMENT,
              SURVIVAL RADIO, RADIO BEACON, EPLRS, SIGNAL MIRROR, SMOKE FLARE, IR SIGNALLING
              DEVICE, SIGNALLING PANEL, FRIENDLY FORCE TRACKER, GPS BEACON, LL PHONE, TACTICAL
              RADIO LOS, TACTICAL RADIO BLOS).

          comm_eq3: Survivor communications equipment. Intended as, but not constrained to,
              MIL-STD-6016 J6.1 Communications Equipment, Isolated Personnel (NO STATEMENT,
              SURVIVAL RADIO, RADIO BEACON, EPLRS, SIGNAL MIRROR, SMOKE FLARE, IR SIGNALLING
              DEVICE, SIGNALLING PANEL, FRIENDLY FORCE TRACKER, GPS BEACON, LL PHONE, TACTICAL
              RADIO LOS, TACTICAL RADIO BLOS).

          identity: The survivor service identity (UNKNOWN MILITARY, UNKNOWN CIVILIAN, FRIEND
              MILITARY, FRIEND CIVIILIAN, NEUTRAL MILITARY, NEUTRAL CIVILIAN, HOSTILE
              MILITARY, HOSTILE CIVILIAN).

          id_weather_report: Unique identifier of a weather report associated with this recovery.

          mil_class: The military classification of the personnel to be recovered. Intended as, but
              not constrained to, MIL-STD-6016 J6.1 Isolated Personnel Classification (NO
              STATEMENT, MILITARY, GOVERNMENT CIVILIAN, GOVERNMENT CONTRACTOR, CIVILIAN,
              MULTIPLE CLASSIFICATIONS).

          nat_alliance: The country of origin or political entity of an isolated person subject to
              rescue or evacuation. If natAlliance is set to 126, then natAlliance1 must be
              non 0. If natAlliance is any number other than 126, then natAlliance1 will be
              set to 0 regardless. Defined in MIL-STD-6016 J6.1 Nationality/Alliance isolated
              person(s).

          nat_alliance1: Extended country of origin or political entity of an isolated person subject to
              rescue or evacuation. Specify an entry here only if natAlliance is 126. Defined
              in MIL-STD-6016 J6.1 Nationality/Alliance isolated person(s), 1.

          num_ambulatory: Number of ambulatory personnel requiring recovery.

          num_ambulatory_injured: Number of injured, but ambulatory, personnel requiring recovery.

          num_non_ambulatory: Number of littered personnel requiring recovery.

          num_persons: The count of persons requiring recovery.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          pickup_alt: Altitude relative to WGS-84 ellipsoid, in meters. Positive values indicate a
              point height above ellipsoid, and negative values indicate a point eight below
              ellipsoid.

          recov_id: UUID identifying the Personnel Recovery mission, which should remain the same on
              subsequent posts related to the same recovery mission.

          rx_freq: Receive voice frequency in 5Hz increments. This field will auto populate with
              the txFreq value if the post element is null.

          survivor_messages: Preloaded message conveying the situation confronting the isolated person(s).
              Intended as, but not constrained to, MIL-STD-6016 J6.1 Survivor Radio Messages
              (e.g. INJURED CANT MOVE NO KNOWN HOSTILES, INJURED CANT MOVE HOSTILES NEARBY,
              UNINJURED CANT MOVE HOSTILES NEARBY, UNINJURED NO KNOWN HOSTILES, INJURED
              LIMITED MOBILITY).

          survivor_radio: Survivor radio equipment. Intended as, but not constrained to, MIL-STD-6016 J6.1
              Survivor Radio Type (NO STATEMENT, PRQ7SEL, PRC90, PRC112, PRC112B B1, PRC112C,
              PRC112D, PRC148 MBITR, PRC148 JEM, PRC149, PRC152, ACRPLB, OTHER).

          term_ind: Flag indicating the cancellation of this recovery.

          text_msg: Additional specific messages received from survivor.

          tx_freq: Transmit voice frequency in 5Hz increments.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/udl/personnelrecovery",
            body=await async_maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "msg_time": msg_time,
                    "pickup_lat": pickup_lat,
                    "pickup_lon": pickup_lon,
                    "source": source,
                    "type": type,
                    "id": id,
                    "auth_method": auth_method,
                    "auth_status": auth_status,
                    "beacon_ind": beacon_ind,
                    "call_sign": call_sign,
                    "comm_eq1": comm_eq1,
                    "comm_eq2": comm_eq2,
                    "comm_eq3": comm_eq3,
                    "execution_info": execution_info,
                    "identity": identity,
                    "id_weather_report": id_weather_report,
                    "mil_class": mil_class,
                    "nat_alliance": nat_alliance,
                    "nat_alliance1": nat_alliance1,
                    "num_ambulatory": num_ambulatory,
                    "num_ambulatory_injured": num_ambulatory_injured,
                    "num_non_ambulatory": num_non_ambulatory,
                    "num_persons": num_persons,
                    "objective_area_info": objective_area_info,
                    "origin": origin,
                    "pickup_alt": pickup_alt,
                    "recov_id": recov_id,
                    "rx_freq": rx_freq,
                    "survivor_messages": survivor_messages,
                    "survivor_radio": survivor_radio,
                    "term_ind": term_ind,
                    "text_msg": text_msg,
                    "tx_freq": tx_freq,
                },
                personnelrecovery_create_params.PersonnelrecoveryCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        *,
        msg_time: Union[str, datetime],
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[PersonnelrecoveryListResponse, AsyncOffsetPage[PersonnelrecoveryListResponse]]:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          msg_time: Time stamp of the original personnel recovery message, in ISO 8601 UTC format.
              (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/personnelrecovery",
            page=AsyncOffsetPage[PersonnelrecoveryListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "msg_time": msg_time,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    personnelrecovery_list_params.PersonnelrecoveryListParams,
                ),
            ),
            model=PersonnelrecoveryListResponse,
        )

    async def count(
        self,
        *,
        msg_time: Union[str, datetime],
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
          msg_time: Time stamp of the original personnel recovery message, in ISO 8601 UTC format.
              (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return await self._get(
            "/udl/personnelrecovery/count",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "msg_time": msg_time,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    personnelrecovery_count_params.PersonnelrecoveryCountParams,
                ),
            ),
            cast_to=str,
        )

    async def create_bulk(
        self,
        *,
        body: Iterable[personnelrecovery_create_bulk_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation intended for initial integration only, to take a list of
        Personnel Recovery records as a POST body and ingest into the database. Requires
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
            "/udl/personnelrecovery/createBulk",
            body=await async_maybe_transform(body, Iterable[personnelrecovery_create_bulk_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def file_create(
        self,
        *,
        body: Iterable[personnelrecovery_file_create_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a list of Personnel Recovery records as a POST body
        and ingest into the database. Requires a specific role, please contact the UDL
        team to gain access. This operation is intended to be used for automated feeds
        into UDL.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/filedrop/udl-personnelrecovery",
            body=await async_maybe_transform(body, Iterable[personnelrecovery_file_create_params.Body]),
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
    ) -> PersonnelRecoveryFullL:
        """
        Service operation to get a single PersonnelRecovery by its unique ID passed as a
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
            f"/udl/personnelrecovery/{id}",
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
                    personnelrecovery_get_params.PersonnelrecoveryGetParams,
                ),
            ),
            cast_to=PersonnelRecoveryFullL,
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
            "/udl/personnelrecovery/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def tuple(
        self,
        *,
        columns: str,
        msg_time: Union[str, datetime],
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PersonnelrecoveryTupleResponse:
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

          msg_time: Time stamp of the original personnel recovery message, in ISO 8601 UTC format.
              (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/udl/personnelrecovery/tuple",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "columns": columns,
                        "msg_time": msg_time,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    personnelrecovery_tuple_params.PersonnelrecoveryTupleParams,
                ),
            ),
            cast_to=PersonnelrecoveryTupleResponse,
        )


class PersonnelrecoveryResourceWithRawResponse:
    def __init__(self, personnelrecovery: PersonnelrecoveryResource) -> None:
        self._personnelrecovery = personnelrecovery

        self.create = to_raw_response_wrapper(
            personnelrecovery.create,
        )
        self.list = to_raw_response_wrapper(
            personnelrecovery.list,
        )
        self.count = to_raw_response_wrapper(
            personnelrecovery.count,
        )
        self.create_bulk = to_raw_response_wrapper(
            personnelrecovery.create_bulk,
        )
        self.file_create = to_raw_response_wrapper(
            personnelrecovery.file_create,
        )
        self.get = to_raw_response_wrapper(
            personnelrecovery.get,
        )
        self.queryhelp = to_raw_response_wrapper(
            personnelrecovery.queryhelp,
        )
        self.tuple = to_raw_response_wrapper(
            personnelrecovery.tuple,
        )

    @cached_property
    def history(self) -> HistoryResourceWithRawResponse:
        return HistoryResourceWithRawResponse(self._personnelrecovery.history)


class AsyncPersonnelrecoveryResourceWithRawResponse:
    def __init__(self, personnelrecovery: AsyncPersonnelrecoveryResource) -> None:
        self._personnelrecovery = personnelrecovery

        self.create = async_to_raw_response_wrapper(
            personnelrecovery.create,
        )
        self.list = async_to_raw_response_wrapper(
            personnelrecovery.list,
        )
        self.count = async_to_raw_response_wrapper(
            personnelrecovery.count,
        )
        self.create_bulk = async_to_raw_response_wrapper(
            personnelrecovery.create_bulk,
        )
        self.file_create = async_to_raw_response_wrapper(
            personnelrecovery.file_create,
        )
        self.get = async_to_raw_response_wrapper(
            personnelrecovery.get,
        )
        self.queryhelp = async_to_raw_response_wrapper(
            personnelrecovery.queryhelp,
        )
        self.tuple = async_to_raw_response_wrapper(
            personnelrecovery.tuple,
        )

    @cached_property
    def history(self) -> AsyncHistoryResourceWithRawResponse:
        return AsyncHistoryResourceWithRawResponse(self._personnelrecovery.history)


class PersonnelrecoveryResourceWithStreamingResponse:
    def __init__(self, personnelrecovery: PersonnelrecoveryResource) -> None:
        self._personnelrecovery = personnelrecovery

        self.create = to_streamed_response_wrapper(
            personnelrecovery.create,
        )
        self.list = to_streamed_response_wrapper(
            personnelrecovery.list,
        )
        self.count = to_streamed_response_wrapper(
            personnelrecovery.count,
        )
        self.create_bulk = to_streamed_response_wrapper(
            personnelrecovery.create_bulk,
        )
        self.file_create = to_streamed_response_wrapper(
            personnelrecovery.file_create,
        )
        self.get = to_streamed_response_wrapper(
            personnelrecovery.get,
        )
        self.queryhelp = to_streamed_response_wrapper(
            personnelrecovery.queryhelp,
        )
        self.tuple = to_streamed_response_wrapper(
            personnelrecovery.tuple,
        )

    @cached_property
    def history(self) -> HistoryResourceWithStreamingResponse:
        return HistoryResourceWithStreamingResponse(self._personnelrecovery.history)


class AsyncPersonnelrecoveryResourceWithStreamingResponse:
    def __init__(self, personnelrecovery: AsyncPersonnelrecoveryResource) -> None:
        self._personnelrecovery = personnelrecovery

        self.create = async_to_streamed_response_wrapper(
            personnelrecovery.create,
        )
        self.list = async_to_streamed_response_wrapper(
            personnelrecovery.list,
        )
        self.count = async_to_streamed_response_wrapper(
            personnelrecovery.count,
        )
        self.create_bulk = async_to_streamed_response_wrapper(
            personnelrecovery.create_bulk,
        )
        self.file_create = async_to_streamed_response_wrapper(
            personnelrecovery.file_create,
        )
        self.get = async_to_streamed_response_wrapper(
            personnelrecovery.get,
        )
        self.queryhelp = async_to_streamed_response_wrapper(
            personnelrecovery.queryhelp,
        )
        self.tuple = async_to_streamed_response_wrapper(
            personnelrecovery.tuple,
        )

    @cached_property
    def history(self) -> AsyncHistoryResourceWithStreamingResponse:
        return AsyncHistoryResourceWithStreamingResponse(self._personnelrecovery.history)
