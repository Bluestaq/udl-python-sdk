# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing_extensions import Literal

import httpx

from ..._files import read_file_content, async_read_file_content
from ..._types import (
    Body,
    Query,
    Headers,
    NoneType,
    NotGiven,
    BinaryTypes,
    FileContent,
    AsyncBinaryTypes,
    not_given,
)
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
from ...types.air_operations import crewpaper_unpublish_params, crewpaper_upload_pdf_params

__all__ = ["CrewpapersResource", "AsyncCrewpapersResource"]


class CrewpapersResource(SyncAPIResource):
    """
    These services provide operations for manipulating and querying Aircraft Sortie, Aircraft Mission, Item Tracking, Flight Plan, Air Event, Sortie Prior Permission Required (PPR), Diplomatic Clearance, Diplomatic Clearance Country, Airspace Control Order, Air Tasking Order, Navigational Obstruction, Logistics Support, Track Route, Air Load Plan, and Aviation Risk Management data. Aircraft Sortie information contains static and dynamic aircraft assignments, departure and arrival times, and remarks. Aircraft Mission information contains static data for mission planning to include assigned aircraft and crews, cargo pickup and dropoff locations, unique identifiers, and prioritization. Item Tracking information contains data for tracking an item from its origin to destination and how it may be configured during transport. Flight Plan information contains schedule and route details. Air Event provides information concerning various aerial events such as fuel transfer and air drops, as well as the associated aircraft involved. Sortie PPR information contains details on operational access to a runway, taxiway, or airport service. Diplomatic Clearance information contains details on the issuance and coordination of aircraft clearance requests. Diplomatic Clearance Country provides information such as entry/exit points, requirements, and points of contact for countries diplomatic clearances are being created for. Airspace Control Order provides information concerning the allocation, restriction, and deconfliction of airspace. Air Tasking Order information contains details on the coordination of air missions and their tasks, resources, and timelines. Navigational Obstruction provides the locations, characteristics, and boundaries of obstacles and structures that can restrict or interfere with navigation. Logistics Support contains information regarding the transport and maintenance of resources and equipment to sustain air operations. Track Route information defines specific flight paths used by aircraft during the transport of fuel and other resources. Air Load Plan information provides mission actuals concerning the loading and air transport of cargo and passengers. Aviation Risk Management information help aid in mission planning by accounting for factors such as mission complexity and crew fatigue.
    """

    @cached_property
    def with_raw_response(self) -> CrewpapersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return CrewpapersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CrewpapersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return CrewpapersResourceWithStreamingResponse(self)

    def unpublish(
        self,
        *,
        ids: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Service operation to remove supporting PDF from an aircraft sortie or sorties.

        A
        specific role is required to perform this service operation. Please contact the
        UDL team for assistance.

        Args:
          ids: Comma-separated list of AircraftSortie IDs where Crew Papers are unpublished.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/udl/crewpapers/unpublish",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"ids": ids}, crewpaper_unpublish_params.CrewpaperUnpublishParams),
            ),
            cast_to=NoneType,
        )

    def upload_pdf(
        self,
        file_content: FileContent | BinaryTypes,
        *,
        aircraft_sortie_ids: str,
        classification_marking: str,
        paper_status: Literal["PUBLISHED", "DELETED", "UPDATED", "READ"],
        papers_version: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Service operation to upload a supporting PDF for the aircraft sortie.

        A specific
        role is required to perform this service operation. Please contact the UDL team
        for assistance.

        Args:
          aircraft_sortie_ids: Comma-separated list of AircraftSortie IDs the Crew Papers are being added to.

          classification_marking: classificationMarking of the Crew Papers.

          paper_status: The status of the supporting document.

          papers_version: The version number of the crew paper.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers["Content-Type"] = "application/pdf"
        return self._post(
            "/filedrop/crewpapers",
            content=read_file_content(file_content) if isinstance(file_content, os.PathLike) else file_content,
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "aircraft_sortie_ids": aircraft_sortie_ids,
                        "classification_marking": classification_marking,
                        "paper_status": paper_status,
                        "papers_version": papers_version,
                    },
                    crewpaper_upload_pdf_params.CrewpaperUploadPdfParams,
                ),
            ),
            cast_to=NoneType,
        )


class AsyncCrewpapersResource(AsyncAPIResource):
    """
    These services provide operations for manipulating and querying Aircraft Sortie, Aircraft Mission, Item Tracking, Flight Plan, Air Event, Sortie Prior Permission Required (PPR), Diplomatic Clearance, Diplomatic Clearance Country, Airspace Control Order, Air Tasking Order, Navigational Obstruction, Logistics Support, Track Route, Air Load Plan, and Aviation Risk Management data. Aircraft Sortie information contains static and dynamic aircraft assignments, departure and arrival times, and remarks. Aircraft Mission information contains static data for mission planning to include assigned aircraft and crews, cargo pickup and dropoff locations, unique identifiers, and prioritization. Item Tracking information contains data for tracking an item from its origin to destination and how it may be configured during transport. Flight Plan information contains schedule and route details. Air Event provides information concerning various aerial events such as fuel transfer and air drops, as well as the associated aircraft involved. Sortie PPR information contains details on operational access to a runway, taxiway, or airport service. Diplomatic Clearance information contains details on the issuance and coordination of aircraft clearance requests. Diplomatic Clearance Country provides information such as entry/exit points, requirements, and points of contact for countries diplomatic clearances are being created for. Airspace Control Order provides information concerning the allocation, restriction, and deconfliction of airspace. Air Tasking Order information contains details on the coordination of air missions and their tasks, resources, and timelines. Navigational Obstruction provides the locations, characteristics, and boundaries of obstacles and structures that can restrict or interfere with navigation. Logistics Support contains information regarding the transport and maintenance of resources and equipment to sustain air operations. Track Route information defines specific flight paths used by aircraft during the transport of fuel and other resources. Air Load Plan information provides mission actuals concerning the loading and air transport of cargo and passengers. Aviation Risk Management information help aid in mission planning by accounting for factors such as mission complexity and crew fatigue.
    """

    @cached_property
    def with_raw_response(self) -> AsyncCrewpapersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncCrewpapersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCrewpapersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncCrewpapersResourceWithStreamingResponse(self)

    async def unpublish(
        self,
        *,
        ids: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Service operation to remove supporting PDF from an aircraft sortie or sorties.

        A
        specific role is required to perform this service operation. Please contact the
        UDL team for assistance.

        Args:
          ids: Comma-separated list of AircraftSortie IDs where Crew Papers are unpublished.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/udl/crewpapers/unpublish",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"ids": ids}, crewpaper_unpublish_params.CrewpaperUnpublishParams),
            ),
            cast_to=NoneType,
        )

    async def upload_pdf(
        self,
        file_content: FileContent | AsyncBinaryTypes,
        *,
        aircraft_sortie_ids: str,
        classification_marking: str,
        paper_status: Literal["PUBLISHED", "DELETED", "UPDATED", "READ"],
        papers_version: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Service operation to upload a supporting PDF for the aircraft sortie.

        A specific
        role is required to perform this service operation. Please contact the UDL team
        for assistance.

        Args:
          aircraft_sortie_ids: Comma-separated list of AircraftSortie IDs the Crew Papers are being added to.

          classification_marking: classificationMarking of the Crew Papers.

          paper_status: The status of the supporting document.

          papers_version: The version number of the crew paper.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers["Content-Type"] = "application/pdf"
        return await self._post(
            "/filedrop/crewpapers",
            content=await async_read_file_content(file_content)
            if isinstance(file_content, os.PathLike)
            else file_content,
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "aircraft_sortie_ids": aircraft_sortie_ids,
                        "classification_marking": classification_marking,
                        "paper_status": paper_status,
                        "papers_version": papers_version,
                    },
                    crewpaper_upload_pdf_params.CrewpaperUploadPdfParams,
                ),
            ),
            cast_to=NoneType,
        )


class CrewpapersResourceWithRawResponse:
    def __init__(self, crewpapers: CrewpapersResource) -> None:
        self._crewpapers = crewpapers

        self.unpublish = to_raw_response_wrapper(
            crewpapers.unpublish,
        )
        self.upload_pdf = to_raw_response_wrapper(
            crewpapers.upload_pdf,
        )


class AsyncCrewpapersResourceWithRawResponse:
    def __init__(self, crewpapers: AsyncCrewpapersResource) -> None:
        self._crewpapers = crewpapers

        self.unpublish = async_to_raw_response_wrapper(
            crewpapers.unpublish,
        )
        self.upload_pdf = async_to_raw_response_wrapper(
            crewpapers.upload_pdf,
        )


class CrewpapersResourceWithStreamingResponse:
    def __init__(self, crewpapers: CrewpapersResource) -> None:
        self._crewpapers = crewpapers

        self.unpublish = to_streamed_response_wrapper(
            crewpapers.unpublish,
        )
        self.upload_pdf = to_streamed_response_wrapper(
            crewpapers.upload_pdf,
        )


class AsyncCrewpapersResourceWithStreamingResponse:
    def __init__(self, crewpapers: AsyncCrewpapersResource) -> None:
        self._crewpapers = crewpapers

        self.unpublish = async_to_streamed_response_wrapper(
            crewpapers.unpublish,
        )
        self.upload_pdf = async_to_streamed_response_wrapper(
            crewpapers.upload_pdf,
        )
