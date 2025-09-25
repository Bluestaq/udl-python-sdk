# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime
from typing_extensions import Literal

import httpx

from .history import (
    HistoryResource,
    AsyncHistoryResource,
    HistoryResourceWithRawResponse,
    AsyncHistoryResourceWithRawResponse,
    HistoryResourceWithStreamingResponse,
    AsyncHistoryResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....pagination import SyncOffsetPage, AsyncOffsetPage
from ...._base_client import AsyncPaginator, make_request_options
from ....types.observations import (
    obscorrelation_list_params,
    obscorrelation_count_params,
    obscorrelation_tuple_params,
    obscorrelation_create_params,
    obscorrelation_retrieve_params,
    obscorrelation_create_bulk_params,
    obscorrelation_unvalidated_publish_params,
)
from ....types.observations.obscorrelation_list_response import ObscorrelationListResponse
from ....types.observations.obscorrelation_tuple_response import ObscorrelationTupleResponse
from ....types.observations.obscorrelation_retrieve_response import ObscorrelationRetrieveResponse
from ....types.observations.obscorrelation_query_help_response import ObscorrelationQueryHelpResponse

__all__ = ["ObscorrelationResource", "AsyncObscorrelationResource"]


class ObscorrelationResource(SyncAPIResource):
    @cached_property
    def history(self) -> HistoryResource:
        return HistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> ObscorrelationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return ObscorrelationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ObscorrelationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return ObscorrelationResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        classification_marking: str,
        corr_type: Literal["OBSERVATION", "TRACK"],
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        msg_ts: Union[str, datetime],
        ob_id: str,
        ob_type: Literal["DOA", "EO", "PASSIVE_RADAR", "RADAR", "RF", "SAR", "SOISET"],
        reference_orbit_id: str,
        reference_orbit_type: Literal["ELSET", "ESID", "SV"],
        source: str,
        id: str | Omit = omit,
        algorithm_corr_type: str | Omit = omit,
        alt_catalog: str | Omit = omit,
        alt_namespace: str | Omit = omit,
        alt_object_id: str | Omit = omit,
        alt_uct: bool | Omit = omit,
        astat: int | Omit = omit,
        corr_quality: float | Omit = omit,
        id_parent_correlation: str | Omit = omit,
        origin: str | Omit = omit,
        orig_object_id: str | Omit = omit,
        sat_no: int | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        track_id: str | Omit = omit,
        transaction_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Service operation to take a single ObsCorrelation record as a POST body and
        ingest into the database. A specific role is required to perform this service
        operation. Please contact the UDL team for assistance.

        Args:
          classification_marking: Classification marking of the data in IC/CAPCO Portion-marked format.

          corr_type:
              Indicator of whether the type of correlation is OBSERVATION or TRACK:
              OBSERVATION: Identifies an observation is being correlated. TRACK: Identifies
              the entire track of observations is being correlated.

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

          msg_ts: Correlation message generation time, in ISO 8601 UTC format with millisecond
              precision.

          ob_id: Identifier of the Observation associated with this Correlation. If
              corrType=TRACK then this field should reference the first Observation in the
              track. Note: To retrieve all remaining Observations in the track, the GET query
              should include this Observation's source and origin field values, along with the
              trackId.

          ob_type: Indicator of whether the type of Observation(s) being correlated is DOA, EO,
              PASSIVE_RADAR, RADAR, RF, SAR, or SOISET: DOA: The observation type being
              correlated is Difference of Arrival. EO: The observation type being correlated
              is Electro-Optical. PASSIVE_RADAR: The observation type being correlated is
              Passive Radar. RADAR: The observation type being correlated is Radar. RF: The
              observation type being correlated is Radio Frequency. SAR: The observation type
              being correlated is Synthetic Aperture Radar. SOISET: The observation type being
              correlated is Space Object Identification Observation Set.

          reference_orbit_id: Identifier of the orbit state used for correlation.

          reference_orbit_type: Indicator of whether the reference orbit type used for correlation is an ELSET,
              ESID, or SV: ELSET: The reference orbit type is an Element Set. ESID: The
              reference orbit type is an Ephemeris Set. SV: The reference orbit type is a
              State Vector.

          source: Source of the data.

          id: Unique identifier of the record, auto-generated by the system.

          algorithm_corr_type: Type of algorithm used for this correlation (e.g. ROTAS, GEOMETRIC, STATISTICAL,
              MAHALANOBIS, AI/ML, OTHER).

          alt_catalog: Name of the alternate catalog.

          alt_namespace: Associates one or more alternate catalogs with a source provider or system.
              Namespaces may be defined by their respective data providers or systems (e.g.
              JCO, 18SDS, EOSSS, EXO, KBR, KRTL, LeoLabs, NorthStar, SAFRAN, Slingshot).

          alt_object_id: Alternate unique object ID within the namespace.

          alt_uct: Boolean indicating whether the observation or track can be correlated to the
              alternate object specified under altObjectId. This flag should only be set to
              true by data providers after an attempt to correlate to an on-orbit object was
              made and failed. If unable to correlate, the 'origObjectId' field may be
              populated with an internal data provider specific identifier.

          astat: Astrostandard ROTAS correlation result (0 - 4), if applicable. Refer to ROTAS
              documentation for an explanation of ASTAT values.

          corr_quality: Correlation score ranging from 0.0 to 1.0. A score of 1.0 represents perfect
              correlation to the orbit of the corresponding satellite, such as when all
              observation residuals equal 0.

          id_parent_correlation: Identifier of the ObsCorrelation record from which this ObsCorrelation record
              originated. This behavior allows for different source providers/systems to make
              changes to a given correlation and maintain traceability back to the original
              correlation.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          orig_object_id: Optional identifier indicates the target on-orbit object being correlated. This
              may be an internal identifier and not necessarily a valid satellite number.

          sat_no: Current 18th SDS satellite/catalog number of the target on-orbit object. Useful
              to know in the case where an observation is correlated to another
              satellite/catalog number.

          tags: Optional array of provider/source specific tags for this data, where each
              element is no longer than 32 characters, used for implementing data owner
              conditional access controls to restrict access to the data. Should be left null
              by data providers unless conditional access controls are coordinated with the
              UDL team.

          track_id: Identifier of the Track associated with this ObsCorrelation.

          transaction_id: Optional identifier to track a commercial or marketplace transaction executed to
              produce this data.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/udl/obscorrelation",
            body=maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "corr_type": corr_type,
                    "data_mode": data_mode,
                    "msg_ts": msg_ts,
                    "ob_id": ob_id,
                    "ob_type": ob_type,
                    "reference_orbit_id": reference_orbit_id,
                    "reference_orbit_type": reference_orbit_type,
                    "source": source,
                    "id": id,
                    "algorithm_corr_type": algorithm_corr_type,
                    "alt_catalog": alt_catalog,
                    "alt_namespace": alt_namespace,
                    "alt_object_id": alt_object_id,
                    "alt_uct": alt_uct,
                    "astat": astat,
                    "corr_quality": corr_quality,
                    "id_parent_correlation": id_parent_correlation,
                    "origin": origin,
                    "orig_object_id": orig_object_id,
                    "sat_no": sat_no,
                    "tags": tags,
                    "track_id": track_id,
                    "transaction_id": transaction_id,
                },
                obscorrelation_create_params.ObscorrelationCreateParams,
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
        first_result: int | Omit = omit,
        max_results: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ObscorrelationRetrieveResponse:
        """
        Service operation to get a single Correlation record by its unique ID passed as
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
            f"/udl/obscorrelation/{id}",
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
                    obscorrelation_retrieve_params.ObscorrelationRetrieveParams,
                ),
            ),
            cast_to=ObscorrelationRetrieveResponse,
        )

    def list(
        self,
        *,
        msg_ts: Union[str, datetime],
        first_result: int | Omit = omit,
        max_results: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncOffsetPage[ObscorrelationListResponse]:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          msg_ts: Correlation message generation time, in ISO 8601 UTC format with millisecond
              precision. (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/obscorrelation",
            page=SyncOffsetPage[ObscorrelationListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "msg_ts": msg_ts,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    obscorrelation_list_params.ObscorrelationListParams,
                ),
            ),
            model=ObscorrelationListResponse,
        )

    def count(
        self,
        *,
        msg_ts: Union[str, datetime],
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
          msg_ts: Correlation message generation time, in ISO 8601 UTC format with millisecond
              precision. (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return self._get(
            "/udl/obscorrelation/count",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "msg_ts": msg_ts,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    obscorrelation_count_params.ObscorrelationCountParams,
                ),
            ),
            cast_to=str,
        )

    def create_bulk(
        self,
        *,
        body: Iterable[obscorrelation_create_bulk_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Service operation intended for initial integration only, to take a list of
        ObsCorrelation records as a POST body and ingest into the database. This
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
            "/udl/obscorrelation/createBulk",
            body=maybe_transform(body, Iterable[obscorrelation_create_bulk_params.Body]),
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ObscorrelationQueryHelpResponse:
        """
        Service operation to provide detailed information on available dynamic query
        parameters for a particular data type.
        """
        return self._get(
            "/udl/obscorrelation/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ObscorrelationQueryHelpResponse,
        )

    def tuple(
        self,
        *,
        columns: str,
        msg_ts: Union[str, datetime],
        first_result: int | Omit = omit,
        max_results: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ObscorrelationTupleResponse:
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

          msg_ts: Correlation message generation time, in ISO 8601 UTC format with millisecond
              precision. (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/udl/obscorrelation/tuple",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "columns": columns,
                        "msg_ts": msg_ts,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    obscorrelation_tuple_params.ObscorrelationTupleParams,
                ),
            ),
            cast_to=ObscorrelationTupleResponse,
        )

    def unvalidated_publish(
        self,
        *,
        body: Iterable[obscorrelation_unvalidated_publish_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Service operation to take multiple ObsCorrelation records as a POST body and
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
            "/filedrop/udl-obscorrelation",
            body=maybe_transform(body, Iterable[obscorrelation_unvalidated_publish_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncObscorrelationResource(AsyncAPIResource):
    @cached_property
    def history(self) -> AsyncHistoryResource:
        return AsyncHistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncObscorrelationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncObscorrelationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncObscorrelationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncObscorrelationResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        classification_marking: str,
        corr_type: Literal["OBSERVATION", "TRACK"],
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        msg_ts: Union[str, datetime],
        ob_id: str,
        ob_type: Literal["DOA", "EO", "PASSIVE_RADAR", "RADAR", "RF", "SAR", "SOISET"],
        reference_orbit_id: str,
        reference_orbit_type: Literal["ELSET", "ESID", "SV"],
        source: str,
        id: str | Omit = omit,
        algorithm_corr_type: str | Omit = omit,
        alt_catalog: str | Omit = omit,
        alt_namespace: str | Omit = omit,
        alt_object_id: str | Omit = omit,
        alt_uct: bool | Omit = omit,
        astat: int | Omit = omit,
        corr_quality: float | Omit = omit,
        id_parent_correlation: str | Omit = omit,
        origin: str | Omit = omit,
        orig_object_id: str | Omit = omit,
        sat_no: int | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        track_id: str | Omit = omit,
        transaction_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Service operation to take a single ObsCorrelation record as a POST body and
        ingest into the database. A specific role is required to perform this service
        operation. Please contact the UDL team for assistance.

        Args:
          classification_marking: Classification marking of the data in IC/CAPCO Portion-marked format.

          corr_type:
              Indicator of whether the type of correlation is OBSERVATION or TRACK:
              OBSERVATION: Identifies an observation is being correlated. TRACK: Identifies
              the entire track of observations is being correlated.

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

          msg_ts: Correlation message generation time, in ISO 8601 UTC format with millisecond
              precision.

          ob_id: Identifier of the Observation associated with this Correlation. If
              corrType=TRACK then this field should reference the first Observation in the
              track. Note: To retrieve all remaining Observations in the track, the GET query
              should include this Observation's source and origin field values, along with the
              trackId.

          ob_type: Indicator of whether the type of Observation(s) being correlated is DOA, EO,
              PASSIVE_RADAR, RADAR, RF, SAR, or SOISET: DOA: The observation type being
              correlated is Difference of Arrival. EO: The observation type being correlated
              is Electro-Optical. PASSIVE_RADAR: The observation type being correlated is
              Passive Radar. RADAR: The observation type being correlated is Radar. RF: The
              observation type being correlated is Radio Frequency. SAR: The observation type
              being correlated is Synthetic Aperture Radar. SOISET: The observation type being
              correlated is Space Object Identification Observation Set.

          reference_orbit_id: Identifier of the orbit state used for correlation.

          reference_orbit_type: Indicator of whether the reference orbit type used for correlation is an ELSET,
              ESID, or SV: ELSET: The reference orbit type is an Element Set. ESID: The
              reference orbit type is an Ephemeris Set. SV: The reference orbit type is a
              State Vector.

          source: Source of the data.

          id: Unique identifier of the record, auto-generated by the system.

          algorithm_corr_type: Type of algorithm used for this correlation (e.g. ROTAS, GEOMETRIC, STATISTICAL,
              MAHALANOBIS, AI/ML, OTHER).

          alt_catalog: Name of the alternate catalog.

          alt_namespace: Associates one or more alternate catalogs with a source provider or system.
              Namespaces may be defined by their respective data providers or systems (e.g.
              JCO, 18SDS, EOSSS, EXO, KBR, KRTL, LeoLabs, NorthStar, SAFRAN, Slingshot).

          alt_object_id: Alternate unique object ID within the namespace.

          alt_uct: Boolean indicating whether the observation or track can be correlated to the
              alternate object specified under altObjectId. This flag should only be set to
              true by data providers after an attempt to correlate to an on-orbit object was
              made and failed. If unable to correlate, the 'origObjectId' field may be
              populated with an internal data provider specific identifier.

          astat: Astrostandard ROTAS correlation result (0 - 4), if applicable. Refer to ROTAS
              documentation for an explanation of ASTAT values.

          corr_quality: Correlation score ranging from 0.0 to 1.0. A score of 1.0 represents perfect
              correlation to the orbit of the corresponding satellite, such as when all
              observation residuals equal 0.

          id_parent_correlation: Identifier of the ObsCorrelation record from which this ObsCorrelation record
              originated. This behavior allows for different source providers/systems to make
              changes to a given correlation and maintain traceability back to the original
              correlation.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          orig_object_id: Optional identifier indicates the target on-orbit object being correlated. This
              may be an internal identifier and not necessarily a valid satellite number.

          sat_no: Current 18th SDS satellite/catalog number of the target on-orbit object. Useful
              to know in the case where an observation is correlated to another
              satellite/catalog number.

          tags: Optional array of provider/source specific tags for this data, where each
              element is no longer than 32 characters, used for implementing data owner
              conditional access controls to restrict access to the data. Should be left null
              by data providers unless conditional access controls are coordinated with the
              UDL team.

          track_id: Identifier of the Track associated with this ObsCorrelation.

          transaction_id: Optional identifier to track a commercial or marketplace transaction executed to
              produce this data.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/udl/obscorrelation",
            body=await async_maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "corr_type": corr_type,
                    "data_mode": data_mode,
                    "msg_ts": msg_ts,
                    "ob_id": ob_id,
                    "ob_type": ob_type,
                    "reference_orbit_id": reference_orbit_id,
                    "reference_orbit_type": reference_orbit_type,
                    "source": source,
                    "id": id,
                    "algorithm_corr_type": algorithm_corr_type,
                    "alt_catalog": alt_catalog,
                    "alt_namespace": alt_namespace,
                    "alt_object_id": alt_object_id,
                    "alt_uct": alt_uct,
                    "astat": astat,
                    "corr_quality": corr_quality,
                    "id_parent_correlation": id_parent_correlation,
                    "origin": origin,
                    "orig_object_id": orig_object_id,
                    "sat_no": sat_no,
                    "tags": tags,
                    "track_id": track_id,
                    "transaction_id": transaction_id,
                },
                obscorrelation_create_params.ObscorrelationCreateParams,
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
        first_result: int | Omit = omit,
        max_results: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ObscorrelationRetrieveResponse:
        """
        Service operation to get a single Correlation record by its unique ID passed as
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
            f"/udl/obscorrelation/{id}",
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
                    obscorrelation_retrieve_params.ObscorrelationRetrieveParams,
                ),
            ),
            cast_to=ObscorrelationRetrieveResponse,
        )

    def list(
        self,
        *,
        msg_ts: Union[str, datetime],
        first_result: int | Omit = omit,
        max_results: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ObscorrelationListResponse, AsyncOffsetPage[ObscorrelationListResponse]]:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          msg_ts: Correlation message generation time, in ISO 8601 UTC format with millisecond
              precision. (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/obscorrelation",
            page=AsyncOffsetPage[ObscorrelationListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "msg_ts": msg_ts,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    obscorrelation_list_params.ObscorrelationListParams,
                ),
            ),
            model=ObscorrelationListResponse,
        )

    async def count(
        self,
        *,
        msg_ts: Union[str, datetime],
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
          msg_ts: Correlation message generation time, in ISO 8601 UTC format with millisecond
              precision. (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return await self._get(
            "/udl/obscorrelation/count",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "msg_ts": msg_ts,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    obscorrelation_count_params.ObscorrelationCountParams,
                ),
            ),
            cast_to=str,
        )

    async def create_bulk(
        self,
        *,
        body: Iterable[obscorrelation_create_bulk_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Service operation intended for initial integration only, to take a list of
        ObsCorrelation records as a POST body and ingest into the database. This
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
            "/udl/obscorrelation/createBulk",
            body=await async_maybe_transform(body, Iterable[obscorrelation_create_bulk_params.Body]),
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ObscorrelationQueryHelpResponse:
        """
        Service operation to provide detailed information on available dynamic query
        parameters for a particular data type.
        """
        return await self._get(
            "/udl/obscorrelation/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ObscorrelationQueryHelpResponse,
        )

    async def tuple(
        self,
        *,
        columns: str,
        msg_ts: Union[str, datetime],
        first_result: int | Omit = omit,
        max_results: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ObscorrelationTupleResponse:
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

          msg_ts: Correlation message generation time, in ISO 8601 UTC format with millisecond
              precision. (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/udl/obscorrelation/tuple",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "columns": columns,
                        "msg_ts": msg_ts,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    obscorrelation_tuple_params.ObscorrelationTupleParams,
                ),
            ),
            cast_to=ObscorrelationTupleResponse,
        )

    async def unvalidated_publish(
        self,
        *,
        body: Iterable[obscorrelation_unvalidated_publish_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Service operation to take multiple ObsCorrelation records as a POST body and
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
            "/filedrop/udl-obscorrelation",
            body=await async_maybe_transform(body, Iterable[obscorrelation_unvalidated_publish_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class ObscorrelationResourceWithRawResponse:
    def __init__(self, obscorrelation: ObscorrelationResource) -> None:
        self._obscorrelation = obscorrelation

        self.create = to_raw_response_wrapper(
            obscorrelation.create,
        )
        self.retrieve = to_raw_response_wrapper(
            obscorrelation.retrieve,
        )
        self.list = to_raw_response_wrapper(
            obscorrelation.list,
        )
        self.count = to_raw_response_wrapper(
            obscorrelation.count,
        )
        self.create_bulk = to_raw_response_wrapper(
            obscorrelation.create_bulk,
        )
        self.query_help = to_raw_response_wrapper(
            obscorrelation.query_help,
        )
        self.tuple = to_raw_response_wrapper(
            obscorrelation.tuple,
        )
        self.unvalidated_publish = to_raw_response_wrapper(
            obscorrelation.unvalidated_publish,
        )

    @cached_property
    def history(self) -> HistoryResourceWithRawResponse:
        return HistoryResourceWithRawResponse(self._obscorrelation.history)


class AsyncObscorrelationResourceWithRawResponse:
    def __init__(self, obscorrelation: AsyncObscorrelationResource) -> None:
        self._obscorrelation = obscorrelation

        self.create = async_to_raw_response_wrapper(
            obscorrelation.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            obscorrelation.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            obscorrelation.list,
        )
        self.count = async_to_raw_response_wrapper(
            obscorrelation.count,
        )
        self.create_bulk = async_to_raw_response_wrapper(
            obscorrelation.create_bulk,
        )
        self.query_help = async_to_raw_response_wrapper(
            obscorrelation.query_help,
        )
        self.tuple = async_to_raw_response_wrapper(
            obscorrelation.tuple,
        )
        self.unvalidated_publish = async_to_raw_response_wrapper(
            obscorrelation.unvalidated_publish,
        )

    @cached_property
    def history(self) -> AsyncHistoryResourceWithRawResponse:
        return AsyncHistoryResourceWithRawResponse(self._obscorrelation.history)


class ObscorrelationResourceWithStreamingResponse:
    def __init__(self, obscorrelation: ObscorrelationResource) -> None:
        self._obscorrelation = obscorrelation

        self.create = to_streamed_response_wrapper(
            obscorrelation.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            obscorrelation.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            obscorrelation.list,
        )
        self.count = to_streamed_response_wrapper(
            obscorrelation.count,
        )
        self.create_bulk = to_streamed_response_wrapper(
            obscorrelation.create_bulk,
        )
        self.query_help = to_streamed_response_wrapper(
            obscorrelation.query_help,
        )
        self.tuple = to_streamed_response_wrapper(
            obscorrelation.tuple,
        )
        self.unvalidated_publish = to_streamed_response_wrapper(
            obscorrelation.unvalidated_publish,
        )

    @cached_property
    def history(self) -> HistoryResourceWithStreamingResponse:
        return HistoryResourceWithStreamingResponse(self._obscorrelation.history)


class AsyncObscorrelationResourceWithStreamingResponse:
    def __init__(self, obscorrelation: AsyncObscorrelationResource) -> None:
        self._obscorrelation = obscorrelation

        self.create = async_to_streamed_response_wrapper(
            obscorrelation.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            obscorrelation.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            obscorrelation.list,
        )
        self.count = async_to_streamed_response_wrapper(
            obscorrelation.count,
        )
        self.create_bulk = async_to_streamed_response_wrapper(
            obscorrelation.create_bulk,
        )
        self.query_help = async_to_streamed_response_wrapper(
            obscorrelation.query_help,
        )
        self.tuple = async_to_streamed_response_wrapper(
            obscorrelation.tuple,
        )
        self.unvalidated_publish = async_to_streamed_response_wrapper(
            obscorrelation.unvalidated_publish,
        )

    @cached_property
    def history(self) -> AsyncHistoryResourceWithStreamingResponse:
        return AsyncHistoryResourceWithStreamingResponse(self._obscorrelation.history)
