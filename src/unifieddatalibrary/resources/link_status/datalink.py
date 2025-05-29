# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from datetime import datetime
from typing_extensions import Literal

import httpx

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
from ...types.link_status import (
    datalink_list_params,
    datalink_count_params,
    datalink_tuple_params,
    datalink_create_params,
)
from ...types.link_status.datalink_ingest_param import DatalinkIngestParam
from ...types.link_status.datalink_list_response import DatalinkListResponse
from ...types.link_status.datalink_tuple_response import DatalinkTupleResponse
from ...types.link_status.datalink_queryhelp_response import DatalinkQueryhelpResponse

__all__ = ["DatalinkResource", "AsyncDatalinkResource"]


class DatalinkResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DatalinkResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return DatalinkResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DatalinkResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return DatalinkResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        op_ex_name: str,
        originator: str,
        source: str,
        start_time: Union[str, datetime],
        id: str | NotGiven = NOT_GIVEN,
        ack_inst_units: List[str] | NotGiven = NOT_GIVEN,
        ack_req: bool | NotGiven = NOT_GIVEN,
        alt_diff: int | NotGiven = NOT_GIVEN,
        canx_id: str | NotGiven = NOT_GIVEN,
        canx_originator: str | NotGiven = NOT_GIVEN,
        canx_serial_num: str | NotGiven = NOT_GIVEN,
        canx_si_cs: List[str] | NotGiven = NOT_GIVEN,
        canx_special_notation: str | NotGiven = NOT_GIVEN,
        canx_ts: Union[str, datetime] | NotGiven = NOT_GIVEN,
        class_reasons: List[str] | NotGiven = NOT_GIVEN,
        class_source: str | NotGiven = NOT_GIVEN,
        consec_decorr: int | NotGiven = NOT_GIVEN,
        course_diff: int | NotGiven = NOT_GIVEN,
        dec_exempt_codes: List[str] | NotGiven = NOT_GIVEN,
        dec_inst_dates: List[str] | NotGiven = NOT_GIVEN,
        decorr_win_mult: float | NotGiven = NOT_GIVEN,
        geo_datum: str | NotGiven = NOT_GIVEN,
        jre_call_sign: str | NotGiven = NOT_GIVEN,
        jre_details: str | NotGiven = NOT_GIVEN,
        jre_pri_add: int | NotGiven = NOT_GIVEN,
        jre_sec_add: int | NotGiven = NOT_GIVEN,
        jre_unit_des: str | NotGiven = NOT_GIVEN,
        max_geo_pos_qual: int | NotGiven = NOT_GIVEN,
        max_track_qual: int | NotGiven = NOT_GIVEN,
        mgmt_code: str | NotGiven = NOT_GIVEN,
        mgmt_code_meaning: str | NotGiven = NOT_GIVEN,
        min_geo_pos_qual: int | NotGiven = NOT_GIVEN,
        min_track_qual: int | NotGiven = NOT_GIVEN,
        month: str | NotGiven = NOT_GIVEN,
        multi_duty: Iterable[datalink_create_params.MultiDuty] | NotGiven = NOT_GIVEN,
        non_link_unit_des: List[str] | NotGiven = NOT_GIVEN,
        op_ex_info: str | NotGiven = NOT_GIVEN,
        op_ex_info_alt: str | NotGiven = NOT_GIVEN,
        ops: Iterable[datalink_create_params.Op] | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        plan_orig_num: str | NotGiven = NOT_GIVEN,
        poc_call_sign: str | NotGiven = NOT_GIVEN,
        poc_lat: float | NotGiven = NOT_GIVEN,
        poc_loc_name: str | NotGiven = NOT_GIVEN,
        poc_lon: float | NotGiven = NOT_GIVEN,
        poc_name: str | NotGiven = NOT_GIVEN,
        poc_nums: List[str] | NotGiven = NOT_GIVEN,
        poc_rank: str | NotGiven = NOT_GIVEN,
        qualifier: str | NotGiven = NOT_GIVEN,
        qual_sn: int | NotGiven = NOT_GIVEN,
        references: Iterable[datalink_create_params.Reference] | NotGiven = NOT_GIVEN,
        ref_points: Iterable[datalink_create_params.RefPoint] | NotGiven = NOT_GIVEN,
        remarks: Iterable[datalink_create_params.Remark] | NotGiven = NOT_GIVEN,
        res_track_qual: int | NotGiven = NOT_GIVEN,
        serial_num: str | NotGiven = NOT_GIVEN,
        spec_tracks: Iterable[datalink_create_params.SpecTrack] | NotGiven = NOT_GIVEN,
        speed_diff: int | NotGiven = NOT_GIVEN,
        stop_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        stop_time_mod: str | NotGiven = NOT_GIVEN,
        sys_default_code: str | NotGiven = NOT_GIVEN,
        track_num_block_l_ls: Iterable[int] | NotGiven = NOT_GIVEN,
        track_num_blocks: List[str] | NotGiven = NOT_GIVEN,
        voice_coord: Iterable[datalink_create_params.VoiceCoord] | NotGiven = NOT_GIVEN,
        win_size_min: float | NotGiven = NOT_GIVEN,
        win_size_mult: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single DataLink record as a POST body and ingest
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

          op_ex_name: Specifies the unique operation or exercise name, nickname, or codeword assigned
              to a joint exercise or operation plan.

          originator: The identifier of the originator of this message.

          source: Source of the data.

          start_time: The start of the effective time period of this data link message, in ISO 8601
              UTC format with millisecond precision.

          id: Unique identifier of the record, auto-generated by the system if not provided on
              create operations.

          ack_inst_units: Array of instructions for acknowledging and the force or units required to
              acknowledge the data link message being sent.

          ack_req: Flag Indicating if formal acknowledgement is required for the particular data
              link message being sent.

          alt_diff: Maximum altitude difference between two air tracks, in thousands of feet.
              Required if sysDefaultCode field is "MAN". Allowable entires are 5 to 50 in
              increments of 5000 feet.

          canx_id: The identifier for this data link message cancellation.

          canx_originator: The originator of this data link message cancellation.

          canx_serial_num: Serial number assigned to this data link message cancellation.

          canx_si_cs: Array of NATO Subject Indicator Codes (SIC) or filing numbers of this data link
              message or document being cancelled.

          canx_special_notation: Indicates any special actions, restrictions, guidance, or information relating
              to this data link message cancellation.

          canx_ts: Timestamp of the data link message cancellation, in ISO 8601 UTC format with
              millisecond precision.

          class_reasons: Array of codes that indicate the reasons material is classified.

          class_source: Markings that define the source material or the original classification
              authority for this data link message.

          consec_decorr: Number of consecutive remote track reports that must meet the decorrelation
              criteria before the decorrelation is executed. Required if sysDefaultCode field
              is "MAN". Allowable entries are integers from 1 to 5.

          course_diff: Maximum difference between the reported course of the remote track and the
              calculated course of the local track. Required if sysDefaultCode field is "MAN".
              Allowable entries are 15 to 90 in increments of 15 degrees.

          dec_exempt_codes: Array of codes that provide justification for exemption from automatic
              downgrading or declassification.

          dec_inst_dates: Array of markings that provide the literal guidance or dates for the downgrading
              or declassification of this data link message.

          decorr_win_mult: Distance between the common and remote track is to exceed the applicable
              correlation window for the two tracks in order to be decorrelated. Required if
              sysDefaultCode field is "MAN". Allowable entries are 1.0 to 2.0 in increments of
              0.1.

          geo_datum: The code for the point of reference from which the coordinates and networks are
              computed.

          jre_call_sign: Call sign which identifies one or more communications facilities, commands,
              authorities, or activities for Joint Range Extension (JRE) units.

          jre_details: Joint Range Extension (JRE) unit details.

          jre_pri_add: Link-16 octal track number assigned as the primary JTIDS unit address.

          jre_sec_add: Link-16 octal track number assigned as the secondary JTIDS unit address.

          jre_unit_des: Designator of the unit for Joint Range Extension (JRE).

          max_geo_pos_qual: Number used for maximum geodetic position quality. Required if sysDefaultCode
              field is "MAN". Allowable entires are integers from 1 to 15.

          max_track_qual: Track quality to prevent correlation windows from being unrealistically small.
              Required if sysDefaultCode field is "MAN". Allowable entries are integers from 8
              to 15.

          mgmt_code: Data link management code word.

          mgmt_code_meaning: Data link management code word meaning.

          min_geo_pos_qual: Number used for minimum geodetic position quality. Required if sysDefaultCode
              field is "MAN". Allowable entries are integers from 1 to 5.

          min_track_qual: Track quality to prevent correlation windows from being unrealistically large.
              Required if sysDefaultCode field is "MAN". Allowable entries are integers from 3
              to 7.

          month: The month in which this message originated.

          multi_duty: Collection of contact and identification information for designated multilink
              coordinator duty assignments. There can be 0 to many DataLinkMultiDuty
              collections within the datalink service.

          non_link_unit_des: Array of non-link specific data unit designators.

          op_ex_info: Provides an additional caveat further identifying the exercise or modifies the
              exercise nickname.

          op_ex_info_alt: The secondary nickname of the option or the alternative of the operational plan
              or order.

          ops: Collection of information describing the establishment and detailed operation of
              tactical data links. There can be 0 to many DataLinkOps collections within the
              datalink service.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          plan_orig_num: The official identifier of the military establishment responsible for the
              operation plan and the identification number assigned to this plan.

          poc_call_sign: The unit identifier or call sign of the point of contact for this data link
              message.

          poc_lat: WGS84 latitude of the point of contact for this data link message, in degrees.
              -90 to 90 degrees (negative values south of equator).

          poc_loc_name: The location name of the point of contact for this data link message.

          poc_lon: WGS84 longitude of the point of contact for this data link message, in degrees.
              -180 to 180 degrees (negative values west of Prime Meridian).

          poc_name: The name of the point of contact for this data link message.

          poc_nums: Array of telephone numbers, radio frequency values, or email addresses of the
              point of contact for this data link message.

          poc_rank: The rank or position of the point of contact for this data link message in a
              military or civilian organization.

          qualifier: The qualifier which caveats the message status such as AMP (Amplification), CHG
              (Change), etc.

          qual_sn: The serial number associated with the message qualifier.

          references: Collection of reference information. There can be 0 to many DataLinkReferences
              collections within the datalink service.

          ref_points: Collection that identifies points of reference used in the establishment of the
              data links. There can be 1 to many DataLinkRefPoints collections within the
              datalink service.

          remarks: Collection of remarks associated with this data link message.

          res_track_qual: Track quality to enter if too many duals involving low track quality tracks are
              occurring. Required if sysDefaultCode field is "MAN". Allowable entries are
              integers from 2 to 6.

          serial_num: The unique message identifier assigned by the originator.

          spec_tracks: Collection of special track numbers used on the data links. There can be 0 to
              many DataLinkSpecTracks collections within the datalink service.

          speed_diff: Maximum percentage the faster track speed may differ from the slower track
              speed. Required if sysDefaultCode field is "MAN". Allowable entries are 10 to
              100 in increments of 10.

          stop_time: The end of the effective time period of this data link message, in ISO 8601 UTC
              format with millisecond precision. This may be a relative stop time if used with
              stopTimeMod.

          stop_time_mod: A qualifier for the end of the effective time period of this data link message,
              such as AFTER, ASOF, NLT, etc. Used with field stopTime to indicate a relative
              time.

          sys_default_code: Indicates the data terminal settings the system defaults to, either automatic
              correlation/decorrelation (AUTO) or manual (MAN).

          track_num_block_l_ls: Array of Link-16 octal track numbers used as the lower limit of a track block.

          track_num_blocks: Array of defined ranges of Link-11/11B track numbers assigned to a participating
              unit or reporting unit.

          voice_coord: Collection of information regarding the function, frequency, and priority of
              interface control and coordination nets for this data link message. There can be
              1 to many DataLinkVoiceCoord collections within the datalink service.

          win_size_min: Number added to the basic window calculated from track qualities to ensure that
              windows still allow valid correlations. Required if sysDefaultCode field is
              "MAN". Allowable entries are 0.0 to 2.0 in increments of 0.25.

          win_size_mult: The correlation window size multiplier to stretch or reduce the window size.
              Required if sysDefaultCode field is "MAN". Allowable entries are 0.5 to 3.0 in
              increments of 0.1.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/udl/datalink",
            body=maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "op_ex_name": op_ex_name,
                    "originator": originator,
                    "source": source,
                    "start_time": start_time,
                    "id": id,
                    "ack_inst_units": ack_inst_units,
                    "ack_req": ack_req,
                    "alt_diff": alt_diff,
                    "canx_id": canx_id,
                    "canx_originator": canx_originator,
                    "canx_serial_num": canx_serial_num,
                    "canx_si_cs": canx_si_cs,
                    "canx_special_notation": canx_special_notation,
                    "canx_ts": canx_ts,
                    "class_reasons": class_reasons,
                    "class_source": class_source,
                    "consec_decorr": consec_decorr,
                    "course_diff": course_diff,
                    "dec_exempt_codes": dec_exempt_codes,
                    "dec_inst_dates": dec_inst_dates,
                    "decorr_win_mult": decorr_win_mult,
                    "geo_datum": geo_datum,
                    "jre_call_sign": jre_call_sign,
                    "jre_details": jre_details,
                    "jre_pri_add": jre_pri_add,
                    "jre_sec_add": jre_sec_add,
                    "jre_unit_des": jre_unit_des,
                    "max_geo_pos_qual": max_geo_pos_qual,
                    "max_track_qual": max_track_qual,
                    "mgmt_code": mgmt_code,
                    "mgmt_code_meaning": mgmt_code_meaning,
                    "min_geo_pos_qual": min_geo_pos_qual,
                    "min_track_qual": min_track_qual,
                    "month": month,
                    "multi_duty": multi_duty,
                    "non_link_unit_des": non_link_unit_des,
                    "op_ex_info": op_ex_info,
                    "op_ex_info_alt": op_ex_info_alt,
                    "ops": ops,
                    "origin": origin,
                    "plan_orig_num": plan_orig_num,
                    "poc_call_sign": poc_call_sign,
                    "poc_lat": poc_lat,
                    "poc_loc_name": poc_loc_name,
                    "poc_lon": poc_lon,
                    "poc_name": poc_name,
                    "poc_nums": poc_nums,
                    "poc_rank": poc_rank,
                    "qualifier": qualifier,
                    "qual_sn": qual_sn,
                    "references": references,
                    "ref_points": ref_points,
                    "remarks": remarks,
                    "res_track_qual": res_track_qual,
                    "serial_num": serial_num,
                    "spec_tracks": spec_tracks,
                    "speed_diff": speed_diff,
                    "stop_time": stop_time,
                    "stop_time_mod": stop_time_mod,
                    "sys_default_code": sys_default_code,
                    "track_num_block_l_ls": track_num_block_l_ls,
                    "track_num_blocks": track_num_blocks,
                    "voice_coord": voice_coord,
                    "win_size_min": win_size_min,
                    "win_size_mult": win_size_mult,
                },
                datalink_create_params.DatalinkCreateParams,
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
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncOffsetPage[DatalinkListResponse]:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          start_time: The start of the effective time period of this data link message, in ISO 8601
              UTC format with millisecond precision. (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/datalink",
            page=SyncOffsetPage[DatalinkListResponse],
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
                    datalink_list_params.DatalinkListParams,
                ),
            ),
            model=DatalinkListResponse,
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
          start_time: The start of the effective time period of this data link message, in ISO 8601
              UTC format with millisecond precision. (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return self._get(
            "/udl/datalink/count",
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
                    datalink_count_params.DatalinkCountParams,
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
    ) -> DatalinkQueryhelpResponse:
        """
        Service operation to provide detailed information on available dynamic query
        parameters for a particular data type.
        """
        return self._get(
            "/udl/datalink/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DatalinkQueryhelpResponse,
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
    ) -> DatalinkTupleResponse:
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

          start_time: The start of the effective time period of this data link message, in ISO 8601
              UTC format with millisecond precision. (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/udl/datalink/tuple",
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
                    datalink_tuple_params.DatalinkTupleParams,
                ),
            ),
            cast_to=DatalinkTupleResponse,
        )

    def unvalidated_publish(
        self,
        *,
        body: Iterable[DatalinkIngestParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take multiple datalink records as a POST body and ingest
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
            "/filedrop/udl-datalink",
            body=maybe_transform(body, Iterable[DatalinkIngestParam]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncDatalinkResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDatalinkResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncDatalinkResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDatalinkResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncDatalinkResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        op_ex_name: str,
        originator: str,
        source: str,
        start_time: Union[str, datetime],
        id: str | NotGiven = NOT_GIVEN,
        ack_inst_units: List[str] | NotGiven = NOT_GIVEN,
        ack_req: bool | NotGiven = NOT_GIVEN,
        alt_diff: int | NotGiven = NOT_GIVEN,
        canx_id: str | NotGiven = NOT_GIVEN,
        canx_originator: str | NotGiven = NOT_GIVEN,
        canx_serial_num: str | NotGiven = NOT_GIVEN,
        canx_si_cs: List[str] | NotGiven = NOT_GIVEN,
        canx_special_notation: str | NotGiven = NOT_GIVEN,
        canx_ts: Union[str, datetime] | NotGiven = NOT_GIVEN,
        class_reasons: List[str] | NotGiven = NOT_GIVEN,
        class_source: str | NotGiven = NOT_GIVEN,
        consec_decorr: int | NotGiven = NOT_GIVEN,
        course_diff: int | NotGiven = NOT_GIVEN,
        dec_exempt_codes: List[str] | NotGiven = NOT_GIVEN,
        dec_inst_dates: List[str] | NotGiven = NOT_GIVEN,
        decorr_win_mult: float | NotGiven = NOT_GIVEN,
        geo_datum: str | NotGiven = NOT_GIVEN,
        jre_call_sign: str | NotGiven = NOT_GIVEN,
        jre_details: str | NotGiven = NOT_GIVEN,
        jre_pri_add: int | NotGiven = NOT_GIVEN,
        jre_sec_add: int | NotGiven = NOT_GIVEN,
        jre_unit_des: str | NotGiven = NOT_GIVEN,
        max_geo_pos_qual: int | NotGiven = NOT_GIVEN,
        max_track_qual: int | NotGiven = NOT_GIVEN,
        mgmt_code: str | NotGiven = NOT_GIVEN,
        mgmt_code_meaning: str | NotGiven = NOT_GIVEN,
        min_geo_pos_qual: int | NotGiven = NOT_GIVEN,
        min_track_qual: int | NotGiven = NOT_GIVEN,
        month: str | NotGiven = NOT_GIVEN,
        multi_duty: Iterable[datalink_create_params.MultiDuty] | NotGiven = NOT_GIVEN,
        non_link_unit_des: List[str] | NotGiven = NOT_GIVEN,
        op_ex_info: str | NotGiven = NOT_GIVEN,
        op_ex_info_alt: str | NotGiven = NOT_GIVEN,
        ops: Iterable[datalink_create_params.Op] | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        plan_orig_num: str | NotGiven = NOT_GIVEN,
        poc_call_sign: str | NotGiven = NOT_GIVEN,
        poc_lat: float | NotGiven = NOT_GIVEN,
        poc_loc_name: str | NotGiven = NOT_GIVEN,
        poc_lon: float | NotGiven = NOT_GIVEN,
        poc_name: str | NotGiven = NOT_GIVEN,
        poc_nums: List[str] | NotGiven = NOT_GIVEN,
        poc_rank: str | NotGiven = NOT_GIVEN,
        qualifier: str | NotGiven = NOT_GIVEN,
        qual_sn: int | NotGiven = NOT_GIVEN,
        references: Iterable[datalink_create_params.Reference] | NotGiven = NOT_GIVEN,
        ref_points: Iterable[datalink_create_params.RefPoint] | NotGiven = NOT_GIVEN,
        remarks: Iterable[datalink_create_params.Remark] | NotGiven = NOT_GIVEN,
        res_track_qual: int | NotGiven = NOT_GIVEN,
        serial_num: str | NotGiven = NOT_GIVEN,
        spec_tracks: Iterable[datalink_create_params.SpecTrack] | NotGiven = NOT_GIVEN,
        speed_diff: int | NotGiven = NOT_GIVEN,
        stop_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        stop_time_mod: str | NotGiven = NOT_GIVEN,
        sys_default_code: str | NotGiven = NOT_GIVEN,
        track_num_block_l_ls: Iterable[int] | NotGiven = NOT_GIVEN,
        track_num_blocks: List[str] | NotGiven = NOT_GIVEN,
        voice_coord: Iterable[datalink_create_params.VoiceCoord] | NotGiven = NOT_GIVEN,
        win_size_min: float | NotGiven = NOT_GIVEN,
        win_size_mult: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single DataLink record as a POST body and ingest
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

          op_ex_name: Specifies the unique operation or exercise name, nickname, or codeword assigned
              to a joint exercise or operation plan.

          originator: The identifier of the originator of this message.

          source: Source of the data.

          start_time: The start of the effective time period of this data link message, in ISO 8601
              UTC format with millisecond precision.

          id: Unique identifier of the record, auto-generated by the system if not provided on
              create operations.

          ack_inst_units: Array of instructions for acknowledging and the force or units required to
              acknowledge the data link message being sent.

          ack_req: Flag Indicating if formal acknowledgement is required for the particular data
              link message being sent.

          alt_diff: Maximum altitude difference between two air tracks, in thousands of feet.
              Required if sysDefaultCode field is "MAN". Allowable entires are 5 to 50 in
              increments of 5000 feet.

          canx_id: The identifier for this data link message cancellation.

          canx_originator: The originator of this data link message cancellation.

          canx_serial_num: Serial number assigned to this data link message cancellation.

          canx_si_cs: Array of NATO Subject Indicator Codes (SIC) or filing numbers of this data link
              message or document being cancelled.

          canx_special_notation: Indicates any special actions, restrictions, guidance, or information relating
              to this data link message cancellation.

          canx_ts: Timestamp of the data link message cancellation, in ISO 8601 UTC format with
              millisecond precision.

          class_reasons: Array of codes that indicate the reasons material is classified.

          class_source: Markings that define the source material or the original classification
              authority for this data link message.

          consec_decorr: Number of consecutive remote track reports that must meet the decorrelation
              criteria before the decorrelation is executed. Required if sysDefaultCode field
              is "MAN". Allowable entries are integers from 1 to 5.

          course_diff: Maximum difference between the reported course of the remote track and the
              calculated course of the local track. Required if sysDefaultCode field is "MAN".
              Allowable entries are 15 to 90 in increments of 15 degrees.

          dec_exempt_codes: Array of codes that provide justification for exemption from automatic
              downgrading or declassification.

          dec_inst_dates: Array of markings that provide the literal guidance or dates for the downgrading
              or declassification of this data link message.

          decorr_win_mult: Distance between the common and remote track is to exceed the applicable
              correlation window for the two tracks in order to be decorrelated. Required if
              sysDefaultCode field is "MAN". Allowable entries are 1.0 to 2.0 in increments of
              0.1.

          geo_datum: The code for the point of reference from which the coordinates and networks are
              computed.

          jre_call_sign: Call sign which identifies one or more communications facilities, commands,
              authorities, or activities for Joint Range Extension (JRE) units.

          jre_details: Joint Range Extension (JRE) unit details.

          jre_pri_add: Link-16 octal track number assigned as the primary JTIDS unit address.

          jre_sec_add: Link-16 octal track number assigned as the secondary JTIDS unit address.

          jre_unit_des: Designator of the unit for Joint Range Extension (JRE).

          max_geo_pos_qual: Number used for maximum geodetic position quality. Required if sysDefaultCode
              field is "MAN". Allowable entires are integers from 1 to 15.

          max_track_qual: Track quality to prevent correlation windows from being unrealistically small.
              Required if sysDefaultCode field is "MAN". Allowable entries are integers from 8
              to 15.

          mgmt_code: Data link management code word.

          mgmt_code_meaning: Data link management code word meaning.

          min_geo_pos_qual: Number used for minimum geodetic position quality. Required if sysDefaultCode
              field is "MAN". Allowable entries are integers from 1 to 5.

          min_track_qual: Track quality to prevent correlation windows from being unrealistically large.
              Required if sysDefaultCode field is "MAN". Allowable entries are integers from 3
              to 7.

          month: The month in which this message originated.

          multi_duty: Collection of contact and identification information for designated multilink
              coordinator duty assignments. There can be 0 to many DataLinkMultiDuty
              collections within the datalink service.

          non_link_unit_des: Array of non-link specific data unit designators.

          op_ex_info: Provides an additional caveat further identifying the exercise or modifies the
              exercise nickname.

          op_ex_info_alt: The secondary nickname of the option or the alternative of the operational plan
              or order.

          ops: Collection of information describing the establishment and detailed operation of
              tactical data links. There can be 0 to many DataLinkOps collections within the
              datalink service.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          plan_orig_num: The official identifier of the military establishment responsible for the
              operation plan and the identification number assigned to this plan.

          poc_call_sign: The unit identifier or call sign of the point of contact for this data link
              message.

          poc_lat: WGS84 latitude of the point of contact for this data link message, in degrees.
              -90 to 90 degrees (negative values south of equator).

          poc_loc_name: The location name of the point of contact for this data link message.

          poc_lon: WGS84 longitude of the point of contact for this data link message, in degrees.
              -180 to 180 degrees (negative values west of Prime Meridian).

          poc_name: The name of the point of contact for this data link message.

          poc_nums: Array of telephone numbers, radio frequency values, or email addresses of the
              point of contact for this data link message.

          poc_rank: The rank or position of the point of contact for this data link message in a
              military or civilian organization.

          qualifier: The qualifier which caveats the message status such as AMP (Amplification), CHG
              (Change), etc.

          qual_sn: The serial number associated with the message qualifier.

          references: Collection of reference information. There can be 0 to many DataLinkReferences
              collections within the datalink service.

          ref_points: Collection that identifies points of reference used in the establishment of the
              data links. There can be 1 to many DataLinkRefPoints collections within the
              datalink service.

          remarks: Collection of remarks associated with this data link message.

          res_track_qual: Track quality to enter if too many duals involving low track quality tracks are
              occurring. Required if sysDefaultCode field is "MAN". Allowable entries are
              integers from 2 to 6.

          serial_num: The unique message identifier assigned by the originator.

          spec_tracks: Collection of special track numbers used on the data links. There can be 0 to
              many DataLinkSpecTracks collections within the datalink service.

          speed_diff: Maximum percentage the faster track speed may differ from the slower track
              speed. Required if sysDefaultCode field is "MAN". Allowable entries are 10 to
              100 in increments of 10.

          stop_time: The end of the effective time period of this data link message, in ISO 8601 UTC
              format with millisecond precision. This may be a relative stop time if used with
              stopTimeMod.

          stop_time_mod: A qualifier for the end of the effective time period of this data link message,
              such as AFTER, ASOF, NLT, etc. Used with field stopTime to indicate a relative
              time.

          sys_default_code: Indicates the data terminal settings the system defaults to, either automatic
              correlation/decorrelation (AUTO) or manual (MAN).

          track_num_block_l_ls: Array of Link-16 octal track numbers used as the lower limit of a track block.

          track_num_blocks: Array of defined ranges of Link-11/11B track numbers assigned to a participating
              unit or reporting unit.

          voice_coord: Collection of information regarding the function, frequency, and priority of
              interface control and coordination nets for this data link message. There can be
              1 to many DataLinkVoiceCoord collections within the datalink service.

          win_size_min: Number added to the basic window calculated from track qualities to ensure that
              windows still allow valid correlations. Required if sysDefaultCode field is
              "MAN". Allowable entries are 0.0 to 2.0 in increments of 0.25.

          win_size_mult: The correlation window size multiplier to stretch or reduce the window size.
              Required if sysDefaultCode field is "MAN". Allowable entries are 0.5 to 3.0 in
              increments of 0.1.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/udl/datalink",
            body=await async_maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "op_ex_name": op_ex_name,
                    "originator": originator,
                    "source": source,
                    "start_time": start_time,
                    "id": id,
                    "ack_inst_units": ack_inst_units,
                    "ack_req": ack_req,
                    "alt_diff": alt_diff,
                    "canx_id": canx_id,
                    "canx_originator": canx_originator,
                    "canx_serial_num": canx_serial_num,
                    "canx_si_cs": canx_si_cs,
                    "canx_special_notation": canx_special_notation,
                    "canx_ts": canx_ts,
                    "class_reasons": class_reasons,
                    "class_source": class_source,
                    "consec_decorr": consec_decorr,
                    "course_diff": course_diff,
                    "dec_exempt_codes": dec_exempt_codes,
                    "dec_inst_dates": dec_inst_dates,
                    "decorr_win_mult": decorr_win_mult,
                    "geo_datum": geo_datum,
                    "jre_call_sign": jre_call_sign,
                    "jre_details": jre_details,
                    "jre_pri_add": jre_pri_add,
                    "jre_sec_add": jre_sec_add,
                    "jre_unit_des": jre_unit_des,
                    "max_geo_pos_qual": max_geo_pos_qual,
                    "max_track_qual": max_track_qual,
                    "mgmt_code": mgmt_code,
                    "mgmt_code_meaning": mgmt_code_meaning,
                    "min_geo_pos_qual": min_geo_pos_qual,
                    "min_track_qual": min_track_qual,
                    "month": month,
                    "multi_duty": multi_duty,
                    "non_link_unit_des": non_link_unit_des,
                    "op_ex_info": op_ex_info,
                    "op_ex_info_alt": op_ex_info_alt,
                    "ops": ops,
                    "origin": origin,
                    "plan_orig_num": plan_orig_num,
                    "poc_call_sign": poc_call_sign,
                    "poc_lat": poc_lat,
                    "poc_loc_name": poc_loc_name,
                    "poc_lon": poc_lon,
                    "poc_name": poc_name,
                    "poc_nums": poc_nums,
                    "poc_rank": poc_rank,
                    "qualifier": qualifier,
                    "qual_sn": qual_sn,
                    "references": references,
                    "ref_points": ref_points,
                    "remarks": remarks,
                    "res_track_qual": res_track_qual,
                    "serial_num": serial_num,
                    "spec_tracks": spec_tracks,
                    "speed_diff": speed_diff,
                    "stop_time": stop_time,
                    "stop_time_mod": stop_time_mod,
                    "sys_default_code": sys_default_code,
                    "track_num_block_l_ls": track_num_block_l_ls,
                    "track_num_blocks": track_num_blocks,
                    "voice_coord": voice_coord,
                    "win_size_min": win_size_min,
                    "win_size_mult": win_size_mult,
                },
                datalink_create_params.DatalinkCreateParams,
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
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[DatalinkListResponse, AsyncOffsetPage[DatalinkListResponse]]:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          start_time: The start of the effective time period of this data link message, in ISO 8601
              UTC format with millisecond precision. (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/datalink",
            page=AsyncOffsetPage[DatalinkListResponse],
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
                    datalink_list_params.DatalinkListParams,
                ),
            ),
            model=DatalinkListResponse,
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
          start_time: The start of the effective time period of this data link message, in ISO 8601
              UTC format with millisecond precision. (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return await self._get(
            "/udl/datalink/count",
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
                    datalink_count_params.DatalinkCountParams,
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
    ) -> DatalinkQueryhelpResponse:
        """
        Service operation to provide detailed information on available dynamic query
        parameters for a particular data type.
        """
        return await self._get(
            "/udl/datalink/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DatalinkQueryhelpResponse,
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
    ) -> DatalinkTupleResponse:
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

          start_time: The start of the effective time period of this data link message, in ISO 8601
              UTC format with millisecond precision. (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/udl/datalink/tuple",
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
                    datalink_tuple_params.DatalinkTupleParams,
                ),
            ),
            cast_to=DatalinkTupleResponse,
        )

    async def unvalidated_publish(
        self,
        *,
        body: Iterable[DatalinkIngestParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take multiple datalink records as a POST body and ingest
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
            "/filedrop/udl-datalink",
            body=await async_maybe_transform(body, Iterable[DatalinkIngestParam]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class DatalinkResourceWithRawResponse:
    def __init__(self, datalink: DatalinkResource) -> None:
        self._datalink = datalink

        self.create = to_raw_response_wrapper(
            datalink.create,
        )
        self.list = to_raw_response_wrapper(
            datalink.list,
        )
        self.count = to_raw_response_wrapper(
            datalink.count,
        )
        self.queryhelp = to_raw_response_wrapper(
            datalink.queryhelp,
        )
        self.tuple = to_raw_response_wrapper(
            datalink.tuple,
        )
        self.unvalidated_publish = to_raw_response_wrapper(
            datalink.unvalidated_publish,
        )


class AsyncDatalinkResourceWithRawResponse:
    def __init__(self, datalink: AsyncDatalinkResource) -> None:
        self._datalink = datalink

        self.create = async_to_raw_response_wrapper(
            datalink.create,
        )
        self.list = async_to_raw_response_wrapper(
            datalink.list,
        )
        self.count = async_to_raw_response_wrapper(
            datalink.count,
        )
        self.queryhelp = async_to_raw_response_wrapper(
            datalink.queryhelp,
        )
        self.tuple = async_to_raw_response_wrapper(
            datalink.tuple,
        )
        self.unvalidated_publish = async_to_raw_response_wrapper(
            datalink.unvalidated_publish,
        )


class DatalinkResourceWithStreamingResponse:
    def __init__(self, datalink: DatalinkResource) -> None:
        self._datalink = datalink

        self.create = to_streamed_response_wrapper(
            datalink.create,
        )
        self.list = to_streamed_response_wrapper(
            datalink.list,
        )
        self.count = to_streamed_response_wrapper(
            datalink.count,
        )
        self.queryhelp = to_streamed_response_wrapper(
            datalink.queryhelp,
        )
        self.tuple = to_streamed_response_wrapper(
            datalink.tuple,
        )
        self.unvalidated_publish = to_streamed_response_wrapper(
            datalink.unvalidated_publish,
        )


class AsyncDatalinkResourceWithStreamingResponse:
    def __init__(self, datalink: AsyncDatalinkResource) -> None:
        self._datalink = datalink

        self.create = async_to_streamed_response_wrapper(
            datalink.create,
        )
        self.list = async_to_streamed_response_wrapper(
            datalink.list,
        )
        self.count = async_to_streamed_response_wrapper(
            datalink.count,
        )
        self.queryhelp = async_to_streamed_response_wrapper(
            datalink.queryhelp,
        )
        self.tuple = async_to_streamed_response_wrapper(
            datalink.tuple,
        )
        self.unvalidated_publish = async_to_streamed_response_wrapper(
            datalink.unvalidated_publish,
        )
