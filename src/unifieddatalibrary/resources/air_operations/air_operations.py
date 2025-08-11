# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from .crewpapers import (
    CrewpapersResource,
    AsyncCrewpapersResource,
    CrewpapersResourceWithRawResponse,
    AsyncCrewpapersResourceWithRawResponse,
    CrewpapersResourceWithStreamingResponse,
    AsyncCrewpapersResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from .aircraft_sorties import (
    AircraftSortiesResource,
    AsyncAircraftSortiesResource,
    AircraftSortiesResourceWithRawResponse,
    AsyncAircraftSortiesResourceWithRawResponse,
    AircraftSortiesResourceWithStreamingResponse,
    AsyncAircraftSortiesResourceWithStreamingResponse,
)
from .air_tasking_orders import (
    AirTaskingOrdersResource,
    AsyncAirTaskingOrdersResource,
    AirTaskingOrdersResourceWithRawResponse,
    AsyncAirTaskingOrdersResourceWithRawResponse,
    AirTaskingOrdersResourceWithStreamingResponse,
    AsyncAirTaskingOrdersResourceWithStreamingResponse,
)
from .diplomatic_clearance import (
    DiplomaticClearanceResource,
    AsyncDiplomaticClearanceResource,
    DiplomaticClearanceResourceWithRawResponse,
    AsyncDiplomaticClearanceResourceWithRawResponse,
    DiplomaticClearanceResourceWithStreamingResponse,
    AsyncDiplomaticClearanceResourceWithStreamingResponse,
)
from .airspace_control_orders import (
    AirspaceControlOrdersResource,
    AsyncAirspaceControlOrdersResource,
    AirspaceControlOrdersResourceWithRawResponse,
    AsyncAirspaceControlOrdersResourceWithRawResponse,
    AirspaceControlOrdersResourceWithStreamingResponse,
    AsyncAirspaceControlOrdersResourceWithStreamingResponse,
)

__all__ = ["AirOperationsResource", "AsyncAirOperationsResource"]


class AirOperationsResource(SyncAPIResource):
    @cached_property
    def air_tasking_orders(self) -> AirTaskingOrdersResource:
        return AirTaskingOrdersResource(self._client)

    @cached_property
    def aircraft_sorties(self) -> AircraftSortiesResource:
        return AircraftSortiesResource(self._client)

    @cached_property
    def airspace_control_orders(self) -> AirspaceControlOrdersResource:
        return AirspaceControlOrdersResource(self._client)

    @cached_property
    def crewpapers(self) -> CrewpapersResource:
        return CrewpapersResource(self._client)

    @cached_property
    def diplomatic_clearance(self) -> DiplomaticClearanceResource:
        return DiplomaticClearanceResource(self._client)

    @cached_property
    def with_raw_response(self) -> AirOperationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AirOperationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AirOperationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AirOperationsResourceWithStreamingResponse(self)


class AsyncAirOperationsResource(AsyncAPIResource):
    @cached_property
    def air_tasking_orders(self) -> AsyncAirTaskingOrdersResource:
        return AsyncAirTaskingOrdersResource(self._client)

    @cached_property
    def aircraft_sorties(self) -> AsyncAircraftSortiesResource:
        return AsyncAircraftSortiesResource(self._client)

    @cached_property
    def airspace_control_orders(self) -> AsyncAirspaceControlOrdersResource:
        return AsyncAirspaceControlOrdersResource(self._client)

    @cached_property
    def crewpapers(self) -> AsyncCrewpapersResource:
        return AsyncCrewpapersResource(self._client)

    @cached_property
    def diplomatic_clearance(self) -> AsyncDiplomaticClearanceResource:
        return AsyncDiplomaticClearanceResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAirOperationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncAirOperationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAirOperationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncAirOperationsResourceWithStreamingResponse(self)


class AirOperationsResourceWithRawResponse:
    def __init__(self, air_operations: AirOperationsResource) -> None:
        self._air_operations = air_operations

    @cached_property
    def air_tasking_orders(self) -> AirTaskingOrdersResourceWithRawResponse:
        return AirTaskingOrdersResourceWithRawResponse(self._air_operations.air_tasking_orders)

    @cached_property
    def aircraft_sorties(self) -> AircraftSortiesResourceWithRawResponse:
        return AircraftSortiesResourceWithRawResponse(self._air_operations.aircraft_sorties)

    @cached_property
    def airspace_control_orders(self) -> AirspaceControlOrdersResourceWithRawResponse:
        return AirspaceControlOrdersResourceWithRawResponse(self._air_operations.airspace_control_orders)

    @cached_property
    def crewpapers(self) -> CrewpapersResourceWithRawResponse:
        return CrewpapersResourceWithRawResponse(self._air_operations.crewpapers)

    @cached_property
    def diplomatic_clearance(self) -> DiplomaticClearanceResourceWithRawResponse:
        return DiplomaticClearanceResourceWithRawResponse(self._air_operations.diplomatic_clearance)


class AsyncAirOperationsResourceWithRawResponse:
    def __init__(self, air_operations: AsyncAirOperationsResource) -> None:
        self._air_operations = air_operations

    @cached_property
    def air_tasking_orders(self) -> AsyncAirTaskingOrdersResourceWithRawResponse:
        return AsyncAirTaskingOrdersResourceWithRawResponse(self._air_operations.air_tasking_orders)

    @cached_property
    def aircraft_sorties(self) -> AsyncAircraftSortiesResourceWithRawResponse:
        return AsyncAircraftSortiesResourceWithRawResponse(self._air_operations.aircraft_sorties)

    @cached_property
    def airspace_control_orders(self) -> AsyncAirspaceControlOrdersResourceWithRawResponse:
        return AsyncAirspaceControlOrdersResourceWithRawResponse(self._air_operations.airspace_control_orders)

    @cached_property
    def crewpapers(self) -> AsyncCrewpapersResourceWithRawResponse:
        return AsyncCrewpapersResourceWithRawResponse(self._air_operations.crewpapers)

    @cached_property
    def diplomatic_clearance(self) -> AsyncDiplomaticClearanceResourceWithRawResponse:
        return AsyncDiplomaticClearanceResourceWithRawResponse(self._air_operations.diplomatic_clearance)


class AirOperationsResourceWithStreamingResponse:
    def __init__(self, air_operations: AirOperationsResource) -> None:
        self._air_operations = air_operations

    @cached_property
    def air_tasking_orders(self) -> AirTaskingOrdersResourceWithStreamingResponse:
        return AirTaskingOrdersResourceWithStreamingResponse(self._air_operations.air_tasking_orders)

    @cached_property
    def aircraft_sorties(self) -> AircraftSortiesResourceWithStreamingResponse:
        return AircraftSortiesResourceWithStreamingResponse(self._air_operations.aircraft_sorties)

    @cached_property
    def airspace_control_orders(self) -> AirspaceControlOrdersResourceWithStreamingResponse:
        return AirspaceControlOrdersResourceWithStreamingResponse(self._air_operations.airspace_control_orders)

    @cached_property
    def crewpapers(self) -> CrewpapersResourceWithStreamingResponse:
        return CrewpapersResourceWithStreamingResponse(self._air_operations.crewpapers)

    @cached_property
    def diplomatic_clearance(self) -> DiplomaticClearanceResourceWithStreamingResponse:
        return DiplomaticClearanceResourceWithStreamingResponse(self._air_operations.diplomatic_clearance)


class AsyncAirOperationsResourceWithStreamingResponse:
    def __init__(self, air_operations: AsyncAirOperationsResource) -> None:
        self._air_operations = air_operations

    @cached_property
    def air_tasking_orders(self) -> AsyncAirTaskingOrdersResourceWithStreamingResponse:
        return AsyncAirTaskingOrdersResourceWithStreamingResponse(self._air_operations.air_tasking_orders)

    @cached_property
    def aircraft_sorties(self) -> AsyncAircraftSortiesResourceWithStreamingResponse:
        return AsyncAircraftSortiesResourceWithStreamingResponse(self._air_operations.aircraft_sorties)

    @cached_property
    def airspace_control_orders(self) -> AsyncAirspaceControlOrdersResourceWithStreamingResponse:
        return AsyncAirspaceControlOrdersResourceWithStreamingResponse(self._air_operations.airspace_control_orders)

    @cached_property
    def crewpapers(self) -> AsyncCrewpapersResourceWithStreamingResponse:
        return AsyncCrewpapersResourceWithStreamingResponse(self._air_operations.crewpapers)

    @cached_property
    def diplomatic_clearance(self) -> AsyncDiplomaticClearanceResourceWithStreamingResponse:
        return AsyncDiplomaticClearanceResourceWithStreamingResponse(self._air_operations.diplomatic_clearance)
