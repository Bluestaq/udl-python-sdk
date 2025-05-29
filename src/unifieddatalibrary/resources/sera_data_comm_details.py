# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import (
    sera_data_comm_detail_get_params,
    sera_data_comm_detail_list_params,
    sera_data_comm_detail_count_params,
    sera_data_comm_detail_tuple_params,
    sera_data_comm_detail_create_params,
    sera_data_comm_detail_update_params,
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
from ..pagination import SyncOffsetPage, AsyncOffsetPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.sera_data_comm_detail_get_response import SeraDataCommDetailGetResponse
from ..types.sera_data_comm_detail_list_response import SeraDataCommDetailListResponse
from ..types.sera_data_comm_detail_tuple_response import SeraDataCommDetailTupleResponse
from ..types.sera_data_comm_detail_queryhelp_response import SeraDataCommDetailQueryhelpResponse

__all__ = ["SeraDataCommDetailsResource", "AsyncSeraDataCommDetailsResource"]


class SeraDataCommDetailsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SeraDataCommDetailsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return SeraDataCommDetailsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SeraDataCommDetailsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return SeraDataCommDetailsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        source: str,
        id: str | NotGiven = NOT_GIVEN,
        band: str | NotGiven = NOT_GIVEN,
        bandwidth: float | NotGiven = NOT_GIVEN,
        eirp: float | NotGiven = NOT_GIVEN,
        est_hts_total_capacity: float | NotGiven = NOT_GIVEN,
        est_hts_total_user_downlink_bandwidth_per_beam: float | NotGiven = NOT_GIVEN,
        est_hts_total_user_uplink_bandwidth_per_beam: float | NotGiven = NOT_GIVEN,
        gateway_downlink_from: float | NotGiven = NOT_GIVEN,
        gateway_downlink_to: float | NotGiven = NOT_GIVEN,
        gateway_uplink_from: float | NotGiven = NOT_GIVEN,
        gateway_uplink_to: float | NotGiven = NOT_GIVEN,
        hosted_for_company_org_id: str | NotGiven = NOT_GIVEN,
        hts_num_user_spot_beams: int | NotGiven = NOT_GIVEN,
        hts_user_downlink_bandwidth_per_beam: float | NotGiven = NOT_GIVEN,
        hts_user_uplink_bandwidth_per_beam: float | NotGiven = NOT_GIVEN,
        id_comm: str | NotGiven = NOT_GIVEN,
        manufacturer_org_id: str | NotGiven = NOT_GIVEN,
        num36_mhz_equivalent_transponders: int | NotGiven = NOT_GIVEN,
        num_operational_transponders: int | NotGiven = NOT_GIVEN,
        num_spare_transponders: int | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        payload_notes: str | NotGiven = NOT_GIVEN,
        polarization: str | NotGiven = NOT_GIVEN,
        solid_state_power_amp: float | NotGiven = NOT_GIVEN,
        spacecraft_id: str | NotGiven = NOT_GIVEN,
        trade_lease_org_id: str | NotGiven = NOT_GIVEN,
        traveling_wave_tube_amplifier: float | NotGiven = NOT_GIVEN,
        user_downlink_from: float | NotGiven = NOT_GIVEN,
        user_downlink_to: float | NotGiven = NOT_GIVEN,
        user_uplink_from: float | NotGiven = NOT_GIVEN,
        user_uplink_to: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single SeradataCommDetails as a POST body and ingest
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

          source: Source of the data.

          id: Unique identifier of the record, auto-generated by the system.

          band: Name of the band of this RF range (e.g.
              X,K,Ku,Ka,L,S,C,UHF,VHF,EHF,SHF,UNK,VLF,HF,E,Q,V,W). See RFBandType for more
              details and descriptions of each band name.

          bandwidth: Comm bandwidth in Mhz.

          eirp: Effective isotropic radiated power in dB.

          est_hts_total_capacity: Comm estimated HtsTotalCapacity in Gbps.

          est_hts_total_user_downlink_bandwidth_per_beam: Comm estimated HtsTotalUserDownlinkBandwidthPerBeam in Mhz.

          est_hts_total_user_uplink_bandwidth_per_beam: Comm estimated HtsTotalUserUplinkBandwidthPerBeam in Mhz.

          gateway_downlink_from: Comm gatewayDownlinkFrom in Ghz.

          gateway_downlink_to: Comm gatewayDownlinkTo in Ghz.

          gateway_uplink_from: Comm gatewayUplinkFrom in Ghz.

          gateway_uplink_to: Comm gatewayUplinkTo in Ghz.

          hosted_for_company_org_id: Comm hostedForCompanyOrgId.

          hts_num_user_spot_beams: Comm htsNumUserSpotBeams.

          hts_user_downlink_bandwidth_per_beam: Comm htsUserDownlinkBandwidthPerBeam in Mhz.

          hts_user_uplink_bandwidth_per_beam: Comm htsUserUplinkBandwidthPerBeam in Mhz.

          id_comm: UUID of the parent Comm record.

          manufacturer_org_id: Comm manufacturerOrgId.

          num36_mhz_equivalent_transponders: Comm num36MhzEquivalentTransponders.

          num_operational_transponders: Comm numOperationalTransponders.

          num_spare_transponders: Comm numSpareTransponders.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          payload_notes: Payload notes.

          polarization: Comm polarization.

          solid_state_power_amp: Solid state power amplifier, in Watts.

          spacecraft_id: Seradata ID of the spacecraft (SeradataSpacecraftDetails ID).

          trade_lease_org_id: Comm tradeLeaseOrgId.

          traveling_wave_tube_amplifier: Comm travelingWaveTubeAmplifier in Watts.

          user_downlink_from: Comm userDownlinkFrom in Ghz.

          user_downlink_to: Comm userDownlinkTo in Ghz.

          user_uplink_from: Comm userUplinkFrom in Ghz.

          user_uplink_to: Comm userUplinkTo in Ghz.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/udl/seradatacommdetails",
            body=maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "source": source,
                    "id": id,
                    "band": band,
                    "bandwidth": bandwidth,
                    "eirp": eirp,
                    "est_hts_total_capacity": est_hts_total_capacity,
                    "est_hts_total_user_downlink_bandwidth_per_beam": est_hts_total_user_downlink_bandwidth_per_beam,
                    "est_hts_total_user_uplink_bandwidth_per_beam": est_hts_total_user_uplink_bandwidth_per_beam,
                    "gateway_downlink_from": gateway_downlink_from,
                    "gateway_downlink_to": gateway_downlink_to,
                    "gateway_uplink_from": gateway_uplink_from,
                    "gateway_uplink_to": gateway_uplink_to,
                    "hosted_for_company_org_id": hosted_for_company_org_id,
                    "hts_num_user_spot_beams": hts_num_user_spot_beams,
                    "hts_user_downlink_bandwidth_per_beam": hts_user_downlink_bandwidth_per_beam,
                    "hts_user_uplink_bandwidth_per_beam": hts_user_uplink_bandwidth_per_beam,
                    "id_comm": id_comm,
                    "manufacturer_org_id": manufacturer_org_id,
                    "num36_mhz_equivalent_transponders": num36_mhz_equivalent_transponders,
                    "num_operational_transponders": num_operational_transponders,
                    "num_spare_transponders": num_spare_transponders,
                    "origin": origin,
                    "payload_notes": payload_notes,
                    "polarization": polarization,
                    "solid_state_power_amp": solid_state_power_amp,
                    "spacecraft_id": spacecraft_id,
                    "trade_lease_org_id": trade_lease_org_id,
                    "traveling_wave_tube_amplifier": traveling_wave_tube_amplifier,
                    "user_downlink_from": user_downlink_from,
                    "user_downlink_to": user_downlink_to,
                    "user_uplink_from": user_uplink_from,
                    "user_uplink_to": user_uplink_to,
                },
                sera_data_comm_detail_create_params.SeraDataCommDetailCreateParams,
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
        source: str,
        body_id: str | NotGiven = NOT_GIVEN,
        band: str | NotGiven = NOT_GIVEN,
        bandwidth: float | NotGiven = NOT_GIVEN,
        eirp: float | NotGiven = NOT_GIVEN,
        est_hts_total_capacity: float | NotGiven = NOT_GIVEN,
        est_hts_total_user_downlink_bandwidth_per_beam: float | NotGiven = NOT_GIVEN,
        est_hts_total_user_uplink_bandwidth_per_beam: float | NotGiven = NOT_GIVEN,
        gateway_downlink_from: float | NotGiven = NOT_GIVEN,
        gateway_downlink_to: float | NotGiven = NOT_GIVEN,
        gateway_uplink_from: float | NotGiven = NOT_GIVEN,
        gateway_uplink_to: float | NotGiven = NOT_GIVEN,
        hosted_for_company_org_id: str | NotGiven = NOT_GIVEN,
        hts_num_user_spot_beams: int | NotGiven = NOT_GIVEN,
        hts_user_downlink_bandwidth_per_beam: float | NotGiven = NOT_GIVEN,
        hts_user_uplink_bandwidth_per_beam: float | NotGiven = NOT_GIVEN,
        id_comm: str | NotGiven = NOT_GIVEN,
        manufacturer_org_id: str | NotGiven = NOT_GIVEN,
        num36_mhz_equivalent_transponders: int | NotGiven = NOT_GIVEN,
        num_operational_transponders: int | NotGiven = NOT_GIVEN,
        num_spare_transponders: int | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        payload_notes: str | NotGiven = NOT_GIVEN,
        polarization: str | NotGiven = NOT_GIVEN,
        solid_state_power_amp: float | NotGiven = NOT_GIVEN,
        spacecraft_id: str | NotGiven = NOT_GIVEN,
        trade_lease_org_id: str | NotGiven = NOT_GIVEN,
        traveling_wave_tube_amplifier: float | NotGiven = NOT_GIVEN,
        user_downlink_from: float | NotGiven = NOT_GIVEN,
        user_downlink_to: float | NotGiven = NOT_GIVEN,
        user_uplink_from: float | NotGiven = NOT_GIVEN,
        user_uplink_to: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Service operation to update an SeradataCommDetails.

        A specific role is required
        to perform this service operation. Please contact the UDL team for assistance.

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

          source: Source of the data.

          body_id: Unique identifier of the record, auto-generated by the system.

          band: Name of the band of this RF range (e.g.
              X,K,Ku,Ka,L,S,C,UHF,VHF,EHF,SHF,UNK,VLF,HF,E,Q,V,W). See RFBandType for more
              details and descriptions of each band name.

          bandwidth: Comm bandwidth in Mhz.

          eirp: Effective isotropic radiated power in dB.

          est_hts_total_capacity: Comm estimated HtsTotalCapacity in Gbps.

          est_hts_total_user_downlink_bandwidth_per_beam: Comm estimated HtsTotalUserDownlinkBandwidthPerBeam in Mhz.

          est_hts_total_user_uplink_bandwidth_per_beam: Comm estimated HtsTotalUserUplinkBandwidthPerBeam in Mhz.

          gateway_downlink_from: Comm gatewayDownlinkFrom in Ghz.

          gateway_downlink_to: Comm gatewayDownlinkTo in Ghz.

          gateway_uplink_from: Comm gatewayUplinkFrom in Ghz.

          gateway_uplink_to: Comm gatewayUplinkTo in Ghz.

          hosted_for_company_org_id: Comm hostedForCompanyOrgId.

          hts_num_user_spot_beams: Comm htsNumUserSpotBeams.

          hts_user_downlink_bandwidth_per_beam: Comm htsUserDownlinkBandwidthPerBeam in Mhz.

          hts_user_uplink_bandwidth_per_beam: Comm htsUserUplinkBandwidthPerBeam in Mhz.

          id_comm: UUID of the parent Comm record.

          manufacturer_org_id: Comm manufacturerOrgId.

          num36_mhz_equivalent_transponders: Comm num36MhzEquivalentTransponders.

          num_operational_transponders: Comm numOperationalTransponders.

          num_spare_transponders: Comm numSpareTransponders.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          payload_notes: Payload notes.

          polarization: Comm polarization.

          solid_state_power_amp: Solid state power amplifier, in Watts.

          spacecraft_id: Seradata ID of the spacecraft (SeradataSpacecraftDetails ID).

          trade_lease_org_id: Comm tradeLeaseOrgId.

          traveling_wave_tube_amplifier: Comm travelingWaveTubeAmplifier in Watts.

          user_downlink_from: Comm userDownlinkFrom in Ghz.

          user_downlink_to: Comm userDownlinkTo in Ghz.

          user_uplink_from: Comm userUplinkFrom in Ghz.

          user_uplink_to: Comm userUplinkTo in Ghz.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            f"/udl/seradatacommdetails/{path_id}",
            body=maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "source": source,
                    "body_id": body_id,
                    "band": band,
                    "bandwidth": bandwidth,
                    "eirp": eirp,
                    "est_hts_total_capacity": est_hts_total_capacity,
                    "est_hts_total_user_downlink_bandwidth_per_beam": est_hts_total_user_downlink_bandwidth_per_beam,
                    "est_hts_total_user_uplink_bandwidth_per_beam": est_hts_total_user_uplink_bandwidth_per_beam,
                    "gateway_downlink_from": gateway_downlink_from,
                    "gateway_downlink_to": gateway_downlink_to,
                    "gateway_uplink_from": gateway_uplink_from,
                    "gateway_uplink_to": gateway_uplink_to,
                    "hosted_for_company_org_id": hosted_for_company_org_id,
                    "hts_num_user_spot_beams": hts_num_user_spot_beams,
                    "hts_user_downlink_bandwidth_per_beam": hts_user_downlink_bandwidth_per_beam,
                    "hts_user_uplink_bandwidth_per_beam": hts_user_uplink_bandwidth_per_beam,
                    "id_comm": id_comm,
                    "manufacturer_org_id": manufacturer_org_id,
                    "num36_mhz_equivalent_transponders": num36_mhz_equivalent_transponders,
                    "num_operational_transponders": num_operational_transponders,
                    "num_spare_transponders": num_spare_transponders,
                    "origin": origin,
                    "payload_notes": payload_notes,
                    "polarization": polarization,
                    "solid_state_power_amp": solid_state_power_amp,
                    "spacecraft_id": spacecraft_id,
                    "trade_lease_org_id": trade_lease_org_id,
                    "traveling_wave_tube_amplifier": traveling_wave_tube_amplifier,
                    "user_downlink_from": user_downlink_from,
                    "user_downlink_to": user_downlink_to,
                    "user_uplink_from": user_uplink_from,
                    "user_uplink_to": user_uplink_to,
                },
                sera_data_comm_detail_update_params.SeraDataCommDetailUpdateParams,
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
    ) -> SyncOffsetPage[SeraDataCommDetailListResponse]:
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
            "/udl/seradatacommdetails",
            page=SyncOffsetPage[SeraDataCommDetailListResponse],
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
                    sera_data_comm_detail_list_params.SeraDataCommDetailListParams,
                ),
            ),
            model=SeraDataCommDetailListResponse,
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
        Service operation to delete an SeradataCommDetails specified by the passed ID
        path parameter. A specific role is required to perform this service operation.
        Please contact the UDL team for assistance.

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
            f"/udl/seradatacommdetails/{id}",
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
            "/udl/seradatacommdetails/count",
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
                    sera_data_comm_detail_count_params.SeraDataCommDetailCountParams,
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
    ) -> SeraDataCommDetailGetResponse:
        """
        Service operation to get a single SeradataCommDetails by its unique ID passed as
        a path parameter.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/udl/seradatacommdetails/{id}",
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
                    sera_data_comm_detail_get_params.SeraDataCommDetailGetParams,
                ),
            ),
            cast_to=SeraDataCommDetailGetResponse,
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
    ) -> SeraDataCommDetailQueryhelpResponse:
        """
        Service operation to provide detailed information on available dynamic query
        parameters for a particular data type.
        """
        return self._get(
            "/udl/seradatacommdetails/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SeraDataCommDetailQueryhelpResponse,
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
    ) -> SeraDataCommDetailTupleResponse:
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
            "/udl/seradatacommdetails/tuple",
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
                    sera_data_comm_detail_tuple_params.SeraDataCommDetailTupleParams,
                ),
            ),
            cast_to=SeraDataCommDetailTupleResponse,
        )


class AsyncSeraDataCommDetailsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSeraDataCommDetailsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncSeraDataCommDetailsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSeraDataCommDetailsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncSeraDataCommDetailsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        source: str,
        id: str | NotGiven = NOT_GIVEN,
        band: str | NotGiven = NOT_GIVEN,
        bandwidth: float | NotGiven = NOT_GIVEN,
        eirp: float | NotGiven = NOT_GIVEN,
        est_hts_total_capacity: float | NotGiven = NOT_GIVEN,
        est_hts_total_user_downlink_bandwidth_per_beam: float | NotGiven = NOT_GIVEN,
        est_hts_total_user_uplink_bandwidth_per_beam: float | NotGiven = NOT_GIVEN,
        gateway_downlink_from: float | NotGiven = NOT_GIVEN,
        gateway_downlink_to: float | NotGiven = NOT_GIVEN,
        gateway_uplink_from: float | NotGiven = NOT_GIVEN,
        gateway_uplink_to: float | NotGiven = NOT_GIVEN,
        hosted_for_company_org_id: str | NotGiven = NOT_GIVEN,
        hts_num_user_spot_beams: int | NotGiven = NOT_GIVEN,
        hts_user_downlink_bandwidth_per_beam: float | NotGiven = NOT_GIVEN,
        hts_user_uplink_bandwidth_per_beam: float | NotGiven = NOT_GIVEN,
        id_comm: str | NotGiven = NOT_GIVEN,
        manufacturer_org_id: str | NotGiven = NOT_GIVEN,
        num36_mhz_equivalent_transponders: int | NotGiven = NOT_GIVEN,
        num_operational_transponders: int | NotGiven = NOT_GIVEN,
        num_spare_transponders: int | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        payload_notes: str | NotGiven = NOT_GIVEN,
        polarization: str | NotGiven = NOT_GIVEN,
        solid_state_power_amp: float | NotGiven = NOT_GIVEN,
        spacecraft_id: str | NotGiven = NOT_GIVEN,
        trade_lease_org_id: str | NotGiven = NOT_GIVEN,
        traveling_wave_tube_amplifier: float | NotGiven = NOT_GIVEN,
        user_downlink_from: float | NotGiven = NOT_GIVEN,
        user_downlink_to: float | NotGiven = NOT_GIVEN,
        user_uplink_from: float | NotGiven = NOT_GIVEN,
        user_uplink_to: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single SeradataCommDetails as a POST body and ingest
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

          source: Source of the data.

          id: Unique identifier of the record, auto-generated by the system.

          band: Name of the band of this RF range (e.g.
              X,K,Ku,Ka,L,S,C,UHF,VHF,EHF,SHF,UNK,VLF,HF,E,Q,V,W). See RFBandType for more
              details and descriptions of each band name.

          bandwidth: Comm bandwidth in Mhz.

          eirp: Effective isotropic radiated power in dB.

          est_hts_total_capacity: Comm estimated HtsTotalCapacity in Gbps.

          est_hts_total_user_downlink_bandwidth_per_beam: Comm estimated HtsTotalUserDownlinkBandwidthPerBeam in Mhz.

          est_hts_total_user_uplink_bandwidth_per_beam: Comm estimated HtsTotalUserUplinkBandwidthPerBeam in Mhz.

          gateway_downlink_from: Comm gatewayDownlinkFrom in Ghz.

          gateway_downlink_to: Comm gatewayDownlinkTo in Ghz.

          gateway_uplink_from: Comm gatewayUplinkFrom in Ghz.

          gateway_uplink_to: Comm gatewayUplinkTo in Ghz.

          hosted_for_company_org_id: Comm hostedForCompanyOrgId.

          hts_num_user_spot_beams: Comm htsNumUserSpotBeams.

          hts_user_downlink_bandwidth_per_beam: Comm htsUserDownlinkBandwidthPerBeam in Mhz.

          hts_user_uplink_bandwidth_per_beam: Comm htsUserUplinkBandwidthPerBeam in Mhz.

          id_comm: UUID of the parent Comm record.

          manufacturer_org_id: Comm manufacturerOrgId.

          num36_mhz_equivalent_transponders: Comm num36MhzEquivalentTransponders.

          num_operational_transponders: Comm numOperationalTransponders.

          num_spare_transponders: Comm numSpareTransponders.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          payload_notes: Payload notes.

          polarization: Comm polarization.

          solid_state_power_amp: Solid state power amplifier, in Watts.

          spacecraft_id: Seradata ID of the spacecraft (SeradataSpacecraftDetails ID).

          trade_lease_org_id: Comm tradeLeaseOrgId.

          traveling_wave_tube_amplifier: Comm travelingWaveTubeAmplifier in Watts.

          user_downlink_from: Comm userDownlinkFrom in Ghz.

          user_downlink_to: Comm userDownlinkTo in Ghz.

          user_uplink_from: Comm userUplinkFrom in Ghz.

          user_uplink_to: Comm userUplinkTo in Ghz.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/udl/seradatacommdetails",
            body=await async_maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "source": source,
                    "id": id,
                    "band": band,
                    "bandwidth": bandwidth,
                    "eirp": eirp,
                    "est_hts_total_capacity": est_hts_total_capacity,
                    "est_hts_total_user_downlink_bandwidth_per_beam": est_hts_total_user_downlink_bandwidth_per_beam,
                    "est_hts_total_user_uplink_bandwidth_per_beam": est_hts_total_user_uplink_bandwidth_per_beam,
                    "gateway_downlink_from": gateway_downlink_from,
                    "gateway_downlink_to": gateway_downlink_to,
                    "gateway_uplink_from": gateway_uplink_from,
                    "gateway_uplink_to": gateway_uplink_to,
                    "hosted_for_company_org_id": hosted_for_company_org_id,
                    "hts_num_user_spot_beams": hts_num_user_spot_beams,
                    "hts_user_downlink_bandwidth_per_beam": hts_user_downlink_bandwidth_per_beam,
                    "hts_user_uplink_bandwidth_per_beam": hts_user_uplink_bandwidth_per_beam,
                    "id_comm": id_comm,
                    "manufacturer_org_id": manufacturer_org_id,
                    "num36_mhz_equivalent_transponders": num36_mhz_equivalent_transponders,
                    "num_operational_transponders": num_operational_transponders,
                    "num_spare_transponders": num_spare_transponders,
                    "origin": origin,
                    "payload_notes": payload_notes,
                    "polarization": polarization,
                    "solid_state_power_amp": solid_state_power_amp,
                    "spacecraft_id": spacecraft_id,
                    "trade_lease_org_id": trade_lease_org_id,
                    "traveling_wave_tube_amplifier": traveling_wave_tube_amplifier,
                    "user_downlink_from": user_downlink_from,
                    "user_downlink_to": user_downlink_to,
                    "user_uplink_from": user_uplink_from,
                    "user_uplink_to": user_uplink_to,
                },
                sera_data_comm_detail_create_params.SeraDataCommDetailCreateParams,
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
        source: str,
        body_id: str | NotGiven = NOT_GIVEN,
        band: str | NotGiven = NOT_GIVEN,
        bandwidth: float | NotGiven = NOT_GIVEN,
        eirp: float | NotGiven = NOT_GIVEN,
        est_hts_total_capacity: float | NotGiven = NOT_GIVEN,
        est_hts_total_user_downlink_bandwidth_per_beam: float | NotGiven = NOT_GIVEN,
        est_hts_total_user_uplink_bandwidth_per_beam: float | NotGiven = NOT_GIVEN,
        gateway_downlink_from: float | NotGiven = NOT_GIVEN,
        gateway_downlink_to: float | NotGiven = NOT_GIVEN,
        gateway_uplink_from: float | NotGiven = NOT_GIVEN,
        gateway_uplink_to: float | NotGiven = NOT_GIVEN,
        hosted_for_company_org_id: str | NotGiven = NOT_GIVEN,
        hts_num_user_spot_beams: int | NotGiven = NOT_GIVEN,
        hts_user_downlink_bandwidth_per_beam: float | NotGiven = NOT_GIVEN,
        hts_user_uplink_bandwidth_per_beam: float | NotGiven = NOT_GIVEN,
        id_comm: str | NotGiven = NOT_GIVEN,
        manufacturer_org_id: str | NotGiven = NOT_GIVEN,
        num36_mhz_equivalent_transponders: int | NotGiven = NOT_GIVEN,
        num_operational_transponders: int | NotGiven = NOT_GIVEN,
        num_spare_transponders: int | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        payload_notes: str | NotGiven = NOT_GIVEN,
        polarization: str | NotGiven = NOT_GIVEN,
        solid_state_power_amp: float | NotGiven = NOT_GIVEN,
        spacecraft_id: str | NotGiven = NOT_GIVEN,
        trade_lease_org_id: str | NotGiven = NOT_GIVEN,
        traveling_wave_tube_amplifier: float | NotGiven = NOT_GIVEN,
        user_downlink_from: float | NotGiven = NOT_GIVEN,
        user_downlink_to: float | NotGiven = NOT_GIVEN,
        user_uplink_from: float | NotGiven = NOT_GIVEN,
        user_uplink_to: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Service operation to update an SeradataCommDetails.

        A specific role is required
        to perform this service operation. Please contact the UDL team for assistance.

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

          source: Source of the data.

          body_id: Unique identifier of the record, auto-generated by the system.

          band: Name of the band of this RF range (e.g.
              X,K,Ku,Ka,L,S,C,UHF,VHF,EHF,SHF,UNK,VLF,HF,E,Q,V,W). See RFBandType for more
              details and descriptions of each band name.

          bandwidth: Comm bandwidth in Mhz.

          eirp: Effective isotropic radiated power in dB.

          est_hts_total_capacity: Comm estimated HtsTotalCapacity in Gbps.

          est_hts_total_user_downlink_bandwidth_per_beam: Comm estimated HtsTotalUserDownlinkBandwidthPerBeam in Mhz.

          est_hts_total_user_uplink_bandwidth_per_beam: Comm estimated HtsTotalUserUplinkBandwidthPerBeam in Mhz.

          gateway_downlink_from: Comm gatewayDownlinkFrom in Ghz.

          gateway_downlink_to: Comm gatewayDownlinkTo in Ghz.

          gateway_uplink_from: Comm gatewayUplinkFrom in Ghz.

          gateway_uplink_to: Comm gatewayUplinkTo in Ghz.

          hosted_for_company_org_id: Comm hostedForCompanyOrgId.

          hts_num_user_spot_beams: Comm htsNumUserSpotBeams.

          hts_user_downlink_bandwidth_per_beam: Comm htsUserDownlinkBandwidthPerBeam in Mhz.

          hts_user_uplink_bandwidth_per_beam: Comm htsUserUplinkBandwidthPerBeam in Mhz.

          id_comm: UUID of the parent Comm record.

          manufacturer_org_id: Comm manufacturerOrgId.

          num36_mhz_equivalent_transponders: Comm num36MhzEquivalentTransponders.

          num_operational_transponders: Comm numOperationalTransponders.

          num_spare_transponders: Comm numSpareTransponders.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          payload_notes: Payload notes.

          polarization: Comm polarization.

          solid_state_power_amp: Solid state power amplifier, in Watts.

          spacecraft_id: Seradata ID of the spacecraft (SeradataSpacecraftDetails ID).

          trade_lease_org_id: Comm tradeLeaseOrgId.

          traveling_wave_tube_amplifier: Comm travelingWaveTubeAmplifier in Watts.

          user_downlink_from: Comm userDownlinkFrom in Ghz.

          user_downlink_to: Comm userDownlinkTo in Ghz.

          user_uplink_from: Comm userUplinkFrom in Ghz.

          user_uplink_to: Comm userUplinkTo in Ghz.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            f"/udl/seradatacommdetails/{path_id}",
            body=await async_maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "source": source,
                    "body_id": body_id,
                    "band": band,
                    "bandwidth": bandwidth,
                    "eirp": eirp,
                    "est_hts_total_capacity": est_hts_total_capacity,
                    "est_hts_total_user_downlink_bandwidth_per_beam": est_hts_total_user_downlink_bandwidth_per_beam,
                    "est_hts_total_user_uplink_bandwidth_per_beam": est_hts_total_user_uplink_bandwidth_per_beam,
                    "gateway_downlink_from": gateway_downlink_from,
                    "gateway_downlink_to": gateway_downlink_to,
                    "gateway_uplink_from": gateway_uplink_from,
                    "gateway_uplink_to": gateway_uplink_to,
                    "hosted_for_company_org_id": hosted_for_company_org_id,
                    "hts_num_user_spot_beams": hts_num_user_spot_beams,
                    "hts_user_downlink_bandwidth_per_beam": hts_user_downlink_bandwidth_per_beam,
                    "hts_user_uplink_bandwidth_per_beam": hts_user_uplink_bandwidth_per_beam,
                    "id_comm": id_comm,
                    "manufacturer_org_id": manufacturer_org_id,
                    "num36_mhz_equivalent_transponders": num36_mhz_equivalent_transponders,
                    "num_operational_transponders": num_operational_transponders,
                    "num_spare_transponders": num_spare_transponders,
                    "origin": origin,
                    "payload_notes": payload_notes,
                    "polarization": polarization,
                    "solid_state_power_amp": solid_state_power_amp,
                    "spacecraft_id": spacecraft_id,
                    "trade_lease_org_id": trade_lease_org_id,
                    "traveling_wave_tube_amplifier": traveling_wave_tube_amplifier,
                    "user_downlink_from": user_downlink_from,
                    "user_downlink_to": user_downlink_to,
                    "user_uplink_from": user_uplink_from,
                    "user_uplink_to": user_uplink_to,
                },
                sera_data_comm_detail_update_params.SeraDataCommDetailUpdateParams,
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
    ) -> AsyncPaginator[SeraDataCommDetailListResponse, AsyncOffsetPage[SeraDataCommDetailListResponse]]:
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
            "/udl/seradatacommdetails",
            page=AsyncOffsetPage[SeraDataCommDetailListResponse],
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
                    sera_data_comm_detail_list_params.SeraDataCommDetailListParams,
                ),
            ),
            model=SeraDataCommDetailListResponse,
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
        Service operation to delete an SeradataCommDetails specified by the passed ID
        path parameter. A specific role is required to perform this service operation.
        Please contact the UDL team for assistance.

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
            f"/udl/seradatacommdetails/{id}",
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
            "/udl/seradatacommdetails/count",
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
                    sera_data_comm_detail_count_params.SeraDataCommDetailCountParams,
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
    ) -> SeraDataCommDetailGetResponse:
        """
        Service operation to get a single SeradataCommDetails by its unique ID passed as
        a path parameter.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/udl/seradatacommdetails/{id}",
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
                    sera_data_comm_detail_get_params.SeraDataCommDetailGetParams,
                ),
            ),
            cast_to=SeraDataCommDetailGetResponse,
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
    ) -> SeraDataCommDetailQueryhelpResponse:
        """
        Service operation to provide detailed information on available dynamic query
        parameters for a particular data type.
        """
        return await self._get(
            "/udl/seradatacommdetails/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SeraDataCommDetailQueryhelpResponse,
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
    ) -> SeraDataCommDetailTupleResponse:
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
            "/udl/seradatacommdetails/tuple",
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
                    sera_data_comm_detail_tuple_params.SeraDataCommDetailTupleParams,
                ),
            ),
            cast_to=SeraDataCommDetailTupleResponse,
        )


class SeraDataCommDetailsResourceWithRawResponse:
    def __init__(self, sera_data_comm_details: SeraDataCommDetailsResource) -> None:
        self._sera_data_comm_details = sera_data_comm_details

        self.create = to_raw_response_wrapper(
            sera_data_comm_details.create,
        )
        self.update = to_raw_response_wrapper(
            sera_data_comm_details.update,
        )
        self.list = to_raw_response_wrapper(
            sera_data_comm_details.list,
        )
        self.delete = to_raw_response_wrapper(
            sera_data_comm_details.delete,
        )
        self.count = to_raw_response_wrapper(
            sera_data_comm_details.count,
        )
        self.get = to_raw_response_wrapper(
            sera_data_comm_details.get,
        )
        self.queryhelp = to_raw_response_wrapper(
            sera_data_comm_details.queryhelp,
        )
        self.tuple = to_raw_response_wrapper(
            sera_data_comm_details.tuple,
        )


class AsyncSeraDataCommDetailsResourceWithRawResponse:
    def __init__(self, sera_data_comm_details: AsyncSeraDataCommDetailsResource) -> None:
        self._sera_data_comm_details = sera_data_comm_details

        self.create = async_to_raw_response_wrapper(
            sera_data_comm_details.create,
        )
        self.update = async_to_raw_response_wrapper(
            sera_data_comm_details.update,
        )
        self.list = async_to_raw_response_wrapper(
            sera_data_comm_details.list,
        )
        self.delete = async_to_raw_response_wrapper(
            sera_data_comm_details.delete,
        )
        self.count = async_to_raw_response_wrapper(
            sera_data_comm_details.count,
        )
        self.get = async_to_raw_response_wrapper(
            sera_data_comm_details.get,
        )
        self.queryhelp = async_to_raw_response_wrapper(
            sera_data_comm_details.queryhelp,
        )
        self.tuple = async_to_raw_response_wrapper(
            sera_data_comm_details.tuple,
        )


class SeraDataCommDetailsResourceWithStreamingResponse:
    def __init__(self, sera_data_comm_details: SeraDataCommDetailsResource) -> None:
        self._sera_data_comm_details = sera_data_comm_details

        self.create = to_streamed_response_wrapper(
            sera_data_comm_details.create,
        )
        self.update = to_streamed_response_wrapper(
            sera_data_comm_details.update,
        )
        self.list = to_streamed_response_wrapper(
            sera_data_comm_details.list,
        )
        self.delete = to_streamed_response_wrapper(
            sera_data_comm_details.delete,
        )
        self.count = to_streamed_response_wrapper(
            sera_data_comm_details.count,
        )
        self.get = to_streamed_response_wrapper(
            sera_data_comm_details.get,
        )
        self.queryhelp = to_streamed_response_wrapper(
            sera_data_comm_details.queryhelp,
        )
        self.tuple = to_streamed_response_wrapper(
            sera_data_comm_details.tuple,
        )


class AsyncSeraDataCommDetailsResourceWithStreamingResponse:
    def __init__(self, sera_data_comm_details: AsyncSeraDataCommDetailsResource) -> None:
        self._sera_data_comm_details = sera_data_comm_details

        self.create = async_to_streamed_response_wrapper(
            sera_data_comm_details.create,
        )
        self.update = async_to_streamed_response_wrapper(
            sera_data_comm_details.update,
        )
        self.list = async_to_streamed_response_wrapper(
            sera_data_comm_details.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            sera_data_comm_details.delete,
        )
        self.count = async_to_streamed_response_wrapper(
            sera_data_comm_details.count,
        )
        self.get = async_to_streamed_response_wrapper(
            sera_data_comm_details.get,
        )
        self.queryhelp = async_to_streamed_response_wrapper(
            sera_data_comm_details.queryhelp,
        )
        self.tuple = async_to_streamed_response_wrapper(
            sera_data_comm_details.tuple,
        )
