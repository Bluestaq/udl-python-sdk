# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import (
    organizationdetail_get_params,
    organizationdetail_list_params,
    organizationdetail_create_params,
    organizationdetail_update_params,
    organizationdetail_find_by_source_params,
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
from ..types.organization_details_full import OrganizationDetailsFull
from ..types.organizationdetail_list_response import OrganizationdetailListResponse
from ..types.organizationdetail_find_by_source_response import OrganizationdetailFindBySourceResponse

__all__ = ["OrganizationdetailsResource", "AsyncOrganizationdetailsResource"]


class OrganizationdetailsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OrganizationdetailsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return OrganizationdetailsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OrganizationdetailsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return OrganizationdetailsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        id_organization: str,
        name: str,
        source: str,
        id: str | NotGiven = NOT_GIVEN,
        address1: str | NotGiven = NOT_GIVEN,
        address2: str | NotGiven = NOT_GIVEN,
        address3: str | NotGiven = NOT_GIVEN,
        broker: str | NotGiven = NOT_GIVEN,
        ceo: str | NotGiven = NOT_GIVEN,
        cfo: str | NotGiven = NOT_GIVEN,
        cto: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        ebitda: float | NotGiven = NOT_GIVEN,
        email: str | NotGiven = NOT_GIVEN,
        financial_notes: str | NotGiven = NOT_GIVEN,
        financial_year_end_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        fleet_plan_notes: str | NotGiven = NOT_GIVEN,
        former_org_id: str | NotGiven = NOT_GIVEN,
        ftes: int | NotGiven = NOT_GIVEN,
        geo_admin_level1: str | NotGiven = NOT_GIVEN,
        geo_admin_level2: str | NotGiven = NOT_GIVEN,
        geo_admin_level3: str | NotGiven = NOT_GIVEN,
        mass_ranking: int | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        parent_org_id: str | NotGiven = NOT_GIVEN,
        postal_code: str | NotGiven = NOT_GIVEN,
        profit: float | NotGiven = NOT_GIVEN,
        revenue: float | NotGiven = NOT_GIVEN,
        revenue_ranking: int | NotGiven = NOT_GIVEN,
        risk_manager: str | NotGiven = NOT_GIVEN,
        services_notes: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single OrganizationDetails as a POST body and ingest
        into the database. OrganizationDetails represent details of organizations such
        as a corporation, manufacturer, consortium, government, etc. An organization can
        have detail records from several sources. A specific role is required to perform
        this service operation. Please contact the UDL team for assistance.

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

          id_organization: Unique identifier of the parent organization.

          name: Organization details name.

          source: Source of the data.

          id: Unique identifier of the record, auto-generated by the system.

          address1: Street number of the organization.

          address2: Field for additional organization address information such as PO Box and unit
              number.

          address3: Contains the third line of address information for an organization.

          broker: Designated broker for this organization.

          ceo: For organizations of type CORPORATION, the name of the Chief Executive Officer.

          cfo: For organizations of type CORPORATION, the name of the Chief Financial Officer.

          cto: For organizations of type CORPORATION, the name of the Chief Technology Officer.

          description: Organization description.

          ebitda: For organizations of type CORPORATION, the company EBITDA value as of
              financialYearEndDate in US Dollars.

          email: Listed contact email address for the organization.

          financial_notes: For organizations of type CORPORATION, notes on company financials.

          financial_year_end_date: For organizations of type CORPORATION, the effective financial year end date for
              revenue, EBITDA, and profit values.

          fleet_plan_notes: Satellite fleet planning notes for this organization.

          former_org_id: Former organization ID (if this organization previously existed as another
              organization).

          ftes: Total number of FTEs in this organization.

          geo_admin_level1: Administrative boundaries of the first sub-national level. Level 1 is simply the
              largest demarcation under whatever demarcation criteria has been determined by
              the governing body. For example, this may be a state or province.

          geo_admin_level2: Administrative boundaries of the second sub-national level. Level 2 is simply
              the second largest demarcation under whatever demarcation criteria has been
              determined by the governing body. For example, this may be a county or district.

          geo_admin_level3: Administrative boundaries of the third sub-national level. Level 3 is simply the
              third largest demarcation under whatever demarcation criteria has been
              determined by the governing body. For example, this may be a city or township.

          mass_ranking: Mass ranking for this organization.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          parent_org_id: Parent organization ID of this organization if it is a child organization.

          postal_code: A postal code, such as PIN or ZIP Code, is a series of letters or digits or both
              included in the postal address of the organization.

          profit: For organizations of type CORPORATION, total annual profit as of
              financialYearEndDate in US Dollars.

          revenue: For organizations of type CORPORATION, total annual revenue as of
              financialYearEndDate in US Dollars.

          revenue_ranking: Revenue ranking for this organization.

          risk_manager: The name of the risk manager for the organization.

          services_notes: Notes on the services provided by the organization.

          tags: Optional array of provider/source specific tags for this data, where each
              element is no longer than 32 characters, used for implementing data owner
              conditional access controls to restrict access to the data. Should be left null
              by data providers unless conditional access controls are coordinated with the
              UDL team.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/udl/organizationdetails",
            body=maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "id_organization": id_organization,
                    "name": name,
                    "source": source,
                    "id": id,
                    "address1": address1,
                    "address2": address2,
                    "address3": address3,
                    "broker": broker,
                    "ceo": ceo,
                    "cfo": cfo,
                    "cto": cto,
                    "description": description,
                    "ebitda": ebitda,
                    "email": email,
                    "financial_notes": financial_notes,
                    "financial_year_end_date": financial_year_end_date,
                    "fleet_plan_notes": fleet_plan_notes,
                    "former_org_id": former_org_id,
                    "ftes": ftes,
                    "geo_admin_level1": geo_admin_level1,
                    "geo_admin_level2": geo_admin_level2,
                    "geo_admin_level3": geo_admin_level3,
                    "mass_ranking": mass_ranking,
                    "origin": origin,
                    "parent_org_id": parent_org_id,
                    "postal_code": postal_code,
                    "profit": profit,
                    "revenue": revenue,
                    "revenue_ranking": revenue_ranking,
                    "risk_manager": risk_manager,
                    "services_notes": services_notes,
                    "tags": tags,
                },
                organizationdetail_create_params.OrganizationdetailCreateParams,
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
        id_organization: str,
        name: str,
        source: str,
        body_id: str | NotGiven = NOT_GIVEN,
        address1: str | NotGiven = NOT_GIVEN,
        address2: str | NotGiven = NOT_GIVEN,
        address3: str | NotGiven = NOT_GIVEN,
        broker: str | NotGiven = NOT_GIVEN,
        ceo: str | NotGiven = NOT_GIVEN,
        cfo: str | NotGiven = NOT_GIVEN,
        cto: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        ebitda: float | NotGiven = NOT_GIVEN,
        email: str | NotGiven = NOT_GIVEN,
        financial_notes: str | NotGiven = NOT_GIVEN,
        financial_year_end_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        fleet_plan_notes: str | NotGiven = NOT_GIVEN,
        former_org_id: str | NotGiven = NOT_GIVEN,
        ftes: int | NotGiven = NOT_GIVEN,
        geo_admin_level1: str | NotGiven = NOT_GIVEN,
        geo_admin_level2: str | NotGiven = NOT_GIVEN,
        geo_admin_level3: str | NotGiven = NOT_GIVEN,
        mass_ranking: int | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        parent_org_id: str | NotGiven = NOT_GIVEN,
        postal_code: str | NotGiven = NOT_GIVEN,
        profit: float | NotGiven = NOT_GIVEN,
        revenue: float | NotGiven = NOT_GIVEN,
        revenue_ranking: int | NotGiven = NOT_GIVEN,
        risk_manager: str | NotGiven = NOT_GIVEN,
        services_notes: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Service operation to update an OrganizationDetails object.

        OrganizationDetails
        represent details of organizations such as a corporation, manufacturer,
        consortium, government, etc. An organization can have detail records from
        several sources. A specific role is required to perform this service operation.
        Please contact the UDL team for assistance.

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

          id_organization: Unique identifier of the parent organization.

          name: Organization details name.

          source: Source of the data.

          body_id: Unique identifier of the record, auto-generated by the system.

          address1: Street number of the organization.

          address2: Field for additional organization address information such as PO Box and unit
              number.

          address3: Contains the third line of address information for an organization.

          broker: Designated broker for this organization.

          ceo: For organizations of type CORPORATION, the name of the Chief Executive Officer.

          cfo: For organizations of type CORPORATION, the name of the Chief Financial Officer.

          cto: For organizations of type CORPORATION, the name of the Chief Technology Officer.

          description: Organization description.

          ebitda: For organizations of type CORPORATION, the company EBITDA value as of
              financialYearEndDate in US Dollars.

          email: Listed contact email address for the organization.

          financial_notes: For organizations of type CORPORATION, notes on company financials.

          financial_year_end_date: For organizations of type CORPORATION, the effective financial year end date for
              revenue, EBITDA, and profit values.

          fleet_plan_notes: Satellite fleet planning notes for this organization.

          former_org_id: Former organization ID (if this organization previously existed as another
              organization).

          ftes: Total number of FTEs in this organization.

          geo_admin_level1: Administrative boundaries of the first sub-national level. Level 1 is simply the
              largest demarcation under whatever demarcation criteria has been determined by
              the governing body. For example, this may be a state or province.

          geo_admin_level2: Administrative boundaries of the second sub-national level. Level 2 is simply
              the second largest demarcation under whatever demarcation criteria has been
              determined by the governing body. For example, this may be a county or district.

          geo_admin_level3: Administrative boundaries of the third sub-national level. Level 3 is simply the
              third largest demarcation under whatever demarcation criteria has been
              determined by the governing body. For example, this may be a city or township.

          mass_ranking: Mass ranking for this organization.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          parent_org_id: Parent organization ID of this organization if it is a child organization.

          postal_code: A postal code, such as PIN or ZIP Code, is a series of letters or digits or both
              included in the postal address of the organization.

          profit: For organizations of type CORPORATION, total annual profit as of
              financialYearEndDate in US Dollars.

          revenue: For organizations of type CORPORATION, total annual revenue as of
              financialYearEndDate in US Dollars.

          revenue_ranking: Revenue ranking for this organization.

          risk_manager: The name of the risk manager for the organization.

          services_notes: Notes on the services provided by the organization.

          tags: Optional array of provider/source specific tags for this data, where each
              element is no longer than 32 characters, used for implementing data owner
              conditional access controls to restrict access to the data. Should be left null
              by data providers unless conditional access controls are coordinated with the
              UDL team.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            f"/udl/organizationdetails/{path_id}",
            body=maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "id_organization": id_organization,
                    "name": name,
                    "source": source,
                    "body_id": body_id,
                    "address1": address1,
                    "address2": address2,
                    "address3": address3,
                    "broker": broker,
                    "ceo": ceo,
                    "cfo": cfo,
                    "cto": cto,
                    "description": description,
                    "ebitda": ebitda,
                    "email": email,
                    "financial_notes": financial_notes,
                    "financial_year_end_date": financial_year_end_date,
                    "fleet_plan_notes": fleet_plan_notes,
                    "former_org_id": former_org_id,
                    "ftes": ftes,
                    "geo_admin_level1": geo_admin_level1,
                    "geo_admin_level2": geo_admin_level2,
                    "geo_admin_level3": geo_admin_level3,
                    "mass_ranking": mass_ranking,
                    "origin": origin,
                    "parent_org_id": parent_org_id,
                    "postal_code": postal_code,
                    "profit": profit,
                    "revenue": revenue,
                    "revenue_ranking": revenue_ranking,
                    "risk_manager": risk_manager,
                    "services_notes": services_notes,
                    "tags": tags,
                },
                organizationdetail_update_params.OrganizationdetailUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        *,
        name: str,
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncOffsetPage[OrganizationdetailListResponse]:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          name: Organization details name.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/organizationdetails",
            page=SyncOffsetPage[OrganizationdetailListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "name": name,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    organizationdetail_list_params.OrganizationdetailListParams,
                ),
            ),
            model=OrganizationdetailListResponse,
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
        Service operation to delete an OrganizationDetails specified by the passed ID
        path parameter. OrganizationDetails represent details of organizations such as a
        corporation, manufacturer, consortium, government, etc. An organization can have
        detail records from several sources. A specific role is required to perform this
        service operation. Please contact the UDL team for assistance.

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
            f"/udl/organizationdetails/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def find_by_source(
        self,
        *,
        name: str,
        source: str,
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrganizationdetailFindBySourceResponse:
        """
        Service operation to get a single OrganizationDetails by a source passed as a
        query parameter. OrganizationDetails represent details of organizations such as
        a corporation, manufacturer, consortium, government, etc. An organization can
        have detail records from several sources.

        Args:
          name: Organization details name.

          source: The source of the OrganizationDetails records to find.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/udl/organizationdetails/findBySource",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "name": name,
                        "source": source,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    organizationdetail_find_by_source_params.OrganizationdetailFindBySourceParams,
                ),
            ),
            cast_to=OrganizationdetailFindBySourceResponse,
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
    ) -> OrganizationDetailsFull:
        """
        Service operation to get a single OrganizationDetails by its unique ID passed as
        a path parameter. OrganizationDetails represent details of organizations such as
        a corporation, manufacturer, consortium, government, etc. An organization can
        have detail records from several sources.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/udl/organizationdetails/{id}",
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
                    organizationdetail_get_params.OrganizationdetailGetParams,
                ),
            ),
            cast_to=OrganizationDetailsFull,
        )


class AsyncOrganizationdetailsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOrganizationdetailsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncOrganizationdetailsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOrganizationdetailsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncOrganizationdetailsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        id_organization: str,
        name: str,
        source: str,
        id: str | NotGiven = NOT_GIVEN,
        address1: str | NotGiven = NOT_GIVEN,
        address2: str | NotGiven = NOT_GIVEN,
        address3: str | NotGiven = NOT_GIVEN,
        broker: str | NotGiven = NOT_GIVEN,
        ceo: str | NotGiven = NOT_GIVEN,
        cfo: str | NotGiven = NOT_GIVEN,
        cto: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        ebitda: float | NotGiven = NOT_GIVEN,
        email: str | NotGiven = NOT_GIVEN,
        financial_notes: str | NotGiven = NOT_GIVEN,
        financial_year_end_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        fleet_plan_notes: str | NotGiven = NOT_GIVEN,
        former_org_id: str | NotGiven = NOT_GIVEN,
        ftes: int | NotGiven = NOT_GIVEN,
        geo_admin_level1: str | NotGiven = NOT_GIVEN,
        geo_admin_level2: str | NotGiven = NOT_GIVEN,
        geo_admin_level3: str | NotGiven = NOT_GIVEN,
        mass_ranking: int | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        parent_org_id: str | NotGiven = NOT_GIVEN,
        postal_code: str | NotGiven = NOT_GIVEN,
        profit: float | NotGiven = NOT_GIVEN,
        revenue: float | NotGiven = NOT_GIVEN,
        revenue_ranking: int | NotGiven = NOT_GIVEN,
        risk_manager: str | NotGiven = NOT_GIVEN,
        services_notes: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single OrganizationDetails as a POST body and ingest
        into the database. OrganizationDetails represent details of organizations such
        as a corporation, manufacturer, consortium, government, etc. An organization can
        have detail records from several sources. A specific role is required to perform
        this service operation. Please contact the UDL team for assistance.

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

          id_organization: Unique identifier of the parent organization.

          name: Organization details name.

          source: Source of the data.

          id: Unique identifier of the record, auto-generated by the system.

          address1: Street number of the organization.

          address2: Field for additional organization address information such as PO Box and unit
              number.

          address3: Contains the third line of address information for an organization.

          broker: Designated broker for this organization.

          ceo: For organizations of type CORPORATION, the name of the Chief Executive Officer.

          cfo: For organizations of type CORPORATION, the name of the Chief Financial Officer.

          cto: For organizations of type CORPORATION, the name of the Chief Technology Officer.

          description: Organization description.

          ebitda: For organizations of type CORPORATION, the company EBITDA value as of
              financialYearEndDate in US Dollars.

          email: Listed contact email address for the organization.

          financial_notes: For organizations of type CORPORATION, notes on company financials.

          financial_year_end_date: For organizations of type CORPORATION, the effective financial year end date for
              revenue, EBITDA, and profit values.

          fleet_plan_notes: Satellite fleet planning notes for this organization.

          former_org_id: Former organization ID (if this organization previously existed as another
              organization).

          ftes: Total number of FTEs in this organization.

          geo_admin_level1: Administrative boundaries of the first sub-national level. Level 1 is simply the
              largest demarcation under whatever demarcation criteria has been determined by
              the governing body. For example, this may be a state or province.

          geo_admin_level2: Administrative boundaries of the second sub-national level. Level 2 is simply
              the second largest demarcation under whatever demarcation criteria has been
              determined by the governing body. For example, this may be a county or district.

          geo_admin_level3: Administrative boundaries of the third sub-national level. Level 3 is simply the
              third largest demarcation under whatever demarcation criteria has been
              determined by the governing body. For example, this may be a city or township.

          mass_ranking: Mass ranking for this organization.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          parent_org_id: Parent organization ID of this organization if it is a child organization.

          postal_code: A postal code, such as PIN or ZIP Code, is a series of letters or digits or both
              included in the postal address of the organization.

          profit: For organizations of type CORPORATION, total annual profit as of
              financialYearEndDate in US Dollars.

          revenue: For organizations of type CORPORATION, total annual revenue as of
              financialYearEndDate in US Dollars.

          revenue_ranking: Revenue ranking for this organization.

          risk_manager: The name of the risk manager for the organization.

          services_notes: Notes on the services provided by the organization.

          tags: Optional array of provider/source specific tags for this data, where each
              element is no longer than 32 characters, used for implementing data owner
              conditional access controls to restrict access to the data. Should be left null
              by data providers unless conditional access controls are coordinated with the
              UDL team.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/udl/organizationdetails",
            body=await async_maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "id_organization": id_organization,
                    "name": name,
                    "source": source,
                    "id": id,
                    "address1": address1,
                    "address2": address2,
                    "address3": address3,
                    "broker": broker,
                    "ceo": ceo,
                    "cfo": cfo,
                    "cto": cto,
                    "description": description,
                    "ebitda": ebitda,
                    "email": email,
                    "financial_notes": financial_notes,
                    "financial_year_end_date": financial_year_end_date,
                    "fleet_plan_notes": fleet_plan_notes,
                    "former_org_id": former_org_id,
                    "ftes": ftes,
                    "geo_admin_level1": geo_admin_level1,
                    "geo_admin_level2": geo_admin_level2,
                    "geo_admin_level3": geo_admin_level3,
                    "mass_ranking": mass_ranking,
                    "origin": origin,
                    "parent_org_id": parent_org_id,
                    "postal_code": postal_code,
                    "profit": profit,
                    "revenue": revenue,
                    "revenue_ranking": revenue_ranking,
                    "risk_manager": risk_manager,
                    "services_notes": services_notes,
                    "tags": tags,
                },
                organizationdetail_create_params.OrganizationdetailCreateParams,
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
        id_organization: str,
        name: str,
        source: str,
        body_id: str | NotGiven = NOT_GIVEN,
        address1: str | NotGiven = NOT_GIVEN,
        address2: str | NotGiven = NOT_GIVEN,
        address3: str | NotGiven = NOT_GIVEN,
        broker: str | NotGiven = NOT_GIVEN,
        ceo: str | NotGiven = NOT_GIVEN,
        cfo: str | NotGiven = NOT_GIVEN,
        cto: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        ebitda: float | NotGiven = NOT_GIVEN,
        email: str | NotGiven = NOT_GIVEN,
        financial_notes: str | NotGiven = NOT_GIVEN,
        financial_year_end_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        fleet_plan_notes: str | NotGiven = NOT_GIVEN,
        former_org_id: str | NotGiven = NOT_GIVEN,
        ftes: int | NotGiven = NOT_GIVEN,
        geo_admin_level1: str | NotGiven = NOT_GIVEN,
        geo_admin_level2: str | NotGiven = NOT_GIVEN,
        geo_admin_level3: str | NotGiven = NOT_GIVEN,
        mass_ranking: int | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        parent_org_id: str | NotGiven = NOT_GIVEN,
        postal_code: str | NotGiven = NOT_GIVEN,
        profit: float | NotGiven = NOT_GIVEN,
        revenue: float | NotGiven = NOT_GIVEN,
        revenue_ranking: int | NotGiven = NOT_GIVEN,
        risk_manager: str | NotGiven = NOT_GIVEN,
        services_notes: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Service operation to update an OrganizationDetails object.

        OrganizationDetails
        represent details of organizations such as a corporation, manufacturer,
        consortium, government, etc. An organization can have detail records from
        several sources. A specific role is required to perform this service operation.
        Please contact the UDL team for assistance.

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

          id_organization: Unique identifier of the parent organization.

          name: Organization details name.

          source: Source of the data.

          body_id: Unique identifier of the record, auto-generated by the system.

          address1: Street number of the organization.

          address2: Field for additional organization address information such as PO Box and unit
              number.

          address3: Contains the third line of address information for an organization.

          broker: Designated broker for this organization.

          ceo: For organizations of type CORPORATION, the name of the Chief Executive Officer.

          cfo: For organizations of type CORPORATION, the name of the Chief Financial Officer.

          cto: For organizations of type CORPORATION, the name of the Chief Technology Officer.

          description: Organization description.

          ebitda: For organizations of type CORPORATION, the company EBITDA value as of
              financialYearEndDate in US Dollars.

          email: Listed contact email address for the organization.

          financial_notes: For organizations of type CORPORATION, notes on company financials.

          financial_year_end_date: For organizations of type CORPORATION, the effective financial year end date for
              revenue, EBITDA, and profit values.

          fleet_plan_notes: Satellite fleet planning notes for this organization.

          former_org_id: Former organization ID (if this organization previously existed as another
              organization).

          ftes: Total number of FTEs in this organization.

          geo_admin_level1: Administrative boundaries of the first sub-national level. Level 1 is simply the
              largest demarcation under whatever demarcation criteria has been determined by
              the governing body. For example, this may be a state or province.

          geo_admin_level2: Administrative boundaries of the second sub-national level. Level 2 is simply
              the second largest demarcation under whatever demarcation criteria has been
              determined by the governing body. For example, this may be a county or district.

          geo_admin_level3: Administrative boundaries of the third sub-national level. Level 3 is simply the
              third largest demarcation under whatever demarcation criteria has been
              determined by the governing body. For example, this may be a city or township.

          mass_ranking: Mass ranking for this organization.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          parent_org_id: Parent organization ID of this organization if it is a child organization.

          postal_code: A postal code, such as PIN or ZIP Code, is a series of letters or digits or both
              included in the postal address of the organization.

          profit: For organizations of type CORPORATION, total annual profit as of
              financialYearEndDate in US Dollars.

          revenue: For organizations of type CORPORATION, total annual revenue as of
              financialYearEndDate in US Dollars.

          revenue_ranking: Revenue ranking for this organization.

          risk_manager: The name of the risk manager for the organization.

          services_notes: Notes on the services provided by the organization.

          tags: Optional array of provider/source specific tags for this data, where each
              element is no longer than 32 characters, used for implementing data owner
              conditional access controls to restrict access to the data. Should be left null
              by data providers unless conditional access controls are coordinated with the
              UDL team.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            f"/udl/organizationdetails/{path_id}",
            body=await async_maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "id_organization": id_organization,
                    "name": name,
                    "source": source,
                    "body_id": body_id,
                    "address1": address1,
                    "address2": address2,
                    "address3": address3,
                    "broker": broker,
                    "ceo": ceo,
                    "cfo": cfo,
                    "cto": cto,
                    "description": description,
                    "ebitda": ebitda,
                    "email": email,
                    "financial_notes": financial_notes,
                    "financial_year_end_date": financial_year_end_date,
                    "fleet_plan_notes": fleet_plan_notes,
                    "former_org_id": former_org_id,
                    "ftes": ftes,
                    "geo_admin_level1": geo_admin_level1,
                    "geo_admin_level2": geo_admin_level2,
                    "geo_admin_level3": geo_admin_level3,
                    "mass_ranking": mass_ranking,
                    "origin": origin,
                    "parent_org_id": parent_org_id,
                    "postal_code": postal_code,
                    "profit": profit,
                    "revenue": revenue,
                    "revenue_ranking": revenue_ranking,
                    "risk_manager": risk_manager,
                    "services_notes": services_notes,
                    "tags": tags,
                },
                organizationdetail_update_params.OrganizationdetailUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        *,
        name: str,
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[OrganizationdetailListResponse, AsyncOffsetPage[OrganizationdetailListResponse]]:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          name: Organization details name.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/organizationdetails",
            page=AsyncOffsetPage[OrganizationdetailListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "name": name,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    organizationdetail_list_params.OrganizationdetailListParams,
                ),
            ),
            model=OrganizationdetailListResponse,
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
        Service operation to delete an OrganizationDetails specified by the passed ID
        path parameter. OrganizationDetails represent details of organizations such as a
        corporation, manufacturer, consortium, government, etc. An organization can have
        detail records from several sources. A specific role is required to perform this
        service operation. Please contact the UDL team for assistance.

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
            f"/udl/organizationdetails/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def find_by_source(
        self,
        *,
        name: str,
        source: str,
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrganizationdetailFindBySourceResponse:
        """
        Service operation to get a single OrganizationDetails by a source passed as a
        query parameter. OrganizationDetails represent details of organizations such as
        a corporation, manufacturer, consortium, government, etc. An organization can
        have detail records from several sources.

        Args:
          name: Organization details name.

          source: The source of the OrganizationDetails records to find.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/udl/organizationdetails/findBySource",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "name": name,
                        "source": source,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    organizationdetail_find_by_source_params.OrganizationdetailFindBySourceParams,
                ),
            ),
            cast_to=OrganizationdetailFindBySourceResponse,
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
    ) -> OrganizationDetailsFull:
        """
        Service operation to get a single OrganizationDetails by its unique ID passed as
        a path parameter. OrganizationDetails represent details of organizations such as
        a corporation, manufacturer, consortium, government, etc. An organization can
        have detail records from several sources.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/udl/organizationdetails/{id}",
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
                    organizationdetail_get_params.OrganizationdetailGetParams,
                ),
            ),
            cast_to=OrganizationDetailsFull,
        )


class OrganizationdetailsResourceWithRawResponse:
    def __init__(self, organizationdetails: OrganizationdetailsResource) -> None:
        self._organizationdetails = organizationdetails

        self.create = to_raw_response_wrapper(
            organizationdetails.create,
        )
        self.update = to_raw_response_wrapper(
            organizationdetails.update,
        )
        self.list = to_raw_response_wrapper(
            organizationdetails.list,
        )
        self.delete = to_raw_response_wrapper(
            organizationdetails.delete,
        )
        self.find_by_source = to_raw_response_wrapper(
            organizationdetails.find_by_source,
        )
        self.get = to_raw_response_wrapper(
            organizationdetails.get,
        )


class AsyncOrganizationdetailsResourceWithRawResponse:
    def __init__(self, organizationdetails: AsyncOrganizationdetailsResource) -> None:
        self._organizationdetails = organizationdetails

        self.create = async_to_raw_response_wrapper(
            organizationdetails.create,
        )
        self.update = async_to_raw_response_wrapper(
            organizationdetails.update,
        )
        self.list = async_to_raw_response_wrapper(
            organizationdetails.list,
        )
        self.delete = async_to_raw_response_wrapper(
            organizationdetails.delete,
        )
        self.find_by_source = async_to_raw_response_wrapper(
            organizationdetails.find_by_source,
        )
        self.get = async_to_raw_response_wrapper(
            organizationdetails.get,
        )


class OrganizationdetailsResourceWithStreamingResponse:
    def __init__(self, organizationdetails: OrganizationdetailsResource) -> None:
        self._organizationdetails = organizationdetails

        self.create = to_streamed_response_wrapper(
            organizationdetails.create,
        )
        self.update = to_streamed_response_wrapper(
            organizationdetails.update,
        )
        self.list = to_streamed_response_wrapper(
            organizationdetails.list,
        )
        self.delete = to_streamed_response_wrapper(
            organizationdetails.delete,
        )
        self.find_by_source = to_streamed_response_wrapper(
            organizationdetails.find_by_source,
        )
        self.get = to_streamed_response_wrapper(
            organizationdetails.get,
        )


class AsyncOrganizationdetailsResourceWithStreamingResponse:
    def __init__(self, organizationdetails: AsyncOrganizationdetailsResource) -> None:
        self._organizationdetails = organizationdetails

        self.create = async_to_streamed_response_wrapper(
            organizationdetails.create,
        )
        self.update = async_to_streamed_response_wrapper(
            organizationdetails.update,
        )
        self.list = async_to_streamed_response_wrapper(
            organizationdetails.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            organizationdetails.delete,
        )
        self.find_by_source = async_to_streamed_response_wrapper(
            organizationdetails.find_by_source,
        )
        self.get = async_to_streamed_response_wrapper(
            organizationdetails.get,
        )
