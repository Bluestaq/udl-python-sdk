# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
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
from ...types.rf_emitter import (
    detail_get_params,
    detail_list_params,
    detail_count_params,
    detail_tuple_params,
    detail_create_params,
    detail_update_params,
)
from ...types.rf_emitter.detail_get_response import DetailGetResponse
from ...types.rf_emitter.detail_list_response import DetailListResponse
from ...types.rf_emitter.detail_tuple_response import DetailTupleResponse
from ...types.rf_emitter.detail_queryhelp_response import DetailQueryhelpResponse

__all__ = ["DetailsResource", "AsyncDetailsResource"]


class DetailsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DetailsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return DetailsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DetailsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return DetailsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        id_rf_emitter: str,
        source: str,
        id: str | Omit = omit,
        alternate_facility_name: str | Omit = omit,
        alt_name: str | Omit = omit,
        amplifier: detail_create_params.Amplifier | Omit = omit,
        antennas: Iterable[detail_create_params.Antenna] | Omit = omit,
        barrage_noise_bandwidth: float | Omit = omit,
        bit_run_time: float | Omit = omit,
        description: str | Omit = omit,
        designator: str | Omit = omit,
        doppler_noise: float | Omit = omit,
        drfm_instantaneous_bandwidth: float | Omit = omit,
        family: str | Omit = omit,
        fixed_attenuation: float | Omit = omit,
        id_manufacturer_org: str | Omit = omit,
        id_production_facility_location: str | Omit = omit,
        loaned_to_cocom: str | Omit = omit,
        notes: str | Omit = omit,
        num_bits: int | Omit = omit,
        num_channels: int | Omit = omit,
        origin: str | Omit = omit,
        power_offsets: Iterable[detail_create_params.PowerOffset] | Omit = omit,
        prep_time: float | Omit = omit,
        primary_cocom: str | Omit = omit,
        production_facility_name: str | Omit = omit,
        receiver_type: str | Omit = omit,
        secondary_notes: str | Omit = omit,
        services: Iterable[detail_create_params.Service] | Omit = omit,
        system_sensitivity_end: float | Omit = omit,
        system_sensitivity_start: float | Omit = omit,
        ttps: Iterable[detail_create_params.Ttp] | Omit = omit,
        urls: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
                detail_create_params.DetailCreateParams,
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
        body_id: str | Omit = omit,
        alternate_facility_name: str | Omit = omit,
        alt_name: str | Omit = omit,
        amplifier: detail_update_params.Amplifier | Omit = omit,
        antennas: Iterable[detail_update_params.Antenna] | Omit = omit,
        barrage_noise_bandwidth: float | Omit = omit,
        bit_run_time: float | Omit = omit,
        description: str | Omit = omit,
        designator: str | Omit = omit,
        doppler_noise: float | Omit = omit,
        drfm_instantaneous_bandwidth: float | Omit = omit,
        family: str | Omit = omit,
        fixed_attenuation: float | Omit = omit,
        id_manufacturer_org: str | Omit = omit,
        id_production_facility_location: str | Omit = omit,
        loaned_to_cocom: str | Omit = omit,
        notes: str | Omit = omit,
        num_bits: int | Omit = omit,
        num_channels: int | Omit = omit,
        origin: str | Omit = omit,
        power_offsets: Iterable[detail_update_params.PowerOffset] | Omit = omit,
        prep_time: float | Omit = omit,
        primary_cocom: str | Omit = omit,
        production_facility_name: str | Omit = omit,
        receiver_type: str | Omit = omit,
        secondary_notes: str | Omit = omit,
        services: Iterable[detail_update_params.Service] | Omit = omit,
        system_sensitivity_end: float | Omit = omit,
        system_sensitivity_start: float | Omit = omit,
        ttps: Iterable[detail_update_params.Ttp] | Omit = omit,
        urls: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
                detail_update_params.DetailUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        *,
        first_result: int | Omit = omit,
        max_results: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncOffsetPage[DetailListResponse]:
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
            page=SyncOffsetPage[DetailListResponse],
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
                    detail_list_params.DetailListParams,
                ),
            ),
            model=DetailListResponse,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        first_result: int | Omit = omit,
        max_results: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
                    detail_count_params.DetailCountParams,
                ),
            ),
            cast_to=str,
        )

    def get(
        self,
        id: str,
        *,
        first_result: int | Omit = omit,
        max_results: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DetailGetResponse:
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
                    detail_get_params.DetailGetParams,
                ),
            ),
            cast_to=DetailGetResponse,
        )

    def queryhelp(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DetailQueryhelpResponse:
        """
        Service operation to provide detailed information on available dynamic query
        parameters for a particular data type.
        """
        return self._get(
            "/udl/rfemitterdetails/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DetailQueryhelpResponse,
        )

    def tuple(
        self,
        *,
        columns: str,
        first_result: int | Omit = omit,
        max_results: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DetailTupleResponse:
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
                    detail_tuple_params.DetailTupleParams,
                ),
            ),
            cast_to=DetailTupleResponse,
        )


class AsyncDetailsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDetailsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncDetailsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDetailsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncDetailsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        id_rf_emitter: str,
        source: str,
        id: str | Omit = omit,
        alternate_facility_name: str | Omit = omit,
        alt_name: str | Omit = omit,
        amplifier: detail_create_params.Amplifier | Omit = omit,
        antennas: Iterable[detail_create_params.Antenna] | Omit = omit,
        barrage_noise_bandwidth: float | Omit = omit,
        bit_run_time: float | Omit = omit,
        description: str | Omit = omit,
        designator: str | Omit = omit,
        doppler_noise: float | Omit = omit,
        drfm_instantaneous_bandwidth: float | Omit = omit,
        family: str | Omit = omit,
        fixed_attenuation: float | Omit = omit,
        id_manufacturer_org: str | Omit = omit,
        id_production_facility_location: str | Omit = omit,
        loaned_to_cocom: str | Omit = omit,
        notes: str | Omit = omit,
        num_bits: int | Omit = omit,
        num_channels: int | Omit = omit,
        origin: str | Omit = omit,
        power_offsets: Iterable[detail_create_params.PowerOffset] | Omit = omit,
        prep_time: float | Omit = omit,
        primary_cocom: str | Omit = omit,
        production_facility_name: str | Omit = omit,
        receiver_type: str | Omit = omit,
        secondary_notes: str | Omit = omit,
        services: Iterable[detail_create_params.Service] | Omit = omit,
        system_sensitivity_end: float | Omit = omit,
        system_sensitivity_start: float | Omit = omit,
        ttps: Iterable[detail_create_params.Ttp] | Omit = omit,
        urls: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
                detail_create_params.DetailCreateParams,
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
        body_id: str | Omit = omit,
        alternate_facility_name: str | Omit = omit,
        alt_name: str | Omit = omit,
        amplifier: detail_update_params.Amplifier | Omit = omit,
        antennas: Iterable[detail_update_params.Antenna] | Omit = omit,
        barrage_noise_bandwidth: float | Omit = omit,
        bit_run_time: float | Omit = omit,
        description: str | Omit = omit,
        designator: str | Omit = omit,
        doppler_noise: float | Omit = omit,
        drfm_instantaneous_bandwidth: float | Omit = omit,
        family: str | Omit = omit,
        fixed_attenuation: float | Omit = omit,
        id_manufacturer_org: str | Omit = omit,
        id_production_facility_location: str | Omit = omit,
        loaned_to_cocom: str | Omit = omit,
        notes: str | Omit = omit,
        num_bits: int | Omit = omit,
        num_channels: int | Omit = omit,
        origin: str | Omit = omit,
        power_offsets: Iterable[detail_update_params.PowerOffset] | Omit = omit,
        prep_time: float | Omit = omit,
        primary_cocom: str | Omit = omit,
        production_facility_name: str | Omit = omit,
        receiver_type: str | Omit = omit,
        secondary_notes: str | Omit = omit,
        services: Iterable[detail_update_params.Service] | Omit = omit,
        system_sensitivity_end: float | Omit = omit,
        system_sensitivity_start: float | Omit = omit,
        ttps: Iterable[detail_update_params.Ttp] | Omit = omit,
        urls: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
                detail_update_params.DetailUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        *,
        first_result: int | Omit = omit,
        max_results: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[DetailListResponse, AsyncOffsetPage[DetailListResponse]]:
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
            page=AsyncOffsetPage[DetailListResponse],
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
                    detail_list_params.DetailListParams,
                ),
            ),
            model=DetailListResponse,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        first_result: int | Omit = omit,
        max_results: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
                    detail_count_params.DetailCountParams,
                ),
            ),
            cast_to=str,
        )

    async def get(
        self,
        id: str,
        *,
        first_result: int | Omit = omit,
        max_results: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DetailGetResponse:
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
                    detail_get_params.DetailGetParams,
                ),
            ),
            cast_to=DetailGetResponse,
        )

    async def queryhelp(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DetailQueryhelpResponse:
        """
        Service operation to provide detailed information on available dynamic query
        parameters for a particular data type.
        """
        return await self._get(
            "/udl/rfemitterdetails/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DetailQueryhelpResponse,
        )

    async def tuple(
        self,
        *,
        columns: str,
        first_result: int | Omit = omit,
        max_results: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DetailTupleResponse:
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
                    detail_tuple_params.DetailTupleParams,
                ),
            ),
            cast_to=DetailTupleResponse,
        )


class DetailsResourceWithRawResponse:
    def __init__(self, details: DetailsResource) -> None:
        self._details = details

        self.create = to_raw_response_wrapper(
            details.create,
        )
        self.update = to_raw_response_wrapper(
            details.update,
        )
        self.list = to_raw_response_wrapper(
            details.list,
        )
        self.delete = to_raw_response_wrapper(
            details.delete,
        )
        self.count = to_raw_response_wrapper(
            details.count,
        )
        self.get = to_raw_response_wrapper(
            details.get,
        )
        self.queryhelp = to_raw_response_wrapper(
            details.queryhelp,
        )
        self.tuple = to_raw_response_wrapper(
            details.tuple,
        )


class AsyncDetailsResourceWithRawResponse:
    def __init__(self, details: AsyncDetailsResource) -> None:
        self._details = details

        self.create = async_to_raw_response_wrapper(
            details.create,
        )
        self.update = async_to_raw_response_wrapper(
            details.update,
        )
        self.list = async_to_raw_response_wrapper(
            details.list,
        )
        self.delete = async_to_raw_response_wrapper(
            details.delete,
        )
        self.count = async_to_raw_response_wrapper(
            details.count,
        )
        self.get = async_to_raw_response_wrapper(
            details.get,
        )
        self.queryhelp = async_to_raw_response_wrapper(
            details.queryhelp,
        )
        self.tuple = async_to_raw_response_wrapper(
            details.tuple,
        )


class DetailsResourceWithStreamingResponse:
    def __init__(self, details: DetailsResource) -> None:
        self._details = details

        self.create = to_streamed_response_wrapper(
            details.create,
        )
        self.update = to_streamed_response_wrapper(
            details.update,
        )
        self.list = to_streamed_response_wrapper(
            details.list,
        )
        self.delete = to_streamed_response_wrapper(
            details.delete,
        )
        self.count = to_streamed_response_wrapper(
            details.count,
        )
        self.get = to_streamed_response_wrapper(
            details.get,
        )
        self.queryhelp = to_streamed_response_wrapper(
            details.queryhelp,
        )
        self.tuple = to_streamed_response_wrapper(
            details.tuple,
        )


class AsyncDetailsResourceWithStreamingResponse:
    def __init__(self, details: AsyncDetailsResource) -> None:
        self._details = details

        self.create = async_to_streamed_response_wrapper(
            details.create,
        )
        self.update = async_to_streamed_response_wrapper(
            details.update,
        )
        self.list = async_to_streamed_response_wrapper(
            details.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            details.delete,
        )
        self.count = async_to_streamed_response_wrapper(
            details.count,
        )
        self.get = async_to_streamed_response_wrapper(
            details.get,
        )
        self.queryhelp = async_to_streamed_response_wrapper(
            details.queryhelp,
        )
        self.tuple = async_to_streamed_response_wrapper(
            details.tuple,
        )
