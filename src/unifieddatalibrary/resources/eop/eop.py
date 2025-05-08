# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal

import httpx

from ...types import (
    eop_list_params,
    eop_count_params,
    eop_create_params,
    eop_update_params,
    eop_retrieve_params,
    eop_list_tuple_params,
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
from ...types.eop_abridged import EopAbridged
from ...types.shared.eop_full import EopFull
from ...types.eop_list_tuple_response import EopListTupleResponse

__all__ = ["EopResource", "AsyncEopResource"]


class EopResource(SyncAPIResource):
    @cached_property
    def history(self) -> HistoryResource:
        return HistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> EopResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return EopResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EopResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return EopResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        eop_date: Union[str, datetime],
        source: str,
        id: str | NotGiven = NOT_GIVEN,
        d_epsilon: float | NotGiven = NOT_GIVEN,
        d_epsilon_b: float | NotGiven = NOT_GIVEN,
        d_epsilon_unc: float | NotGiven = NOT_GIVEN,
        d_psi: float | NotGiven = NOT_GIVEN,
        d_psib: float | NotGiven = NOT_GIVEN,
        d_psi_unc: float | NotGiven = NOT_GIVEN,
        d_x: float | NotGiven = NOT_GIVEN,
        d_xb: float | NotGiven = NOT_GIVEN,
        d_x_unc: float | NotGiven = NOT_GIVEN,
        d_y: float | NotGiven = NOT_GIVEN,
        d_yb: float | NotGiven = NOT_GIVEN,
        d_y_unc: float | NotGiven = NOT_GIVEN,
        lod: float | NotGiven = NOT_GIVEN,
        lod_unc: float | NotGiven = NOT_GIVEN,
        nutation_state: Literal["I", "P"] | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        polar_motion_state: Literal["I", "P"] | NotGiven = NOT_GIVEN,
        polar_motion_x: float | NotGiven = NOT_GIVEN,
        polar_motion_xb: float | NotGiven = NOT_GIVEN,
        polar_motion_x_unc: float | NotGiven = NOT_GIVEN,
        polar_motion_y: float | NotGiven = NOT_GIVEN,
        polar_motion_yb: float | NotGiven = NOT_GIVEN,
        polar_motion_y_unc: float | NotGiven = NOT_GIVEN,
        precession_nutation_std: str | NotGiven = NOT_GIVEN,
        raw_file_uri: str | NotGiven = NOT_GIVEN,
        ut1_utc: float | NotGiven = NOT_GIVEN,
        ut1_utcb: float | NotGiven = NOT_GIVEN,
        ut1_utc_state: Literal["I", "P"] | NotGiven = NOT_GIVEN,
        ut1_utc_unc: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single EOP Record as a POST body and ingest into the
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

          eop_date: Effective date/time for the EOP values in ISO8601 UTC format. The values could
              be current or predicted.

          source: Source of the data.

          id: Unique identifier of the record, auto-generated by the system.

          d_epsilon: The Bulletin A offset in obliquity dDe1980 with respect to the IAU 1976 Theory
              of Precession and the IAU 1980 Theory of Nutation, measured in milliseconds of
              arc. Note: dEpsilon is not used when this record represents IAU 2000 data.

          d_epsilon_b: The Bulletin B offset in obliquity dDe1980 with respect to the IAU 1976 Theory
              of Precession and the IAU 1980 Theory of Nutation, measured in milliseconds of
              arc. Note: dEpsilonB is not used when this record represents IAU 2000 data.

          d_epsilon_unc: The estimated uncertainty/error in the dEpsilon value in milliseconds of arc.

          d_psi: The Bulletin A offset in longitude dDy1980 with respect to the IAU 1976 Theory
              of Precession and the IAU 1980 Theory of Nutation, measured in milliseconds of
              arc. Note: dPSI is not used when this record represents IAU 2000 data.

          d_psib: The Bulletin B offset in longitude dDy1980 with respect to the IAU 1976 Theory
              of Precession and the IAU 1980 Theory of Nutation, measured in milliseconds of
              arc. Note: dPSIB is not used when this record represents IAU 2000 data.

          d_psi_unc: The estimated uncertainty/error in the dPSI value in milliseconds of arc.

          d_x: The Bulletin A celestial pole offset along x-axis with respect to the IAU 2000A
              Theory of Precession and Nutation, measured in milliseconds of arc. Note: dX is
              not used when this record represents IAU 1980 data.

          d_xb: The Bulletin B celestial pole offset along the X-axis with respect to the IAU
              2000A Theory of Precession and Nutation, measured in milliseconds of arc. Note:
              dXB is not used when this record represents IAU 1980 data.

          d_x_unc: The estimated uncertainty/error in the Bulletin A dX value, in milliseconds of
              arc.

          d_y: The Bulletin A celestial pole offset along y-axis with respect to the IAU 2000A
              Theory of Precession and Nutation, measured in milliseconds of arc. Note: dY is
              not used when this record represents IAU 1980 data.

          d_yb: The Bulletin B celestial pole offset along the Y-axis with respect to the IAU
              2000A Theory of Precession and Nutation, measured in milliseconds of arc. Note:
              dYB is not used when this record represents IAU 1980 data.

          d_y_unc: The estimated uncertainty/error in the Bulletin A dY value, in milliseconds of
              arc.

          lod: Bulletin A length of day or LOD in milliseconds. Universal time (UT1) is the
              time of the earth clock, which performs one revolution in about 24h. It is
              practically proportional to the sidereal time. The excess revolution time is
              called length of day (LOD).

          lod_unc: The estimated uncertainty/error in the lod value in seconds.

          nutation_state: Flag indicating Issued (I), or Predicted (P) for this record's nutation values
              (dPSI and dEpsilon).

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          polar_motion_state: Flag indicating Issued (I), or Predicted (P) for this record's polar motion
              values.

          polar_motion_x: The Bulletin A X coordinate value of earth polar motion at eopDate. Polar motion
              of the Earth is the motion of the Earth's rotational axis relative to its crust.
              This is measured with respect to a reference frame in which the solid Earth is
              fixed (a so-called Earth-centered, Earth-fixed or ECEF reference frame).
              Measured in arc seconds.

          polar_motion_xb: Bulletin B X coordinate value of earth polar motion at eopDate. Polar motion of
              the Earth is the motion of the Earth's rotational axis relative to its crust.
              This is measured with respect to a reference frame in which the solid Earth is
              fixed (a so-called Earth-centered, Earth-fixed or ECEF reference frame).
              Measured in arc seconds.

          polar_motion_x_unc: Estimated uncertainty/error in polarMotionX value in arc seconds.

          polar_motion_y: The Bulletin A Y coordinate value of earth polar motion at eopDate. Polar motion
              of the Earth is the motion of the Earth's rotational axis relative to its crust.
              This is measured with respect to a reference frame in which the solid Earth is
              fixed (a so-called Earth-centered, Earth-fixed or ECEF reference frame).
              Measured in arc seconds.

          polar_motion_yb: Bulletin B Y coordinate value of earth polar motion at eopDate. Polar motion of
              the Earth is the motion of the Earth's rotational axis relative to its crust.
              This is measured with respect to a reference frame in which the solid Earth is
              fixed (a so-called Earth-centered, Earth-fixed or ECEF reference frame).
              Measured in arc seconds.

          polar_motion_y_unc: Estimated uncertainty/error in polarMotionY value in arc seconds.

          precession_nutation_std: The IAU Theory of Precession and Theory of Nutation applied to the data in this
              record. IAU1980 records employ the IAU 1976 Theory of Precession and IAU 1980
              Theory of Nutation, and IAU2000 records employ the IAU 2000A Theory of
              Precession and Nutation.

          raw_file_uri: Optional URI location in the document repository of the raw file parsed by the
              system to produce this record. To download the raw file, prepend
              https://udl-hostname/scs/download?id= to this value.

          ut1_utc: The difference between the Bulletin A UT1 and UTC time scales as of eopDate in
              seconds.

          ut1_utcb: The Bulletin B difference between the UT1 and UTC time scales as of eopDate in
              seconds.

          ut1_utc_state: Flag indicating Issued (I), or Predicted (P) for this record''s Bulletin A
              UT1-UTC values.

          ut1_utc_unc: The estimated uncertainty/error in the ut1UTC value in seconds.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/udl/eop",
            body=maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "eop_date": eop_date,
                    "source": source,
                    "id": id,
                    "d_epsilon": d_epsilon,
                    "d_epsilon_b": d_epsilon_b,
                    "d_epsilon_unc": d_epsilon_unc,
                    "d_psi": d_psi,
                    "d_psib": d_psib,
                    "d_psi_unc": d_psi_unc,
                    "d_x": d_x,
                    "d_xb": d_xb,
                    "d_x_unc": d_x_unc,
                    "d_y": d_y,
                    "d_yb": d_yb,
                    "d_y_unc": d_y_unc,
                    "lod": lod,
                    "lod_unc": lod_unc,
                    "nutation_state": nutation_state,
                    "origin": origin,
                    "polar_motion_state": polar_motion_state,
                    "polar_motion_x": polar_motion_x,
                    "polar_motion_xb": polar_motion_xb,
                    "polar_motion_x_unc": polar_motion_x_unc,
                    "polar_motion_y": polar_motion_y,
                    "polar_motion_yb": polar_motion_yb,
                    "polar_motion_y_unc": polar_motion_y_unc,
                    "precession_nutation_std": precession_nutation_std,
                    "raw_file_uri": raw_file_uri,
                    "ut1_utc": ut1_utc,
                    "ut1_utcb": ut1_utcb,
                    "ut1_utc_state": ut1_utc_state,
                    "ut1_utc_unc": ut1_utc_unc,
                },
                eop_create_params.EopCreateParams,
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
    ) -> EopFull:
        """
        Service operation to get a single EOP record by its unique ID passed as a path
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
            f"/udl/eop/{id}",
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
                    eop_retrieve_params.EopRetrieveParams,
                ),
            ),
            cast_to=EopFull,
        )

    def update(
        self,
        path_id: str,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        eop_date: Union[str, datetime],
        source: str,
        body_id: str | NotGiven = NOT_GIVEN,
        d_epsilon: float | NotGiven = NOT_GIVEN,
        d_epsilon_b: float | NotGiven = NOT_GIVEN,
        d_epsilon_unc: float | NotGiven = NOT_GIVEN,
        d_psi: float | NotGiven = NOT_GIVEN,
        d_psib: float | NotGiven = NOT_GIVEN,
        d_psi_unc: float | NotGiven = NOT_GIVEN,
        d_x: float | NotGiven = NOT_GIVEN,
        d_xb: float | NotGiven = NOT_GIVEN,
        d_x_unc: float | NotGiven = NOT_GIVEN,
        d_y: float | NotGiven = NOT_GIVEN,
        d_yb: float | NotGiven = NOT_GIVEN,
        d_y_unc: float | NotGiven = NOT_GIVEN,
        lod: float | NotGiven = NOT_GIVEN,
        lod_unc: float | NotGiven = NOT_GIVEN,
        nutation_state: Literal["I", "P"] | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        polar_motion_state: Literal["I", "P"] | NotGiven = NOT_GIVEN,
        polar_motion_x: float | NotGiven = NOT_GIVEN,
        polar_motion_xb: float | NotGiven = NOT_GIVEN,
        polar_motion_x_unc: float | NotGiven = NOT_GIVEN,
        polar_motion_y: float | NotGiven = NOT_GIVEN,
        polar_motion_yb: float | NotGiven = NOT_GIVEN,
        polar_motion_y_unc: float | NotGiven = NOT_GIVEN,
        precession_nutation_std: str | NotGiven = NOT_GIVEN,
        raw_file_uri: str | NotGiven = NOT_GIVEN,
        ut1_utc: float | NotGiven = NOT_GIVEN,
        ut1_utcb: float | NotGiven = NOT_GIVEN,
        ut1_utc_state: Literal["I", "P"] | NotGiven = NOT_GIVEN,
        ut1_utc_unc: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Service operation to update a single EOP Record.

        A specific role is required to
        perform this service operation. Please contact the UDL team for assistance.

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

          eop_date: Effective date/time for the EOP values in ISO8601 UTC format. The values could
              be current or predicted.

          source: Source of the data.

          body_id: Unique identifier of the record, auto-generated by the system.

          d_epsilon: The Bulletin A offset in obliquity dDe1980 with respect to the IAU 1976 Theory
              of Precession and the IAU 1980 Theory of Nutation, measured in milliseconds of
              arc. Note: dEpsilon is not used when this record represents IAU 2000 data.

          d_epsilon_b: The Bulletin B offset in obliquity dDe1980 with respect to the IAU 1976 Theory
              of Precession and the IAU 1980 Theory of Nutation, measured in milliseconds of
              arc. Note: dEpsilonB is not used when this record represents IAU 2000 data.

          d_epsilon_unc: The estimated uncertainty/error in the dEpsilon value in milliseconds of arc.

          d_psi: The Bulletin A offset in longitude dDy1980 with respect to the IAU 1976 Theory
              of Precession and the IAU 1980 Theory of Nutation, measured in milliseconds of
              arc. Note: dPSI is not used when this record represents IAU 2000 data.

          d_psib: The Bulletin B offset in longitude dDy1980 with respect to the IAU 1976 Theory
              of Precession and the IAU 1980 Theory of Nutation, measured in milliseconds of
              arc. Note: dPSIB is not used when this record represents IAU 2000 data.

          d_psi_unc: The estimated uncertainty/error in the dPSI value in milliseconds of arc.

          d_x: The Bulletin A celestial pole offset along x-axis with respect to the IAU 2000A
              Theory of Precession and Nutation, measured in milliseconds of arc. Note: dX is
              not used when this record represents IAU 1980 data.

          d_xb: The Bulletin B celestial pole offset along the X-axis with respect to the IAU
              2000A Theory of Precession and Nutation, measured in milliseconds of arc. Note:
              dXB is not used when this record represents IAU 1980 data.

          d_x_unc: The estimated uncertainty/error in the Bulletin A dX value, in milliseconds of
              arc.

          d_y: The Bulletin A celestial pole offset along y-axis with respect to the IAU 2000A
              Theory of Precession and Nutation, measured in milliseconds of arc. Note: dY is
              not used when this record represents IAU 1980 data.

          d_yb: The Bulletin B celestial pole offset along the Y-axis with respect to the IAU
              2000A Theory of Precession and Nutation, measured in milliseconds of arc. Note:
              dYB is not used when this record represents IAU 1980 data.

          d_y_unc: The estimated uncertainty/error in the Bulletin A dY value, in milliseconds of
              arc.

          lod: Bulletin A length of day or LOD in milliseconds. Universal time (UT1) is the
              time of the earth clock, which performs one revolution in about 24h. It is
              practically proportional to the sidereal time. The excess revolution time is
              called length of day (LOD).

          lod_unc: The estimated uncertainty/error in the lod value in seconds.

          nutation_state: Flag indicating Issued (I), or Predicted (P) for this record's nutation values
              (dPSI and dEpsilon).

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          polar_motion_state: Flag indicating Issued (I), or Predicted (P) for this record's polar motion
              values.

          polar_motion_x: The Bulletin A X coordinate value of earth polar motion at eopDate. Polar motion
              of the Earth is the motion of the Earth's rotational axis relative to its crust.
              This is measured with respect to a reference frame in which the solid Earth is
              fixed (a so-called Earth-centered, Earth-fixed or ECEF reference frame).
              Measured in arc seconds.

          polar_motion_xb: Bulletin B X coordinate value of earth polar motion at eopDate. Polar motion of
              the Earth is the motion of the Earth's rotational axis relative to its crust.
              This is measured with respect to a reference frame in which the solid Earth is
              fixed (a so-called Earth-centered, Earth-fixed or ECEF reference frame).
              Measured in arc seconds.

          polar_motion_x_unc: Estimated uncertainty/error in polarMotionX value in arc seconds.

          polar_motion_y: The Bulletin A Y coordinate value of earth polar motion at eopDate. Polar motion
              of the Earth is the motion of the Earth's rotational axis relative to its crust.
              This is measured with respect to a reference frame in which the solid Earth is
              fixed (a so-called Earth-centered, Earth-fixed or ECEF reference frame).
              Measured in arc seconds.

          polar_motion_yb: Bulletin B Y coordinate value of earth polar motion at eopDate. Polar motion of
              the Earth is the motion of the Earth's rotational axis relative to its crust.
              This is measured with respect to a reference frame in which the solid Earth is
              fixed (a so-called Earth-centered, Earth-fixed or ECEF reference frame).
              Measured in arc seconds.

          polar_motion_y_unc: Estimated uncertainty/error in polarMotionY value in arc seconds.

          precession_nutation_std: The IAU Theory of Precession and Theory of Nutation applied to the data in this
              record. IAU1980 records employ the IAU 1976 Theory of Precession and IAU 1980
              Theory of Nutation, and IAU2000 records employ the IAU 2000A Theory of
              Precession and Nutation.

          raw_file_uri: Optional URI location in the document repository of the raw file parsed by the
              system to produce this record. To download the raw file, prepend
              https://udl-hostname/scs/download?id= to this value.

          ut1_utc: The difference between the Bulletin A UT1 and UTC time scales as of eopDate in
              seconds.

          ut1_utcb: The Bulletin B difference between the UT1 and UTC time scales as of eopDate in
              seconds.

          ut1_utc_state: Flag indicating Issued (I), or Predicted (P) for this record''s Bulletin A
              UT1-UTC values.

          ut1_utc_unc: The estimated uncertainty/error in the ut1UTC value in seconds.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            f"/udl/eop/{path_id}",
            body=maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "eop_date": eop_date,
                    "source": source,
                    "body_id": body_id,
                    "d_epsilon": d_epsilon,
                    "d_epsilon_b": d_epsilon_b,
                    "d_epsilon_unc": d_epsilon_unc,
                    "d_psi": d_psi,
                    "d_psib": d_psib,
                    "d_psi_unc": d_psi_unc,
                    "d_x": d_x,
                    "d_xb": d_xb,
                    "d_x_unc": d_x_unc,
                    "d_y": d_y,
                    "d_yb": d_yb,
                    "d_y_unc": d_y_unc,
                    "lod": lod,
                    "lod_unc": lod_unc,
                    "nutation_state": nutation_state,
                    "origin": origin,
                    "polar_motion_state": polar_motion_state,
                    "polar_motion_x": polar_motion_x,
                    "polar_motion_xb": polar_motion_xb,
                    "polar_motion_x_unc": polar_motion_x_unc,
                    "polar_motion_y": polar_motion_y,
                    "polar_motion_yb": polar_motion_yb,
                    "polar_motion_y_unc": polar_motion_y_unc,
                    "precession_nutation_std": precession_nutation_std,
                    "raw_file_uri": raw_file_uri,
                    "ut1_utc": ut1_utc,
                    "ut1_utcb": ut1_utcb,
                    "ut1_utc_state": ut1_utc_state,
                    "ut1_utc_unc": ut1_utc_unc,
                },
                eop_update_params.EopUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        *,
        eop_date: Union[str, datetime],
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncOffsetPage[EopAbridged]:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          eop_date: Effective date/time for the EOP values in ISO8601 UTC format. The values could
              be current or predicted. (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/eop",
            page=SyncOffsetPage[EopAbridged],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "eop_date": eop_date,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    eop_list_params.EopListParams,
                ),
            ),
            model=EopAbridged,
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
        Service operation to delete an EOP Record specified by the passed ID path
        parameter. Note, delete operations do not remove data from historical or
        publish/subscribe stores. A specific role is required to perform this service
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
            f"/udl/eop/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def count(
        self,
        *,
        eop_date: Union[str, datetime],
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
          eop_date: Effective date/time for the EOP values in ISO8601 UTC format. The values could
              be current or predicted. (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return self._get(
            "/udl/eop/count",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "eop_date": eop_date,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    eop_count_params.EopCountParams,
                ),
            ),
            cast_to=str,
        )

    def list_tuple(
        self,
        *,
        columns: str,
        eop_date: Union[str, datetime],
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EopListTupleResponse:
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

          eop_date: Effective date/time for the EOP values in ISO8601 UTC format. The values could
              be current or predicted. (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/udl/eop/tuple",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "columns": columns,
                        "eop_date": eop_date,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    eop_list_tuple_params.EopListTupleParams,
                ),
            ),
            cast_to=EopListTupleResponse,
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
            "/udl/eop/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncEopResource(AsyncAPIResource):
    @cached_property
    def history(self) -> AsyncHistoryResource:
        return AsyncHistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncEopResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncEopResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEopResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncEopResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        eop_date: Union[str, datetime],
        source: str,
        id: str | NotGiven = NOT_GIVEN,
        d_epsilon: float | NotGiven = NOT_GIVEN,
        d_epsilon_b: float | NotGiven = NOT_GIVEN,
        d_epsilon_unc: float | NotGiven = NOT_GIVEN,
        d_psi: float | NotGiven = NOT_GIVEN,
        d_psib: float | NotGiven = NOT_GIVEN,
        d_psi_unc: float | NotGiven = NOT_GIVEN,
        d_x: float | NotGiven = NOT_GIVEN,
        d_xb: float | NotGiven = NOT_GIVEN,
        d_x_unc: float | NotGiven = NOT_GIVEN,
        d_y: float | NotGiven = NOT_GIVEN,
        d_yb: float | NotGiven = NOT_GIVEN,
        d_y_unc: float | NotGiven = NOT_GIVEN,
        lod: float | NotGiven = NOT_GIVEN,
        lod_unc: float | NotGiven = NOT_GIVEN,
        nutation_state: Literal["I", "P"] | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        polar_motion_state: Literal["I", "P"] | NotGiven = NOT_GIVEN,
        polar_motion_x: float | NotGiven = NOT_GIVEN,
        polar_motion_xb: float | NotGiven = NOT_GIVEN,
        polar_motion_x_unc: float | NotGiven = NOT_GIVEN,
        polar_motion_y: float | NotGiven = NOT_GIVEN,
        polar_motion_yb: float | NotGiven = NOT_GIVEN,
        polar_motion_y_unc: float | NotGiven = NOT_GIVEN,
        precession_nutation_std: str | NotGiven = NOT_GIVEN,
        raw_file_uri: str | NotGiven = NOT_GIVEN,
        ut1_utc: float | NotGiven = NOT_GIVEN,
        ut1_utcb: float | NotGiven = NOT_GIVEN,
        ut1_utc_state: Literal["I", "P"] | NotGiven = NOT_GIVEN,
        ut1_utc_unc: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single EOP Record as a POST body and ingest into the
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

          eop_date: Effective date/time for the EOP values in ISO8601 UTC format. The values could
              be current or predicted.

          source: Source of the data.

          id: Unique identifier of the record, auto-generated by the system.

          d_epsilon: The Bulletin A offset in obliquity dDe1980 with respect to the IAU 1976 Theory
              of Precession and the IAU 1980 Theory of Nutation, measured in milliseconds of
              arc. Note: dEpsilon is not used when this record represents IAU 2000 data.

          d_epsilon_b: The Bulletin B offset in obliquity dDe1980 with respect to the IAU 1976 Theory
              of Precession and the IAU 1980 Theory of Nutation, measured in milliseconds of
              arc. Note: dEpsilonB is not used when this record represents IAU 2000 data.

          d_epsilon_unc: The estimated uncertainty/error in the dEpsilon value in milliseconds of arc.

          d_psi: The Bulletin A offset in longitude dDy1980 with respect to the IAU 1976 Theory
              of Precession and the IAU 1980 Theory of Nutation, measured in milliseconds of
              arc. Note: dPSI is not used when this record represents IAU 2000 data.

          d_psib: The Bulletin B offset in longitude dDy1980 with respect to the IAU 1976 Theory
              of Precession and the IAU 1980 Theory of Nutation, measured in milliseconds of
              arc. Note: dPSIB is not used when this record represents IAU 2000 data.

          d_psi_unc: The estimated uncertainty/error in the dPSI value in milliseconds of arc.

          d_x: The Bulletin A celestial pole offset along x-axis with respect to the IAU 2000A
              Theory of Precession and Nutation, measured in milliseconds of arc. Note: dX is
              not used when this record represents IAU 1980 data.

          d_xb: The Bulletin B celestial pole offset along the X-axis with respect to the IAU
              2000A Theory of Precession and Nutation, measured in milliseconds of arc. Note:
              dXB is not used when this record represents IAU 1980 data.

          d_x_unc: The estimated uncertainty/error in the Bulletin A dX value, in milliseconds of
              arc.

          d_y: The Bulletin A celestial pole offset along y-axis with respect to the IAU 2000A
              Theory of Precession and Nutation, measured in milliseconds of arc. Note: dY is
              not used when this record represents IAU 1980 data.

          d_yb: The Bulletin B celestial pole offset along the Y-axis with respect to the IAU
              2000A Theory of Precession and Nutation, measured in milliseconds of arc. Note:
              dYB is not used when this record represents IAU 1980 data.

          d_y_unc: The estimated uncertainty/error in the Bulletin A dY value, in milliseconds of
              arc.

          lod: Bulletin A length of day or LOD in milliseconds. Universal time (UT1) is the
              time of the earth clock, which performs one revolution in about 24h. It is
              practically proportional to the sidereal time. The excess revolution time is
              called length of day (LOD).

          lod_unc: The estimated uncertainty/error in the lod value in seconds.

          nutation_state: Flag indicating Issued (I), or Predicted (P) for this record's nutation values
              (dPSI and dEpsilon).

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          polar_motion_state: Flag indicating Issued (I), or Predicted (P) for this record's polar motion
              values.

          polar_motion_x: The Bulletin A X coordinate value of earth polar motion at eopDate. Polar motion
              of the Earth is the motion of the Earth's rotational axis relative to its crust.
              This is measured with respect to a reference frame in which the solid Earth is
              fixed (a so-called Earth-centered, Earth-fixed or ECEF reference frame).
              Measured in arc seconds.

          polar_motion_xb: Bulletin B X coordinate value of earth polar motion at eopDate. Polar motion of
              the Earth is the motion of the Earth's rotational axis relative to its crust.
              This is measured with respect to a reference frame in which the solid Earth is
              fixed (a so-called Earth-centered, Earth-fixed or ECEF reference frame).
              Measured in arc seconds.

          polar_motion_x_unc: Estimated uncertainty/error in polarMotionX value in arc seconds.

          polar_motion_y: The Bulletin A Y coordinate value of earth polar motion at eopDate. Polar motion
              of the Earth is the motion of the Earth's rotational axis relative to its crust.
              This is measured with respect to a reference frame in which the solid Earth is
              fixed (a so-called Earth-centered, Earth-fixed or ECEF reference frame).
              Measured in arc seconds.

          polar_motion_yb: Bulletin B Y coordinate value of earth polar motion at eopDate. Polar motion of
              the Earth is the motion of the Earth's rotational axis relative to its crust.
              This is measured with respect to a reference frame in which the solid Earth is
              fixed (a so-called Earth-centered, Earth-fixed or ECEF reference frame).
              Measured in arc seconds.

          polar_motion_y_unc: Estimated uncertainty/error in polarMotionY value in arc seconds.

          precession_nutation_std: The IAU Theory of Precession and Theory of Nutation applied to the data in this
              record. IAU1980 records employ the IAU 1976 Theory of Precession and IAU 1980
              Theory of Nutation, and IAU2000 records employ the IAU 2000A Theory of
              Precession and Nutation.

          raw_file_uri: Optional URI location in the document repository of the raw file parsed by the
              system to produce this record. To download the raw file, prepend
              https://udl-hostname/scs/download?id= to this value.

          ut1_utc: The difference between the Bulletin A UT1 and UTC time scales as of eopDate in
              seconds.

          ut1_utcb: The Bulletin B difference between the UT1 and UTC time scales as of eopDate in
              seconds.

          ut1_utc_state: Flag indicating Issued (I), or Predicted (P) for this record''s Bulletin A
              UT1-UTC values.

          ut1_utc_unc: The estimated uncertainty/error in the ut1UTC value in seconds.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/udl/eop",
            body=await async_maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "eop_date": eop_date,
                    "source": source,
                    "id": id,
                    "d_epsilon": d_epsilon,
                    "d_epsilon_b": d_epsilon_b,
                    "d_epsilon_unc": d_epsilon_unc,
                    "d_psi": d_psi,
                    "d_psib": d_psib,
                    "d_psi_unc": d_psi_unc,
                    "d_x": d_x,
                    "d_xb": d_xb,
                    "d_x_unc": d_x_unc,
                    "d_y": d_y,
                    "d_yb": d_yb,
                    "d_y_unc": d_y_unc,
                    "lod": lod,
                    "lod_unc": lod_unc,
                    "nutation_state": nutation_state,
                    "origin": origin,
                    "polar_motion_state": polar_motion_state,
                    "polar_motion_x": polar_motion_x,
                    "polar_motion_xb": polar_motion_xb,
                    "polar_motion_x_unc": polar_motion_x_unc,
                    "polar_motion_y": polar_motion_y,
                    "polar_motion_yb": polar_motion_yb,
                    "polar_motion_y_unc": polar_motion_y_unc,
                    "precession_nutation_std": precession_nutation_std,
                    "raw_file_uri": raw_file_uri,
                    "ut1_utc": ut1_utc,
                    "ut1_utcb": ut1_utcb,
                    "ut1_utc_state": ut1_utc_state,
                    "ut1_utc_unc": ut1_utc_unc,
                },
                eop_create_params.EopCreateParams,
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
    ) -> EopFull:
        """
        Service operation to get a single EOP record by its unique ID passed as a path
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
            f"/udl/eop/{id}",
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
                    eop_retrieve_params.EopRetrieveParams,
                ),
            ),
            cast_to=EopFull,
        )

    async def update(
        self,
        path_id: str,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        eop_date: Union[str, datetime],
        source: str,
        body_id: str | NotGiven = NOT_GIVEN,
        d_epsilon: float | NotGiven = NOT_GIVEN,
        d_epsilon_b: float | NotGiven = NOT_GIVEN,
        d_epsilon_unc: float | NotGiven = NOT_GIVEN,
        d_psi: float | NotGiven = NOT_GIVEN,
        d_psib: float | NotGiven = NOT_GIVEN,
        d_psi_unc: float | NotGiven = NOT_GIVEN,
        d_x: float | NotGiven = NOT_GIVEN,
        d_xb: float | NotGiven = NOT_GIVEN,
        d_x_unc: float | NotGiven = NOT_GIVEN,
        d_y: float | NotGiven = NOT_GIVEN,
        d_yb: float | NotGiven = NOT_GIVEN,
        d_y_unc: float | NotGiven = NOT_GIVEN,
        lod: float | NotGiven = NOT_GIVEN,
        lod_unc: float | NotGiven = NOT_GIVEN,
        nutation_state: Literal["I", "P"] | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        polar_motion_state: Literal["I", "P"] | NotGiven = NOT_GIVEN,
        polar_motion_x: float | NotGiven = NOT_GIVEN,
        polar_motion_xb: float | NotGiven = NOT_GIVEN,
        polar_motion_x_unc: float | NotGiven = NOT_GIVEN,
        polar_motion_y: float | NotGiven = NOT_GIVEN,
        polar_motion_yb: float | NotGiven = NOT_GIVEN,
        polar_motion_y_unc: float | NotGiven = NOT_GIVEN,
        precession_nutation_std: str | NotGiven = NOT_GIVEN,
        raw_file_uri: str | NotGiven = NOT_GIVEN,
        ut1_utc: float | NotGiven = NOT_GIVEN,
        ut1_utcb: float | NotGiven = NOT_GIVEN,
        ut1_utc_state: Literal["I", "P"] | NotGiven = NOT_GIVEN,
        ut1_utc_unc: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Service operation to update a single EOP Record.

        A specific role is required to
        perform this service operation. Please contact the UDL team for assistance.

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

          eop_date: Effective date/time for the EOP values in ISO8601 UTC format. The values could
              be current or predicted.

          source: Source of the data.

          body_id: Unique identifier of the record, auto-generated by the system.

          d_epsilon: The Bulletin A offset in obliquity dDe1980 with respect to the IAU 1976 Theory
              of Precession and the IAU 1980 Theory of Nutation, measured in milliseconds of
              arc. Note: dEpsilon is not used when this record represents IAU 2000 data.

          d_epsilon_b: The Bulletin B offset in obliquity dDe1980 with respect to the IAU 1976 Theory
              of Precession and the IAU 1980 Theory of Nutation, measured in milliseconds of
              arc. Note: dEpsilonB is not used when this record represents IAU 2000 data.

          d_epsilon_unc: The estimated uncertainty/error in the dEpsilon value in milliseconds of arc.

          d_psi: The Bulletin A offset in longitude dDy1980 with respect to the IAU 1976 Theory
              of Precession and the IAU 1980 Theory of Nutation, measured in milliseconds of
              arc. Note: dPSI is not used when this record represents IAU 2000 data.

          d_psib: The Bulletin B offset in longitude dDy1980 with respect to the IAU 1976 Theory
              of Precession and the IAU 1980 Theory of Nutation, measured in milliseconds of
              arc. Note: dPSIB is not used when this record represents IAU 2000 data.

          d_psi_unc: The estimated uncertainty/error in the dPSI value in milliseconds of arc.

          d_x: The Bulletin A celestial pole offset along x-axis with respect to the IAU 2000A
              Theory of Precession and Nutation, measured in milliseconds of arc. Note: dX is
              not used when this record represents IAU 1980 data.

          d_xb: The Bulletin B celestial pole offset along the X-axis with respect to the IAU
              2000A Theory of Precession and Nutation, measured in milliseconds of arc. Note:
              dXB is not used when this record represents IAU 1980 data.

          d_x_unc: The estimated uncertainty/error in the Bulletin A dX value, in milliseconds of
              arc.

          d_y: The Bulletin A celestial pole offset along y-axis with respect to the IAU 2000A
              Theory of Precession and Nutation, measured in milliseconds of arc. Note: dY is
              not used when this record represents IAU 1980 data.

          d_yb: The Bulletin B celestial pole offset along the Y-axis with respect to the IAU
              2000A Theory of Precession and Nutation, measured in milliseconds of arc. Note:
              dYB is not used when this record represents IAU 1980 data.

          d_y_unc: The estimated uncertainty/error in the Bulletin A dY value, in milliseconds of
              arc.

          lod: Bulletin A length of day or LOD in milliseconds. Universal time (UT1) is the
              time of the earth clock, which performs one revolution in about 24h. It is
              practically proportional to the sidereal time. The excess revolution time is
              called length of day (LOD).

          lod_unc: The estimated uncertainty/error in the lod value in seconds.

          nutation_state: Flag indicating Issued (I), or Predicted (P) for this record's nutation values
              (dPSI and dEpsilon).

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          polar_motion_state: Flag indicating Issued (I), or Predicted (P) for this record's polar motion
              values.

          polar_motion_x: The Bulletin A X coordinate value of earth polar motion at eopDate. Polar motion
              of the Earth is the motion of the Earth's rotational axis relative to its crust.
              This is measured with respect to a reference frame in which the solid Earth is
              fixed (a so-called Earth-centered, Earth-fixed or ECEF reference frame).
              Measured in arc seconds.

          polar_motion_xb: Bulletin B X coordinate value of earth polar motion at eopDate. Polar motion of
              the Earth is the motion of the Earth's rotational axis relative to its crust.
              This is measured with respect to a reference frame in which the solid Earth is
              fixed (a so-called Earth-centered, Earth-fixed or ECEF reference frame).
              Measured in arc seconds.

          polar_motion_x_unc: Estimated uncertainty/error in polarMotionX value in arc seconds.

          polar_motion_y: The Bulletin A Y coordinate value of earth polar motion at eopDate. Polar motion
              of the Earth is the motion of the Earth's rotational axis relative to its crust.
              This is measured with respect to a reference frame in which the solid Earth is
              fixed (a so-called Earth-centered, Earth-fixed or ECEF reference frame).
              Measured in arc seconds.

          polar_motion_yb: Bulletin B Y coordinate value of earth polar motion at eopDate. Polar motion of
              the Earth is the motion of the Earth's rotational axis relative to its crust.
              This is measured with respect to a reference frame in which the solid Earth is
              fixed (a so-called Earth-centered, Earth-fixed or ECEF reference frame).
              Measured in arc seconds.

          polar_motion_y_unc: Estimated uncertainty/error in polarMotionY value in arc seconds.

          precession_nutation_std: The IAU Theory of Precession and Theory of Nutation applied to the data in this
              record. IAU1980 records employ the IAU 1976 Theory of Precession and IAU 1980
              Theory of Nutation, and IAU2000 records employ the IAU 2000A Theory of
              Precession and Nutation.

          raw_file_uri: Optional URI location in the document repository of the raw file parsed by the
              system to produce this record. To download the raw file, prepend
              https://udl-hostname/scs/download?id= to this value.

          ut1_utc: The difference between the Bulletin A UT1 and UTC time scales as of eopDate in
              seconds.

          ut1_utcb: The Bulletin B difference between the UT1 and UTC time scales as of eopDate in
              seconds.

          ut1_utc_state: Flag indicating Issued (I), or Predicted (P) for this record''s Bulletin A
              UT1-UTC values.

          ut1_utc_unc: The estimated uncertainty/error in the ut1UTC value in seconds.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            f"/udl/eop/{path_id}",
            body=await async_maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "eop_date": eop_date,
                    "source": source,
                    "body_id": body_id,
                    "d_epsilon": d_epsilon,
                    "d_epsilon_b": d_epsilon_b,
                    "d_epsilon_unc": d_epsilon_unc,
                    "d_psi": d_psi,
                    "d_psib": d_psib,
                    "d_psi_unc": d_psi_unc,
                    "d_x": d_x,
                    "d_xb": d_xb,
                    "d_x_unc": d_x_unc,
                    "d_y": d_y,
                    "d_yb": d_yb,
                    "d_y_unc": d_y_unc,
                    "lod": lod,
                    "lod_unc": lod_unc,
                    "nutation_state": nutation_state,
                    "origin": origin,
                    "polar_motion_state": polar_motion_state,
                    "polar_motion_x": polar_motion_x,
                    "polar_motion_xb": polar_motion_xb,
                    "polar_motion_x_unc": polar_motion_x_unc,
                    "polar_motion_y": polar_motion_y,
                    "polar_motion_yb": polar_motion_yb,
                    "polar_motion_y_unc": polar_motion_y_unc,
                    "precession_nutation_std": precession_nutation_std,
                    "raw_file_uri": raw_file_uri,
                    "ut1_utc": ut1_utc,
                    "ut1_utcb": ut1_utcb,
                    "ut1_utc_state": ut1_utc_state,
                    "ut1_utc_unc": ut1_utc_unc,
                },
                eop_update_params.EopUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        *,
        eop_date: Union[str, datetime],
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[EopAbridged, AsyncOffsetPage[EopAbridged]]:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          eop_date: Effective date/time for the EOP values in ISO8601 UTC format. The values could
              be current or predicted. (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/eop",
            page=AsyncOffsetPage[EopAbridged],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "eop_date": eop_date,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    eop_list_params.EopListParams,
                ),
            ),
            model=EopAbridged,
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
        Service operation to delete an EOP Record specified by the passed ID path
        parameter. Note, delete operations do not remove data from historical or
        publish/subscribe stores. A specific role is required to perform this service
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
            f"/udl/eop/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def count(
        self,
        *,
        eop_date: Union[str, datetime],
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
          eop_date: Effective date/time for the EOP values in ISO8601 UTC format. The values could
              be current or predicted. (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return await self._get(
            "/udl/eop/count",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "eop_date": eop_date,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    eop_count_params.EopCountParams,
                ),
            ),
            cast_to=str,
        )

    async def list_tuple(
        self,
        *,
        columns: str,
        eop_date: Union[str, datetime],
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EopListTupleResponse:
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

          eop_date: Effective date/time for the EOP values in ISO8601 UTC format. The values could
              be current or predicted. (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/udl/eop/tuple",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "columns": columns,
                        "eop_date": eop_date,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    eop_list_tuple_params.EopListTupleParams,
                ),
            ),
            cast_to=EopListTupleResponse,
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
            "/udl/eop/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class EopResourceWithRawResponse:
    def __init__(self, eop: EopResource) -> None:
        self._eop = eop

        self.create = to_raw_response_wrapper(
            eop.create,
        )
        self.retrieve = to_raw_response_wrapper(
            eop.retrieve,
        )
        self.update = to_raw_response_wrapper(
            eop.update,
        )
        self.list = to_raw_response_wrapper(
            eop.list,
        )
        self.delete = to_raw_response_wrapper(
            eop.delete,
        )
        self.count = to_raw_response_wrapper(
            eop.count,
        )
        self.list_tuple = to_raw_response_wrapper(
            eop.list_tuple,
        )
        self.queryhelp = to_raw_response_wrapper(
            eop.queryhelp,
        )

    @cached_property
    def history(self) -> HistoryResourceWithRawResponse:
        return HistoryResourceWithRawResponse(self._eop.history)


class AsyncEopResourceWithRawResponse:
    def __init__(self, eop: AsyncEopResource) -> None:
        self._eop = eop

        self.create = async_to_raw_response_wrapper(
            eop.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            eop.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            eop.update,
        )
        self.list = async_to_raw_response_wrapper(
            eop.list,
        )
        self.delete = async_to_raw_response_wrapper(
            eop.delete,
        )
        self.count = async_to_raw_response_wrapper(
            eop.count,
        )
        self.list_tuple = async_to_raw_response_wrapper(
            eop.list_tuple,
        )
        self.queryhelp = async_to_raw_response_wrapper(
            eop.queryhelp,
        )

    @cached_property
    def history(self) -> AsyncHistoryResourceWithRawResponse:
        return AsyncHistoryResourceWithRawResponse(self._eop.history)


class EopResourceWithStreamingResponse:
    def __init__(self, eop: EopResource) -> None:
        self._eop = eop

        self.create = to_streamed_response_wrapper(
            eop.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            eop.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            eop.update,
        )
        self.list = to_streamed_response_wrapper(
            eop.list,
        )
        self.delete = to_streamed_response_wrapper(
            eop.delete,
        )
        self.count = to_streamed_response_wrapper(
            eop.count,
        )
        self.list_tuple = to_streamed_response_wrapper(
            eop.list_tuple,
        )
        self.queryhelp = to_streamed_response_wrapper(
            eop.queryhelp,
        )

    @cached_property
    def history(self) -> HistoryResourceWithStreamingResponse:
        return HistoryResourceWithStreamingResponse(self._eop.history)


class AsyncEopResourceWithStreamingResponse:
    def __init__(self, eop: AsyncEopResource) -> None:
        self._eop = eop

        self.create = async_to_streamed_response_wrapper(
            eop.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            eop.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            eop.update,
        )
        self.list = async_to_streamed_response_wrapper(
            eop.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            eop.delete,
        )
        self.count = async_to_streamed_response_wrapper(
            eop.count,
        )
        self.list_tuple = async_to_streamed_response_wrapper(
            eop.list_tuple,
        )
        self.queryhelp = async_to_streamed_response_wrapper(
            eop.queryhelp,
        )

    @cached_property
    def history(self) -> AsyncHistoryResourceWithStreamingResponse:
        return AsyncHistoryResourceWithStreamingResponse(self._eop.history)
