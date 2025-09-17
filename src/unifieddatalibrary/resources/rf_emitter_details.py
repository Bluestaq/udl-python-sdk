# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal

import httpx

from ..types import (
    rf_emitter_detail_get_params,
    rf_emitter_detail_list_params,
    rf_emitter_detail_count_params,
    rf_emitter_detail_tuple_params,
    rf_emitter_detail_create_params,
    rf_emitter_detail_update_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven, SequenceNotStr
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
from ..types.rf_emitter_detail_get_response import RfEmitterDetailGetResponse
from ..types.rf_emitter_detail_list_response import RfEmitterDetailListResponse
from ..types.rf_emitter_detail_tuple_response import RfEmitterDetailTupleResponse
from ..types.rf_emitter_detail_queryhelp_response import RfEmitterDetailQueryhelpResponse

__all__ = ["RfEmitterDetailsResource", "AsyncRfEmitterDetailsResource"]


class RfEmitterDetailsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RfEmitterDetailsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return RfEmitterDetailsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RfEmitterDetailsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return RfEmitterDetailsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        id_rf_emitter: str,
        source: str,
        id: str | NotGiven = NOT_GIVEN,
        alternate_facility_name: str | NotGiven = NOT_GIVEN,
        alt_name: str | NotGiven = NOT_GIVEN,
        amplifier: rf_emitter_detail_create_params.Amplifier | NotGiven = NOT_GIVEN,
        antennas: Iterable[rf_emitter_detail_create_params.Antenna] | NotGiven = NOT_GIVEN,
        barrage_noise_bandwidth: float | NotGiven = NOT_GIVEN,
        bit_run_time: float | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        designator: str | NotGiven = NOT_GIVEN,
        doppler_noise: float | NotGiven = NOT_GIVEN,
        drfm_instantaneous_bandwidth: float | NotGiven = NOT_GIVEN,
        family: str | NotGiven = NOT_GIVEN,
        fixed_attenuation: float | NotGiven = NOT_GIVEN,
        id_manufacturer_org: str | NotGiven = NOT_GIVEN,
        id_production_facility_location: str | NotGiven = NOT_GIVEN,
        loaned_to_cocom: str | NotGiven = NOT_GIVEN,
        notes: str | NotGiven = NOT_GIVEN,
        num_bits: int | NotGiven = NOT_GIVEN,
        num_channels: int | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        power_offsets: Iterable[rf_emitter_detail_create_params.PowerOffset] | NotGiven = NOT_GIVEN,
        prep_time: float | NotGiven = NOT_GIVEN,
        primary_cocom: str | NotGiven = NOT_GIVEN,
        production_facility_name: str | NotGiven = NOT_GIVEN,
        receiver_type: str | NotGiven = NOT_GIVEN,
        secondary_notes: str | NotGiven = NOT_GIVEN,
        services: Iterable[rf_emitter_detail_create_params.Service] | NotGiven = NOT_GIVEN,
        system_sensitivity_end: float | NotGiven = NOT_GIVEN,
        system_sensitivity_start: float | NotGiven = NOT_GIVEN,
        ttps: Iterable[rf_emitter_detail_create_params.Ttp] | NotGiven = NOT_GIVEN,
        urls: SequenceNotStr[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single RFEmitterDetails as a POST body and ingest
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

          id_rf_emitter: Unique identifier of the parent RF Emitter.

          source: Source of the data.

          id: Unique identifier of the record, auto-generated by the system.

          alternate_facility_name: Alternate facility name for this RF Emitter.

          alt_name: Optional alternate name or alias for this RF Emitter.

          amplifier: An RF Amplifier associated with an RF Emitter Details.

          antennas: The set of antennas hosted on this EW Emitter system.

          barrage_noise_bandwidth: Barrage noise bandwidth, in megahertz.

          bit_run_time: The length of time, in seconds, for the RF Emitter built-in test to run to
              completion.

          description: Detailed description of the RF Emitter.

          designator: Designator of this RF Emitter.

          doppler_noise: Doppler noise value, in megahertz.

          drfm_instantaneous_bandwidth: Digital Form Radio Memory instantaneous bandwidth in megahertz.

          family: Family of this RF Emitter type.

          fixed_attenuation: A fixed attenuation value to be set on the SRF Emitter HPA when commanding an
              Electronic Attack/Techniques Tactics and Procedures task, in decibels.

          id_manufacturer_org: Unique identifier of the organization which manufactured this RF Emitter.

          id_production_facility_location: Unique identifier of the location of the production facility for this RF
              Emitter.

          loaned_to_cocom: COCOM that has temporary responsibility for scheduling and management of the RF
              Emitter (e.g. SPACEFOR-CENT, SPACEFOR-EURAF, SPACEFOR-INDOPAC, SPACEFOR-KOR,
              SPACEFOR-STRATNORTH, SPACESOC, NONE).

          notes: Notes on the RF Emitter.

          num_bits: Number of bits.

          num_channels: Number of channels.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          power_offsets: A set of system/frequency band adjustments to the power offset commanded in an
              EA/TTP task.

          prep_time: The length of time, in seconds, for the RF Emitter to prepare for a task,
              including sufficient time to slew the antenna and configure the equipment.

          primary_cocom: Primary COCOM that is responsible for scheduling and management of the RF
              Emitter (e.g. SPACEFOR-CENT, SPACEFOR-EURAF, SPACEFOR-INDOPAC, SPACEFOR-KOR,
              SPACEFOR-STRATNORTH, SPACESOC, NONE).

          production_facility_name: Name of the production facility for this RF Emitter.

          receiver_type: Type or name of receiver.

          secondary_notes: Secondary notes on the RF Emitter.

          services: The set of software services running on this EW Emitter system.

          system_sensitivity_end: Receiver sensitivity is the lowest power level at which the receiver can detect
              an RF signal and demodulate data. Sensitivity is purely a receiver specification
              and is independent of the transmitter. End sensitivity range, in
              decibel-milliwatts.

          system_sensitivity_start: Receiver sensitivity is the lowest power level at which the receiver can detect
              an RF signal and demodulate data. Sensitivity is purely a receiver specification
              and is independent of the transmitter. Start sensitivity range, in
              decibel-milliwatts.

          ttps: The set of EA/TTP techniques that are supported by this EW Emitter system.

          urls: Array of URLs containing additional information on this RF Emitter.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/udl/rfemitterdetails",
            body=maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "id_rf_emitter": id_rf_emitter,
                    "source": source,
                    "id": id,
                    "alternate_facility_name": alternate_facility_name,
                    "alt_name": alt_name,
                    "amplifier": amplifier,
                    "antennas": antennas,
                    "barrage_noise_bandwidth": barrage_noise_bandwidth,
                    "bit_run_time": bit_run_time,
                    "description": description,
                    "designator": designator,
                    "doppler_noise": doppler_noise,
                    "drfm_instantaneous_bandwidth": drfm_instantaneous_bandwidth,
                    "family": family,
                    "fixed_attenuation": fixed_attenuation,
                    "id_manufacturer_org": id_manufacturer_org,
                    "id_production_facility_location": id_production_facility_location,
                    "loaned_to_cocom": loaned_to_cocom,
                    "notes": notes,
                    "num_bits": num_bits,
                    "num_channels": num_channels,
                    "origin": origin,
                    "power_offsets": power_offsets,
                    "prep_time": prep_time,
                    "primary_cocom": primary_cocom,
                    "production_facility_name": production_facility_name,
                    "receiver_type": receiver_type,
                    "secondary_notes": secondary_notes,
                    "services": services,
                    "system_sensitivity_end": system_sensitivity_end,
                    "system_sensitivity_start": system_sensitivity_start,
                    "ttps": ttps,
                    "urls": urls,
                },
                rf_emitter_detail_create_params.RfEmitterDetailCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def update(
        self,
        path_id: str,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        id_rf_emitter: str,
        source: str,
        body_id: str | NotGiven = NOT_GIVEN,
        alternate_facility_name: str | NotGiven = NOT_GIVEN,
        alt_name: str | NotGiven = NOT_GIVEN,
        amplifier: rf_emitter_detail_update_params.Amplifier | NotGiven = NOT_GIVEN,
        antennas: Iterable[rf_emitter_detail_update_params.Antenna] | NotGiven = NOT_GIVEN,
        barrage_noise_bandwidth: float | NotGiven = NOT_GIVEN,
        bit_run_time: float | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        designator: str | NotGiven = NOT_GIVEN,
        doppler_noise: float | NotGiven = NOT_GIVEN,
        drfm_instantaneous_bandwidth: float | NotGiven = NOT_GIVEN,
        family: str | NotGiven = NOT_GIVEN,
        fixed_attenuation: float | NotGiven = NOT_GIVEN,
        id_manufacturer_org: str | NotGiven = NOT_GIVEN,
        id_production_facility_location: str | NotGiven = NOT_GIVEN,
        loaned_to_cocom: str | NotGiven = NOT_GIVEN,
        notes: str | NotGiven = NOT_GIVEN,
        num_bits: int | NotGiven = NOT_GIVEN,
        num_channels: int | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        power_offsets: Iterable[rf_emitter_detail_update_params.PowerOffset] | NotGiven = NOT_GIVEN,
        prep_time: float | NotGiven = NOT_GIVEN,
        primary_cocom: str | NotGiven = NOT_GIVEN,
        production_facility_name: str | NotGiven = NOT_GIVEN,
        receiver_type: str | NotGiven = NOT_GIVEN,
        secondary_notes: str | NotGiven = NOT_GIVEN,
        services: Iterable[rf_emitter_detail_update_params.Service] | NotGiven = NOT_GIVEN,
        system_sensitivity_end: float | NotGiven = NOT_GIVEN,
        system_sensitivity_start: float | NotGiven = NOT_GIVEN,
        ttps: Iterable[rf_emitter_detail_update_params.Ttp] | NotGiven = NOT_GIVEN,
        urls: SequenceNotStr[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Service operation to update a single RFEmitterDetails record.

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

          id_rf_emitter: Unique identifier of the parent RF Emitter.

          source: Source of the data.

          body_id: Unique identifier of the record, auto-generated by the system.

          alternate_facility_name: Alternate facility name for this RF Emitter.

          alt_name: Optional alternate name or alias for this RF Emitter.

          amplifier: An RF Amplifier associated with an RF Emitter Details.

          antennas: The set of antennas hosted on this EW Emitter system.

          barrage_noise_bandwidth: Barrage noise bandwidth, in megahertz.

          bit_run_time: The length of time, in seconds, for the RF Emitter built-in test to run to
              completion.

          description: Detailed description of the RF Emitter.

          designator: Designator of this RF Emitter.

          doppler_noise: Doppler noise value, in megahertz.

          drfm_instantaneous_bandwidth: Digital Form Radio Memory instantaneous bandwidth in megahertz.

          family: Family of this RF Emitter type.

          fixed_attenuation: A fixed attenuation value to be set on the SRF Emitter HPA when commanding an
              Electronic Attack/Techniques Tactics and Procedures task, in decibels.

          id_manufacturer_org: Unique identifier of the organization which manufactured this RF Emitter.

          id_production_facility_location: Unique identifier of the location of the production facility for this RF
              Emitter.

          loaned_to_cocom: COCOM that has temporary responsibility for scheduling and management of the RF
              Emitter (e.g. SPACEFOR-CENT, SPACEFOR-EURAF, SPACEFOR-INDOPAC, SPACEFOR-KOR,
              SPACEFOR-STRATNORTH, SPACESOC, NONE).

          notes: Notes on the RF Emitter.

          num_bits: Number of bits.

          num_channels: Number of channels.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          power_offsets: A set of system/frequency band adjustments to the power offset commanded in an
              EA/TTP task.

          prep_time: The length of time, in seconds, for the RF Emitter to prepare for a task,
              including sufficient time to slew the antenna and configure the equipment.

          primary_cocom: Primary COCOM that is responsible for scheduling and management of the RF
              Emitter (e.g. SPACEFOR-CENT, SPACEFOR-EURAF, SPACEFOR-INDOPAC, SPACEFOR-KOR,
              SPACEFOR-STRATNORTH, SPACESOC, NONE).

          production_facility_name: Name of the production facility for this RF Emitter.

          receiver_type: Type or name of receiver.

          secondary_notes: Secondary notes on the RF Emitter.

          services: The set of software services running on this EW Emitter system.

          system_sensitivity_end: Receiver sensitivity is the lowest power level at which the receiver can detect
              an RF signal and demodulate data. Sensitivity is purely a receiver specification
              and is independent of the transmitter. End sensitivity range, in
              decibel-milliwatts.

          system_sensitivity_start: Receiver sensitivity is the lowest power level at which the receiver can detect
              an RF signal and demodulate data. Sensitivity is purely a receiver specification
              and is independent of the transmitter. Start sensitivity range, in
              decibel-milliwatts.

          ttps: The set of EA/TTP techniques that are supported by this EW Emitter system.

          urls: Array of URLs containing additional information on this RF Emitter.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            f"/udl/rfemitterdetails/{path_id}",
            body=maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "id_rf_emitter": id_rf_emitter,
                    "source": source,
                    "body_id": body_id,
                    "alternate_facility_name": alternate_facility_name,
                    "alt_name": alt_name,
                    "amplifier": amplifier,
                    "antennas": antennas,
                    "barrage_noise_bandwidth": barrage_noise_bandwidth,
                    "bit_run_time": bit_run_time,
                    "description": description,
                    "designator": designator,
                    "doppler_noise": doppler_noise,
                    "drfm_instantaneous_bandwidth": drfm_instantaneous_bandwidth,
                    "family": family,
                    "fixed_attenuation": fixed_attenuation,
                    "id_manufacturer_org": id_manufacturer_org,
                    "id_production_facility_location": id_production_facility_location,
                    "loaned_to_cocom": loaned_to_cocom,
                    "notes": notes,
                    "num_bits": num_bits,
                    "num_channels": num_channels,
                    "origin": origin,
                    "power_offsets": power_offsets,
                    "prep_time": prep_time,
                    "primary_cocom": primary_cocom,
                    "production_facility_name": production_facility_name,
                    "receiver_type": receiver_type,
                    "secondary_notes": secondary_notes,
                    "services": services,
                    "system_sensitivity_end": system_sensitivity_end,
                    "system_sensitivity_start": system_sensitivity_start,
                    "ttps": ttps,
                    "urls": urls,
                },
                rf_emitter_detail_update_params.RfEmitterDetailUpdateParams,
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
    ) -> SyncOffsetPage[RfEmitterDetailListResponse]:
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
            "/udl/rfemitterdetails",
            page=SyncOffsetPage[RfEmitterDetailListResponse],
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
                    rf_emitter_detail_list_params.RfEmitterDetailListParams,
                ),
            ),
            model=RfEmitterDetailListResponse,
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
        Service operation to delete a single RFEmitterDetails record specified by the
        passed ID path parameter. A specific role is required to perform this service
        operation. Please contact the UDL team for assistance.

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
            f"/udl/rfemitterdetails/{id}",
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
            "/udl/rfemitterdetails/count",
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
                    rf_emitter_detail_count_params.RfEmitterDetailCountParams,
                ),
            ),
            cast_to=str,
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
    ) -> RfEmitterDetailGetResponse:
        """
        Service operation to get a single RFEmitterDetails record by its unique ID
        passed as a path parameter.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/udl/rfemitterdetails/{id}",
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
                    rf_emitter_detail_get_params.RfEmitterDetailGetParams,
                ),
            ),
            cast_to=RfEmitterDetailGetResponse,
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
    ) -> RfEmitterDetailQueryhelpResponse:
        """
        Service operation to provide detailed information on available dynamic query
        parameters for a particular data type.
        """
        return self._get(
            "/udl/rfemitterdetails/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RfEmitterDetailQueryhelpResponse,
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
    ) -> RfEmitterDetailTupleResponse:
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
            "/udl/rfemitterdetails/tuple",
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
                    rf_emitter_detail_tuple_params.RfEmitterDetailTupleParams,
                ),
            ),
            cast_to=RfEmitterDetailTupleResponse,
        )


class AsyncRfEmitterDetailsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRfEmitterDetailsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncRfEmitterDetailsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRfEmitterDetailsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncRfEmitterDetailsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        id_rf_emitter: str,
        source: str,
        id: str | NotGiven = NOT_GIVEN,
        alternate_facility_name: str | NotGiven = NOT_GIVEN,
        alt_name: str | NotGiven = NOT_GIVEN,
        amplifier: rf_emitter_detail_create_params.Amplifier | NotGiven = NOT_GIVEN,
        antennas: Iterable[rf_emitter_detail_create_params.Antenna] | NotGiven = NOT_GIVEN,
        barrage_noise_bandwidth: float | NotGiven = NOT_GIVEN,
        bit_run_time: float | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        designator: str | NotGiven = NOT_GIVEN,
        doppler_noise: float | NotGiven = NOT_GIVEN,
        drfm_instantaneous_bandwidth: float | NotGiven = NOT_GIVEN,
        family: str | NotGiven = NOT_GIVEN,
        fixed_attenuation: float | NotGiven = NOT_GIVEN,
        id_manufacturer_org: str | NotGiven = NOT_GIVEN,
        id_production_facility_location: str | NotGiven = NOT_GIVEN,
        loaned_to_cocom: str | NotGiven = NOT_GIVEN,
        notes: str | NotGiven = NOT_GIVEN,
        num_bits: int | NotGiven = NOT_GIVEN,
        num_channels: int | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        power_offsets: Iterable[rf_emitter_detail_create_params.PowerOffset] | NotGiven = NOT_GIVEN,
        prep_time: float | NotGiven = NOT_GIVEN,
        primary_cocom: str | NotGiven = NOT_GIVEN,
        production_facility_name: str | NotGiven = NOT_GIVEN,
        receiver_type: str | NotGiven = NOT_GIVEN,
        secondary_notes: str | NotGiven = NOT_GIVEN,
        services: Iterable[rf_emitter_detail_create_params.Service] | NotGiven = NOT_GIVEN,
        system_sensitivity_end: float | NotGiven = NOT_GIVEN,
        system_sensitivity_start: float | NotGiven = NOT_GIVEN,
        ttps: Iterable[rf_emitter_detail_create_params.Ttp] | NotGiven = NOT_GIVEN,
        urls: SequenceNotStr[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single RFEmitterDetails as a POST body and ingest
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

          id_rf_emitter: Unique identifier of the parent RF Emitter.

          source: Source of the data.

          id: Unique identifier of the record, auto-generated by the system.

          alternate_facility_name: Alternate facility name for this RF Emitter.

          alt_name: Optional alternate name or alias for this RF Emitter.

          amplifier: An RF Amplifier associated with an RF Emitter Details.

          antennas: The set of antennas hosted on this EW Emitter system.

          barrage_noise_bandwidth: Barrage noise bandwidth, in megahertz.

          bit_run_time: The length of time, in seconds, for the RF Emitter built-in test to run to
              completion.

          description: Detailed description of the RF Emitter.

          designator: Designator of this RF Emitter.

          doppler_noise: Doppler noise value, in megahertz.

          drfm_instantaneous_bandwidth: Digital Form Radio Memory instantaneous bandwidth in megahertz.

          family: Family of this RF Emitter type.

          fixed_attenuation: A fixed attenuation value to be set on the SRF Emitter HPA when commanding an
              Electronic Attack/Techniques Tactics and Procedures task, in decibels.

          id_manufacturer_org: Unique identifier of the organization which manufactured this RF Emitter.

          id_production_facility_location: Unique identifier of the location of the production facility for this RF
              Emitter.

          loaned_to_cocom: COCOM that has temporary responsibility for scheduling and management of the RF
              Emitter (e.g. SPACEFOR-CENT, SPACEFOR-EURAF, SPACEFOR-INDOPAC, SPACEFOR-KOR,
              SPACEFOR-STRATNORTH, SPACESOC, NONE).

          notes: Notes on the RF Emitter.

          num_bits: Number of bits.

          num_channels: Number of channels.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          power_offsets: A set of system/frequency band adjustments to the power offset commanded in an
              EA/TTP task.

          prep_time: The length of time, in seconds, for the RF Emitter to prepare for a task,
              including sufficient time to slew the antenna and configure the equipment.

          primary_cocom: Primary COCOM that is responsible for scheduling and management of the RF
              Emitter (e.g. SPACEFOR-CENT, SPACEFOR-EURAF, SPACEFOR-INDOPAC, SPACEFOR-KOR,
              SPACEFOR-STRATNORTH, SPACESOC, NONE).

          production_facility_name: Name of the production facility for this RF Emitter.

          receiver_type: Type or name of receiver.

          secondary_notes: Secondary notes on the RF Emitter.

          services: The set of software services running on this EW Emitter system.

          system_sensitivity_end: Receiver sensitivity is the lowest power level at which the receiver can detect
              an RF signal and demodulate data. Sensitivity is purely a receiver specification
              and is independent of the transmitter. End sensitivity range, in
              decibel-milliwatts.

          system_sensitivity_start: Receiver sensitivity is the lowest power level at which the receiver can detect
              an RF signal and demodulate data. Sensitivity is purely a receiver specification
              and is independent of the transmitter. Start sensitivity range, in
              decibel-milliwatts.

          ttps: The set of EA/TTP techniques that are supported by this EW Emitter system.

          urls: Array of URLs containing additional information on this RF Emitter.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/udl/rfemitterdetails",
            body=await async_maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "id_rf_emitter": id_rf_emitter,
                    "source": source,
                    "id": id,
                    "alternate_facility_name": alternate_facility_name,
                    "alt_name": alt_name,
                    "amplifier": amplifier,
                    "antennas": antennas,
                    "barrage_noise_bandwidth": barrage_noise_bandwidth,
                    "bit_run_time": bit_run_time,
                    "description": description,
                    "designator": designator,
                    "doppler_noise": doppler_noise,
                    "drfm_instantaneous_bandwidth": drfm_instantaneous_bandwidth,
                    "family": family,
                    "fixed_attenuation": fixed_attenuation,
                    "id_manufacturer_org": id_manufacturer_org,
                    "id_production_facility_location": id_production_facility_location,
                    "loaned_to_cocom": loaned_to_cocom,
                    "notes": notes,
                    "num_bits": num_bits,
                    "num_channels": num_channels,
                    "origin": origin,
                    "power_offsets": power_offsets,
                    "prep_time": prep_time,
                    "primary_cocom": primary_cocom,
                    "production_facility_name": production_facility_name,
                    "receiver_type": receiver_type,
                    "secondary_notes": secondary_notes,
                    "services": services,
                    "system_sensitivity_end": system_sensitivity_end,
                    "system_sensitivity_start": system_sensitivity_start,
                    "ttps": ttps,
                    "urls": urls,
                },
                rf_emitter_detail_create_params.RfEmitterDetailCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def update(
        self,
        path_id: str,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        id_rf_emitter: str,
        source: str,
        body_id: str | NotGiven = NOT_GIVEN,
        alternate_facility_name: str | NotGiven = NOT_GIVEN,
        alt_name: str | NotGiven = NOT_GIVEN,
        amplifier: rf_emitter_detail_update_params.Amplifier | NotGiven = NOT_GIVEN,
        antennas: Iterable[rf_emitter_detail_update_params.Antenna] | NotGiven = NOT_GIVEN,
        barrage_noise_bandwidth: float | NotGiven = NOT_GIVEN,
        bit_run_time: float | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        designator: str | NotGiven = NOT_GIVEN,
        doppler_noise: float | NotGiven = NOT_GIVEN,
        drfm_instantaneous_bandwidth: float | NotGiven = NOT_GIVEN,
        family: str | NotGiven = NOT_GIVEN,
        fixed_attenuation: float | NotGiven = NOT_GIVEN,
        id_manufacturer_org: str | NotGiven = NOT_GIVEN,
        id_production_facility_location: str | NotGiven = NOT_GIVEN,
        loaned_to_cocom: str | NotGiven = NOT_GIVEN,
        notes: str | NotGiven = NOT_GIVEN,
        num_bits: int | NotGiven = NOT_GIVEN,
        num_channels: int | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        power_offsets: Iterable[rf_emitter_detail_update_params.PowerOffset] | NotGiven = NOT_GIVEN,
        prep_time: float | NotGiven = NOT_GIVEN,
        primary_cocom: str | NotGiven = NOT_GIVEN,
        production_facility_name: str | NotGiven = NOT_GIVEN,
        receiver_type: str | NotGiven = NOT_GIVEN,
        secondary_notes: str | NotGiven = NOT_GIVEN,
        services: Iterable[rf_emitter_detail_update_params.Service] | NotGiven = NOT_GIVEN,
        system_sensitivity_end: float | NotGiven = NOT_GIVEN,
        system_sensitivity_start: float | NotGiven = NOT_GIVEN,
        ttps: Iterable[rf_emitter_detail_update_params.Ttp] | NotGiven = NOT_GIVEN,
        urls: SequenceNotStr[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Service operation to update a single RFEmitterDetails record.

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

          id_rf_emitter: Unique identifier of the parent RF Emitter.

          source: Source of the data.

          body_id: Unique identifier of the record, auto-generated by the system.

          alternate_facility_name: Alternate facility name for this RF Emitter.

          alt_name: Optional alternate name or alias for this RF Emitter.

          amplifier: An RF Amplifier associated with an RF Emitter Details.

          antennas: The set of antennas hosted on this EW Emitter system.

          barrage_noise_bandwidth: Barrage noise bandwidth, in megahertz.

          bit_run_time: The length of time, in seconds, for the RF Emitter built-in test to run to
              completion.

          description: Detailed description of the RF Emitter.

          designator: Designator of this RF Emitter.

          doppler_noise: Doppler noise value, in megahertz.

          drfm_instantaneous_bandwidth: Digital Form Radio Memory instantaneous bandwidth in megahertz.

          family: Family of this RF Emitter type.

          fixed_attenuation: A fixed attenuation value to be set on the SRF Emitter HPA when commanding an
              Electronic Attack/Techniques Tactics and Procedures task, in decibels.

          id_manufacturer_org: Unique identifier of the organization which manufactured this RF Emitter.

          id_production_facility_location: Unique identifier of the location of the production facility for this RF
              Emitter.

          loaned_to_cocom: COCOM that has temporary responsibility for scheduling and management of the RF
              Emitter (e.g. SPACEFOR-CENT, SPACEFOR-EURAF, SPACEFOR-INDOPAC, SPACEFOR-KOR,
              SPACEFOR-STRATNORTH, SPACESOC, NONE).

          notes: Notes on the RF Emitter.

          num_bits: Number of bits.

          num_channels: Number of channels.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          power_offsets: A set of system/frequency band adjustments to the power offset commanded in an
              EA/TTP task.

          prep_time: The length of time, in seconds, for the RF Emitter to prepare for a task,
              including sufficient time to slew the antenna and configure the equipment.

          primary_cocom: Primary COCOM that is responsible for scheduling and management of the RF
              Emitter (e.g. SPACEFOR-CENT, SPACEFOR-EURAF, SPACEFOR-INDOPAC, SPACEFOR-KOR,
              SPACEFOR-STRATNORTH, SPACESOC, NONE).

          production_facility_name: Name of the production facility for this RF Emitter.

          receiver_type: Type or name of receiver.

          secondary_notes: Secondary notes on the RF Emitter.

          services: The set of software services running on this EW Emitter system.

          system_sensitivity_end: Receiver sensitivity is the lowest power level at which the receiver can detect
              an RF signal and demodulate data. Sensitivity is purely a receiver specification
              and is independent of the transmitter. End sensitivity range, in
              decibel-milliwatts.

          system_sensitivity_start: Receiver sensitivity is the lowest power level at which the receiver can detect
              an RF signal and demodulate data. Sensitivity is purely a receiver specification
              and is independent of the transmitter. Start sensitivity range, in
              decibel-milliwatts.

          ttps: The set of EA/TTP techniques that are supported by this EW Emitter system.

          urls: Array of URLs containing additional information on this RF Emitter.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            f"/udl/rfemitterdetails/{path_id}",
            body=await async_maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "id_rf_emitter": id_rf_emitter,
                    "source": source,
                    "body_id": body_id,
                    "alternate_facility_name": alternate_facility_name,
                    "alt_name": alt_name,
                    "amplifier": amplifier,
                    "antennas": antennas,
                    "barrage_noise_bandwidth": barrage_noise_bandwidth,
                    "bit_run_time": bit_run_time,
                    "description": description,
                    "designator": designator,
                    "doppler_noise": doppler_noise,
                    "drfm_instantaneous_bandwidth": drfm_instantaneous_bandwidth,
                    "family": family,
                    "fixed_attenuation": fixed_attenuation,
                    "id_manufacturer_org": id_manufacturer_org,
                    "id_production_facility_location": id_production_facility_location,
                    "loaned_to_cocom": loaned_to_cocom,
                    "notes": notes,
                    "num_bits": num_bits,
                    "num_channels": num_channels,
                    "origin": origin,
                    "power_offsets": power_offsets,
                    "prep_time": prep_time,
                    "primary_cocom": primary_cocom,
                    "production_facility_name": production_facility_name,
                    "receiver_type": receiver_type,
                    "secondary_notes": secondary_notes,
                    "services": services,
                    "system_sensitivity_end": system_sensitivity_end,
                    "system_sensitivity_start": system_sensitivity_start,
                    "ttps": ttps,
                    "urls": urls,
                },
                rf_emitter_detail_update_params.RfEmitterDetailUpdateParams,
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
    ) -> AsyncPaginator[RfEmitterDetailListResponse, AsyncOffsetPage[RfEmitterDetailListResponse]]:
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
            "/udl/rfemitterdetails",
            page=AsyncOffsetPage[RfEmitterDetailListResponse],
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
                    rf_emitter_detail_list_params.RfEmitterDetailListParams,
                ),
            ),
            model=RfEmitterDetailListResponse,
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
        Service operation to delete a single RFEmitterDetails record specified by the
        passed ID path parameter. A specific role is required to perform this service
        operation. Please contact the UDL team for assistance.

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
            f"/udl/rfemitterdetails/{id}",
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
            "/udl/rfemitterdetails/count",
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
                    rf_emitter_detail_count_params.RfEmitterDetailCountParams,
                ),
            ),
            cast_to=str,
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
    ) -> RfEmitterDetailGetResponse:
        """
        Service operation to get a single RFEmitterDetails record by its unique ID
        passed as a path parameter.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/udl/rfemitterdetails/{id}",
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
                    rf_emitter_detail_get_params.RfEmitterDetailGetParams,
                ),
            ),
            cast_to=RfEmitterDetailGetResponse,
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
    ) -> RfEmitterDetailQueryhelpResponse:
        """
        Service operation to provide detailed information on available dynamic query
        parameters for a particular data type.
        """
        return await self._get(
            "/udl/rfemitterdetails/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RfEmitterDetailQueryhelpResponse,
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
    ) -> RfEmitterDetailTupleResponse:
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
            "/udl/rfemitterdetails/tuple",
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
                    rf_emitter_detail_tuple_params.RfEmitterDetailTupleParams,
                ),
            ),
            cast_to=RfEmitterDetailTupleResponse,
        )


class RfEmitterDetailsResourceWithRawResponse:
    def __init__(self, rf_emitter_details: RfEmitterDetailsResource) -> None:
        self._rf_emitter_details = rf_emitter_details

        self.create = to_raw_response_wrapper(
            rf_emitter_details.create,
        )
        self.update = to_raw_response_wrapper(
            rf_emitter_details.update,
        )
        self.list = to_raw_response_wrapper(
            rf_emitter_details.list,
        )
        self.delete = to_raw_response_wrapper(
            rf_emitter_details.delete,
        )
        self.count = to_raw_response_wrapper(
            rf_emitter_details.count,
        )
        self.get = to_raw_response_wrapper(
            rf_emitter_details.get,
        )
        self.queryhelp = to_raw_response_wrapper(
            rf_emitter_details.queryhelp,
        )
        self.tuple = to_raw_response_wrapper(
            rf_emitter_details.tuple,
        )


class AsyncRfEmitterDetailsResourceWithRawResponse:
    def __init__(self, rf_emitter_details: AsyncRfEmitterDetailsResource) -> None:
        self._rf_emitter_details = rf_emitter_details

        self.create = async_to_raw_response_wrapper(
            rf_emitter_details.create,
        )
        self.update = async_to_raw_response_wrapper(
            rf_emitter_details.update,
        )
        self.list = async_to_raw_response_wrapper(
            rf_emitter_details.list,
        )
        self.delete = async_to_raw_response_wrapper(
            rf_emitter_details.delete,
        )
        self.count = async_to_raw_response_wrapper(
            rf_emitter_details.count,
        )
        self.get = async_to_raw_response_wrapper(
            rf_emitter_details.get,
        )
        self.queryhelp = async_to_raw_response_wrapper(
            rf_emitter_details.queryhelp,
        )
        self.tuple = async_to_raw_response_wrapper(
            rf_emitter_details.tuple,
        )


class RfEmitterDetailsResourceWithStreamingResponse:
    def __init__(self, rf_emitter_details: RfEmitterDetailsResource) -> None:
        self._rf_emitter_details = rf_emitter_details

        self.create = to_streamed_response_wrapper(
            rf_emitter_details.create,
        )
        self.update = to_streamed_response_wrapper(
            rf_emitter_details.update,
        )
        self.list = to_streamed_response_wrapper(
            rf_emitter_details.list,
        )
        self.delete = to_streamed_response_wrapper(
            rf_emitter_details.delete,
        )
        self.count = to_streamed_response_wrapper(
            rf_emitter_details.count,
        )
        self.get = to_streamed_response_wrapper(
            rf_emitter_details.get,
        )
        self.queryhelp = to_streamed_response_wrapper(
            rf_emitter_details.queryhelp,
        )
        self.tuple = to_streamed_response_wrapper(
            rf_emitter_details.tuple,
        )


class AsyncRfEmitterDetailsResourceWithStreamingResponse:
    def __init__(self, rf_emitter_details: AsyncRfEmitterDetailsResource) -> None:
        self._rf_emitter_details = rf_emitter_details

        self.create = async_to_streamed_response_wrapper(
            rf_emitter_details.create,
        )
        self.update = async_to_streamed_response_wrapper(
            rf_emitter_details.update,
        )
        self.list = async_to_streamed_response_wrapper(
            rf_emitter_details.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            rf_emitter_details.delete,
        )
        self.count = async_to_streamed_response_wrapper(
            rf_emitter_details.count,
        )
        self.get = async_to_streamed_response_wrapper(
            rf_emitter_details.get,
        )
        self.queryhelp = async_to_streamed_response_wrapper(
            rf_emitter_details.queryhelp,
        )
        self.tuple = async_to_streamed_response_wrapper(
            rf_emitter_details.tuple,
        )
