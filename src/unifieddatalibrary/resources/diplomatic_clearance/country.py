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
from ...types.diplomatic_clearance import (
    country_list_params,
    country_count_params,
    country_tuple_params,
    country_create_params,
    country_update_params,
    country_retrieve_params,
    country_create_bulk_params,
    country_unvalidated_publish_params,
)
from ...types.diplomatic_clearance.country_list_response import CountryListResponse
from ...types.diplomatic_clearance.country_tuple_response import CountryTupleResponse
from ...types.diplomatic_clearance.country_retrieve_response import CountryRetrieveResponse
from ...types.diplomatic_clearance.country_query_help_response import CountryQueryHelpResponse

__all__ = ["CountryResource", "AsyncCountryResource"]


class CountryResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CountryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return CountryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CountryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return CountryResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        classification_marking: str,
        country_code: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        last_changed_date: Union[str, datetime],
        source: str,
        id: str | NotGiven = NOT_GIVEN,
        accepts_dms: bool | NotGiven = NOT_GIVEN,
        accepts_email: bool | NotGiven = NOT_GIVEN,
        accepts_fax: bool | NotGiven = NOT_GIVEN,
        accepts_sipr_net: bool | NotGiven = NOT_GIVEN,
        agency: str | NotGiven = NOT_GIVEN,
        alt_country_code: str | NotGiven = NOT_GIVEN,
        close_time: str | NotGiven = NOT_GIVEN,
        country_id: str | NotGiven = NOT_GIVEN,
        country_name: str | NotGiven = NOT_GIVEN,
        country_remark: str | NotGiven = NOT_GIVEN,
        diplomatic_clearance_country_contacts: Iterable[country_create_params.DiplomaticClearanceCountryContact]
        | NotGiven = NOT_GIVEN,
        diplomatic_clearance_country_entry_exit_points: Iterable[
            country_create_params.DiplomaticClearanceCountryEntryExitPoint
        ]
        | NotGiven = NOT_GIVEN,
        diplomatic_clearance_country_profiles: Iterable[country_create_params.DiplomaticClearanceCountryProfile]
        | NotGiven = NOT_GIVEN,
        existing_profile: bool | NotGiven = NOT_GIVEN,
        gmt_offset: str | NotGiven = NOT_GIVEN,
        office_name: str | NotGiven = NOT_GIVEN,
        office_poc: str | NotGiven = NOT_GIVEN,
        office_remark: str | NotGiven = NOT_GIVEN,
        open_fri: bool | NotGiven = NOT_GIVEN,
        open_mon: bool | NotGiven = NOT_GIVEN,
        open_sat: bool | NotGiven = NOT_GIVEN,
        open_sun: bool | NotGiven = NOT_GIVEN,
        open_thu: bool | NotGiven = NOT_GIVEN,
        open_time: str | NotGiven = NOT_GIVEN,
        open_tue: bool | NotGiven = NOT_GIVEN,
        open_wed: bool | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single diplomaticclearancecountry record as a POST
        body and ingest into the database. A specific role is required to perform this
        service operation. Please contact the UDL team for assistance.

        Args:
          classification_marking: Classification marking of the data in IC/CAPCO Portion-marked format.

          country_code: The DoD Standard Country Code designator for the country for which the
              diplomatic clearance will be issued. This field should be set to "OTHR" if the
              source value does not match a UDL country code value (ISO-3166-ALPHA-2).

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

          last_changed_date: Last time this country's diplomatic clearance profile information was updated,
              in ISO 8601 UTC format with millisecond precision.

          source: Source of the data.

          id: Unique identifier of the record, auto-generated by the system.

          accepts_dms: Flag indicating whether this country's diplomatic clearance office can receive
              messages using the Defense Message System (DMS).

          accepts_email: Flag indicating whether this country's diplomatic clearance office can receive
              messages via email.

          accepts_fax: Flag indicating whether this country's diplomatic clearance office can receive
              messages via fax.

          accepts_sipr_net: Flag indicating whether this country's diplomatic clearance office can receive
              messages via SIPRNet.

          agency: The source agency of the diplomatic clearance country data.

          alt_country_code: Specifies an alternate country code if the data provider code does not match a
              UDL Country code value (ISO-3166-ALPHA-2). This field will be set to the value
              provided by the source and should be used for all Queries specifying a Country
              Code.

          close_time: Zulu closing time of this country's diplomatic clearance office expressed in
              HH:MM format.

          country_id: System generated code used to identify a country.

          country_name: Name of the country for which the diplomatic clearance will be issued.

          country_remark: Remarks concerning the country for which the diplomatic clearance will be
              issued.

          diplomatic_clearance_country_contacts: Collection of diplomatic clearance profile information for this country.

          diplomatic_clearance_country_entry_exit_points: Collection of diplomatic clearance profile information for this country.

          diplomatic_clearance_country_profiles: Collection of diplomatic clearance profile information for this country.

          existing_profile: Flag indicating whether a diplomatic clearance profile exists for this country.

          gmt_offset: Time difference between the location of the country for which the diplomatic
              clearance will be issued and the Greenwich Mean Time (GMT), expressed as
              +/-HH:MM. Time zones east of Greenwich have positive offsets and time zones west
              of Greenwich are negative.

          office_name: Name of this country's diplomatic clearance office.

          office_poc: Name of the point of contact for this country's diplomatic clearance office.

          office_remark: Remarks concerning this country's diplomatic clearance office.

          open_fri: Flag indicating whether this country's diplomatic clearance office is open on
              Friday.

          open_mon: Flag indicating whether this country's diplomatic clearance office is open on
              Monday.

          open_sat: Flag indicating whether this country's diplomatic clearance office is open on
              Saturday.

          open_sun: Flag indicating whether this country's diplomatic clearance office is open on
              Sunday.

          open_thu: Flag indicating whether this country's diplomatic clearance office is open on
              Thursday.

          open_time: Zulu opening time of this country's diplomatic clearance office expressed in
              HH:MM format.

          open_tue: Flag indicating whether this country's diplomatic clearance office is open on
              Tuesday.

          open_wed: Flag indicating whether this country's diplomatic clearance office is open on
              Wednesday.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/udl/diplomaticclearancecountry",
            body=maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "country_code": country_code,
                    "data_mode": data_mode,
                    "last_changed_date": last_changed_date,
                    "source": source,
                    "id": id,
                    "accepts_dms": accepts_dms,
                    "accepts_email": accepts_email,
                    "accepts_fax": accepts_fax,
                    "accepts_sipr_net": accepts_sipr_net,
                    "agency": agency,
                    "alt_country_code": alt_country_code,
                    "close_time": close_time,
                    "country_id": country_id,
                    "country_name": country_name,
                    "country_remark": country_remark,
                    "diplomatic_clearance_country_contacts": diplomatic_clearance_country_contacts,
                    "diplomatic_clearance_country_entry_exit_points": diplomatic_clearance_country_entry_exit_points,
                    "diplomatic_clearance_country_profiles": diplomatic_clearance_country_profiles,
                    "existing_profile": existing_profile,
                    "gmt_offset": gmt_offset,
                    "office_name": office_name,
                    "office_poc": office_poc,
                    "office_remark": office_remark,
                    "open_fri": open_fri,
                    "open_mon": open_mon,
                    "open_sat": open_sat,
                    "open_sun": open_sun,
                    "open_thu": open_thu,
                    "open_time": open_time,
                    "open_tue": open_tue,
                    "open_wed": open_wed,
                    "origin": origin,
                },
                country_create_params.CountryCreateParams,
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
    ) -> CountryRetrieveResponse:
        """
        Service operation to get a single diplomaticclearancecountry record by its
        unique ID passed as a path parameter.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/udl/diplomaticclearancecountry/{id}",
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
                    country_retrieve_params.CountryRetrieveParams,
                ),
            ),
            cast_to=CountryRetrieveResponse,
        )

    def update(
        self,
        path_id: str,
        *,
        classification_marking: str,
        country_code: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        last_changed_date: Union[str, datetime],
        source: str,
        body_id: str | NotGiven = NOT_GIVEN,
        accepts_dms: bool | NotGiven = NOT_GIVEN,
        accepts_email: bool | NotGiven = NOT_GIVEN,
        accepts_fax: bool | NotGiven = NOT_GIVEN,
        accepts_sipr_net: bool | NotGiven = NOT_GIVEN,
        agency: str | NotGiven = NOT_GIVEN,
        alt_country_code: str | NotGiven = NOT_GIVEN,
        close_time: str | NotGiven = NOT_GIVEN,
        country_id: str | NotGiven = NOT_GIVEN,
        country_name: str | NotGiven = NOT_GIVEN,
        country_remark: str | NotGiven = NOT_GIVEN,
        diplomatic_clearance_country_contacts: Iterable[country_update_params.DiplomaticClearanceCountryContact]
        | NotGiven = NOT_GIVEN,
        diplomatic_clearance_country_entry_exit_points: Iterable[
            country_update_params.DiplomaticClearanceCountryEntryExitPoint
        ]
        | NotGiven = NOT_GIVEN,
        diplomatic_clearance_country_profiles: Iterable[country_update_params.DiplomaticClearanceCountryProfile]
        | NotGiven = NOT_GIVEN,
        existing_profile: bool | NotGiven = NOT_GIVEN,
        gmt_offset: str | NotGiven = NOT_GIVEN,
        office_name: str | NotGiven = NOT_GIVEN,
        office_poc: str | NotGiven = NOT_GIVEN,
        office_remark: str | NotGiven = NOT_GIVEN,
        open_fri: bool | NotGiven = NOT_GIVEN,
        open_mon: bool | NotGiven = NOT_GIVEN,
        open_sat: bool | NotGiven = NOT_GIVEN,
        open_sun: bool | NotGiven = NOT_GIVEN,
        open_thu: bool | NotGiven = NOT_GIVEN,
        open_time: str | NotGiven = NOT_GIVEN,
        open_tue: bool | NotGiven = NOT_GIVEN,
        open_wed: bool | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Service operation to update a single diplomaticclearancecountry record.

        A
        specific role is required to perform this service operation. Please contact the
        UDL team for assistance.

        Args:
          classification_marking: Classification marking of the data in IC/CAPCO Portion-marked format.

          country_code: The DoD Standard Country Code designator for the country for which the
              diplomatic clearance will be issued. This field should be set to "OTHR" if the
              source value does not match a UDL country code value (ISO-3166-ALPHA-2).

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

          last_changed_date: Last time this country's diplomatic clearance profile information was updated,
              in ISO 8601 UTC format with millisecond precision.

          source: Source of the data.

          body_id: Unique identifier of the record, auto-generated by the system.

          accepts_dms: Flag indicating whether this country's diplomatic clearance office can receive
              messages using the Defense Message System (DMS).

          accepts_email: Flag indicating whether this country's diplomatic clearance office can receive
              messages via email.

          accepts_fax: Flag indicating whether this country's diplomatic clearance office can receive
              messages via fax.

          accepts_sipr_net: Flag indicating whether this country's diplomatic clearance office can receive
              messages via SIPRNet.

          agency: The source agency of the diplomatic clearance country data.

          alt_country_code: Specifies an alternate country code if the data provider code does not match a
              UDL Country code value (ISO-3166-ALPHA-2). This field will be set to the value
              provided by the source and should be used for all Queries specifying a Country
              Code.

          close_time: Zulu closing time of this country's diplomatic clearance office expressed in
              HH:MM format.

          country_id: System generated code used to identify a country.

          country_name: Name of the country for which the diplomatic clearance will be issued.

          country_remark: Remarks concerning the country for which the diplomatic clearance will be
              issued.

          diplomatic_clearance_country_contacts: Collection of diplomatic clearance profile information for this country.

          diplomatic_clearance_country_entry_exit_points: Collection of diplomatic clearance profile information for this country.

          diplomatic_clearance_country_profiles: Collection of diplomatic clearance profile information for this country.

          existing_profile: Flag indicating whether a diplomatic clearance profile exists for this country.

          gmt_offset: Time difference between the location of the country for which the diplomatic
              clearance will be issued and the Greenwich Mean Time (GMT), expressed as
              +/-HH:MM. Time zones east of Greenwich have positive offsets and time zones west
              of Greenwich are negative.

          office_name: Name of this country's diplomatic clearance office.

          office_poc: Name of the point of contact for this country's diplomatic clearance office.

          office_remark: Remarks concerning this country's diplomatic clearance office.

          open_fri: Flag indicating whether this country's diplomatic clearance office is open on
              Friday.

          open_mon: Flag indicating whether this country's diplomatic clearance office is open on
              Monday.

          open_sat: Flag indicating whether this country's diplomatic clearance office is open on
              Saturday.

          open_sun: Flag indicating whether this country's diplomatic clearance office is open on
              Sunday.

          open_thu: Flag indicating whether this country's diplomatic clearance office is open on
              Thursday.

          open_time: Zulu opening time of this country's diplomatic clearance office expressed in
              HH:MM format.

          open_tue: Flag indicating whether this country's diplomatic clearance office is open on
              Tuesday.

          open_wed: Flag indicating whether this country's diplomatic clearance office is open on
              Wednesday.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            f"/udl/diplomaticclearancecountry/{path_id}",
            body=maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "country_code": country_code,
                    "data_mode": data_mode,
                    "last_changed_date": last_changed_date,
                    "source": source,
                    "body_id": body_id,
                    "accepts_dms": accepts_dms,
                    "accepts_email": accepts_email,
                    "accepts_fax": accepts_fax,
                    "accepts_sipr_net": accepts_sipr_net,
                    "agency": agency,
                    "alt_country_code": alt_country_code,
                    "close_time": close_time,
                    "country_id": country_id,
                    "country_name": country_name,
                    "country_remark": country_remark,
                    "diplomatic_clearance_country_contacts": diplomatic_clearance_country_contacts,
                    "diplomatic_clearance_country_entry_exit_points": diplomatic_clearance_country_entry_exit_points,
                    "diplomatic_clearance_country_profiles": diplomatic_clearance_country_profiles,
                    "existing_profile": existing_profile,
                    "gmt_offset": gmt_offset,
                    "office_name": office_name,
                    "office_poc": office_poc,
                    "office_remark": office_remark,
                    "open_fri": open_fri,
                    "open_mon": open_mon,
                    "open_sat": open_sat,
                    "open_sun": open_sun,
                    "open_thu": open_thu,
                    "open_time": open_time,
                    "open_tue": open_tue,
                    "open_wed": open_wed,
                    "origin": origin,
                },
                country_update_params.CountryUpdateParams,
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
    ) -> SyncOffsetPage[CountryListResponse]:
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
            "/udl/diplomaticclearancecountry",
            page=SyncOffsetPage[CountryListResponse],
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
                    country_list_params.CountryListParams,
                ),
            ),
            model=CountryListResponse,
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
        Service operation to delete a diplomaticclearancecountry record specified by the
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
            f"/udl/diplomaticclearancecountry/{id}",
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
            "/udl/diplomaticclearancecountry/count",
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
                    country_count_params.CountryCountParams,
                ),
            ),
            cast_to=str,
        )

    def create_bulk(
        self,
        *,
        body: Iterable[country_create_bulk_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation intended for initial integration only, to take a list of
        diplomaticclearancecountry records as a POST body and ingest into the database.
        This operation is not intended to be used for automated feeds into UDL. Data
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
            "/udl/diplomaticclearancecountry/createBulk",
            body=maybe_transform(body, Iterable[country_create_bulk_params.Body]),
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
    ) -> CountryQueryHelpResponse:
        """
        Service operation to provide detailed information on available dynamic query
        parameters for a particular data type.
        """
        return self._get(
            "/udl/diplomaticclearancecountry/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CountryQueryHelpResponse,
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
    ) -> CountryTupleResponse:
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
            "/udl/diplomaticclearancecountry/tuple",
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
                    country_tuple_params.CountryTupleParams,
                ),
            ),
            cast_to=CountryTupleResponse,
        )

    def unvalidated_publish(
        self,
        *,
        body: Iterable[country_unvalidated_publish_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take multiple diplomaticclearancecountry records as a POST
        body and ingest into the database. This operation is intended to be used for
        automated feeds into UDL. A specific role is required to perform this service
        operation. Please contact the UDL team for assistance.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/filedrop/udl-diplomaticclearancecountry",
            body=maybe_transform(body, Iterable[country_unvalidated_publish_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncCountryResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCountryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncCountryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCountryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncCountryResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        classification_marking: str,
        country_code: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        last_changed_date: Union[str, datetime],
        source: str,
        id: str | NotGiven = NOT_GIVEN,
        accepts_dms: bool | NotGiven = NOT_GIVEN,
        accepts_email: bool | NotGiven = NOT_GIVEN,
        accepts_fax: bool | NotGiven = NOT_GIVEN,
        accepts_sipr_net: bool | NotGiven = NOT_GIVEN,
        agency: str | NotGiven = NOT_GIVEN,
        alt_country_code: str | NotGiven = NOT_GIVEN,
        close_time: str | NotGiven = NOT_GIVEN,
        country_id: str | NotGiven = NOT_GIVEN,
        country_name: str | NotGiven = NOT_GIVEN,
        country_remark: str | NotGiven = NOT_GIVEN,
        diplomatic_clearance_country_contacts: Iterable[country_create_params.DiplomaticClearanceCountryContact]
        | NotGiven = NOT_GIVEN,
        diplomatic_clearance_country_entry_exit_points: Iterable[
            country_create_params.DiplomaticClearanceCountryEntryExitPoint
        ]
        | NotGiven = NOT_GIVEN,
        diplomatic_clearance_country_profiles: Iterable[country_create_params.DiplomaticClearanceCountryProfile]
        | NotGiven = NOT_GIVEN,
        existing_profile: bool | NotGiven = NOT_GIVEN,
        gmt_offset: str | NotGiven = NOT_GIVEN,
        office_name: str | NotGiven = NOT_GIVEN,
        office_poc: str | NotGiven = NOT_GIVEN,
        office_remark: str | NotGiven = NOT_GIVEN,
        open_fri: bool | NotGiven = NOT_GIVEN,
        open_mon: bool | NotGiven = NOT_GIVEN,
        open_sat: bool | NotGiven = NOT_GIVEN,
        open_sun: bool | NotGiven = NOT_GIVEN,
        open_thu: bool | NotGiven = NOT_GIVEN,
        open_time: str | NotGiven = NOT_GIVEN,
        open_tue: bool | NotGiven = NOT_GIVEN,
        open_wed: bool | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single diplomaticclearancecountry record as a POST
        body and ingest into the database. A specific role is required to perform this
        service operation. Please contact the UDL team for assistance.

        Args:
          classification_marking: Classification marking of the data in IC/CAPCO Portion-marked format.

          country_code: The DoD Standard Country Code designator for the country for which the
              diplomatic clearance will be issued. This field should be set to "OTHR" if the
              source value does not match a UDL country code value (ISO-3166-ALPHA-2).

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

          last_changed_date: Last time this country's diplomatic clearance profile information was updated,
              in ISO 8601 UTC format with millisecond precision.

          source: Source of the data.

          id: Unique identifier of the record, auto-generated by the system.

          accepts_dms: Flag indicating whether this country's diplomatic clearance office can receive
              messages using the Defense Message System (DMS).

          accepts_email: Flag indicating whether this country's diplomatic clearance office can receive
              messages via email.

          accepts_fax: Flag indicating whether this country's diplomatic clearance office can receive
              messages via fax.

          accepts_sipr_net: Flag indicating whether this country's diplomatic clearance office can receive
              messages via SIPRNet.

          agency: The source agency of the diplomatic clearance country data.

          alt_country_code: Specifies an alternate country code if the data provider code does not match a
              UDL Country code value (ISO-3166-ALPHA-2). This field will be set to the value
              provided by the source and should be used for all Queries specifying a Country
              Code.

          close_time: Zulu closing time of this country's diplomatic clearance office expressed in
              HH:MM format.

          country_id: System generated code used to identify a country.

          country_name: Name of the country for which the diplomatic clearance will be issued.

          country_remark: Remarks concerning the country for which the diplomatic clearance will be
              issued.

          diplomatic_clearance_country_contacts: Collection of diplomatic clearance profile information for this country.

          diplomatic_clearance_country_entry_exit_points: Collection of diplomatic clearance profile information for this country.

          diplomatic_clearance_country_profiles: Collection of diplomatic clearance profile information for this country.

          existing_profile: Flag indicating whether a diplomatic clearance profile exists for this country.

          gmt_offset: Time difference between the location of the country for which the diplomatic
              clearance will be issued and the Greenwich Mean Time (GMT), expressed as
              +/-HH:MM. Time zones east of Greenwich have positive offsets and time zones west
              of Greenwich are negative.

          office_name: Name of this country's diplomatic clearance office.

          office_poc: Name of the point of contact for this country's diplomatic clearance office.

          office_remark: Remarks concerning this country's diplomatic clearance office.

          open_fri: Flag indicating whether this country's diplomatic clearance office is open on
              Friday.

          open_mon: Flag indicating whether this country's diplomatic clearance office is open on
              Monday.

          open_sat: Flag indicating whether this country's diplomatic clearance office is open on
              Saturday.

          open_sun: Flag indicating whether this country's diplomatic clearance office is open on
              Sunday.

          open_thu: Flag indicating whether this country's diplomatic clearance office is open on
              Thursday.

          open_time: Zulu opening time of this country's diplomatic clearance office expressed in
              HH:MM format.

          open_tue: Flag indicating whether this country's diplomatic clearance office is open on
              Tuesday.

          open_wed: Flag indicating whether this country's diplomatic clearance office is open on
              Wednesday.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/udl/diplomaticclearancecountry",
            body=await async_maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "country_code": country_code,
                    "data_mode": data_mode,
                    "last_changed_date": last_changed_date,
                    "source": source,
                    "id": id,
                    "accepts_dms": accepts_dms,
                    "accepts_email": accepts_email,
                    "accepts_fax": accepts_fax,
                    "accepts_sipr_net": accepts_sipr_net,
                    "agency": agency,
                    "alt_country_code": alt_country_code,
                    "close_time": close_time,
                    "country_id": country_id,
                    "country_name": country_name,
                    "country_remark": country_remark,
                    "diplomatic_clearance_country_contacts": diplomatic_clearance_country_contacts,
                    "diplomatic_clearance_country_entry_exit_points": diplomatic_clearance_country_entry_exit_points,
                    "diplomatic_clearance_country_profiles": diplomatic_clearance_country_profiles,
                    "existing_profile": existing_profile,
                    "gmt_offset": gmt_offset,
                    "office_name": office_name,
                    "office_poc": office_poc,
                    "office_remark": office_remark,
                    "open_fri": open_fri,
                    "open_mon": open_mon,
                    "open_sat": open_sat,
                    "open_sun": open_sun,
                    "open_thu": open_thu,
                    "open_time": open_time,
                    "open_tue": open_tue,
                    "open_wed": open_wed,
                    "origin": origin,
                },
                country_create_params.CountryCreateParams,
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
    ) -> CountryRetrieveResponse:
        """
        Service operation to get a single diplomaticclearancecountry record by its
        unique ID passed as a path parameter.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/udl/diplomaticclearancecountry/{id}",
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
                    country_retrieve_params.CountryRetrieveParams,
                ),
            ),
            cast_to=CountryRetrieveResponse,
        )

    async def update(
        self,
        path_id: str,
        *,
        classification_marking: str,
        country_code: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        last_changed_date: Union[str, datetime],
        source: str,
        body_id: str | NotGiven = NOT_GIVEN,
        accepts_dms: bool | NotGiven = NOT_GIVEN,
        accepts_email: bool | NotGiven = NOT_GIVEN,
        accepts_fax: bool | NotGiven = NOT_GIVEN,
        accepts_sipr_net: bool | NotGiven = NOT_GIVEN,
        agency: str | NotGiven = NOT_GIVEN,
        alt_country_code: str | NotGiven = NOT_GIVEN,
        close_time: str | NotGiven = NOT_GIVEN,
        country_id: str | NotGiven = NOT_GIVEN,
        country_name: str | NotGiven = NOT_GIVEN,
        country_remark: str | NotGiven = NOT_GIVEN,
        diplomatic_clearance_country_contacts: Iterable[country_update_params.DiplomaticClearanceCountryContact]
        | NotGiven = NOT_GIVEN,
        diplomatic_clearance_country_entry_exit_points: Iterable[
            country_update_params.DiplomaticClearanceCountryEntryExitPoint
        ]
        | NotGiven = NOT_GIVEN,
        diplomatic_clearance_country_profiles: Iterable[country_update_params.DiplomaticClearanceCountryProfile]
        | NotGiven = NOT_GIVEN,
        existing_profile: bool | NotGiven = NOT_GIVEN,
        gmt_offset: str | NotGiven = NOT_GIVEN,
        office_name: str | NotGiven = NOT_GIVEN,
        office_poc: str | NotGiven = NOT_GIVEN,
        office_remark: str | NotGiven = NOT_GIVEN,
        open_fri: bool | NotGiven = NOT_GIVEN,
        open_mon: bool | NotGiven = NOT_GIVEN,
        open_sat: bool | NotGiven = NOT_GIVEN,
        open_sun: bool | NotGiven = NOT_GIVEN,
        open_thu: bool | NotGiven = NOT_GIVEN,
        open_time: str | NotGiven = NOT_GIVEN,
        open_tue: bool | NotGiven = NOT_GIVEN,
        open_wed: bool | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Service operation to update a single diplomaticclearancecountry record.

        A
        specific role is required to perform this service operation. Please contact the
        UDL team for assistance.

        Args:
          classification_marking: Classification marking of the data in IC/CAPCO Portion-marked format.

          country_code: The DoD Standard Country Code designator for the country for which the
              diplomatic clearance will be issued. This field should be set to "OTHR" if the
              source value does not match a UDL country code value (ISO-3166-ALPHA-2).

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

          last_changed_date: Last time this country's diplomatic clearance profile information was updated,
              in ISO 8601 UTC format with millisecond precision.

          source: Source of the data.

          body_id: Unique identifier of the record, auto-generated by the system.

          accepts_dms: Flag indicating whether this country's diplomatic clearance office can receive
              messages using the Defense Message System (DMS).

          accepts_email: Flag indicating whether this country's diplomatic clearance office can receive
              messages via email.

          accepts_fax: Flag indicating whether this country's diplomatic clearance office can receive
              messages via fax.

          accepts_sipr_net: Flag indicating whether this country's diplomatic clearance office can receive
              messages via SIPRNet.

          agency: The source agency of the diplomatic clearance country data.

          alt_country_code: Specifies an alternate country code if the data provider code does not match a
              UDL Country code value (ISO-3166-ALPHA-2). This field will be set to the value
              provided by the source and should be used for all Queries specifying a Country
              Code.

          close_time: Zulu closing time of this country's diplomatic clearance office expressed in
              HH:MM format.

          country_id: System generated code used to identify a country.

          country_name: Name of the country for which the diplomatic clearance will be issued.

          country_remark: Remarks concerning the country for which the diplomatic clearance will be
              issued.

          diplomatic_clearance_country_contacts: Collection of diplomatic clearance profile information for this country.

          diplomatic_clearance_country_entry_exit_points: Collection of diplomatic clearance profile information for this country.

          diplomatic_clearance_country_profiles: Collection of diplomatic clearance profile information for this country.

          existing_profile: Flag indicating whether a diplomatic clearance profile exists for this country.

          gmt_offset: Time difference between the location of the country for which the diplomatic
              clearance will be issued and the Greenwich Mean Time (GMT), expressed as
              +/-HH:MM. Time zones east of Greenwich have positive offsets and time zones west
              of Greenwich are negative.

          office_name: Name of this country's diplomatic clearance office.

          office_poc: Name of the point of contact for this country's diplomatic clearance office.

          office_remark: Remarks concerning this country's diplomatic clearance office.

          open_fri: Flag indicating whether this country's diplomatic clearance office is open on
              Friday.

          open_mon: Flag indicating whether this country's diplomatic clearance office is open on
              Monday.

          open_sat: Flag indicating whether this country's diplomatic clearance office is open on
              Saturday.

          open_sun: Flag indicating whether this country's diplomatic clearance office is open on
              Sunday.

          open_thu: Flag indicating whether this country's diplomatic clearance office is open on
              Thursday.

          open_time: Zulu opening time of this country's diplomatic clearance office expressed in
              HH:MM format.

          open_tue: Flag indicating whether this country's diplomatic clearance office is open on
              Tuesday.

          open_wed: Flag indicating whether this country's diplomatic clearance office is open on
              Wednesday.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            f"/udl/diplomaticclearancecountry/{path_id}",
            body=await async_maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "country_code": country_code,
                    "data_mode": data_mode,
                    "last_changed_date": last_changed_date,
                    "source": source,
                    "body_id": body_id,
                    "accepts_dms": accepts_dms,
                    "accepts_email": accepts_email,
                    "accepts_fax": accepts_fax,
                    "accepts_sipr_net": accepts_sipr_net,
                    "agency": agency,
                    "alt_country_code": alt_country_code,
                    "close_time": close_time,
                    "country_id": country_id,
                    "country_name": country_name,
                    "country_remark": country_remark,
                    "diplomatic_clearance_country_contacts": diplomatic_clearance_country_contacts,
                    "diplomatic_clearance_country_entry_exit_points": diplomatic_clearance_country_entry_exit_points,
                    "diplomatic_clearance_country_profiles": diplomatic_clearance_country_profiles,
                    "existing_profile": existing_profile,
                    "gmt_offset": gmt_offset,
                    "office_name": office_name,
                    "office_poc": office_poc,
                    "office_remark": office_remark,
                    "open_fri": open_fri,
                    "open_mon": open_mon,
                    "open_sat": open_sat,
                    "open_sun": open_sun,
                    "open_thu": open_thu,
                    "open_time": open_time,
                    "open_tue": open_tue,
                    "open_wed": open_wed,
                    "origin": origin,
                },
                country_update_params.CountryUpdateParams,
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
    ) -> AsyncPaginator[CountryListResponse, AsyncOffsetPage[CountryListResponse]]:
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
            "/udl/diplomaticclearancecountry",
            page=AsyncOffsetPage[CountryListResponse],
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
                    country_list_params.CountryListParams,
                ),
            ),
            model=CountryListResponse,
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
        Service operation to delete a diplomaticclearancecountry record specified by the
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
            f"/udl/diplomaticclearancecountry/{id}",
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
            "/udl/diplomaticclearancecountry/count",
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
                    country_count_params.CountryCountParams,
                ),
            ),
            cast_to=str,
        )

    async def create_bulk(
        self,
        *,
        body: Iterable[country_create_bulk_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation intended for initial integration only, to take a list of
        diplomaticclearancecountry records as a POST body and ingest into the database.
        This operation is not intended to be used for automated feeds into UDL. Data
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
            "/udl/diplomaticclearancecountry/createBulk",
            body=await async_maybe_transform(body, Iterable[country_create_bulk_params.Body]),
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
    ) -> CountryQueryHelpResponse:
        """
        Service operation to provide detailed information on available dynamic query
        parameters for a particular data type.
        """
        return await self._get(
            "/udl/diplomaticclearancecountry/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CountryQueryHelpResponse,
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
    ) -> CountryTupleResponse:
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
            "/udl/diplomaticclearancecountry/tuple",
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
                    country_tuple_params.CountryTupleParams,
                ),
            ),
            cast_to=CountryTupleResponse,
        )

    async def unvalidated_publish(
        self,
        *,
        body: Iterable[country_unvalidated_publish_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take multiple diplomaticclearancecountry records as a POST
        body and ingest into the database. This operation is intended to be used for
        automated feeds into UDL. A specific role is required to perform this service
        operation. Please contact the UDL team for assistance.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/filedrop/udl-diplomaticclearancecountry",
            body=await async_maybe_transform(body, Iterable[country_unvalidated_publish_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class CountryResourceWithRawResponse:
    def __init__(self, country: CountryResource) -> None:
        self._country = country

        self.create = to_raw_response_wrapper(
            country.create,
        )
        self.retrieve = to_raw_response_wrapper(
            country.retrieve,
        )
        self.update = to_raw_response_wrapper(
            country.update,
        )
        self.list = to_raw_response_wrapper(
            country.list,
        )
        self.delete = to_raw_response_wrapper(
            country.delete,
        )
        self.count = to_raw_response_wrapper(
            country.count,
        )
        self.create_bulk = to_raw_response_wrapper(
            country.create_bulk,
        )
        self.query_help = to_raw_response_wrapper(
            country.query_help,
        )
        self.tuple = to_raw_response_wrapper(
            country.tuple,
        )
        self.unvalidated_publish = to_raw_response_wrapper(
            country.unvalidated_publish,
        )


class AsyncCountryResourceWithRawResponse:
    def __init__(self, country: AsyncCountryResource) -> None:
        self._country = country

        self.create = async_to_raw_response_wrapper(
            country.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            country.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            country.update,
        )
        self.list = async_to_raw_response_wrapper(
            country.list,
        )
        self.delete = async_to_raw_response_wrapper(
            country.delete,
        )
        self.count = async_to_raw_response_wrapper(
            country.count,
        )
        self.create_bulk = async_to_raw_response_wrapper(
            country.create_bulk,
        )
        self.query_help = async_to_raw_response_wrapper(
            country.query_help,
        )
        self.tuple = async_to_raw_response_wrapper(
            country.tuple,
        )
        self.unvalidated_publish = async_to_raw_response_wrapper(
            country.unvalidated_publish,
        )


class CountryResourceWithStreamingResponse:
    def __init__(self, country: CountryResource) -> None:
        self._country = country

        self.create = to_streamed_response_wrapper(
            country.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            country.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            country.update,
        )
        self.list = to_streamed_response_wrapper(
            country.list,
        )
        self.delete = to_streamed_response_wrapper(
            country.delete,
        )
        self.count = to_streamed_response_wrapper(
            country.count,
        )
        self.create_bulk = to_streamed_response_wrapper(
            country.create_bulk,
        )
        self.query_help = to_streamed_response_wrapper(
            country.query_help,
        )
        self.tuple = to_streamed_response_wrapper(
            country.tuple,
        )
        self.unvalidated_publish = to_streamed_response_wrapper(
            country.unvalidated_publish,
        )


class AsyncCountryResourceWithStreamingResponse:
    def __init__(self, country: AsyncCountryResource) -> None:
        self._country = country

        self.create = async_to_streamed_response_wrapper(
            country.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            country.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            country.update,
        )
        self.list = async_to_streamed_response_wrapper(
            country.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            country.delete,
        )
        self.count = async_to_streamed_response_wrapper(
            country.count,
        )
        self.create_bulk = async_to_streamed_response_wrapper(
            country.create_bulk,
        )
        self.query_help = async_to_streamed_response_wrapper(
            country.query_help,
        )
        self.tuple = async_to_streamed_response_wrapper(
            country.tuple,
        )
        self.unvalidated_publish = async_to_streamed_response_wrapper(
            country.unvalidated_publish,
        )
