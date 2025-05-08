# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import (
    surface_get_params,
    surface_list_params,
    surface_count_params,
    surface_tuple_params,
    surface_create_params,
    surface_update_params,
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
from ..types.surface_get_response import SurfaceGetResponse
from ..types.surface_list_response import SurfaceListResponse
from ..types.surface_tuple_response import SurfaceTupleResponse

__all__ = ["SurfaceResource", "AsyncSurfaceResource"]


class SurfaceResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SurfaceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return SurfaceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SurfaceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return SurfaceResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        name: str,
        source: str,
        type: str,
        id: str | NotGiven = NOT_GIVEN,
        alt_site_id: str | NotGiven = NOT_GIVEN,
        condition: str | NotGiven = NOT_GIVEN,
        ddt_wt_kip: float | NotGiven = NOT_GIVEN,
        ddt_wt_kip_mod: float | NotGiven = NOT_GIVEN,
        ddt_wt_kip_mod_note: str | NotGiven = NOT_GIVEN,
        ddt_wt_kn: float | NotGiven = NOT_GIVEN,
        dd_wt_kip: float | NotGiven = NOT_GIVEN,
        dd_wt_kip_mod: float | NotGiven = NOT_GIVEN,
        dd_wt_kip_mod_note: str | NotGiven = NOT_GIVEN,
        dd_wt_kn: float | NotGiven = NOT_GIVEN,
        end_lat: float | NotGiven = NOT_GIVEN,
        end_lon: float | NotGiven = NOT_GIVEN,
        id_site: str | NotGiven = NOT_GIVEN,
        lcn: int | NotGiven = NOT_GIVEN,
        lda_ft: float | NotGiven = NOT_GIVEN,
        lda_m: float | NotGiven = NOT_GIVEN,
        length_ft: float | NotGiven = NOT_GIVEN,
        length_m: float | NotGiven = NOT_GIVEN,
        lighting: bool | NotGiven = NOT_GIVEN,
        lights_aprch: bool | NotGiven = NOT_GIVEN,
        lights_cl: bool | NotGiven = NOT_GIVEN,
        lights_ols: bool | NotGiven = NOT_GIVEN,
        lights_papi: bool | NotGiven = NOT_GIVEN,
        lights_reil: bool | NotGiven = NOT_GIVEN,
        lights_rwy: bool | NotGiven = NOT_GIVEN,
        lights_seqfl: bool | NotGiven = NOT_GIVEN,
        lights_tdzl: bool | NotGiven = NOT_GIVEN,
        lights_unkn: bool | NotGiven = NOT_GIVEN,
        lights_vasi: bool | NotGiven = NOT_GIVEN,
        material: str | NotGiven = NOT_GIVEN,
        obstacle: bool | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        pcn: str | NotGiven = NOT_GIVEN,
        point_reference: str | NotGiven = NOT_GIVEN,
        primary: bool | NotGiven = NOT_GIVEN,
        raw_wbc: str | NotGiven = NOT_GIVEN,
        sbtt_wt_kip: float | NotGiven = NOT_GIVEN,
        sbtt_wt_kip_mod: float | NotGiven = NOT_GIVEN,
        sbtt_wt_kip_mod_note: str | NotGiven = NOT_GIVEN,
        sbtt_wt_kn: float | NotGiven = NOT_GIVEN,
        start_lat: float | NotGiven = NOT_GIVEN,
        start_lon: float | NotGiven = NOT_GIVEN,
        st_wt_kip: float | NotGiven = NOT_GIVEN,
        st_wt_kip_mod: float | NotGiven = NOT_GIVEN,
        st_wt_kip_mod_note: str | NotGiven = NOT_GIVEN,
        st_wt_kn: float | NotGiven = NOT_GIVEN,
        s_wt_kip: float | NotGiven = NOT_GIVEN,
        s_wt_kip_mod: float | NotGiven = NOT_GIVEN,
        s_wt_kip_mod_note: str | NotGiven = NOT_GIVEN,
        s_wt_kn: float | NotGiven = NOT_GIVEN,
        tdt_wtkip: float | NotGiven = NOT_GIVEN,
        tdt_wt_kip_mod: float | NotGiven = NOT_GIVEN,
        tdt_wt_kip_mod_note: str | NotGiven = NOT_GIVEN,
        tdt_wt_kn: float | NotGiven = NOT_GIVEN,
        trt_wt_kip: float | NotGiven = NOT_GIVEN,
        trt_wt_kip_mod: float | NotGiven = NOT_GIVEN,
        trt_wt_kip_mod_note: str | NotGiven = NOT_GIVEN,
        trt_wt_kn: float | NotGiven = NOT_GIVEN,
        tt_wt_kip: float | NotGiven = NOT_GIVEN,
        tt_wt_kip_mod: float | NotGiven = NOT_GIVEN,
        tt_wt_kip_mod_note: str | NotGiven = NOT_GIVEN,
        tt_wt_kn: float | NotGiven = NOT_GIVEN,
        t_wt_kip: float | NotGiven = NOT_GIVEN,
        t_wt_kip_mod: float | NotGiven = NOT_GIVEN,
        t_wt_kip_mod_note: str | NotGiven = NOT_GIVEN,
        t_wt_kn: float | NotGiven = NOT_GIVEN,
        width_ft: float | NotGiven = NOT_GIVEN,
        width_m: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single Surface as a POST body and ingest into the
        database. A specific role is required to perform this service operation. Please
        contact the UDL team for assistance.

        Args:
          classification_marking: Classification marking of the data in IC/CAPCO Portion-marked format.

          data_mode: Indicator of whether the data is REAL, TEST, SIMULATED, or EXERCISE data.

          name: The surface name or identifier.

          source: Source of the data.

          type: The surface type of this record (e.g. RUNWAY, TAXIWAY, PARKING).

          id: Unique identifier of the record, auto-generated by the system.

          alt_site_id: Alternate site identifier provided by the source.

          condition: The surface condition (e.g. GOOD, FAIR, POOR, SERIOUS, FAILED, CLOSED, UNKNOWN).

          ddt_wt_kip: The max weight allowable on this surface type for a DDT-type (double dual
              tandem) landing gear configuration, in kilopounds (kip).Note: The corresponding
              equivalent field is not converted by the UDL and may or may not be supplied by
              the provider. The provider/consumer is responsible for all unit conversions.

          ddt_wt_kip_mod: The modified max weight allowable on this surface type for a DDT-type (double
              dual tandem) landing gear configuration, in kilopounds (kip).

          ddt_wt_kip_mod_note: User input rationale for the manual modification of the prescribed value
              indicating the max weight allowable on this surface for a DDT-type (double dual
              tandem) landing gear configuration. For more information, contact the provider
              source.

          ddt_wt_kn: The max weight allowable on this surface type for a DDT-type (double dual
              tandem) landing gear configuration, in kilonewtons (kN).Note: The corresponding
              equivalent field is not converted by the UDL and may or may not be supplied by
              the provider. The provider/consumer is responsible for all unit conversions.

          dd_wt_kip: The max weight allowable on this surface type for an FAA 2D-type (twin tandem)
              landing gear configuration, in kilopounds (kip).Note: The corresponding
              equivalent field is not converted by the UDL and may or may not be supplied by
              the provider. The provider/consumer is responsible for all unit conversions.

          dd_wt_kip_mod: The modified max weight allowable on this surface type for an FAA 2D-type (twin
              tandem) landing gear configuration, in kilopounds (kip).

          dd_wt_kip_mod_note: User input rationale for the manual modification of the prescribed value
              indicating the max weight allowable on this surface for an FAA 2D-type (twin
              tandem) landing gear configuration. For more information, contact the provider
              source.

          dd_wt_kn: The max weight allowable on this surface type for an FAA 2D-type (twin tandem)
              landing gear configuration, in kilonewtons (kN).Note: The corresponding
              equivalent field is not converted by the UDL and may or may not be supplied by
              the provider. The provider/consumer is responsible for all unit conversions.

          end_lat: WGS-84 latitude of the coordinate representing the end-point of a surface, in
              degrees. -90 to 90 degrees (negative values south of equator).

          end_lon: WGS-84 longitude of the coordinate representing the end-point of a surface, in
              degrees. -180 to 180 degrees (negative values west of Prime Meridian).

          id_site: The unique identifier of the Site record that contains location information
              about this surface.

          lcn: Load classification number or pavement rating which ranks aircraft on a scale of
              1 to 120.

          lda_ft: The landing distance available for the runway, in feet. Applicable for runway
              surface types only.

          lda_m: The landing distance available for the runway, in meters. Applicable for runway
              surface types only.

          length_ft: The length of the surface type, in feet. Applicable for runway and parking
              surface types.

          length_m: The length of the surface type, in meters. Applicable for runway and parking
              surface types.

          lighting: Flag indicating the surface has lighting.

          lights_aprch: Flag indicating the runway has approach lights. Applicable for runway surface
              types only.

          lights_cl: Flag indicating the runway has centerline lights. Applicable for runway surface
              types only.

          lights_ols: Flag indicating the runway has Optical Landing System (OLS) lights. Applicable
              for runway surface types only.

          lights_papi: Flag indicating the runway has Precision Approach Path Indicator (PAPI) lights.
              Applicable for runway surface types only.

          lights_reil: Flag indicating the runway has Runway End Identifier Lights (REIL). Applicable
              for runway surface types only.

          lights_rwy: Flag indicating the runway has edge lighting. Applicable for runway surface
              types only.

          lights_seqfl: Flag indicating the runway has Sequential Flashing (SEQFL) lights. Applicable
              for runway surface types only.

          lights_tdzl: Flag indicating the runway has Touchdown Zone lights. Applicable for runway
              surface types only.

          lights_unkn: Flag indicating the runway lighting is unknown. Applicable for runway surface
              types only.

          lights_vasi: Flag indicating the runway has Visual Approach Slope Indicator (VASI) lights.
              Applicable for runway surface types only.

          material: The surface material (e.g. Asphalt, Concrete, Dirt).

          obstacle: Flag indicating that one or more obstacles or obstructions exist in the
              proximity of this surface.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          pcn: Pavement classification number (PCN) and tire pressure code.

          point_reference: Description of the surface and its dimensions or how it is measured or oriented.

          primary: Flag indicating this is the primary runway. Applicable for runway surface types
              only.

          raw_wbc: Raw weight bearing capacity value or pavement strength.

          sbtt_wt_kip: The max weight allowable on this surface type for an SBTT-type (single belly
              twin tandem) landing gear configuration, in kilopounds (kip).Note: The
              corresponding equivalent field is not converted by the UDL and may or may not be
              supplied by the provider. The provider/consumer is responsible for all unit
              conversions.

          sbtt_wt_kip_mod: The modified max weight allowable on this surface type for an SBTT-type (single
              belly twin tandem) landing gear configuration, in kilopounds (kip).

          sbtt_wt_kip_mod_note: User input rationale for the manual modification of the prescribed value
              indicating the max weight allowable on this surface for an SBTT-type (single
              belly twin tandem) landing gear configuration. For more information, contact the
              provider source.

          sbtt_wt_kn: The max weight allowable on this surface type for an SBTT-type (single belly
              twin tandem) landing gear configuration, in kilonewtons (kN).Note: The
              corresponding equivalent field is not converted by the UDL and may or may not be
              supplied by the provider. The provider/consumer is responsible for all unit
              conversions.

          start_lat: WGS-84 latitude of the coordinate representing the start-point of a surface, in
              degrees. -90 to 90 degrees (negative values south of equator).

          start_lon: WGS-84 longitude of the coordinate representing the start-point of a surface, in
              degrees. -180 to 180 degrees (negative values west of Prime Meridian).

          st_wt_kip: The max weight allowable on this surface type for an ST-type (single tandem)
              landing gear configuration, in kilopounds (kip).Note: The corresponding
              equivalent field is not converted by the UDL and may or may not be supplied by
              the provider. The provider/consumer is responsible for all unit conversions.

          st_wt_kip_mod: The modified max weight allowable on this surface type for an ST-type (single
              tandem) landing gear configuration, in kilopounds (kip).

          st_wt_kip_mod_note: User input rationale for the manual modification of the prescribed value
              indicating the max weight allowable on this surface for an ST-type (single
              tandem) landing gear configuration. For more information, contact the provider
              source.

          st_wt_kn: The max weight allowable on this surface type for an ST-type (single tandem)
              landing gear configuration, in kilonewtons (kN).Note: The corresponding
              equivalent field is not converted by the UDL and may or may not be supplied by
              the provider. The provider/consumer is responsible for all unit conversions.

          s_wt_kip: The max weight allowable on this surface type for an S-type (single) landing
              gear configuration, in kilopounds (kip). Note: The corresponding equivalent
              field is not converted by the UDL and may or may not be supplied by the
              provider. The provider/consumer is responsible for all unit conversions.

          s_wt_kip_mod: The modified max weight allowable on this surface type for an S-type (single)
              landing gear configuration, in kilopounds (kip).

          s_wt_kip_mod_note: User input rationale for the manual modification of the prescribed value
              indicating the max weight allowable on this surface for an S-type (single)
              landing gear configuration. For more information, contact the provider source.

          s_wt_kn: The max weight allowable on this surface type for an S-type (single) landing
              gear configuration, in kilonewtons (kN).Note: The corresponding equivalent field
              is not converted by the UDL and may or may not be supplied by the provider. The
              provider/consumer is responsible for all unit conversions.

          tdt_wtkip: The max weight allowable on this surface type for a TDT-type (twin delta tandem)
              landing gear configuration, in kilopounds (kip).Note: The corresponding
              equivalent field is not converted by the UDL and may or may not be supplied by
              the provider. The provider/consumer is responsible for all unit conversions.

          tdt_wt_kip_mod: The modified max weight allowable on this surface type for a TDT-type (twin
              delta tandem) landing gear configuration, in kilopounds (kip).

          tdt_wt_kip_mod_note: User input rationale for the manual modification of the prescribed value
              indicating the max weight allowable on this surface for a TDT-type (twin delta
              tandem) landing gear configuration. For more information, contact the provider
              source.

          tdt_wt_kn: The max weight allowable on this surface type for a TDT-type (twin delta tandem)
              landing gear configuration, in kilonewtons (kN).Note: The corresponding
              equivalent field is not converted by the UDL and may or may not be supplied by
              the provider. The provider/consumer is responsible for all unit conversions.

          trt_wt_kip: The max weight allowable on this surface type for a TRT-type (triple tandem)
              landing gear configuration, in kilopounds (kip).Note: The corresponding
              equivalent field is not converted by the UDL and may or may not be supplied by
              the provider. The provider/consumer is responsible for all unit conversions.

          trt_wt_kip_mod: The modified max weight allowable on this surface type for a TRT-type (triple
              tandem) landing gear configuration, in kilopounds (kip).

          trt_wt_kip_mod_note: User input rationale for the manual modification of the prescribed value
              indicating the max weight allowable on this surface for a TRT-type (triple
              tandem) landing gear configuration. For more information, contact the provider
              source.

          trt_wt_kn: The max weight allowable on this surface type for a TRT-type (triple tandem)
              landing gear configuration, in kilonewtons (kN).Note: The corresponding
              equivalent field is not converted by the UDL and may or may not be supplied by
              the provider. The provider/consumer is responsible for all unit conversions.

          tt_wt_kip: The max weight allowable on this surface type for a GDSS TT-type (twin tandem)
              landing gear configuration, in kilopounds (kip).Note: The corresponding
              equivalent field is not converted by the UDL and may or may not be supplied by
              the provider. The provider/consumer is responsible for all unit conversions.

          tt_wt_kip_mod: The modified max weight allowable on this surface type for a GDSS TT-type (twin
              tandem) landing gear configuration, in kilopounds (kip).

          tt_wt_kip_mod_note: User input rationale for the manual modification of the prescribed value
              indicating the max weight allowable on this surface for a GDSS TT-type (twin
              tandem) landing gear configuration. For more information, contact the provider
              source.

          tt_wt_kn: The max weight allowable on this surface type for a GDSS TT-type (twin tandem)
              landing gear configuration, in kilonewtons (kN).Note: The corresponding
              equivalent field is not converted by the UDL and may or may not be supplied by
              the provider. The provider/consumer is responsible for all unit conversions.

          t_wt_kip: The max weight allowable on this surface type for a T-type (twin (dual)) landing
              gear configuration, in kilopounds (kip).Note: The corresponding equivalent field
              is not converted by the UDL and may or may not be supplied by the provider. The
              provider/consumer is responsible for all unit conversions.

          t_wt_kip_mod: The modified max weight allowable on this surface type for a T-type (twin
              (dual)) landing gear configuration, in kilopounds (kip).

          t_wt_kip_mod_note: User input rationale for the manual modification of the prescribed value
              indicating the max weight allowable on this surface for a T-type (twin(dual))
              landing gear configuration. For more information, contact the provider source.

          t_wt_kn: The max weight allowable on this surface type for a T-type (twin (dual)) landing
              gear configuration, in kilonewtons (kN).Note: The corresponding equivalent field
              is not converted by the UDL and may or may not be supplied by the provider. The
              provider/consumer is responsible for all unit conversions.

          width_ft: The width of the surface type, in feet.

          width_m: The width of the surface type, in meters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/udl/surface",
            body=maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "name": name,
                    "source": source,
                    "type": type,
                    "id": id,
                    "alt_site_id": alt_site_id,
                    "condition": condition,
                    "ddt_wt_kip": ddt_wt_kip,
                    "ddt_wt_kip_mod": ddt_wt_kip_mod,
                    "ddt_wt_kip_mod_note": ddt_wt_kip_mod_note,
                    "ddt_wt_kn": ddt_wt_kn,
                    "dd_wt_kip": dd_wt_kip,
                    "dd_wt_kip_mod": dd_wt_kip_mod,
                    "dd_wt_kip_mod_note": dd_wt_kip_mod_note,
                    "dd_wt_kn": dd_wt_kn,
                    "end_lat": end_lat,
                    "end_lon": end_lon,
                    "id_site": id_site,
                    "lcn": lcn,
                    "lda_ft": lda_ft,
                    "lda_m": lda_m,
                    "length_ft": length_ft,
                    "length_m": length_m,
                    "lighting": lighting,
                    "lights_aprch": lights_aprch,
                    "lights_cl": lights_cl,
                    "lights_ols": lights_ols,
                    "lights_papi": lights_papi,
                    "lights_reil": lights_reil,
                    "lights_rwy": lights_rwy,
                    "lights_seqfl": lights_seqfl,
                    "lights_tdzl": lights_tdzl,
                    "lights_unkn": lights_unkn,
                    "lights_vasi": lights_vasi,
                    "material": material,
                    "obstacle": obstacle,
                    "origin": origin,
                    "pcn": pcn,
                    "point_reference": point_reference,
                    "primary": primary,
                    "raw_wbc": raw_wbc,
                    "sbtt_wt_kip": sbtt_wt_kip,
                    "sbtt_wt_kip_mod": sbtt_wt_kip_mod,
                    "sbtt_wt_kip_mod_note": sbtt_wt_kip_mod_note,
                    "sbtt_wt_kn": sbtt_wt_kn,
                    "start_lat": start_lat,
                    "start_lon": start_lon,
                    "st_wt_kip": st_wt_kip,
                    "st_wt_kip_mod": st_wt_kip_mod,
                    "st_wt_kip_mod_note": st_wt_kip_mod_note,
                    "st_wt_kn": st_wt_kn,
                    "s_wt_kip": s_wt_kip,
                    "s_wt_kip_mod": s_wt_kip_mod,
                    "s_wt_kip_mod_note": s_wt_kip_mod_note,
                    "s_wt_kn": s_wt_kn,
                    "tdt_wtkip": tdt_wtkip,
                    "tdt_wt_kip_mod": tdt_wt_kip_mod,
                    "tdt_wt_kip_mod_note": tdt_wt_kip_mod_note,
                    "tdt_wt_kn": tdt_wt_kn,
                    "trt_wt_kip": trt_wt_kip,
                    "trt_wt_kip_mod": trt_wt_kip_mod,
                    "trt_wt_kip_mod_note": trt_wt_kip_mod_note,
                    "trt_wt_kn": trt_wt_kn,
                    "tt_wt_kip": tt_wt_kip,
                    "tt_wt_kip_mod": tt_wt_kip_mod,
                    "tt_wt_kip_mod_note": tt_wt_kip_mod_note,
                    "tt_wt_kn": tt_wt_kn,
                    "t_wt_kip": t_wt_kip,
                    "t_wt_kip_mod": t_wt_kip_mod,
                    "t_wt_kip_mod_note": t_wt_kip_mod_note,
                    "t_wt_kn": t_wt_kn,
                    "width_ft": width_ft,
                    "width_m": width_m,
                },
                surface_create_params.SurfaceCreateParams,
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
        name: str,
        source: str,
        type: str,
        body_id: str | NotGiven = NOT_GIVEN,
        alt_site_id: str | NotGiven = NOT_GIVEN,
        condition: str | NotGiven = NOT_GIVEN,
        ddt_wt_kip: float | NotGiven = NOT_GIVEN,
        ddt_wt_kip_mod: float | NotGiven = NOT_GIVEN,
        ddt_wt_kip_mod_note: str | NotGiven = NOT_GIVEN,
        ddt_wt_kn: float | NotGiven = NOT_GIVEN,
        dd_wt_kip: float | NotGiven = NOT_GIVEN,
        dd_wt_kip_mod: float | NotGiven = NOT_GIVEN,
        dd_wt_kip_mod_note: str | NotGiven = NOT_GIVEN,
        dd_wt_kn: float | NotGiven = NOT_GIVEN,
        end_lat: float | NotGiven = NOT_GIVEN,
        end_lon: float | NotGiven = NOT_GIVEN,
        id_site: str | NotGiven = NOT_GIVEN,
        lcn: int | NotGiven = NOT_GIVEN,
        lda_ft: float | NotGiven = NOT_GIVEN,
        lda_m: float | NotGiven = NOT_GIVEN,
        length_ft: float | NotGiven = NOT_GIVEN,
        length_m: float | NotGiven = NOT_GIVEN,
        lighting: bool | NotGiven = NOT_GIVEN,
        lights_aprch: bool | NotGiven = NOT_GIVEN,
        lights_cl: bool | NotGiven = NOT_GIVEN,
        lights_ols: bool | NotGiven = NOT_GIVEN,
        lights_papi: bool | NotGiven = NOT_GIVEN,
        lights_reil: bool | NotGiven = NOT_GIVEN,
        lights_rwy: bool | NotGiven = NOT_GIVEN,
        lights_seqfl: bool | NotGiven = NOT_GIVEN,
        lights_tdzl: bool | NotGiven = NOT_GIVEN,
        lights_unkn: bool | NotGiven = NOT_GIVEN,
        lights_vasi: bool | NotGiven = NOT_GIVEN,
        material: str | NotGiven = NOT_GIVEN,
        obstacle: bool | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        pcn: str | NotGiven = NOT_GIVEN,
        point_reference: str | NotGiven = NOT_GIVEN,
        primary: bool | NotGiven = NOT_GIVEN,
        raw_wbc: str | NotGiven = NOT_GIVEN,
        sbtt_wt_kip: float | NotGiven = NOT_GIVEN,
        sbtt_wt_kip_mod: float | NotGiven = NOT_GIVEN,
        sbtt_wt_kip_mod_note: str | NotGiven = NOT_GIVEN,
        sbtt_wt_kn: float | NotGiven = NOT_GIVEN,
        start_lat: float | NotGiven = NOT_GIVEN,
        start_lon: float | NotGiven = NOT_GIVEN,
        st_wt_kip: float | NotGiven = NOT_GIVEN,
        st_wt_kip_mod: float | NotGiven = NOT_GIVEN,
        st_wt_kip_mod_note: str | NotGiven = NOT_GIVEN,
        st_wt_kn: float | NotGiven = NOT_GIVEN,
        s_wt_kip: float | NotGiven = NOT_GIVEN,
        s_wt_kip_mod: float | NotGiven = NOT_GIVEN,
        s_wt_kip_mod_note: str | NotGiven = NOT_GIVEN,
        s_wt_kn: float | NotGiven = NOT_GIVEN,
        tdt_wtkip: float | NotGiven = NOT_GIVEN,
        tdt_wt_kip_mod: float | NotGiven = NOT_GIVEN,
        tdt_wt_kip_mod_note: str | NotGiven = NOT_GIVEN,
        tdt_wt_kn: float | NotGiven = NOT_GIVEN,
        trt_wt_kip: float | NotGiven = NOT_GIVEN,
        trt_wt_kip_mod: float | NotGiven = NOT_GIVEN,
        trt_wt_kip_mod_note: str | NotGiven = NOT_GIVEN,
        trt_wt_kn: float | NotGiven = NOT_GIVEN,
        tt_wt_kip: float | NotGiven = NOT_GIVEN,
        tt_wt_kip_mod: float | NotGiven = NOT_GIVEN,
        tt_wt_kip_mod_note: str | NotGiven = NOT_GIVEN,
        tt_wt_kn: float | NotGiven = NOT_GIVEN,
        t_wt_kip: float | NotGiven = NOT_GIVEN,
        t_wt_kip_mod: float | NotGiven = NOT_GIVEN,
        t_wt_kip_mod_note: str | NotGiven = NOT_GIVEN,
        t_wt_kn: float | NotGiven = NOT_GIVEN,
        width_ft: float | NotGiven = NOT_GIVEN,
        width_m: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Service operation to update a single Surface.

        A specific role is required to
        perform this service operation. Please contact the UDL team for assistance.

        Args:
          classification_marking: Classification marking of the data in IC/CAPCO Portion-marked format.

          data_mode: Indicator of whether the data is REAL, TEST, SIMULATED, or EXERCISE data.

          name: The surface name or identifier.

          source: Source of the data.

          type: The surface type of this record (e.g. RUNWAY, TAXIWAY, PARKING).

          body_id: Unique identifier of the record, auto-generated by the system.

          alt_site_id: Alternate site identifier provided by the source.

          condition: The surface condition (e.g. GOOD, FAIR, POOR, SERIOUS, FAILED, CLOSED, UNKNOWN).

          ddt_wt_kip: The max weight allowable on this surface type for a DDT-type (double dual
              tandem) landing gear configuration, in kilopounds (kip).Note: The corresponding
              equivalent field is not converted by the UDL and may or may not be supplied by
              the provider. The provider/consumer is responsible for all unit conversions.

          ddt_wt_kip_mod: The modified max weight allowable on this surface type for a DDT-type (double
              dual tandem) landing gear configuration, in kilopounds (kip).

          ddt_wt_kip_mod_note: User input rationale for the manual modification of the prescribed value
              indicating the max weight allowable on this surface for a DDT-type (double dual
              tandem) landing gear configuration. For more information, contact the provider
              source.

          ddt_wt_kn: The max weight allowable on this surface type for a DDT-type (double dual
              tandem) landing gear configuration, in kilonewtons (kN).Note: The corresponding
              equivalent field is not converted by the UDL and may or may not be supplied by
              the provider. The provider/consumer is responsible for all unit conversions.

          dd_wt_kip: The max weight allowable on this surface type for an FAA 2D-type (twin tandem)
              landing gear configuration, in kilopounds (kip).Note: The corresponding
              equivalent field is not converted by the UDL and may or may not be supplied by
              the provider. The provider/consumer is responsible for all unit conversions.

          dd_wt_kip_mod: The modified max weight allowable on this surface type for an FAA 2D-type (twin
              tandem) landing gear configuration, in kilopounds (kip).

          dd_wt_kip_mod_note: User input rationale for the manual modification of the prescribed value
              indicating the max weight allowable on this surface for an FAA 2D-type (twin
              tandem) landing gear configuration. For more information, contact the provider
              source.

          dd_wt_kn: The max weight allowable on this surface type for an FAA 2D-type (twin tandem)
              landing gear configuration, in kilonewtons (kN).Note: The corresponding
              equivalent field is not converted by the UDL and may or may not be supplied by
              the provider. The provider/consumer is responsible for all unit conversions.

          end_lat: WGS-84 latitude of the coordinate representing the end-point of a surface, in
              degrees. -90 to 90 degrees (negative values south of equator).

          end_lon: WGS-84 longitude of the coordinate representing the end-point of a surface, in
              degrees. -180 to 180 degrees (negative values west of Prime Meridian).

          id_site: The unique identifier of the Site record that contains location information
              about this surface.

          lcn: Load classification number or pavement rating which ranks aircraft on a scale of
              1 to 120.

          lda_ft: The landing distance available for the runway, in feet. Applicable for runway
              surface types only.

          lda_m: The landing distance available for the runway, in meters. Applicable for runway
              surface types only.

          length_ft: The length of the surface type, in feet. Applicable for runway and parking
              surface types.

          length_m: The length of the surface type, in meters. Applicable for runway and parking
              surface types.

          lighting: Flag indicating the surface has lighting.

          lights_aprch: Flag indicating the runway has approach lights. Applicable for runway surface
              types only.

          lights_cl: Flag indicating the runway has centerline lights. Applicable for runway surface
              types only.

          lights_ols: Flag indicating the runway has Optical Landing System (OLS) lights. Applicable
              for runway surface types only.

          lights_papi: Flag indicating the runway has Precision Approach Path Indicator (PAPI) lights.
              Applicable for runway surface types only.

          lights_reil: Flag indicating the runway has Runway End Identifier Lights (REIL). Applicable
              for runway surface types only.

          lights_rwy: Flag indicating the runway has edge lighting. Applicable for runway surface
              types only.

          lights_seqfl: Flag indicating the runway has Sequential Flashing (SEQFL) lights. Applicable
              for runway surface types only.

          lights_tdzl: Flag indicating the runway has Touchdown Zone lights. Applicable for runway
              surface types only.

          lights_unkn: Flag indicating the runway lighting is unknown. Applicable for runway surface
              types only.

          lights_vasi: Flag indicating the runway has Visual Approach Slope Indicator (VASI) lights.
              Applicable for runway surface types only.

          material: The surface material (e.g. Asphalt, Concrete, Dirt).

          obstacle: Flag indicating that one or more obstacles or obstructions exist in the
              proximity of this surface.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          pcn: Pavement classification number (PCN) and tire pressure code.

          point_reference: Description of the surface and its dimensions or how it is measured or oriented.

          primary: Flag indicating this is the primary runway. Applicable for runway surface types
              only.

          raw_wbc: Raw weight bearing capacity value or pavement strength.

          sbtt_wt_kip: The max weight allowable on this surface type for an SBTT-type (single belly
              twin tandem) landing gear configuration, in kilopounds (kip).Note: The
              corresponding equivalent field is not converted by the UDL and may or may not be
              supplied by the provider. The provider/consumer is responsible for all unit
              conversions.

          sbtt_wt_kip_mod: The modified max weight allowable on this surface type for an SBTT-type (single
              belly twin tandem) landing gear configuration, in kilopounds (kip).

          sbtt_wt_kip_mod_note: User input rationale for the manual modification of the prescribed value
              indicating the max weight allowable on this surface for an SBTT-type (single
              belly twin tandem) landing gear configuration. For more information, contact the
              provider source.

          sbtt_wt_kn: The max weight allowable on this surface type for an SBTT-type (single belly
              twin tandem) landing gear configuration, in kilonewtons (kN).Note: The
              corresponding equivalent field is not converted by the UDL and may or may not be
              supplied by the provider. The provider/consumer is responsible for all unit
              conversions.

          start_lat: WGS-84 latitude of the coordinate representing the start-point of a surface, in
              degrees. -90 to 90 degrees (negative values south of equator).

          start_lon: WGS-84 longitude of the coordinate representing the start-point of a surface, in
              degrees. -180 to 180 degrees (negative values west of Prime Meridian).

          st_wt_kip: The max weight allowable on this surface type for an ST-type (single tandem)
              landing gear configuration, in kilopounds (kip).Note: The corresponding
              equivalent field is not converted by the UDL and may or may not be supplied by
              the provider. The provider/consumer is responsible for all unit conversions.

          st_wt_kip_mod: The modified max weight allowable on this surface type for an ST-type (single
              tandem) landing gear configuration, in kilopounds (kip).

          st_wt_kip_mod_note: User input rationale for the manual modification of the prescribed value
              indicating the max weight allowable on this surface for an ST-type (single
              tandem) landing gear configuration. For more information, contact the provider
              source.

          st_wt_kn: The max weight allowable on this surface type for an ST-type (single tandem)
              landing gear configuration, in kilonewtons (kN).Note: The corresponding
              equivalent field is not converted by the UDL and may or may not be supplied by
              the provider. The provider/consumer is responsible for all unit conversions.

          s_wt_kip: The max weight allowable on this surface type for an S-type (single) landing
              gear configuration, in kilopounds (kip). Note: The corresponding equivalent
              field is not converted by the UDL and may or may not be supplied by the
              provider. The provider/consumer is responsible for all unit conversions.

          s_wt_kip_mod: The modified max weight allowable on this surface type for an S-type (single)
              landing gear configuration, in kilopounds (kip).

          s_wt_kip_mod_note: User input rationale for the manual modification of the prescribed value
              indicating the max weight allowable on this surface for an S-type (single)
              landing gear configuration. For more information, contact the provider source.

          s_wt_kn: The max weight allowable on this surface type for an S-type (single) landing
              gear configuration, in kilonewtons (kN).Note: The corresponding equivalent field
              is not converted by the UDL and may or may not be supplied by the provider. The
              provider/consumer is responsible for all unit conversions.

          tdt_wtkip: The max weight allowable on this surface type for a TDT-type (twin delta tandem)
              landing gear configuration, in kilopounds (kip).Note: The corresponding
              equivalent field is not converted by the UDL and may or may not be supplied by
              the provider. The provider/consumer is responsible for all unit conversions.

          tdt_wt_kip_mod: The modified max weight allowable on this surface type for a TDT-type (twin
              delta tandem) landing gear configuration, in kilopounds (kip).

          tdt_wt_kip_mod_note: User input rationale for the manual modification of the prescribed value
              indicating the max weight allowable on this surface for a TDT-type (twin delta
              tandem) landing gear configuration. For more information, contact the provider
              source.

          tdt_wt_kn: The max weight allowable on this surface type for a TDT-type (twin delta tandem)
              landing gear configuration, in kilonewtons (kN).Note: The corresponding
              equivalent field is not converted by the UDL and may or may not be supplied by
              the provider. The provider/consumer is responsible for all unit conversions.

          trt_wt_kip: The max weight allowable on this surface type for a TRT-type (triple tandem)
              landing gear configuration, in kilopounds (kip).Note: The corresponding
              equivalent field is not converted by the UDL and may or may not be supplied by
              the provider. The provider/consumer is responsible for all unit conversions.

          trt_wt_kip_mod: The modified max weight allowable on this surface type for a TRT-type (triple
              tandem) landing gear configuration, in kilopounds (kip).

          trt_wt_kip_mod_note: User input rationale for the manual modification of the prescribed value
              indicating the max weight allowable on this surface for a TRT-type (triple
              tandem) landing gear configuration. For more information, contact the provider
              source.

          trt_wt_kn: The max weight allowable on this surface type for a TRT-type (triple tandem)
              landing gear configuration, in kilonewtons (kN).Note: The corresponding
              equivalent field is not converted by the UDL and may or may not be supplied by
              the provider. The provider/consumer is responsible for all unit conversions.

          tt_wt_kip: The max weight allowable on this surface type for a GDSS TT-type (twin tandem)
              landing gear configuration, in kilopounds (kip).Note: The corresponding
              equivalent field is not converted by the UDL and may or may not be supplied by
              the provider. The provider/consumer is responsible for all unit conversions.

          tt_wt_kip_mod: The modified max weight allowable on this surface type for a GDSS TT-type (twin
              tandem) landing gear configuration, in kilopounds (kip).

          tt_wt_kip_mod_note: User input rationale for the manual modification of the prescribed value
              indicating the max weight allowable on this surface for a GDSS TT-type (twin
              tandem) landing gear configuration. For more information, contact the provider
              source.

          tt_wt_kn: The max weight allowable on this surface type for a GDSS TT-type (twin tandem)
              landing gear configuration, in kilonewtons (kN).Note: The corresponding
              equivalent field is not converted by the UDL and may or may not be supplied by
              the provider. The provider/consumer is responsible for all unit conversions.

          t_wt_kip: The max weight allowable on this surface type for a T-type (twin (dual)) landing
              gear configuration, in kilopounds (kip).Note: The corresponding equivalent field
              is not converted by the UDL and may or may not be supplied by the provider. The
              provider/consumer is responsible for all unit conversions.

          t_wt_kip_mod: The modified max weight allowable on this surface type for a T-type (twin
              (dual)) landing gear configuration, in kilopounds (kip).

          t_wt_kip_mod_note: User input rationale for the manual modification of the prescribed value
              indicating the max weight allowable on this surface for a T-type (twin(dual))
              landing gear configuration. For more information, contact the provider source.

          t_wt_kn: The max weight allowable on this surface type for a T-type (twin (dual)) landing
              gear configuration, in kilonewtons (kN).Note: The corresponding equivalent field
              is not converted by the UDL and may or may not be supplied by the provider. The
              provider/consumer is responsible for all unit conversions.

          width_ft: The width of the surface type, in feet.

          width_m: The width of the surface type, in meters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            f"/udl/surface/{path_id}",
            body=maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "name": name,
                    "source": source,
                    "type": type,
                    "body_id": body_id,
                    "alt_site_id": alt_site_id,
                    "condition": condition,
                    "ddt_wt_kip": ddt_wt_kip,
                    "ddt_wt_kip_mod": ddt_wt_kip_mod,
                    "ddt_wt_kip_mod_note": ddt_wt_kip_mod_note,
                    "ddt_wt_kn": ddt_wt_kn,
                    "dd_wt_kip": dd_wt_kip,
                    "dd_wt_kip_mod": dd_wt_kip_mod,
                    "dd_wt_kip_mod_note": dd_wt_kip_mod_note,
                    "dd_wt_kn": dd_wt_kn,
                    "end_lat": end_lat,
                    "end_lon": end_lon,
                    "id_site": id_site,
                    "lcn": lcn,
                    "lda_ft": lda_ft,
                    "lda_m": lda_m,
                    "length_ft": length_ft,
                    "length_m": length_m,
                    "lighting": lighting,
                    "lights_aprch": lights_aprch,
                    "lights_cl": lights_cl,
                    "lights_ols": lights_ols,
                    "lights_papi": lights_papi,
                    "lights_reil": lights_reil,
                    "lights_rwy": lights_rwy,
                    "lights_seqfl": lights_seqfl,
                    "lights_tdzl": lights_tdzl,
                    "lights_unkn": lights_unkn,
                    "lights_vasi": lights_vasi,
                    "material": material,
                    "obstacle": obstacle,
                    "origin": origin,
                    "pcn": pcn,
                    "point_reference": point_reference,
                    "primary": primary,
                    "raw_wbc": raw_wbc,
                    "sbtt_wt_kip": sbtt_wt_kip,
                    "sbtt_wt_kip_mod": sbtt_wt_kip_mod,
                    "sbtt_wt_kip_mod_note": sbtt_wt_kip_mod_note,
                    "sbtt_wt_kn": sbtt_wt_kn,
                    "start_lat": start_lat,
                    "start_lon": start_lon,
                    "st_wt_kip": st_wt_kip,
                    "st_wt_kip_mod": st_wt_kip_mod,
                    "st_wt_kip_mod_note": st_wt_kip_mod_note,
                    "st_wt_kn": st_wt_kn,
                    "s_wt_kip": s_wt_kip,
                    "s_wt_kip_mod": s_wt_kip_mod,
                    "s_wt_kip_mod_note": s_wt_kip_mod_note,
                    "s_wt_kn": s_wt_kn,
                    "tdt_wtkip": tdt_wtkip,
                    "tdt_wt_kip_mod": tdt_wt_kip_mod,
                    "tdt_wt_kip_mod_note": tdt_wt_kip_mod_note,
                    "tdt_wt_kn": tdt_wt_kn,
                    "trt_wt_kip": trt_wt_kip,
                    "trt_wt_kip_mod": trt_wt_kip_mod,
                    "trt_wt_kip_mod_note": trt_wt_kip_mod_note,
                    "trt_wt_kn": trt_wt_kn,
                    "tt_wt_kip": tt_wt_kip,
                    "tt_wt_kip_mod": tt_wt_kip_mod,
                    "tt_wt_kip_mod_note": tt_wt_kip_mod_note,
                    "tt_wt_kn": tt_wt_kn,
                    "t_wt_kip": t_wt_kip,
                    "t_wt_kip_mod": t_wt_kip_mod,
                    "t_wt_kip_mod_note": t_wt_kip_mod_note,
                    "t_wt_kn": t_wt_kn,
                    "width_ft": width_ft,
                    "width_m": width_m,
                },
                surface_update_params.SurfaceUpdateParams,
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
    ) -> SyncOffsetPage[SurfaceListResponse]:
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
            "/udl/surface",
            page=SyncOffsetPage[SurfaceListResponse],
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
                    surface_list_params.SurfaceListParams,
                ),
            ),
            model=SurfaceListResponse,
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
        Service operation to delete a Surface object specified by the passed ID path
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
            f"/udl/surface/{id}",
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
            "/udl/surface/count",
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
                    surface_count_params.SurfaceCountParams,
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
    ) -> SurfaceGetResponse:
        """
        Service operation to get a single Surface record by its unique ID passed as a
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
            f"/udl/surface/{id}",
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
                    surface_get_params.SurfaceGetParams,
                ),
            ),
            cast_to=SurfaceGetResponse,
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
            "/udl/surface/queryhelp",
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
    ) -> SurfaceTupleResponse:
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
            "/udl/surface/tuple",
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
                    surface_tuple_params.SurfaceTupleParams,
                ),
            ),
            cast_to=SurfaceTupleResponse,
        )


class AsyncSurfaceResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSurfaceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncSurfaceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSurfaceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncSurfaceResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        name: str,
        source: str,
        type: str,
        id: str | NotGiven = NOT_GIVEN,
        alt_site_id: str | NotGiven = NOT_GIVEN,
        condition: str | NotGiven = NOT_GIVEN,
        ddt_wt_kip: float | NotGiven = NOT_GIVEN,
        ddt_wt_kip_mod: float | NotGiven = NOT_GIVEN,
        ddt_wt_kip_mod_note: str | NotGiven = NOT_GIVEN,
        ddt_wt_kn: float | NotGiven = NOT_GIVEN,
        dd_wt_kip: float | NotGiven = NOT_GIVEN,
        dd_wt_kip_mod: float | NotGiven = NOT_GIVEN,
        dd_wt_kip_mod_note: str | NotGiven = NOT_GIVEN,
        dd_wt_kn: float | NotGiven = NOT_GIVEN,
        end_lat: float | NotGiven = NOT_GIVEN,
        end_lon: float | NotGiven = NOT_GIVEN,
        id_site: str | NotGiven = NOT_GIVEN,
        lcn: int | NotGiven = NOT_GIVEN,
        lda_ft: float | NotGiven = NOT_GIVEN,
        lda_m: float | NotGiven = NOT_GIVEN,
        length_ft: float | NotGiven = NOT_GIVEN,
        length_m: float | NotGiven = NOT_GIVEN,
        lighting: bool | NotGiven = NOT_GIVEN,
        lights_aprch: bool | NotGiven = NOT_GIVEN,
        lights_cl: bool | NotGiven = NOT_GIVEN,
        lights_ols: bool | NotGiven = NOT_GIVEN,
        lights_papi: bool | NotGiven = NOT_GIVEN,
        lights_reil: bool | NotGiven = NOT_GIVEN,
        lights_rwy: bool | NotGiven = NOT_GIVEN,
        lights_seqfl: bool | NotGiven = NOT_GIVEN,
        lights_tdzl: bool | NotGiven = NOT_GIVEN,
        lights_unkn: bool | NotGiven = NOT_GIVEN,
        lights_vasi: bool | NotGiven = NOT_GIVEN,
        material: str | NotGiven = NOT_GIVEN,
        obstacle: bool | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        pcn: str | NotGiven = NOT_GIVEN,
        point_reference: str | NotGiven = NOT_GIVEN,
        primary: bool | NotGiven = NOT_GIVEN,
        raw_wbc: str | NotGiven = NOT_GIVEN,
        sbtt_wt_kip: float | NotGiven = NOT_GIVEN,
        sbtt_wt_kip_mod: float | NotGiven = NOT_GIVEN,
        sbtt_wt_kip_mod_note: str | NotGiven = NOT_GIVEN,
        sbtt_wt_kn: float | NotGiven = NOT_GIVEN,
        start_lat: float | NotGiven = NOT_GIVEN,
        start_lon: float | NotGiven = NOT_GIVEN,
        st_wt_kip: float | NotGiven = NOT_GIVEN,
        st_wt_kip_mod: float | NotGiven = NOT_GIVEN,
        st_wt_kip_mod_note: str | NotGiven = NOT_GIVEN,
        st_wt_kn: float | NotGiven = NOT_GIVEN,
        s_wt_kip: float | NotGiven = NOT_GIVEN,
        s_wt_kip_mod: float | NotGiven = NOT_GIVEN,
        s_wt_kip_mod_note: str | NotGiven = NOT_GIVEN,
        s_wt_kn: float | NotGiven = NOT_GIVEN,
        tdt_wtkip: float | NotGiven = NOT_GIVEN,
        tdt_wt_kip_mod: float | NotGiven = NOT_GIVEN,
        tdt_wt_kip_mod_note: str | NotGiven = NOT_GIVEN,
        tdt_wt_kn: float | NotGiven = NOT_GIVEN,
        trt_wt_kip: float | NotGiven = NOT_GIVEN,
        trt_wt_kip_mod: float | NotGiven = NOT_GIVEN,
        trt_wt_kip_mod_note: str | NotGiven = NOT_GIVEN,
        trt_wt_kn: float | NotGiven = NOT_GIVEN,
        tt_wt_kip: float | NotGiven = NOT_GIVEN,
        tt_wt_kip_mod: float | NotGiven = NOT_GIVEN,
        tt_wt_kip_mod_note: str | NotGiven = NOT_GIVEN,
        tt_wt_kn: float | NotGiven = NOT_GIVEN,
        t_wt_kip: float | NotGiven = NOT_GIVEN,
        t_wt_kip_mod: float | NotGiven = NOT_GIVEN,
        t_wt_kip_mod_note: str | NotGiven = NOT_GIVEN,
        t_wt_kn: float | NotGiven = NOT_GIVEN,
        width_ft: float | NotGiven = NOT_GIVEN,
        width_m: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single Surface as a POST body and ingest into the
        database. A specific role is required to perform this service operation. Please
        contact the UDL team for assistance.

        Args:
          classification_marking: Classification marking of the data in IC/CAPCO Portion-marked format.

          data_mode: Indicator of whether the data is REAL, TEST, SIMULATED, or EXERCISE data.

          name: The surface name or identifier.

          source: Source of the data.

          type: The surface type of this record (e.g. RUNWAY, TAXIWAY, PARKING).

          id: Unique identifier of the record, auto-generated by the system.

          alt_site_id: Alternate site identifier provided by the source.

          condition: The surface condition (e.g. GOOD, FAIR, POOR, SERIOUS, FAILED, CLOSED, UNKNOWN).

          ddt_wt_kip: The max weight allowable on this surface type for a DDT-type (double dual
              tandem) landing gear configuration, in kilopounds (kip).Note: The corresponding
              equivalent field is not converted by the UDL and may or may not be supplied by
              the provider. The provider/consumer is responsible for all unit conversions.

          ddt_wt_kip_mod: The modified max weight allowable on this surface type for a DDT-type (double
              dual tandem) landing gear configuration, in kilopounds (kip).

          ddt_wt_kip_mod_note: User input rationale for the manual modification of the prescribed value
              indicating the max weight allowable on this surface for a DDT-type (double dual
              tandem) landing gear configuration. For more information, contact the provider
              source.

          ddt_wt_kn: The max weight allowable on this surface type for a DDT-type (double dual
              tandem) landing gear configuration, in kilonewtons (kN).Note: The corresponding
              equivalent field is not converted by the UDL and may or may not be supplied by
              the provider. The provider/consumer is responsible for all unit conversions.

          dd_wt_kip: The max weight allowable on this surface type for an FAA 2D-type (twin tandem)
              landing gear configuration, in kilopounds (kip).Note: The corresponding
              equivalent field is not converted by the UDL and may or may not be supplied by
              the provider. The provider/consumer is responsible for all unit conversions.

          dd_wt_kip_mod: The modified max weight allowable on this surface type for an FAA 2D-type (twin
              tandem) landing gear configuration, in kilopounds (kip).

          dd_wt_kip_mod_note: User input rationale for the manual modification of the prescribed value
              indicating the max weight allowable on this surface for an FAA 2D-type (twin
              tandem) landing gear configuration. For more information, contact the provider
              source.

          dd_wt_kn: The max weight allowable on this surface type for an FAA 2D-type (twin tandem)
              landing gear configuration, in kilonewtons (kN).Note: The corresponding
              equivalent field is not converted by the UDL and may or may not be supplied by
              the provider. The provider/consumer is responsible for all unit conversions.

          end_lat: WGS-84 latitude of the coordinate representing the end-point of a surface, in
              degrees. -90 to 90 degrees (negative values south of equator).

          end_lon: WGS-84 longitude of the coordinate representing the end-point of a surface, in
              degrees. -180 to 180 degrees (negative values west of Prime Meridian).

          id_site: The unique identifier of the Site record that contains location information
              about this surface.

          lcn: Load classification number or pavement rating which ranks aircraft on a scale of
              1 to 120.

          lda_ft: The landing distance available for the runway, in feet. Applicable for runway
              surface types only.

          lda_m: The landing distance available for the runway, in meters. Applicable for runway
              surface types only.

          length_ft: The length of the surface type, in feet. Applicable for runway and parking
              surface types.

          length_m: The length of the surface type, in meters. Applicable for runway and parking
              surface types.

          lighting: Flag indicating the surface has lighting.

          lights_aprch: Flag indicating the runway has approach lights. Applicable for runway surface
              types only.

          lights_cl: Flag indicating the runway has centerline lights. Applicable for runway surface
              types only.

          lights_ols: Flag indicating the runway has Optical Landing System (OLS) lights. Applicable
              for runway surface types only.

          lights_papi: Flag indicating the runway has Precision Approach Path Indicator (PAPI) lights.
              Applicable for runway surface types only.

          lights_reil: Flag indicating the runway has Runway End Identifier Lights (REIL). Applicable
              for runway surface types only.

          lights_rwy: Flag indicating the runway has edge lighting. Applicable for runway surface
              types only.

          lights_seqfl: Flag indicating the runway has Sequential Flashing (SEQFL) lights. Applicable
              for runway surface types only.

          lights_tdzl: Flag indicating the runway has Touchdown Zone lights. Applicable for runway
              surface types only.

          lights_unkn: Flag indicating the runway lighting is unknown. Applicable for runway surface
              types only.

          lights_vasi: Flag indicating the runway has Visual Approach Slope Indicator (VASI) lights.
              Applicable for runway surface types only.

          material: The surface material (e.g. Asphalt, Concrete, Dirt).

          obstacle: Flag indicating that one or more obstacles or obstructions exist in the
              proximity of this surface.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          pcn: Pavement classification number (PCN) and tire pressure code.

          point_reference: Description of the surface and its dimensions or how it is measured or oriented.

          primary: Flag indicating this is the primary runway. Applicable for runway surface types
              only.

          raw_wbc: Raw weight bearing capacity value or pavement strength.

          sbtt_wt_kip: The max weight allowable on this surface type for an SBTT-type (single belly
              twin tandem) landing gear configuration, in kilopounds (kip).Note: The
              corresponding equivalent field is not converted by the UDL and may or may not be
              supplied by the provider. The provider/consumer is responsible for all unit
              conversions.

          sbtt_wt_kip_mod: The modified max weight allowable on this surface type for an SBTT-type (single
              belly twin tandem) landing gear configuration, in kilopounds (kip).

          sbtt_wt_kip_mod_note: User input rationale for the manual modification of the prescribed value
              indicating the max weight allowable on this surface for an SBTT-type (single
              belly twin tandem) landing gear configuration. For more information, contact the
              provider source.

          sbtt_wt_kn: The max weight allowable on this surface type for an SBTT-type (single belly
              twin tandem) landing gear configuration, in kilonewtons (kN).Note: The
              corresponding equivalent field is not converted by the UDL and may or may not be
              supplied by the provider. The provider/consumer is responsible for all unit
              conversions.

          start_lat: WGS-84 latitude of the coordinate representing the start-point of a surface, in
              degrees. -90 to 90 degrees (negative values south of equator).

          start_lon: WGS-84 longitude of the coordinate representing the start-point of a surface, in
              degrees. -180 to 180 degrees (negative values west of Prime Meridian).

          st_wt_kip: The max weight allowable on this surface type for an ST-type (single tandem)
              landing gear configuration, in kilopounds (kip).Note: The corresponding
              equivalent field is not converted by the UDL and may or may not be supplied by
              the provider. The provider/consumer is responsible for all unit conversions.

          st_wt_kip_mod: The modified max weight allowable on this surface type for an ST-type (single
              tandem) landing gear configuration, in kilopounds (kip).

          st_wt_kip_mod_note: User input rationale for the manual modification of the prescribed value
              indicating the max weight allowable on this surface for an ST-type (single
              tandem) landing gear configuration. For more information, contact the provider
              source.

          st_wt_kn: The max weight allowable on this surface type for an ST-type (single tandem)
              landing gear configuration, in kilonewtons (kN).Note: The corresponding
              equivalent field is not converted by the UDL and may or may not be supplied by
              the provider. The provider/consumer is responsible for all unit conversions.

          s_wt_kip: The max weight allowable on this surface type for an S-type (single) landing
              gear configuration, in kilopounds (kip). Note: The corresponding equivalent
              field is not converted by the UDL and may or may not be supplied by the
              provider. The provider/consumer is responsible for all unit conversions.

          s_wt_kip_mod: The modified max weight allowable on this surface type for an S-type (single)
              landing gear configuration, in kilopounds (kip).

          s_wt_kip_mod_note: User input rationale for the manual modification of the prescribed value
              indicating the max weight allowable on this surface for an S-type (single)
              landing gear configuration. For more information, contact the provider source.

          s_wt_kn: The max weight allowable on this surface type for an S-type (single) landing
              gear configuration, in kilonewtons (kN).Note: The corresponding equivalent field
              is not converted by the UDL and may or may not be supplied by the provider. The
              provider/consumer is responsible for all unit conversions.

          tdt_wtkip: The max weight allowable on this surface type for a TDT-type (twin delta tandem)
              landing gear configuration, in kilopounds (kip).Note: The corresponding
              equivalent field is not converted by the UDL and may or may not be supplied by
              the provider. The provider/consumer is responsible for all unit conversions.

          tdt_wt_kip_mod: The modified max weight allowable on this surface type for a TDT-type (twin
              delta tandem) landing gear configuration, in kilopounds (kip).

          tdt_wt_kip_mod_note: User input rationale for the manual modification of the prescribed value
              indicating the max weight allowable on this surface for a TDT-type (twin delta
              tandem) landing gear configuration. For more information, contact the provider
              source.

          tdt_wt_kn: The max weight allowable on this surface type for a TDT-type (twin delta tandem)
              landing gear configuration, in kilonewtons (kN).Note: The corresponding
              equivalent field is not converted by the UDL and may or may not be supplied by
              the provider. The provider/consumer is responsible for all unit conversions.

          trt_wt_kip: The max weight allowable on this surface type for a TRT-type (triple tandem)
              landing gear configuration, in kilopounds (kip).Note: The corresponding
              equivalent field is not converted by the UDL and may or may not be supplied by
              the provider. The provider/consumer is responsible for all unit conversions.

          trt_wt_kip_mod: The modified max weight allowable on this surface type for a TRT-type (triple
              tandem) landing gear configuration, in kilopounds (kip).

          trt_wt_kip_mod_note: User input rationale for the manual modification of the prescribed value
              indicating the max weight allowable on this surface for a TRT-type (triple
              tandem) landing gear configuration. For more information, contact the provider
              source.

          trt_wt_kn: The max weight allowable on this surface type for a TRT-type (triple tandem)
              landing gear configuration, in kilonewtons (kN).Note: The corresponding
              equivalent field is not converted by the UDL and may or may not be supplied by
              the provider. The provider/consumer is responsible for all unit conversions.

          tt_wt_kip: The max weight allowable on this surface type for a GDSS TT-type (twin tandem)
              landing gear configuration, in kilopounds (kip).Note: The corresponding
              equivalent field is not converted by the UDL and may or may not be supplied by
              the provider. The provider/consumer is responsible for all unit conversions.

          tt_wt_kip_mod: The modified max weight allowable on this surface type for a GDSS TT-type (twin
              tandem) landing gear configuration, in kilopounds (kip).

          tt_wt_kip_mod_note: User input rationale for the manual modification of the prescribed value
              indicating the max weight allowable on this surface for a GDSS TT-type (twin
              tandem) landing gear configuration. For more information, contact the provider
              source.

          tt_wt_kn: The max weight allowable on this surface type for a GDSS TT-type (twin tandem)
              landing gear configuration, in kilonewtons (kN).Note: The corresponding
              equivalent field is not converted by the UDL and may or may not be supplied by
              the provider. The provider/consumer is responsible for all unit conversions.

          t_wt_kip: The max weight allowable on this surface type for a T-type (twin (dual)) landing
              gear configuration, in kilopounds (kip).Note: The corresponding equivalent field
              is not converted by the UDL and may or may not be supplied by the provider. The
              provider/consumer is responsible for all unit conversions.

          t_wt_kip_mod: The modified max weight allowable on this surface type for a T-type (twin
              (dual)) landing gear configuration, in kilopounds (kip).

          t_wt_kip_mod_note: User input rationale for the manual modification of the prescribed value
              indicating the max weight allowable on this surface for a T-type (twin(dual))
              landing gear configuration. For more information, contact the provider source.

          t_wt_kn: The max weight allowable on this surface type for a T-type (twin (dual)) landing
              gear configuration, in kilonewtons (kN).Note: The corresponding equivalent field
              is not converted by the UDL and may or may not be supplied by the provider. The
              provider/consumer is responsible for all unit conversions.

          width_ft: The width of the surface type, in feet.

          width_m: The width of the surface type, in meters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/udl/surface",
            body=await async_maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "name": name,
                    "source": source,
                    "type": type,
                    "id": id,
                    "alt_site_id": alt_site_id,
                    "condition": condition,
                    "ddt_wt_kip": ddt_wt_kip,
                    "ddt_wt_kip_mod": ddt_wt_kip_mod,
                    "ddt_wt_kip_mod_note": ddt_wt_kip_mod_note,
                    "ddt_wt_kn": ddt_wt_kn,
                    "dd_wt_kip": dd_wt_kip,
                    "dd_wt_kip_mod": dd_wt_kip_mod,
                    "dd_wt_kip_mod_note": dd_wt_kip_mod_note,
                    "dd_wt_kn": dd_wt_kn,
                    "end_lat": end_lat,
                    "end_lon": end_lon,
                    "id_site": id_site,
                    "lcn": lcn,
                    "lda_ft": lda_ft,
                    "lda_m": lda_m,
                    "length_ft": length_ft,
                    "length_m": length_m,
                    "lighting": lighting,
                    "lights_aprch": lights_aprch,
                    "lights_cl": lights_cl,
                    "lights_ols": lights_ols,
                    "lights_papi": lights_papi,
                    "lights_reil": lights_reil,
                    "lights_rwy": lights_rwy,
                    "lights_seqfl": lights_seqfl,
                    "lights_tdzl": lights_tdzl,
                    "lights_unkn": lights_unkn,
                    "lights_vasi": lights_vasi,
                    "material": material,
                    "obstacle": obstacle,
                    "origin": origin,
                    "pcn": pcn,
                    "point_reference": point_reference,
                    "primary": primary,
                    "raw_wbc": raw_wbc,
                    "sbtt_wt_kip": sbtt_wt_kip,
                    "sbtt_wt_kip_mod": sbtt_wt_kip_mod,
                    "sbtt_wt_kip_mod_note": sbtt_wt_kip_mod_note,
                    "sbtt_wt_kn": sbtt_wt_kn,
                    "start_lat": start_lat,
                    "start_lon": start_lon,
                    "st_wt_kip": st_wt_kip,
                    "st_wt_kip_mod": st_wt_kip_mod,
                    "st_wt_kip_mod_note": st_wt_kip_mod_note,
                    "st_wt_kn": st_wt_kn,
                    "s_wt_kip": s_wt_kip,
                    "s_wt_kip_mod": s_wt_kip_mod,
                    "s_wt_kip_mod_note": s_wt_kip_mod_note,
                    "s_wt_kn": s_wt_kn,
                    "tdt_wtkip": tdt_wtkip,
                    "tdt_wt_kip_mod": tdt_wt_kip_mod,
                    "tdt_wt_kip_mod_note": tdt_wt_kip_mod_note,
                    "tdt_wt_kn": tdt_wt_kn,
                    "trt_wt_kip": trt_wt_kip,
                    "trt_wt_kip_mod": trt_wt_kip_mod,
                    "trt_wt_kip_mod_note": trt_wt_kip_mod_note,
                    "trt_wt_kn": trt_wt_kn,
                    "tt_wt_kip": tt_wt_kip,
                    "tt_wt_kip_mod": tt_wt_kip_mod,
                    "tt_wt_kip_mod_note": tt_wt_kip_mod_note,
                    "tt_wt_kn": tt_wt_kn,
                    "t_wt_kip": t_wt_kip,
                    "t_wt_kip_mod": t_wt_kip_mod,
                    "t_wt_kip_mod_note": t_wt_kip_mod_note,
                    "t_wt_kn": t_wt_kn,
                    "width_ft": width_ft,
                    "width_m": width_m,
                },
                surface_create_params.SurfaceCreateParams,
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
        name: str,
        source: str,
        type: str,
        body_id: str | NotGiven = NOT_GIVEN,
        alt_site_id: str | NotGiven = NOT_GIVEN,
        condition: str | NotGiven = NOT_GIVEN,
        ddt_wt_kip: float | NotGiven = NOT_GIVEN,
        ddt_wt_kip_mod: float | NotGiven = NOT_GIVEN,
        ddt_wt_kip_mod_note: str | NotGiven = NOT_GIVEN,
        ddt_wt_kn: float | NotGiven = NOT_GIVEN,
        dd_wt_kip: float | NotGiven = NOT_GIVEN,
        dd_wt_kip_mod: float | NotGiven = NOT_GIVEN,
        dd_wt_kip_mod_note: str | NotGiven = NOT_GIVEN,
        dd_wt_kn: float | NotGiven = NOT_GIVEN,
        end_lat: float | NotGiven = NOT_GIVEN,
        end_lon: float | NotGiven = NOT_GIVEN,
        id_site: str | NotGiven = NOT_GIVEN,
        lcn: int | NotGiven = NOT_GIVEN,
        lda_ft: float | NotGiven = NOT_GIVEN,
        lda_m: float | NotGiven = NOT_GIVEN,
        length_ft: float | NotGiven = NOT_GIVEN,
        length_m: float | NotGiven = NOT_GIVEN,
        lighting: bool | NotGiven = NOT_GIVEN,
        lights_aprch: bool | NotGiven = NOT_GIVEN,
        lights_cl: bool | NotGiven = NOT_GIVEN,
        lights_ols: bool | NotGiven = NOT_GIVEN,
        lights_papi: bool | NotGiven = NOT_GIVEN,
        lights_reil: bool | NotGiven = NOT_GIVEN,
        lights_rwy: bool | NotGiven = NOT_GIVEN,
        lights_seqfl: bool | NotGiven = NOT_GIVEN,
        lights_tdzl: bool | NotGiven = NOT_GIVEN,
        lights_unkn: bool | NotGiven = NOT_GIVEN,
        lights_vasi: bool | NotGiven = NOT_GIVEN,
        material: str | NotGiven = NOT_GIVEN,
        obstacle: bool | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        pcn: str | NotGiven = NOT_GIVEN,
        point_reference: str | NotGiven = NOT_GIVEN,
        primary: bool | NotGiven = NOT_GIVEN,
        raw_wbc: str | NotGiven = NOT_GIVEN,
        sbtt_wt_kip: float | NotGiven = NOT_GIVEN,
        sbtt_wt_kip_mod: float | NotGiven = NOT_GIVEN,
        sbtt_wt_kip_mod_note: str | NotGiven = NOT_GIVEN,
        sbtt_wt_kn: float | NotGiven = NOT_GIVEN,
        start_lat: float | NotGiven = NOT_GIVEN,
        start_lon: float | NotGiven = NOT_GIVEN,
        st_wt_kip: float | NotGiven = NOT_GIVEN,
        st_wt_kip_mod: float | NotGiven = NOT_GIVEN,
        st_wt_kip_mod_note: str | NotGiven = NOT_GIVEN,
        st_wt_kn: float | NotGiven = NOT_GIVEN,
        s_wt_kip: float | NotGiven = NOT_GIVEN,
        s_wt_kip_mod: float | NotGiven = NOT_GIVEN,
        s_wt_kip_mod_note: str | NotGiven = NOT_GIVEN,
        s_wt_kn: float | NotGiven = NOT_GIVEN,
        tdt_wtkip: float | NotGiven = NOT_GIVEN,
        tdt_wt_kip_mod: float | NotGiven = NOT_GIVEN,
        tdt_wt_kip_mod_note: str | NotGiven = NOT_GIVEN,
        tdt_wt_kn: float | NotGiven = NOT_GIVEN,
        trt_wt_kip: float | NotGiven = NOT_GIVEN,
        trt_wt_kip_mod: float | NotGiven = NOT_GIVEN,
        trt_wt_kip_mod_note: str | NotGiven = NOT_GIVEN,
        trt_wt_kn: float | NotGiven = NOT_GIVEN,
        tt_wt_kip: float | NotGiven = NOT_GIVEN,
        tt_wt_kip_mod: float | NotGiven = NOT_GIVEN,
        tt_wt_kip_mod_note: str | NotGiven = NOT_GIVEN,
        tt_wt_kn: float | NotGiven = NOT_GIVEN,
        t_wt_kip: float | NotGiven = NOT_GIVEN,
        t_wt_kip_mod: float | NotGiven = NOT_GIVEN,
        t_wt_kip_mod_note: str | NotGiven = NOT_GIVEN,
        t_wt_kn: float | NotGiven = NOT_GIVEN,
        width_ft: float | NotGiven = NOT_GIVEN,
        width_m: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Service operation to update a single Surface.

        A specific role is required to
        perform this service operation. Please contact the UDL team for assistance.

        Args:
          classification_marking: Classification marking of the data in IC/CAPCO Portion-marked format.

          data_mode: Indicator of whether the data is REAL, TEST, SIMULATED, or EXERCISE data.

          name: The surface name or identifier.

          source: Source of the data.

          type: The surface type of this record (e.g. RUNWAY, TAXIWAY, PARKING).

          body_id: Unique identifier of the record, auto-generated by the system.

          alt_site_id: Alternate site identifier provided by the source.

          condition: The surface condition (e.g. GOOD, FAIR, POOR, SERIOUS, FAILED, CLOSED, UNKNOWN).

          ddt_wt_kip: The max weight allowable on this surface type for a DDT-type (double dual
              tandem) landing gear configuration, in kilopounds (kip).Note: The corresponding
              equivalent field is not converted by the UDL and may or may not be supplied by
              the provider. The provider/consumer is responsible for all unit conversions.

          ddt_wt_kip_mod: The modified max weight allowable on this surface type for a DDT-type (double
              dual tandem) landing gear configuration, in kilopounds (kip).

          ddt_wt_kip_mod_note: User input rationale for the manual modification of the prescribed value
              indicating the max weight allowable on this surface for a DDT-type (double dual
              tandem) landing gear configuration. For more information, contact the provider
              source.

          ddt_wt_kn: The max weight allowable on this surface type for a DDT-type (double dual
              tandem) landing gear configuration, in kilonewtons (kN).Note: The corresponding
              equivalent field is not converted by the UDL and may or may not be supplied by
              the provider. The provider/consumer is responsible for all unit conversions.

          dd_wt_kip: The max weight allowable on this surface type for an FAA 2D-type (twin tandem)
              landing gear configuration, in kilopounds (kip).Note: The corresponding
              equivalent field is not converted by the UDL and may or may not be supplied by
              the provider. The provider/consumer is responsible for all unit conversions.

          dd_wt_kip_mod: The modified max weight allowable on this surface type for an FAA 2D-type (twin
              tandem) landing gear configuration, in kilopounds (kip).

          dd_wt_kip_mod_note: User input rationale for the manual modification of the prescribed value
              indicating the max weight allowable on this surface for an FAA 2D-type (twin
              tandem) landing gear configuration. For more information, contact the provider
              source.

          dd_wt_kn: The max weight allowable on this surface type for an FAA 2D-type (twin tandem)
              landing gear configuration, in kilonewtons (kN).Note: The corresponding
              equivalent field is not converted by the UDL and may or may not be supplied by
              the provider. The provider/consumer is responsible for all unit conversions.

          end_lat: WGS-84 latitude of the coordinate representing the end-point of a surface, in
              degrees. -90 to 90 degrees (negative values south of equator).

          end_lon: WGS-84 longitude of the coordinate representing the end-point of a surface, in
              degrees. -180 to 180 degrees (negative values west of Prime Meridian).

          id_site: The unique identifier of the Site record that contains location information
              about this surface.

          lcn: Load classification number or pavement rating which ranks aircraft on a scale of
              1 to 120.

          lda_ft: The landing distance available for the runway, in feet. Applicable for runway
              surface types only.

          lda_m: The landing distance available for the runway, in meters. Applicable for runway
              surface types only.

          length_ft: The length of the surface type, in feet. Applicable for runway and parking
              surface types.

          length_m: The length of the surface type, in meters. Applicable for runway and parking
              surface types.

          lighting: Flag indicating the surface has lighting.

          lights_aprch: Flag indicating the runway has approach lights. Applicable for runway surface
              types only.

          lights_cl: Flag indicating the runway has centerline lights. Applicable for runway surface
              types only.

          lights_ols: Flag indicating the runway has Optical Landing System (OLS) lights. Applicable
              for runway surface types only.

          lights_papi: Flag indicating the runway has Precision Approach Path Indicator (PAPI) lights.
              Applicable for runway surface types only.

          lights_reil: Flag indicating the runway has Runway End Identifier Lights (REIL). Applicable
              for runway surface types only.

          lights_rwy: Flag indicating the runway has edge lighting. Applicable for runway surface
              types only.

          lights_seqfl: Flag indicating the runway has Sequential Flashing (SEQFL) lights. Applicable
              for runway surface types only.

          lights_tdzl: Flag indicating the runway has Touchdown Zone lights. Applicable for runway
              surface types only.

          lights_unkn: Flag indicating the runway lighting is unknown. Applicable for runway surface
              types only.

          lights_vasi: Flag indicating the runway has Visual Approach Slope Indicator (VASI) lights.
              Applicable for runway surface types only.

          material: The surface material (e.g. Asphalt, Concrete, Dirt).

          obstacle: Flag indicating that one or more obstacles or obstructions exist in the
              proximity of this surface.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          pcn: Pavement classification number (PCN) and tire pressure code.

          point_reference: Description of the surface and its dimensions or how it is measured or oriented.

          primary: Flag indicating this is the primary runway. Applicable for runway surface types
              only.

          raw_wbc: Raw weight bearing capacity value or pavement strength.

          sbtt_wt_kip: The max weight allowable on this surface type for an SBTT-type (single belly
              twin tandem) landing gear configuration, in kilopounds (kip).Note: The
              corresponding equivalent field is not converted by the UDL and may or may not be
              supplied by the provider. The provider/consumer is responsible for all unit
              conversions.

          sbtt_wt_kip_mod: The modified max weight allowable on this surface type for an SBTT-type (single
              belly twin tandem) landing gear configuration, in kilopounds (kip).

          sbtt_wt_kip_mod_note: User input rationale for the manual modification of the prescribed value
              indicating the max weight allowable on this surface for an SBTT-type (single
              belly twin tandem) landing gear configuration. For more information, contact the
              provider source.

          sbtt_wt_kn: The max weight allowable on this surface type for an SBTT-type (single belly
              twin tandem) landing gear configuration, in kilonewtons (kN).Note: The
              corresponding equivalent field is not converted by the UDL and may or may not be
              supplied by the provider. The provider/consumer is responsible for all unit
              conversions.

          start_lat: WGS-84 latitude of the coordinate representing the start-point of a surface, in
              degrees. -90 to 90 degrees (negative values south of equator).

          start_lon: WGS-84 longitude of the coordinate representing the start-point of a surface, in
              degrees. -180 to 180 degrees (negative values west of Prime Meridian).

          st_wt_kip: The max weight allowable on this surface type for an ST-type (single tandem)
              landing gear configuration, in kilopounds (kip).Note: The corresponding
              equivalent field is not converted by the UDL and may or may not be supplied by
              the provider. The provider/consumer is responsible for all unit conversions.

          st_wt_kip_mod: The modified max weight allowable on this surface type for an ST-type (single
              tandem) landing gear configuration, in kilopounds (kip).

          st_wt_kip_mod_note: User input rationale for the manual modification of the prescribed value
              indicating the max weight allowable on this surface for an ST-type (single
              tandem) landing gear configuration. For more information, contact the provider
              source.

          st_wt_kn: The max weight allowable on this surface type for an ST-type (single tandem)
              landing gear configuration, in kilonewtons (kN).Note: The corresponding
              equivalent field is not converted by the UDL and may or may not be supplied by
              the provider. The provider/consumer is responsible for all unit conversions.

          s_wt_kip: The max weight allowable on this surface type for an S-type (single) landing
              gear configuration, in kilopounds (kip). Note: The corresponding equivalent
              field is not converted by the UDL and may or may not be supplied by the
              provider. The provider/consumer is responsible for all unit conversions.

          s_wt_kip_mod: The modified max weight allowable on this surface type for an S-type (single)
              landing gear configuration, in kilopounds (kip).

          s_wt_kip_mod_note: User input rationale for the manual modification of the prescribed value
              indicating the max weight allowable on this surface for an S-type (single)
              landing gear configuration. For more information, contact the provider source.

          s_wt_kn: The max weight allowable on this surface type for an S-type (single) landing
              gear configuration, in kilonewtons (kN).Note: The corresponding equivalent field
              is not converted by the UDL and may or may not be supplied by the provider. The
              provider/consumer is responsible for all unit conversions.

          tdt_wtkip: The max weight allowable on this surface type for a TDT-type (twin delta tandem)
              landing gear configuration, in kilopounds (kip).Note: The corresponding
              equivalent field is not converted by the UDL and may or may not be supplied by
              the provider. The provider/consumer is responsible for all unit conversions.

          tdt_wt_kip_mod: The modified max weight allowable on this surface type for a TDT-type (twin
              delta tandem) landing gear configuration, in kilopounds (kip).

          tdt_wt_kip_mod_note: User input rationale for the manual modification of the prescribed value
              indicating the max weight allowable on this surface for a TDT-type (twin delta
              tandem) landing gear configuration. For more information, contact the provider
              source.

          tdt_wt_kn: The max weight allowable on this surface type for a TDT-type (twin delta tandem)
              landing gear configuration, in kilonewtons (kN).Note: The corresponding
              equivalent field is not converted by the UDL and may or may not be supplied by
              the provider. The provider/consumer is responsible for all unit conversions.

          trt_wt_kip: The max weight allowable on this surface type for a TRT-type (triple tandem)
              landing gear configuration, in kilopounds (kip).Note: The corresponding
              equivalent field is not converted by the UDL and may or may not be supplied by
              the provider. The provider/consumer is responsible for all unit conversions.

          trt_wt_kip_mod: The modified max weight allowable on this surface type for a TRT-type (triple
              tandem) landing gear configuration, in kilopounds (kip).

          trt_wt_kip_mod_note: User input rationale for the manual modification of the prescribed value
              indicating the max weight allowable on this surface for a TRT-type (triple
              tandem) landing gear configuration. For more information, contact the provider
              source.

          trt_wt_kn: The max weight allowable on this surface type for a TRT-type (triple tandem)
              landing gear configuration, in kilonewtons (kN).Note: The corresponding
              equivalent field is not converted by the UDL and may or may not be supplied by
              the provider. The provider/consumer is responsible for all unit conversions.

          tt_wt_kip: The max weight allowable on this surface type for a GDSS TT-type (twin tandem)
              landing gear configuration, in kilopounds (kip).Note: The corresponding
              equivalent field is not converted by the UDL and may or may not be supplied by
              the provider. The provider/consumer is responsible for all unit conversions.

          tt_wt_kip_mod: The modified max weight allowable on this surface type for a GDSS TT-type (twin
              tandem) landing gear configuration, in kilopounds (kip).

          tt_wt_kip_mod_note: User input rationale for the manual modification of the prescribed value
              indicating the max weight allowable on this surface for a GDSS TT-type (twin
              tandem) landing gear configuration. For more information, contact the provider
              source.

          tt_wt_kn: The max weight allowable on this surface type for a GDSS TT-type (twin tandem)
              landing gear configuration, in kilonewtons (kN).Note: The corresponding
              equivalent field is not converted by the UDL and may or may not be supplied by
              the provider. The provider/consumer is responsible for all unit conversions.

          t_wt_kip: The max weight allowable on this surface type for a T-type (twin (dual)) landing
              gear configuration, in kilopounds (kip).Note: The corresponding equivalent field
              is not converted by the UDL and may or may not be supplied by the provider. The
              provider/consumer is responsible for all unit conversions.

          t_wt_kip_mod: The modified max weight allowable on this surface type for a T-type (twin
              (dual)) landing gear configuration, in kilopounds (kip).

          t_wt_kip_mod_note: User input rationale for the manual modification of the prescribed value
              indicating the max weight allowable on this surface for a T-type (twin(dual))
              landing gear configuration. For more information, contact the provider source.

          t_wt_kn: The max weight allowable on this surface type for a T-type (twin (dual)) landing
              gear configuration, in kilonewtons (kN).Note: The corresponding equivalent field
              is not converted by the UDL and may or may not be supplied by the provider. The
              provider/consumer is responsible for all unit conversions.

          width_ft: The width of the surface type, in feet.

          width_m: The width of the surface type, in meters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            f"/udl/surface/{path_id}",
            body=await async_maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "name": name,
                    "source": source,
                    "type": type,
                    "body_id": body_id,
                    "alt_site_id": alt_site_id,
                    "condition": condition,
                    "ddt_wt_kip": ddt_wt_kip,
                    "ddt_wt_kip_mod": ddt_wt_kip_mod,
                    "ddt_wt_kip_mod_note": ddt_wt_kip_mod_note,
                    "ddt_wt_kn": ddt_wt_kn,
                    "dd_wt_kip": dd_wt_kip,
                    "dd_wt_kip_mod": dd_wt_kip_mod,
                    "dd_wt_kip_mod_note": dd_wt_kip_mod_note,
                    "dd_wt_kn": dd_wt_kn,
                    "end_lat": end_lat,
                    "end_lon": end_lon,
                    "id_site": id_site,
                    "lcn": lcn,
                    "lda_ft": lda_ft,
                    "lda_m": lda_m,
                    "length_ft": length_ft,
                    "length_m": length_m,
                    "lighting": lighting,
                    "lights_aprch": lights_aprch,
                    "lights_cl": lights_cl,
                    "lights_ols": lights_ols,
                    "lights_papi": lights_papi,
                    "lights_reil": lights_reil,
                    "lights_rwy": lights_rwy,
                    "lights_seqfl": lights_seqfl,
                    "lights_tdzl": lights_tdzl,
                    "lights_unkn": lights_unkn,
                    "lights_vasi": lights_vasi,
                    "material": material,
                    "obstacle": obstacle,
                    "origin": origin,
                    "pcn": pcn,
                    "point_reference": point_reference,
                    "primary": primary,
                    "raw_wbc": raw_wbc,
                    "sbtt_wt_kip": sbtt_wt_kip,
                    "sbtt_wt_kip_mod": sbtt_wt_kip_mod,
                    "sbtt_wt_kip_mod_note": sbtt_wt_kip_mod_note,
                    "sbtt_wt_kn": sbtt_wt_kn,
                    "start_lat": start_lat,
                    "start_lon": start_lon,
                    "st_wt_kip": st_wt_kip,
                    "st_wt_kip_mod": st_wt_kip_mod,
                    "st_wt_kip_mod_note": st_wt_kip_mod_note,
                    "st_wt_kn": st_wt_kn,
                    "s_wt_kip": s_wt_kip,
                    "s_wt_kip_mod": s_wt_kip_mod,
                    "s_wt_kip_mod_note": s_wt_kip_mod_note,
                    "s_wt_kn": s_wt_kn,
                    "tdt_wtkip": tdt_wtkip,
                    "tdt_wt_kip_mod": tdt_wt_kip_mod,
                    "tdt_wt_kip_mod_note": tdt_wt_kip_mod_note,
                    "tdt_wt_kn": tdt_wt_kn,
                    "trt_wt_kip": trt_wt_kip,
                    "trt_wt_kip_mod": trt_wt_kip_mod,
                    "trt_wt_kip_mod_note": trt_wt_kip_mod_note,
                    "trt_wt_kn": trt_wt_kn,
                    "tt_wt_kip": tt_wt_kip,
                    "tt_wt_kip_mod": tt_wt_kip_mod,
                    "tt_wt_kip_mod_note": tt_wt_kip_mod_note,
                    "tt_wt_kn": tt_wt_kn,
                    "t_wt_kip": t_wt_kip,
                    "t_wt_kip_mod": t_wt_kip_mod,
                    "t_wt_kip_mod_note": t_wt_kip_mod_note,
                    "t_wt_kn": t_wt_kn,
                    "width_ft": width_ft,
                    "width_m": width_m,
                },
                surface_update_params.SurfaceUpdateParams,
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
    ) -> AsyncPaginator[SurfaceListResponse, AsyncOffsetPage[SurfaceListResponse]]:
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
            "/udl/surface",
            page=AsyncOffsetPage[SurfaceListResponse],
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
                    surface_list_params.SurfaceListParams,
                ),
            ),
            model=SurfaceListResponse,
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
        Service operation to delete a Surface object specified by the passed ID path
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
            f"/udl/surface/{id}",
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
            "/udl/surface/count",
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
                    surface_count_params.SurfaceCountParams,
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
    ) -> SurfaceGetResponse:
        """
        Service operation to get a single Surface record by its unique ID passed as a
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
            f"/udl/surface/{id}",
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
                    surface_get_params.SurfaceGetParams,
                ),
            ),
            cast_to=SurfaceGetResponse,
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
            "/udl/surface/queryhelp",
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
    ) -> SurfaceTupleResponse:
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
            "/udl/surface/tuple",
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
                    surface_tuple_params.SurfaceTupleParams,
                ),
            ),
            cast_to=SurfaceTupleResponse,
        )


class SurfaceResourceWithRawResponse:
    def __init__(self, surface: SurfaceResource) -> None:
        self._surface = surface

        self.create = to_raw_response_wrapper(
            surface.create,
        )
        self.update = to_raw_response_wrapper(
            surface.update,
        )
        self.list = to_raw_response_wrapper(
            surface.list,
        )
        self.delete = to_raw_response_wrapper(
            surface.delete,
        )
        self.count = to_raw_response_wrapper(
            surface.count,
        )
        self.get = to_raw_response_wrapper(
            surface.get,
        )
        self.queryhelp = to_raw_response_wrapper(
            surface.queryhelp,
        )
        self.tuple = to_raw_response_wrapper(
            surface.tuple,
        )


class AsyncSurfaceResourceWithRawResponse:
    def __init__(self, surface: AsyncSurfaceResource) -> None:
        self._surface = surface

        self.create = async_to_raw_response_wrapper(
            surface.create,
        )
        self.update = async_to_raw_response_wrapper(
            surface.update,
        )
        self.list = async_to_raw_response_wrapper(
            surface.list,
        )
        self.delete = async_to_raw_response_wrapper(
            surface.delete,
        )
        self.count = async_to_raw_response_wrapper(
            surface.count,
        )
        self.get = async_to_raw_response_wrapper(
            surface.get,
        )
        self.queryhelp = async_to_raw_response_wrapper(
            surface.queryhelp,
        )
        self.tuple = async_to_raw_response_wrapper(
            surface.tuple,
        )


class SurfaceResourceWithStreamingResponse:
    def __init__(self, surface: SurfaceResource) -> None:
        self._surface = surface

        self.create = to_streamed_response_wrapper(
            surface.create,
        )
        self.update = to_streamed_response_wrapper(
            surface.update,
        )
        self.list = to_streamed_response_wrapper(
            surface.list,
        )
        self.delete = to_streamed_response_wrapper(
            surface.delete,
        )
        self.count = to_streamed_response_wrapper(
            surface.count,
        )
        self.get = to_streamed_response_wrapper(
            surface.get,
        )
        self.queryhelp = to_streamed_response_wrapper(
            surface.queryhelp,
        )
        self.tuple = to_streamed_response_wrapper(
            surface.tuple,
        )


class AsyncSurfaceResourceWithStreamingResponse:
    def __init__(self, surface: AsyncSurfaceResource) -> None:
        self._surface = surface

        self.create = async_to_streamed_response_wrapper(
            surface.create,
        )
        self.update = async_to_streamed_response_wrapper(
            surface.update,
        )
        self.list = async_to_streamed_response_wrapper(
            surface.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            surface.delete,
        )
        self.count = async_to_streamed_response_wrapper(
            surface.count,
        )
        self.get = async_to_streamed_response_wrapper(
            surface.get,
        )
        self.queryhelp = async_to_streamed_response_wrapper(
            surface.queryhelp,
        )
        self.tuple = async_to_streamed_response_wrapper(
            surface.tuple,
        )
