# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import (
    onorbitevent_get_params,
    onorbitevent_list_params,
    onorbitevent_count_params,
    onorbitevent_tuple_params,
    onorbitevent_create_params,
    onorbitevent_update_params,
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
from ..types.onorbitevent_get_response import OnorbiteventGetResponse
from ..types.onorbitevent_list_response import OnorbiteventListResponse
from ..types.onorbitevent_tuple_response import OnorbiteventTupleResponse

__all__ = ["OnorbiteventResource", "AsyncOnorbiteventResource"]


class OnorbiteventResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OnorbiteventResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return OnorbiteventResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OnorbiteventResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return OnorbiteventResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        event_time: Union[str, datetime],
        source: str,
        id: str | NotGiven = NOT_GIVEN,
        achieved_flight_phase: str | NotGiven = NOT_GIVEN,
        age_at_event: float | NotGiven = NOT_GIVEN,
        capability_loss: float | NotGiven = NOT_GIVEN,
        capability_loss_notes: str | NotGiven = NOT_GIVEN,
        capacity_loss: float | NotGiven = NOT_GIVEN,
        consequential_equipment_failure: str | NotGiven = NOT_GIVEN,
        declassification_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        declassification_string: str | NotGiven = NOT_GIVEN,
        derived_from: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        equipment_at_fault: str | NotGiven = NOT_GIVEN,
        equipment_causing_loss_notes: str | NotGiven = NOT_GIVEN,
        equipment_part_at_fault: str | NotGiven = NOT_GIVEN,
        equipment_type_at_fault: str | NotGiven = NOT_GIVEN,
        event_result: str | NotGiven = NOT_GIVEN,
        event_time_notes: str | NotGiven = NOT_GIVEN,
        event_type: str | NotGiven = NOT_GIVEN,
        geo_position: float | NotGiven = NOT_GIVEN,
        id_on_orbit: str | NotGiven = NOT_GIVEN,
        inclined: bool | NotGiven = NOT_GIVEN,
        injured: int | NotGiven = NOT_GIVEN,
        insurance_carried_notes: str | NotGiven = NOT_GIVEN,
        insurance_loss: float | NotGiven = NOT_GIVEN,
        insurance_loss_notes: str | NotGiven = NOT_GIVEN,
        killed: int | NotGiven = NOT_GIVEN,
        lessee_org_id: str | NotGiven = NOT_GIVEN,
        life_lost: float | NotGiven = NOT_GIVEN,
        net_amount: float | NotGiven = NOT_GIVEN,
        object_status: str | NotGiven = NOT_GIVEN,
        occurrence_flight_phase: str | NotGiven = NOT_GIVEN,
        official_loss_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        operated_on_behalf_of_org_id: str | NotGiven = NOT_GIVEN,
        operator_org_id: str | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        orig_object_id: str | NotGiven = NOT_GIVEN,
        owner_org_id: str | NotGiven = NOT_GIVEN,
        plane_number: str | NotGiven = NOT_GIVEN,
        plane_slot: str | NotGiven = NOT_GIVEN,
        position_status: str | NotGiven = NOT_GIVEN,
        remarks: str | NotGiven = NOT_GIVEN,
        satellite_position: str | NotGiven = NOT_GIVEN,
        sat_no: int | NotGiven = NOT_GIVEN,
        stage_at_fault: str | NotGiven = NOT_GIVEN,
        third_party_insurance_loss: float | NotGiven = NOT_GIVEN,
        underlying_cause: str | NotGiven = NOT_GIVEN,
        until_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single OnorbitEvent as a POST body and ingest into
        the database. An OnorbitEvent is an event associated with a particular on-orbit
        spacecraft including insurance related losses, anomalies and incidents. A
        specific role is required to perform this service operation. Please contact the
        UDL team for assistance.

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

          event_time: Date/Time of the event. See eventTimeNotes for remarks on the accuracy of the
              date time.

          source: Source of the data.

          id: Unique identifier of the record, auto-generated by the system.

          achieved_flight_phase: Achieved phase of flight prior to the event.

          age_at_event: Spacecraft age at the event in years.

          capability_loss: Spacecraft capability loss incurred, as a fraction of 1.

          capability_loss_notes: Notes on capability loss at the time of event.

          capacity_loss: Spacecraft capacity loss incurred, as a fraction of 1.

          consequential_equipment_failure: Additional equipment which failed as a result of faulty equipment on the
              spacecraft during the event.

          declassification_date: The declassification date of this data, in ISO 8601 UTC format.

          declassification_string: Declassification string of this data.

          derived_from: The sources or SCG references from which the classification of this data is
              derived.

          description: Notes/description of the event.

          equipment_at_fault: Equipment on the spacecraft which caused the event.

          equipment_causing_loss_notes: Additional notes on the equipment causing the event/loss.

          equipment_part_at_fault: Specific part of the equipment on the spacecraft which caused the event.

          equipment_type_at_fault: Type of the equipment on the spacecraft which caused the event.

          event_result: The result of the reported event.

          event_time_notes: Notes/remarks on the validity/accuracy of the eventTime.

          event_type: The type of on-orbit event being reported.

          geo_position: GEO position longitude at event time if applicable. Negative values are west.

          id_on_orbit: Unique identifier of the on-orbit object for this event.

          inclined: Boolean indicating if the spacecraft is inclined.

          injured: Number of humans injured in the event.

          insurance_carried_notes: Additional insurance notes on coverages at the time of event.

          insurance_loss: Insurance loss incurred, as a fraction of 1.

          insurance_loss_notes: Additional insurance notes if the event is an official loss.

          killed: Number of humans killed in the event.

          lessee_org_id: Unique identifier of the organization which leases this on-orbit spacecraft.

          life_lost: Spacecraft life lost due to the event as a percent/fraction of 1.

          net_amount: Net amount of the insurance claim for the event, in USD.

          object_status: The status of the on-orbit object.

          occurrence_flight_phase: Phase of flight during which the event occurred.

          official_loss_date: Date time of official loss of the spacecraft.

          operated_on_behalf_of_org_id: Unique identifier of the organization on whose behalf the on-orbit spacecraft is
              operated.

          operator_org_id: Organization ID of the operator of the on-orbit spacecraft at the time of the
              event.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          orig_object_id: Original object ID or Catalog Number provided by source (may not map to an
              existing idOnOrbit in UDL).

          owner_org_id: Organization ID of the owner of the on-orbit spacecraft at the time of the
              event.

          plane_number: GEO slot plane number/designator of the spacecraft at event time.

          plane_slot: GEO plane slot of the spacecraft at event time.

          position_status: Position status of the spacecraft at event time (e.g. Stable, Drifting/Tumbling,
              etc).

          remarks: Additional remarks on the event description.

          satellite_position: Description of the satellite orbital position or regime.

          sat_no: Satellite/Catalog number of the target on-orbit object.

          stage_at_fault: Faulty stage of flight for the event.

          third_party_insurance_loss: Insurance loss incurred by 3rd party insurance, in USD.

          underlying_cause: Underlying cause of the event.

          until_time: Maximum validity time of the event.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/udl/onorbitevent",
            body=maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "event_time": event_time,
                    "source": source,
                    "id": id,
                    "achieved_flight_phase": achieved_flight_phase,
                    "age_at_event": age_at_event,
                    "capability_loss": capability_loss,
                    "capability_loss_notes": capability_loss_notes,
                    "capacity_loss": capacity_loss,
                    "consequential_equipment_failure": consequential_equipment_failure,
                    "declassification_date": declassification_date,
                    "declassification_string": declassification_string,
                    "derived_from": derived_from,
                    "description": description,
                    "equipment_at_fault": equipment_at_fault,
                    "equipment_causing_loss_notes": equipment_causing_loss_notes,
                    "equipment_part_at_fault": equipment_part_at_fault,
                    "equipment_type_at_fault": equipment_type_at_fault,
                    "event_result": event_result,
                    "event_time_notes": event_time_notes,
                    "event_type": event_type,
                    "geo_position": geo_position,
                    "id_on_orbit": id_on_orbit,
                    "inclined": inclined,
                    "injured": injured,
                    "insurance_carried_notes": insurance_carried_notes,
                    "insurance_loss": insurance_loss,
                    "insurance_loss_notes": insurance_loss_notes,
                    "killed": killed,
                    "lessee_org_id": lessee_org_id,
                    "life_lost": life_lost,
                    "net_amount": net_amount,
                    "object_status": object_status,
                    "occurrence_flight_phase": occurrence_flight_phase,
                    "official_loss_date": official_loss_date,
                    "operated_on_behalf_of_org_id": operated_on_behalf_of_org_id,
                    "operator_org_id": operator_org_id,
                    "origin": origin,
                    "orig_object_id": orig_object_id,
                    "owner_org_id": owner_org_id,
                    "plane_number": plane_number,
                    "plane_slot": plane_slot,
                    "position_status": position_status,
                    "remarks": remarks,
                    "satellite_position": satellite_position,
                    "sat_no": sat_no,
                    "stage_at_fault": stage_at_fault,
                    "third_party_insurance_loss": third_party_insurance_loss,
                    "underlying_cause": underlying_cause,
                    "until_time": until_time,
                },
                onorbitevent_create_params.OnorbiteventCreateParams,
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
        event_time: Union[str, datetime],
        source: str,
        body_id: str | NotGiven = NOT_GIVEN,
        achieved_flight_phase: str | NotGiven = NOT_GIVEN,
        age_at_event: float | NotGiven = NOT_GIVEN,
        capability_loss: float | NotGiven = NOT_GIVEN,
        capability_loss_notes: str | NotGiven = NOT_GIVEN,
        capacity_loss: float | NotGiven = NOT_GIVEN,
        consequential_equipment_failure: str | NotGiven = NOT_GIVEN,
        declassification_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        declassification_string: str | NotGiven = NOT_GIVEN,
        derived_from: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        equipment_at_fault: str | NotGiven = NOT_GIVEN,
        equipment_causing_loss_notes: str | NotGiven = NOT_GIVEN,
        equipment_part_at_fault: str | NotGiven = NOT_GIVEN,
        equipment_type_at_fault: str | NotGiven = NOT_GIVEN,
        event_result: str | NotGiven = NOT_GIVEN,
        event_time_notes: str | NotGiven = NOT_GIVEN,
        event_type: str | NotGiven = NOT_GIVEN,
        geo_position: float | NotGiven = NOT_GIVEN,
        id_on_orbit: str | NotGiven = NOT_GIVEN,
        inclined: bool | NotGiven = NOT_GIVEN,
        injured: int | NotGiven = NOT_GIVEN,
        insurance_carried_notes: str | NotGiven = NOT_GIVEN,
        insurance_loss: float | NotGiven = NOT_GIVEN,
        insurance_loss_notes: str | NotGiven = NOT_GIVEN,
        killed: int | NotGiven = NOT_GIVEN,
        lessee_org_id: str | NotGiven = NOT_GIVEN,
        life_lost: float | NotGiven = NOT_GIVEN,
        net_amount: float | NotGiven = NOT_GIVEN,
        object_status: str | NotGiven = NOT_GIVEN,
        occurrence_flight_phase: str | NotGiven = NOT_GIVEN,
        official_loss_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        operated_on_behalf_of_org_id: str | NotGiven = NOT_GIVEN,
        operator_org_id: str | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        orig_object_id: str | NotGiven = NOT_GIVEN,
        owner_org_id: str | NotGiven = NOT_GIVEN,
        plane_number: str | NotGiven = NOT_GIVEN,
        plane_slot: str | NotGiven = NOT_GIVEN,
        position_status: str | NotGiven = NOT_GIVEN,
        remarks: str | NotGiven = NOT_GIVEN,
        satellite_position: str | NotGiven = NOT_GIVEN,
        sat_no: int | NotGiven = NOT_GIVEN,
        stage_at_fault: str | NotGiven = NOT_GIVEN,
        third_party_insurance_loss: float | NotGiven = NOT_GIVEN,
        underlying_cause: str | NotGiven = NOT_GIVEN,
        until_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Service operation to update a single OnorbitEvent.

        An OnorbitEvent is an event
        associated with a particular on-orbit spacecraft including insurance related
        losses, anomalies and incidents. A specific role is required to perform this
        service operation. Please contact the UDL team for assistance.

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

          event_time: Date/Time of the event. See eventTimeNotes for remarks on the accuracy of the
              date time.

          source: Source of the data.

          body_id: Unique identifier of the record, auto-generated by the system.

          achieved_flight_phase: Achieved phase of flight prior to the event.

          age_at_event: Spacecraft age at the event in years.

          capability_loss: Spacecraft capability loss incurred, as a fraction of 1.

          capability_loss_notes: Notes on capability loss at the time of event.

          capacity_loss: Spacecraft capacity loss incurred, as a fraction of 1.

          consequential_equipment_failure: Additional equipment which failed as a result of faulty equipment on the
              spacecraft during the event.

          declassification_date: The declassification date of this data, in ISO 8601 UTC format.

          declassification_string: Declassification string of this data.

          derived_from: The sources or SCG references from which the classification of this data is
              derived.

          description: Notes/description of the event.

          equipment_at_fault: Equipment on the spacecraft which caused the event.

          equipment_causing_loss_notes: Additional notes on the equipment causing the event/loss.

          equipment_part_at_fault: Specific part of the equipment on the spacecraft which caused the event.

          equipment_type_at_fault: Type of the equipment on the spacecraft which caused the event.

          event_result: The result of the reported event.

          event_time_notes: Notes/remarks on the validity/accuracy of the eventTime.

          event_type: The type of on-orbit event being reported.

          geo_position: GEO position longitude at event time if applicable. Negative values are west.

          id_on_orbit: Unique identifier of the on-orbit object for this event.

          inclined: Boolean indicating if the spacecraft is inclined.

          injured: Number of humans injured in the event.

          insurance_carried_notes: Additional insurance notes on coverages at the time of event.

          insurance_loss: Insurance loss incurred, as a fraction of 1.

          insurance_loss_notes: Additional insurance notes if the event is an official loss.

          killed: Number of humans killed in the event.

          lessee_org_id: Unique identifier of the organization which leases this on-orbit spacecraft.

          life_lost: Spacecraft life lost due to the event as a percent/fraction of 1.

          net_amount: Net amount of the insurance claim for the event, in USD.

          object_status: The status of the on-orbit object.

          occurrence_flight_phase: Phase of flight during which the event occurred.

          official_loss_date: Date time of official loss of the spacecraft.

          operated_on_behalf_of_org_id: Unique identifier of the organization on whose behalf the on-orbit spacecraft is
              operated.

          operator_org_id: Organization ID of the operator of the on-orbit spacecraft at the time of the
              event.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          orig_object_id: Original object ID or Catalog Number provided by source (may not map to an
              existing idOnOrbit in UDL).

          owner_org_id: Organization ID of the owner of the on-orbit spacecraft at the time of the
              event.

          plane_number: GEO slot plane number/designator of the spacecraft at event time.

          plane_slot: GEO plane slot of the spacecraft at event time.

          position_status: Position status of the spacecraft at event time (e.g. Stable, Drifting/Tumbling,
              etc).

          remarks: Additional remarks on the event description.

          satellite_position: Description of the satellite orbital position or regime.

          sat_no: Satellite/Catalog number of the target on-orbit object.

          stage_at_fault: Faulty stage of flight for the event.

          third_party_insurance_loss: Insurance loss incurred by 3rd party insurance, in USD.

          underlying_cause: Underlying cause of the event.

          until_time: Maximum validity time of the event.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            f"/udl/onorbitevent/{path_id}",
            body=maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "event_time": event_time,
                    "source": source,
                    "body_id": body_id,
                    "achieved_flight_phase": achieved_flight_phase,
                    "age_at_event": age_at_event,
                    "capability_loss": capability_loss,
                    "capability_loss_notes": capability_loss_notes,
                    "capacity_loss": capacity_loss,
                    "consequential_equipment_failure": consequential_equipment_failure,
                    "declassification_date": declassification_date,
                    "declassification_string": declassification_string,
                    "derived_from": derived_from,
                    "description": description,
                    "equipment_at_fault": equipment_at_fault,
                    "equipment_causing_loss_notes": equipment_causing_loss_notes,
                    "equipment_part_at_fault": equipment_part_at_fault,
                    "equipment_type_at_fault": equipment_type_at_fault,
                    "event_result": event_result,
                    "event_time_notes": event_time_notes,
                    "event_type": event_type,
                    "geo_position": geo_position,
                    "id_on_orbit": id_on_orbit,
                    "inclined": inclined,
                    "injured": injured,
                    "insurance_carried_notes": insurance_carried_notes,
                    "insurance_loss": insurance_loss,
                    "insurance_loss_notes": insurance_loss_notes,
                    "killed": killed,
                    "lessee_org_id": lessee_org_id,
                    "life_lost": life_lost,
                    "net_amount": net_amount,
                    "object_status": object_status,
                    "occurrence_flight_phase": occurrence_flight_phase,
                    "official_loss_date": official_loss_date,
                    "operated_on_behalf_of_org_id": operated_on_behalf_of_org_id,
                    "operator_org_id": operator_org_id,
                    "origin": origin,
                    "orig_object_id": orig_object_id,
                    "owner_org_id": owner_org_id,
                    "plane_number": plane_number,
                    "plane_slot": plane_slot,
                    "position_status": position_status,
                    "remarks": remarks,
                    "satellite_position": satellite_position,
                    "sat_no": sat_no,
                    "stage_at_fault": stage_at_fault,
                    "third_party_insurance_loss": third_party_insurance_loss,
                    "underlying_cause": underlying_cause,
                    "until_time": until_time,
                },
                onorbitevent_update_params.OnorbiteventUpdateParams,
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
    ) -> SyncOffsetPage[OnorbiteventListResponse]:
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
            "/udl/onorbitevent",
            page=SyncOffsetPage[OnorbiteventListResponse],
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
                    onorbitevent_list_params.OnorbiteventListParams,
                ),
            ),
            model=OnorbiteventListResponse,
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
        Service operation to delete a OnorbitEvent object specified by the passed ID
        path parameter. An OnorbitEvent is an event associated with a particular
        on-orbit spacecraft including insurance related losses, anomalies and incidents.
        A specific role is required to perform this service operation. Please contact
        the UDL team for assistance.

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
            f"/udl/onorbitevent/{id}",
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
            "/udl/onorbitevent/count",
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
                    onorbitevent_count_params.OnorbiteventCountParams,
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
    ) -> OnorbiteventGetResponse:
        """
        Service operation to get a single OnorbitEvent record by its unique ID passed as
        a path parameter. An OnorbitEvent is an event associated with a particular
        on-orbit spacecraft including insurance related losses, anomalies and incidents.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/udl/onorbitevent/{id}",
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
                    onorbitevent_get_params.OnorbiteventGetParams,
                ),
            ),
            cast_to=OnorbiteventGetResponse,
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
            "/udl/onorbitevent/queryhelp",
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
    ) -> OnorbiteventTupleResponse:
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
            "/udl/onorbitevent/tuple",
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
                    onorbitevent_tuple_params.OnorbiteventTupleParams,
                ),
            ),
            cast_to=OnorbiteventTupleResponse,
        )


class AsyncOnorbiteventResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOnorbiteventResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncOnorbiteventResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOnorbiteventResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncOnorbiteventResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        event_time: Union[str, datetime],
        source: str,
        id: str | NotGiven = NOT_GIVEN,
        achieved_flight_phase: str | NotGiven = NOT_GIVEN,
        age_at_event: float | NotGiven = NOT_GIVEN,
        capability_loss: float | NotGiven = NOT_GIVEN,
        capability_loss_notes: str | NotGiven = NOT_GIVEN,
        capacity_loss: float | NotGiven = NOT_GIVEN,
        consequential_equipment_failure: str | NotGiven = NOT_GIVEN,
        declassification_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        declassification_string: str | NotGiven = NOT_GIVEN,
        derived_from: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        equipment_at_fault: str | NotGiven = NOT_GIVEN,
        equipment_causing_loss_notes: str | NotGiven = NOT_GIVEN,
        equipment_part_at_fault: str | NotGiven = NOT_GIVEN,
        equipment_type_at_fault: str | NotGiven = NOT_GIVEN,
        event_result: str | NotGiven = NOT_GIVEN,
        event_time_notes: str | NotGiven = NOT_GIVEN,
        event_type: str | NotGiven = NOT_GIVEN,
        geo_position: float | NotGiven = NOT_GIVEN,
        id_on_orbit: str | NotGiven = NOT_GIVEN,
        inclined: bool | NotGiven = NOT_GIVEN,
        injured: int | NotGiven = NOT_GIVEN,
        insurance_carried_notes: str | NotGiven = NOT_GIVEN,
        insurance_loss: float | NotGiven = NOT_GIVEN,
        insurance_loss_notes: str | NotGiven = NOT_GIVEN,
        killed: int | NotGiven = NOT_GIVEN,
        lessee_org_id: str | NotGiven = NOT_GIVEN,
        life_lost: float | NotGiven = NOT_GIVEN,
        net_amount: float | NotGiven = NOT_GIVEN,
        object_status: str | NotGiven = NOT_GIVEN,
        occurrence_flight_phase: str | NotGiven = NOT_GIVEN,
        official_loss_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        operated_on_behalf_of_org_id: str | NotGiven = NOT_GIVEN,
        operator_org_id: str | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        orig_object_id: str | NotGiven = NOT_GIVEN,
        owner_org_id: str | NotGiven = NOT_GIVEN,
        plane_number: str | NotGiven = NOT_GIVEN,
        plane_slot: str | NotGiven = NOT_GIVEN,
        position_status: str | NotGiven = NOT_GIVEN,
        remarks: str | NotGiven = NOT_GIVEN,
        satellite_position: str | NotGiven = NOT_GIVEN,
        sat_no: int | NotGiven = NOT_GIVEN,
        stage_at_fault: str | NotGiven = NOT_GIVEN,
        third_party_insurance_loss: float | NotGiven = NOT_GIVEN,
        underlying_cause: str | NotGiven = NOT_GIVEN,
        until_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single OnorbitEvent as a POST body and ingest into
        the database. An OnorbitEvent is an event associated with a particular on-orbit
        spacecraft including insurance related losses, anomalies and incidents. A
        specific role is required to perform this service operation. Please contact the
        UDL team for assistance.

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

          event_time: Date/Time of the event. See eventTimeNotes for remarks on the accuracy of the
              date time.

          source: Source of the data.

          id: Unique identifier of the record, auto-generated by the system.

          achieved_flight_phase: Achieved phase of flight prior to the event.

          age_at_event: Spacecraft age at the event in years.

          capability_loss: Spacecraft capability loss incurred, as a fraction of 1.

          capability_loss_notes: Notes on capability loss at the time of event.

          capacity_loss: Spacecraft capacity loss incurred, as a fraction of 1.

          consequential_equipment_failure: Additional equipment which failed as a result of faulty equipment on the
              spacecraft during the event.

          declassification_date: The declassification date of this data, in ISO 8601 UTC format.

          declassification_string: Declassification string of this data.

          derived_from: The sources or SCG references from which the classification of this data is
              derived.

          description: Notes/description of the event.

          equipment_at_fault: Equipment on the spacecraft which caused the event.

          equipment_causing_loss_notes: Additional notes on the equipment causing the event/loss.

          equipment_part_at_fault: Specific part of the equipment on the spacecraft which caused the event.

          equipment_type_at_fault: Type of the equipment on the spacecraft which caused the event.

          event_result: The result of the reported event.

          event_time_notes: Notes/remarks on the validity/accuracy of the eventTime.

          event_type: The type of on-orbit event being reported.

          geo_position: GEO position longitude at event time if applicable. Negative values are west.

          id_on_orbit: Unique identifier of the on-orbit object for this event.

          inclined: Boolean indicating if the spacecraft is inclined.

          injured: Number of humans injured in the event.

          insurance_carried_notes: Additional insurance notes on coverages at the time of event.

          insurance_loss: Insurance loss incurred, as a fraction of 1.

          insurance_loss_notes: Additional insurance notes if the event is an official loss.

          killed: Number of humans killed in the event.

          lessee_org_id: Unique identifier of the organization which leases this on-orbit spacecraft.

          life_lost: Spacecraft life lost due to the event as a percent/fraction of 1.

          net_amount: Net amount of the insurance claim for the event, in USD.

          object_status: The status of the on-orbit object.

          occurrence_flight_phase: Phase of flight during which the event occurred.

          official_loss_date: Date time of official loss of the spacecraft.

          operated_on_behalf_of_org_id: Unique identifier of the organization on whose behalf the on-orbit spacecraft is
              operated.

          operator_org_id: Organization ID of the operator of the on-orbit spacecraft at the time of the
              event.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          orig_object_id: Original object ID or Catalog Number provided by source (may not map to an
              existing idOnOrbit in UDL).

          owner_org_id: Organization ID of the owner of the on-orbit spacecraft at the time of the
              event.

          plane_number: GEO slot plane number/designator of the spacecraft at event time.

          plane_slot: GEO plane slot of the spacecraft at event time.

          position_status: Position status of the spacecraft at event time (e.g. Stable, Drifting/Tumbling,
              etc).

          remarks: Additional remarks on the event description.

          satellite_position: Description of the satellite orbital position or regime.

          sat_no: Satellite/Catalog number of the target on-orbit object.

          stage_at_fault: Faulty stage of flight for the event.

          third_party_insurance_loss: Insurance loss incurred by 3rd party insurance, in USD.

          underlying_cause: Underlying cause of the event.

          until_time: Maximum validity time of the event.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/udl/onorbitevent",
            body=await async_maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "event_time": event_time,
                    "source": source,
                    "id": id,
                    "achieved_flight_phase": achieved_flight_phase,
                    "age_at_event": age_at_event,
                    "capability_loss": capability_loss,
                    "capability_loss_notes": capability_loss_notes,
                    "capacity_loss": capacity_loss,
                    "consequential_equipment_failure": consequential_equipment_failure,
                    "declassification_date": declassification_date,
                    "declassification_string": declassification_string,
                    "derived_from": derived_from,
                    "description": description,
                    "equipment_at_fault": equipment_at_fault,
                    "equipment_causing_loss_notes": equipment_causing_loss_notes,
                    "equipment_part_at_fault": equipment_part_at_fault,
                    "equipment_type_at_fault": equipment_type_at_fault,
                    "event_result": event_result,
                    "event_time_notes": event_time_notes,
                    "event_type": event_type,
                    "geo_position": geo_position,
                    "id_on_orbit": id_on_orbit,
                    "inclined": inclined,
                    "injured": injured,
                    "insurance_carried_notes": insurance_carried_notes,
                    "insurance_loss": insurance_loss,
                    "insurance_loss_notes": insurance_loss_notes,
                    "killed": killed,
                    "lessee_org_id": lessee_org_id,
                    "life_lost": life_lost,
                    "net_amount": net_amount,
                    "object_status": object_status,
                    "occurrence_flight_phase": occurrence_flight_phase,
                    "official_loss_date": official_loss_date,
                    "operated_on_behalf_of_org_id": operated_on_behalf_of_org_id,
                    "operator_org_id": operator_org_id,
                    "origin": origin,
                    "orig_object_id": orig_object_id,
                    "owner_org_id": owner_org_id,
                    "plane_number": plane_number,
                    "plane_slot": plane_slot,
                    "position_status": position_status,
                    "remarks": remarks,
                    "satellite_position": satellite_position,
                    "sat_no": sat_no,
                    "stage_at_fault": stage_at_fault,
                    "third_party_insurance_loss": third_party_insurance_loss,
                    "underlying_cause": underlying_cause,
                    "until_time": until_time,
                },
                onorbitevent_create_params.OnorbiteventCreateParams,
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
        event_time: Union[str, datetime],
        source: str,
        body_id: str | NotGiven = NOT_GIVEN,
        achieved_flight_phase: str | NotGiven = NOT_GIVEN,
        age_at_event: float | NotGiven = NOT_GIVEN,
        capability_loss: float | NotGiven = NOT_GIVEN,
        capability_loss_notes: str | NotGiven = NOT_GIVEN,
        capacity_loss: float | NotGiven = NOT_GIVEN,
        consequential_equipment_failure: str | NotGiven = NOT_GIVEN,
        declassification_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        declassification_string: str | NotGiven = NOT_GIVEN,
        derived_from: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        equipment_at_fault: str | NotGiven = NOT_GIVEN,
        equipment_causing_loss_notes: str | NotGiven = NOT_GIVEN,
        equipment_part_at_fault: str | NotGiven = NOT_GIVEN,
        equipment_type_at_fault: str | NotGiven = NOT_GIVEN,
        event_result: str | NotGiven = NOT_GIVEN,
        event_time_notes: str | NotGiven = NOT_GIVEN,
        event_type: str | NotGiven = NOT_GIVEN,
        geo_position: float | NotGiven = NOT_GIVEN,
        id_on_orbit: str | NotGiven = NOT_GIVEN,
        inclined: bool | NotGiven = NOT_GIVEN,
        injured: int | NotGiven = NOT_GIVEN,
        insurance_carried_notes: str | NotGiven = NOT_GIVEN,
        insurance_loss: float | NotGiven = NOT_GIVEN,
        insurance_loss_notes: str | NotGiven = NOT_GIVEN,
        killed: int | NotGiven = NOT_GIVEN,
        lessee_org_id: str | NotGiven = NOT_GIVEN,
        life_lost: float | NotGiven = NOT_GIVEN,
        net_amount: float | NotGiven = NOT_GIVEN,
        object_status: str | NotGiven = NOT_GIVEN,
        occurrence_flight_phase: str | NotGiven = NOT_GIVEN,
        official_loss_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        operated_on_behalf_of_org_id: str | NotGiven = NOT_GIVEN,
        operator_org_id: str | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        orig_object_id: str | NotGiven = NOT_GIVEN,
        owner_org_id: str | NotGiven = NOT_GIVEN,
        plane_number: str | NotGiven = NOT_GIVEN,
        plane_slot: str | NotGiven = NOT_GIVEN,
        position_status: str | NotGiven = NOT_GIVEN,
        remarks: str | NotGiven = NOT_GIVEN,
        satellite_position: str | NotGiven = NOT_GIVEN,
        sat_no: int | NotGiven = NOT_GIVEN,
        stage_at_fault: str | NotGiven = NOT_GIVEN,
        third_party_insurance_loss: float | NotGiven = NOT_GIVEN,
        underlying_cause: str | NotGiven = NOT_GIVEN,
        until_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Service operation to update a single OnorbitEvent.

        An OnorbitEvent is an event
        associated with a particular on-orbit spacecraft including insurance related
        losses, anomalies and incidents. A specific role is required to perform this
        service operation. Please contact the UDL team for assistance.

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

          event_time: Date/Time of the event. See eventTimeNotes for remarks on the accuracy of the
              date time.

          source: Source of the data.

          body_id: Unique identifier of the record, auto-generated by the system.

          achieved_flight_phase: Achieved phase of flight prior to the event.

          age_at_event: Spacecraft age at the event in years.

          capability_loss: Spacecraft capability loss incurred, as a fraction of 1.

          capability_loss_notes: Notes on capability loss at the time of event.

          capacity_loss: Spacecraft capacity loss incurred, as a fraction of 1.

          consequential_equipment_failure: Additional equipment which failed as a result of faulty equipment on the
              spacecraft during the event.

          declassification_date: The declassification date of this data, in ISO 8601 UTC format.

          declassification_string: Declassification string of this data.

          derived_from: The sources or SCG references from which the classification of this data is
              derived.

          description: Notes/description of the event.

          equipment_at_fault: Equipment on the spacecraft which caused the event.

          equipment_causing_loss_notes: Additional notes on the equipment causing the event/loss.

          equipment_part_at_fault: Specific part of the equipment on the spacecraft which caused the event.

          equipment_type_at_fault: Type of the equipment on the spacecraft which caused the event.

          event_result: The result of the reported event.

          event_time_notes: Notes/remarks on the validity/accuracy of the eventTime.

          event_type: The type of on-orbit event being reported.

          geo_position: GEO position longitude at event time if applicable. Negative values are west.

          id_on_orbit: Unique identifier of the on-orbit object for this event.

          inclined: Boolean indicating if the spacecraft is inclined.

          injured: Number of humans injured in the event.

          insurance_carried_notes: Additional insurance notes on coverages at the time of event.

          insurance_loss: Insurance loss incurred, as a fraction of 1.

          insurance_loss_notes: Additional insurance notes if the event is an official loss.

          killed: Number of humans killed in the event.

          lessee_org_id: Unique identifier of the organization which leases this on-orbit spacecraft.

          life_lost: Spacecraft life lost due to the event as a percent/fraction of 1.

          net_amount: Net amount of the insurance claim for the event, in USD.

          object_status: The status of the on-orbit object.

          occurrence_flight_phase: Phase of flight during which the event occurred.

          official_loss_date: Date time of official loss of the spacecraft.

          operated_on_behalf_of_org_id: Unique identifier of the organization on whose behalf the on-orbit spacecraft is
              operated.

          operator_org_id: Organization ID of the operator of the on-orbit spacecraft at the time of the
              event.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          orig_object_id: Original object ID or Catalog Number provided by source (may not map to an
              existing idOnOrbit in UDL).

          owner_org_id: Organization ID of the owner of the on-orbit spacecraft at the time of the
              event.

          plane_number: GEO slot plane number/designator of the spacecraft at event time.

          plane_slot: GEO plane slot of the spacecraft at event time.

          position_status: Position status of the spacecraft at event time (e.g. Stable, Drifting/Tumbling,
              etc).

          remarks: Additional remarks on the event description.

          satellite_position: Description of the satellite orbital position or regime.

          sat_no: Satellite/Catalog number of the target on-orbit object.

          stage_at_fault: Faulty stage of flight for the event.

          third_party_insurance_loss: Insurance loss incurred by 3rd party insurance, in USD.

          underlying_cause: Underlying cause of the event.

          until_time: Maximum validity time of the event.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            f"/udl/onorbitevent/{path_id}",
            body=await async_maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "event_time": event_time,
                    "source": source,
                    "body_id": body_id,
                    "achieved_flight_phase": achieved_flight_phase,
                    "age_at_event": age_at_event,
                    "capability_loss": capability_loss,
                    "capability_loss_notes": capability_loss_notes,
                    "capacity_loss": capacity_loss,
                    "consequential_equipment_failure": consequential_equipment_failure,
                    "declassification_date": declassification_date,
                    "declassification_string": declassification_string,
                    "derived_from": derived_from,
                    "description": description,
                    "equipment_at_fault": equipment_at_fault,
                    "equipment_causing_loss_notes": equipment_causing_loss_notes,
                    "equipment_part_at_fault": equipment_part_at_fault,
                    "equipment_type_at_fault": equipment_type_at_fault,
                    "event_result": event_result,
                    "event_time_notes": event_time_notes,
                    "event_type": event_type,
                    "geo_position": geo_position,
                    "id_on_orbit": id_on_orbit,
                    "inclined": inclined,
                    "injured": injured,
                    "insurance_carried_notes": insurance_carried_notes,
                    "insurance_loss": insurance_loss,
                    "insurance_loss_notes": insurance_loss_notes,
                    "killed": killed,
                    "lessee_org_id": lessee_org_id,
                    "life_lost": life_lost,
                    "net_amount": net_amount,
                    "object_status": object_status,
                    "occurrence_flight_phase": occurrence_flight_phase,
                    "official_loss_date": official_loss_date,
                    "operated_on_behalf_of_org_id": operated_on_behalf_of_org_id,
                    "operator_org_id": operator_org_id,
                    "origin": origin,
                    "orig_object_id": orig_object_id,
                    "owner_org_id": owner_org_id,
                    "plane_number": plane_number,
                    "plane_slot": plane_slot,
                    "position_status": position_status,
                    "remarks": remarks,
                    "satellite_position": satellite_position,
                    "sat_no": sat_no,
                    "stage_at_fault": stage_at_fault,
                    "third_party_insurance_loss": third_party_insurance_loss,
                    "underlying_cause": underlying_cause,
                    "until_time": until_time,
                },
                onorbitevent_update_params.OnorbiteventUpdateParams,
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
    ) -> AsyncPaginator[OnorbiteventListResponse, AsyncOffsetPage[OnorbiteventListResponse]]:
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
            "/udl/onorbitevent",
            page=AsyncOffsetPage[OnorbiteventListResponse],
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
                    onorbitevent_list_params.OnorbiteventListParams,
                ),
            ),
            model=OnorbiteventListResponse,
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
        Service operation to delete a OnorbitEvent object specified by the passed ID
        path parameter. An OnorbitEvent is an event associated with a particular
        on-orbit spacecraft including insurance related losses, anomalies and incidents.
        A specific role is required to perform this service operation. Please contact
        the UDL team for assistance.

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
            f"/udl/onorbitevent/{id}",
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
            "/udl/onorbitevent/count",
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
                    onorbitevent_count_params.OnorbiteventCountParams,
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
    ) -> OnorbiteventGetResponse:
        """
        Service operation to get a single OnorbitEvent record by its unique ID passed as
        a path parameter. An OnorbitEvent is an event associated with a particular
        on-orbit spacecraft including insurance related losses, anomalies and incidents.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/udl/onorbitevent/{id}",
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
                    onorbitevent_get_params.OnorbiteventGetParams,
                ),
            ),
            cast_to=OnorbiteventGetResponse,
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
            "/udl/onorbitevent/queryhelp",
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
    ) -> OnorbiteventTupleResponse:
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
            "/udl/onorbitevent/tuple",
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
                    onorbitevent_tuple_params.OnorbiteventTupleParams,
                ),
            ),
            cast_to=OnorbiteventTupleResponse,
        )


class OnorbiteventResourceWithRawResponse:
    def __init__(self, onorbitevent: OnorbiteventResource) -> None:
        self._onorbitevent = onorbitevent

        self.create = to_raw_response_wrapper(
            onorbitevent.create,
        )
        self.update = to_raw_response_wrapper(
            onorbitevent.update,
        )
        self.list = to_raw_response_wrapper(
            onorbitevent.list,
        )
        self.delete = to_raw_response_wrapper(
            onorbitevent.delete,
        )
        self.count = to_raw_response_wrapper(
            onorbitevent.count,
        )
        self.get = to_raw_response_wrapper(
            onorbitevent.get,
        )
        self.queryhelp = to_raw_response_wrapper(
            onorbitevent.queryhelp,
        )
        self.tuple = to_raw_response_wrapper(
            onorbitevent.tuple,
        )


class AsyncOnorbiteventResourceWithRawResponse:
    def __init__(self, onorbitevent: AsyncOnorbiteventResource) -> None:
        self._onorbitevent = onorbitevent

        self.create = async_to_raw_response_wrapper(
            onorbitevent.create,
        )
        self.update = async_to_raw_response_wrapper(
            onorbitevent.update,
        )
        self.list = async_to_raw_response_wrapper(
            onorbitevent.list,
        )
        self.delete = async_to_raw_response_wrapper(
            onorbitevent.delete,
        )
        self.count = async_to_raw_response_wrapper(
            onorbitevent.count,
        )
        self.get = async_to_raw_response_wrapper(
            onorbitevent.get,
        )
        self.queryhelp = async_to_raw_response_wrapper(
            onorbitevent.queryhelp,
        )
        self.tuple = async_to_raw_response_wrapper(
            onorbitevent.tuple,
        )


class OnorbiteventResourceWithStreamingResponse:
    def __init__(self, onorbitevent: OnorbiteventResource) -> None:
        self._onorbitevent = onorbitevent

        self.create = to_streamed_response_wrapper(
            onorbitevent.create,
        )
        self.update = to_streamed_response_wrapper(
            onorbitevent.update,
        )
        self.list = to_streamed_response_wrapper(
            onorbitevent.list,
        )
        self.delete = to_streamed_response_wrapper(
            onorbitevent.delete,
        )
        self.count = to_streamed_response_wrapper(
            onorbitevent.count,
        )
        self.get = to_streamed_response_wrapper(
            onorbitevent.get,
        )
        self.queryhelp = to_streamed_response_wrapper(
            onorbitevent.queryhelp,
        )
        self.tuple = to_streamed_response_wrapper(
            onorbitevent.tuple,
        )


class AsyncOnorbiteventResourceWithStreamingResponse:
    def __init__(self, onorbitevent: AsyncOnorbiteventResource) -> None:
        self._onorbitevent = onorbitevent

        self.create = async_to_streamed_response_wrapper(
            onorbitevent.create,
        )
        self.update = async_to_streamed_response_wrapper(
            onorbitevent.update,
        )
        self.list = async_to_streamed_response_wrapper(
            onorbitevent.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            onorbitevent.delete,
        )
        self.count = async_to_streamed_response_wrapper(
            onorbitevent.count,
        )
        self.get = async_to_streamed_response_wrapper(
            onorbitevent.get,
        )
        self.queryhelp = async_to_streamed_response_wrapper(
            onorbitevent.queryhelp,
        )
        self.tuple = async_to_streamed_response_wrapper(
            onorbitevent.tuple,
        )
