# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from datetime import datetime
from typing_extensions import Literal

import httpx

from ...types import (
    feature_assessment_count_params,
    feature_assessment_query_params,
    feature_assessment_tuple_params,
    feature_assessment_create_params,
    feature_assessment_retrieve_params,
    feature_assessment_create_bulk_params,
    feature_assessment_unvalidated_publish_params,
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
from ..._base_client import make_request_options
from ...types.feature_assessment_query_response import FeatureAssessmentQueryResponse
from ...types.feature_assessment_tuple_response import FeatureAssessmentTupleResponse
from ...types.feature_assessment_retrieve_response import FeatureAssessmentRetrieveResponse
from ...types.feature_assessment_query_help_response import FeatureAssessmentQueryHelpResponse

__all__ = ["FeatureAssessmentResource", "AsyncFeatureAssessmentResource"]


class FeatureAssessmentResource(SyncAPIResource):
    @cached_property
    def history(self) -> HistoryResource:
        return HistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> FeatureAssessmentResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return FeatureAssessmentResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FeatureAssessmentResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return FeatureAssessmentResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        feature_ts: Union[str, datetime],
        feature_uo_m: str,
        id_analytic_imagery: str,
        source: str,
        id: str | NotGiven = NOT_GIVEN,
        agjson: str | NotGiven = NOT_GIVEN,
        andims: int | NotGiven = NOT_GIVEN,
        ann_lims: Iterable[Iterable[int]] | NotGiven = NOT_GIVEN,
        ann_text: List[str] | NotGiven = NOT_GIVEN,
        area: str | NotGiven = NOT_GIVEN,
        asrid: int | NotGiven = NOT_GIVEN,
        assessment: str | NotGiven = NOT_GIVEN,
        atext: str | NotGiven = NOT_GIVEN,
        atype: str | NotGiven = NOT_GIVEN,
        confidence: float | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        feature_array: Iterable[float] | NotGiven = NOT_GIVEN,
        feature_bool: bool | NotGiven = NOT_GIVEN,
        feature_string: str | NotGiven = NOT_GIVEN,
        feature_string_array: List[str] | NotGiven = NOT_GIVEN,
        feature_value: float | NotGiven = NOT_GIVEN,
        heading: float | NotGiven = NOT_GIVEN,
        height: float | NotGiven = NOT_GIVEN,
        length: float | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        speed: float | NotGiven = NOT_GIVEN,
        src_ids: List[str] | NotGiven = NOT_GIVEN,
        src_ts: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        src_typs: List[str] | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        transaction_id: str | NotGiven = NOT_GIVEN,
        type: str | NotGiven = NOT_GIVEN,
        width: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single FeatureAssessment record as a POST body and
        ingest into the database. A specific role is required to perform this service
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

          feature_ts: Datetime type value associated with this record, in ISO 8601 UTC format with
              millisecond precision.

          feature_uo_m: The Unit of Measure associated with this feature. If there are no physical units
              associated with the feature a value of NONE should be specified.

          id_analytic_imagery: Unique identifier of the Analytic Imagery associated with this Feature
              Assessment record.

          source: Source of the data.

          id: Unique identifier of the record, auto-generated by the system.

          agjson: Geographical region or polygon (lat/lon pairs), as depicted by the GeoJSON
              representation of the geometry/geography, of the feature assessment as projected
              on the ground. GeoJSON Reference: https://geojson.org/. Ignored if included with
              a POST or PUT request that also specifies a valid 'area' or 'atext' field.

          andims: Number of dimensions of the geometry depicted by region.

          ann_lims: Polygonal annotation limits, specified in pixels, as an array of arrays N x M.
              Allows the image provider to highlight one or more polygonal area(s) of
              interest. The array must contain NxM two-element arrays, where N is the number
              of polygons of interest. The associated annotation(s) should be included in the
              annText array.

          ann_text: Annotation text, a string array of annotation(s) corresponding to the
              rectangular areas specified in annLims. This array contains the annotation text
              associated with the areas of interest indicated in annLims, in order. This array
              should contain one annotation per four values of the area (annLims) array.

          area: Optional geographical region or polygon (lat/lon pairs) of the area surrounding
              the feature assessment as projected on the ground.

          asrid: Geographical spatial_ref_sys for region.

          assessment: Descriptive or additional information associated with this feature/assessment.

          atext: Geographical region or polygon (lon/lat pairs), as depicted by the Well-Known
              Text representation of the geometry/geography, of the feature assessment as
              projected on the ground. WKT reference:
              https://www.opengeospatial.org/standards/wkt-crs. Ignored if included with a
              POST or PUT request that also specifies a valid 'area' field.

          atype: Type of region as projected on the ground (POLYGON, POINT, LINE).

          confidence: Analytic confidence of feature accuracy (0 to 1).

          external_id: Feature Assessment ID from external systems. This field has no meaning within
              UDL and is provided as a convenience for systems that require tracking of an
              internal system generated ID.

          feature_array: An array of numeric feature/assessment values expressed in the specified unit of
              measure (obUoM). Because of the variability of the Feature Assessment data
              types, each record may employ a numeric observation value (featureValue), a
              string observation value (featureString), a Boolean observation value
              (featureBool), an array of numeric observation values (featureArray), or any
              combination of these.

          feature_bool: A boolean feature/assessment. Because of the variability of the Feature
              Assessment data types, each record may employ a numeric observation value
              (featureValue), a string observation value (featureString), a Boolean
              observation value (featureBool), an array of numeric observation values
              (featureArray), or any combination of these.

          feature_string: A single feature/assessment string expressed in the specified unit of measure
              (obUoM). Because of the variability of the Feature Assessment data types, each
              record may employ a numeric observation value (featureValue), a string
              observation value (featureString), a Boolean observation value (featureBool), an
              array of numeric observation values (featureArray), or any combination of these.

          feature_string_array: An array of string feature/assessment expressions. Because of the variability of
              the Feature Assessment data types, each record may employ a numeric observation
              value (featureValue), a string observation value (featureString), a Boolean
              observation value (featureBool), an array of numeric observation values
              (featureArray), or any combination of these.

          feature_value: A single feature/assessment value expressed in the specified unit of measure
              (obUoM). Because of the variability of the Feature Assessment data types, each
              record may employ a numeric observation value (featureValue), a string
              observation value (featureString), a Boolean observation value (featureBool), an
              array of numeric observation values (featureArray), or any combination of these.

          heading: The feature object heading, in degrees clockwise from true North at the object
              location.

          height: Estimated physical height of the feature, in meters.

          length: Estimated physical length of the feature, in meters.

          name: Source defined name of the feature associated with this record. If an annotation
              for this feature element exists on the parent image it can be referenced here.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          speed: Feature's speed of travel, in meters per second.

          src_ids: Array of UUIDs of the UDL data records that are related to the determination of
              this activity or event. See the associated 'srcTyps' array for the specific
              types of data, positionally corresponding to the UUIDs in this array. The
              'srcTyps', 'srcIds', and 'srcTs' arrays must contain the same number of
              elements. See the corresponding srcTyps array element for the data type of the
              UUID and use the appropriate API operation to retrieve that object.

          src_ts: Array of the primary timestamps, in ISO 8601 UTC format, with appropriate
              precision for the datatype of each correspondng srcTyp/srcId record. See the
              associated 'srcTyps' and 'srcIds' arrays for the record type and UUID,
              respectively, positionally corresponding to the record types in this array. The
              'srcTyps', 'srcIds', and 'srcTs' arrays must contain the same number of
              elements. These timestamps are included to support services which do not include
              a GET by {id} operation. If referencing a datatype which does not include a
              primary timestamp, the corresponding srcTs array element should be included as
              null.

          src_typs: Array of UDL record types (AIS, GROUNDIMAGE, MTI, ONORBIT, POI, SAR, SKYIMAGE,
              SOI, TRACK) related to this feature assessment. See the associated 'srcIds' and
              'srcTs' arrays for the record UUIDs and timetsmps. respectively, positionally
              corresponding to the record types in this array. The 'srcTyps', 'srcIds', and
              'srcTs' arrays must contain the same number of elements.

          tags: Optional array of provider/source specific tags for this data, where each
              element is no longer than 32 characters, used for implementing data owner
              conditional access controls to restrict access to the data. Should be left null
              by data providers unless conditional access controls are coordinated with the
              UDL team.

          transaction_id: Optional identifier to track a commercial or marketplace transaction executed to
              produce this data.

          type: The type of feature (e.g. AIRCRAFT, ANTENNA, SOLAR ARRAY, SITE, STRUCTURE,
              VESSEL, VEHICLE, UNKNOWN, etc.) detailed in this feature assessment record. This
              type may be a primary feature within an image, for example a VESSEL, or may be a
              component or characteristic of a primary feature, for example an ANTENNA mounted
              on a vessel.

          width: Estimated physical width of the feature, in meters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/udl/featureassessment",
            body=maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "feature_ts": feature_ts,
                    "feature_uo_m": feature_uo_m,
                    "id_analytic_imagery": id_analytic_imagery,
                    "source": source,
                    "id": id,
                    "agjson": agjson,
                    "andims": andims,
                    "ann_lims": ann_lims,
                    "ann_text": ann_text,
                    "area": area,
                    "asrid": asrid,
                    "assessment": assessment,
                    "atext": atext,
                    "atype": atype,
                    "confidence": confidence,
                    "external_id": external_id,
                    "feature_array": feature_array,
                    "feature_bool": feature_bool,
                    "feature_string": feature_string,
                    "feature_string_array": feature_string_array,
                    "feature_value": feature_value,
                    "heading": heading,
                    "height": height,
                    "length": length,
                    "name": name,
                    "origin": origin,
                    "speed": speed,
                    "src_ids": src_ids,
                    "src_ts": src_ts,
                    "src_typs": src_typs,
                    "tags": tags,
                    "transaction_id": transaction_id,
                    "type": type,
                    "width": width,
                },
                feature_assessment_create_params.FeatureAssessmentCreateParams,
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
    ) -> FeatureAssessmentRetrieveResponse:
        """
        Service operation to get a single FeatureAssessment record by its unique ID
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
            f"/udl/featureassessment/{id}",
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
                    feature_assessment_retrieve_params.FeatureAssessmentRetrieveParams,
                ),
            ),
            cast_to=FeatureAssessmentRetrieveResponse,
        )

    def count(
        self,
        *,
        id_analytic_imagery: str,
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
          id_analytic_imagery: Unique identifier of the Analytic Imagery associated with this Feature
              Assessment record.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return self._get(
            "/udl/featureassessment/count",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id_analytic_imagery": id_analytic_imagery,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    feature_assessment_count_params.FeatureAssessmentCountParams,
                ),
            ),
            cast_to=str,
        )

    def create_bulk(
        self,
        *,
        body: Iterable[feature_assessment_create_bulk_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation intended for initial integration only, to take a list of
        FeatureAssessment records as a POST body and ingest into the database. This
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
            "/udl/featureassessment/createBulk",
            body=maybe_transform(body, Iterable[feature_assessment_create_bulk_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def query(
        self,
        *,
        id_analytic_imagery: str,
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FeatureAssessmentQueryResponse:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          id_analytic_imagery: Unique identifier of the Analytic Imagery associated with this Feature
              Assessment record.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/udl/featureassessment",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id_analytic_imagery": id_analytic_imagery,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    feature_assessment_query_params.FeatureAssessmentQueryParams,
                ),
            ),
            cast_to=FeatureAssessmentQueryResponse,
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
    ) -> FeatureAssessmentQueryHelpResponse:
        """
        Service operation to provide detailed information on available dynamic query
        parameters for a particular data type.
        """
        return self._get(
            "/udl/featureassessment/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FeatureAssessmentQueryHelpResponse,
        )

    def tuple(
        self,
        *,
        columns: str,
        id_analytic_imagery: str,
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FeatureAssessmentTupleResponse:
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

          id_analytic_imagery: Unique identifier of the Analytic Imagery associated with this Feature
              Assessment record.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/udl/featureassessment/tuple",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "columns": columns,
                        "id_analytic_imagery": id_analytic_imagery,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    feature_assessment_tuple_params.FeatureAssessmentTupleParams,
                ),
            ),
            cast_to=FeatureAssessmentTupleResponse,
        )

    def unvalidated_publish(
        self,
        *,
        body: Iterable[feature_assessment_unvalidated_publish_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take multiple FeatureAssessment records as a POST body and
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
            "/filedrop/udl-featureassessment",
            body=maybe_transform(body, Iterable[feature_assessment_unvalidated_publish_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncFeatureAssessmentResource(AsyncAPIResource):
    @cached_property
    def history(self) -> AsyncHistoryResource:
        return AsyncHistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncFeatureAssessmentResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncFeatureAssessmentResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFeatureAssessmentResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncFeatureAssessmentResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        feature_ts: Union[str, datetime],
        feature_uo_m: str,
        id_analytic_imagery: str,
        source: str,
        id: str | NotGiven = NOT_GIVEN,
        agjson: str | NotGiven = NOT_GIVEN,
        andims: int | NotGiven = NOT_GIVEN,
        ann_lims: Iterable[Iterable[int]] | NotGiven = NOT_GIVEN,
        ann_text: List[str] | NotGiven = NOT_GIVEN,
        area: str | NotGiven = NOT_GIVEN,
        asrid: int | NotGiven = NOT_GIVEN,
        assessment: str | NotGiven = NOT_GIVEN,
        atext: str | NotGiven = NOT_GIVEN,
        atype: str | NotGiven = NOT_GIVEN,
        confidence: float | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        feature_array: Iterable[float] | NotGiven = NOT_GIVEN,
        feature_bool: bool | NotGiven = NOT_GIVEN,
        feature_string: str | NotGiven = NOT_GIVEN,
        feature_string_array: List[str] | NotGiven = NOT_GIVEN,
        feature_value: float | NotGiven = NOT_GIVEN,
        heading: float | NotGiven = NOT_GIVEN,
        height: float | NotGiven = NOT_GIVEN,
        length: float | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        speed: float | NotGiven = NOT_GIVEN,
        src_ids: List[str] | NotGiven = NOT_GIVEN,
        src_ts: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        src_typs: List[str] | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        transaction_id: str | NotGiven = NOT_GIVEN,
        type: str | NotGiven = NOT_GIVEN,
        width: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single FeatureAssessment record as a POST body and
        ingest into the database. A specific role is required to perform this service
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

          feature_ts: Datetime type value associated with this record, in ISO 8601 UTC format with
              millisecond precision.

          feature_uo_m: The Unit of Measure associated with this feature. If there are no physical units
              associated with the feature a value of NONE should be specified.

          id_analytic_imagery: Unique identifier of the Analytic Imagery associated with this Feature
              Assessment record.

          source: Source of the data.

          id: Unique identifier of the record, auto-generated by the system.

          agjson: Geographical region or polygon (lat/lon pairs), as depicted by the GeoJSON
              representation of the geometry/geography, of the feature assessment as projected
              on the ground. GeoJSON Reference: https://geojson.org/. Ignored if included with
              a POST or PUT request that also specifies a valid 'area' or 'atext' field.

          andims: Number of dimensions of the geometry depicted by region.

          ann_lims: Polygonal annotation limits, specified in pixels, as an array of arrays N x M.
              Allows the image provider to highlight one or more polygonal area(s) of
              interest. The array must contain NxM two-element arrays, where N is the number
              of polygons of interest. The associated annotation(s) should be included in the
              annText array.

          ann_text: Annotation text, a string array of annotation(s) corresponding to the
              rectangular areas specified in annLims. This array contains the annotation text
              associated with the areas of interest indicated in annLims, in order. This array
              should contain one annotation per four values of the area (annLims) array.

          area: Optional geographical region or polygon (lat/lon pairs) of the area surrounding
              the feature assessment as projected on the ground.

          asrid: Geographical spatial_ref_sys for region.

          assessment: Descriptive or additional information associated with this feature/assessment.

          atext: Geographical region or polygon (lon/lat pairs), as depicted by the Well-Known
              Text representation of the geometry/geography, of the feature assessment as
              projected on the ground. WKT reference:
              https://www.opengeospatial.org/standards/wkt-crs. Ignored if included with a
              POST or PUT request that also specifies a valid 'area' field.

          atype: Type of region as projected on the ground (POLYGON, POINT, LINE).

          confidence: Analytic confidence of feature accuracy (0 to 1).

          external_id: Feature Assessment ID from external systems. This field has no meaning within
              UDL and is provided as a convenience for systems that require tracking of an
              internal system generated ID.

          feature_array: An array of numeric feature/assessment values expressed in the specified unit of
              measure (obUoM). Because of the variability of the Feature Assessment data
              types, each record may employ a numeric observation value (featureValue), a
              string observation value (featureString), a Boolean observation value
              (featureBool), an array of numeric observation values (featureArray), or any
              combination of these.

          feature_bool: A boolean feature/assessment. Because of the variability of the Feature
              Assessment data types, each record may employ a numeric observation value
              (featureValue), a string observation value (featureString), a Boolean
              observation value (featureBool), an array of numeric observation values
              (featureArray), or any combination of these.

          feature_string: A single feature/assessment string expressed in the specified unit of measure
              (obUoM). Because of the variability of the Feature Assessment data types, each
              record may employ a numeric observation value (featureValue), a string
              observation value (featureString), a Boolean observation value (featureBool), an
              array of numeric observation values (featureArray), or any combination of these.

          feature_string_array: An array of string feature/assessment expressions. Because of the variability of
              the Feature Assessment data types, each record may employ a numeric observation
              value (featureValue), a string observation value (featureString), a Boolean
              observation value (featureBool), an array of numeric observation values
              (featureArray), or any combination of these.

          feature_value: A single feature/assessment value expressed in the specified unit of measure
              (obUoM). Because of the variability of the Feature Assessment data types, each
              record may employ a numeric observation value (featureValue), a string
              observation value (featureString), a Boolean observation value (featureBool), an
              array of numeric observation values (featureArray), or any combination of these.

          heading: The feature object heading, in degrees clockwise from true North at the object
              location.

          height: Estimated physical height of the feature, in meters.

          length: Estimated physical length of the feature, in meters.

          name: Source defined name of the feature associated with this record. If an annotation
              for this feature element exists on the parent image it can be referenced here.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          speed: Feature's speed of travel, in meters per second.

          src_ids: Array of UUIDs of the UDL data records that are related to the determination of
              this activity or event. See the associated 'srcTyps' array for the specific
              types of data, positionally corresponding to the UUIDs in this array. The
              'srcTyps', 'srcIds', and 'srcTs' arrays must contain the same number of
              elements. See the corresponding srcTyps array element for the data type of the
              UUID and use the appropriate API operation to retrieve that object.

          src_ts: Array of the primary timestamps, in ISO 8601 UTC format, with appropriate
              precision for the datatype of each correspondng srcTyp/srcId record. See the
              associated 'srcTyps' and 'srcIds' arrays for the record type and UUID,
              respectively, positionally corresponding to the record types in this array. The
              'srcTyps', 'srcIds', and 'srcTs' arrays must contain the same number of
              elements. These timestamps are included to support services which do not include
              a GET by {id} operation. If referencing a datatype which does not include a
              primary timestamp, the corresponding srcTs array element should be included as
              null.

          src_typs: Array of UDL record types (AIS, GROUNDIMAGE, MTI, ONORBIT, POI, SAR, SKYIMAGE,
              SOI, TRACK) related to this feature assessment. See the associated 'srcIds' and
              'srcTs' arrays for the record UUIDs and timetsmps. respectively, positionally
              corresponding to the record types in this array. The 'srcTyps', 'srcIds', and
              'srcTs' arrays must contain the same number of elements.

          tags: Optional array of provider/source specific tags for this data, where each
              element is no longer than 32 characters, used for implementing data owner
              conditional access controls to restrict access to the data. Should be left null
              by data providers unless conditional access controls are coordinated with the
              UDL team.

          transaction_id: Optional identifier to track a commercial or marketplace transaction executed to
              produce this data.

          type: The type of feature (e.g. AIRCRAFT, ANTENNA, SOLAR ARRAY, SITE, STRUCTURE,
              VESSEL, VEHICLE, UNKNOWN, etc.) detailed in this feature assessment record. This
              type may be a primary feature within an image, for example a VESSEL, or may be a
              component or characteristic of a primary feature, for example an ANTENNA mounted
              on a vessel.

          width: Estimated physical width of the feature, in meters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/udl/featureassessment",
            body=await async_maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "feature_ts": feature_ts,
                    "feature_uo_m": feature_uo_m,
                    "id_analytic_imagery": id_analytic_imagery,
                    "source": source,
                    "id": id,
                    "agjson": agjson,
                    "andims": andims,
                    "ann_lims": ann_lims,
                    "ann_text": ann_text,
                    "area": area,
                    "asrid": asrid,
                    "assessment": assessment,
                    "atext": atext,
                    "atype": atype,
                    "confidence": confidence,
                    "external_id": external_id,
                    "feature_array": feature_array,
                    "feature_bool": feature_bool,
                    "feature_string": feature_string,
                    "feature_string_array": feature_string_array,
                    "feature_value": feature_value,
                    "heading": heading,
                    "height": height,
                    "length": length,
                    "name": name,
                    "origin": origin,
                    "speed": speed,
                    "src_ids": src_ids,
                    "src_ts": src_ts,
                    "src_typs": src_typs,
                    "tags": tags,
                    "transaction_id": transaction_id,
                    "type": type,
                    "width": width,
                },
                feature_assessment_create_params.FeatureAssessmentCreateParams,
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
    ) -> FeatureAssessmentRetrieveResponse:
        """
        Service operation to get a single FeatureAssessment record by its unique ID
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
            f"/udl/featureassessment/{id}",
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
                    feature_assessment_retrieve_params.FeatureAssessmentRetrieveParams,
                ),
            ),
            cast_to=FeatureAssessmentRetrieveResponse,
        )

    async def count(
        self,
        *,
        id_analytic_imagery: str,
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
          id_analytic_imagery: Unique identifier of the Analytic Imagery associated with this Feature
              Assessment record.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return await self._get(
            "/udl/featureassessment/count",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "id_analytic_imagery": id_analytic_imagery,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    feature_assessment_count_params.FeatureAssessmentCountParams,
                ),
            ),
            cast_to=str,
        )

    async def create_bulk(
        self,
        *,
        body: Iterable[feature_assessment_create_bulk_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation intended for initial integration only, to take a list of
        FeatureAssessment records as a POST body and ingest into the database. This
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
            "/udl/featureassessment/createBulk",
            body=await async_maybe_transform(body, Iterable[feature_assessment_create_bulk_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def query(
        self,
        *,
        id_analytic_imagery: str,
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FeatureAssessmentQueryResponse:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          id_analytic_imagery: Unique identifier of the Analytic Imagery associated with this Feature
              Assessment record.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/udl/featureassessment",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "id_analytic_imagery": id_analytic_imagery,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    feature_assessment_query_params.FeatureAssessmentQueryParams,
                ),
            ),
            cast_to=FeatureAssessmentQueryResponse,
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
    ) -> FeatureAssessmentQueryHelpResponse:
        """
        Service operation to provide detailed information on available dynamic query
        parameters for a particular data type.
        """
        return await self._get(
            "/udl/featureassessment/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FeatureAssessmentQueryHelpResponse,
        )

    async def tuple(
        self,
        *,
        columns: str,
        id_analytic_imagery: str,
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FeatureAssessmentTupleResponse:
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

          id_analytic_imagery: Unique identifier of the Analytic Imagery associated with this Feature
              Assessment record.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/udl/featureassessment/tuple",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "columns": columns,
                        "id_analytic_imagery": id_analytic_imagery,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    feature_assessment_tuple_params.FeatureAssessmentTupleParams,
                ),
            ),
            cast_to=FeatureAssessmentTupleResponse,
        )

    async def unvalidated_publish(
        self,
        *,
        body: Iterable[feature_assessment_unvalidated_publish_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take multiple FeatureAssessment records as a POST body and
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
            "/filedrop/udl-featureassessment",
            body=await async_maybe_transform(body, Iterable[feature_assessment_unvalidated_publish_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class FeatureAssessmentResourceWithRawResponse:
    def __init__(self, feature_assessment: FeatureAssessmentResource) -> None:
        self._feature_assessment = feature_assessment

        self.create = to_raw_response_wrapper(
            feature_assessment.create,
        )
        self.retrieve = to_raw_response_wrapper(
            feature_assessment.retrieve,
        )
        self.count = to_raw_response_wrapper(
            feature_assessment.count,
        )
        self.create_bulk = to_raw_response_wrapper(
            feature_assessment.create_bulk,
        )
        self.query = to_raw_response_wrapper(
            feature_assessment.query,
        )
        self.query_help = to_raw_response_wrapper(
            feature_assessment.query_help,
        )
        self.tuple = to_raw_response_wrapper(
            feature_assessment.tuple,
        )
        self.unvalidated_publish = to_raw_response_wrapper(
            feature_assessment.unvalidated_publish,
        )

    @cached_property
    def history(self) -> HistoryResourceWithRawResponse:
        return HistoryResourceWithRawResponse(self._feature_assessment.history)


class AsyncFeatureAssessmentResourceWithRawResponse:
    def __init__(self, feature_assessment: AsyncFeatureAssessmentResource) -> None:
        self._feature_assessment = feature_assessment

        self.create = async_to_raw_response_wrapper(
            feature_assessment.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            feature_assessment.retrieve,
        )
        self.count = async_to_raw_response_wrapper(
            feature_assessment.count,
        )
        self.create_bulk = async_to_raw_response_wrapper(
            feature_assessment.create_bulk,
        )
        self.query = async_to_raw_response_wrapper(
            feature_assessment.query,
        )
        self.query_help = async_to_raw_response_wrapper(
            feature_assessment.query_help,
        )
        self.tuple = async_to_raw_response_wrapper(
            feature_assessment.tuple,
        )
        self.unvalidated_publish = async_to_raw_response_wrapper(
            feature_assessment.unvalidated_publish,
        )

    @cached_property
    def history(self) -> AsyncHistoryResourceWithRawResponse:
        return AsyncHistoryResourceWithRawResponse(self._feature_assessment.history)


class FeatureAssessmentResourceWithStreamingResponse:
    def __init__(self, feature_assessment: FeatureAssessmentResource) -> None:
        self._feature_assessment = feature_assessment

        self.create = to_streamed_response_wrapper(
            feature_assessment.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            feature_assessment.retrieve,
        )
        self.count = to_streamed_response_wrapper(
            feature_assessment.count,
        )
        self.create_bulk = to_streamed_response_wrapper(
            feature_assessment.create_bulk,
        )
        self.query = to_streamed_response_wrapper(
            feature_assessment.query,
        )
        self.query_help = to_streamed_response_wrapper(
            feature_assessment.query_help,
        )
        self.tuple = to_streamed_response_wrapper(
            feature_assessment.tuple,
        )
        self.unvalidated_publish = to_streamed_response_wrapper(
            feature_assessment.unvalidated_publish,
        )

    @cached_property
    def history(self) -> HistoryResourceWithStreamingResponse:
        return HistoryResourceWithStreamingResponse(self._feature_assessment.history)


class AsyncFeatureAssessmentResourceWithStreamingResponse:
    def __init__(self, feature_assessment: AsyncFeatureAssessmentResource) -> None:
        self._feature_assessment = feature_assessment

        self.create = async_to_streamed_response_wrapper(
            feature_assessment.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            feature_assessment.retrieve,
        )
        self.count = async_to_streamed_response_wrapper(
            feature_assessment.count,
        )
        self.create_bulk = async_to_streamed_response_wrapper(
            feature_assessment.create_bulk,
        )
        self.query = async_to_streamed_response_wrapper(
            feature_assessment.query,
        )
        self.query_help = async_to_streamed_response_wrapper(
            feature_assessment.query_help,
        )
        self.tuple = async_to_streamed_response_wrapper(
            feature_assessment.tuple,
        )
        self.unvalidated_publish = async_to_streamed_response_wrapper(
            feature_assessment.unvalidated_publish,
        )

    @cached_property
    def history(self) -> AsyncHistoryResourceWithStreamingResponse:
        return AsyncHistoryResourceWithStreamingResponse(self._feature_assessment.history)
