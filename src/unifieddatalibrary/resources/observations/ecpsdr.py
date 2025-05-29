# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
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
from ...types.observations import (
    ecpsdr_list_params,
    ecpsdr_count_params,
    ecpsdr_tuple_params,
    ecpsdr_create_params,
    ecpsdr_retrieve_params,
    ecpsdr_create_bulk_params,
)
from ...types.observations.ecpsdr import Ecpsdr
from ...types.observations.ecpsdr_abridged import EcpsdrAbridged
from ...types.observations.ecpsdr_tuple_response import EcpsdrTupleResponse
from ...types.observations.ecpsdr_query_help_response import EcpsdrQueryHelpResponse

__all__ = ["EcpsdrResource", "AsyncEcpsdrResource"]


class EcpsdrResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EcpsdrResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return EcpsdrResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EcpsdrResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return EcpsdrResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        msg_time: Union[str, datetime],
        source: str,
        type: str,
        id: str | NotGiven = NOT_GIVEN,
        asl5_v_curr_mon: int | NotGiven = NOT_GIVEN,
        cds_plate_v_mon: int | NotGiven = NOT_GIVEN,
        cds_ref_v_mon: int | NotGiven = NOT_GIVEN,
        cds_threshold: int | NotGiven = NOT_GIVEN,
        cds_throttle: int | NotGiven = NOT_GIVEN,
        checksum: int | NotGiven = NOT_GIVEN,
        dos_bias: int | NotGiven = NOT_GIVEN,
        dsl5_v_curr_mon: int | NotGiven = NOT_GIVEN,
        esd_trig_count_h: int | NotGiven = NOT_GIVEN,
        esd_trig_count_l: int | NotGiven = NOT_GIVEN,
        hi_let_l: int | NotGiven = NOT_GIVEN,
        hi_let_m: int | NotGiven = NOT_GIVEN,
        id_sensor: str | NotGiven = NOT_GIVEN,
        low_let_l: int | NotGiven = NOT_GIVEN,
        low_let_m: int | NotGiven = NOT_GIVEN,
        med_let1_l: int | NotGiven = NOT_GIVEN,
        med_let1_m: int | NotGiven = NOT_GIVEN,
        med_let2_l: int | NotGiven = NOT_GIVEN,
        med_let2_m: int | NotGiven = NOT_GIVEN,
        med_let3_l: int | NotGiven = NOT_GIVEN,
        med_let3_m: int | NotGiven = NOT_GIVEN,
        med_let4_l: int | NotGiven = NOT_GIVEN,
        med_let4_m: int | NotGiven = NOT_GIVEN,
        mp_temp: int | NotGiven = NOT_GIVEN,
        ob_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        orig_object_id: str | NotGiven = NOT_GIVEN,
        orig_sensor_id: str | NotGiven = NOT_GIVEN,
        pd1_sig_lev: int | NotGiven = NOT_GIVEN,
        pd2_sig_lev: int | NotGiven = NOT_GIVEN,
        ps_temp_mon: int | NotGiven = NOT_GIVEN,
        retransmit: bool | NotGiven = NOT_GIVEN,
        sat_no: int | NotGiven = NOT_GIVEN,
        sen_mode: str | NotGiven = NOT_GIVEN,
        surf_dos_charge_h: int | NotGiven = NOT_GIVEN,
        surf_dos_charge_l: int | NotGiven = NOT_GIVEN,
        surf_dos_h: int | NotGiven = NOT_GIVEN,
        surf_dos_l: int | NotGiven = NOT_GIVEN,
        surf_dos_m: int | NotGiven = NOT_GIVEN,
        surf_dos_stat: int | NotGiven = NOT_GIVEN,
        transient_data: Iterable[int] | NotGiven = NOT_GIVEN,
        v_ref: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single ECPSDR as a POST body and ingest into the
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

          msg_time: Time stamp of time packet receipt on ground, in ISO 8601 UTC format with
              millisecond precision.

          source: Source of the data.

          type: The type of data associated with this record (STANDARD, TRANSIENT).

          id: Unique identifier of the record, auto-generated by the system.

          asl5_v_curr_mon: Internal 5V current monitor for analog supply line. This is sensor status
              telemetry. See vRef for conversion factor to Volts.

          cds_plate_v_mon: CDS Charge Plate voltage monitor. See vRef for conversion factor to Volts.

          cds_ref_v_mon: CDS reference voltage monitor. See vRef for conversion factor to Volts.

          cds_threshold: CDS Threshold setting for ESD detection threshold. The CDS Threshold is the
              adjustable sensitivity of recording/digitizing an ESD as a transient packet.

          cds_throttle: CDS throttle number of seconds between CDS transient capture readouts.

          checksum: Two byte CRC-16-CCITT checksum (ordered as first byte, second byte).

          dos_bias: Unitless dosimeter detector bias for MedLET and HiLET. MedLET (Linear Energy
              Transfer) and HiLET subsensors detect particles above LET thresholds, 300keV and
              1MeV, respectively.

          dsl5_v_curr_mon: Internal 5V current monitor for digital supply line. This is sensor status
              telemetry. See vRef for conversion factor to Volts.

          esd_trig_count_h: Number of ESD triggers, high byte of 2-byte counter.

          esd_trig_count_l: Number of ESD triggers, low byte of 2-byte counter.

          hi_let_l: HiLET dosimeter low range output. Low byte of scaler (HiLET) dosimeter output.

          hi_let_m: Unitless HiLET dosimeter medium range output. Medium byte of (HiLET) dosimeter
              output.

          id_sensor: Unique identifier of the reporting sensor.

          low_let_l: LowLET dosimeter low range output. Low byte of (LowLET) dosimeter output.

          low_let_m: LowLET dosimeter medium range output. Medium byte of (LowLET) dosimeter output.

          med_let1_l: MedLET1 dosimeter low range output. Low byte of the 1st (MedLET) dosimeter
              output.

          med_let1_m: MedLET1 dosimeter medium range output. Medium byte of the 1st (MedLET) dosimeter
              output.

          med_let2_l: MedLET2 dosimeter low range output. Low byte of the 2nd (MedLET) dosimeter
              output.

          med_let2_m: MedLET2 dosimeter medium range output. Medium byte of the 2nd (MedLET) dosimeter
              output.

          med_let3_l: MedLET3 dosimeter low range output. Low byte of the 3rd (MedLET) dosimeter
              output.

          med_let3_m: MedLET3 dosimeter medium range output. Medium byte of the 3rd (MedLET) dosimeter
              output.

          med_let4_l: MedLET4 dosimeter low range output. Low byte of the 4th (MedLET) dosimeter
              output.

          med_let4_m: MedLET4 dosimeter medium range output. Medium byte of the 4th (MedLET) dosimeter
              output.

          mp_temp: Unitless sensor mounting plate temperature.

          ob_time: Time of the observation, in ISO 8601 UTC format with millisecond precision.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          orig_object_id: Optional identifier provided by the record source to indicate the satellite
              hosting the sensor. This may be an internal identifier and not necessarily map
              to a valid satellite number.

          orig_sensor_id: Optional identifier provided by the record source to indicate the sensor
              identifier which produced this data. This may be an internal identifier and not
              necessarily a valid sensor ID.

          pd1_sig_lev: Photodiode 1 signal level.

          pd2_sig_lev: Photodiode 2 signal level.

          ps_temp_mon: Power supply temperature monitor. This is sensor status telemetry.

          retransmit: Flag indicating whether this record is an original or re-transmitted dataset
              (TRUE indicates a retransmit from the host).

          sat_no: Satellite/catalog number of the on-orbit satellite hosting the sensor.

          sen_mode: The sensor mode associated with this measurements (NORMAL, TEST).

          surf_dos_charge_h: Surface dosimeter charge rate high output (converts to pico-amps/bit). High byte
              of 2 bytes.

          surf_dos_charge_l: Surface dosimeter charge rate low output (converts to pico-amps/bit). Low byte
              of 2 bytes.

          surf_dos_h: Surface dosimeter high range output (converts to pico-coulombs/bit). High byte
              of 3 bytes.

          surf_dos_l: Surface dosimeter low range output (converts to pico-coulombs/bit). Low byte of
              3 bytes.

          surf_dos_m: Surface dosimeter medium range output (converts to pico-coulombs/bit). Middle
              byte of 3 bytes.

          surf_dos_stat: Surface dosimeter status byte.

          transient_data: Array of 144 digitized samples of ESD waveform for transient packets.

          v_ref: Reference voltage (volts/bit). Conversion factor used to convert analog V
              monitor data from bytes to volts.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/udl/ecpsdr",
            body=maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "msg_time": msg_time,
                    "source": source,
                    "type": type,
                    "id": id,
                    "asl5_v_curr_mon": asl5_v_curr_mon,
                    "cds_plate_v_mon": cds_plate_v_mon,
                    "cds_ref_v_mon": cds_ref_v_mon,
                    "cds_threshold": cds_threshold,
                    "cds_throttle": cds_throttle,
                    "checksum": checksum,
                    "dos_bias": dos_bias,
                    "dsl5_v_curr_mon": dsl5_v_curr_mon,
                    "esd_trig_count_h": esd_trig_count_h,
                    "esd_trig_count_l": esd_trig_count_l,
                    "hi_let_l": hi_let_l,
                    "hi_let_m": hi_let_m,
                    "id_sensor": id_sensor,
                    "low_let_l": low_let_l,
                    "low_let_m": low_let_m,
                    "med_let1_l": med_let1_l,
                    "med_let1_m": med_let1_m,
                    "med_let2_l": med_let2_l,
                    "med_let2_m": med_let2_m,
                    "med_let3_l": med_let3_l,
                    "med_let3_m": med_let3_m,
                    "med_let4_l": med_let4_l,
                    "med_let4_m": med_let4_m,
                    "mp_temp": mp_temp,
                    "ob_time": ob_time,
                    "origin": origin,
                    "orig_object_id": orig_object_id,
                    "orig_sensor_id": orig_sensor_id,
                    "pd1_sig_lev": pd1_sig_lev,
                    "pd2_sig_lev": pd2_sig_lev,
                    "ps_temp_mon": ps_temp_mon,
                    "retransmit": retransmit,
                    "sat_no": sat_no,
                    "sen_mode": sen_mode,
                    "surf_dos_charge_h": surf_dos_charge_h,
                    "surf_dos_charge_l": surf_dos_charge_l,
                    "surf_dos_h": surf_dos_h,
                    "surf_dos_l": surf_dos_l,
                    "surf_dos_m": surf_dos_m,
                    "surf_dos_stat": surf_dos_stat,
                    "transient_data": transient_data,
                    "v_ref": v_ref,
                },
                ecpsdr_create_params.EcpsdrCreateParams,
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
    ) -> Ecpsdr:
        """
        Service operation to get a single ECPSDR by its unique ID passed as a path
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
            f"/udl/ecpsdr/{id}",
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
                    ecpsdr_retrieve_params.EcpsdrRetrieveParams,
                ),
            ),
            cast_to=Ecpsdr,
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
    ) -> SyncOffsetPage[EcpsdrAbridged]:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          msg_time: Time stamp of time packet receipt on ground, in ISO 8601 UTC format with
              millisecond precision. (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/ecpsdr",
            page=SyncOffsetPage[EcpsdrAbridged],
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
                    ecpsdr_list_params.EcpsdrListParams,
                ),
            ),
            model=EcpsdrAbridged,
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
          msg_time: Time stamp of time packet receipt on ground, in ISO 8601 UTC format with
              millisecond precision. (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return self._get(
            "/udl/ecpsdr/count",
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
                    ecpsdr_count_params.EcpsdrCountParams,
                ),
            ),
            cast_to=str,
        )

    def create_bulk(
        self,
        *,
        body: Iterable[ecpsdr_create_bulk_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation intended for initial integration only, to take a list of
        ECPSDR as a POST body and ingest into the database. This operation is not
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
            "/udl/ecpsdr/createBulk",
            body=maybe_transform(body, Iterable[ecpsdr_create_bulk_params.Body]),
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
    ) -> EcpsdrQueryHelpResponse:
        """
        Service operation to provide detailed information on available dynamic query
        parameters for a particular data type.
        """
        return self._get(
            "/udl/ecpsdr/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EcpsdrQueryHelpResponse,
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
    ) -> EcpsdrTupleResponse:
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

          msg_time: Time stamp of time packet receipt on ground, in ISO 8601 UTC format with
              millisecond precision. (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/udl/ecpsdr/tuple",
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
                    ecpsdr_tuple_params.EcpsdrTupleParams,
                ),
            ),
            cast_to=EcpsdrTupleResponse,
        )


class AsyncEcpsdrResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEcpsdrResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncEcpsdrResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEcpsdrResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncEcpsdrResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        msg_time: Union[str, datetime],
        source: str,
        type: str,
        id: str | NotGiven = NOT_GIVEN,
        asl5_v_curr_mon: int | NotGiven = NOT_GIVEN,
        cds_plate_v_mon: int | NotGiven = NOT_GIVEN,
        cds_ref_v_mon: int | NotGiven = NOT_GIVEN,
        cds_threshold: int | NotGiven = NOT_GIVEN,
        cds_throttle: int | NotGiven = NOT_GIVEN,
        checksum: int | NotGiven = NOT_GIVEN,
        dos_bias: int | NotGiven = NOT_GIVEN,
        dsl5_v_curr_mon: int | NotGiven = NOT_GIVEN,
        esd_trig_count_h: int | NotGiven = NOT_GIVEN,
        esd_trig_count_l: int | NotGiven = NOT_GIVEN,
        hi_let_l: int | NotGiven = NOT_GIVEN,
        hi_let_m: int | NotGiven = NOT_GIVEN,
        id_sensor: str | NotGiven = NOT_GIVEN,
        low_let_l: int | NotGiven = NOT_GIVEN,
        low_let_m: int | NotGiven = NOT_GIVEN,
        med_let1_l: int | NotGiven = NOT_GIVEN,
        med_let1_m: int | NotGiven = NOT_GIVEN,
        med_let2_l: int | NotGiven = NOT_GIVEN,
        med_let2_m: int | NotGiven = NOT_GIVEN,
        med_let3_l: int | NotGiven = NOT_GIVEN,
        med_let3_m: int | NotGiven = NOT_GIVEN,
        med_let4_l: int | NotGiven = NOT_GIVEN,
        med_let4_m: int | NotGiven = NOT_GIVEN,
        mp_temp: int | NotGiven = NOT_GIVEN,
        ob_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        orig_object_id: str | NotGiven = NOT_GIVEN,
        orig_sensor_id: str | NotGiven = NOT_GIVEN,
        pd1_sig_lev: int | NotGiven = NOT_GIVEN,
        pd2_sig_lev: int | NotGiven = NOT_GIVEN,
        ps_temp_mon: int | NotGiven = NOT_GIVEN,
        retransmit: bool | NotGiven = NOT_GIVEN,
        sat_no: int | NotGiven = NOT_GIVEN,
        sen_mode: str | NotGiven = NOT_GIVEN,
        surf_dos_charge_h: int | NotGiven = NOT_GIVEN,
        surf_dos_charge_l: int | NotGiven = NOT_GIVEN,
        surf_dos_h: int | NotGiven = NOT_GIVEN,
        surf_dos_l: int | NotGiven = NOT_GIVEN,
        surf_dos_m: int | NotGiven = NOT_GIVEN,
        surf_dos_stat: int | NotGiven = NOT_GIVEN,
        transient_data: Iterable[int] | NotGiven = NOT_GIVEN,
        v_ref: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single ECPSDR as a POST body and ingest into the
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

          msg_time: Time stamp of time packet receipt on ground, in ISO 8601 UTC format with
              millisecond precision.

          source: Source of the data.

          type: The type of data associated with this record (STANDARD, TRANSIENT).

          id: Unique identifier of the record, auto-generated by the system.

          asl5_v_curr_mon: Internal 5V current monitor for analog supply line. This is sensor status
              telemetry. See vRef for conversion factor to Volts.

          cds_plate_v_mon: CDS Charge Plate voltage monitor. See vRef for conversion factor to Volts.

          cds_ref_v_mon: CDS reference voltage monitor. See vRef for conversion factor to Volts.

          cds_threshold: CDS Threshold setting for ESD detection threshold. The CDS Threshold is the
              adjustable sensitivity of recording/digitizing an ESD as a transient packet.

          cds_throttle: CDS throttle number of seconds between CDS transient capture readouts.

          checksum: Two byte CRC-16-CCITT checksum (ordered as first byte, second byte).

          dos_bias: Unitless dosimeter detector bias for MedLET and HiLET. MedLET (Linear Energy
              Transfer) and HiLET subsensors detect particles above LET thresholds, 300keV and
              1MeV, respectively.

          dsl5_v_curr_mon: Internal 5V current monitor for digital supply line. This is sensor status
              telemetry. See vRef for conversion factor to Volts.

          esd_trig_count_h: Number of ESD triggers, high byte of 2-byte counter.

          esd_trig_count_l: Number of ESD triggers, low byte of 2-byte counter.

          hi_let_l: HiLET dosimeter low range output. Low byte of scaler (HiLET) dosimeter output.

          hi_let_m: Unitless HiLET dosimeter medium range output. Medium byte of (HiLET) dosimeter
              output.

          id_sensor: Unique identifier of the reporting sensor.

          low_let_l: LowLET dosimeter low range output. Low byte of (LowLET) dosimeter output.

          low_let_m: LowLET dosimeter medium range output. Medium byte of (LowLET) dosimeter output.

          med_let1_l: MedLET1 dosimeter low range output. Low byte of the 1st (MedLET) dosimeter
              output.

          med_let1_m: MedLET1 dosimeter medium range output. Medium byte of the 1st (MedLET) dosimeter
              output.

          med_let2_l: MedLET2 dosimeter low range output. Low byte of the 2nd (MedLET) dosimeter
              output.

          med_let2_m: MedLET2 dosimeter medium range output. Medium byte of the 2nd (MedLET) dosimeter
              output.

          med_let3_l: MedLET3 dosimeter low range output. Low byte of the 3rd (MedLET) dosimeter
              output.

          med_let3_m: MedLET3 dosimeter medium range output. Medium byte of the 3rd (MedLET) dosimeter
              output.

          med_let4_l: MedLET4 dosimeter low range output. Low byte of the 4th (MedLET) dosimeter
              output.

          med_let4_m: MedLET4 dosimeter medium range output. Medium byte of the 4th (MedLET) dosimeter
              output.

          mp_temp: Unitless sensor mounting plate temperature.

          ob_time: Time of the observation, in ISO 8601 UTC format with millisecond precision.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          orig_object_id: Optional identifier provided by the record source to indicate the satellite
              hosting the sensor. This may be an internal identifier and not necessarily map
              to a valid satellite number.

          orig_sensor_id: Optional identifier provided by the record source to indicate the sensor
              identifier which produced this data. This may be an internal identifier and not
              necessarily a valid sensor ID.

          pd1_sig_lev: Photodiode 1 signal level.

          pd2_sig_lev: Photodiode 2 signal level.

          ps_temp_mon: Power supply temperature monitor. This is sensor status telemetry.

          retransmit: Flag indicating whether this record is an original or re-transmitted dataset
              (TRUE indicates a retransmit from the host).

          sat_no: Satellite/catalog number of the on-orbit satellite hosting the sensor.

          sen_mode: The sensor mode associated with this measurements (NORMAL, TEST).

          surf_dos_charge_h: Surface dosimeter charge rate high output (converts to pico-amps/bit). High byte
              of 2 bytes.

          surf_dos_charge_l: Surface dosimeter charge rate low output (converts to pico-amps/bit). Low byte
              of 2 bytes.

          surf_dos_h: Surface dosimeter high range output (converts to pico-coulombs/bit). High byte
              of 3 bytes.

          surf_dos_l: Surface dosimeter low range output (converts to pico-coulombs/bit). Low byte of
              3 bytes.

          surf_dos_m: Surface dosimeter medium range output (converts to pico-coulombs/bit). Middle
              byte of 3 bytes.

          surf_dos_stat: Surface dosimeter status byte.

          transient_data: Array of 144 digitized samples of ESD waveform for transient packets.

          v_ref: Reference voltage (volts/bit). Conversion factor used to convert analog V
              monitor data from bytes to volts.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/udl/ecpsdr",
            body=await async_maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "msg_time": msg_time,
                    "source": source,
                    "type": type,
                    "id": id,
                    "asl5_v_curr_mon": asl5_v_curr_mon,
                    "cds_plate_v_mon": cds_plate_v_mon,
                    "cds_ref_v_mon": cds_ref_v_mon,
                    "cds_threshold": cds_threshold,
                    "cds_throttle": cds_throttle,
                    "checksum": checksum,
                    "dos_bias": dos_bias,
                    "dsl5_v_curr_mon": dsl5_v_curr_mon,
                    "esd_trig_count_h": esd_trig_count_h,
                    "esd_trig_count_l": esd_trig_count_l,
                    "hi_let_l": hi_let_l,
                    "hi_let_m": hi_let_m,
                    "id_sensor": id_sensor,
                    "low_let_l": low_let_l,
                    "low_let_m": low_let_m,
                    "med_let1_l": med_let1_l,
                    "med_let1_m": med_let1_m,
                    "med_let2_l": med_let2_l,
                    "med_let2_m": med_let2_m,
                    "med_let3_l": med_let3_l,
                    "med_let3_m": med_let3_m,
                    "med_let4_l": med_let4_l,
                    "med_let4_m": med_let4_m,
                    "mp_temp": mp_temp,
                    "ob_time": ob_time,
                    "origin": origin,
                    "orig_object_id": orig_object_id,
                    "orig_sensor_id": orig_sensor_id,
                    "pd1_sig_lev": pd1_sig_lev,
                    "pd2_sig_lev": pd2_sig_lev,
                    "ps_temp_mon": ps_temp_mon,
                    "retransmit": retransmit,
                    "sat_no": sat_no,
                    "sen_mode": sen_mode,
                    "surf_dos_charge_h": surf_dos_charge_h,
                    "surf_dos_charge_l": surf_dos_charge_l,
                    "surf_dos_h": surf_dos_h,
                    "surf_dos_l": surf_dos_l,
                    "surf_dos_m": surf_dos_m,
                    "surf_dos_stat": surf_dos_stat,
                    "transient_data": transient_data,
                    "v_ref": v_ref,
                },
                ecpsdr_create_params.EcpsdrCreateParams,
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
    ) -> Ecpsdr:
        """
        Service operation to get a single ECPSDR by its unique ID passed as a path
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
            f"/udl/ecpsdr/{id}",
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
                    ecpsdr_retrieve_params.EcpsdrRetrieveParams,
                ),
            ),
            cast_to=Ecpsdr,
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
    ) -> AsyncPaginator[EcpsdrAbridged, AsyncOffsetPage[EcpsdrAbridged]]:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          msg_time: Time stamp of time packet receipt on ground, in ISO 8601 UTC format with
              millisecond precision. (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/ecpsdr",
            page=AsyncOffsetPage[EcpsdrAbridged],
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
                    ecpsdr_list_params.EcpsdrListParams,
                ),
            ),
            model=EcpsdrAbridged,
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
          msg_time: Time stamp of time packet receipt on ground, in ISO 8601 UTC format with
              millisecond precision. (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return await self._get(
            "/udl/ecpsdr/count",
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
                    ecpsdr_count_params.EcpsdrCountParams,
                ),
            ),
            cast_to=str,
        )

    async def create_bulk(
        self,
        *,
        body: Iterable[ecpsdr_create_bulk_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation intended for initial integration only, to take a list of
        ECPSDR as a POST body and ingest into the database. This operation is not
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
            "/udl/ecpsdr/createBulk",
            body=await async_maybe_transform(body, Iterable[ecpsdr_create_bulk_params.Body]),
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
    ) -> EcpsdrQueryHelpResponse:
        """
        Service operation to provide detailed information on available dynamic query
        parameters for a particular data type.
        """
        return await self._get(
            "/udl/ecpsdr/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EcpsdrQueryHelpResponse,
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
    ) -> EcpsdrTupleResponse:
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

          msg_time: Time stamp of time packet receipt on ground, in ISO 8601 UTC format with
              millisecond precision. (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/udl/ecpsdr/tuple",
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
                    ecpsdr_tuple_params.EcpsdrTupleParams,
                ),
            ),
            cast_to=EcpsdrTupleResponse,
        )


class EcpsdrResourceWithRawResponse:
    def __init__(self, ecpsdr: EcpsdrResource) -> None:
        self._ecpsdr = ecpsdr

        self.create = to_raw_response_wrapper(
            ecpsdr.create,
        )
        self.retrieve = to_raw_response_wrapper(
            ecpsdr.retrieve,
        )
        self.list = to_raw_response_wrapper(
            ecpsdr.list,
        )
        self.count = to_raw_response_wrapper(
            ecpsdr.count,
        )
        self.create_bulk = to_raw_response_wrapper(
            ecpsdr.create_bulk,
        )
        self.query_help = to_raw_response_wrapper(
            ecpsdr.query_help,
        )
        self.tuple = to_raw_response_wrapper(
            ecpsdr.tuple,
        )


class AsyncEcpsdrResourceWithRawResponse:
    def __init__(self, ecpsdr: AsyncEcpsdrResource) -> None:
        self._ecpsdr = ecpsdr

        self.create = async_to_raw_response_wrapper(
            ecpsdr.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            ecpsdr.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            ecpsdr.list,
        )
        self.count = async_to_raw_response_wrapper(
            ecpsdr.count,
        )
        self.create_bulk = async_to_raw_response_wrapper(
            ecpsdr.create_bulk,
        )
        self.query_help = async_to_raw_response_wrapper(
            ecpsdr.query_help,
        )
        self.tuple = async_to_raw_response_wrapper(
            ecpsdr.tuple,
        )


class EcpsdrResourceWithStreamingResponse:
    def __init__(self, ecpsdr: EcpsdrResource) -> None:
        self._ecpsdr = ecpsdr

        self.create = to_streamed_response_wrapper(
            ecpsdr.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            ecpsdr.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            ecpsdr.list,
        )
        self.count = to_streamed_response_wrapper(
            ecpsdr.count,
        )
        self.create_bulk = to_streamed_response_wrapper(
            ecpsdr.create_bulk,
        )
        self.query_help = to_streamed_response_wrapper(
            ecpsdr.query_help,
        )
        self.tuple = to_streamed_response_wrapper(
            ecpsdr.tuple,
        )


class AsyncEcpsdrResourceWithStreamingResponse:
    def __init__(self, ecpsdr: AsyncEcpsdrResource) -> None:
        self._ecpsdr = ecpsdr

        self.create = async_to_streamed_response_wrapper(
            ecpsdr.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            ecpsdr.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            ecpsdr.list,
        )
        self.count = async_to_streamed_response_wrapper(
            ecpsdr.count,
        )
        self.create_bulk = async_to_streamed_response_wrapper(
            ecpsdr.create_bulk,
        )
        self.query_help = async_to_streamed_response_wrapper(
            ecpsdr.query_help,
        )
        self.tuple = async_to_streamed_response_wrapper(
            ecpsdr.tuple,
        )
