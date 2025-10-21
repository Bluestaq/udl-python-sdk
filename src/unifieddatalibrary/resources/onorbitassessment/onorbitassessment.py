# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime
from typing_extensions import Literal

import httpx

from ...types import (
    onorbitassessment_get_params,
    onorbitassessment_list_params,
    onorbitassessment_count_params,
    onorbitassessment_tuple_params,
    onorbitassessment_create_params,
    onorbitassessment_create_bulk_params,
    onorbitassessment_unvalidated_publish_params,
)
from .history import (
    HistoryResource,
    AsyncHistoryResource,
    HistoryResourceWithRawResponse,
    AsyncHistoryResourceWithRawResponse,
    HistoryResourceWithStreamingResponse,
    AsyncHistoryResourceWithStreamingResponse,
)
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
from ...types.onorbitassessment_get_response import OnorbitassessmentGetResponse
from ...types.onorbitassessment_list_response import OnorbitassessmentListResponse
from ...types.onorbitassessment_tuple_response import OnorbitassessmentTupleResponse
from ...types.onorbitassessment_queryhelp_response import OnorbitassessmentQueryhelpResponse

__all__ = ["OnorbitassessmentResource", "AsyncOnorbitassessmentResource"]


class OnorbitassessmentResource(SyncAPIResource):
    @cached_property
    def history(self) -> HistoryResource:
        return HistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> OnorbitassessmentResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return OnorbitassessmentResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OnorbitassessmentResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return OnorbitassessmentResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        assmt_time: Union[str, datetime],
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        source: str,
        id: str | Omit = omit,
        assessment: str | Omit = omit,
        assmt_details: str | Omit = omit,
        assmt_level: str | Omit = omit,
        assmt_rot_period: float | Omit = omit,
        assmt_sub_type: str | Omit = omit,
        assmt_url: str | Omit = omit,
        auto_assmt: bool | Omit = omit,
        collection_url: str | Omit = omit,
        components: SequenceNotStr[str] | Omit = omit,
        id_on_orbit: str | Omit = omit,
        id_sensor: str | Omit = omit,
        ob_duration: float | Omit = omit,
        ob_time: Union[str, datetime] | Omit = omit,
        origin: str | Omit = omit,
        orig_object_id: str | Omit = omit,
        orig_sensor_id: str | Omit = omit,
        sat_no: int | Omit = omit,
        sig_data_type: str | Omit = omit,
        src_ids: SequenceNotStr[str] | Omit = omit,
        src_typs: SequenceNotStr[str] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        transaction_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Service operation to take a single OnorbitAssessment as a POST body and ingest
        into the database. A specific role is required to perform this service
        operation. Please contact the UDL team for assistance.

        Args:
          assmt_time: The time of the assessment, in ISO 8601 UTC format with millisecond precision.

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

          assessment: The overall assessment of the on-orbit object. The assessment will vary
              depending on the assessment level. If assmtLevel = SATELLITE, then expected
              values include HEALTHY, NO DATA, UNHEALTHY, and UNKNOWN. If assmtLevel =
              SIGNATURE, then expected values include ANOMALOUS, BAD, NOMINAL, and UNKNOWN.

          assmt_details: Comments and details concerning this assessment.

          assmt_level: The level (SATELLITE, SIGNATURE) of this assessment.

          assmt_rot_period: The rotational period, in seconds, determined in the assessment of the on-orbit
              object.

          assmt_sub_type: The sub-type for this assessment. The sub-type provides an additional level of
              specification when the assessment level = SIGNATURE, and will vary based on the
              overall assessment. If assessment = ANOMALOUS, then expected values include
              ACTIVITY OBSERVED, BAD CONFIGURATION, MANEUVERING, OTHER, POSSIBLE SAFE MODE,
              UNSTABLE, and WRONG ATTITUDE. If assessment = BAD, then expected values include
              BAD-MISSING STATE VECTOR, CORRUPT-NOISY, CROSS-TAG, DROPOUTS, INSUFFICIENT DATA,
              INSUFFICIENT LOOK ANGLE, NO CROSSOVER, and SHORT. If assessment = NOMINAL, then
              expected values include ACTIVITY OBSERVED, GRAVITY GRADIENT, HORIZON STABLE,
              INERTIAL, MANEUVERING, SPIN STABLE, and STABLE. If assessment = UNKNOWN, then
              expected values include NO COHORT, and OTHER.

          assmt_url: URL to an external location containing additional assessment information.

          auto_assmt: Flag indicating whether this assessment was auto-generated (true) or produced by
              an analyst.

          collection_url: URL to an external location containing the data that was used to make this
              assessment.

          components: Array of the affected spacecraft component(s) relevant to this assessment, if
              non-nominal.

          id_on_orbit: Unique identifier of the target satellite on-orbit object to which this
              assessment applies. This ID can be used to obtain additional information on an
              OnOrbit object using the 'get by ID' operation (e.g. /udl/onorbit/{id}). For
              example, the OnOrbit with idOnOrbit = 25544 would be queried as
              /udl/onorbit/25544.

          id_sensor: Unique identifier of the sensor from which the signature data applied in this
              assessment was collected. This ID can be used to obtain additional information
              on a sensor using the 'get by ID' operation (e.g. /udl/sensor/{id}). For
              example, the sensor with idSensor = abc would be queried as /udl/sensor/abc.

          ob_duration: The total duration, in hours, of the signature or set of signatures used to
              create this assessment.

          ob_time: The observation time, in ISO 8601 UTC format with millisecond precision. For
              non-instantaneous collections, the observation time will correspond to the
              earliest timestamp in the signature or signature set data.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          orig_object_id: Optional identifier provided by the source to indicate the target on-orbit
              object to which this assessment applies. This may be an internal identifier and
              not necessarily map to a valid satellite number.

          orig_sensor_id: Optional identifier provided by the observation source to indicate the sensor
              which produced this observation. This may be an internal identifier and not
              necessarily a valid sensor ID.

          sat_no: Satellite/Catalog number of the target on-orbit object to which this assessment
              applies.

          sig_data_type: The observation data type (LONG DWELL, NARROWBAND, PHOTOMETRIC POL, PHOTOMETRY,
              RANGE PROFILER, WIDEBAND, etc.) contained in the signature. Applies when
              assmtLevel = SIGNATURE.

          src_ids: Array of UUIDs of the UDL data records that are related to this assessment. See
              the associated 'srcTyps' array for the specific types of data, positionally
              corresponding to the UUIDs in this array. The 'srcTyps' and 'srcIds' arrays must
              match in size. See the corresponding srcTyps array element for the data type of
              the UUID and use the appropriate API operation to retrieve that object.

          src_typs: Array of UDL record types (DOA, ELSET, EO, ESID, GROUNDIMAGE, POI, MANEUVER,
              MTI, RADAR, RF, SIGACT, SKYIMAGE, SV, TRACK, etc.) that are related to this
              assessment. See the associated 'srcIds' array for the record UUIDs, positionally
              corresponding to the record types in this array. The 'srcTyps' and 'srcIds'
              arrays must match in size.

          tags: Optional array of provider/source specific tags for this data, where each
              element is no longer than 32 characters, used for implementing data owner
              conditional access controls to restrict access to the data. Should be left null
              by data providers unless conditional access controls are coordinated with the
              UDL team.

          transaction_id: Optional identifier to track a commercial or marketplace transaction executed to
              produce this data.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/udl/onorbitassessment",
            body=maybe_transform(
                {
                    "assmt_time": assmt_time,
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "source": source,
                    "id": id,
                    "assessment": assessment,
                    "assmt_details": assmt_details,
                    "assmt_level": assmt_level,
                    "assmt_rot_period": assmt_rot_period,
                    "assmt_sub_type": assmt_sub_type,
                    "assmt_url": assmt_url,
                    "auto_assmt": auto_assmt,
                    "collection_url": collection_url,
                    "components": components,
                    "id_on_orbit": id_on_orbit,
                    "id_sensor": id_sensor,
                    "ob_duration": ob_duration,
                    "ob_time": ob_time,
                    "origin": origin,
                    "orig_object_id": orig_object_id,
                    "orig_sensor_id": orig_sensor_id,
                    "sat_no": sat_no,
                    "sig_data_type": sig_data_type,
                    "src_ids": src_ids,
                    "src_typs": src_typs,
                    "tags": tags,
                    "transaction_id": transaction_id,
                },
                onorbitassessment_create_params.OnorbitassessmentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        *,
        assmt_time: Union[str, datetime],
        first_result: int | Omit = omit,
        max_results: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncOffsetPage[OnorbitassessmentListResponse]:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          assmt_time: The time of the assessment, in ISO 8601 UTC format with millisecond precision.
              (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/onorbitassessment",
            page=SyncOffsetPage[OnorbitassessmentListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "assmt_time": assmt_time,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    onorbitassessment_list_params.OnorbitassessmentListParams,
                ),
            ),
            model=OnorbitassessmentListResponse,
        )

    def count(
        self,
        *,
        assmt_time: Union[str, datetime],
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
          assmt_time: The time of the assessment, in ISO 8601 UTC format with millisecond precision.
              (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return self._get(
            "/udl/onorbitassessment/count",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "assmt_time": assmt_time,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    onorbitassessment_count_params.OnorbitassessmentCountParams,
                ),
            ),
            cast_to=str,
        )

    def create_bulk(
        self,
        *,
        body: Iterable[onorbitassessment_create_bulk_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Service operation intended for initial integration only, to take a list of
        OnorbitAssessment records as a POST body and ingest into the database. This
        operation is not intended to be used for automated feeds into UDL. Data
        providers should contact the UDL team for specific role assignments and for
        instructions on setting up a permanent feed through an alternate mechanism.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/udl/onorbitassessment/createBulk",
            body=maybe_transform(body, Iterable[onorbitassessment_create_bulk_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
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
    ) -> OnorbitassessmentGetResponse:
        """
        Service operation to get a single OnorbitAssessment record by its unique ID
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
            f"/udl/onorbitassessment/{id}",
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
                    onorbitassessment_get_params.OnorbitassessmentGetParams,
                ),
            ),
            cast_to=OnorbitassessmentGetResponse,
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
    ) -> OnorbitassessmentQueryhelpResponse:
        """
        Service operation to provide detailed information on available dynamic query
        parameters for a particular data type.
        """
        return self._get(
            "/udl/onorbitassessment/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OnorbitassessmentQueryhelpResponse,
        )

    def tuple(
        self,
        *,
        assmt_time: Union[str, datetime],
        columns: str,
        first_result: int | Omit = omit,
        max_results: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OnorbitassessmentTupleResponse:
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
          assmt_time: The time of the assessment, in ISO 8601 UTC format with millisecond precision.
              (YYYY-MM-DDTHH:MM:SS.sssZ)

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
            "/udl/onorbitassessment/tuple",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "assmt_time": assmt_time,
                        "columns": columns,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    onorbitassessment_tuple_params.OnorbitassessmentTupleParams,
                ),
            ),
            cast_to=OnorbitassessmentTupleResponse,
        )

    def unvalidated_publish(
        self,
        *,
        body: Iterable[onorbitassessment_unvalidated_publish_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Service operation to take multiple OnorbitAssessment records as a POST body and
        ingest into the database. This operation is intended to be used for automated
        feeds into UDL. A specific role is required to perform this service operation.
        Please contact the UDL team for assistance.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/filedrop/udl-onorbitassessment",
            body=maybe_transform(body, Iterable[onorbitassessment_unvalidated_publish_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncOnorbitassessmentResource(AsyncAPIResource):
    @cached_property
    def history(self) -> AsyncHistoryResource:
        return AsyncHistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncOnorbitassessmentResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncOnorbitassessmentResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOnorbitassessmentResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncOnorbitassessmentResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        assmt_time: Union[str, datetime],
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        source: str,
        id: str | Omit = omit,
        assessment: str | Omit = omit,
        assmt_details: str | Omit = omit,
        assmt_level: str | Omit = omit,
        assmt_rot_period: float | Omit = omit,
        assmt_sub_type: str | Omit = omit,
        assmt_url: str | Omit = omit,
        auto_assmt: bool | Omit = omit,
        collection_url: str | Omit = omit,
        components: SequenceNotStr[str] | Omit = omit,
        id_on_orbit: str | Omit = omit,
        id_sensor: str | Omit = omit,
        ob_duration: float | Omit = omit,
        ob_time: Union[str, datetime] | Omit = omit,
        origin: str | Omit = omit,
        orig_object_id: str | Omit = omit,
        orig_sensor_id: str | Omit = omit,
        sat_no: int | Omit = omit,
        sig_data_type: str | Omit = omit,
        src_ids: SequenceNotStr[str] | Omit = omit,
        src_typs: SequenceNotStr[str] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        transaction_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Service operation to take a single OnorbitAssessment as a POST body and ingest
        into the database. A specific role is required to perform this service
        operation. Please contact the UDL team for assistance.

        Args:
          assmt_time: The time of the assessment, in ISO 8601 UTC format with millisecond precision.

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

          assessment: The overall assessment of the on-orbit object. The assessment will vary
              depending on the assessment level. If assmtLevel = SATELLITE, then expected
              values include HEALTHY, NO DATA, UNHEALTHY, and UNKNOWN. If assmtLevel =
              SIGNATURE, then expected values include ANOMALOUS, BAD, NOMINAL, and UNKNOWN.

          assmt_details: Comments and details concerning this assessment.

          assmt_level: The level (SATELLITE, SIGNATURE) of this assessment.

          assmt_rot_period: The rotational period, in seconds, determined in the assessment of the on-orbit
              object.

          assmt_sub_type: The sub-type for this assessment. The sub-type provides an additional level of
              specification when the assessment level = SIGNATURE, and will vary based on the
              overall assessment. If assessment = ANOMALOUS, then expected values include
              ACTIVITY OBSERVED, BAD CONFIGURATION, MANEUVERING, OTHER, POSSIBLE SAFE MODE,
              UNSTABLE, and WRONG ATTITUDE. If assessment = BAD, then expected values include
              BAD-MISSING STATE VECTOR, CORRUPT-NOISY, CROSS-TAG, DROPOUTS, INSUFFICIENT DATA,
              INSUFFICIENT LOOK ANGLE, NO CROSSOVER, and SHORT. If assessment = NOMINAL, then
              expected values include ACTIVITY OBSERVED, GRAVITY GRADIENT, HORIZON STABLE,
              INERTIAL, MANEUVERING, SPIN STABLE, and STABLE. If assessment = UNKNOWN, then
              expected values include NO COHORT, and OTHER.

          assmt_url: URL to an external location containing additional assessment information.

          auto_assmt: Flag indicating whether this assessment was auto-generated (true) or produced by
              an analyst.

          collection_url: URL to an external location containing the data that was used to make this
              assessment.

          components: Array of the affected spacecraft component(s) relevant to this assessment, if
              non-nominal.

          id_on_orbit: Unique identifier of the target satellite on-orbit object to which this
              assessment applies. This ID can be used to obtain additional information on an
              OnOrbit object using the 'get by ID' operation (e.g. /udl/onorbit/{id}). For
              example, the OnOrbit with idOnOrbit = 25544 would be queried as
              /udl/onorbit/25544.

          id_sensor: Unique identifier of the sensor from which the signature data applied in this
              assessment was collected. This ID can be used to obtain additional information
              on a sensor using the 'get by ID' operation (e.g. /udl/sensor/{id}). For
              example, the sensor with idSensor = abc would be queried as /udl/sensor/abc.

          ob_duration: The total duration, in hours, of the signature or set of signatures used to
              create this assessment.

          ob_time: The observation time, in ISO 8601 UTC format with millisecond precision. For
              non-instantaneous collections, the observation time will correspond to the
              earliest timestamp in the signature or signature set data.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          orig_object_id: Optional identifier provided by the source to indicate the target on-orbit
              object to which this assessment applies. This may be an internal identifier and
              not necessarily map to a valid satellite number.

          orig_sensor_id: Optional identifier provided by the observation source to indicate the sensor
              which produced this observation. This may be an internal identifier and not
              necessarily a valid sensor ID.

          sat_no: Satellite/Catalog number of the target on-orbit object to which this assessment
              applies.

          sig_data_type: The observation data type (LONG DWELL, NARROWBAND, PHOTOMETRIC POL, PHOTOMETRY,
              RANGE PROFILER, WIDEBAND, etc.) contained in the signature. Applies when
              assmtLevel = SIGNATURE.

          src_ids: Array of UUIDs of the UDL data records that are related to this assessment. See
              the associated 'srcTyps' array for the specific types of data, positionally
              corresponding to the UUIDs in this array. The 'srcTyps' and 'srcIds' arrays must
              match in size. See the corresponding srcTyps array element for the data type of
              the UUID and use the appropriate API operation to retrieve that object.

          src_typs: Array of UDL record types (DOA, ELSET, EO, ESID, GROUNDIMAGE, POI, MANEUVER,
              MTI, RADAR, RF, SIGACT, SKYIMAGE, SV, TRACK, etc.) that are related to this
              assessment. See the associated 'srcIds' array for the record UUIDs, positionally
              corresponding to the record types in this array. The 'srcTyps' and 'srcIds'
              arrays must match in size.

          tags: Optional array of provider/source specific tags for this data, where each
              element is no longer than 32 characters, used for implementing data owner
              conditional access controls to restrict access to the data. Should be left null
              by data providers unless conditional access controls are coordinated with the
              UDL team.

          transaction_id: Optional identifier to track a commercial or marketplace transaction executed to
              produce this data.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/udl/onorbitassessment",
            body=await async_maybe_transform(
                {
                    "assmt_time": assmt_time,
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "source": source,
                    "id": id,
                    "assessment": assessment,
                    "assmt_details": assmt_details,
                    "assmt_level": assmt_level,
                    "assmt_rot_period": assmt_rot_period,
                    "assmt_sub_type": assmt_sub_type,
                    "assmt_url": assmt_url,
                    "auto_assmt": auto_assmt,
                    "collection_url": collection_url,
                    "components": components,
                    "id_on_orbit": id_on_orbit,
                    "id_sensor": id_sensor,
                    "ob_duration": ob_duration,
                    "ob_time": ob_time,
                    "origin": origin,
                    "orig_object_id": orig_object_id,
                    "orig_sensor_id": orig_sensor_id,
                    "sat_no": sat_no,
                    "sig_data_type": sig_data_type,
                    "src_ids": src_ids,
                    "src_typs": src_typs,
                    "tags": tags,
                    "transaction_id": transaction_id,
                },
                onorbitassessment_create_params.OnorbitassessmentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        *,
        assmt_time: Union[str, datetime],
        first_result: int | Omit = omit,
        max_results: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[OnorbitassessmentListResponse, AsyncOffsetPage[OnorbitassessmentListResponse]]:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          assmt_time: The time of the assessment, in ISO 8601 UTC format with millisecond precision.
              (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/onorbitassessment",
            page=AsyncOffsetPage[OnorbitassessmentListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "assmt_time": assmt_time,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    onorbitassessment_list_params.OnorbitassessmentListParams,
                ),
            ),
            model=OnorbitassessmentListResponse,
        )

    async def count(
        self,
        *,
        assmt_time: Union[str, datetime],
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
          assmt_time: The time of the assessment, in ISO 8601 UTC format with millisecond precision.
              (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return await self._get(
            "/udl/onorbitassessment/count",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "assmt_time": assmt_time,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    onorbitassessment_count_params.OnorbitassessmentCountParams,
                ),
            ),
            cast_to=str,
        )

    async def create_bulk(
        self,
        *,
        body: Iterable[onorbitassessment_create_bulk_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Service operation intended for initial integration only, to take a list of
        OnorbitAssessment records as a POST body and ingest into the database. This
        operation is not intended to be used for automated feeds into UDL. Data
        providers should contact the UDL team for specific role assignments and for
        instructions on setting up a permanent feed through an alternate mechanism.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/udl/onorbitassessment/createBulk",
            body=await async_maybe_transform(body, Iterable[onorbitassessment_create_bulk_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
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
    ) -> OnorbitassessmentGetResponse:
        """
        Service operation to get a single OnorbitAssessment record by its unique ID
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
            f"/udl/onorbitassessment/{id}",
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
                    onorbitassessment_get_params.OnorbitassessmentGetParams,
                ),
            ),
            cast_to=OnorbitassessmentGetResponse,
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
    ) -> OnorbitassessmentQueryhelpResponse:
        """
        Service operation to provide detailed information on available dynamic query
        parameters for a particular data type.
        """
        return await self._get(
            "/udl/onorbitassessment/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OnorbitassessmentQueryhelpResponse,
        )

    async def tuple(
        self,
        *,
        assmt_time: Union[str, datetime],
        columns: str,
        first_result: int | Omit = omit,
        max_results: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OnorbitassessmentTupleResponse:
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
          assmt_time: The time of the assessment, in ISO 8601 UTC format with millisecond precision.
              (YYYY-MM-DDTHH:MM:SS.sssZ)

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
            "/udl/onorbitassessment/tuple",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "assmt_time": assmt_time,
                        "columns": columns,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    onorbitassessment_tuple_params.OnorbitassessmentTupleParams,
                ),
            ),
            cast_to=OnorbitassessmentTupleResponse,
        )

    async def unvalidated_publish(
        self,
        *,
        body: Iterable[onorbitassessment_unvalidated_publish_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Service operation to take multiple OnorbitAssessment records as a POST body and
        ingest into the database. This operation is intended to be used for automated
        feeds into UDL. A specific role is required to perform this service operation.
        Please contact the UDL team for assistance.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/filedrop/udl-onorbitassessment",
            body=await async_maybe_transform(body, Iterable[onorbitassessment_unvalidated_publish_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class OnorbitassessmentResourceWithRawResponse:
    def __init__(self, onorbitassessment: OnorbitassessmentResource) -> None:
        self._onorbitassessment = onorbitassessment

        self.create = to_raw_response_wrapper(
            onorbitassessment.create,
        )
        self.list = to_raw_response_wrapper(
            onorbitassessment.list,
        )
        self.count = to_raw_response_wrapper(
            onorbitassessment.count,
        )
        self.create_bulk = to_raw_response_wrapper(
            onorbitassessment.create_bulk,
        )
        self.get = to_raw_response_wrapper(
            onorbitassessment.get,
        )
        self.queryhelp = to_raw_response_wrapper(
            onorbitassessment.queryhelp,
        )
        self.tuple = to_raw_response_wrapper(
            onorbitassessment.tuple,
        )
        self.unvalidated_publish = to_raw_response_wrapper(
            onorbitassessment.unvalidated_publish,
        )

    @cached_property
    def history(self) -> HistoryResourceWithRawResponse:
        return HistoryResourceWithRawResponse(self._onorbitassessment.history)


class AsyncOnorbitassessmentResourceWithRawResponse:
    def __init__(self, onorbitassessment: AsyncOnorbitassessmentResource) -> None:
        self._onorbitassessment = onorbitassessment

        self.create = async_to_raw_response_wrapper(
            onorbitassessment.create,
        )
        self.list = async_to_raw_response_wrapper(
            onorbitassessment.list,
        )
        self.count = async_to_raw_response_wrapper(
            onorbitassessment.count,
        )
        self.create_bulk = async_to_raw_response_wrapper(
            onorbitassessment.create_bulk,
        )
        self.get = async_to_raw_response_wrapper(
            onorbitassessment.get,
        )
        self.queryhelp = async_to_raw_response_wrapper(
            onorbitassessment.queryhelp,
        )
        self.tuple = async_to_raw_response_wrapper(
            onorbitassessment.tuple,
        )
        self.unvalidated_publish = async_to_raw_response_wrapper(
            onorbitassessment.unvalidated_publish,
        )

    @cached_property
    def history(self) -> AsyncHistoryResourceWithRawResponse:
        return AsyncHistoryResourceWithRawResponse(self._onorbitassessment.history)


class OnorbitassessmentResourceWithStreamingResponse:
    def __init__(self, onorbitassessment: OnorbitassessmentResource) -> None:
        self._onorbitassessment = onorbitassessment

        self.create = to_streamed_response_wrapper(
            onorbitassessment.create,
        )
        self.list = to_streamed_response_wrapper(
            onorbitassessment.list,
        )
        self.count = to_streamed_response_wrapper(
            onorbitassessment.count,
        )
        self.create_bulk = to_streamed_response_wrapper(
            onorbitassessment.create_bulk,
        )
        self.get = to_streamed_response_wrapper(
            onorbitassessment.get,
        )
        self.queryhelp = to_streamed_response_wrapper(
            onorbitassessment.queryhelp,
        )
        self.tuple = to_streamed_response_wrapper(
            onorbitassessment.tuple,
        )
        self.unvalidated_publish = to_streamed_response_wrapper(
            onorbitassessment.unvalidated_publish,
        )

    @cached_property
    def history(self) -> HistoryResourceWithStreamingResponse:
        return HistoryResourceWithStreamingResponse(self._onorbitassessment.history)


class AsyncOnorbitassessmentResourceWithStreamingResponse:
    def __init__(self, onorbitassessment: AsyncOnorbitassessmentResource) -> None:
        self._onorbitassessment = onorbitassessment

        self.create = async_to_streamed_response_wrapper(
            onorbitassessment.create,
        )
        self.list = async_to_streamed_response_wrapper(
            onorbitassessment.list,
        )
        self.count = async_to_streamed_response_wrapper(
            onorbitassessment.count,
        )
        self.create_bulk = async_to_streamed_response_wrapper(
            onorbitassessment.create_bulk,
        )
        self.get = async_to_streamed_response_wrapper(
            onorbitassessment.get,
        )
        self.queryhelp = async_to_streamed_response_wrapper(
            onorbitassessment.queryhelp,
        )
        self.tuple = async_to_streamed_response_wrapper(
            onorbitassessment.tuple,
        )
        self.unvalidated_publish = async_to_streamed_response_wrapper(
            onorbitassessment.unvalidated_publish,
        )

    @cached_property
    def history(self) -> AsyncHistoryResourceWithStreamingResponse:
        return AsyncHistoryResourceWithStreamingResponse(self._onorbitassessment.history)
