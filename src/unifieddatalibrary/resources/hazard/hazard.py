# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from datetime import datetime
from typing_extensions import Literal

import httpx

from ...types import (
    hazard_get_params,
    hazard_list_params,
    hazard_count_params,
    hazard_tuple_params,
    hazard_create_params,
    hazard_create_bulk_params,
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
from ...types.hazard_get_response import HazardGetResponse
from ...types.hazard_list_response import HazardListResponse
from ...types.hazard_tuple_response import HazardTupleResponse

__all__ = ["HazardResource", "AsyncHazardResource"]


class HazardResource(SyncAPIResource):
    @cached_property
    def history(self) -> HistoryResource:
        return HistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> HazardResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return HazardResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HazardResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return HazardResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        alarms: List[str],
        alarm_values: Iterable[float],
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        detect_time: Union[str, datetime],
        detect_type: str,
        source: str,
        id: str | NotGiven = NOT_GIVEN,
        a: int | NotGiven = NOT_GIVEN,
        activity: float | NotGiven = NOT_GIVEN,
        bottle_id: str | NotGiven = NOT_GIVEN,
        cas_rn: str | NotGiven = NOT_GIVEN,
        channel: str | NotGiven = NOT_GIVEN,
        ctrn_time: float | NotGiven = NOT_GIVEN,
        density: float | NotGiven = NOT_GIVEN,
        dep: float | NotGiven = NOT_GIVEN,
        dep_ctrn: float | NotGiven = NOT_GIVEN,
        dose: float | NotGiven = NOT_GIVEN,
        dose_rate: float | NotGiven = NOT_GIVEN,
        duration: int | NotGiven = NOT_GIVEN,
        g_bar: float | NotGiven = NOT_GIVEN,
        harmful: bool | NotGiven = NOT_GIVEN,
        h_bar: float | NotGiven = NOT_GIVEN,
        id_poi: str | NotGiven = NOT_GIVEN,
        id_track: str | NotGiven = NOT_GIVEN,
        mass_frac: float | NotGiven = NOT_GIVEN,
        mat_cat: int | NotGiven = NOT_GIVEN,
        mat_class: str | NotGiven = NOT_GIVEN,
        mat_name: str | NotGiven = NOT_GIVEN,
        mat_type: str | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        ppm: int | NotGiven = NOT_GIVEN,
        rad_ctrn: float | NotGiven = NOT_GIVEN,
        readings: List[str] | NotGiven = NOT_GIVEN,
        reading_units: List[str] | NotGiven = NOT_GIVEN,
        reading_values: Iterable[float] | NotGiven = NOT_GIVEN,
        z: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single hazard as a POST body and ingest into the
        database. This operation is not intended to be used for automated feeds into
        UDL. Data providers should contact the UDL team for specific role assignments
        and for instructions on setting up a permanent feed through an alternate
        mechanism.

        Args:
          alarms: Array of the specific alarms associated with this detection. The alarms and
              alarmValues arrays must contain the same number of elements.

          alarm_values: Array of the values that correspond to each of the alarms contained in alarms.
              The alarms and alarmValues arrays must contain the same number of elements.

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

          detect_time: The detect time, in ISO 8601 UTC format, with millisecond precision.

          detect_type: The type of hazard (Chemical, Biological, Radiological, Nuclear) detect
              associated with this record.

          source: Source of the data.

          id: Unique identifier of the record, auto-generated by the system.

          a: The (rounded) Mass Number of the material associated with this detection. The
              rounded value is the mass number of the most abundant isotope of the element.

          activity: The radioactivity measurement of the material associated with this detection, in
              becquerels (Bq). One becquerel (Bq) is equal to one nuclear decay per second.

          bottle_id: The specific bottle ID associated with this detection.

          cas_rn: The CAS Registry Number, also referred to as CAS Number or CAS RN, associated
              with the this detection. The CAS Number is a unique numerical identifier
              assigned by the Chemical Abstracts Service (CAS), to every chemical substance
              described in the open scientific literature. It includes organic and inorganic
              compounds, minerals, isotopes, alloys, mixtures, and nonstructurable materials
              (UVCBs, substances of unknown or variable composition, complex reaction
              products, or biological origin). For further information, reference
              https://www.cas.org/cas-data/cas-registry.

          channel: The applicable channel involved in this biological material detection (e.g.
              Digestive, Eyes, Respiratory, Skin, etc.) .

          ctrn_time: The concentration time, in (kg/sec)/m^3, associated with this material
              detection.

          density: Measure of density of the material associated with this detection, in kg/m^3.

          dep: The deposition measurement of the contaminant to surface area, in kg/m^2.

          dep_ctrn: The deposition concentration of the contaminant to surface area, in
              becquerels/m^2.

          dose: The dose associated with this detection, in gray. Dose is the measure of the
              energy deposited in matter by ionizing radiation per unit mass. One gray is
              defined as one Joule of energy absorbed per kilogram of matter.

          dose_rate: The dose rate associated with this detection, in gray/sec. One gray is defined
              as one Joule of energy absorbed per kilogram of matter.

          duration: The known or projected hazard duration, in seconds, associated with this
              material detection.

          g_bar: Chemical Agent Monitor (CAM) G-type agent measurement, in number of display
              bars. In G-mode, CAMs monitor for G-series nerve agents.

          harmful: Flag indicating whether this detection is harmful to humans.

          h_bar: Chemical Agent Monitor (CAM) H-type agent measurement, in number of display
              bars. In H-mode, CAMs monitor for blister agents.

          id_poi: ID of the Point of Interest (POI) record related to this hazard record.

          id_track: ID of the Track record related to this hazard record.

          mass_frac: Ratio of the chemical substance mass to the total mass of the mixture.

          mat_cat: The Radiological Category (1 - 5) which applies to the material associated with
              this detection, according to the following definitions:

              Category 1: If not safely or securely managed, would be likely to cause
              permanent injury to a person who handled them or was otherwise in contact with
              them for more than a few minutes. It would probably be fatal to be close to this
              amount of unshielded material for a period of a few minutes to an hour.

              Category 2: If not safely or securely managed, could cause permanent injury to a
              person who handled them or was otherwise in contact with them for a short time
              (minutes to hours). It could possibly be fatal to be close to this amount of
              unshielded radioactive material for a period of hours to days.

              Category 3: If not safely or securely managed, could cause permanent injury to a
              person who handled them or was otherwise in contact with them for hours. It
              could possibly - although it is unlikely to be - fatal to be close to this
              amount of unshielded radioactive material for a period of days to weeks.

              Category 4: If not safely managed or securely protected, could possibly cause
              temporary injury to someone who handled them or was otherwise in contact with or
              close to them for a period of many weeks, though this is unlikely. It is very
              unlikely anyone would be permanently injured by this amount of radioactive
              material.

              Category 5: Cannot cause permanent injury. This category applies to x-ray
              fluorescence devices and electron capture devices.

          mat_class: The specific Material Class for the material associated with this detect. The
              material class is generally associated with chemical and biological detections.

          mat_name: The material common name associated with this detection.

          mat_type: The specific material type (MT) or MT Code involved in this detection, when
              applicable. The material type is generally associated with radiological and/or
              nuclear detections. For further information, reference Nuclear Materials
              Management and Safeguards System (NMMSS) Users Guide Rev. 2.1.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          ppm: Measure of the concentration of the material associated with this detection, in
              parts per million (units of contaminant mass per million parts of total mass).

          rad_ctrn: Measure of radioactive concentration of the material associated with this
              detection, in becquerels/m^3. One becquerel (Bq) is equal to one nuclear decay
              per second.

          readings: Array of the specific readings associated with this detection. The readings,
              readingUnits, and readingValues arrays must contain the same number of elements.

          reading_units: Array of the units that correspond to each of the readingValues. The readings,
              readingUnits, and readingValues arrays must contain the same number of elements.

          reading_values: Array of the values that correspond to each of the readings contained in
              readings. The readings, readingUnits, and readingValues arrays must contain the
              same number of elements.

          z: The Atomic Number of the material associated with this detection.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/udl/hazard",
            body=maybe_transform(
                {
                    "alarms": alarms,
                    "alarm_values": alarm_values,
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "detect_time": detect_time,
                    "detect_type": detect_type,
                    "source": source,
                    "id": id,
                    "a": a,
                    "activity": activity,
                    "bottle_id": bottle_id,
                    "cas_rn": cas_rn,
                    "channel": channel,
                    "ctrn_time": ctrn_time,
                    "density": density,
                    "dep": dep,
                    "dep_ctrn": dep_ctrn,
                    "dose": dose,
                    "dose_rate": dose_rate,
                    "duration": duration,
                    "g_bar": g_bar,
                    "harmful": harmful,
                    "h_bar": h_bar,
                    "id_poi": id_poi,
                    "id_track": id_track,
                    "mass_frac": mass_frac,
                    "mat_cat": mat_cat,
                    "mat_class": mat_class,
                    "mat_name": mat_name,
                    "mat_type": mat_type,
                    "origin": origin,
                    "ppm": ppm,
                    "rad_ctrn": rad_ctrn,
                    "readings": readings,
                    "reading_units": reading_units,
                    "reading_values": reading_values,
                    "z": z,
                },
                hazard_create_params.HazardCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        *,
        detect_time: Union[str, datetime],
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncOffsetPage[HazardListResponse]:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          detect_time: The detect time, in ISO 8601 UTC format, with millisecond precision.
              (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/hazard",
            page=SyncOffsetPage[HazardListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "detect_time": detect_time,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    hazard_list_params.HazardListParams,
                ),
            ),
            model=HazardListResponse,
        )

    def count(
        self,
        *,
        detect_time: Union[str, datetime],
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
          detect_time: The detect time, in ISO 8601 UTC format, with millisecond precision.
              (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return self._get(
            "/udl/hazard/count",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "detect_time": detect_time,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    hazard_count_params.HazardCountParams,
                ),
            ),
            cast_to=str,
        )

    def create_bulk(
        self,
        *,
        body: Iterable[hazard_create_bulk_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation intended for initial integration only, to take a list of
        hazards as a POST body and ingest into the database. This operation is not
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
            "/udl/hazard/createBulk",
            body=maybe_transform(body, Iterable[hazard_create_bulk_params.Body]),
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
    ) -> HazardGetResponse:
        """
        Service operation to get a single Hazard by its unique ID passed as a path
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
            f"/udl/hazard/{id}",
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
                    hazard_get_params.HazardGetParams,
                ),
            ),
            cast_to=HazardGetResponse,
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
            "/udl/hazard/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def tuple(
        self,
        *,
        columns: str,
        detect_time: Union[str, datetime],
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> HazardTupleResponse:
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

          detect_time: The detect time, in ISO 8601 UTC format, with millisecond precision.
              (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/udl/hazard/tuple",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "columns": columns,
                        "detect_time": detect_time,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    hazard_tuple_params.HazardTupleParams,
                ),
            ),
            cast_to=HazardTupleResponse,
        )


class AsyncHazardResource(AsyncAPIResource):
    @cached_property
    def history(self) -> AsyncHistoryResource:
        return AsyncHistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncHazardResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncHazardResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHazardResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncHazardResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        alarms: List[str],
        alarm_values: Iterable[float],
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        detect_time: Union[str, datetime],
        detect_type: str,
        source: str,
        id: str | NotGiven = NOT_GIVEN,
        a: int | NotGiven = NOT_GIVEN,
        activity: float | NotGiven = NOT_GIVEN,
        bottle_id: str | NotGiven = NOT_GIVEN,
        cas_rn: str | NotGiven = NOT_GIVEN,
        channel: str | NotGiven = NOT_GIVEN,
        ctrn_time: float | NotGiven = NOT_GIVEN,
        density: float | NotGiven = NOT_GIVEN,
        dep: float | NotGiven = NOT_GIVEN,
        dep_ctrn: float | NotGiven = NOT_GIVEN,
        dose: float | NotGiven = NOT_GIVEN,
        dose_rate: float | NotGiven = NOT_GIVEN,
        duration: int | NotGiven = NOT_GIVEN,
        g_bar: float | NotGiven = NOT_GIVEN,
        harmful: bool | NotGiven = NOT_GIVEN,
        h_bar: float | NotGiven = NOT_GIVEN,
        id_poi: str | NotGiven = NOT_GIVEN,
        id_track: str | NotGiven = NOT_GIVEN,
        mass_frac: float | NotGiven = NOT_GIVEN,
        mat_cat: int | NotGiven = NOT_GIVEN,
        mat_class: str | NotGiven = NOT_GIVEN,
        mat_name: str | NotGiven = NOT_GIVEN,
        mat_type: str | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        ppm: int | NotGiven = NOT_GIVEN,
        rad_ctrn: float | NotGiven = NOT_GIVEN,
        readings: List[str] | NotGiven = NOT_GIVEN,
        reading_units: List[str] | NotGiven = NOT_GIVEN,
        reading_values: Iterable[float] | NotGiven = NOT_GIVEN,
        z: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single hazard as a POST body and ingest into the
        database. This operation is not intended to be used for automated feeds into
        UDL. Data providers should contact the UDL team for specific role assignments
        and for instructions on setting up a permanent feed through an alternate
        mechanism.

        Args:
          alarms: Array of the specific alarms associated with this detection. The alarms and
              alarmValues arrays must contain the same number of elements.

          alarm_values: Array of the values that correspond to each of the alarms contained in alarms.
              The alarms and alarmValues arrays must contain the same number of elements.

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

          detect_time: The detect time, in ISO 8601 UTC format, with millisecond precision.

          detect_type: The type of hazard (Chemical, Biological, Radiological, Nuclear) detect
              associated with this record.

          source: Source of the data.

          id: Unique identifier of the record, auto-generated by the system.

          a: The (rounded) Mass Number of the material associated with this detection. The
              rounded value is the mass number of the most abundant isotope of the element.

          activity: The radioactivity measurement of the material associated with this detection, in
              becquerels (Bq). One becquerel (Bq) is equal to one nuclear decay per second.

          bottle_id: The specific bottle ID associated with this detection.

          cas_rn: The CAS Registry Number, also referred to as CAS Number or CAS RN, associated
              with the this detection. The CAS Number is a unique numerical identifier
              assigned by the Chemical Abstracts Service (CAS), to every chemical substance
              described in the open scientific literature. It includes organic and inorganic
              compounds, minerals, isotopes, alloys, mixtures, and nonstructurable materials
              (UVCBs, substances of unknown or variable composition, complex reaction
              products, or biological origin). For further information, reference
              https://www.cas.org/cas-data/cas-registry.

          channel: The applicable channel involved in this biological material detection (e.g.
              Digestive, Eyes, Respiratory, Skin, etc.) .

          ctrn_time: The concentration time, in (kg/sec)/m^3, associated with this material
              detection.

          density: Measure of density of the material associated with this detection, in kg/m^3.

          dep: The deposition measurement of the contaminant to surface area, in kg/m^2.

          dep_ctrn: The deposition concentration of the contaminant to surface area, in
              becquerels/m^2.

          dose: The dose associated with this detection, in gray. Dose is the measure of the
              energy deposited in matter by ionizing radiation per unit mass. One gray is
              defined as one Joule of energy absorbed per kilogram of matter.

          dose_rate: The dose rate associated with this detection, in gray/sec. One gray is defined
              as one Joule of energy absorbed per kilogram of matter.

          duration: The known or projected hazard duration, in seconds, associated with this
              material detection.

          g_bar: Chemical Agent Monitor (CAM) G-type agent measurement, in number of display
              bars. In G-mode, CAMs monitor for G-series nerve agents.

          harmful: Flag indicating whether this detection is harmful to humans.

          h_bar: Chemical Agent Monitor (CAM) H-type agent measurement, in number of display
              bars. In H-mode, CAMs monitor for blister agents.

          id_poi: ID of the Point of Interest (POI) record related to this hazard record.

          id_track: ID of the Track record related to this hazard record.

          mass_frac: Ratio of the chemical substance mass to the total mass of the mixture.

          mat_cat: The Radiological Category (1 - 5) which applies to the material associated with
              this detection, according to the following definitions:

              Category 1: If not safely or securely managed, would be likely to cause
              permanent injury to a person who handled them or was otherwise in contact with
              them for more than a few minutes. It would probably be fatal to be close to this
              amount of unshielded material for a period of a few minutes to an hour.

              Category 2: If not safely or securely managed, could cause permanent injury to a
              person who handled them or was otherwise in contact with them for a short time
              (minutes to hours). It could possibly be fatal to be close to this amount of
              unshielded radioactive material for a period of hours to days.

              Category 3: If not safely or securely managed, could cause permanent injury to a
              person who handled them or was otherwise in contact with them for hours. It
              could possibly - although it is unlikely to be - fatal to be close to this
              amount of unshielded radioactive material for a period of days to weeks.

              Category 4: If not safely managed or securely protected, could possibly cause
              temporary injury to someone who handled them or was otherwise in contact with or
              close to them for a period of many weeks, though this is unlikely. It is very
              unlikely anyone would be permanently injured by this amount of radioactive
              material.

              Category 5: Cannot cause permanent injury. This category applies to x-ray
              fluorescence devices and electron capture devices.

          mat_class: The specific Material Class for the material associated with this detect. The
              material class is generally associated with chemical and biological detections.

          mat_name: The material common name associated with this detection.

          mat_type: The specific material type (MT) or MT Code involved in this detection, when
              applicable. The material type is generally associated with radiological and/or
              nuclear detections. For further information, reference Nuclear Materials
              Management and Safeguards System (NMMSS) Users Guide Rev. 2.1.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          ppm: Measure of the concentration of the material associated with this detection, in
              parts per million (units of contaminant mass per million parts of total mass).

          rad_ctrn: Measure of radioactive concentration of the material associated with this
              detection, in becquerels/m^3. One becquerel (Bq) is equal to one nuclear decay
              per second.

          readings: Array of the specific readings associated with this detection. The readings,
              readingUnits, and readingValues arrays must contain the same number of elements.

          reading_units: Array of the units that correspond to each of the readingValues. The readings,
              readingUnits, and readingValues arrays must contain the same number of elements.

          reading_values: Array of the values that correspond to each of the readings contained in
              readings. The readings, readingUnits, and readingValues arrays must contain the
              same number of elements.

          z: The Atomic Number of the material associated with this detection.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/udl/hazard",
            body=await async_maybe_transform(
                {
                    "alarms": alarms,
                    "alarm_values": alarm_values,
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "detect_time": detect_time,
                    "detect_type": detect_type,
                    "source": source,
                    "id": id,
                    "a": a,
                    "activity": activity,
                    "bottle_id": bottle_id,
                    "cas_rn": cas_rn,
                    "channel": channel,
                    "ctrn_time": ctrn_time,
                    "density": density,
                    "dep": dep,
                    "dep_ctrn": dep_ctrn,
                    "dose": dose,
                    "dose_rate": dose_rate,
                    "duration": duration,
                    "g_bar": g_bar,
                    "harmful": harmful,
                    "h_bar": h_bar,
                    "id_poi": id_poi,
                    "id_track": id_track,
                    "mass_frac": mass_frac,
                    "mat_cat": mat_cat,
                    "mat_class": mat_class,
                    "mat_name": mat_name,
                    "mat_type": mat_type,
                    "origin": origin,
                    "ppm": ppm,
                    "rad_ctrn": rad_ctrn,
                    "readings": readings,
                    "reading_units": reading_units,
                    "reading_values": reading_values,
                    "z": z,
                },
                hazard_create_params.HazardCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        *,
        detect_time: Union[str, datetime],
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[HazardListResponse, AsyncOffsetPage[HazardListResponse]]:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          detect_time: The detect time, in ISO 8601 UTC format, with millisecond precision.
              (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/hazard",
            page=AsyncOffsetPage[HazardListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "detect_time": detect_time,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    hazard_list_params.HazardListParams,
                ),
            ),
            model=HazardListResponse,
        )

    async def count(
        self,
        *,
        detect_time: Union[str, datetime],
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
          detect_time: The detect time, in ISO 8601 UTC format, with millisecond precision.
              (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return await self._get(
            "/udl/hazard/count",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "detect_time": detect_time,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    hazard_count_params.HazardCountParams,
                ),
            ),
            cast_to=str,
        )

    async def create_bulk(
        self,
        *,
        body: Iterable[hazard_create_bulk_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation intended for initial integration only, to take a list of
        hazards as a POST body and ingest into the database. This operation is not
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
            "/udl/hazard/createBulk",
            body=await async_maybe_transform(body, Iterable[hazard_create_bulk_params.Body]),
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
    ) -> HazardGetResponse:
        """
        Service operation to get a single Hazard by its unique ID passed as a path
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
            f"/udl/hazard/{id}",
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
                    hazard_get_params.HazardGetParams,
                ),
            ),
            cast_to=HazardGetResponse,
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
            "/udl/hazard/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def tuple(
        self,
        *,
        columns: str,
        detect_time: Union[str, datetime],
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> HazardTupleResponse:
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

          detect_time: The detect time, in ISO 8601 UTC format, with millisecond precision.
              (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/udl/hazard/tuple",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "columns": columns,
                        "detect_time": detect_time,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    hazard_tuple_params.HazardTupleParams,
                ),
            ),
            cast_to=HazardTupleResponse,
        )


class HazardResourceWithRawResponse:
    def __init__(self, hazard: HazardResource) -> None:
        self._hazard = hazard

        self.create = to_raw_response_wrapper(
            hazard.create,
        )
        self.list = to_raw_response_wrapper(
            hazard.list,
        )
        self.count = to_raw_response_wrapper(
            hazard.count,
        )
        self.create_bulk = to_raw_response_wrapper(
            hazard.create_bulk,
        )
        self.get = to_raw_response_wrapper(
            hazard.get,
        )
        self.queryhelp = to_raw_response_wrapper(
            hazard.queryhelp,
        )
        self.tuple = to_raw_response_wrapper(
            hazard.tuple,
        )

    @cached_property
    def history(self) -> HistoryResourceWithRawResponse:
        return HistoryResourceWithRawResponse(self._hazard.history)


class AsyncHazardResourceWithRawResponse:
    def __init__(self, hazard: AsyncHazardResource) -> None:
        self._hazard = hazard

        self.create = async_to_raw_response_wrapper(
            hazard.create,
        )
        self.list = async_to_raw_response_wrapper(
            hazard.list,
        )
        self.count = async_to_raw_response_wrapper(
            hazard.count,
        )
        self.create_bulk = async_to_raw_response_wrapper(
            hazard.create_bulk,
        )
        self.get = async_to_raw_response_wrapper(
            hazard.get,
        )
        self.queryhelp = async_to_raw_response_wrapper(
            hazard.queryhelp,
        )
        self.tuple = async_to_raw_response_wrapper(
            hazard.tuple,
        )

    @cached_property
    def history(self) -> AsyncHistoryResourceWithRawResponse:
        return AsyncHistoryResourceWithRawResponse(self._hazard.history)


class HazardResourceWithStreamingResponse:
    def __init__(self, hazard: HazardResource) -> None:
        self._hazard = hazard

        self.create = to_streamed_response_wrapper(
            hazard.create,
        )
        self.list = to_streamed_response_wrapper(
            hazard.list,
        )
        self.count = to_streamed_response_wrapper(
            hazard.count,
        )
        self.create_bulk = to_streamed_response_wrapper(
            hazard.create_bulk,
        )
        self.get = to_streamed_response_wrapper(
            hazard.get,
        )
        self.queryhelp = to_streamed_response_wrapper(
            hazard.queryhelp,
        )
        self.tuple = to_streamed_response_wrapper(
            hazard.tuple,
        )

    @cached_property
    def history(self) -> HistoryResourceWithStreamingResponse:
        return HistoryResourceWithStreamingResponse(self._hazard.history)


class AsyncHazardResourceWithStreamingResponse:
    def __init__(self, hazard: AsyncHazardResource) -> None:
        self._hazard = hazard

        self.create = async_to_streamed_response_wrapper(
            hazard.create,
        )
        self.list = async_to_streamed_response_wrapper(
            hazard.list,
        )
        self.count = async_to_streamed_response_wrapper(
            hazard.count,
        )
        self.create_bulk = async_to_streamed_response_wrapper(
            hazard.create_bulk,
        )
        self.get = async_to_streamed_response_wrapper(
            hazard.get,
        )
        self.queryhelp = async_to_streamed_response_wrapper(
            hazard.queryhelp,
        )
        self.tuple = async_to_streamed_response_wrapper(
            hazard.tuple,
        )

    @cached_property
    def history(self) -> AsyncHistoryResourceWithStreamingResponse:
        return AsyncHistoryResourceWithStreamingResponse(self._hazard.history)
