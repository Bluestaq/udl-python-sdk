# Shared Types

```python
from unifieddatalibrary.types import (
    AirTaskingOrderFull,
    AirTransportMissionFull,
    AircraftFull,
    AircraftsortieFull,
    AircraftstatusFull,
    AircraftstatusremarkFull,
    AirfieldFull,
    AirfieldslotFull,
    AirfieldslotconsumptionFull,
    AirfieldstatusFull,
    AirloadplanFull,
    AirspacecontrolorderFull,
    AIsFull,
    AnalyticImageryFull,
    AntennaDetailsFull,
    AntennaFull,
    AntennaIngest,
    AttitudedataFull,
    AttitudesetFull,
    BatteryFull,
    BatteryIngest,
    BatterydetailsFull,
    BeamFull,
    BeamcontourFull,
    BusFull,
    ChannelFull,
    CollectRequestFull,
    CollectResponseFull,
    CommFull,
    ConjunctionFull,
    CountryFull,
    CrewFull,
    DailyOperationFull,
    DiplomaticclearanceFull,
    DriftHistoryAbridged,
    DriftHistoryFull,
    Engine,
    EngineDetailsFull,
    EngineIngest,
    EntityFull,
    EoObservationFull,
    EopFull,
    EphemerisFull,
    EvacFull,
    EventEvolutionFull,
    FileData,
    FlightPlanFull,
    LocationAbridged,
    LocationFull,
    MaximumOnGroundFull,
    NotificationFull,
    OnboardnavigationFull,
    OnorbitAntennaFull,
    OnorbitBatteryFull,
    OnorbitDetailsFull,
    OnorbitFull,
    OnorbitSolarArrayFull,
    OnorbitThrusterFull,
    OnorbitthrusterstatusFull,
    OperatingHoursFull,
    OperatingUnitRemarkFull,
    OperatingunitFull,
    OperationalDeviationFull,
    OperationalPlanningFull,
    OrganizationDetailsFull,
    OrganizationFull,
    ParamDescriptor,
    PathwayFull,
    RelatedDocumentFull,
    RfBandFull,
    SofDataSourceRefFull,
    SolarArrayDetailsFull,
    SolarArrayFull,
    SolarArrayIngest,
    SortiePprFull,
    StateVectorFull,
    StatusFull,
    SubStatusFull,
    SubStatusIngest,
    WaiverFull,
)
```

# AirEvents

Types:

```python
from unifieddatalibrary.types import (
    AirEventListResponse,
    AirEventCountResponse,
    AirEventGetResponse,
    AirEventQueryhelpResponse,
    AirEventTupleResponse,
)
```

Methods:

- <code title="post /udl/airevent">client.air_events.<a href="./src/unifieddatalibrary/resources/air_events.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/air_event_create_params.py">params</a>) -> None</code>
- <code title="put /udl/airevent/{id}">client.air_events.<a href="./src/unifieddatalibrary/resources/air_events.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/air_event_update_params.py">params</a>) -> None</code>
- <code title="get /udl/airevent">client.air_events.<a href="./src/unifieddatalibrary/resources/air_events.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/air_event_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/air_event_list_response.py">SyncOffsetPage[AirEventListResponse]</a></code>
- <code title="delete /udl/airevent/{id}">client.air_events.<a href="./src/unifieddatalibrary/resources/air_events.py">delete</a>(id) -> None</code>
- <code title="get /udl/airevent/count">client.air_events.<a href="./src/unifieddatalibrary/resources/air_events.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/air_event_count_params.py">params</a>) -> str</code>
- <code title="post /udl/airevent/createBulk">client.air_events.<a href="./src/unifieddatalibrary/resources/air_events.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/air_event_create_bulk_params.py">params</a>) -> None</code>
- <code title="get /udl/airevent/{id}">client.air_events.<a href="./src/unifieddatalibrary/resources/air_events.py">get</a>(id, \*\*<a href="src/unifieddatalibrary/types/air_event_get_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/air_event_get_response.py">AirEventGetResponse</a></code>
- <code title="get /udl/airevent/queryhelp">client.air_events.<a href="./src/unifieddatalibrary/resources/air_events.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/air_event_queryhelp_response.py">AirEventQueryhelpResponse</a></code>
- <code title="get /udl/airevent/tuple">client.air_events.<a href="./src/unifieddatalibrary/resources/air_events.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/air_event_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/air_event_tuple_response.py">AirEventTupleResponse</a></code>
- <code title="post /filedrop/udl-airevent">client.air_events.<a href="./src/unifieddatalibrary/resources/air_events.py">unvalidated_publish</a>(\*\*<a href="src/unifieddatalibrary/types/air_event_unvalidated_publish_params.py">params</a>) -> None</code>

# AirOperations

## AirTaskingOrders

Types:

```python
from unifieddatalibrary.types.air_operations import (
    AirtaskingorderAbridged,
    AirTaskingOrderCountResponse,
    AirTaskingOrderQueryHelpResponse,
    AirTaskingOrderTupleResponse,
)
```

Methods:

- <code title="post /udl/airtaskingorder">client.air_operations.air_tasking_orders.<a href="./src/unifieddatalibrary/resources/air_operations/air_tasking_orders.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/air_operations/air_tasking_order_create_params.py">params</a>) -> None</code>
- <code title="get /udl/airtaskingorder/{id}">client.air_operations.air_tasking_orders.<a href="./src/unifieddatalibrary/resources/air_operations/air_tasking_orders.py">retrieve</a>(id, \*\*<a href="src/unifieddatalibrary/types/air_operations/air_tasking_order_retrieve_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/shared/air_tasking_order_full.py">AirTaskingOrderFull</a></code>
- <code title="get /udl/airtaskingorder">client.air_operations.air_tasking_orders.<a href="./src/unifieddatalibrary/resources/air_operations/air_tasking_orders.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/air_operations/air_tasking_order_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/air_operations/airtaskingorder_abridged.py">SyncOffsetPage[AirtaskingorderAbridged]</a></code>
- <code title="get /udl/airtaskingorder/count">client.air_operations.air_tasking_orders.<a href="./src/unifieddatalibrary/resources/air_operations/air_tasking_orders.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/air_operations/air_tasking_order_count_params.py">params</a>) -> str</code>
- <code title="get /udl/airtaskingorder/queryhelp">client.air_operations.air_tasking_orders.<a href="./src/unifieddatalibrary/resources/air_operations/air_tasking_orders.py">query_help</a>() -> <a href="./src/unifieddatalibrary/types/air_operations/air_tasking_order_query_help_response.py">AirTaskingOrderQueryHelpResponse</a></code>
- <code title="get /udl/airtaskingorder/tuple">client.air_operations.air_tasking_orders.<a href="./src/unifieddatalibrary/resources/air_operations/air_tasking_orders.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/air_operations/air_tasking_order_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/air_operations/air_tasking_order_tuple_response.py">AirTaskingOrderTupleResponse</a></code>
- <code title="post /filedrop/udl-airtaskingorder">client.air_operations.air_tasking_orders.<a href="./src/unifieddatalibrary/resources/air_operations/air_tasking_orders.py">unvalidated_publish</a>(\*\*<a href="src/unifieddatalibrary/types/air_operations/air_tasking_order_unvalidated_publish_params.py">params</a>) -> None</code>

## AircraftSorties

Types:

```python
from unifieddatalibrary.types.air_operations import (
    AircraftsortieAbridged,
    AircraftSortyCountResponse,
)
```

Methods:

- <code title="post /udl/aircraftsortie">client.air_operations.aircraft_sorties.<a href="./src/unifieddatalibrary/resources/air_operations/aircraft_sorties/aircraft_sorties.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/air_operations/aircraft_sorty_create_params.py">params</a>) -> None</code>
- <code title="get /udl/aircraftsortie">client.air_operations.aircraft_sorties.<a href="./src/unifieddatalibrary/resources/air_operations/aircraft_sorties/aircraft_sorties.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/air_operations/aircraft_sorty_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/air_operations/aircraftsortie_abridged.py">SyncOffsetPage[AircraftsortieAbridged]</a></code>
- <code title="get /udl/aircraftsortie/count">client.air_operations.aircraft_sorties.<a href="./src/unifieddatalibrary/resources/air_operations/aircraft_sorties/aircraft_sorties.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/air_operations/aircraft_sorty_count_params.py">params</a>) -> str</code>
- <code title="post /udl/aircraftsortie/createBulk">client.air_operations.aircraft_sorties.<a href="./src/unifieddatalibrary/resources/air_operations/aircraft_sorties/aircraft_sorties.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/air_operations/aircraft_sorty_create_bulk_params.py">params</a>) -> None</code>
- <code title="post /filedrop/udl-aircraftsortie">client.air_operations.aircraft_sorties.<a href="./src/unifieddatalibrary/resources/air_operations/aircraft_sorties/aircraft_sorties.py">unvalidated_publish</a>(\*\*<a href="src/unifieddatalibrary/types/air_operations/aircraft_sorty_unvalidated_publish_params.py">params</a>) -> None</code>

### History

Types:

```python
from unifieddatalibrary.types.air_operations.aircraft_sorties import HistoryCountResponse
```

Methods:

- <code title="get /udl/aircraftsortie/history">client.air_operations.aircraft_sorties.history.<a href="./src/unifieddatalibrary/resources/air_operations/aircraft_sorties/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/air_operations/aircraft_sorties/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/shared/aircraftsortie_full.py">SyncOffsetPage[AircraftsortieFull]</a></code>
- <code title="get /udl/aircraftsortie/history/aodr">client.air_operations.aircraft_sorties.history.<a href="./src/unifieddatalibrary/resources/air_operations/aircraft_sorties/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/air_operations/aircraft_sorties/history_aodr_params.py">params</a>) -> None</code>
- <code title="get /udl/aircraftsortie/history/count">client.air_operations.aircraft_sorties.history.<a href="./src/unifieddatalibrary/resources/air_operations/aircraft_sorties/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/air_operations/aircraft_sorties/history_count_params.py">params</a>) -> str</code>

## AirspaceControlOrders

Methods:

- <code title="post /filedrop/udl-airspacecontrolorder">client.air_operations.airspace_control_orders.<a href="./src/unifieddatalibrary/resources/air_operations/airspace_control_orders.py">unvalidated_publish</a>(\*\*<a href="src/unifieddatalibrary/types/air_operations/airspace_control_order_unvalidated_publish_params.py">params</a>) -> None</code>

## Crewpapers

Methods:

- <code title="post /udl/crewpapers/unpublish">client.air_operations.crewpapers.<a href="./src/unifieddatalibrary/resources/air_operations/crewpapers.py">unpublish</a>(\*\*<a href="src/unifieddatalibrary/types/air_operations/crewpaper_unpublish_params.py">params</a>) -> None</code>
- <code title="post /filedrop/crewpapers">client.air_operations.crewpapers.<a href="./src/unifieddatalibrary/resources/air_operations/crewpapers.py">upload_pdf</a>(file_content, \*\*<a href="src/unifieddatalibrary/types/air_operations/crewpaper_upload_pdf_params.py">params</a>) -> None</code>

## DiplomaticClearance

Types:

```python
from unifieddatalibrary.types.air_operations import DiplomaticclearanceAbridged
```

Methods:

- <code title="post /filedrop/udl-diplomaticclearance">client.air_operations.diplomatic_clearance.<a href="./src/unifieddatalibrary/resources/air_operations/diplomatic_clearance.py">unvalidated_publish</a>(\*\*<a href="src/unifieddatalibrary/types/air_operations/diplomatic_clearance_unvalidated_publish_params.py">params</a>) -> None</code>

# AirTransportMissions

Types:

```python
from unifieddatalibrary.types import (
    AirTransportMissionAbridged,
    AirTransportMissionCountResponse,
    AirTransportMissionQueryhelpResponse,
    AirTransportMissionTupleResponse,
)
```

Methods:

- <code title="post /udl/airtransportmission">client.air_transport_missions.<a href="./src/unifieddatalibrary/resources/air_transport_missions/air_transport_missions.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/air_transport_mission_create_params.py">params</a>) -> None</code>
- <code title="get /udl/airtransportmission/{id}">client.air_transport_missions.<a href="./src/unifieddatalibrary/resources/air_transport_missions/air_transport_missions.py">retrieve</a>(id, \*\*<a href="src/unifieddatalibrary/types/air_transport_mission_retrieve_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/shared/air_transport_mission_full.py">AirTransportMissionFull</a></code>
- <code title="put /udl/airtransportmission/{id}">client.air_transport_missions.<a href="./src/unifieddatalibrary/resources/air_transport_missions/air_transport_missions.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/air_transport_mission_update_params.py">params</a>) -> None</code>
- <code title="get /udl/airtransportmission">client.air_transport_missions.<a href="./src/unifieddatalibrary/resources/air_transport_missions/air_transport_missions.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/air_transport_mission_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/air_transport_mission_abridged.py">SyncOffsetPage[AirTransportMissionAbridged]</a></code>
- <code title="get /udl/airtransportmission/count">client.air_transport_missions.<a href="./src/unifieddatalibrary/resources/air_transport_missions/air_transport_missions.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/air_transport_mission_count_params.py">params</a>) -> str</code>
- <code title="get /udl/airtransportmission/queryhelp">client.air_transport_missions.<a href="./src/unifieddatalibrary/resources/air_transport_missions/air_transport_missions.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/air_transport_mission_queryhelp_response.py">AirTransportMissionQueryhelpResponse</a></code>
- <code title="get /udl/airtransportmission/tuple">client.air_transport_missions.<a href="./src/unifieddatalibrary/resources/air_transport_missions/air_transport_missions.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/air_transport_mission_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/air_transport_mission_tuple_response.py">AirTransportMissionTupleResponse</a></code>

## History

Types:

```python
from unifieddatalibrary.types.air_transport_missions import HistoryCountResponse
```

Methods:

- <code title="get /udl/airtransportmission/history">client.air_transport_missions.history.<a href="./src/unifieddatalibrary/resources/air_transport_missions/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/air_transport_missions/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/shared/air_transport_mission_full.py">SyncOffsetPage[AirTransportMissionFull]</a></code>
- <code title="get /udl/airtransportmission/history/aodr">client.air_transport_missions.history.<a href="./src/unifieddatalibrary/resources/air_transport_missions/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/air_transport_missions/history_aodr_params.py">params</a>) -> None</code>
- <code title="get /udl/airtransportmission/history/count">client.air_transport_missions.history.<a href="./src/unifieddatalibrary/resources/air_transport_missions/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/air_transport_missions/history_count_params.py">params</a>) -> str</code>

# Aircraft

Types:

```python
from unifieddatalibrary.types import (
    AircraftAbridged,
    AircraftCountResponse,
    AircraftQueryhelpResponse,
    AircraftTupleResponse,
)
```

Methods:

- <code title="post /udl/aircraft">client.aircraft.<a href="./src/unifieddatalibrary/resources/aircraft.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/aircraft_create_params.py">params</a>) -> None</code>
- <code title="get /udl/aircraft/{id}">client.aircraft.<a href="./src/unifieddatalibrary/resources/aircraft.py">retrieve</a>(id, \*\*<a href="src/unifieddatalibrary/types/aircraft_retrieve_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/shared/aircraft_full.py">AircraftFull</a></code>
- <code title="put /udl/aircraft/{id}">client.aircraft.<a href="./src/unifieddatalibrary/resources/aircraft.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/aircraft_update_params.py">params</a>) -> None</code>
- <code title="get /udl/aircraft">client.aircraft.<a href="./src/unifieddatalibrary/resources/aircraft.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/aircraft_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/aircraft_abridged.py">SyncOffsetPage[AircraftAbridged]</a></code>
- <code title="get /udl/aircraft/count">client.aircraft.<a href="./src/unifieddatalibrary/resources/aircraft.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/aircraft_count_params.py">params</a>) -> str</code>
- <code title="get /udl/aircraft/queryhelp">client.aircraft.<a href="./src/unifieddatalibrary/resources/aircraft.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/aircraft_queryhelp_response.py">AircraftQueryhelpResponse</a></code>
- <code title="get /udl/aircraft/tuple">client.aircraft.<a href="./src/unifieddatalibrary/resources/aircraft.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/aircraft_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/aircraft_tuple_response.py">AircraftTupleResponse</a></code>

# AircraftSorties

Types:

```python
from unifieddatalibrary.types import AircraftSortyQueryhelpResponse, AircraftSortyTupleResponse
```

Methods:

- <code title="get /udl/aircraftsortie/{id}">client.aircraft_sorties.<a href="./src/unifieddatalibrary/resources/aircraft_sorties.py">retrieve</a>(id, \*\*<a href="src/unifieddatalibrary/types/aircraft_sorty_retrieve_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/shared/aircraftsortie_full.py">AircraftsortieFull</a></code>
- <code title="put /udl/aircraftsortie/{id}">client.aircraft_sorties.<a href="./src/unifieddatalibrary/resources/aircraft_sorties.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/aircraft_sorty_update_params.py">params</a>) -> None</code>
- <code title="get /udl/aircraftsortie/queryhelp">client.aircraft_sorties.<a href="./src/unifieddatalibrary/resources/aircraft_sorties.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/aircraft_sorty_queryhelp_response.py">AircraftSortyQueryhelpResponse</a></code>
- <code title="get /udl/aircraftsortie/tuple">client.aircraft_sorties.<a href="./src/unifieddatalibrary/resources/aircraft_sorties.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/aircraft_sorty_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/aircraft_sorty_tuple_response.py">AircraftSortyTupleResponse</a></code>

# AircraftStatusRemarks

Types:

```python
from unifieddatalibrary.types import (
    AircraftstatusremarkAbridged,
    AircraftStatusRemarkCountResponse,
    AircraftStatusRemarkQueryhelpResponse,
    AircraftStatusRemarkTupleResponse,
)
```

Methods:

- <code title="post /udl/aircraftstatusremark">client.aircraft_status_remarks.<a href="./src/unifieddatalibrary/resources/aircraft_status_remarks.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/aircraft_status_remark_create_params.py">params</a>) -> None</code>
- <code title="get /udl/aircraftstatusremark/{id}">client.aircraft_status_remarks.<a href="./src/unifieddatalibrary/resources/aircraft_status_remarks.py">retrieve</a>(id, \*\*<a href="src/unifieddatalibrary/types/aircraft_status_remark_retrieve_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/shared/aircraftstatusremark_full.py">AircraftstatusremarkFull</a></code>
- <code title="put /udl/aircraftstatusremark/{id}">client.aircraft_status_remarks.<a href="./src/unifieddatalibrary/resources/aircraft_status_remarks.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/aircraft_status_remark_update_params.py">params</a>) -> None</code>
- <code title="get /udl/aircraftstatusremark">client.aircraft_status_remarks.<a href="./src/unifieddatalibrary/resources/aircraft_status_remarks.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/aircraft_status_remark_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/aircraftstatusremark_abridged.py">SyncOffsetPage[AircraftstatusremarkAbridged]</a></code>
- <code title="delete /udl/aircraftstatusremark/{id}">client.aircraft_status_remarks.<a href="./src/unifieddatalibrary/resources/aircraft_status_remarks.py">delete</a>(id) -> None</code>
- <code title="get /udl/aircraftstatusremark/count">client.aircraft_status_remarks.<a href="./src/unifieddatalibrary/resources/aircraft_status_remarks.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/aircraft_status_remark_count_params.py">params</a>) -> str</code>
- <code title="get /udl/aircraftstatusremark/queryhelp">client.aircraft_status_remarks.<a href="./src/unifieddatalibrary/resources/aircraft_status_remarks.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/aircraft_status_remark_queryhelp_response.py">AircraftStatusRemarkQueryhelpResponse</a></code>
- <code title="get /udl/aircraftstatusremark/tuple">client.aircraft_status_remarks.<a href="./src/unifieddatalibrary/resources/aircraft_status_remarks.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/aircraft_status_remark_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/aircraft_status_remark_tuple_response.py">AircraftStatusRemarkTupleResponse</a></code>

# AircraftStatuses

Types:

```python
from unifieddatalibrary.types import (
    AircraftstatusAbridged,
    AircraftStatusCountResponse,
    AircraftStatusQueryhelpResponse,
    AircraftStatusTupleResponse,
)
```

Methods:

- <code title="post /udl/aircraftstatus">client.aircraft_statuses.<a href="./src/unifieddatalibrary/resources/aircraft_statuses/aircraft_statuses.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/aircraft_status_create_params.py">params</a>) -> None</code>
- <code title="get /udl/aircraftstatus/{id}">client.aircraft_statuses.<a href="./src/unifieddatalibrary/resources/aircraft_statuses/aircraft_statuses.py">retrieve</a>(id, \*\*<a href="src/unifieddatalibrary/types/aircraft_status_retrieve_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/shared/aircraftstatus_full.py">AircraftstatusFull</a></code>
- <code title="put /udl/aircraftstatus/{id}">client.aircraft_statuses.<a href="./src/unifieddatalibrary/resources/aircraft_statuses/aircraft_statuses.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/aircraft_status_update_params.py">params</a>) -> None</code>
- <code title="get /udl/aircraftstatus">client.aircraft_statuses.<a href="./src/unifieddatalibrary/resources/aircraft_statuses/aircraft_statuses.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/aircraft_status_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/aircraftstatus_abridged.py">SyncOffsetPage[AircraftstatusAbridged]</a></code>
- <code title="delete /udl/aircraftstatus/{id}">client.aircraft_statuses.<a href="./src/unifieddatalibrary/resources/aircraft_statuses/aircraft_statuses.py">delete</a>(id) -> None</code>
- <code title="get /udl/aircraftstatus/count">client.aircraft_statuses.<a href="./src/unifieddatalibrary/resources/aircraft_statuses/aircraft_statuses.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/aircraft_status_count_params.py">params</a>) -> str</code>
- <code title="get /udl/aircraftstatus/queryhelp">client.aircraft_statuses.<a href="./src/unifieddatalibrary/resources/aircraft_statuses/aircraft_statuses.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/aircraft_status_queryhelp_response.py">AircraftStatusQueryhelpResponse</a></code>
- <code title="get /udl/aircraftstatus/tuple">client.aircraft_statuses.<a href="./src/unifieddatalibrary/resources/aircraft_statuses/aircraft_statuses.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/aircraft_status_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/aircraft_status_tuple_response.py">AircraftStatusTupleResponse</a></code>

## History

Types:

```python
from unifieddatalibrary.types.aircraft_statuses import HistoryCountResponse
```

Methods:

- <code title="get /udl/aircraftstatus/history">client.aircraft_statuses.history.<a href="./src/unifieddatalibrary/resources/aircraft_statuses/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/aircraft_statuses/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/shared/aircraftstatus_full.py">SyncOffsetPage[AircraftstatusFull]</a></code>
- <code title="get /udl/aircraftstatus/history/count">client.aircraft_statuses.history.<a href="./src/unifieddatalibrary/resources/aircraft_statuses/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/aircraft_statuses/history_count_params.py">params</a>) -> str</code>

# AirfieldSlotConsumptions

Types:

```python
from unifieddatalibrary.types import (
    AirfieldslotconsumptionAbridged,
    AirfieldSlotConsumptionCountResponse,
    AirfieldSlotConsumptionQueryhelpResponse,
    AirfieldSlotConsumptionTupleResponse,
)
```

Methods:

- <code title="post /udl/airfieldslotconsumption">client.airfield_slot_consumptions.<a href="./src/unifieddatalibrary/resources/airfield_slot_consumptions.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/airfield_slot_consumption_create_params.py">params</a>) -> None</code>
- <code title="get /udl/airfieldslotconsumption/{id}">client.airfield_slot_consumptions.<a href="./src/unifieddatalibrary/resources/airfield_slot_consumptions.py">retrieve</a>(id, \*\*<a href="src/unifieddatalibrary/types/airfield_slot_consumption_retrieve_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/shared/airfieldslotconsumption_full.py">AirfieldslotconsumptionFull</a></code>
- <code title="put /udl/airfieldslotconsumption/{id}">client.airfield_slot_consumptions.<a href="./src/unifieddatalibrary/resources/airfield_slot_consumptions.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/airfield_slot_consumption_update_params.py">params</a>) -> None</code>
- <code title="get /udl/airfieldslotconsumption">client.airfield_slot_consumptions.<a href="./src/unifieddatalibrary/resources/airfield_slot_consumptions.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/airfield_slot_consumption_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/airfieldslotconsumption_abridged.py">SyncOffsetPage[AirfieldslotconsumptionAbridged]</a></code>
- <code title="delete /udl/airfieldslotconsumption/{id}">client.airfield_slot_consumptions.<a href="./src/unifieddatalibrary/resources/airfield_slot_consumptions.py">delete</a>(id) -> None</code>
- <code title="get /udl/airfieldslotconsumption/count">client.airfield_slot_consumptions.<a href="./src/unifieddatalibrary/resources/airfield_slot_consumptions.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/airfield_slot_consumption_count_params.py">params</a>) -> str</code>
- <code title="get /udl/airfieldslotconsumption/queryhelp">client.airfield_slot_consumptions.<a href="./src/unifieddatalibrary/resources/airfield_slot_consumptions.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/airfield_slot_consumption_queryhelp_response.py">AirfieldSlotConsumptionQueryhelpResponse</a></code>
- <code title="get /udl/airfieldslotconsumption/tuple">client.airfield_slot_consumptions.<a href="./src/unifieddatalibrary/resources/airfield_slot_consumptions.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/airfield_slot_consumption_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/airfield_slot_consumption_tuple_response.py">AirfieldSlotConsumptionTupleResponse</a></code>

# AirfieldSlots

Types:

```python
from unifieddatalibrary.types import (
    AirfieldslotAbridged,
    AirfieldSlotCountResponse,
    AirfieldSlotQueryhelpResponse,
    AirfieldSlotTupleResponse,
)
```

Methods:

- <code title="post /udl/airfieldslot">client.airfield_slots.<a href="./src/unifieddatalibrary/resources/airfield_slots.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/airfield_slot_create_params.py">params</a>) -> None</code>
- <code title="get /udl/airfieldslot/{id}">client.airfield_slots.<a href="./src/unifieddatalibrary/resources/airfield_slots.py">retrieve</a>(id, \*\*<a href="src/unifieddatalibrary/types/airfield_slot_retrieve_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/shared/airfieldslot_full.py">AirfieldslotFull</a></code>
- <code title="put /udl/airfieldslot/{id}">client.airfield_slots.<a href="./src/unifieddatalibrary/resources/airfield_slots.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/airfield_slot_update_params.py">params</a>) -> None</code>
- <code title="get /udl/airfieldslot">client.airfield_slots.<a href="./src/unifieddatalibrary/resources/airfield_slots.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/airfield_slot_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/airfieldslot_abridged.py">SyncOffsetPage[AirfieldslotAbridged]</a></code>
- <code title="delete /udl/airfieldslot/{id}">client.airfield_slots.<a href="./src/unifieddatalibrary/resources/airfield_slots.py">delete</a>(id) -> None</code>
- <code title="get /udl/airfieldslot/count">client.airfield_slots.<a href="./src/unifieddatalibrary/resources/airfield_slots.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/airfield_slot_count_params.py">params</a>) -> str</code>
- <code title="get /udl/airfieldslot/queryhelp">client.airfield_slots.<a href="./src/unifieddatalibrary/resources/airfield_slots.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/airfield_slot_queryhelp_response.py">AirfieldSlotQueryhelpResponse</a></code>
- <code title="get /udl/airfieldslot/tuple">client.airfield_slots.<a href="./src/unifieddatalibrary/resources/airfield_slots.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/airfield_slot_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/airfield_slot_tuple_response.py">AirfieldSlotTupleResponse</a></code>

# AirfieldStatus

Types:

```python
from unifieddatalibrary.types import (
    AirfieldstatusAbridged,
    AirfieldStatusCountResponse,
    AirfieldStatusQueryhelpResponse,
    AirfieldStatusTupleResponse,
)
```

Methods:

- <code title="post /udl/airfieldstatus">client.airfield_status.<a href="./src/unifieddatalibrary/resources/airfield_status/airfield_status.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/airfield_status_create_params.py">params</a>) -> None</code>
- <code title="get /udl/airfieldstatus/{id}">client.airfield_status.<a href="./src/unifieddatalibrary/resources/airfield_status/airfield_status.py">retrieve</a>(id, \*\*<a href="src/unifieddatalibrary/types/airfield_status_retrieve_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/shared/airfieldstatus_full.py">AirfieldstatusFull</a></code>
- <code title="put /udl/airfieldstatus/{id}">client.airfield_status.<a href="./src/unifieddatalibrary/resources/airfield_status/airfield_status.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/airfield_status_update_params.py">params</a>) -> None</code>
- <code title="get /udl/airfieldstatus">client.airfield_status.<a href="./src/unifieddatalibrary/resources/airfield_status/airfield_status.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/airfield_status_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/airfieldstatus_abridged.py">SyncOffsetPage[AirfieldstatusAbridged]</a></code>
- <code title="delete /udl/airfieldstatus/{id}">client.airfield_status.<a href="./src/unifieddatalibrary/resources/airfield_status/airfield_status.py">delete</a>(id) -> None</code>
- <code title="get /udl/airfieldstatus/count">client.airfield_status.<a href="./src/unifieddatalibrary/resources/airfield_status/airfield_status.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/airfield_status_count_params.py">params</a>) -> str</code>
- <code title="get /udl/airfieldstatus/queryhelp">client.airfield_status.<a href="./src/unifieddatalibrary/resources/airfield_status/airfield_status.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/airfield_status_queryhelp_response.py">AirfieldStatusQueryhelpResponse</a></code>
- <code title="get /udl/airfieldstatus/tuple">client.airfield_status.<a href="./src/unifieddatalibrary/resources/airfield_status/airfield_status.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/airfield_status_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/airfield_status_tuple_response.py">AirfieldStatusTupleResponse</a></code>

## History

Types:

```python
from unifieddatalibrary.types.airfield_status import HistoryCountResponse
```

Methods:

- <code title="get /udl/airfieldstatus/history">client.airfield_status.history.<a href="./src/unifieddatalibrary/resources/airfield_status/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/airfield_status/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/shared/airfieldstatus_full.py">SyncOffsetPage[AirfieldstatusFull]</a></code>
- <code title="get /udl/airfieldstatus/history/count">client.airfield_status.history.<a href="./src/unifieddatalibrary/resources/airfield_status/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/airfield_status/history_count_params.py">params</a>) -> str</code>

# Airfields

Types:

```python
from unifieddatalibrary.types import (
    AirfieldAbridged,
    AirfieldCountResponse,
    AirfieldQueryhelpResponse,
    AirfieldTupleResponse,
)
```

Methods:

- <code title="post /udl/airfield">client.airfields.<a href="./src/unifieddatalibrary/resources/airfields.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/airfield_create_params.py">params</a>) -> None</code>
- <code title="get /udl/airfield/{id}">client.airfields.<a href="./src/unifieddatalibrary/resources/airfields.py">retrieve</a>(id, \*\*<a href="src/unifieddatalibrary/types/airfield_retrieve_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/shared/airfield_full.py">AirfieldFull</a></code>
- <code title="put /udl/airfield/{id}">client.airfields.<a href="./src/unifieddatalibrary/resources/airfields.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/airfield_update_params.py">params</a>) -> None</code>
- <code title="get /udl/airfield">client.airfields.<a href="./src/unifieddatalibrary/resources/airfields.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/airfield_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/airfield_abridged.py">SyncOffsetPage[AirfieldAbridged]</a></code>
- <code title="get /udl/airfield/count">client.airfields.<a href="./src/unifieddatalibrary/resources/airfields.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/airfield_count_params.py">params</a>) -> str</code>
- <code title="get /udl/airfield/queryhelp">client.airfields.<a href="./src/unifieddatalibrary/resources/airfields.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/airfield_queryhelp_response.py">AirfieldQueryhelpResponse</a></code>
- <code title="get /udl/airfield/tuple">client.airfields.<a href="./src/unifieddatalibrary/resources/airfields.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/airfield_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/airfield_tuple_response.py">AirfieldTupleResponse</a></code>

# AirloadPlans

Types:

```python
from unifieddatalibrary.types import (
    AirloadplanAbridged,
    AirloadPlanCountResponse,
    AirloadPlanQueryhelpResponse,
    AirloadPlanTupleResponse,
)
```

Methods:

- <code title="post /udl/airloadplan">client.airload_plans.<a href="./src/unifieddatalibrary/resources/airload_plans.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/airload_plan_create_params.py">params</a>) -> None</code>
- <code title="get /udl/airloadplan/{id}">client.airload_plans.<a href="./src/unifieddatalibrary/resources/airload_plans.py">retrieve</a>(id, \*\*<a href="src/unifieddatalibrary/types/airload_plan_retrieve_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/shared/airloadplan_full.py">AirloadplanFull</a></code>
- <code title="put /udl/airloadplan/{id}">client.airload_plans.<a href="./src/unifieddatalibrary/resources/airload_plans.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/airload_plan_update_params.py">params</a>) -> None</code>
- <code title="get /udl/airloadplan">client.airload_plans.<a href="./src/unifieddatalibrary/resources/airload_plans.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/airload_plan_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/airloadplan_abridged.py">SyncOffsetPage[AirloadplanAbridged]</a></code>
- <code title="delete /udl/airloadplan/{id}">client.airload_plans.<a href="./src/unifieddatalibrary/resources/airload_plans.py">delete</a>(id) -> None</code>
- <code title="get /udl/airloadplan/count">client.airload_plans.<a href="./src/unifieddatalibrary/resources/airload_plans.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/airload_plan_count_params.py">params</a>) -> str</code>
- <code title="get /udl/airloadplan/queryhelp">client.airload_plans.<a href="./src/unifieddatalibrary/resources/airload_plans.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/airload_plan_queryhelp_response.py">AirloadPlanQueryhelpResponse</a></code>
- <code title="get /udl/airloadplan/tuple">client.airload_plans.<a href="./src/unifieddatalibrary/resources/airload_plans.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/airload_plan_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/airload_plan_tuple_response.py">AirloadPlanTupleResponse</a></code>

# AirspaceControlOrders

Types:

```python
from unifieddatalibrary.types import (
    AirspacecontrolorderAbridged,
    AirspaceControlOrderCountResponse,
    AirspaceControlOrderQueryHelpResponse,
    AirspaceControlOrderTupleResponse,
)
```

Methods:

- <code title="post /udl/airspacecontrolorder">client.airspace_control_orders.<a href="./src/unifieddatalibrary/resources/airspace_control_orders.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/airspace_control_order_create_params.py">params</a>) -> None</code>
- <code title="get /udl/airspacecontrolorder/{id}">client.airspace_control_orders.<a href="./src/unifieddatalibrary/resources/airspace_control_orders.py">retrieve</a>(id, \*\*<a href="src/unifieddatalibrary/types/airspace_control_order_retrieve_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/shared/airspacecontrolorder_full.py">AirspacecontrolorderFull</a></code>
- <code title="get /udl/airspacecontrolorder">client.airspace_control_orders.<a href="./src/unifieddatalibrary/resources/airspace_control_orders.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/airspace_control_order_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/airspacecontrolorder_abridged.py">SyncOffsetPage[AirspacecontrolorderAbridged]</a></code>
- <code title="get /udl/airspacecontrolorder/count">client.airspace_control_orders.<a href="./src/unifieddatalibrary/resources/airspace_control_orders.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/airspace_control_order_count_params.py">params</a>) -> str</code>
- <code title="post /udl/airspacecontrolorder/createBulk">client.airspace_control_orders.<a href="./src/unifieddatalibrary/resources/airspace_control_orders.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/airspace_control_order_create_bulk_params.py">params</a>) -> None</code>
- <code title="get /udl/airspacecontrolorder/queryhelp">client.airspace_control_orders.<a href="./src/unifieddatalibrary/resources/airspace_control_orders.py">query_help</a>() -> <a href="./src/unifieddatalibrary/types/airspace_control_order_query_help_response.py">AirspaceControlOrderQueryHelpResponse</a></code>
- <code title="get /udl/airspacecontrolorder/tuple">client.airspace_control_orders.<a href="./src/unifieddatalibrary/resources/airspace_control_orders.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/airspace_control_order_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/airspace_control_order_tuple_response.py">AirspaceControlOrderTupleResponse</a></code>

# AIs

Types:

```python
from unifieddatalibrary.types import (
    AIsAbridged,
    AICountResponse,
    AIQueryhelpResponse,
    AITupleResponse,
)
```

Methods:

- <code title="get /udl/ais">client.ais.<a href="./src/unifieddatalibrary/resources/ais/ais.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/ai_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/ais_abridged.py">SyncOffsetPage[AIsAbridged]</a></code>
- <code title="get /udl/ais/count">client.ais.<a href="./src/unifieddatalibrary/resources/ais/ais.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/ai_count_params.py">params</a>) -> str</code>
- <code title="post /udl/ais/createBulk">client.ais.<a href="./src/unifieddatalibrary/resources/ais/ais.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/ai_create_bulk_params.py">params</a>) -> None</code>
- <code title="get /udl/ais/queryhelp">client.ais.<a href="./src/unifieddatalibrary/resources/ais/ais.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/ai_queryhelp_response.py">AIQueryhelpResponse</a></code>
- <code title="get /udl/ais/tuple">client.ais.<a href="./src/unifieddatalibrary/resources/ais/ais.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/ai_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/ai_tuple_response.py">AITupleResponse</a></code>

## History

Types:

```python
from unifieddatalibrary.types.ais import HistoryCountResponse
```

Methods:

- <code title="get /udl/ais/history">client.ais.history.<a href="./src/unifieddatalibrary/resources/ais/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/ais/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/shared/ais_full.py">SyncOffsetPage[AIsFull]</a></code>
- <code title="get /udl/ais/history/aodr">client.ais.history.<a href="./src/unifieddatalibrary/resources/ais/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/ais/history_aodr_params.py">params</a>) -> None</code>
- <code title="get /udl/ais/history/count">client.ais.history.<a href="./src/unifieddatalibrary/resources/ais/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/ais/history_count_params.py">params</a>) -> str</code>

# AIsObjects

Methods:

- <code title="post /filedrop/udl-ais">client.ais_objects.<a href="./src/unifieddatalibrary/resources/ais_objects.py">unvalidated_publish</a>(\*\*<a href="src/unifieddatalibrary/types/ais_object_unvalidated_publish_params.py">params</a>) -> None</code>

# AnalyticImagery

Types:

```python
from unifieddatalibrary.types import (
    AnalyticImageryAbridged,
    AnalyticImageryCountResponse,
    AnalyticImageryQueryhelpResponse,
    AnalyticImageryTupleResponse,
)
```

Methods:

- <code title="get /udl/analyticimagery/{id}">client.analytic_imagery.<a href="./src/unifieddatalibrary/resources/analytic_imagery/analytic_imagery.py">retrieve</a>(id, \*\*<a href="src/unifieddatalibrary/types/analytic_imagery_retrieve_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/shared/analytic_imagery_full.py">AnalyticImageryFull</a></code>
- <code title="get /udl/analyticimagery">client.analytic_imagery.<a href="./src/unifieddatalibrary/resources/analytic_imagery/analytic_imagery.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/analytic_imagery_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/analytic_imagery_abridged.py">SyncOffsetPage[AnalyticImageryAbridged]</a></code>
- <code title="get /udl/analyticimagery/count">client.analytic_imagery.<a href="./src/unifieddatalibrary/resources/analytic_imagery/analytic_imagery.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/analytic_imagery_count_params.py">params</a>) -> str</code>
- <code title="get /udl/analyticimagery/getFile/{id}">client.analytic_imagery.<a href="./src/unifieddatalibrary/resources/analytic_imagery/analytic_imagery.py">file_get</a>(id, \*\*<a href="src/unifieddatalibrary/types/analytic_imagery_file_get_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="get /udl/analyticimagery/queryhelp">client.analytic_imagery.<a href="./src/unifieddatalibrary/resources/analytic_imagery/analytic_imagery.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/analytic_imagery_queryhelp_response.py">AnalyticImageryQueryhelpResponse</a></code>
- <code title="get /udl/analyticimagery/tuple">client.analytic_imagery.<a href="./src/unifieddatalibrary/resources/analytic_imagery/analytic_imagery.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/analytic_imagery_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/analytic_imagery_tuple_response.py">AnalyticImageryTupleResponse</a></code>
- <code title="post /filedrop/udl-analyticimagery">client.analytic_imagery.<a href="./src/unifieddatalibrary/resources/analytic_imagery/analytic_imagery.py">unvalidated_publish</a>(\*\*<a href="src/unifieddatalibrary/types/analytic_imagery_unvalidated_publish_params.py">params</a>) -> None</code>

## History

Types:

```python
from unifieddatalibrary.types.analytic_imagery import HistoryCountResponse
```

Methods:

- <code title="get /udl/analyticimagery/history">client.analytic_imagery.history.<a href="./src/unifieddatalibrary/resources/analytic_imagery/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/analytic_imagery/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/analytic_imagery_abridged.py">SyncOffsetPage[AnalyticImageryAbridged]</a></code>
- <code title="get /udl/analyticimagery/history/aodr">client.analytic_imagery.history.<a href="./src/unifieddatalibrary/resources/analytic_imagery/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/analytic_imagery/history_aodr_params.py">params</a>) -> None</code>
- <code title="get /udl/analyticimagery/history/count">client.analytic_imagery.history.<a href="./src/unifieddatalibrary/resources/analytic_imagery/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/analytic_imagery/history_count_params.py">params</a>) -> str</code>

# Antennas

Types:

```python
from unifieddatalibrary.types import (
    AntennaAbridged,
    AntennaCountResponse,
    AntennaQueryhelpResponse,
    AntennaTupleResponse,
)
```

Methods:

- <code title="post /udl/antenna">client.antennas.<a href="./src/unifieddatalibrary/resources/antennas.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/antenna_create_params.py">params</a>) -> None</code>
- <code title="get /udl/antenna/{id}">client.antennas.<a href="./src/unifieddatalibrary/resources/antennas.py">retrieve</a>(id, \*\*<a href="src/unifieddatalibrary/types/antenna_retrieve_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/shared/antenna_full.py">AntennaFull</a></code>
- <code title="put /udl/antenna/{id}">client.antennas.<a href="./src/unifieddatalibrary/resources/antennas.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/antenna_update_params.py">params</a>) -> None</code>
- <code title="get /udl/antenna">client.antennas.<a href="./src/unifieddatalibrary/resources/antennas.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/antenna_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/antenna_abridged.py">SyncOffsetPage[AntennaAbridged]</a></code>
- <code title="delete /udl/antenna/{id}">client.antennas.<a href="./src/unifieddatalibrary/resources/antennas.py">delete</a>(id) -> None</code>
- <code title="get /udl/antenna/count">client.antennas.<a href="./src/unifieddatalibrary/resources/antennas.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/antenna_count_params.py">params</a>) -> str</code>
- <code title="get /udl/antenna/queryhelp">client.antennas.<a href="./src/unifieddatalibrary/resources/antennas.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/antenna_queryhelp_response.py">AntennaQueryhelpResponse</a></code>
- <code title="get /udl/antenna/tuple">client.antennas.<a href="./src/unifieddatalibrary/resources/antennas.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/antenna_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/antenna_tuple_response.py">AntennaTupleResponse</a></code>

# AttitudeData

Types:

```python
from unifieddatalibrary.types import AttitudeDataQueryHelpResponse, AttitudeDataTupleResponse
```

Methods:

- <code title="get /udl/attitudedata/queryhelp">client.attitude_data.<a href="./src/unifieddatalibrary/resources/attitude_data.py">query_help</a>() -> <a href="./src/unifieddatalibrary/types/attitude_data_query_help_response.py">AttitudeDataQueryHelpResponse</a></code>
- <code title="get /udl/attitudedata/tuple">client.attitude_data.<a href="./src/unifieddatalibrary/resources/attitude_data.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/attitude_data_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/attitude_data_tuple_response.py">AttitudeDataTupleResponse</a></code>

# AttitudeSets

Types:

```python
from unifieddatalibrary.types import (
    AttitudesetAbridged,
    AttitudeSetCountResponse,
    AttitudeSetQueryHelpResponse,
    AttitudeSetTupleResponse,
)
```

Methods:

- <code title="post /udl/attitudeset">client.attitude_sets.<a href="./src/unifieddatalibrary/resources/attitude_sets/attitude_sets.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/attitude_set_create_params.py">params</a>) -> None</code>
- <code title="get /udl/attitudeset/{id}">client.attitude_sets.<a href="./src/unifieddatalibrary/resources/attitude_sets/attitude_sets.py">retrieve</a>(id, \*\*<a href="src/unifieddatalibrary/types/attitude_set_retrieve_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/shared/attitudeset_full.py">AttitudesetFull</a></code>
- <code title="get /udl/attitudeset">client.attitude_sets.<a href="./src/unifieddatalibrary/resources/attitude_sets/attitude_sets.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/attitude_set_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/attitudeset_abridged.py">SyncOffsetPage[AttitudesetAbridged]</a></code>
- <code title="get /udl/attitudeset/count">client.attitude_sets.<a href="./src/unifieddatalibrary/resources/attitude_sets/attitude_sets.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/attitude_set_count_params.py">params</a>) -> str</code>
- <code title="get /udl/attitudeset/queryhelp">client.attitude_sets.<a href="./src/unifieddatalibrary/resources/attitude_sets/attitude_sets.py">query_help</a>() -> <a href="./src/unifieddatalibrary/types/attitude_set_query_help_response.py">AttitudeSetQueryHelpResponse</a></code>
- <code title="get /udl/attitudeset/tuple">client.attitude_sets.<a href="./src/unifieddatalibrary/resources/attitude_sets/attitude_sets.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/attitude_set_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/attitude_set_tuple_response.py">AttitudeSetTupleResponse</a></code>
- <code title="post /filedrop/udl-attitudeset">client.attitude_sets.<a href="./src/unifieddatalibrary/resources/attitude_sets/attitude_sets.py">unvalidated_publish</a>(\*\*<a href="src/unifieddatalibrary/types/attitude_set_unvalidated_publish_params.py">params</a>) -> None</code>

## History

Types:

```python
from unifieddatalibrary.types.attitude_sets import HistoryCountResponse
```

Methods:

- <code title="get /udl/attitudeset/history">client.attitude_sets.history.<a href="./src/unifieddatalibrary/resources/attitude_sets/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/attitude_sets/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/shared/attitudeset_full.py">SyncOffsetPage[AttitudesetFull]</a></code>
- <code title="get /udl/attitudeset/history/aodr">client.attitude_sets.history.<a href="./src/unifieddatalibrary/resources/attitude_sets/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/attitude_sets/history_aodr_params.py">params</a>) -> None</code>
- <code title="get /udl/attitudeset/history/count">client.attitude_sets.history.<a href="./src/unifieddatalibrary/resources/attitude_sets/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/attitude_sets/history_count_params.py">params</a>) -> str</code>

# AviationRiskManagement

Types:

```python
from unifieddatalibrary.types import (
    AviationRiskManagementRetrieveResponse,
    AviationRiskManagementListResponse,
    AviationRiskManagementCountResponse,
    AviationRiskManagementQueryHelpResponse,
    AviationRiskManagementTupleResponse,
)
```

Methods:

- <code title="post /udl/aviationriskmanagement">client.aviation_risk_management.<a href="./src/unifieddatalibrary/resources/aviation_risk_management.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/aviation_risk_management_create_params.py">params</a>) -> None</code>
- <code title="get /udl/aviationriskmanagement/{id}">client.aviation_risk_management.<a href="./src/unifieddatalibrary/resources/aviation_risk_management.py">retrieve</a>(id, \*\*<a href="src/unifieddatalibrary/types/aviation_risk_management_retrieve_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/aviation_risk_management_retrieve_response.py">AviationRiskManagementRetrieveResponse</a></code>
- <code title="put /udl/aviationriskmanagement/{id}">client.aviation_risk_management.<a href="./src/unifieddatalibrary/resources/aviation_risk_management.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/aviation_risk_management_update_params.py">params</a>) -> None</code>
- <code title="get /udl/aviationriskmanagement">client.aviation_risk_management.<a href="./src/unifieddatalibrary/resources/aviation_risk_management.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/aviation_risk_management_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/aviation_risk_management_list_response.py">SyncOffsetPage[AviationRiskManagementListResponse]</a></code>
- <code title="delete /udl/aviationriskmanagement/{id}">client.aviation_risk_management.<a href="./src/unifieddatalibrary/resources/aviation_risk_management.py">delete</a>(id) -> None</code>
- <code title="get /udl/aviationriskmanagement/count">client.aviation_risk_management.<a href="./src/unifieddatalibrary/resources/aviation_risk_management.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/aviation_risk_management_count_params.py">params</a>) -> str</code>
- <code title="post /udl/aviationriskmanagement/createBulk">client.aviation_risk_management.<a href="./src/unifieddatalibrary/resources/aviation_risk_management.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/aviation_risk_management_create_bulk_params.py">params</a>) -> None</code>
- <code title="get /udl/aviationriskmanagement/queryhelp">client.aviation_risk_management.<a href="./src/unifieddatalibrary/resources/aviation_risk_management.py">query_help</a>() -> <a href="./src/unifieddatalibrary/types/aviation_risk_management_query_help_response.py">AviationRiskManagementQueryHelpResponse</a></code>
- <code title="get /udl/aviationriskmanagement/tuple">client.aviation_risk_management.<a href="./src/unifieddatalibrary/resources/aviation_risk_management.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/aviation_risk_management_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/aviation_risk_management_tuple_response.py">AviationRiskManagementTupleResponse</a></code>
- <code title="post /filedrop/udl-aviationriskmanagement">client.aviation_risk_management.<a href="./src/unifieddatalibrary/resources/aviation_risk_management.py">unvalidated_publish</a>(\*\*<a href="src/unifieddatalibrary/types/aviation_risk_management_unvalidated_publish_params.py">params</a>) -> None</code>

# Batteries

Types:

```python
from unifieddatalibrary.types import (
    BatteryAbridged,
    BatteryCountResponse,
    BatteryQueryhelpResponse,
    BatteryTupleResponse,
)
```

Methods:

- <code title="post /udl/battery">client.batteries.<a href="./src/unifieddatalibrary/resources/batteries.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/battery_create_params.py">params</a>) -> None</code>
- <code title="get /udl/battery/{id}">client.batteries.<a href="./src/unifieddatalibrary/resources/batteries.py">retrieve</a>(id, \*\*<a href="src/unifieddatalibrary/types/battery_retrieve_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/shared/battery_full.py">BatteryFull</a></code>
- <code title="put /udl/battery/{id}">client.batteries.<a href="./src/unifieddatalibrary/resources/batteries.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/battery_update_params.py">params</a>) -> None</code>
- <code title="get /udl/battery">client.batteries.<a href="./src/unifieddatalibrary/resources/batteries.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/battery_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/battery_abridged.py">SyncOffsetPage[BatteryAbridged]</a></code>
- <code title="delete /udl/battery/{id}">client.batteries.<a href="./src/unifieddatalibrary/resources/batteries.py">delete</a>(id) -> None</code>
- <code title="get /udl/battery/count">client.batteries.<a href="./src/unifieddatalibrary/resources/batteries.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/battery_count_params.py">params</a>) -> str</code>
- <code title="get /udl/battery/queryhelp">client.batteries.<a href="./src/unifieddatalibrary/resources/batteries.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/battery_queryhelp_response.py">BatteryQueryhelpResponse</a></code>
- <code title="get /udl/battery/tuple">client.batteries.<a href="./src/unifieddatalibrary/resources/batteries.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/battery_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/battery_tuple_response.py">BatteryTupleResponse</a></code>

# Batterydetails

Types:

```python
from unifieddatalibrary.types import BatterydetailsAbridged
```

Methods:

- <code title="post /udl/batterydetails">client.batterydetails.<a href="./src/unifieddatalibrary/resources/batterydetails.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/batterydetail_create_params.py">params</a>) -> None</code>
- <code title="get /udl/batterydetails/{id}">client.batterydetails.<a href="./src/unifieddatalibrary/resources/batterydetails.py">retrieve</a>(id, \*\*<a href="src/unifieddatalibrary/types/batterydetail_retrieve_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/shared/batterydetails_full.py">BatterydetailsFull</a></code>
- <code title="put /udl/batterydetails/{id}">client.batterydetails.<a href="./src/unifieddatalibrary/resources/batterydetails.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/batterydetail_update_params.py">params</a>) -> None</code>
- <code title="get /udl/batterydetails">client.batterydetails.<a href="./src/unifieddatalibrary/resources/batterydetails.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/batterydetail_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/batterydetails_abridged.py">SyncOffsetPage[BatterydetailsAbridged]</a></code>
- <code title="delete /udl/batterydetails/{id}">client.batterydetails.<a href="./src/unifieddatalibrary/resources/batterydetails.py">delete</a>(id) -> None</code>

# Beam

Types:

```python
from unifieddatalibrary.types import (
    BeamAbridged,
    BeamCountResponse,
    BeamQueryHelpResponse,
    BeamTupleResponse,
)
```

Methods:

- <code title="post /udl/beam">client.beam.<a href="./src/unifieddatalibrary/resources/beam.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/beam_create_params.py">params</a>) -> None</code>
- <code title="get /udl/beam/{id}">client.beam.<a href="./src/unifieddatalibrary/resources/beam.py">retrieve</a>(id, \*\*<a href="src/unifieddatalibrary/types/beam_retrieve_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/shared/beam_full.py">BeamFull</a></code>
- <code title="put /udl/beam/{id}">client.beam.<a href="./src/unifieddatalibrary/resources/beam.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/beam_update_params.py">params</a>) -> None</code>
- <code title="get /udl/beam">client.beam.<a href="./src/unifieddatalibrary/resources/beam.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/beam_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/beam_abridged.py">SyncOffsetPage[BeamAbridged]</a></code>
- <code title="delete /udl/beam/{id}">client.beam.<a href="./src/unifieddatalibrary/resources/beam.py">delete</a>(id) -> None</code>
- <code title="get /udl/beam/count">client.beam.<a href="./src/unifieddatalibrary/resources/beam.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/beam_count_params.py">params</a>) -> str</code>
- <code title="get /udl/beam/queryhelp">client.beam.<a href="./src/unifieddatalibrary/resources/beam.py">query_help</a>() -> <a href="./src/unifieddatalibrary/types/beam_query_help_response.py">BeamQueryHelpResponse</a></code>
- <code title="get /udl/beam/tuple">client.beam.<a href="./src/unifieddatalibrary/resources/beam.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/beam_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/beam_tuple_response.py">BeamTupleResponse</a></code>

# BeamContours

Types:

```python
from unifieddatalibrary.types import (
    BeamcontourAbridged,
    BeamContourCountResponse,
    BeamContourQueryHelpResponse,
    BeamContourTupleResponse,
)
```

Methods:

- <code title="post /udl/beamcontour">client.beam_contours.<a href="./src/unifieddatalibrary/resources/beam_contours.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/beam_contour_create_params.py">params</a>) -> None</code>
- <code title="get /udl/beamcontour/{id}">client.beam_contours.<a href="./src/unifieddatalibrary/resources/beam_contours.py">retrieve</a>(id, \*\*<a href="src/unifieddatalibrary/types/beam_contour_retrieve_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/shared/beamcontour_full.py">BeamcontourFull</a></code>
- <code title="put /udl/beamcontour/{id}">client.beam_contours.<a href="./src/unifieddatalibrary/resources/beam_contours.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/beam_contour_update_params.py">params</a>) -> None</code>
- <code title="get /udl/beamcontour">client.beam_contours.<a href="./src/unifieddatalibrary/resources/beam_contours.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/beam_contour_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/beamcontour_abridged.py">SyncOffsetPage[BeamcontourAbridged]</a></code>
- <code title="delete /udl/beamcontour/{id}">client.beam_contours.<a href="./src/unifieddatalibrary/resources/beam_contours.py">delete</a>(id) -> None</code>
- <code title="get /udl/beamcontour/count">client.beam_contours.<a href="./src/unifieddatalibrary/resources/beam_contours.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/beam_contour_count_params.py">params</a>) -> str</code>
- <code title="post /udl/beamcontour/createBulk">client.beam_contours.<a href="./src/unifieddatalibrary/resources/beam_contours.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/beam_contour_create_bulk_params.py">params</a>) -> None</code>
- <code title="get /udl/beamcontour/queryhelp">client.beam_contours.<a href="./src/unifieddatalibrary/resources/beam_contours.py">query_help</a>() -> <a href="./src/unifieddatalibrary/types/beam_contour_query_help_response.py">BeamContourQueryHelpResponse</a></code>
- <code title="get /udl/beamcontour/tuple">client.beam_contours.<a href="./src/unifieddatalibrary/resources/beam_contours.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/beam_contour_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/beam_contour_tuple_response.py">BeamContourTupleResponse</a></code>

# Buses

Types:

```python
from unifieddatalibrary.types import (
    BusAbridged,
    BusCountResponse,
    BusQueryHelpResponse,
    BusTupleResponse,
)
```

Methods:

- <code title="post /udl/bus">client.buses.<a href="./src/unifieddatalibrary/resources/buses.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/bus_create_params.py">params</a>) -> None</code>
- <code title="get /udl/bus/{id}">client.buses.<a href="./src/unifieddatalibrary/resources/buses.py">retrieve</a>(id, \*\*<a href="src/unifieddatalibrary/types/bus_retrieve_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/shared/bus_full.py">BusFull</a></code>
- <code title="put /udl/bus/{id}">client.buses.<a href="./src/unifieddatalibrary/resources/buses.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/bus_update_params.py">params</a>) -> None</code>
- <code title="get /udl/bus">client.buses.<a href="./src/unifieddatalibrary/resources/buses.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/bus_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/bus_abridged.py">SyncOffsetPage[BusAbridged]</a></code>
- <code title="delete /udl/bus/{id}">client.buses.<a href="./src/unifieddatalibrary/resources/buses.py">delete</a>(id) -> None</code>
- <code title="get /udl/bus/count">client.buses.<a href="./src/unifieddatalibrary/resources/buses.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/bus_count_params.py">params</a>) -> str</code>
- <code title="get /udl/bus/queryhelp">client.buses.<a href="./src/unifieddatalibrary/resources/buses.py">query_help</a>() -> <a href="./src/unifieddatalibrary/types/bus_query_help_response.py">BusQueryHelpResponse</a></code>
- <code title="get /udl/bus/tuple">client.buses.<a href="./src/unifieddatalibrary/resources/buses.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/bus_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/bus_tuple_response.py">BusTupleResponse</a></code>

# Channels

Types:

```python
from unifieddatalibrary.types import (
    ChannelAbridged,
    ChannelCountResponse,
    ChannelQueryhelpResponse,
    ChannelTupleResponse,
)
```

Methods:

- <code title="post /udl/channel">client.channels.<a href="./src/unifieddatalibrary/resources/channels.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/channel_create_params.py">params</a>) -> None</code>
- <code title="get /udl/channel/{id}">client.channels.<a href="./src/unifieddatalibrary/resources/channels.py">retrieve</a>(id, \*\*<a href="src/unifieddatalibrary/types/channel_retrieve_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/shared/channel_full.py">ChannelFull</a></code>
- <code title="put /udl/channel/{id}">client.channels.<a href="./src/unifieddatalibrary/resources/channels.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/channel_update_params.py">params</a>) -> None</code>
- <code title="get /udl/channel">client.channels.<a href="./src/unifieddatalibrary/resources/channels.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/channel_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/channel_abridged.py">SyncOffsetPage[ChannelAbridged]</a></code>
- <code title="delete /udl/channel/{id}">client.channels.<a href="./src/unifieddatalibrary/resources/channels.py">delete</a>(id) -> None</code>
- <code title="get /udl/channel/count">client.channels.<a href="./src/unifieddatalibrary/resources/channels.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/channel_count_params.py">params</a>) -> str</code>
- <code title="get /udl/channel/queryhelp">client.channels.<a href="./src/unifieddatalibrary/resources/channels.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/channel_queryhelp_response.py">ChannelQueryhelpResponse</a></code>
- <code title="get /udl/channel/tuple">client.channels.<a href="./src/unifieddatalibrary/resources/channels.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/channel_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/channel_tuple_response.py">ChannelTupleResponse</a></code>

# CollectRequests

Types:

```python
from unifieddatalibrary.types import (
    CollectRequestAbridged,
    CollectRequestCountResponse,
    CollectRequestQueryHelpResponse,
    CollectRequestTupleResponse,
)
```

Methods:

- <code title="post /udl/collectrequest">client.collect_requests.<a href="./src/unifieddatalibrary/resources/collect_requests/collect_requests.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/collect_request_create_params.py">params</a>) -> None</code>
- <code title="get /udl/collectrequest/{id}">client.collect_requests.<a href="./src/unifieddatalibrary/resources/collect_requests/collect_requests.py">retrieve</a>(id, \*\*<a href="src/unifieddatalibrary/types/collect_request_retrieve_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/shared/collect_request_full.py">CollectRequestFull</a></code>
- <code title="get /udl/collectrequest">client.collect_requests.<a href="./src/unifieddatalibrary/resources/collect_requests/collect_requests.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/collect_request_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/collect_request_abridged.py">SyncOffsetPage[CollectRequestAbridged]</a></code>
- <code title="get /udl/collectrequest/count">client.collect_requests.<a href="./src/unifieddatalibrary/resources/collect_requests/collect_requests.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/collect_request_count_params.py">params</a>) -> str</code>
- <code title="post /udl/collectrequest/createBulk">client.collect_requests.<a href="./src/unifieddatalibrary/resources/collect_requests/collect_requests.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/collect_request_create_bulk_params.py">params</a>) -> None</code>
- <code title="get /udl/collectrequest/queryhelp">client.collect_requests.<a href="./src/unifieddatalibrary/resources/collect_requests/collect_requests.py">query_help</a>() -> <a href="./src/unifieddatalibrary/types/collect_request_query_help_response.py">CollectRequestQueryHelpResponse</a></code>
- <code title="get /udl/collectrequest/tuple">client.collect_requests.<a href="./src/unifieddatalibrary/resources/collect_requests/collect_requests.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/collect_request_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/collect_request_tuple_response.py">CollectRequestTupleResponse</a></code>
- <code title="post /filedrop/udl-collectrequest">client.collect_requests.<a href="./src/unifieddatalibrary/resources/collect_requests/collect_requests.py">unvalidated_publish</a>(\*\*<a href="src/unifieddatalibrary/types/collect_request_unvalidated_publish_params.py">params</a>) -> None</code>

## History

Types:

```python
from unifieddatalibrary.types.collect_requests import HistoryCountResponse
```

Methods:

- <code title="get /udl/collectrequest/history">client.collect_requests.history.<a href="./src/unifieddatalibrary/resources/collect_requests/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/collect_requests/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/shared/collect_request_full.py">SyncOffsetPage[CollectRequestFull]</a></code>
- <code title="get /udl/collectrequest/history/aodr">client.collect_requests.history.<a href="./src/unifieddatalibrary/resources/collect_requests/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/collect_requests/history_aodr_params.py">params</a>) -> None</code>
- <code title="get /udl/collectrequest/history/count">client.collect_requests.history.<a href="./src/unifieddatalibrary/resources/collect_requests/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/collect_requests/history_count_params.py">params</a>) -> str</code>

# CollectResponses

Types:

```python
from unifieddatalibrary.types import (
    CollectResponseAbridged,
    CollectResponseCountResponse,
    CollectResponseQueryHelpResponse,
)
```

Methods:

- <code title="post /udl/collectresponse">client.collect_responses.<a href="./src/unifieddatalibrary/resources/collect_responses/collect_responses.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/collect_response_create_params.py">params</a>) -> None</code>
- <code title="get /udl/collectresponse/{id}">client.collect_responses.<a href="./src/unifieddatalibrary/resources/collect_responses/collect_responses.py">retrieve</a>(id, \*\*<a href="src/unifieddatalibrary/types/collect_response_retrieve_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/shared/collect_response_full.py">CollectResponseFull</a></code>
- <code title="get /udl/collectresponse">client.collect_responses.<a href="./src/unifieddatalibrary/resources/collect_responses/collect_responses.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/collect_response_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/collect_response_abridged.py">SyncOffsetPage[CollectResponseAbridged]</a></code>
- <code title="get /udl/collectresponse/count">client.collect_responses.<a href="./src/unifieddatalibrary/resources/collect_responses/collect_responses.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/collect_response_count_params.py">params</a>) -> str</code>
- <code title="post /udl/collectresponse/createBulk">client.collect_responses.<a href="./src/unifieddatalibrary/resources/collect_responses/collect_responses.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/collect_response_create_bulk_params.py">params</a>) -> None</code>
- <code title="get /udl/collectresponse/queryhelp">client.collect_responses.<a href="./src/unifieddatalibrary/resources/collect_responses/collect_responses.py">query_help</a>() -> <a href="./src/unifieddatalibrary/types/collect_response_query_help_response.py">CollectResponseQueryHelpResponse</a></code>
- <code title="post /filedrop/udl-collectresponse">client.collect_responses.<a href="./src/unifieddatalibrary/resources/collect_responses/collect_responses.py">unvalidated_publish</a>(\*\*<a href="src/unifieddatalibrary/types/collect_response_unvalidated_publish_params.py">params</a>) -> None</code>

## History

Types:

```python
from unifieddatalibrary.types.collect_responses import HistoryCountResponse
```

Methods:

- <code title="get /udl/collectresponse/history">client.collect_responses.history.<a href="./src/unifieddatalibrary/resources/collect_responses/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/collect_responses/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/shared/collect_response_full.py">SyncOffsetPage[CollectResponseFull]</a></code>
- <code title="get /udl/collectresponse/history/aodr">client.collect_responses.history.<a href="./src/unifieddatalibrary/resources/collect_responses/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/collect_responses/history_aodr_params.py">params</a>) -> None</code>
- <code title="get /udl/collectresponse/history/count">client.collect_responses.history.<a href="./src/unifieddatalibrary/resources/collect_responses/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/collect_responses/history_count_params.py">params</a>) -> str</code>

## Tuple

Methods:

- <code title="get /udl/collectresponse/tuple">client.collect_responses.tuple.<a href="./src/unifieddatalibrary/resources/collect_responses/tuple.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/collect_responses/tuple_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/shared/collect_response_full.py">SyncOffsetPage[CollectResponseFull]</a></code>

# Comm

Types:

```python
from unifieddatalibrary.types import (
    CommAbridged,
    CommCountResponse,
    CommQueryhelpResponse,
    CommTupleResponse,
)
```

Methods:

- <code title="post /udl/comm">client.comm.<a href="./src/unifieddatalibrary/resources/comm.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/comm_create_params.py">params</a>) -> None</code>
- <code title="get /udl/comm/{id}">client.comm.<a href="./src/unifieddatalibrary/resources/comm.py">retrieve</a>(id, \*\*<a href="src/unifieddatalibrary/types/comm_retrieve_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/shared/comm_full.py">CommFull</a></code>
- <code title="put /udl/comm/{id}">client.comm.<a href="./src/unifieddatalibrary/resources/comm.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/comm_update_params.py">params</a>) -> None</code>
- <code title="get /udl/comm">client.comm.<a href="./src/unifieddatalibrary/resources/comm.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/comm_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/comm_abridged.py">SyncOffsetPage[CommAbridged]</a></code>
- <code title="delete /udl/comm/{id}">client.comm.<a href="./src/unifieddatalibrary/resources/comm.py">delete</a>(id) -> None</code>
- <code title="get /udl/comm/count">client.comm.<a href="./src/unifieddatalibrary/resources/comm.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/comm_count_params.py">params</a>) -> str</code>
- <code title="get /udl/comm/queryhelp">client.comm.<a href="./src/unifieddatalibrary/resources/comm.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/comm_queryhelp_response.py">CommQueryhelpResponse</a></code>
- <code title="get /udl/comm/tuple">client.comm.<a href="./src/unifieddatalibrary/resources/comm.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/comm_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/comm_tuple_response.py">CommTupleResponse</a></code>

# Conjunctions

Types:

```python
from unifieddatalibrary.types import (
    ConjunctionAbridged,
    ConjunctionCountResponse,
    ConjunctionGetHistoryResponse,
    ConjunctionQueryhelpResponse,
    ConjunctionTupleResponse,
)
```

Methods:

- <code title="get /udl/conjunction/{id}">client.conjunctions.<a href="./src/unifieddatalibrary/resources/conjunctions/conjunctions.py">retrieve</a>(id, \*\*<a href="src/unifieddatalibrary/types/conjunction_retrieve_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/shared/conjunction_full.py">ConjunctionFull</a></code>
- <code title="get /udl/conjunction">client.conjunctions.<a href="./src/unifieddatalibrary/resources/conjunctions/conjunctions.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/conjunction_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/conjunction_abridged.py">SyncOffsetPage[ConjunctionAbridged]</a></code>
- <code title="get /udl/conjunction/count">client.conjunctions.<a href="./src/unifieddatalibrary/resources/conjunctions/conjunctions.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/conjunction_count_params.py">params</a>) -> str</code>
- <code title="post /udl/conjunction">client.conjunctions.<a href="./src/unifieddatalibrary/resources/conjunctions/conjunctions.py">create_udl</a>(\*\*<a href="src/unifieddatalibrary/types/conjunction_create_udl_params.py">params</a>) -> None</code>
- <code title="post /udl/conjunction/createBulk">client.conjunctions.<a href="./src/unifieddatalibrary/resources/conjunctions/conjunctions.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/conjunction_create_bulk_params.py">params</a>) -> None</code>
- <code title="get /udl/conjunction/history">client.conjunctions.<a href="./src/unifieddatalibrary/resources/conjunctions/conjunctions.py">get_history</a>(\*\*<a href="src/unifieddatalibrary/types/conjunction_get_history_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/conjunction_get_history_response.py">ConjunctionGetHistoryResponse</a></code>
- <code title="get /udl/conjunction/queryhelp">client.conjunctions.<a href="./src/unifieddatalibrary/resources/conjunctions/conjunctions.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/conjunction_queryhelp_response.py">ConjunctionQueryhelpResponse</a></code>
- <code title="get /udl/conjunction/tuple">client.conjunctions.<a href="./src/unifieddatalibrary/resources/conjunctions/conjunctions.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/conjunction_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/conjunction_tuple_response.py">ConjunctionTupleResponse</a></code>
- <code title="post /filedrop/udl-conjunction">client.conjunctions.<a href="./src/unifieddatalibrary/resources/conjunctions/conjunctions.py">unvalidated_publish</a>(\*\*<a href="src/unifieddatalibrary/types/conjunction_unvalidated_publish_params.py">params</a>) -> None</code>
- <code title="post /filedrop/cdms">client.conjunctions.<a href="./src/unifieddatalibrary/resources/conjunctions/conjunctions.py">upload_conjunction_data_message</a>(file_content, \*\*<a href="src/unifieddatalibrary/types/conjunction_upload_conjunction_data_message_params.py">params</a>) -> None</code>

## History

Types:

```python
from unifieddatalibrary.types.conjunctions import HistoryCountResponse
```

Methods:

- <code title="get /udl/conjunction/history/aodr">client.conjunctions.history.<a href="./src/unifieddatalibrary/resources/conjunctions/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/conjunctions/history_aodr_params.py">params</a>) -> None</code>
- <code title="get /udl/conjunction/history/count">client.conjunctions.history.<a href="./src/unifieddatalibrary/resources/conjunctions/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/conjunctions/history_count_params.py">params</a>) -> str</code>

# Cots

Methods:

- <code title="post /udl/cot">client.cots.<a href="./src/unifieddatalibrary/resources/cots.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/cot_create_params.py">params</a>) -> None</code>

# Countries

Types:

```python
from unifieddatalibrary.types import (
    CountryAbridged,
    CountryCountResponse,
    CountryQueryhelpResponse,
    CountryTupleResponse,
)
```

Methods:

- <code title="post /udl/country">client.countries.<a href="./src/unifieddatalibrary/resources/countries.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/country_create_params.py">params</a>) -> None</code>
- <code title="get /udl/country/{code}">client.countries.<a href="./src/unifieddatalibrary/resources/countries.py">retrieve</a>(code, \*\*<a href="src/unifieddatalibrary/types/country_retrieve_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/shared/country_full.py">CountryFull</a></code>
- <code title="put /udl/country/{code}">client.countries.<a href="./src/unifieddatalibrary/resources/countries.py">update</a>(path_code, \*\*<a href="src/unifieddatalibrary/types/country_update_params.py">params</a>) -> None</code>
- <code title="get /udl/country">client.countries.<a href="./src/unifieddatalibrary/resources/countries.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/country_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/country_abridged.py">SyncOffsetPage[CountryAbridged]</a></code>
- <code title="delete /udl/country/{code}">client.countries.<a href="./src/unifieddatalibrary/resources/countries.py">delete</a>(code) -> None</code>
- <code title="get /udl/country/count">client.countries.<a href="./src/unifieddatalibrary/resources/countries.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/country_count_params.py">params</a>) -> str</code>
- <code title="get /udl/country/queryhelp">client.countries.<a href="./src/unifieddatalibrary/resources/countries.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/country_queryhelp_response.py">CountryQueryhelpResponse</a></code>
- <code title="get /udl/country/tuple">client.countries.<a href="./src/unifieddatalibrary/resources/countries.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/country_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/country_tuple_response.py">CountryTupleResponse</a></code>

# Crew

Types:

```python
from unifieddatalibrary.types import (
    CrewAbridged,
    CrewCountResponse,
    CrewQueryhelpResponse,
    CrewTupleResponse,
)
```

Methods:

- <code title="post /udl/crew">client.crew.<a href="./src/unifieddatalibrary/resources/crew.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/crew_create_params.py">params</a>) -> None</code>
- <code title="get /udl/crew/{id}">client.crew.<a href="./src/unifieddatalibrary/resources/crew.py">retrieve</a>(id, \*\*<a href="src/unifieddatalibrary/types/crew_retrieve_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/shared/crew_full.py">CrewFull</a></code>
- <code title="put /udl/crew/{id}">client.crew.<a href="./src/unifieddatalibrary/resources/crew.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/crew_update_params.py">params</a>) -> None</code>
- <code title="get /udl/crew">client.crew.<a href="./src/unifieddatalibrary/resources/crew.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/crew_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/crew_abridged.py">SyncOffsetPage[CrewAbridged]</a></code>
- <code title="get /udl/crew/count">client.crew.<a href="./src/unifieddatalibrary/resources/crew.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/crew_count_params.py">params</a>) -> str</code>
- <code title="get /udl/crew/queryhelp">client.crew.<a href="./src/unifieddatalibrary/resources/crew.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/crew_queryhelp_response.py">CrewQueryhelpResponse</a></code>
- <code title="get /udl/crew/tuple">client.crew.<a href="./src/unifieddatalibrary/resources/crew.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/crew_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/crew_tuple_response.py">CrewTupleResponse</a></code>
- <code title="post /filedrop/udl-crew">client.crew.<a href="./src/unifieddatalibrary/resources/crew.py">unvalidated_publish</a>(\*\*<a href="src/unifieddatalibrary/types/crew_unvalidated_publish_params.py">params</a>) -> None</code>

# Deconflictset

Types:

```python
from unifieddatalibrary.types import (
    DeconflictsetListResponse,
    DeconflictsetCountResponse,
    DeconflictsetGetResponse,
    DeconflictsetQueryhelpResponse,
    DeconflictsetTupleResponse,
)
```

Methods:

- <code title="post /udl/deconflictset">client.deconflictset.<a href="./src/unifieddatalibrary/resources/deconflictset/deconflictset.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/deconflictset_create_params.py">params</a>) -> None</code>
- <code title="get /udl/deconflictset">client.deconflictset.<a href="./src/unifieddatalibrary/resources/deconflictset/deconflictset.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/deconflictset_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/deconflictset_list_response.py">SyncOffsetPage[DeconflictsetListResponse]</a></code>
- <code title="get /udl/deconflictset/count">client.deconflictset.<a href="./src/unifieddatalibrary/resources/deconflictset/deconflictset.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/deconflictset_count_params.py">params</a>) -> str</code>
- <code title="get /udl/deconflictset/{id}">client.deconflictset.<a href="./src/unifieddatalibrary/resources/deconflictset/deconflictset.py">get</a>(id, \*\*<a href="src/unifieddatalibrary/types/deconflictset_get_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/deconflictset_get_response.py">DeconflictsetGetResponse</a></code>
- <code title="get /udl/deconflictset/queryhelp">client.deconflictset.<a href="./src/unifieddatalibrary/resources/deconflictset/deconflictset.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/deconflictset_queryhelp_response.py">DeconflictsetQueryhelpResponse</a></code>
- <code title="get /udl/deconflictset/tuple">client.deconflictset.<a href="./src/unifieddatalibrary/resources/deconflictset/deconflictset.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/deconflictset_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/deconflictset_tuple_response.py">DeconflictsetTupleResponse</a></code>
- <code title="post /filedrop/udl-deconflictset">client.deconflictset.<a href="./src/unifieddatalibrary/resources/deconflictset/deconflictset.py">unvalidated_publish</a>(\*\*<a href="src/unifieddatalibrary/types/deconflictset_unvalidated_publish_params.py">params</a>) -> None</code>

## History

Types:

```python
from unifieddatalibrary.types.deconflictset import HistoryListResponse, HistoryCountResponse
```

Methods:

- <code title="get /udl/deconflictset/history">client.deconflictset.history.<a href="./src/unifieddatalibrary/resources/deconflictset/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/deconflictset/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/deconflictset/history_list_response.py">SyncOffsetPage[HistoryListResponse]</a></code>
- <code title="get /udl/deconflictset/history/aodr">client.deconflictset.history.<a href="./src/unifieddatalibrary/resources/deconflictset/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/deconflictset/history_aodr_params.py">params</a>) -> None</code>
- <code title="get /udl/deconflictset/history/count">client.deconflictset.history.<a href="./src/unifieddatalibrary/resources/deconflictset/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/deconflictset/history_count_params.py">params</a>) -> str</code>

# DiffOfArrival

Types:

```python
from unifieddatalibrary.types import DiffOfArrivalQueryhelpResponse, DiffOfArrivalTupleResponse
```

Methods:

- <code title="get /udl/diffofarrival/{id}">client.diff_of_arrival.<a href="./src/unifieddatalibrary/resources/diff_of_arrival/diff_of_arrival.py">retrieve</a>(id, \*\*<a href="src/unifieddatalibrary/types/diff_of_arrival_retrieve_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/tdoa_fdoa/diffofarrival_full.py">DiffofarrivalFull</a></code>
- <code title="get /udl/diffofarrival/queryhelp">client.diff_of_arrival.<a href="./src/unifieddatalibrary/resources/diff_of_arrival/diff_of_arrival.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/diff_of_arrival_queryhelp_response.py">DiffOfArrivalQueryhelpResponse</a></code>
- <code title="get /udl/diffofarrival/tuple">client.diff_of_arrival.<a href="./src/unifieddatalibrary/resources/diff_of_arrival/diff_of_arrival.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/diff_of_arrival_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/diff_of_arrival_tuple_response.py">DiffOfArrivalTupleResponse</a></code>
- <code title="post /filedrop/udl-diffofarrival">client.diff_of_arrival.<a href="./src/unifieddatalibrary/resources/diff_of_arrival/diff_of_arrival.py">unvalidated_publish</a>(\*\*<a href="src/unifieddatalibrary/types/diff_of_arrival_unvalidated_publish_params.py">params</a>) -> None</code>

## History

Types:

```python
from unifieddatalibrary.types.diff_of_arrival import HistoryCountResponse
```

Methods:

- <code title="get /udl/diffofarrival/history/count">client.diff_of_arrival.history.<a href="./src/unifieddatalibrary/resources/diff_of_arrival/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/diff_of_arrival/history_count_params.py">params</a>) -> str</code>

# DiplomaticClearance

Types:

```python
from unifieddatalibrary.types import (
    DiplomaticClearanceCountResponse,
    DiplomaticClearanceQueryhelpResponse,
    DiplomaticClearanceTupleResponse,
)
```

Methods:

- <code title="post /udl/diplomaticclearance">client.diplomatic_clearance.<a href="./src/unifieddatalibrary/resources/diplomatic_clearance/diplomatic_clearance.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/diplomatic_clearance_create_params.py">params</a>) -> None</code>
- <code title="get /udl/diplomaticclearance/{id}">client.diplomatic_clearance.<a href="./src/unifieddatalibrary/resources/diplomatic_clearance/diplomatic_clearance.py">retrieve</a>(id, \*\*<a href="src/unifieddatalibrary/types/diplomatic_clearance_retrieve_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/shared/diplomaticclearance_full.py">DiplomaticclearanceFull</a></code>
- <code title="put /udl/diplomaticclearance/{id}">client.diplomatic_clearance.<a href="./src/unifieddatalibrary/resources/diplomatic_clearance/diplomatic_clearance.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/diplomatic_clearance_update_params.py">params</a>) -> None</code>
- <code title="get /udl/diplomaticclearance">client.diplomatic_clearance.<a href="./src/unifieddatalibrary/resources/diplomatic_clearance/diplomatic_clearance.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/diplomatic_clearance_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/air_operations/diplomaticclearance_abridged.py">SyncOffsetPage[DiplomaticclearanceAbridged]</a></code>
- <code title="delete /udl/diplomaticclearance/{id}">client.diplomatic_clearance.<a href="./src/unifieddatalibrary/resources/diplomatic_clearance/diplomatic_clearance.py">delete</a>(id) -> None</code>
- <code title="get /udl/diplomaticclearance/count">client.diplomatic_clearance.<a href="./src/unifieddatalibrary/resources/diplomatic_clearance/diplomatic_clearance.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/diplomatic_clearance_count_params.py">params</a>) -> str</code>
- <code title="post /udl/diplomaticclearance/createBulk">client.diplomatic_clearance.<a href="./src/unifieddatalibrary/resources/diplomatic_clearance/diplomatic_clearance.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/diplomatic_clearance_create_bulk_params.py">params</a>) -> None</code>
- <code title="get /udl/diplomaticclearance/queryhelp">client.diplomatic_clearance.<a href="./src/unifieddatalibrary/resources/diplomatic_clearance/diplomatic_clearance.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/diplomatic_clearance_queryhelp_response.py">DiplomaticClearanceQueryhelpResponse</a></code>
- <code title="get /udl/diplomaticclearance/tuple">client.diplomatic_clearance.<a href="./src/unifieddatalibrary/resources/diplomatic_clearance/diplomatic_clearance.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/diplomatic_clearance_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/diplomatic_clearance_tuple_response.py">DiplomaticClearanceTupleResponse</a></code>

## Country

Types:

```python
from unifieddatalibrary.types.diplomatic_clearance import (
    CountryRetrieveResponse,
    CountryListResponse,
    CountryCountResponse,
    CountryQueryHelpResponse,
    CountryTupleResponse,
)
```

Methods:

- <code title="post /udl/diplomaticclearancecountry">client.diplomatic_clearance.country.<a href="./src/unifieddatalibrary/resources/diplomatic_clearance/country.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/diplomatic_clearance/country_create_params.py">params</a>) -> None</code>
- <code title="get /udl/diplomaticclearancecountry/{id}">client.diplomatic_clearance.country.<a href="./src/unifieddatalibrary/resources/diplomatic_clearance/country.py">retrieve</a>(id, \*\*<a href="src/unifieddatalibrary/types/diplomatic_clearance/country_retrieve_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/diplomatic_clearance/country_retrieve_response.py">CountryRetrieveResponse</a></code>
- <code title="put /udl/diplomaticclearancecountry/{id}">client.diplomatic_clearance.country.<a href="./src/unifieddatalibrary/resources/diplomatic_clearance/country.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/diplomatic_clearance/country_update_params.py">params</a>) -> None</code>
- <code title="get /udl/diplomaticclearancecountry">client.diplomatic_clearance.country.<a href="./src/unifieddatalibrary/resources/diplomatic_clearance/country.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/diplomatic_clearance/country_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/diplomatic_clearance/country_list_response.py">SyncOffsetPage[CountryListResponse]</a></code>
- <code title="delete /udl/diplomaticclearancecountry/{id}">client.diplomatic_clearance.country.<a href="./src/unifieddatalibrary/resources/diplomatic_clearance/country.py">delete</a>(id) -> None</code>
- <code title="get /udl/diplomaticclearancecountry/count">client.diplomatic_clearance.country.<a href="./src/unifieddatalibrary/resources/diplomatic_clearance/country.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/diplomatic_clearance/country_count_params.py">params</a>) -> str</code>
- <code title="post /udl/diplomaticclearancecountry/createBulk">client.diplomatic_clearance.country.<a href="./src/unifieddatalibrary/resources/diplomatic_clearance/country.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/diplomatic_clearance/country_create_bulk_params.py">params</a>) -> None</code>
- <code title="get /udl/diplomaticclearancecountry/queryhelp">client.diplomatic_clearance.country.<a href="./src/unifieddatalibrary/resources/diplomatic_clearance/country.py">query_help</a>() -> <a href="./src/unifieddatalibrary/types/diplomatic_clearance/country_query_help_response.py">CountryQueryHelpResponse</a></code>
- <code title="get /udl/diplomaticclearancecountry/tuple">client.diplomatic_clearance.country.<a href="./src/unifieddatalibrary/resources/diplomatic_clearance/country.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/diplomatic_clearance/country_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/diplomatic_clearance/country_tuple_response.py">CountryTupleResponse</a></code>
- <code title="post /filedrop/udl-diplomaticclearancecountry">client.diplomatic_clearance.country.<a href="./src/unifieddatalibrary/resources/diplomatic_clearance/country.py">unvalidated_publish</a>(\*\*<a href="src/unifieddatalibrary/types/diplomatic_clearance/country_unvalidated_publish_params.py">params</a>) -> None</code>

## History

Types:

```python
from unifieddatalibrary.types.diplomatic_clearance import HistoryCountResponse
```

Methods:

- <code title="get /udl/diplomaticclearance/history">client.diplomatic_clearance.history.<a href="./src/unifieddatalibrary/resources/diplomatic_clearance/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/diplomatic_clearance/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/shared/diplomaticclearance_full.py">SyncOffsetPage[DiplomaticclearanceFull]</a></code>
- <code title="get /udl/diplomaticclearance/history/aodr">client.diplomatic_clearance.history.<a href="./src/unifieddatalibrary/resources/diplomatic_clearance/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/diplomatic_clearance/history_aodr_params.py">params</a>) -> None</code>
- <code title="get /udl/diplomaticclearance/history/count">client.diplomatic_clearance.history.<a href="./src/unifieddatalibrary/resources/diplomatic_clearance/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/diplomatic_clearance/history_count_params.py">params</a>) -> str</code>

# DriftHistory

Types:

```python
from unifieddatalibrary.types import (
    DriftHistoryCountResponse,
    DriftHistoryQueryhelpResponse,
    DriftHistoryTupleResponse,
)
```

Methods:

- <code title="get /udl/drifthistory/{id}">client.drift_history.<a href="./src/unifieddatalibrary/resources/drift_history.py">retrieve</a>(id, \*\*<a href="src/unifieddatalibrary/types/drift_history_retrieve_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/shared/drift_history_full.py">DriftHistoryFull</a></code>
- <code title="get /udl/drifthistory">client.drift_history.<a href="./src/unifieddatalibrary/resources/drift_history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/drift_history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/shared/drift_history_abridged.py">SyncOffsetPage[DriftHistoryAbridged]</a></code>
- <code title="get /udl/drifthistory/count">client.drift_history.<a href="./src/unifieddatalibrary/resources/drift_history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/drift_history_count_params.py">params</a>) -> str</code>
- <code title="get /udl/drifthistory/queryhelp">client.drift_history.<a href="./src/unifieddatalibrary/resources/drift_history.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/drift_history_queryhelp_response.py">DriftHistoryQueryhelpResponse</a></code>
- <code title="get /udl/drifthistory/tuple">client.drift_history.<a href="./src/unifieddatalibrary/resources/drift_history.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/drift_history_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/drift_history_tuple_response.py">DriftHistoryTupleResponse</a></code>

# Dropzone

Types:

```python
from unifieddatalibrary.types import (
    DropzoneRetrieveResponse,
    DropzoneListResponse,
    DropzoneCountResponse,
    DropzoneQueryHelpResponse,
    DropzoneTupleResponse,
)
```

Methods:

- <code title="post /udl/dropzone">client.dropzone.<a href="./src/unifieddatalibrary/resources/dropzone.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/dropzone_create_params.py">params</a>) -> None</code>
- <code title="get /udl/dropzone/{id}">client.dropzone.<a href="./src/unifieddatalibrary/resources/dropzone.py">retrieve</a>(id, \*\*<a href="src/unifieddatalibrary/types/dropzone_retrieve_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/dropzone_retrieve_response.py">DropzoneRetrieveResponse</a></code>
- <code title="put /udl/dropzone/{id}">client.dropzone.<a href="./src/unifieddatalibrary/resources/dropzone.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/dropzone_update_params.py">params</a>) -> None</code>
- <code title="get /udl/dropzone">client.dropzone.<a href="./src/unifieddatalibrary/resources/dropzone.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/dropzone_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/dropzone_list_response.py">SyncOffsetPage[DropzoneListResponse]</a></code>
- <code title="delete /udl/dropzone/{id}">client.dropzone.<a href="./src/unifieddatalibrary/resources/dropzone.py">delete</a>(id) -> None</code>
- <code title="get /udl/dropzone/count">client.dropzone.<a href="./src/unifieddatalibrary/resources/dropzone.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/dropzone_count_params.py">params</a>) -> str</code>
- <code title="post /udl/dropzone/createBulk">client.dropzone.<a href="./src/unifieddatalibrary/resources/dropzone.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/dropzone_create_bulk_params.py">params</a>) -> None</code>
- <code title="get /udl/dropzone/queryhelp">client.dropzone.<a href="./src/unifieddatalibrary/resources/dropzone.py">query_help</a>() -> <a href="./src/unifieddatalibrary/types/dropzone_query_help_response.py">DropzoneQueryHelpResponse</a></code>
- <code title="get /udl/dropzone/tuple">client.dropzone.<a href="./src/unifieddatalibrary/resources/dropzone.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/dropzone_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/dropzone_tuple_response.py">DropzoneTupleResponse</a></code>
- <code title="post /filedrop/udl-dropzone">client.dropzone.<a href="./src/unifieddatalibrary/resources/dropzone.py">unvalidated_publish</a>(\*\*<a href="src/unifieddatalibrary/types/dropzone_unvalidated_publish_params.py">params</a>) -> None</code>

# Ecpedr

Types:

```python
from unifieddatalibrary.types import (
    EcpedrListResponse,
    EcpedrCountResponse,
    EcpedrQueryhelpResponse,
    EcpedrTupleResponse,
)
```

Methods:

- <code title="post /udl/ecpedr">client.ecpedr.<a href="./src/unifieddatalibrary/resources/ecpedr/ecpedr.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/ecpedr_create_params.py">params</a>) -> None</code>
- <code title="get /udl/ecpedr">client.ecpedr.<a href="./src/unifieddatalibrary/resources/ecpedr/ecpedr.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/ecpedr_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/ecpedr_list_response.py">SyncOffsetPage[EcpedrListResponse]</a></code>
- <code title="get /udl/ecpedr/count">client.ecpedr.<a href="./src/unifieddatalibrary/resources/ecpedr/ecpedr.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/ecpedr_count_params.py">params</a>) -> str</code>
- <code title="post /udl/ecpedr/createBulk">client.ecpedr.<a href="./src/unifieddatalibrary/resources/ecpedr/ecpedr.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/ecpedr_create_bulk_params.py">params</a>) -> None</code>
- <code title="get /udl/ecpedr/queryhelp">client.ecpedr.<a href="./src/unifieddatalibrary/resources/ecpedr/ecpedr.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/ecpedr_queryhelp_response.py">EcpedrQueryhelpResponse</a></code>
- <code title="get /udl/ecpedr/tuple">client.ecpedr.<a href="./src/unifieddatalibrary/resources/ecpedr/ecpedr.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/ecpedr_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/ecpedr_tuple_response.py">EcpedrTupleResponse</a></code>
- <code title="post /filedrop/udl-ecpedr">client.ecpedr.<a href="./src/unifieddatalibrary/resources/ecpedr/ecpedr.py">unvalidated_publish</a>(\*\*<a href="src/unifieddatalibrary/types/ecpedr_unvalidated_publish_params.py">params</a>) -> None</code>

## History

Types:

```python
from unifieddatalibrary.types.ecpedr import HistoryListResponse, HistoryCountResponse
```

Methods:

- <code title="get /udl/ecpedr/history">client.ecpedr.history.<a href="./src/unifieddatalibrary/resources/ecpedr/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/ecpedr/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/ecpedr/history_list_response.py">SyncOffsetPage[HistoryListResponse]</a></code>
- <code title="get /udl/ecpedr/history/aodr">client.ecpedr.history.<a href="./src/unifieddatalibrary/resources/ecpedr/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/ecpedr/history_aodr_params.py">params</a>) -> None</code>
- <code title="get /udl/ecpedr/history/count">client.ecpedr.history.<a href="./src/unifieddatalibrary/resources/ecpedr/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/ecpedr/history_count_params.py">params</a>) -> str</code>

# EffectRequests

Types:

```python
from unifieddatalibrary.types import (
    EffectRequestRetrieveResponse,
    EffectRequestListResponse,
    EffectRequestCountResponse,
    EffectRequestQueryHelpResponse,
    EffectRequestTupleResponse,
)
```

Methods:

- <code title="post /udl/effectrequest">client.effect_requests.<a href="./src/unifieddatalibrary/resources/effect_requests/effect_requests.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/effect_request_create_params.py">params</a>) -> None</code>
- <code title="get /udl/effectrequest/{id}">client.effect_requests.<a href="./src/unifieddatalibrary/resources/effect_requests/effect_requests.py">retrieve</a>(id, \*\*<a href="src/unifieddatalibrary/types/effect_request_retrieve_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/effect_request_retrieve_response.py">EffectRequestRetrieveResponse</a></code>
- <code title="get /udl/effectrequest">client.effect_requests.<a href="./src/unifieddatalibrary/resources/effect_requests/effect_requests.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/effect_request_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/effect_request_list_response.py">SyncOffsetPage[EffectRequestListResponse]</a></code>
- <code title="get /udl/effectrequest/count">client.effect_requests.<a href="./src/unifieddatalibrary/resources/effect_requests/effect_requests.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/effect_request_count_params.py">params</a>) -> str</code>
- <code title="post /udl/effectrequest/createBulk">client.effect_requests.<a href="./src/unifieddatalibrary/resources/effect_requests/effect_requests.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/effect_request_create_bulk_params.py">params</a>) -> None</code>
- <code title="get /udl/effectrequest/queryhelp">client.effect_requests.<a href="./src/unifieddatalibrary/resources/effect_requests/effect_requests.py">query_help</a>() -> <a href="./src/unifieddatalibrary/types/effect_request_query_help_response.py">EffectRequestQueryHelpResponse</a></code>
- <code title="get /udl/effectrequest/tuple">client.effect_requests.<a href="./src/unifieddatalibrary/resources/effect_requests/effect_requests.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/effect_request_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/effect_request_tuple_response.py">EffectRequestTupleResponse</a></code>
- <code title="post /filedrop/udl-effectrequest">client.effect_requests.<a href="./src/unifieddatalibrary/resources/effect_requests/effect_requests.py">unvalidated_publish</a>(\*\*<a href="src/unifieddatalibrary/types/effect_request_unvalidated_publish_params.py">params</a>) -> None</code>

## History

Types:

```python
from unifieddatalibrary.types.effect_requests import HistoryListResponse, HistoryCountResponse
```

Methods:

- <code title="get /udl/effectrequest/history">client.effect_requests.history.<a href="./src/unifieddatalibrary/resources/effect_requests/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/effect_requests/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/effect_requests/history_list_response.py">SyncOffsetPage[HistoryListResponse]</a></code>
- <code title="get /udl/effectrequest/history/aodr">client.effect_requests.history.<a href="./src/unifieddatalibrary/resources/effect_requests/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/effect_requests/history_aodr_params.py">params</a>) -> None</code>
- <code title="get /udl/effectrequest/history/count">client.effect_requests.history.<a href="./src/unifieddatalibrary/resources/effect_requests/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/effect_requests/history_count_params.py">params</a>) -> str</code>

# EffectResponses

Types:

```python
from unifieddatalibrary.types import (
    EffectResponseActionsListFull,
    EffectResponseMetricsFull,
    EffectResponseRetrieveResponse,
    EffectResponseListResponse,
    EffectResponseCountResponse,
    EffectResponseQueryHelpResponse,
    EffectResponseTupleResponse,
)
```

Methods:

- <code title="post /udl/effectresponse">client.effect_responses.<a href="./src/unifieddatalibrary/resources/effect_responses/effect_responses.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/effect_response_create_params.py">params</a>) -> None</code>
- <code title="get /udl/effectresponse/{id}">client.effect_responses.<a href="./src/unifieddatalibrary/resources/effect_responses/effect_responses.py">retrieve</a>(id, \*\*<a href="src/unifieddatalibrary/types/effect_response_retrieve_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/effect_response_retrieve_response.py">EffectResponseRetrieveResponse</a></code>
- <code title="get /udl/effectresponse">client.effect_responses.<a href="./src/unifieddatalibrary/resources/effect_responses/effect_responses.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/effect_response_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/effect_response_list_response.py">SyncOffsetPage[EffectResponseListResponse]</a></code>
- <code title="get /udl/effectresponse/count">client.effect_responses.<a href="./src/unifieddatalibrary/resources/effect_responses/effect_responses.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/effect_response_count_params.py">params</a>) -> str</code>
- <code title="post /udl/effectresponse/createBulk">client.effect_responses.<a href="./src/unifieddatalibrary/resources/effect_responses/effect_responses.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/effect_response_create_bulk_params.py">params</a>) -> None</code>
- <code title="get /udl/effectresponse/queryhelp">client.effect_responses.<a href="./src/unifieddatalibrary/resources/effect_responses/effect_responses.py">query_help</a>() -> <a href="./src/unifieddatalibrary/types/effect_response_query_help_response.py">EffectResponseQueryHelpResponse</a></code>
- <code title="get /udl/effectresponse/tuple">client.effect_responses.<a href="./src/unifieddatalibrary/resources/effect_responses/effect_responses.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/effect_response_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/effect_response_tuple_response.py">EffectResponseTupleResponse</a></code>
- <code title="post /filedrop/udl-effectresponse">client.effect_responses.<a href="./src/unifieddatalibrary/resources/effect_responses/effect_responses.py">unvalidated_publish</a>(\*\*<a href="src/unifieddatalibrary/types/effect_response_unvalidated_publish_params.py">params</a>) -> None</code>

## History

Types:

```python
from unifieddatalibrary.types.effect_responses import HistoryListResponse, HistoryCountResponse
```

Methods:

- <code title="get /udl/effectresponse/history">client.effect_responses.history.<a href="./src/unifieddatalibrary/resources/effect_responses/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/effect_responses/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/effect_responses/history_list_response.py">SyncOffsetPage[HistoryListResponse]</a></code>
- <code title="get /udl/effectresponse/history/aodr">client.effect_responses.history.<a href="./src/unifieddatalibrary/resources/effect_responses/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/effect_responses/history_aodr_params.py">params</a>) -> None</code>
- <code title="get /udl/effectresponse/history/count">client.effect_responses.history.<a href="./src/unifieddatalibrary/resources/effect_responses/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/effect_responses/history_count_params.py">params</a>) -> str</code>

# Elsets

Types:

```python
from unifieddatalibrary.types import (
    Elset,
    ElsetIngest,
    ElsetAbridged,
    ElsetCountResponse,
    ElsetQueryCurrentElsetHelpResponse,
    ElsetQueryhelpResponse,
    ElsetTupleResponse,
)
```

Methods:

- <code title="post /udl/elset">client.elsets.<a href="./src/unifieddatalibrary/resources/elsets/elsets.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/elset_create_params.py">params</a>) -> None</code>
- <code title="get /udl/elset/{id}">client.elsets.<a href="./src/unifieddatalibrary/resources/elsets/elsets.py">retrieve</a>(id, \*\*<a href="src/unifieddatalibrary/types/elset_retrieve_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/elset.py">Elset</a></code>
- <code title="get /udl/elset">client.elsets.<a href="./src/unifieddatalibrary/resources/elsets/elsets.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/elset_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/elset_abridged.py">SyncOffsetPage[ElsetAbridged]</a></code>
- <code title="get /udl/elset/count">client.elsets.<a href="./src/unifieddatalibrary/resources/elsets/elsets.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/elset_count_params.py">params</a>) -> str</code>
- <code title="post /udl/elset/createBulk">client.elsets.<a href="./src/unifieddatalibrary/resources/elsets/elsets.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/elset_create_bulk_params.py">params</a>) -> None</code>
- <code title="post /udl/elset/createBulkFromTLE">client.elsets.<a href="./src/unifieddatalibrary/resources/elsets/elsets.py">create_bulk_from_tle</a>(\*\*<a href="src/unifieddatalibrary/types/elset_create_bulk_from_tle_params.py">params</a>) -> None</code>
- <code title="get /udl/currentelset/queryhelp">client.elsets.<a href="./src/unifieddatalibrary/resources/elsets/elsets.py">query_current_elset_help</a>() -> <a href="./src/unifieddatalibrary/types/elset_query_current_elset_help_response.py">ElsetQueryCurrentElsetHelpResponse</a></code>
- <code title="get /udl/elset/queryhelp">client.elsets.<a href="./src/unifieddatalibrary/resources/elsets/elsets.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/elset_queryhelp_response.py">ElsetQueryhelpResponse</a></code>
- <code title="get /udl/elset/tuple">client.elsets.<a href="./src/unifieddatalibrary/resources/elsets/elsets.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/elset_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/elset_tuple_response.py">ElsetTupleResponse</a></code>
- <code title="post /filedrop/udl-elset">client.elsets.<a href="./src/unifieddatalibrary/resources/elsets/elsets.py">unvalidated_publish</a>(\*\*<a href="src/unifieddatalibrary/types/elset_unvalidated_publish_params.py">params</a>) -> None</code>

## Current

Types:

```python
from unifieddatalibrary.types.elsets import CurrentTupleResponse
```

Methods:

- <code title="get /udl/elset/current">client.elsets.current.<a href="./src/unifieddatalibrary/resources/elsets/current.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/elsets/current_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/elset_abridged.py">SyncOffsetPage[ElsetAbridged]</a></code>
- <code title="get /udl/elset/current/tuple">client.elsets.current.<a href="./src/unifieddatalibrary/resources/elsets/current.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/elsets/current_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/elsets/current_tuple_response.py">CurrentTupleResponse</a></code>

## History

Types:

```python
from unifieddatalibrary.types.elsets import HistoryCountResponse
```

Methods:

- <code title="get /udl/elset/history">client.elsets.history.<a href="./src/unifieddatalibrary/resources/elsets/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/elsets/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/elset.py">SyncOffsetPage[Elset]</a></code>
- <code title="get /udl/elset/history/aodr">client.elsets.history.<a href="./src/unifieddatalibrary/resources/elsets/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/elsets/history_aodr_params.py">params</a>) -> None</code>
- <code title="get /udl/elset/history/count">client.elsets.history.<a href="./src/unifieddatalibrary/resources/elsets/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/elsets/history_count_params.py">params</a>) -> str</code>

# Emireport

Types:

```python
from unifieddatalibrary.types import (
    EmireportListResponse,
    EmireportCountResponse,
    EmireportGetResponse,
    EmireportQueryhelpResponse,
    EmireportTupleResponse,
)
```

Methods:

- <code title="post /udl/emireport">client.emireport.<a href="./src/unifieddatalibrary/resources/emireport/emireport.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/emireport_create_params.py">params</a>) -> None</code>
- <code title="get /udl/emireport">client.emireport.<a href="./src/unifieddatalibrary/resources/emireport/emireport.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/emireport_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/emireport_list_response.py">SyncOffsetPage[EmireportListResponse]</a></code>
- <code title="get /udl/emireport/count">client.emireport.<a href="./src/unifieddatalibrary/resources/emireport/emireport.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/emireport_count_params.py">params</a>) -> str</code>
- <code title="post /udl/emireport/createBulk">client.emireport.<a href="./src/unifieddatalibrary/resources/emireport/emireport.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/emireport_create_bulk_params.py">params</a>) -> None</code>
- <code title="get /udl/emireport/{id}">client.emireport.<a href="./src/unifieddatalibrary/resources/emireport/emireport.py">get</a>(id, \*\*<a href="src/unifieddatalibrary/types/emireport_get_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/emireport_get_response.py">EmireportGetResponse</a></code>
- <code title="get /udl/emireport/queryhelp">client.emireport.<a href="./src/unifieddatalibrary/resources/emireport/emireport.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/emireport_queryhelp_response.py">EmireportQueryhelpResponse</a></code>
- <code title="get /udl/emireport/tuple">client.emireport.<a href="./src/unifieddatalibrary/resources/emireport/emireport.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/emireport_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/emireport_tuple_response.py">EmireportTupleResponse</a></code>
- <code title="post /filedrop/udl-emireport">client.emireport.<a href="./src/unifieddatalibrary/resources/emireport/emireport.py">unvalidated_publish</a>(\*\*<a href="src/unifieddatalibrary/types/emireport_unvalidated_publish_params.py">params</a>) -> None</code>

## History

Types:

```python
from unifieddatalibrary.types.emireport import HistoryListResponse, HistoryCountResponse
```

Methods:

- <code title="get /udl/emireport/history">client.emireport.history.<a href="./src/unifieddatalibrary/resources/emireport/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/emireport/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/emireport/history_list_response.py">SyncOffsetPage[HistoryListResponse]</a></code>
- <code title="get /udl/emireport/history/aodr">client.emireport.history.<a href="./src/unifieddatalibrary/resources/emireport/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/emireport/history_aodr_params.py">params</a>) -> None</code>
- <code title="get /udl/emireport/history/count">client.emireport.history.<a href="./src/unifieddatalibrary/resources/emireport/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/emireport/history_count_params.py">params</a>) -> str</code>

# EmitterGeolocation

Types:

```python
from unifieddatalibrary.types import (
    EmitterGeolocationRetrieveResponse,
    EmitterGeolocationListResponse,
    EmitterGeolocationCountResponse,
    EmitterGeolocationQueryHelpResponse,
    EmitterGeolocationTupleResponse,
)
```

Methods:

- <code title="post /udl/emittergeolocation">client.emitter_geolocation.<a href="./src/unifieddatalibrary/resources/emitter_geolocation.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/emitter_geolocation_create_params.py">params</a>) -> None</code>
- <code title="get /udl/emittergeolocation/{id}">client.emitter_geolocation.<a href="./src/unifieddatalibrary/resources/emitter_geolocation.py">retrieve</a>(id, \*\*<a href="src/unifieddatalibrary/types/emitter_geolocation_retrieve_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/emitter_geolocation_retrieve_response.py">EmitterGeolocationRetrieveResponse</a></code>
- <code title="get /udl/emittergeolocation">client.emitter_geolocation.<a href="./src/unifieddatalibrary/resources/emitter_geolocation.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/emitter_geolocation_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/emitter_geolocation_list_response.py">SyncOffsetPage[EmitterGeolocationListResponse]</a></code>
- <code title="delete /udl/emittergeolocation/{id}">client.emitter_geolocation.<a href="./src/unifieddatalibrary/resources/emitter_geolocation.py">delete</a>(id) -> None</code>
- <code title="get /udl/emittergeolocation/count">client.emitter_geolocation.<a href="./src/unifieddatalibrary/resources/emitter_geolocation.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/emitter_geolocation_count_params.py">params</a>) -> str</code>
- <code title="post /udl/emittergeolocation/createBulk">client.emitter_geolocation.<a href="./src/unifieddatalibrary/resources/emitter_geolocation.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/emitter_geolocation_create_bulk_params.py">params</a>) -> None</code>
- <code title="get /udl/emittergeolocation/queryhelp">client.emitter_geolocation.<a href="./src/unifieddatalibrary/resources/emitter_geolocation.py">query_help</a>() -> <a href="./src/unifieddatalibrary/types/emitter_geolocation_query_help_response.py">EmitterGeolocationQueryHelpResponse</a></code>
- <code title="get /udl/emittergeolocation/tuple">client.emitter_geolocation.<a href="./src/unifieddatalibrary/resources/emitter_geolocation.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/emitter_geolocation_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/emitter_geolocation_tuple_response.py">EmitterGeolocationTupleResponse</a></code>
- <code title="post /filedrop/udl-emittergeolocation">client.emitter_geolocation.<a href="./src/unifieddatalibrary/resources/emitter_geolocation.py">unvalidated_publish</a>(\*\*<a href="src/unifieddatalibrary/types/emitter_geolocation_unvalidated_publish_params.py">params</a>) -> None</code>

# EngineDetails

Types:

```python
from unifieddatalibrary.types import EngineDetailsAbridged
```

Methods:

- <code title="post /udl/enginedetails">client.engine_details.<a href="./src/unifieddatalibrary/resources/engine_details.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/engine_detail_create_params.py">params</a>) -> None</code>
- <code title="get /udl/enginedetails/{id}">client.engine_details.<a href="./src/unifieddatalibrary/resources/engine_details.py">retrieve</a>(id, \*\*<a href="src/unifieddatalibrary/types/engine_detail_retrieve_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/shared/engine_details_full.py">EngineDetailsFull</a></code>
- <code title="put /udl/enginedetails/{id}">client.engine_details.<a href="./src/unifieddatalibrary/resources/engine_details.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/engine_detail_update_params.py">params</a>) -> None</code>
- <code title="get /udl/enginedetails">client.engine_details.<a href="./src/unifieddatalibrary/resources/engine_details.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/engine_detail_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/engine_details_abridged.py">SyncOffsetPage[EngineDetailsAbridged]</a></code>
- <code title="delete /udl/enginedetails/{id}">client.engine_details.<a href="./src/unifieddatalibrary/resources/engine_details.py">delete</a>(id) -> None</code>

# Engines

Types:

```python
from unifieddatalibrary.types import (
    EngineAbridged,
    EngineCountResponse,
    EngineQueryhelpResponse,
    EngineTupleResponse,
)
```

Methods:

- <code title="post /udl/engine">client.engines.<a href="./src/unifieddatalibrary/resources/engines.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/engine_create_params.py">params</a>) -> None</code>
- <code title="get /udl/engine/{id}">client.engines.<a href="./src/unifieddatalibrary/resources/engines.py">retrieve</a>(id, \*\*<a href="src/unifieddatalibrary/types/engine_retrieve_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/shared/engine.py">Engine</a></code>
- <code title="put /udl/engine/{id}">client.engines.<a href="./src/unifieddatalibrary/resources/engines.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/engine_update_params.py">params</a>) -> None</code>
- <code title="get /udl/engine">client.engines.<a href="./src/unifieddatalibrary/resources/engines.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/engine_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/engine_abridged.py">SyncOffsetPage[EngineAbridged]</a></code>
- <code title="delete /udl/engine/{id}">client.engines.<a href="./src/unifieddatalibrary/resources/engines.py">delete</a>(id) -> None</code>
- <code title="get /udl/engine/count">client.engines.<a href="./src/unifieddatalibrary/resources/engines.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/engine_count_params.py">params</a>) -> str</code>
- <code title="get /udl/engine/queryhelp">client.engines.<a href="./src/unifieddatalibrary/resources/engines.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/engine_queryhelp_response.py">EngineQueryhelpResponse</a></code>
- <code title="get /udl/engine/tuple">client.engines.<a href="./src/unifieddatalibrary/resources/engines.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/engine_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/engine_tuple_response.py">EngineTupleResponse</a></code>

# Entities

Types:

```python
from unifieddatalibrary.types import (
    EntityAbridged,
    EntityIngest,
    EntityCountResponse,
    EntityGetAllTypesResponse,
    EntityQueryHelpResponse,
    EntityTupleResponse,
)
```

Methods:

- <code title="post /udl/entity">client.entities.<a href="./src/unifieddatalibrary/resources/entities.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/entity_create_params.py">params</a>) -> None</code>
- <code title="get /udl/entity/{id}">client.entities.<a href="./src/unifieddatalibrary/resources/entities.py">retrieve</a>(id, \*\*<a href="src/unifieddatalibrary/types/entity_retrieve_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/shared/entity_full.py">EntityFull</a></code>
- <code title="put /udl/entity/{id}">client.entities.<a href="./src/unifieddatalibrary/resources/entities.py">update</a>(id, \*\*<a href="src/unifieddatalibrary/types/entity_update_params.py">params</a>) -> None</code>
- <code title="get /udl/entity">client.entities.<a href="./src/unifieddatalibrary/resources/entities.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/entity_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/entity_abridged.py">SyncOffsetPage[EntityAbridged]</a></code>
- <code title="delete /udl/entity/{id}">client.entities.<a href="./src/unifieddatalibrary/resources/entities.py">delete</a>(id) -> None</code>
- <code title="get /udl/entity/count">client.entities.<a href="./src/unifieddatalibrary/resources/entities.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/entity_count_params.py">params</a>) -> str</code>
- <code title="get /udl/entity/getAllTypes">client.entities.<a href="./src/unifieddatalibrary/resources/entities.py">get_all_types</a>(\*\*<a href="src/unifieddatalibrary/types/entity_get_all_types_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/entity_get_all_types_response.py">EntityGetAllTypesResponse</a></code>
- <code title="get /udl/entity/queryhelp">client.entities.<a href="./src/unifieddatalibrary/resources/entities.py">query_help</a>() -> <a href="./src/unifieddatalibrary/types/entity_query_help_response.py">EntityQueryHelpResponse</a></code>
- <code title="get /udl/entity/tuple">client.entities.<a href="./src/unifieddatalibrary/resources/entities.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/entity_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/entity_tuple_response.py">EntityTupleResponse</a></code>

# Eop

Types:

```python
from unifieddatalibrary.types import (
    EopAbridged,
    EopCountResponse,
    EopListTupleResponse,
    EopQueryhelpResponse,
)
```

Methods:

- <code title="post /udl/eop">client.eop.<a href="./src/unifieddatalibrary/resources/eop/eop.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/eop_create_params.py">params</a>) -> None</code>
- <code title="get /udl/eop/{id}">client.eop.<a href="./src/unifieddatalibrary/resources/eop/eop.py">retrieve</a>(id, \*\*<a href="src/unifieddatalibrary/types/eop_retrieve_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/shared/eop_full.py">EopFull</a></code>
- <code title="put /udl/eop/{id}">client.eop.<a href="./src/unifieddatalibrary/resources/eop/eop.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/eop_update_params.py">params</a>) -> None</code>
- <code title="get /udl/eop">client.eop.<a href="./src/unifieddatalibrary/resources/eop/eop.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/eop_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/eop_abridged.py">SyncOffsetPage[EopAbridged]</a></code>
- <code title="delete /udl/eop/{id}">client.eop.<a href="./src/unifieddatalibrary/resources/eop/eop.py">delete</a>(id) -> None</code>
- <code title="get /udl/eop/count">client.eop.<a href="./src/unifieddatalibrary/resources/eop/eop.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/eop_count_params.py">params</a>) -> str</code>
- <code title="get /udl/eop/tuple">client.eop.<a href="./src/unifieddatalibrary/resources/eop/eop.py">list_tuple</a>(\*\*<a href="src/unifieddatalibrary/types/eop_list_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/eop_list_tuple_response.py">EopListTupleResponse</a></code>
- <code title="get /udl/eop/queryhelp">client.eop.<a href="./src/unifieddatalibrary/resources/eop/eop.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/eop_queryhelp_response.py">EopQueryhelpResponse</a></code>

## History

Types:

```python
from unifieddatalibrary.types.eop import HistoryCountResponse
```

Methods:

- <code title="get /udl/eop/history">client.eop.history.<a href="./src/unifieddatalibrary/resources/eop/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/eop/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/shared/eop_full.py">SyncOffsetPage[EopFull]</a></code>
- <code title="get /udl/eop/history/aodr">client.eop.history.<a href="./src/unifieddatalibrary/resources/eop/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/eop/history_aodr_params.py">params</a>) -> None</code>
- <code title="get /udl/eop/history/count">client.eop.history.<a href="./src/unifieddatalibrary/resources/eop/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/eop/history_count_params.py">params</a>) -> str</code>

# Ephemeris

Types:

```python
from unifieddatalibrary.types import (
    EphemerisAbridged,
    EphemerisCountResponse,
    EphemerisQueryhelpResponse,
    EphemerisTupleResponse,
)
```

Methods:

- <code title="get /udl/ephemeris">client.ephemeris.<a href="./src/unifieddatalibrary/resources/ephemeris/ephemeris.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/ephemeris_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/ephemeris_abridged.py">SyncOffsetPage[EphemerisAbridged]</a></code>
- <code title="get /udl/ephemeris/count">client.ephemeris.<a href="./src/unifieddatalibrary/resources/ephemeris/ephemeris.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/ephemeris_count_params.py">params</a>) -> str</code>
- <code title="post /filedrop/ephem">client.ephemeris.<a href="./src/unifieddatalibrary/resources/ephemeris/ephemeris.py">file_upload</a>(\*\*<a href="src/unifieddatalibrary/types/ephemeris_file_upload_params.py">params</a>) -> None</code>
- <code title="get /udl/ephemeris/queryhelp">client.ephemeris.<a href="./src/unifieddatalibrary/resources/ephemeris/ephemeris.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/ephemeris_queryhelp_response.py">EphemerisQueryhelpResponse</a></code>
- <code title="get /udl/ephemeris/tuple">client.ephemeris.<a href="./src/unifieddatalibrary/resources/ephemeris/ephemeris.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/ephemeris_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/ephemeris_tuple_response.py">EphemerisTupleResponse</a></code>
- <code title="post /filedrop/udl-ephset">client.ephemeris.<a href="./src/unifieddatalibrary/resources/ephemeris/ephemeris.py">unvalidated_publish</a>(\*\*<a href="src/unifieddatalibrary/types/ephemeris_unvalidated_publish_params.py">params</a>) -> None</code>

## AttitudeData

Types:

```python
from unifieddatalibrary.types.ephemeris import AttitudeDataAbridged, AttitudeDataCountResponse
```

Methods:

- <code title="get /udl/attitudedata">client.ephemeris.attitude_data.<a href="./src/unifieddatalibrary/resources/ephemeris/attitude_data/attitude_data.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/ephemeris/attitude_data_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/ephemeris/attitude_data_abridged.py">SyncOffsetPage[AttitudeDataAbridged]</a></code>
- <code title="get /udl/attitudedata/count">client.ephemeris.attitude_data.<a href="./src/unifieddatalibrary/resources/ephemeris/attitude_data/attitude_data.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/ephemeris/attitude_data_count_params.py">params</a>) -> str</code>

### History

Types:

```python
from unifieddatalibrary.types.ephemeris.attitude_data import (
    HistoryRetrieveResponse,
    HistoryCountResponse,
)
```

Methods:

- <code title="get /udl/attitudedata/history">client.ephemeris.attitude_data.history.<a href="./src/unifieddatalibrary/resources/ephemeris/attitude_data/history.py">retrieve</a>(\*\*<a href="src/unifieddatalibrary/types/ephemeris/attitude_data/history_retrieve_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/ephemeris/attitude_data/history_retrieve_response.py">HistoryRetrieveResponse</a></code>
- <code title="get /udl/attitudedata/history/aodr">client.ephemeris.attitude_data.history.<a href="./src/unifieddatalibrary/resources/ephemeris/attitude_data/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/ephemeris/attitude_data/history_aodr_params.py">params</a>) -> None</code>
- <code title="get /udl/attitudedata/history/count">client.ephemeris.attitude_data.history.<a href="./src/unifieddatalibrary/resources/ephemeris/attitude_data/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/ephemeris/attitude_data/history_count_params.py">params</a>) -> str</code>

## History

Types:

```python
from unifieddatalibrary.types.ephemeris import HistoryCountResponse
```

Methods:

- <code title="get /udl/ephemeris/history">client.ephemeris.history.<a href="./src/unifieddatalibrary/resources/ephemeris/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/ephemeris/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/shared/ephemeris_full.py">SyncOffsetPage[EphemerisFull]</a></code>
- <code title="get /udl/ephemeris/history/aodr">client.ephemeris.history.<a href="./src/unifieddatalibrary/resources/ephemeris/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/ephemeris/history_aodr_params.py">params</a>) -> None</code>
- <code title="get /udl/ephemeris/history/count">client.ephemeris.history.<a href="./src/unifieddatalibrary/resources/ephemeris/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/ephemeris/history_count_params.py">params</a>) -> str</code>

# EphemerisSets

Types:

```python
from unifieddatalibrary.types import (
    EphemerisSet,
    EphemerisSetAbridged,
    EphemerisSetCountResponse,
    EphemerisSetQueryhelpResponse,
    EphemerisSetTupleResponse,
)
```

Methods:

- <code title="post /udl/ephemerisset">client.ephemeris_sets.<a href="./src/unifieddatalibrary/resources/ephemeris_sets/ephemeris_sets.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/ephemeris_set_create_params.py">params</a>) -> None</code>
- <code title="get /udl/ephemerisset/{id}">client.ephemeris_sets.<a href="./src/unifieddatalibrary/resources/ephemeris_sets/ephemeris_sets.py">retrieve</a>(id, \*\*<a href="src/unifieddatalibrary/types/ephemeris_set_retrieve_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/ephemeris_set.py">EphemerisSet</a></code>
- <code title="get /udl/ephemerisset">client.ephemeris_sets.<a href="./src/unifieddatalibrary/resources/ephemeris_sets/ephemeris_sets.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/ephemeris_set_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/ephemeris_set_abridged.py">SyncOffsetPage[EphemerisSetAbridged]</a></code>
- <code title="get /udl/ephemerisset/count">client.ephemeris_sets.<a href="./src/unifieddatalibrary/resources/ephemeris_sets/ephemeris_sets.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/ephemeris_set_count_params.py">params</a>) -> str</code>
- <code title="get /udl/ephemerisset/getFile/{id}">client.ephemeris_sets.<a href="./src/unifieddatalibrary/resources/ephemeris_sets/ephemeris_sets.py">file_retrieve</a>(id, \*\*<a href="src/unifieddatalibrary/types/ephemeris_set_file_retrieve_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="get /udl/ephemerisset/queryhelp">client.ephemeris_sets.<a href="./src/unifieddatalibrary/resources/ephemeris_sets/ephemeris_sets.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/ephemeris_set_queryhelp_response.py">EphemerisSetQueryhelpResponse</a></code>
- <code title="get /udl/ephemerisset/tuple">client.ephemeris_sets.<a href="./src/unifieddatalibrary/resources/ephemeris_sets/ephemeris_sets.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/ephemeris_set_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/ephemeris_set_tuple_response.py">EphemerisSetTupleResponse</a></code>

## History

Types:

```python
from unifieddatalibrary.types.ephemeris_sets import HistoryCountResponse
```

Methods:

- <code title="get /udl/ephemerisset/history">client.ephemeris_sets.history.<a href="./src/unifieddatalibrary/resources/ephemeris_sets/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/ephemeris_sets/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/ephemeris_set.py">SyncOffsetPage[EphemerisSet]</a></code>
- <code title="get /udl/ephemerisset/history/aodr">client.ephemeris_sets.history.<a href="./src/unifieddatalibrary/resources/ephemeris_sets/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/ephemeris_sets/history_aodr_params.py">params</a>) -> None</code>
- <code title="get /udl/ephemerisset/history/count">client.ephemeris_sets.history.<a href="./src/unifieddatalibrary/resources/ephemeris_sets/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/ephemeris_sets/history_count_params.py">params</a>) -> str</code>

# Equipment

Types:

```python
from unifieddatalibrary.types import (
    EquipmentAbridged,
    EquipmentFull,
    EquipmentCountResponse,
    EquipmentQueryHelpResponse,
    EquipmentTupleResponse,
)
```

Methods:

- <code title="post /udl/equipment">client.equipment.<a href="./src/unifieddatalibrary/resources/equipment.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/equipment_create_params.py">params</a>) -> None</code>
- <code title="get /udl/equipment/{id}">client.equipment.<a href="./src/unifieddatalibrary/resources/equipment.py">retrieve</a>(id, \*\*<a href="src/unifieddatalibrary/types/equipment_retrieve_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/equipment_full.py">EquipmentFull</a></code>
- <code title="put /udl/equipment/{id}">client.equipment.<a href="./src/unifieddatalibrary/resources/equipment.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/equipment_update_params.py">params</a>) -> None</code>
- <code title="get /udl/equipment">client.equipment.<a href="./src/unifieddatalibrary/resources/equipment.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/equipment_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/equipment_abridged.py">SyncOffsetPage[EquipmentAbridged]</a></code>
- <code title="delete /udl/equipment/{id}">client.equipment.<a href="./src/unifieddatalibrary/resources/equipment.py">delete</a>(id) -> None</code>
- <code title="get /udl/equipment/count">client.equipment.<a href="./src/unifieddatalibrary/resources/equipment.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/equipment_count_params.py">params</a>) -> str</code>
- <code title="post /udl/equipment/createBulk">client.equipment.<a href="./src/unifieddatalibrary/resources/equipment.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/equipment_create_bulk_params.py">params</a>) -> None</code>
- <code title="get /udl/equipment/queryhelp">client.equipment.<a href="./src/unifieddatalibrary/resources/equipment.py">query_help</a>() -> <a href="./src/unifieddatalibrary/types/equipment_query_help_response.py">EquipmentQueryHelpResponse</a></code>
- <code title="get /udl/equipment/tuple">client.equipment.<a href="./src/unifieddatalibrary/resources/equipment.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/equipment_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/equipment_tuple_response.py">EquipmentTupleResponse</a></code>

# EquipmentRemarks

Types:

```python
from unifieddatalibrary.types import (
    EquipmentRemarkAbridged,
    EquipmentRemarkFull,
    EquipmentRemarkCountResponse,
    EquipmentRemarkQueryHelpResponse,
    EquipmentRemarkTupleResponse,
)
```

Methods:

- <code title="post /udl/equipmentremark">client.equipment_remarks.<a href="./src/unifieddatalibrary/resources/equipment_remarks.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/equipment_remark_create_params.py">params</a>) -> None</code>
- <code title="get /udl/equipmentremark/{id}">client.equipment_remarks.<a href="./src/unifieddatalibrary/resources/equipment_remarks.py">retrieve</a>(id, \*\*<a href="src/unifieddatalibrary/types/equipment_remark_retrieve_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/equipment_remark_full.py">EquipmentRemarkFull</a></code>
- <code title="get /udl/equipmentremark">client.equipment_remarks.<a href="./src/unifieddatalibrary/resources/equipment_remarks.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/equipment_remark_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/equipment_remark_abridged.py">SyncOffsetPage[EquipmentRemarkAbridged]</a></code>
- <code title="get /udl/equipmentremark/count">client.equipment_remarks.<a href="./src/unifieddatalibrary/resources/equipment_remarks.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/equipment_remark_count_params.py">params</a>) -> str</code>
- <code title="post /udl/equipmentremark/createBulk">client.equipment_remarks.<a href="./src/unifieddatalibrary/resources/equipment_remarks.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/equipment_remark_create_bulk_params.py">params</a>) -> None</code>
- <code title="get /udl/equipmentremark/queryhelp">client.equipment_remarks.<a href="./src/unifieddatalibrary/resources/equipment_remarks.py">query_help</a>() -> <a href="./src/unifieddatalibrary/types/equipment_remark_query_help_response.py">EquipmentRemarkQueryHelpResponse</a></code>
- <code title="get /udl/equipmentremark/tuple">client.equipment_remarks.<a href="./src/unifieddatalibrary/resources/equipment_remarks.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/equipment_remark_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/equipment_remark_tuple_response.py">EquipmentRemarkTupleResponse</a></code>

# Evac

Types:

```python
from unifieddatalibrary.types import EvacAbridged, EvacCountResponse, EvacQueryHelpResponse
```

Methods:

- <code title="post /udl/evac">client.evac.<a href="./src/unifieddatalibrary/resources/evac/evac.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/evac_create_params.py">params</a>) -> None</code>
- <code title="get /udl/evac/{id}">client.evac.<a href="./src/unifieddatalibrary/resources/evac/evac.py">retrieve</a>(id, \*\*<a href="src/unifieddatalibrary/types/evac_retrieve_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/shared/evac_full.py">EvacFull</a></code>
- <code title="get /udl/evac">client.evac.<a href="./src/unifieddatalibrary/resources/evac/evac.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/evac_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/evac_abridged.py">SyncOffsetPage[EvacAbridged]</a></code>
- <code title="get /udl/evac/count">client.evac.<a href="./src/unifieddatalibrary/resources/evac/evac.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/evac_count_params.py">params</a>) -> str</code>
- <code title="post /udl/evac/createBulk">client.evac.<a href="./src/unifieddatalibrary/resources/evac/evac.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/evac_create_bulk_params.py">params</a>) -> None</code>
- <code title="get /udl/evac/queryhelp">client.evac.<a href="./src/unifieddatalibrary/resources/evac/evac.py">query_help</a>() -> <a href="./src/unifieddatalibrary/types/evac_query_help_response.py">EvacQueryHelpResponse</a></code>
- <code title="post /filedrop/udl-evac">client.evac.<a href="./src/unifieddatalibrary/resources/evac/evac.py">unvalidated_publish</a>(\*\*<a href="src/unifieddatalibrary/types/evac_unvalidated_publish_params.py">params</a>) -> None</code>

## History

Types:

```python
from unifieddatalibrary.types.evac import HistoryCountResponse
```

Methods:

- <code title="get /udl/evac/history">client.evac.history.<a href="./src/unifieddatalibrary/resources/evac/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/evac/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/shared/evac_full.py">SyncOffsetPage[EvacFull]</a></code>
- <code title="get /udl/evac/history/count">client.evac.history.<a href="./src/unifieddatalibrary/resources/evac/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/evac/history_count_params.py">params</a>) -> str</code>

## Tuple

Methods:

- <code title="get /udl/evac/tuple">client.evac.tuple.<a href="./src/unifieddatalibrary/resources/evac/tuple.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/evac/tuple_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/shared/evac_full.py">SyncOffsetPage[EvacFull]</a></code>

# EventEvolution

Types:

```python
from unifieddatalibrary.types import (
    EventEvolutionListResponse,
    EventEvolutionCountResponse,
    EventEvolutionQueryhelpResponse,
    EventEvolutionTupleResponse,
)
```

Methods:

- <code title="post /udl/eventevolution">client.event_evolution.<a href="./src/unifieddatalibrary/resources/event_evolution/event_evolution.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/event_evolution_create_params.py">params</a>) -> None</code>
- <code title="get /udl/eventevolution/{id}">client.event_evolution.<a href="./src/unifieddatalibrary/resources/event_evolution/event_evolution.py">retrieve</a>(id, \*\*<a href="src/unifieddatalibrary/types/event_evolution_retrieve_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/shared/event_evolution_full.py">EventEvolutionFull</a></code>
- <code title="get /udl/eventevolution">client.event_evolution.<a href="./src/unifieddatalibrary/resources/event_evolution/event_evolution.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/event_evolution_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/event_evolution_list_response.py">SyncOffsetPage[EventEvolutionListResponse]</a></code>
- <code title="get /udl/eventevolution/count">client.event_evolution.<a href="./src/unifieddatalibrary/resources/event_evolution/event_evolution.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/event_evolution_count_params.py">params</a>) -> str</code>
- <code title="post /udl/eventevolution/createBulk">client.event_evolution.<a href="./src/unifieddatalibrary/resources/event_evolution/event_evolution.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/event_evolution_create_bulk_params.py">params</a>) -> None</code>
- <code title="get /udl/eventevolution/queryhelp">client.event_evolution.<a href="./src/unifieddatalibrary/resources/event_evolution/event_evolution.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/event_evolution_queryhelp_response.py">EventEvolutionQueryhelpResponse</a></code>
- <code title="get /udl/eventevolution/tuple">client.event_evolution.<a href="./src/unifieddatalibrary/resources/event_evolution/event_evolution.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/event_evolution_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/event_evolution_tuple_response.py">EventEvolutionTupleResponse</a></code>
- <code title="post /filedrop/udl-eventevolution">client.event_evolution.<a href="./src/unifieddatalibrary/resources/event_evolution/event_evolution.py">unvalidated_publish</a>(\*\*<a href="src/unifieddatalibrary/types/event_evolution_unvalidated_publish_params.py">params</a>) -> None</code>

## History

Types:

```python
from unifieddatalibrary.types.event_evolution import HistoryCountResponse
```

Methods:

- <code title="get /udl/eventevolution/history">client.event_evolution.history.<a href="./src/unifieddatalibrary/resources/event_evolution/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/event_evolution/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/shared/event_evolution_full.py">SyncOffsetPage[EventEvolutionFull]</a></code>
- <code title="get /udl/eventevolution/history/aodr">client.event_evolution.history.<a href="./src/unifieddatalibrary/resources/event_evolution/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/event_evolution/history_aodr_params.py">params</a>) -> None</code>
- <code title="get /udl/eventevolution/history/count">client.event_evolution.history.<a href="./src/unifieddatalibrary/resources/event_evolution/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/event_evolution/history_count_params.py">params</a>) -> str</code>

# FeatureAssessment

Types:

```python
from unifieddatalibrary.types import (
    FeatureAssessmentRetrieveResponse,
    FeatureAssessmentListResponse,
    FeatureAssessmentCountResponse,
    FeatureAssessmentQueryHelpResponse,
    FeatureAssessmentTupleResponse,
)
```

Methods:

- <code title="post /udl/featureassessment">client.feature_assessment.<a href="./src/unifieddatalibrary/resources/feature_assessment/feature_assessment.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/feature_assessment_create_params.py">params</a>) -> None</code>
- <code title="get /udl/featureassessment/{id}">client.feature_assessment.<a href="./src/unifieddatalibrary/resources/feature_assessment/feature_assessment.py">retrieve</a>(id, \*\*<a href="src/unifieddatalibrary/types/feature_assessment_retrieve_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/feature_assessment_retrieve_response.py">FeatureAssessmentRetrieveResponse</a></code>
- <code title="get /udl/featureassessment">client.feature_assessment.<a href="./src/unifieddatalibrary/resources/feature_assessment/feature_assessment.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/feature_assessment_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/feature_assessment_list_response.py">SyncOffsetPage[FeatureAssessmentListResponse]</a></code>
- <code title="get /udl/featureassessment/count">client.feature_assessment.<a href="./src/unifieddatalibrary/resources/feature_assessment/feature_assessment.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/feature_assessment_count_params.py">params</a>) -> str</code>
- <code title="post /udl/featureassessment/createBulk">client.feature_assessment.<a href="./src/unifieddatalibrary/resources/feature_assessment/feature_assessment.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/feature_assessment_create_bulk_params.py">params</a>) -> None</code>
- <code title="get /udl/featureassessment/queryhelp">client.feature_assessment.<a href="./src/unifieddatalibrary/resources/feature_assessment/feature_assessment.py">query_help</a>() -> <a href="./src/unifieddatalibrary/types/feature_assessment_query_help_response.py">FeatureAssessmentQueryHelpResponse</a></code>
- <code title="get /udl/featureassessment/tuple">client.feature_assessment.<a href="./src/unifieddatalibrary/resources/feature_assessment/feature_assessment.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/feature_assessment_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/feature_assessment_tuple_response.py">FeatureAssessmentTupleResponse</a></code>
- <code title="post /filedrop/udl-featureassessment">client.feature_assessment.<a href="./src/unifieddatalibrary/resources/feature_assessment/feature_assessment.py">unvalidated_publish</a>(\*\*<a href="src/unifieddatalibrary/types/feature_assessment_unvalidated_publish_params.py">params</a>) -> None</code>

## History

Types:

```python
from unifieddatalibrary.types.feature_assessment import HistoryListResponse, HistoryCountResponse
```

Methods:

- <code title="get /udl/featureassessment/history">client.feature_assessment.history.<a href="./src/unifieddatalibrary/resources/feature_assessment/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/feature_assessment/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/feature_assessment/history_list_response.py">SyncOffsetPage[HistoryListResponse]</a></code>
- <code title="get /udl/featureassessment/history/aodr">client.feature_assessment.history.<a href="./src/unifieddatalibrary/resources/feature_assessment/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/feature_assessment/history_aodr_params.py">params</a>) -> None</code>
- <code title="get /udl/featureassessment/history/count">client.feature_assessment.history.<a href="./src/unifieddatalibrary/resources/feature_assessment/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/feature_assessment/history_count_params.py">params</a>) -> str</code>

# Flightplan

Types:

```python
from unifieddatalibrary.types import (
    FlightPlanAbridged,
    FlightplanCountResponse,
    FlightplanQueryhelpResponse,
    FlightplanTupleResponse,
)
```

Methods:

- <code title="post /udl/flightplan">client.flightplan.<a href="./src/unifieddatalibrary/resources/flightplan.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/flightplan_create_params.py">params</a>) -> None</code>
- <code title="get /udl/flightplan/{id}">client.flightplan.<a href="./src/unifieddatalibrary/resources/flightplan.py">retrieve</a>(id, \*\*<a href="src/unifieddatalibrary/types/flightplan_retrieve_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/shared/flight_plan_full.py">FlightPlanFull</a></code>
- <code title="put /udl/flightplan/{id}">client.flightplan.<a href="./src/unifieddatalibrary/resources/flightplan.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/flightplan_update_params.py">params</a>) -> None</code>
- <code title="get /udl/flightplan">client.flightplan.<a href="./src/unifieddatalibrary/resources/flightplan.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/flightplan_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/flight_plan_abridged.py">SyncOffsetPage[FlightPlanAbridged]</a></code>
- <code title="delete /udl/flightplan/{id}">client.flightplan.<a href="./src/unifieddatalibrary/resources/flightplan.py">delete</a>(id) -> None</code>
- <code title="get /udl/flightplan/count">client.flightplan.<a href="./src/unifieddatalibrary/resources/flightplan.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/flightplan_count_params.py">params</a>) -> str</code>
- <code title="get /udl/flightplan/queryhelp">client.flightplan.<a href="./src/unifieddatalibrary/resources/flightplan.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/flightplan_queryhelp_response.py">FlightplanQueryhelpResponse</a></code>
- <code title="get /udl/flightplan/tuple">client.flightplan.<a href="./src/unifieddatalibrary/resources/flightplan.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/flightplan_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/flightplan_tuple_response.py">FlightplanTupleResponse</a></code>
- <code title="post /filedrop/udl-flightplan">client.flightplan.<a href="./src/unifieddatalibrary/resources/flightplan.py">unvalidated_publish</a>(\*\*<a href="src/unifieddatalibrary/types/flightplan_unvalidated_publish_params.py">params</a>) -> None</code>

# GeoStatus

Types:

```python
from unifieddatalibrary.types import (
    GeoStatusListResponse,
    GeoStatusCountResponse,
    GeoStatusQueryhelpResponse,
    GeoStatusTupleResponse,
)
```

Methods:

- <code title="post /udl/geostatus">client.geo_status.<a href="./src/unifieddatalibrary/resources/geo_status/geo_status.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/geo_status_create_params.py">params</a>) -> None</code>
- <code title="get /udl/geostatus">client.geo_status.<a href="./src/unifieddatalibrary/resources/geo_status/geo_status.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/geo_status_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/geo_status_list_response.py">SyncOffsetPage[GeoStatusListResponse]</a></code>
- <code title="get /udl/geostatus/count">client.geo_status.<a href="./src/unifieddatalibrary/resources/geo_status/geo_status.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/geo_status_count_params.py">params</a>) -> str</code>
- <code title="post /udl/geostatus/createBulk">client.geo_status.<a href="./src/unifieddatalibrary/resources/geo_status/geo_status.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/geo_status_create_bulk_params.py">params</a>) -> None</code>
- <code title="get /udl/geostatus/{id}">client.geo_status.<a href="./src/unifieddatalibrary/resources/geo_status/geo_status.py">get</a>(id, \*\*<a href="src/unifieddatalibrary/types/geo_status_get_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/geo_status/geo_status_full.py">GeoStatusFull</a></code>
- <code title="get /udl/geostatus/queryhelp">client.geo_status.<a href="./src/unifieddatalibrary/resources/geo_status/geo_status.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/geo_status_queryhelp_response.py">GeoStatusQueryhelpResponse</a></code>
- <code title="get /udl/geostatus/tuple">client.geo_status.<a href="./src/unifieddatalibrary/resources/geo_status/geo_status.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/geo_status_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/geo_status_tuple_response.py">GeoStatusTupleResponse</a></code>

## History

Types:

```python
from unifieddatalibrary.types.geo_status import GeoStatusFull, HistoryCountResponse
```

Methods:

- <code title="get /udl/geostatus/history">client.geo_status.history.<a href="./src/unifieddatalibrary/resources/geo_status/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/geo_status/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/geo_status/geo_status_full.py">SyncOffsetPage[GeoStatusFull]</a></code>
- <code title="get /udl/geostatus/history/aodr">client.geo_status.history.<a href="./src/unifieddatalibrary/resources/geo_status/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/geo_status/history_aodr_params.py">params</a>) -> None</code>
- <code title="get /udl/geostatus/history/count">client.geo_status.history.<a href="./src/unifieddatalibrary/resources/geo_status/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/geo_status/history_count_params.py">params</a>) -> str</code>

# GlobalAtmosphericModel

Types:

```python
from unifieddatalibrary.types import (
    GlobalAtmosphericModelRetrieveResponse,
    GlobalAtmosphericModelListResponse,
    GlobalAtmosphericModelCountResponse,
    GlobalAtmosphericModelQueryHelpResponse,
    GlobalAtmosphericModelTupleResponse,
)
```

Methods:

- <code title="get /udl/globalatmosphericmodel/{id}">client.global_atmospheric_model.<a href="./src/unifieddatalibrary/resources/global_atmospheric_model/global_atmospheric_model.py">retrieve</a>(id, \*\*<a href="src/unifieddatalibrary/types/global_atmospheric_model_retrieve_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/global_atmospheric_model_retrieve_response.py">GlobalAtmosphericModelRetrieveResponse</a></code>
- <code title="get /udl/globalatmosphericmodel">client.global_atmospheric_model.<a href="./src/unifieddatalibrary/resources/global_atmospheric_model/global_atmospheric_model.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/global_atmospheric_model_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/global_atmospheric_model_list_response.py">SyncOffsetPage[GlobalAtmosphericModelListResponse]</a></code>
- <code title="get /udl/globalatmosphericmodel/count">client.global_atmospheric_model.<a href="./src/unifieddatalibrary/resources/global_atmospheric_model/global_atmospheric_model.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/global_atmospheric_model_count_params.py">params</a>) -> str</code>
- <code title="get /udl/globalatmosphericmodel/getFile/{id}">client.global_atmospheric_model.<a href="./src/unifieddatalibrary/resources/global_atmospheric_model/global_atmospheric_model.py">get_file</a>(id, \*\*<a href="src/unifieddatalibrary/types/global_atmospheric_model_get_file_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="get /udl/globalatmosphericmodel/queryhelp">client.global_atmospheric_model.<a href="./src/unifieddatalibrary/resources/global_atmospheric_model/global_atmospheric_model.py">query_help</a>() -> <a href="./src/unifieddatalibrary/types/global_atmospheric_model_query_help_response.py">GlobalAtmosphericModelQueryHelpResponse</a></code>
- <code title="get /udl/globalatmosphericmodel/tuple">client.global_atmospheric_model.<a href="./src/unifieddatalibrary/resources/global_atmospheric_model/global_atmospheric_model.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/global_atmospheric_model_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/global_atmospheric_model_tuple_response.py">GlobalAtmosphericModelTupleResponse</a></code>
- <code title="post /filedrop/udl-globalatmosphericmodel">client.global_atmospheric_model.<a href="./src/unifieddatalibrary/resources/global_atmospheric_model/global_atmospheric_model.py">unvalidated_publish</a>(\*\*<a href="src/unifieddatalibrary/types/global_atmospheric_model_unvalidated_publish_params.py">params</a>) -> None</code>

## History

Types:

```python
from unifieddatalibrary.types.global_atmospheric_model import (
    HistoryListResponse,
    HistoryCountResponse,
)
```

Methods:

- <code title="get /udl/globalatmosphericmodel/history">client.global_atmospheric_model.history.<a href="./src/unifieddatalibrary/resources/global_atmospheric_model/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/global_atmospheric_model/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/global_atmospheric_model/history_list_response.py">SyncOffsetPage[HistoryListResponse]</a></code>
- <code title="get /udl/globalatmosphericmodel/history/aodr">client.global_atmospheric_model.history.<a href="./src/unifieddatalibrary/resources/global_atmospheric_model/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/global_atmospheric_model/history_aodr_params.py">params</a>) -> None</code>
- <code title="get /udl/globalatmosphericmodel/history/count">client.global_atmospheric_model.history.<a href="./src/unifieddatalibrary/resources/global_atmospheric_model/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/global_atmospheric_model/history_count_params.py">params</a>) -> str</code>

# GnssObservations

## History

Types:

```python
from unifieddatalibrary.types.gnss_observations import HistoryCountResponse
```

Methods:

- <code title="get /udl/gnssobservationset/history/count">client.gnss_observations.history.<a href="./src/unifieddatalibrary/resources/gnss_observations/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/gnss_observations/history_count_params.py">params</a>) -> str</code>

# GnssObservationset

Types:

```python
from unifieddatalibrary.types import (
    GnssObservationsetListResponse,
    GnssObservationsetCountResponse,
    GnssObservationsetQueryhelpResponse,
    GnssObservationsetTupleResponse,
)
```

Methods:

- <code title="get /udl/gnssobservationset">client.gnss_observationset.<a href="./src/unifieddatalibrary/resources/gnss_observationset/gnss_observationset.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/gnss_observationset_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/gnss_observationset_list_response.py">SyncOffsetPage[GnssObservationsetListResponse]</a></code>
- <code title="get /udl/gnssobservationset/count">client.gnss_observationset.<a href="./src/unifieddatalibrary/resources/gnss_observationset/gnss_observationset.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/gnss_observationset_count_params.py">params</a>) -> str</code>
- <code title="post /udl/gnssobservationset/createBulk">client.gnss_observationset.<a href="./src/unifieddatalibrary/resources/gnss_observationset/gnss_observationset.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/gnss_observationset_create_bulk_params.py">params</a>) -> None</code>
- <code title="get /udl/gnssobservationset/queryhelp">client.gnss_observationset.<a href="./src/unifieddatalibrary/resources/gnss_observationset/gnss_observationset.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/gnss_observationset_queryhelp_response.py">GnssObservationsetQueryhelpResponse</a></code>
- <code title="get /udl/gnssobservationset/tuple">client.gnss_observationset.<a href="./src/unifieddatalibrary/resources/gnss_observationset/gnss_observationset.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/gnss_observationset_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/gnss_observationset_tuple_response.py">GnssObservationsetTupleResponse</a></code>
- <code title="post /filedrop/udl-gnssobset">client.gnss_observationset.<a href="./src/unifieddatalibrary/resources/gnss_observationset/gnss_observationset.py">unvalidated_publish</a>(\*\*<a href="src/unifieddatalibrary/types/gnss_observationset_unvalidated_publish_params.py">params</a>) -> None</code>

## History

Types:

```python
from unifieddatalibrary.types.gnss_observationset import GnssObservationSetFull
```

Methods:

- <code title="get /udl/gnssobservationset/history">client.gnss_observationset.history.<a href="./src/unifieddatalibrary/resources/gnss_observationset/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/gnss_observationset/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/gnss_observationset/gnss_observation_set_full.py">SyncOffsetPage[GnssObservationSetFull]</a></code>
- <code title="get /udl/gnssobservationset/history/aodr">client.gnss_observationset.history.<a href="./src/unifieddatalibrary/resources/gnss_observationset/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/gnss_observationset/history_aodr_params.py">params</a>) -> None</code>

# GnssRawIf

Types:

```python
from unifieddatalibrary.types import (
    GnssRawIfListResponse,
    GnssRawIfCountResponse,
    GnssRawIfGetResponse,
    GnssRawIfQueryhelpResponse,
    GnssRawIfTupleResponse,
)
```

Methods:

- <code title="get /udl/gnssrawif">client.gnss_raw_if.<a href="./src/unifieddatalibrary/resources/gnss_raw_if/gnss_raw_if.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/gnss_raw_if_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/gnss_raw_if_list_response.py">SyncOffsetPage[GnssRawIfListResponse]</a></code>
- <code title="get /udl/gnssrawif/count">client.gnss_raw_if.<a href="./src/unifieddatalibrary/resources/gnss_raw_if/gnss_raw_if.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/gnss_raw_if_count_params.py">params</a>) -> str</code>
- <code title="get /udl/gnssrawif/getFile/{id}">client.gnss_raw_if.<a href="./src/unifieddatalibrary/resources/gnss_raw_if/gnss_raw_if.py">file_get</a>(id, \*\*<a href="src/unifieddatalibrary/types/gnss_raw_if_file_get_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="get /udl/gnssrawif/{id}">client.gnss_raw_if.<a href="./src/unifieddatalibrary/resources/gnss_raw_if/gnss_raw_if.py">get</a>(id, \*\*<a href="src/unifieddatalibrary/types/gnss_raw_if_get_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/gnss_raw_if_get_response.py">GnssRawIfGetResponse</a></code>
- <code title="get /udl/gnssrawif/queryhelp">client.gnss_raw_if.<a href="./src/unifieddatalibrary/resources/gnss_raw_if/gnss_raw_if.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/gnss_raw_if_queryhelp_response.py">GnssRawIfQueryhelpResponse</a></code>
- <code title="get /udl/gnssrawif/tuple">client.gnss_raw_if.<a href="./src/unifieddatalibrary/resources/gnss_raw_if/gnss_raw_if.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/gnss_raw_if_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/gnss_raw_if_tuple_response.py">GnssRawIfTupleResponse</a></code>
- <code title="post /filedrop/udl-gnssrawif">client.gnss_raw_if.<a href="./src/unifieddatalibrary/resources/gnss_raw_if/gnss_raw_if.py">upload_zip</a>(\*\*<a href="src/unifieddatalibrary/types/gnss_raw_if_upload_zip_params.py">params</a>) -> None</code>

## History

Types:

```python
from unifieddatalibrary.types.gnss_raw_if import HistoryListResponse, HistoryCountResponse
```

Methods:

- <code title="get /udl/gnssrawif/history">client.gnss_raw_if.history.<a href="./src/unifieddatalibrary/resources/gnss_raw_if/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/gnss_raw_if/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/gnss_raw_if/history_list_response.py">SyncOffsetPage[HistoryListResponse]</a></code>
- <code title="get /udl/gnssrawif/history/aodr">client.gnss_raw_if.history.<a href="./src/unifieddatalibrary/resources/gnss_raw_if/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/gnss_raw_if/history_aodr_params.py">params</a>) -> None</code>
- <code title="get /udl/gnssrawif/history/count">client.gnss_raw_if.history.<a href="./src/unifieddatalibrary/resources/gnss_raw_if/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/gnss_raw_if/history_count_params.py">params</a>) -> str</code>

# GroundImagery

Types:

```python
from unifieddatalibrary.types import (
    GroundImageryListResponse,
    GroundImageryCountResponse,
    GroundImageryGetResponse,
    GroundImageryQueryhelpResponse,
    GroundImageryTupleResponse,
)
```

Methods:

- <code title="post /udl/groundimagery">client.ground_imagery.<a href="./src/unifieddatalibrary/resources/ground_imagery/ground_imagery.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/ground_imagery_create_params.py">params</a>) -> None</code>
- <code title="get /udl/groundimagery">client.ground_imagery.<a href="./src/unifieddatalibrary/resources/ground_imagery/ground_imagery.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/ground_imagery_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/ground_imagery_list_response.py">SyncOffsetPage[GroundImageryListResponse]</a></code>
- <code title="get /udl/groundimagery/history/aodr">client.ground_imagery.<a href="./src/unifieddatalibrary/resources/ground_imagery/ground_imagery.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/ground_imagery_aodr_params.py">params</a>) -> None</code>
- <code title="get /udl/groundimagery/count">client.ground_imagery.<a href="./src/unifieddatalibrary/resources/ground_imagery/ground_imagery.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/ground_imagery_count_params.py">params</a>) -> str</code>
- <code title="get /udl/groundimagery/{id}">client.ground_imagery.<a href="./src/unifieddatalibrary/resources/ground_imagery/ground_imagery.py">get</a>(id, \*\*<a href="src/unifieddatalibrary/types/ground_imagery_get_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/ground_imagery_get_response.py">GroundImageryGetResponse</a></code>
- <code title="get /udl/groundimagery/getFile/{id}">client.ground_imagery.<a href="./src/unifieddatalibrary/resources/ground_imagery/ground_imagery.py">get_file</a>(id, \*\*<a href="src/unifieddatalibrary/types/ground_imagery_get_file_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="get /udl/groundimagery/queryhelp">client.ground_imagery.<a href="./src/unifieddatalibrary/resources/ground_imagery/ground_imagery.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/ground_imagery_queryhelp_response.py">GroundImageryQueryhelpResponse</a></code>
- <code title="get /udl/groundimagery/tuple">client.ground_imagery.<a href="./src/unifieddatalibrary/resources/ground_imagery/ground_imagery.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/ground_imagery_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/ground_imagery_tuple_response.py">GroundImageryTupleResponse</a></code>
- <code title="post /filedrop/udl-groundimagery">client.ground_imagery.<a href="./src/unifieddatalibrary/resources/ground_imagery/ground_imagery.py">upload_zip</a>(\*\*<a href="src/unifieddatalibrary/types/ground_imagery_upload_zip_params.py">params</a>) -> None</code>

## History

Types:

```python
from unifieddatalibrary.types.ground_imagery import HistoryListResponse, HistoryCountResponse
```

Methods:

- <code title="get /udl/groundimagery/history">client.ground_imagery.history.<a href="./src/unifieddatalibrary/resources/ground_imagery/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/ground_imagery/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/ground_imagery/history_list_response.py">SyncOffsetPage[HistoryListResponse]</a></code>
- <code title="get /udl/groundimagery/history/count">client.ground_imagery.history.<a href="./src/unifieddatalibrary/resources/ground_imagery/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/ground_imagery/history_count_params.py">params</a>) -> str</code>

# H3Geo

Types:

```python
from unifieddatalibrary.types import (
    H3GeoListResponse,
    H3GeoCountResponse,
    H3GeoGetResponse,
    H3GeoQueryhelpResponse,
    H3GeoTupleResponse,
)
```

Methods:

- <code title="post /udl/h3geo">client.h3_geo.<a href="./src/unifieddatalibrary/resources/h3_geo/h3_geo.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/h3_geo_create_params.py">params</a>) -> None</code>
- <code title="get /udl/h3geo">client.h3_geo.<a href="./src/unifieddatalibrary/resources/h3_geo/h3_geo.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/h3_geo_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/h3_geo_list_response.py">SyncOffsetPage[H3GeoListResponse]</a></code>
- <code title="get /udl/h3geo/count">client.h3_geo.<a href="./src/unifieddatalibrary/resources/h3_geo/h3_geo.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/h3_geo_count_params.py">params</a>) -> str</code>
- <code title="get /udl/h3geo/{id}">client.h3_geo.<a href="./src/unifieddatalibrary/resources/h3_geo/h3_geo.py">get</a>(id, \*\*<a href="src/unifieddatalibrary/types/h3_geo_get_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/h3_geo_get_response.py">H3GeoGetResponse</a></code>
- <code title="get /udl/h3geo/queryhelp">client.h3_geo.<a href="./src/unifieddatalibrary/resources/h3_geo/h3_geo.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/h3_geo_queryhelp_response.py">H3GeoQueryhelpResponse</a></code>
- <code title="get /udl/h3geo/tuple">client.h3_geo.<a href="./src/unifieddatalibrary/resources/h3_geo/h3_geo.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/h3_geo_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/h3_geo_tuple_response.py">H3GeoTupleResponse</a></code>

## History

Types:

```python
from unifieddatalibrary.types.h3_geo import HistoryListResponse, HistoryCountResponse
```

Methods:

- <code title="get /udl/h3geo/history">client.h3_geo.history.<a href="./src/unifieddatalibrary/resources/h3_geo/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/h3_geo/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/h3_geo/history_list_response.py">SyncOffsetPage[HistoryListResponse]</a></code>
- <code title="get /udl/h3geo/history/aodr">client.h3_geo.history.<a href="./src/unifieddatalibrary/resources/h3_geo/history.py">ador</a>(\*\*<a href="src/unifieddatalibrary/types/h3_geo/history_ador_params.py">params</a>) -> None</code>
- <code title="get /udl/h3geo/history/count">client.h3_geo.history.<a href="./src/unifieddatalibrary/resources/h3_geo/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/h3_geo/history_count_params.py">params</a>) -> str</code>

# H3GeoHexCell

Types:

```python
from unifieddatalibrary.types import (
    H3GeoHexCellListResponse,
    H3GeoHexCellCountResponse,
    H3GeoHexCellQueryhelpResponse,
    H3GeoHexCellTupleResponse,
)
```

Methods:

- <code title="get /udl/h3geohexcell">client.h3_geo_hex_cell.<a href="./src/unifieddatalibrary/resources/h3_geo_hex_cell.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/h3_geo_hex_cell_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/h3_geo_hex_cell_list_response.py">SyncOffsetPage[H3GeoHexCellListResponse]</a></code>
- <code title="get /udl/h3geohexcell/count">client.h3_geo_hex_cell.<a href="./src/unifieddatalibrary/resources/h3_geo_hex_cell.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/h3_geo_hex_cell_count_params.py">params</a>) -> str</code>
- <code title="get /udl/h3geohexcell/queryhelp">client.h3_geo_hex_cell.<a href="./src/unifieddatalibrary/resources/h3_geo_hex_cell.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/h3_geo_hex_cell_queryhelp_response.py">H3GeoHexCellQueryhelpResponse</a></code>
- <code title="get /udl/h3geohexcell/tuple">client.h3_geo_hex_cell.<a href="./src/unifieddatalibrary/resources/h3_geo_hex_cell.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/h3_geo_hex_cell_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/h3_geo_hex_cell_tuple_response.py">H3GeoHexCellTupleResponse</a></code>

# Hazard

Types:

```python
from unifieddatalibrary.types import (
    HazardListResponse,
    HazardCountResponse,
    HazardGetResponse,
    HazardQueryhelpResponse,
    HazardTupleResponse,
)
```

Methods:

- <code title="post /udl/hazard">client.hazard.<a href="./src/unifieddatalibrary/resources/hazard/hazard.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/hazard_create_params.py">params</a>) -> None</code>
- <code title="get /udl/hazard">client.hazard.<a href="./src/unifieddatalibrary/resources/hazard/hazard.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/hazard_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/hazard_list_response.py">SyncOffsetPage[HazardListResponse]</a></code>
- <code title="get /udl/hazard/count">client.hazard.<a href="./src/unifieddatalibrary/resources/hazard/hazard.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/hazard_count_params.py">params</a>) -> str</code>
- <code title="post /udl/hazard/createBulk">client.hazard.<a href="./src/unifieddatalibrary/resources/hazard/hazard.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/hazard_create_bulk_params.py">params</a>) -> None</code>
- <code title="get /udl/hazard/{id}">client.hazard.<a href="./src/unifieddatalibrary/resources/hazard/hazard.py">get</a>(id, \*\*<a href="src/unifieddatalibrary/types/hazard_get_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/hazard_get_response.py">HazardGetResponse</a></code>
- <code title="get /udl/hazard/queryhelp">client.hazard.<a href="./src/unifieddatalibrary/resources/hazard/hazard.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/hazard_queryhelp_response.py">HazardQueryhelpResponse</a></code>
- <code title="get /udl/hazard/tuple">client.hazard.<a href="./src/unifieddatalibrary/resources/hazard/hazard.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/hazard_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/hazard_tuple_response.py">HazardTupleResponse</a></code>

## History

Types:

```python
from unifieddatalibrary.types.hazard import HistoryListResponse, HistoryCountResponse
```

Methods:

- <code title="get /udl/hazard/history">client.hazard.history.<a href="./src/unifieddatalibrary/resources/hazard/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/hazard/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/hazard/history_list_response.py">SyncOffsetPage[HistoryListResponse]</a></code>
- <code title="get /udl/hazard/history/aodr">client.hazard.history.<a href="./src/unifieddatalibrary/resources/hazard/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/hazard/history_aodr_params.py">params</a>) -> None</code>
- <code title="get /udl/hazard/history/count">client.hazard.history.<a href="./src/unifieddatalibrary/resources/hazard/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/hazard/history_count_params.py">params</a>) -> str</code>

# IonoObservations

Types:

```python
from unifieddatalibrary.types import (
    IonoObservationListResponse,
    IonoObservationCountResponse,
    IonoObservationQueryhelpResponse,
    IonoObservationTupleResponse,
)
```

Methods:

- <code title="get /udl/ionoobservation">client.iono_observations.<a href="./src/unifieddatalibrary/resources/iono_observations/iono_observations.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/iono_observation_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/iono_observation_list_response.py">SyncOffsetPage[IonoObservationListResponse]</a></code>
- <code title="get /udl/ionoobservation/count">client.iono_observations.<a href="./src/unifieddatalibrary/resources/iono_observations/iono_observations.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/iono_observation_count_params.py">params</a>) -> str</code>
- <code title="post /udl/ionoobservation/createBulk">client.iono_observations.<a href="./src/unifieddatalibrary/resources/iono_observations/iono_observations.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/iono_observation_create_bulk_params.py">params</a>) -> None</code>
- <code title="get /udl/ionoobservation/queryhelp">client.iono_observations.<a href="./src/unifieddatalibrary/resources/iono_observations/iono_observations.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/iono_observation_queryhelp_response.py">IonoObservationQueryhelpResponse</a></code>
- <code title="get /udl/ionoobservation/tuple">client.iono_observations.<a href="./src/unifieddatalibrary/resources/iono_observations/iono_observations.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/iono_observation_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/iono_observation_tuple_response.py">IonoObservationTupleResponse</a></code>
- <code title="post /filedrop/udl-ionoobs">client.iono_observations.<a href="./src/unifieddatalibrary/resources/iono_observations/iono_observations.py">unvalidated_publish</a>(\*\*<a href="src/unifieddatalibrary/types/iono_observation_unvalidated_publish_params.py">params</a>) -> None</code>

## History

Types:

```python
from unifieddatalibrary.types.iono_observations import HistoryListResponse, HistoryCountResponse
```

Methods:

- <code title="get /udl/ionoobservation/history">client.iono_observations.history.<a href="./src/unifieddatalibrary/resources/iono_observations/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/iono_observations/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/iono_observations/history_list_response.py">SyncOffsetPage[HistoryListResponse]</a></code>
- <code title="get /udl/ionoobservation/history/aodr">client.iono_observations.history.<a href="./src/unifieddatalibrary/resources/iono_observations/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/iono_observations/history_aodr_params.py">params</a>) -> None</code>
- <code title="get /udl/ionoobservation/history/count">client.iono_observations.history.<a href="./src/unifieddatalibrary/resources/iono_observations/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/iono_observations/history_count_params.py">params</a>) -> str</code>

# Ir

Types:

```python
from unifieddatalibrary.types import (
    IrListResponse,
    IrCountResponse,
    IrGetResponse,
    IrQueryhelpResponse,
    IrTupleResponse,
)
```

Methods:

- <code title="post /udl/ir">client.ir.<a href="./src/unifieddatalibrary/resources/ir.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/ir_create_params.py">params</a>) -> None</code>
- <code title="put /udl/ir/{id}">client.ir.<a href="./src/unifieddatalibrary/resources/ir.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/ir_update_params.py">params</a>) -> None</code>
- <code title="get /udl/ir">client.ir.<a href="./src/unifieddatalibrary/resources/ir.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/ir_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/ir_list_response.py">SyncOffsetPage[IrListResponse]</a></code>
- <code title="delete /udl/ir/{id}">client.ir.<a href="./src/unifieddatalibrary/resources/ir.py">delete</a>(id) -> None</code>
- <code title="get /udl/ir/count">client.ir.<a href="./src/unifieddatalibrary/resources/ir.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/ir_count_params.py">params</a>) -> str</code>
- <code title="get /udl/ir/{id}">client.ir.<a href="./src/unifieddatalibrary/resources/ir.py">get</a>(id, \*\*<a href="src/unifieddatalibrary/types/ir_get_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/ir_get_response.py">IrGetResponse</a></code>
- <code title="get /udl/ir/queryhelp">client.ir.<a href="./src/unifieddatalibrary/resources/ir.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/ir_queryhelp_response.py">IrQueryhelpResponse</a></code>
- <code title="get /udl/ir/tuple">client.ir.<a href="./src/unifieddatalibrary/resources/ir.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/ir_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/ir_tuple_response.py">IrTupleResponse</a></code>

# IsrCollections

Types:

```python
from unifieddatalibrary.types import (
    IsrCollectionCriticalTimesFull,
    IsrCollectionExploitationRequirementFull,
    IsrCollectionPocFull,
    IsrCollectionRequirementsFull,
    IsrCollectionListResponse,
    IsrCollectionCountResponse,
    IsrCollectionQueryhelpResponse,
    IsrCollectionTupleResponse,
)
```

Methods:

- <code title="get /udl/isrcollection">client.isr_collections.<a href="./src/unifieddatalibrary/resources/isr_collections/isr_collections.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/isr_collection_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/isr_collection_list_response.py">SyncOffsetPage[IsrCollectionListResponse]</a></code>
- <code title="get /udl/isrcollection/count">client.isr_collections.<a href="./src/unifieddatalibrary/resources/isr_collections/isr_collections.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/isr_collection_count_params.py">params</a>) -> str</code>
- <code title="post /udl/isrcollection/createBulk">client.isr_collections.<a href="./src/unifieddatalibrary/resources/isr_collections/isr_collections.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/isr_collection_create_bulk_params.py">params</a>) -> None</code>
- <code title="get /udl/isrcollection/queryhelp">client.isr_collections.<a href="./src/unifieddatalibrary/resources/isr_collections/isr_collections.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/isr_collection_queryhelp_response.py">IsrCollectionQueryhelpResponse</a></code>
- <code title="get /udl/isrcollection/tuple">client.isr_collections.<a href="./src/unifieddatalibrary/resources/isr_collections/isr_collections.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/isr_collection_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/isr_collection_tuple_response.py">IsrCollectionTupleResponse</a></code>
- <code title="post /filedrop/udl-isrcollection">client.isr_collections.<a href="./src/unifieddatalibrary/resources/isr_collections/isr_collections.py">unvalidated_publish</a>(\*\*<a href="src/unifieddatalibrary/types/isr_collection_unvalidated_publish_params.py">params</a>) -> None</code>

## History

Types:

```python
from unifieddatalibrary.types.isr_collections import HistoryListResponse, HistoryCountResponse
```

Methods:

- <code title="get /udl/isrcollection/history">client.isr_collections.history.<a href="./src/unifieddatalibrary/resources/isr_collections/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/isr_collections/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/isr_collections/history_list_response.py">SyncOffsetPage[HistoryListResponse]</a></code>
- <code title="get /udl/isrcollection/history/aodr">client.isr_collections.history.<a href="./src/unifieddatalibrary/resources/isr_collections/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/isr_collections/history_aodr_params.py">params</a>) -> None</code>
- <code title="get /udl/isrcollection/history/count">client.isr_collections.history.<a href="./src/unifieddatalibrary/resources/isr_collections/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/isr_collections/history_count_params.py">params</a>) -> str</code>

# Item

Types:

```python
from unifieddatalibrary.types import (
    ItemListResponse,
    ItemCountResponse,
    ItemGetResponse,
    ItemQueryhelpResponse,
    ItemTupleResponse,
)
```

Methods:

- <code title="post /udl/item">client.item.<a href="./src/unifieddatalibrary/resources/item.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/item_create_params.py">params</a>) -> None</code>
- <code title="put /udl/item/{id}">client.item.<a href="./src/unifieddatalibrary/resources/item.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/item_update_params.py">params</a>) -> None</code>
- <code title="get /udl/item">client.item.<a href="./src/unifieddatalibrary/resources/item.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/item_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/item_list_response.py">SyncOffsetPage[ItemListResponse]</a></code>
- <code title="delete /udl/item/{id}">client.item.<a href="./src/unifieddatalibrary/resources/item.py">delete</a>(id) -> None</code>
- <code title="get /udl/item/count">client.item.<a href="./src/unifieddatalibrary/resources/item.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/item_count_params.py">params</a>) -> str</code>
- <code title="get /udl/item/{id}">client.item.<a href="./src/unifieddatalibrary/resources/item.py">get</a>(id, \*\*<a href="src/unifieddatalibrary/types/item_get_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/item_get_response.py">ItemGetResponse</a></code>
- <code title="get /udl/item/queryhelp">client.item.<a href="./src/unifieddatalibrary/resources/item.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/item_queryhelp_response.py">ItemQueryhelpResponse</a></code>
- <code title="get /udl/item/tuple">client.item.<a href="./src/unifieddatalibrary/resources/item.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/item_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/item_tuple_response.py">ItemTupleResponse</a></code>
- <code title="post /filedrop/udl-item">client.item.<a href="./src/unifieddatalibrary/resources/item.py">unvalidated_publish</a>(\*\*<a href="src/unifieddatalibrary/types/item_unvalidated_publish_params.py">params</a>) -> None</code>

# ItemTrackings

Types:

```python
from unifieddatalibrary.types import (
    ItemTrackingListResponse,
    ItemTrackingCountResponse,
    ItemTrackingGetResponse,
    ItemTrackingQueryhelpResponse,
    ItemTrackingTupleResponse,
)
```

Methods:

- <code title="post /udl/itemtracking">client.item_trackings.<a href="./src/unifieddatalibrary/resources/item_trackings/item_trackings.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/item_tracking_create_params.py">params</a>) -> None</code>
- <code title="get /udl/itemtracking">client.item_trackings.<a href="./src/unifieddatalibrary/resources/item_trackings/item_trackings.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/item_tracking_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/item_tracking_list_response.py">SyncOffsetPage[ItemTrackingListResponse]</a></code>
- <code title="delete /udl/itemtracking/{id}">client.item_trackings.<a href="./src/unifieddatalibrary/resources/item_trackings/item_trackings.py">delete</a>(id) -> None</code>
- <code title="get /udl/itemtracking/count">client.item_trackings.<a href="./src/unifieddatalibrary/resources/item_trackings/item_trackings.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/item_tracking_count_params.py">params</a>) -> str</code>
- <code title="get /udl/itemtracking/{id}">client.item_trackings.<a href="./src/unifieddatalibrary/resources/item_trackings/item_trackings.py">get</a>(id, \*\*<a href="src/unifieddatalibrary/types/item_tracking_get_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/item_tracking_get_response.py">ItemTrackingGetResponse</a></code>
- <code title="get /udl/itemtracking/queryhelp">client.item_trackings.<a href="./src/unifieddatalibrary/resources/item_trackings/item_trackings.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/item_tracking_queryhelp_response.py">ItemTrackingQueryhelpResponse</a></code>
- <code title="get /udl/itemtracking/tuple">client.item_trackings.<a href="./src/unifieddatalibrary/resources/item_trackings/item_trackings.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/item_tracking_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/item_tracking_tuple_response.py">ItemTrackingTupleResponse</a></code>
- <code title="post /filedrop/udl-itemtracking">client.item_trackings.<a href="./src/unifieddatalibrary/resources/item_trackings/item_trackings.py">unvalidated_publish</a>(\*\*<a href="src/unifieddatalibrary/types/item_tracking_unvalidated_publish_params.py">params</a>) -> None</code>

## History

Types:

```python
from unifieddatalibrary.types.item_trackings import HistoryListResponse, HistoryCountResponse
```

Methods:

- <code title="get /udl/itemtracking/history">client.item_trackings.history.<a href="./src/unifieddatalibrary/resources/item_trackings/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/item_trackings/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/item_trackings/history_list_response.py">SyncOffsetPage[HistoryListResponse]</a></code>
- <code title="get /udl/itemtracking/history/count">client.item_trackings.history.<a href="./src/unifieddatalibrary/resources/item_trackings/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/item_trackings/history_count_params.py">params</a>) -> str</code>

# Laserdeconflictrequest

Types:

```python
from unifieddatalibrary.types import (
    FixedPointFull,
    LaserdeconflictrequestListResponse,
    LaserdeconflictrequestCountResponse,
    LaserdeconflictrequestGetResponse,
    LaserdeconflictrequestQueryhelpResponse,
    LaserdeconflictrequestTupleResponse,
)
```

Methods:

- <code title="post /udl/laserdeconflictrequest">client.laserdeconflictrequest.<a href="./src/unifieddatalibrary/resources/laserdeconflictrequest/laserdeconflictrequest.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/laserdeconflictrequest_create_params.py">params</a>) -> None</code>
- <code title="get /udl/laserdeconflictrequest">client.laserdeconflictrequest.<a href="./src/unifieddatalibrary/resources/laserdeconflictrequest/laserdeconflictrequest.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/laserdeconflictrequest_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/laserdeconflictrequest_list_response.py">SyncOffsetPage[LaserdeconflictrequestListResponse]</a></code>
- <code title="get /udl/laserdeconflictrequest/count">client.laserdeconflictrequest.<a href="./src/unifieddatalibrary/resources/laserdeconflictrequest/laserdeconflictrequest.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/laserdeconflictrequest_count_params.py">params</a>) -> str</code>
- <code title="get /udl/laserdeconflictrequest/{id}">client.laserdeconflictrequest.<a href="./src/unifieddatalibrary/resources/laserdeconflictrequest/laserdeconflictrequest.py">get</a>(id, \*\*<a href="src/unifieddatalibrary/types/laserdeconflictrequest_get_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/laserdeconflictrequest_get_response.py">LaserdeconflictrequestGetResponse</a></code>
- <code title="get /udl/laserdeconflictrequest/queryhelp">client.laserdeconflictrequest.<a href="./src/unifieddatalibrary/resources/laserdeconflictrequest/laserdeconflictrequest.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/laserdeconflictrequest_queryhelp_response.py">LaserdeconflictrequestQueryhelpResponse</a></code>
- <code title="get /udl/laserdeconflictrequest/tuple">client.laserdeconflictrequest.<a href="./src/unifieddatalibrary/resources/laserdeconflictrequest/laserdeconflictrequest.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/laserdeconflictrequest_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/laserdeconflictrequest_tuple_response.py">LaserdeconflictrequestTupleResponse</a></code>
- <code title="post /filedrop/udl-laserdeconflictrequest">client.laserdeconflictrequest.<a href="./src/unifieddatalibrary/resources/laserdeconflictrequest/laserdeconflictrequest.py">unvalidated_publish</a>(\*\*<a href="src/unifieddatalibrary/types/laserdeconflictrequest_unvalidated_publish_params.py">params</a>) -> None</code>

## History

Types:

```python
from unifieddatalibrary.types.laserdeconflictrequest import (
    HistoryListResponse,
    HistoryCountResponse,
)
```

Methods:

- <code title="get /udl/laserdeconflictrequest/history">client.laserdeconflictrequest.history.<a href="./src/unifieddatalibrary/resources/laserdeconflictrequest/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/laserdeconflictrequest/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/laserdeconflictrequest/history_list_response.py">SyncOffsetPage[HistoryListResponse]</a></code>
- <code title="get /udl/laserdeconflictrequest/history/aodr">client.laserdeconflictrequest.history.<a href="./src/unifieddatalibrary/resources/laserdeconflictrequest/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/laserdeconflictrequest/history_aodr_params.py">params</a>) -> None</code>
- <code title="get /udl/laserdeconflictrequest/history/count">client.laserdeconflictrequest.history.<a href="./src/unifieddatalibrary/resources/laserdeconflictrequest/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/laserdeconflictrequest/history_count_params.py">params</a>) -> str</code>

# Laseremitter

Types:

```python
from unifieddatalibrary.types import (
    LaseremitterListResponse,
    LaseremitterCountResponse,
    LaseremitterGetResponse,
    LaseremitterQueryhelpResponse,
    LaseremitterTupleResponse,
)
```

Methods:

- <code title="post /udl/laseremitter">client.laseremitter.<a href="./src/unifieddatalibrary/resources/laseremitter/laseremitter.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/laseremitter_create_params.py">params</a>) -> None</code>
- <code title="put /udl/laseremitter/{id}">client.laseremitter.<a href="./src/unifieddatalibrary/resources/laseremitter/laseremitter.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/laseremitter_update_params.py">params</a>) -> None</code>
- <code title="get /udl/laseremitter">client.laseremitter.<a href="./src/unifieddatalibrary/resources/laseremitter/laseremitter.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/laseremitter_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/laseremitter_list_response.py">SyncOffsetPage[LaseremitterListResponse]</a></code>
- <code title="delete /udl/laseremitter/{id}">client.laseremitter.<a href="./src/unifieddatalibrary/resources/laseremitter/laseremitter.py">delete</a>(id) -> None</code>
- <code title="get /udl/laseremitter/count">client.laseremitter.<a href="./src/unifieddatalibrary/resources/laseremitter/laseremitter.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/laseremitter_count_params.py">params</a>) -> str</code>
- <code title="get /udl/laseremitter/{id}">client.laseremitter.<a href="./src/unifieddatalibrary/resources/laseremitter/laseremitter.py">get</a>(id, \*\*<a href="src/unifieddatalibrary/types/laseremitter_get_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/laseremitter_get_response.py">LaseremitterGetResponse</a></code>
- <code title="get /udl/laseremitter/queryhelp">client.laseremitter.<a href="./src/unifieddatalibrary/resources/laseremitter/laseremitter.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/laseremitter_queryhelp_response.py">LaseremitterQueryhelpResponse</a></code>
- <code title="get /udl/laseremitter/tuple">client.laseremitter.<a href="./src/unifieddatalibrary/resources/laseremitter/laseremitter.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/laseremitter_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/laseremitter_tuple_response.py">LaseremitterTupleResponse</a></code>

## Staging

Types:

```python
from unifieddatalibrary.types.laseremitter import (
    StagingRetrieveResponse,
    StagingListResponse,
    StagingQueryhelpResponse,
)
```

Methods:

- <code title="post /udl/laseremitterstaging">client.laseremitter.staging.<a href="./src/unifieddatalibrary/resources/laseremitter/staging.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/laseremitter/staging_create_params.py">params</a>) -> None</code>
- <code title="get /udl/laseremitterstaging/{id}">client.laseremitter.staging.<a href="./src/unifieddatalibrary/resources/laseremitter/staging.py">retrieve</a>(id, \*\*<a href="src/unifieddatalibrary/types/laseremitter/staging_retrieve_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/laseremitter/staging_retrieve_response.py">StagingRetrieveResponse</a></code>
- <code title="put /udl/laseremitterstaging/{id}">client.laseremitter.staging.<a href="./src/unifieddatalibrary/resources/laseremitter/staging.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/laseremitter/staging_update_params.py">params</a>) -> None</code>
- <code title="get /udl/laseremitterstaging">client.laseremitter.staging.<a href="./src/unifieddatalibrary/resources/laseremitter/staging.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/laseremitter/staging_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/laseremitter/staging_list_response.py">SyncOffsetPage[StagingListResponse]</a></code>
- <code title="delete /udl/laseremitterstaging/{id}">client.laseremitter.staging.<a href="./src/unifieddatalibrary/resources/laseremitter/staging.py">delete</a>(id) -> None</code>
- <code title="post /udl/laseremitterstaging/createBulk">client.laseremitter.staging.<a href="./src/unifieddatalibrary/resources/laseremitter/staging.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/laseremitter/staging_create_bulk_params.py">params</a>) -> None</code>
- <code title="get /udl/laseremitterstaging/queryhelp">client.laseremitter.staging.<a href="./src/unifieddatalibrary/resources/laseremitter/staging.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/laseremitter/staging_queryhelp_response.py">StagingQueryhelpResponse</a></code>

# LaunchDetection

Types:

```python
from unifieddatalibrary.types import (
    LaunchDetectionListResponse,
    LaunchDetectionCountResponse,
    LaunchDetectionGetResponse,
    LaunchDetectionQueryhelpResponse,
    LaunchDetectionTupleResponse,
)
```

Methods:

- <code title="post /udl/launchdetection">client.launch_detection.<a href="./src/unifieddatalibrary/resources/launch_detection.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/launch_detection_create_params.py">params</a>) -> None</code>
- <code title="put /udl/launchdetection/{id}">client.launch_detection.<a href="./src/unifieddatalibrary/resources/launch_detection.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/launch_detection_update_params.py">params</a>) -> None</code>
- <code title="get /udl/launchdetection">client.launch_detection.<a href="./src/unifieddatalibrary/resources/launch_detection.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/launch_detection_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/launch_detection_list_response.py">SyncOffsetPage[LaunchDetectionListResponse]</a></code>
- <code title="delete /udl/launchdetection/{id}">client.launch_detection.<a href="./src/unifieddatalibrary/resources/launch_detection.py">delete</a>(id) -> None</code>
- <code title="get /udl/launchdetection/count">client.launch_detection.<a href="./src/unifieddatalibrary/resources/launch_detection.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/launch_detection_count_params.py">params</a>) -> str</code>
- <code title="get /udl/launchdetection/{id}">client.launch_detection.<a href="./src/unifieddatalibrary/resources/launch_detection.py">get</a>(id, \*\*<a href="src/unifieddatalibrary/types/launch_detection_get_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/launch_detection_get_response.py">LaunchDetectionGetResponse</a></code>
- <code title="get /udl/launchdetection/queryhelp">client.launch_detection.<a href="./src/unifieddatalibrary/resources/launch_detection.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/launch_detection_queryhelp_response.py">LaunchDetectionQueryhelpResponse</a></code>
- <code title="get /udl/launchdetection/tuple">client.launch_detection.<a href="./src/unifieddatalibrary/resources/launch_detection.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/launch_detection_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/launch_detection_tuple_response.py">LaunchDetectionTupleResponse</a></code>

# LaunchEvent

Types:

```python
from unifieddatalibrary.types import (
    LaunchEventListResponse,
    LaunchEventCountResponse,
    LaunchEventGetResponse,
    LaunchEventQueryhelpResponse,
    LaunchEventTupleResponse,
)
```

Methods:

- <code title="post /udl/launchevent">client.launch_event.<a href="./src/unifieddatalibrary/resources/launch_event/launch_event.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/launch_event_create_params.py">params</a>) -> None</code>
- <code title="get /udl/launchevent">client.launch_event.<a href="./src/unifieddatalibrary/resources/launch_event/launch_event.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/launch_event_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/launch_event_list_response.py">SyncOffsetPage[LaunchEventListResponse]</a></code>
- <code title="get /udl/launchevent/count">client.launch_event.<a href="./src/unifieddatalibrary/resources/launch_event/launch_event.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/launch_event_count_params.py">params</a>) -> str</code>
- <code title="post /udl/launchevent/createBulk">client.launch_event.<a href="./src/unifieddatalibrary/resources/launch_event/launch_event.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/launch_event_create_bulk_params.py">params</a>) -> None</code>
- <code title="get /udl/launchevent/{id}">client.launch_event.<a href="./src/unifieddatalibrary/resources/launch_event/launch_event.py">get</a>(id, \*\*<a href="src/unifieddatalibrary/types/launch_event_get_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/launch_event_get_response.py">LaunchEventGetResponse</a></code>
- <code title="get /udl/launchevent/queryhelp">client.launch_event.<a href="./src/unifieddatalibrary/resources/launch_event/launch_event.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/launch_event_queryhelp_response.py">LaunchEventQueryhelpResponse</a></code>
- <code title="get /udl/launchevent/tuple">client.launch_event.<a href="./src/unifieddatalibrary/resources/launch_event/launch_event.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/launch_event_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/launch_event_tuple_response.py">LaunchEventTupleResponse</a></code>
- <code title="post /filedrop/udl-launchevent">client.launch_event.<a href="./src/unifieddatalibrary/resources/launch_event/launch_event.py">unvalidated_publish</a>(\*\*<a href="src/unifieddatalibrary/types/launch_event_unvalidated_publish_params.py">params</a>) -> None</code>

## History

Types:

```python
from unifieddatalibrary.types.launch_event import HistoryListResponse, HistoryCountResponse
```

Methods:

- <code title="get /udl/launchevent/history">client.launch_event.history.<a href="./src/unifieddatalibrary/resources/launch_event/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/launch_event/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/launch_event/history_list_response.py">SyncOffsetPage[HistoryListResponse]</a></code>
- <code title="get /udl/launchevent/history/aodr">client.launch_event.history.<a href="./src/unifieddatalibrary/resources/launch_event/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/launch_event/history_aodr_params.py">params</a>) -> None</code>
- <code title="get /udl/launchevent/history/count">client.launch_event.history.<a href="./src/unifieddatalibrary/resources/launch_event/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/launch_event/history_count_params.py">params</a>) -> str</code>

# LaunchSite

Types:

```python
from unifieddatalibrary.types import (
    LaunchSiteListResponse,
    LaunchSiteCountResponse,
    LaunchSiteGetResponse,
    LaunchSiteQueryhelpResponse,
    LaunchSiteTupleResponse,
)
```

Methods:

- <code title="post /udl/launchsite">client.launch_site.<a href="./src/unifieddatalibrary/resources/launch_site.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/launch_site_create_params.py">params</a>) -> None</code>
- <code title="put /udl/launchsite/{id}">client.launch_site.<a href="./src/unifieddatalibrary/resources/launch_site.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/launch_site_update_params.py">params</a>) -> None</code>
- <code title="get /udl/launchsite">client.launch_site.<a href="./src/unifieddatalibrary/resources/launch_site.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/launch_site_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/launch_site_list_response.py">SyncOffsetPage[LaunchSiteListResponse]</a></code>
- <code title="delete /udl/launchsite/{id}">client.launch_site.<a href="./src/unifieddatalibrary/resources/launch_site.py">delete</a>(id) -> None</code>
- <code title="get /udl/launchsite/count">client.launch_site.<a href="./src/unifieddatalibrary/resources/launch_site.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/launch_site_count_params.py">params</a>) -> str</code>
- <code title="get /udl/launchsite/{id}">client.launch_site.<a href="./src/unifieddatalibrary/resources/launch_site.py">get</a>(id, \*\*<a href="src/unifieddatalibrary/types/launch_site_get_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/launch_site_get_response.py">LaunchSiteGetResponse</a></code>
- <code title="get /udl/launchsite/queryhelp">client.launch_site.<a href="./src/unifieddatalibrary/resources/launch_site.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/launch_site_queryhelp_response.py">LaunchSiteQueryhelpResponse</a></code>
- <code title="get /udl/launchsite/tuple">client.launch_site.<a href="./src/unifieddatalibrary/resources/launch_site.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/launch_site_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/launch_site_tuple_response.py">LaunchSiteTupleResponse</a></code>

# LaunchSiteDetails

Types:

```python
from unifieddatalibrary.types import (
    LaunchSiteDetailListResponse,
    LaunchSiteDetailFindBySourceResponse,
    LaunchSiteDetailGetResponse,
)
```

Methods:

- <code title="post /udl/launchsitedetails">client.launch_site_details.<a href="./src/unifieddatalibrary/resources/launch_site_details.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/launch_site_detail_create_params.py">params</a>) -> None</code>
- <code title="put /udl/launchsitedetails/{id}">client.launch_site_details.<a href="./src/unifieddatalibrary/resources/launch_site_details.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/launch_site_detail_update_params.py">params</a>) -> None</code>
- <code title="get /udl/launchsitedetails">client.launch_site_details.<a href="./src/unifieddatalibrary/resources/launch_site_details.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/launch_site_detail_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/launch_site_detail_list_response.py">SyncOffsetPage[LaunchSiteDetailListResponse]</a></code>
- <code title="delete /udl/launchsitedetails/{id}">client.launch_site_details.<a href="./src/unifieddatalibrary/resources/launch_site_details.py">delete</a>(id) -> None</code>
- <code title="get /udl/launchsitedetails/findBySource">client.launch_site_details.<a href="./src/unifieddatalibrary/resources/launch_site_details.py">find_by_source</a>(\*\*<a href="src/unifieddatalibrary/types/launch_site_detail_find_by_source_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/launch_site_detail_find_by_source_response.py">LaunchSiteDetailFindBySourceResponse</a></code>
- <code title="get /udl/launchsitedetails/{id}">client.launch_site_details.<a href="./src/unifieddatalibrary/resources/launch_site_details.py">get</a>(id, \*\*<a href="src/unifieddatalibrary/types/launch_site_detail_get_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/launch_site_detail_get_response.py">LaunchSiteDetailGetResponse</a></code>

# LaunchVehicle

Types:

```python
from unifieddatalibrary.types import (
    LaunchVehicleListResponse,
    LaunchVehicleCountResponse,
    LaunchVehicleGetResponse,
    LaunchVehicleQueryhelpResponse,
    LaunchVehicleTupleResponse,
)
```

Methods:

- <code title="post /udl/launchvehicle">client.launch_vehicle.<a href="./src/unifieddatalibrary/resources/launch_vehicle.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/launch_vehicle_create_params.py">params</a>) -> None</code>
- <code title="put /udl/launchvehicle/{id}">client.launch_vehicle.<a href="./src/unifieddatalibrary/resources/launch_vehicle.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/launch_vehicle_update_params.py">params</a>) -> None</code>
- <code title="get /udl/launchvehicle">client.launch_vehicle.<a href="./src/unifieddatalibrary/resources/launch_vehicle.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/launch_vehicle_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/launch_vehicle_list_response.py">SyncOffsetPage[LaunchVehicleListResponse]</a></code>
- <code title="delete /udl/launchvehicle/{id}">client.launch_vehicle.<a href="./src/unifieddatalibrary/resources/launch_vehicle.py">delete</a>(id) -> None</code>
- <code title="get /udl/launchvehicle/count">client.launch_vehicle.<a href="./src/unifieddatalibrary/resources/launch_vehicle.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/launch_vehicle_count_params.py">params</a>) -> str</code>
- <code title="get /udl/launchvehicle/{id}">client.launch_vehicle.<a href="./src/unifieddatalibrary/resources/launch_vehicle.py">get</a>(id, \*\*<a href="src/unifieddatalibrary/types/launch_vehicle_get_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/launch_vehicle_get_response.py">LaunchVehicleGetResponse</a></code>
- <code title="get /udl/launchvehicle/queryhelp">client.launch_vehicle.<a href="./src/unifieddatalibrary/resources/launch_vehicle.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/launch_vehicle_queryhelp_response.py">LaunchVehicleQueryhelpResponse</a></code>
- <code title="get /udl/launchvehicle/tuple">client.launch_vehicle.<a href="./src/unifieddatalibrary/resources/launch_vehicle.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/launch_vehicle_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/launch_vehicle_tuple_response.py">LaunchVehicleTupleResponse</a></code>

# LaunchVehicleDetails

Types:

```python
from unifieddatalibrary.types import LaunchVehicleDetailListResponse, LaunchVehicleDetailGetResponse
```

Methods:

- <code title="post /udl/launchvehicledetails">client.launch_vehicle_details.<a href="./src/unifieddatalibrary/resources/launch_vehicle_details.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/launch_vehicle_detail_create_params.py">params</a>) -> None</code>
- <code title="put /udl/launchvehicledetails/{id}">client.launch_vehicle_details.<a href="./src/unifieddatalibrary/resources/launch_vehicle_details.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/launch_vehicle_detail_update_params.py">params</a>) -> None</code>
- <code title="get /udl/launchvehicledetails">client.launch_vehicle_details.<a href="./src/unifieddatalibrary/resources/launch_vehicle_details.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/launch_vehicle_detail_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/launch_vehicle_detail_list_response.py">SyncOffsetPage[LaunchVehicleDetailListResponse]</a></code>
- <code title="delete /udl/launchvehicledetails/{id}">client.launch_vehicle_details.<a href="./src/unifieddatalibrary/resources/launch_vehicle_details.py">delete</a>(id) -> None</code>
- <code title="get /udl/launchvehicledetails/{id}">client.launch_vehicle_details.<a href="./src/unifieddatalibrary/resources/launch_vehicle_details.py">get</a>(id, \*\*<a href="src/unifieddatalibrary/types/launch_vehicle_detail_get_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/launch_vehicle_detail_get_response.py">LaunchVehicleDetailGetResponse</a></code>

# LinkStatus

Types:

```python
from unifieddatalibrary.types import (
    LinkStatusListResponse,
    LinkStatusCountResponse,
    LinkStatusGetResponse,
    LinkStatusQueryhelpResponse,
    LinkStatusTupleResponse,
)
```

Methods:

- <code title="post /udl/linkstatus">client.link_status.<a href="./src/unifieddatalibrary/resources/link_status/link_status.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/link_status_create_params.py">params</a>) -> None</code>
- <code title="get /udl/linkstatus">client.link_status.<a href="./src/unifieddatalibrary/resources/link_status/link_status.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/link_status_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/link_status_list_response.py">SyncOffsetPage[LinkStatusListResponse]</a></code>
- <code title="get /udl/linkstatus/count">client.link_status.<a href="./src/unifieddatalibrary/resources/link_status/link_status.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/link_status_count_params.py">params</a>) -> str</code>
- <code title="get /udl/linkstatus/{id}">client.link_status.<a href="./src/unifieddatalibrary/resources/link_status/link_status.py">get</a>(id, \*\*<a href="src/unifieddatalibrary/types/link_status_get_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/link_status_get_response.py">LinkStatusGetResponse</a></code>
- <code title="get /udl/linkstatus/queryhelp">client.link_status.<a href="./src/unifieddatalibrary/resources/link_status/link_status.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/link_status_queryhelp_response.py">LinkStatusQueryhelpResponse</a></code>
- <code title="get /udl/linkstatus/tuple">client.link_status.<a href="./src/unifieddatalibrary/resources/link_status/link_status.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/link_status_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/link_status_tuple_response.py">LinkStatusTupleResponse</a></code>

## Datalink

Types:

```python
from unifieddatalibrary.types.link_status import (
    DatalinkIngest,
    DatalinkListResponse,
    DatalinkCountResponse,
    DatalinkQueryhelpResponse,
    DatalinkTupleResponse,
)
```

Methods:

- <code title="post /udl/datalink">client.link_status.datalink.<a href="./src/unifieddatalibrary/resources/link_status/datalink.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/link_status/datalink_create_params.py">params</a>) -> None</code>
- <code title="get /udl/datalink">client.link_status.datalink.<a href="./src/unifieddatalibrary/resources/link_status/datalink.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/link_status/datalink_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/link_status/datalink_list_response.py">SyncOffsetPage[DatalinkListResponse]</a></code>
- <code title="get /udl/datalink/count">client.link_status.datalink.<a href="./src/unifieddatalibrary/resources/link_status/datalink.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/link_status/datalink_count_params.py">params</a>) -> str</code>
- <code title="get /udl/datalink/queryhelp">client.link_status.datalink.<a href="./src/unifieddatalibrary/resources/link_status/datalink.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/link_status/datalink_queryhelp_response.py">DatalinkQueryhelpResponse</a></code>
- <code title="get /udl/datalink/tuple">client.link_status.datalink.<a href="./src/unifieddatalibrary/resources/link_status/datalink.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/link_status/datalink_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/link_status/datalink_tuple_response.py">DatalinkTupleResponse</a></code>
- <code title="post /filedrop/udl-datalink">client.link_status.datalink.<a href="./src/unifieddatalibrary/resources/link_status/datalink.py">unvalidated_publish</a>(\*\*<a href="src/unifieddatalibrary/types/link_status/datalink_unvalidated_publish_params.py">params</a>) -> None</code>

## History

Types:

```python
from unifieddatalibrary.types.link_status import HistoryListResponse, HistoryCountResponse
```

Methods:

- <code title="get /udl/linkstatus/history">client.link_status.history.<a href="./src/unifieddatalibrary/resources/link_status/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/link_status/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/link_status/history_list_response.py">SyncOffsetPage[HistoryListResponse]</a></code>
- <code title="get /udl/linkstatus/history/aodr">client.link_status.history.<a href="./src/unifieddatalibrary/resources/link_status/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/link_status/history_aodr_params.py">params</a>) -> None</code>
- <code title="get /udl/linkstatus/history/count">client.link_status.history.<a href="./src/unifieddatalibrary/resources/link_status/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/link_status/history_count_params.py">params</a>) -> str</code>

# Linkstatus

Methods:

- <code title="put /udl/linkstatus/{id}">client.linkstatus.<a href="./src/unifieddatalibrary/resources/linkstatus.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/linkstatus_update_params.py">params</a>) -> None</code>
- <code title="delete /udl/linkstatus/{id}">client.linkstatus.<a href="./src/unifieddatalibrary/resources/linkstatus.py">delete</a>(id) -> None</code>

# Location

Types:

```python
from unifieddatalibrary.types import (
    LocationIngest,
    LocationCountResponse,
    LocationQueryhelpResponse,
    LocationTupleResponse,
)
```

Methods:

- <code title="post /udl/location">client.location.<a href="./src/unifieddatalibrary/resources/location.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/location_create_params.py">params</a>) -> None</code>
- <code title="put /udl/location/{id}">client.location.<a href="./src/unifieddatalibrary/resources/location.py">update</a>(id, \*\*<a href="src/unifieddatalibrary/types/location_update_params.py">params</a>) -> None</code>
- <code title="get /udl/location">client.location.<a href="./src/unifieddatalibrary/resources/location.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/location_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/shared/location_abridged.py">SyncOffsetPage[LocationAbridged]</a></code>
- <code title="delete /udl/location/{id}">client.location.<a href="./src/unifieddatalibrary/resources/location.py">delete</a>(id) -> None</code>
- <code title="get /udl/location/count">client.location.<a href="./src/unifieddatalibrary/resources/location.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/location_count_params.py">params</a>) -> str</code>
- <code title="get /udl/location/{id}">client.location.<a href="./src/unifieddatalibrary/resources/location.py">get</a>(id, \*\*<a href="src/unifieddatalibrary/types/location_get_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/shared/location_full.py">LocationFull</a></code>
- <code title="get /udl/location/queryhelp">client.location.<a href="./src/unifieddatalibrary/resources/location.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/location_queryhelp_response.py">LocationQueryhelpResponse</a></code>
- <code title="get /udl/location/tuple">client.location.<a href="./src/unifieddatalibrary/resources/location.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/location_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/location_tuple_response.py">LocationTupleResponse</a></code>

# LogisticsSupport

Types:

```python
from unifieddatalibrary.types import (
    LogisticsDiscrepancyInfosFull,
    LogisticsPartsFull,
    LogisticsRemarksAbridged,
    LogisticsRemarksFull,
    LogisticsRemarksIngest,
    LogisticsSegmentsFull,
    LogisticsSpecialtiesFull,
    LogisticsStocksFull,
    LogisticsSupportItemsFull,
    LogisticsTransportationPlansFull,
    LogisticsSupportListResponse,
    LogisticsSupportCountResponse,
    LogisticsSupportGetResponse,
    LogisticsSupportQueryhelpResponse,
    LogisticsSupportTupleResponse,
)
```

Methods:

- <code title="post /udl/logisticssupport">client.logistics_support.<a href="./src/unifieddatalibrary/resources/logistics_support/logistics_support.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/logistics_support_create_params.py">params</a>) -> None</code>
- <code title="put /udl/logisticssupport/{id}">client.logistics_support.<a href="./src/unifieddatalibrary/resources/logistics_support/logistics_support.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/logistics_support_update_params.py">params</a>) -> None</code>
- <code title="get /udl/logisticssupport">client.logistics_support.<a href="./src/unifieddatalibrary/resources/logistics_support/logistics_support.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/logistics_support_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/logistics_support_list_response.py">SyncOffsetPage[LogisticsSupportListResponse]</a></code>
- <code title="get /udl/logisticssupport/count">client.logistics_support.<a href="./src/unifieddatalibrary/resources/logistics_support/logistics_support.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/logistics_support_count_params.py">params</a>) -> str</code>
- <code title="post /udl/logisticssupport/createBulk">client.logistics_support.<a href="./src/unifieddatalibrary/resources/logistics_support/logistics_support.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/logistics_support_create_bulk_params.py">params</a>) -> None</code>
- <code title="get /udl/logisticssupport/{id}">client.logistics_support.<a href="./src/unifieddatalibrary/resources/logistics_support/logistics_support.py">get</a>(id, \*\*<a href="src/unifieddatalibrary/types/logistics_support_get_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/logistics_support_get_response.py">LogisticsSupportGetResponse</a></code>
- <code title="get /udl/logisticssupport/queryhelp">client.logistics_support.<a href="./src/unifieddatalibrary/resources/logistics_support/logistics_support.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/logistics_support_queryhelp_response.py">LogisticsSupportQueryhelpResponse</a></code>
- <code title="get /udl/logisticssupport/tuple">client.logistics_support.<a href="./src/unifieddatalibrary/resources/logistics_support/logistics_support.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/logistics_support_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/logistics_support_tuple_response.py">LogisticsSupportTupleResponse</a></code>
- <code title="post /filedrop/udl-logisticssupport">client.logistics_support.<a href="./src/unifieddatalibrary/resources/logistics_support/logistics_support.py">unvalidated_publish</a>(\*\*<a href="src/unifieddatalibrary/types/logistics_support_unvalidated_publish_params.py">params</a>) -> None</code>

## History

Types:

```python
from unifieddatalibrary.types.logistics_support import HistoryListResponse, HistoryCountResponse
```

Methods:

- <code title="get /udl/logisticssupport/history">client.logistics_support.history.<a href="./src/unifieddatalibrary/resources/logistics_support/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/logistics_support/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/logistics_support/history_list_response.py">SyncOffsetPage[HistoryListResponse]</a></code>
- <code title="get /udl/logisticssupport/history/aodr">client.logistics_support.history.<a href="./src/unifieddatalibrary/resources/logistics_support/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/logistics_support/history_aodr_params.py">params</a>) -> None</code>
- <code title="get /udl/logisticssupport/history/count">client.logistics_support.history.<a href="./src/unifieddatalibrary/resources/logistics_support/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/logistics_support/history_count_params.py">params</a>) -> str</code>

# Maneuvers

Types:

```python
from unifieddatalibrary.types import (
    ManeuverListResponse,
    ManeuverCountResponse,
    ManeuverGetResponse,
    ManeuverQueryhelpResponse,
    ManeuverTupleResponse,
)
```

Methods:

- <code title="post /udl/maneuver">client.maneuvers.<a href="./src/unifieddatalibrary/resources/maneuvers/maneuvers.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/maneuver_create_params.py">params</a>) -> None</code>
- <code title="get /udl/maneuver">client.maneuvers.<a href="./src/unifieddatalibrary/resources/maneuvers/maneuvers.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/maneuver_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/maneuver_list_response.py">SyncOffsetPage[ManeuverListResponse]</a></code>
- <code title="get /udl/maneuver/count">client.maneuvers.<a href="./src/unifieddatalibrary/resources/maneuvers/maneuvers.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/maneuver_count_params.py">params</a>) -> str</code>
- <code title="post /udl/maneuver/createBulk">client.maneuvers.<a href="./src/unifieddatalibrary/resources/maneuvers/maneuvers.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/maneuver_create_bulk_params.py">params</a>) -> None</code>
- <code title="get /udl/maneuver/{id}">client.maneuvers.<a href="./src/unifieddatalibrary/resources/maneuvers/maneuvers.py">get</a>(id, \*\*<a href="src/unifieddatalibrary/types/maneuver_get_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/maneuver_get_response.py">ManeuverGetResponse</a></code>
- <code title="get /udl/maneuver/queryhelp">client.maneuvers.<a href="./src/unifieddatalibrary/resources/maneuvers/maneuvers.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/maneuver_queryhelp_response.py">ManeuverQueryhelpResponse</a></code>
- <code title="get /udl/maneuver/tuple">client.maneuvers.<a href="./src/unifieddatalibrary/resources/maneuvers/maneuvers.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/maneuver_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/maneuver_tuple_response.py">ManeuverTupleResponse</a></code>
- <code title="post /filedrop/udl-maneuver">client.maneuvers.<a href="./src/unifieddatalibrary/resources/maneuvers/maneuvers.py">unvalidated_publish</a>(\*\*<a href="src/unifieddatalibrary/types/maneuver_unvalidated_publish_params.py">params</a>) -> None</code>

## History

Types:

```python
from unifieddatalibrary.types.maneuvers import HistoryListResponse, HistoryCountResponse
```

Methods:

- <code title="get /udl/maneuver/history">client.maneuvers.history.<a href="./src/unifieddatalibrary/resources/maneuvers/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/maneuvers/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/maneuvers/history_list_response.py">SyncOffsetPage[HistoryListResponse]</a></code>
- <code title="get /udl/maneuver/history/aodr">client.maneuvers.history.<a href="./src/unifieddatalibrary/resources/maneuvers/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/maneuvers/history_aodr_params.py">params</a>) -> None</code>
- <code title="get /udl/maneuver/history/count">client.maneuvers.history.<a href="./src/unifieddatalibrary/resources/maneuvers/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/maneuvers/history_count_params.py">params</a>) -> str</code>

# Manifold

Types:

```python
from unifieddatalibrary.types import (
    ManifoldListResponse,
    ManifoldCountResponse,
    ManifoldGetResponse,
    ManifoldQueryhelpResponse,
    ManifoldTupleResponse,
)
```

Methods:

- <code title="post /udl/manifold">client.manifold.<a href="./src/unifieddatalibrary/resources/manifold.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/manifold_create_params.py">params</a>) -> None</code>
- <code title="put /udl/manifold/{id}">client.manifold.<a href="./src/unifieddatalibrary/resources/manifold.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/manifold_update_params.py">params</a>) -> None</code>
- <code title="get /udl/manifold">client.manifold.<a href="./src/unifieddatalibrary/resources/manifold.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/manifold_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/manifold_list_response.py">SyncOffsetPage[ManifoldListResponse]</a></code>
- <code title="delete /udl/manifold/{id}">client.manifold.<a href="./src/unifieddatalibrary/resources/manifold.py">delete</a>(id) -> None</code>
- <code title="get /udl/manifold/count">client.manifold.<a href="./src/unifieddatalibrary/resources/manifold.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/manifold_count_params.py">params</a>) -> str</code>
- <code title="post /udl/manifold/createBulk">client.manifold.<a href="./src/unifieddatalibrary/resources/manifold.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/manifold_create_bulk_params.py">params</a>) -> None</code>
- <code title="get /udl/manifold/{id}">client.manifold.<a href="./src/unifieddatalibrary/resources/manifold.py">get</a>(id, \*\*<a href="src/unifieddatalibrary/types/manifold_get_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/manifold_get_response.py">ManifoldGetResponse</a></code>
- <code title="get /udl/manifold/queryhelp">client.manifold.<a href="./src/unifieddatalibrary/resources/manifold.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/manifold_queryhelp_response.py">ManifoldQueryhelpResponse</a></code>
- <code title="get /udl/manifold/tuple">client.manifold.<a href="./src/unifieddatalibrary/resources/manifold.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/manifold_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/manifold_tuple_response.py">ManifoldTupleResponse</a></code>

# Manifoldelset

Types:

```python
from unifieddatalibrary.types import (
    ManifoldelsetListResponse,
    ManifoldelsetCountResponse,
    ManifoldelsetGetResponse,
    ManifoldelsetQueryhelpResponse,
    ManifoldelsetTupleResponse,
)
```

Methods:

- <code title="post /udl/manifoldelset">client.manifoldelset.<a href="./src/unifieddatalibrary/resources/manifoldelset.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/manifoldelset_create_params.py">params</a>) -> None</code>
- <code title="put /udl/manifoldelset/{id}">client.manifoldelset.<a href="./src/unifieddatalibrary/resources/manifoldelset.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/manifoldelset_update_params.py">params</a>) -> None</code>
- <code title="get /udl/manifoldelset">client.manifoldelset.<a href="./src/unifieddatalibrary/resources/manifoldelset.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/manifoldelset_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/manifoldelset_list_response.py">SyncOffsetPage[ManifoldelsetListResponse]</a></code>
- <code title="delete /udl/manifoldelset/{id}">client.manifoldelset.<a href="./src/unifieddatalibrary/resources/manifoldelset.py">delete</a>(id) -> None</code>
- <code title="get /udl/manifoldelset/count">client.manifoldelset.<a href="./src/unifieddatalibrary/resources/manifoldelset.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/manifoldelset_count_params.py">params</a>) -> str</code>
- <code title="post /udl/manifoldelset/createBulk">client.manifoldelset.<a href="./src/unifieddatalibrary/resources/manifoldelset.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/manifoldelset_create_bulk_params.py">params</a>) -> None</code>
- <code title="get /udl/manifoldelset/{id}">client.manifoldelset.<a href="./src/unifieddatalibrary/resources/manifoldelset.py">get</a>(id, \*\*<a href="src/unifieddatalibrary/types/manifoldelset_get_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/manifoldelset_get_response.py">ManifoldelsetGetResponse</a></code>
- <code title="get /udl/manifoldelset/queryhelp">client.manifoldelset.<a href="./src/unifieddatalibrary/resources/manifoldelset.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/manifoldelset_queryhelp_response.py">ManifoldelsetQueryhelpResponse</a></code>
- <code title="get /udl/manifoldelset/tuple">client.manifoldelset.<a href="./src/unifieddatalibrary/resources/manifoldelset.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/manifoldelset_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/manifoldelset_tuple_response.py">ManifoldelsetTupleResponse</a></code>

# MissileTracks

Types:

```python
from unifieddatalibrary.types import (
    MissileTrackListResponse,
    MissileTrackCountResponse,
    MissileTrackQueryhelpResponse,
    MissileTrackTupleResponse,
)
```

Methods:

- <code title="get /udl/missiletrack">client.missile_tracks.<a href="./src/unifieddatalibrary/resources/missile_tracks/missile_tracks.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/missile_track_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/missile_track_list_response.py">SyncOffsetPage[MissileTrackListResponse]</a></code>
- <code title="get /udl/missiletrack/count">client.missile_tracks.<a href="./src/unifieddatalibrary/resources/missile_tracks/missile_tracks.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/missile_track_count_params.py">params</a>) -> str</code>
- <code title="post /udl/missiletrack/createBulk">client.missile_tracks.<a href="./src/unifieddatalibrary/resources/missile_tracks/missile_tracks.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/missile_track_create_bulk_params.py">params</a>) -> None</code>
- <code title="get /udl/missiletrack/queryhelp">client.missile_tracks.<a href="./src/unifieddatalibrary/resources/missile_tracks/missile_tracks.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/missile_track_queryhelp_response.py">MissileTrackQueryhelpResponse</a></code>
- <code title="get /udl/missiletrack/tuple">client.missile_tracks.<a href="./src/unifieddatalibrary/resources/missile_tracks/missile_tracks.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/missile_track_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/missile_track_tuple_response.py">MissileTrackTupleResponse</a></code>
- <code title="post /filedrop/udl-missiletrack">client.missile_tracks.<a href="./src/unifieddatalibrary/resources/missile_tracks/missile_tracks.py">unvalidated_publish</a>(\*\*<a href="src/unifieddatalibrary/types/missile_track_unvalidated_publish_params.py">params</a>) -> None</code>

## History

Types:

```python
from unifieddatalibrary.types.missile_tracks import HistoryListResponse, HistoryCountResponse
```

Methods:

- <code title="get /udl/missiletrack/history">client.missile_tracks.history.<a href="./src/unifieddatalibrary/resources/missile_tracks/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/missile_tracks/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/missile_tracks/history_list_response.py">SyncOffsetPage[HistoryListResponse]</a></code>
- <code title="get /udl/missiletrack/history/aodr">client.missile_tracks.history.<a href="./src/unifieddatalibrary/resources/missile_tracks/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/missile_tracks/history_aodr_params.py">params</a>) -> None</code>
- <code title="get /udl/missiletrack/history/count">client.missile_tracks.history.<a href="./src/unifieddatalibrary/resources/missile_tracks/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/missile_tracks/history_count_params.py">params</a>) -> str</code>

# MissionAssignment

Types:

```python
from unifieddatalibrary.types import (
    MissionAssignmentListResponse,
    MissionAssignmentCountResponse,
    MissionAssignmentGetResponse,
    MissionAssignmentQueryhelpResponse,
    MissionAssignmentTupleResponse,
)
```

Methods:

- <code title="post /udl/missionassignment">client.mission_assignment.<a href="./src/unifieddatalibrary/resources/mission_assignment/mission_assignment.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/mission_assignment_create_params.py">params</a>) -> None</code>
- <code title="put /udl/missionassignment/{id}">client.mission_assignment.<a href="./src/unifieddatalibrary/resources/mission_assignment/mission_assignment.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/mission_assignment_update_params.py">params</a>) -> None</code>
- <code title="get /udl/missionassignment">client.mission_assignment.<a href="./src/unifieddatalibrary/resources/mission_assignment/mission_assignment.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/mission_assignment_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/mission_assignment_list_response.py">SyncOffsetPage[MissionAssignmentListResponse]</a></code>
- <code title="delete /udl/missionassignment/{id}">client.mission_assignment.<a href="./src/unifieddatalibrary/resources/mission_assignment/mission_assignment.py">delete</a>(id) -> None</code>
- <code title="get /udl/missionassignment/count">client.mission_assignment.<a href="./src/unifieddatalibrary/resources/mission_assignment/mission_assignment.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/mission_assignment_count_params.py">params</a>) -> str</code>
- <code title="post /udl/missionassignment/createBulk">client.mission_assignment.<a href="./src/unifieddatalibrary/resources/mission_assignment/mission_assignment.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/mission_assignment_create_bulk_params.py">params</a>) -> None</code>
- <code title="get /udl/missionassignment/{id}">client.mission_assignment.<a href="./src/unifieddatalibrary/resources/mission_assignment/mission_assignment.py">get</a>(id, \*\*<a href="src/unifieddatalibrary/types/mission_assignment_get_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/mission_assignment_get_response.py">MissionAssignmentGetResponse</a></code>
- <code title="get /udl/missionassignment/queryhelp">client.mission_assignment.<a href="./src/unifieddatalibrary/resources/mission_assignment/mission_assignment.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/mission_assignment_queryhelp_response.py">MissionAssignmentQueryhelpResponse</a></code>
- <code title="get /udl/missionassignment/tuple">client.mission_assignment.<a href="./src/unifieddatalibrary/resources/mission_assignment/mission_assignment.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/mission_assignment_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/mission_assignment_tuple_response.py">MissionAssignmentTupleResponse</a></code>

## History

Types:

```python
from unifieddatalibrary.types.mission_assignment import HistoryListResponse, HistoryCountResponse
```

Methods:

- <code title="get /udl/missionassignment/history">client.mission_assignment.history.<a href="./src/unifieddatalibrary/resources/mission_assignment/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/mission_assignment/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/mission_assignment/history_list_response.py">SyncOffsetPage[HistoryListResponse]</a></code>
- <code title="get /udl/missionassignment/history/aodr">client.mission_assignment.history.<a href="./src/unifieddatalibrary/resources/mission_assignment/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/mission_assignment/history_aodr_params.py">params</a>) -> None</code>
- <code title="get /udl/missionassignment/history/count">client.mission_assignment.history.<a href="./src/unifieddatalibrary/resources/mission_assignment/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/mission_assignment/history_count_params.py">params</a>) -> str</code>

# Mti

Types:

```python
from unifieddatalibrary.types import (
    MtiListResponse,
    MtiCountResponse,
    MtiQueryhelpResponse,
    MtiTupleResponse,
)
```

Methods:

- <code title="get /udl/mti">client.mti.<a href="./src/unifieddatalibrary/resources/mti/mti.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/mti_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/mti_list_response.py">SyncOffsetPage[MtiListResponse]</a></code>
- <code title="get /udl/mti/count">client.mti.<a href="./src/unifieddatalibrary/resources/mti/mti.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/mti_count_params.py">params</a>) -> str</code>
- <code title="post /udl/mti/createBulk">client.mti.<a href="./src/unifieddatalibrary/resources/mti/mti.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/mti_create_bulk_params.py">params</a>) -> None</code>
- <code title="get /udl/mti/queryhelp">client.mti.<a href="./src/unifieddatalibrary/resources/mti/mti.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/mti_queryhelp_response.py">MtiQueryhelpResponse</a></code>
- <code title="get /udl/mti/tuple">client.mti.<a href="./src/unifieddatalibrary/resources/mti/mti.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/mti_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/mti_tuple_response.py">MtiTupleResponse</a></code>
- <code title="post /filedrop/udl-mti">client.mti.<a href="./src/unifieddatalibrary/resources/mti/mti.py">unvalidated_publish</a>(\*\*<a href="src/unifieddatalibrary/types/mti_unvalidated_publish_params.py">params</a>) -> None</code>

## History

Types:

```python
from unifieddatalibrary.types.mti import MtiFull, HistoryCountResponse
```

Methods:

- <code title="get /udl/mti/history">client.mti.history.<a href="./src/unifieddatalibrary/resources/mti/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/mti/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/mti/mti_full.py">SyncOffsetPage[MtiFull]</a></code>
- <code title="get /udl/mti/history/aodr">client.mti.history.<a href="./src/unifieddatalibrary/resources/mti/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/mti/history_aodr_params.py">params</a>) -> None</code>
- <code title="get /udl/mti/history/count">client.mti.history.<a href="./src/unifieddatalibrary/resources/mti/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/mti/history_count_params.py">params</a>) -> str</code>

# Navigation

Types:

```python
from unifieddatalibrary.types import (
    NavigationListResponse,
    NavigationCountResponse,
    NavigationGetResponse,
    NavigationQueryhelpResponse,
    NavigationTupleResponse,
)
```

Methods:

- <code title="post /udl/navigation">client.navigation.<a href="./src/unifieddatalibrary/resources/navigation.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/navigation_create_params.py">params</a>) -> None</code>
- <code title="put /udl/navigation/{id}">client.navigation.<a href="./src/unifieddatalibrary/resources/navigation.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/navigation_update_params.py">params</a>) -> None</code>
- <code title="get /udl/navigation">client.navigation.<a href="./src/unifieddatalibrary/resources/navigation.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/navigation_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/navigation_list_response.py">SyncOffsetPage[NavigationListResponse]</a></code>
- <code title="delete /udl/navigation/{id}">client.navigation.<a href="./src/unifieddatalibrary/resources/navigation.py">delete</a>(id) -> None</code>
- <code title="get /udl/navigation/count">client.navigation.<a href="./src/unifieddatalibrary/resources/navigation.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/navigation_count_params.py">params</a>) -> str</code>
- <code title="get /udl/navigation/{id}">client.navigation.<a href="./src/unifieddatalibrary/resources/navigation.py">get</a>(id, \*\*<a href="src/unifieddatalibrary/types/navigation_get_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/navigation_get_response.py">NavigationGetResponse</a></code>
- <code title="get /udl/navigation/queryhelp">client.navigation.<a href="./src/unifieddatalibrary/resources/navigation.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/navigation_queryhelp_response.py">NavigationQueryhelpResponse</a></code>
- <code title="get /udl/navigation/tuple">client.navigation.<a href="./src/unifieddatalibrary/resources/navigation.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/navigation_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/navigation_tuple_response.py">NavigationTupleResponse</a></code>

# NavigationalObstruction

Types:

```python
from unifieddatalibrary.types import (
    NavigationalObstructionListResponse,
    NavigationalObstructionCountResponse,
    NavigationalObstructionGetResponse,
    NavigationalObstructionQueryhelpResponse,
    NavigationalObstructionTupleResponse,
)
```

Methods:

- <code title="post /udl/navigationalobstruction">client.navigational_obstruction.<a href="./src/unifieddatalibrary/resources/navigational_obstruction.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/navigational_obstruction_create_params.py">params</a>) -> None</code>
- <code title="put /udl/navigationalobstruction/{id}">client.navigational_obstruction.<a href="./src/unifieddatalibrary/resources/navigational_obstruction.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/navigational_obstruction_update_params.py">params</a>) -> None</code>
- <code title="get /udl/navigationalobstruction">client.navigational_obstruction.<a href="./src/unifieddatalibrary/resources/navigational_obstruction.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/navigational_obstruction_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/navigational_obstruction_list_response.py">SyncOffsetPage[NavigationalObstructionListResponse]</a></code>
- <code title="get /udl/navigationalobstruction/count">client.navigational_obstruction.<a href="./src/unifieddatalibrary/resources/navigational_obstruction.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/navigational_obstruction_count_params.py">params</a>) -> str</code>
- <code title="post /udl/navigationalobstruction/createBulk">client.navigational_obstruction.<a href="./src/unifieddatalibrary/resources/navigational_obstruction.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/navigational_obstruction_create_bulk_params.py">params</a>) -> None</code>
- <code title="get /udl/navigationalobstruction/{id}">client.navigational_obstruction.<a href="./src/unifieddatalibrary/resources/navigational_obstruction.py">get</a>(id, \*\*<a href="src/unifieddatalibrary/types/navigational_obstruction_get_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/navigational_obstruction_get_response.py">NavigationalObstructionGetResponse</a></code>
- <code title="get /udl/navigationalobstruction/queryhelp">client.navigational_obstruction.<a href="./src/unifieddatalibrary/resources/navigational_obstruction.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/navigational_obstruction_queryhelp_response.py">NavigationalObstructionQueryhelpResponse</a></code>
- <code title="get /udl/navigationalobstruction/tuple">client.navigational_obstruction.<a href="./src/unifieddatalibrary/resources/navigational_obstruction.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/navigational_obstruction_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/navigational_obstruction_tuple_response.py">NavigationalObstructionTupleResponse</a></code>

# Notification

Types:

```python
from unifieddatalibrary.types import (
    NotificationListResponse,
    NotificationCountResponse,
    NotificationQueryhelpResponse,
    NotificationTupleResponse,
)
```

Methods:

- <code title="post /udl/notification">client.notification.<a href="./src/unifieddatalibrary/resources/notification/notification.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/notification_create_params.py">params</a>) -> None</code>
- <code title="get /udl/notification">client.notification.<a href="./src/unifieddatalibrary/resources/notification/notification.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/notification_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/notification_list_response.py">SyncOffsetPage[NotificationListResponse]</a></code>
- <code title="get /udl/notification/count">client.notification.<a href="./src/unifieddatalibrary/resources/notification/notification.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/notification_count_params.py">params</a>) -> str</code>
- <code title="post /udl/notification/createRaw">client.notification.<a href="./src/unifieddatalibrary/resources/notification/notification.py">create_raw</a>(\*\*<a href="src/unifieddatalibrary/types/notification_create_raw_params.py">params</a>) -> None</code>
- <code title="get /udl/notification/{id}">client.notification.<a href="./src/unifieddatalibrary/resources/notification/notification.py">get</a>(id, \*\*<a href="src/unifieddatalibrary/types/notification_get_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/shared/notification_full.py">NotificationFull</a></code>
- <code title="get /udl/notification/queryhelp">client.notification.<a href="./src/unifieddatalibrary/resources/notification/notification.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/notification_queryhelp_response.py">NotificationQueryhelpResponse</a></code>
- <code title="get /udl/notification/tuple">client.notification.<a href="./src/unifieddatalibrary/resources/notification/notification.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/notification_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/notification_tuple_response.py">NotificationTupleResponse</a></code>

## History

Types:

```python
from unifieddatalibrary.types.notification import HistoryCountResponse
```

Methods:

- <code title="get /udl/notification/history">client.notification.history.<a href="./src/unifieddatalibrary/resources/notification/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/notification/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/shared/notification_full.py">SyncOffsetPage[NotificationFull]</a></code>
- <code title="get /udl/notification/history/aodr">client.notification.history.<a href="./src/unifieddatalibrary/resources/notification/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/notification/history_aodr_params.py">params</a>) -> None</code>
- <code title="get /udl/notification/history/count">client.notification.history.<a href="./src/unifieddatalibrary/resources/notification/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/notification/history_count_params.py">params</a>) -> str</code>

# ObjectOfInterest

Types:

```python
from unifieddatalibrary.types import (
    ObjectOfInterestListResponse,
    ObjectOfInterestCountResponse,
    ObjectOfInterestGetResponse,
    ObjectOfInterestQueryhelpResponse,
    ObjectOfInterestTupleResponse,
)
```

Methods:

- <code title="post /udl/objectofinterest">client.object_of_interest.<a href="./src/unifieddatalibrary/resources/object_of_interest.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/object_of_interest_create_params.py">params</a>) -> None</code>
- <code title="put /udl/objectofinterest/{id}">client.object_of_interest.<a href="./src/unifieddatalibrary/resources/object_of_interest.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/object_of_interest_update_params.py">params</a>) -> None</code>
- <code title="get /udl/objectofinterest">client.object_of_interest.<a href="./src/unifieddatalibrary/resources/object_of_interest.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/object_of_interest_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/object_of_interest_list_response.py">SyncOffsetPage[ObjectOfInterestListResponse]</a></code>
- <code title="delete /udl/objectofinterest/{id}">client.object_of_interest.<a href="./src/unifieddatalibrary/resources/object_of_interest.py">delete</a>(id) -> None</code>
- <code title="get /udl/objectofinterest/count">client.object_of_interest.<a href="./src/unifieddatalibrary/resources/object_of_interest.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/object_of_interest_count_params.py">params</a>) -> str</code>
- <code title="get /udl/objectofinterest/{id}">client.object_of_interest.<a href="./src/unifieddatalibrary/resources/object_of_interest.py">get</a>(id, \*\*<a href="src/unifieddatalibrary/types/object_of_interest_get_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/object_of_interest_get_response.py">ObjectOfInterestGetResponse</a></code>
- <code title="get /udl/objectofinterest/queryhelp">client.object_of_interest.<a href="./src/unifieddatalibrary/resources/object_of_interest.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/object_of_interest_queryhelp_response.py">ObjectOfInterestQueryhelpResponse</a></code>
- <code title="get /udl/objectofinterest/tuple">client.object_of_interest.<a href="./src/unifieddatalibrary/resources/object_of_interest.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/object_of_interest_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/object_of_interest_tuple_response.py">ObjectOfInterestTupleResponse</a></code>

# Observations

## Ecpsdr

Types:

```python
from unifieddatalibrary.types.observations import (
    Ecpsdr,
    EcpsdrAbridged,
    EcpsdrCountResponse,
    EcpsdrQueryHelpResponse,
    EcpsdrTupleResponse,
)
```

Methods:

- <code title="post /udl/ecpsdr">client.observations.ecpsdr.<a href="./src/unifieddatalibrary/resources/observations/ecpsdr.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/observations/ecpsdr_create_params.py">params</a>) -> None</code>
- <code title="get /udl/ecpsdr/{id}">client.observations.ecpsdr.<a href="./src/unifieddatalibrary/resources/observations/ecpsdr.py">retrieve</a>(id, \*\*<a href="src/unifieddatalibrary/types/observations/ecpsdr_retrieve_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/observations/ecpsdr.py">Ecpsdr</a></code>
- <code title="get /udl/ecpsdr">client.observations.ecpsdr.<a href="./src/unifieddatalibrary/resources/observations/ecpsdr.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/observations/ecpsdr_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/observations/ecpsdr_abridged.py">SyncOffsetPage[EcpsdrAbridged]</a></code>
- <code title="get /udl/ecpsdr/count">client.observations.ecpsdr.<a href="./src/unifieddatalibrary/resources/observations/ecpsdr.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/observations/ecpsdr_count_params.py">params</a>) -> str</code>
- <code title="post /udl/ecpsdr/createBulk">client.observations.ecpsdr.<a href="./src/unifieddatalibrary/resources/observations/ecpsdr.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/observations/ecpsdr_create_bulk_params.py">params</a>) -> None</code>
- <code title="get /udl/ecpsdr/queryhelp">client.observations.ecpsdr.<a href="./src/unifieddatalibrary/resources/observations/ecpsdr.py">query_help</a>() -> <a href="./src/unifieddatalibrary/types/observations/ecpsdr_query_help_response.py">EcpsdrQueryHelpResponse</a></code>
- <code title="get /udl/ecpsdr/tuple">client.observations.ecpsdr.<a href="./src/unifieddatalibrary/resources/observations/ecpsdr.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/observations/ecpsdr_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/observations/ecpsdr_tuple_response.py">EcpsdrTupleResponse</a></code>
- <code title="post /filedrop/udl-ecpsdr">client.observations.ecpsdr.<a href="./src/unifieddatalibrary/resources/observations/ecpsdr.py">unvalidated_publish</a>(\*\*<a href="src/unifieddatalibrary/types/observations/ecpsdr_unvalidated_publish_params.py">params</a>) -> None</code>

## EoObservations

Types:

```python
from unifieddatalibrary.types.observations import (
    EoObservationAbridged,
    EoObservationCountResponse,
    EoObservationQueryhelpResponse,
    EoObservationTupleResponse,
)
```

Methods:

- <code title="post /udl/eoobservation">client.observations.eo_observations.<a href="./src/unifieddatalibrary/resources/observations/eo_observations/eo_observations.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/observations/eo_observation_create_params.py">params</a>) -> None</code>
- <code title="get /udl/eoobservation/{id}">client.observations.eo_observations.<a href="./src/unifieddatalibrary/resources/observations/eo_observations/eo_observations.py">retrieve</a>(id, \*\*<a href="src/unifieddatalibrary/types/observations/eo_observation_retrieve_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/shared/eo_observation_full.py">EoObservationFull</a></code>
- <code title="get /udl/eoobservation">client.observations.eo_observations.<a href="./src/unifieddatalibrary/resources/observations/eo_observations/eo_observations.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/observations/eo_observation_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/observations/eo_observation_abridged.py">SyncOffsetPage[EoObservationAbridged]</a></code>
- <code title="get /udl/eoobservation/count">client.observations.eo_observations.<a href="./src/unifieddatalibrary/resources/observations/eo_observations/eo_observations.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/observations/eo_observation_count_params.py">params</a>) -> str</code>
- <code title="post /udl/eoobservation/createBulk">client.observations.eo_observations.<a href="./src/unifieddatalibrary/resources/observations/eo_observations/eo_observations.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/observations/eo_observation_create_bulk_params.py">params</a>) -> None</code>
- <code title="get /udl/eoobservation/queryhelp">client.observations.eo_observations.<a href="./src/unifieddatalibrary/resources/observations/eo_observations/eo_observations.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/observations/eo_observation_queryhelp_response.py">EoObservationQueryhelpResponse</a></code>
- <code title="get /udl/eoobservation/tuple">client.observations.eo_observations.<a href="./src/unifieddatalibrary/resources/observations/eo_observations/eo_observations.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/observations/eo_observation_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/observations/eo_observation_tuple_response.py">EoObservationTupleResponse</a></code>
- <code title="post /filedrop/udl-eo">client.observations.eo_observations.<a href="./src/unifieddatalibrary/resources/observations/eo_observations/eo_observations.py">unvalidated_publish</a>(\*\*<a href="src/unifieddatalibrary/types/observations/eo_observation_unvalidated_publish_params.py">params</a>) -> None</code>

### History

Types:

```python
from unifieddatalibrary.types.observations.eo_observations import HistoryCountResponse
```

Methods:

- <code title="get /udl/eoobservation/history">client.observations.eo_observations.history.<a href="./src/unifieddatalibrary/resources/observations/eo_observations/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/observations/eo_observations/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/shared/eo_observation_full.py">SyncOffsetPage[EoObservationFull]</a></code>
- <code title="get /udl/eoobservation/history/aodr">client.observations.eo_observations.history.<a href="./src/unifieddatalibrary/resources/observations/eo_observations/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/observations/eo_observations/history_aodr_params.py">params</a>) -> None</code>
- <code title="get /udl/eoobservation/history/count">client.observations.eo_observations.history.<a href="./src/unifieddatalibrary/resources/observations/eo_observations/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/observations/eo_observations/history_count_params.py">params</a>) -> str</code>

## Monoradar

Types:

```python
from unifieddatalibrary.types.observations import (
    MonoradarListResponse,
    MonoradarCountResponse,
    MonoradarQueryhelpResponse,
    MonoradarTupleResponse,
)
```

Methods:

- <code title="get /udl/monoradar">client.observations.monoradar.<a href="./src/unifieddatalibrary/resources/observations/monoradar/monoradar.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/observations/monoradar_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/observations/monoradar_list_response.py">SyncOffsetPage[MonoradarListResponse]</a></code>
- <code title="get /udl/monoradar/count">client.observations.monoradar.<a href="./src/unifieddatalibrary/resources/observations/monoradar/monoradar.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/observations/monoradar_count_params.py">params</a>) -> str</code>
- <code title="post /udl/monoradar/createBulk">client.observations.monoradar.<a href="./src/unifieddatalibrary/resources/observations/monoradar/monoradar.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/observations/monoradar_create_bulk_params.py">params</a>) -> None</code>
- <code title="get /udl/monoradar/queryhelp">client.observations.monoradar.<a href="./src/unifieddatalibrary/resources/observations/monoradar/monoradar.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/observations/monoradar_queryhelp_response.py">MonoradarQueryhelpResponse</a></code>
- <code title="get /udl/monoradar/tuple">client.observations.monoradar.<a href="./src/unifieddatalibrary/resources/observations/monoradar/monoradar.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/observations/monoradar_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/observations/monoradar_tuple_response.py">MonoradarTupleResponse</a></code>
- <code title="post /filedrop/monoradar">client.observations.monoradar.<a href="./src/unifieddatalibrary/resources/observations/monoradar/monoradar.py">unvalidated_publish</a>(\*\*<a href="src/unifieddatalibrary/types/observations/monoradar_unvalidated_publish_params.py">params</a>) -> None</code>

### History

Types:

```python
from unifieddatalibrary.types.observations.monoradar import (
    HistoryListResponse,
    HistoryCountResponse,
)
```

Methods:

- <code title="get /udl/monoradar/history">client.observations.monoradar.history.<a href="./src/unifieddatalibrary/resources/observations/monoradar/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/observations/monoradar/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/observations/monoradar/history_list_response.py">SyncOffsetPage[HistoryListResponse]</a></code>
- <code title="get /udl/monoradar/history/aodr">client.observations.monoradar.history.<a href="./src/unifieddatalibrary/resources/observations/monoradar/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/observations/monoradar/history_aodr_params.py">params</a>) -> None</code>
- <code title="get /udl/monoradar/history/count">client.observations.monoradar.history.<a href="./src/unifieddatalibrary/resources/observations/monoradar/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/observations/monoradar/history_count_params.py">params</a>) -> str</code>

## Obscorrelation

Types:

```python
from unifieddatalibrary.types.observations import (
    ObscorrelationRetrieveResponse,
    ObscorrelationListResponse,
    ObscorrelationCountResponse,
    ObscorrelationQueryHelpResponse,
    ObscorrelationTupleResponse,
)
```

Methods:

- <code title="post /udl/obscorrelation">client.observations.obscorrelation.<a href="./src/unifieddatalibrary/resources/observations/obscorrelation/obscorrelation.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/observations/obscorrelation_create_params.py">params</a>) -> None</code>
- <code title="get /udl/obscorrelation/{id}">client.observations.obscorrelation.<a href="./src/unifieddatalibrary/resources/observations/obscorrelation/obscorrelation.py">retrieve</a>(id, \*\*<a href="src/unifieddatalibrary/types/observations/obscorrelation_retrieve_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/observations/obscorrelation_retrieve_response.py">ObscorrelationRetrieveResponse</a></code>
- <code title="get /udl/obscorrelation">client.observations.obscorrelation.<a href="./src/unifieddatalibrary/resources/observations/obscorrelation/obscorrelation.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/observations/obscorrelation_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/observations/obscorrelation_list_response.py">SyncOffsetPage[ObscorrelationListResponse]</a></code>
- <code title="get /udl/obscorrelation/count">client.observations.obscorrelation.<a href="./src/unifieddatalibrary/resources/observations/obscorrelation/obscorrelation.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/observations/obscorrelation_count_params.py">params</a>) -> str</code>
- <code title="post /udl/obscorrelation/createBulk">client.observations.obscorrelation.<a href="./src/unifieddatalibrary/resources/observations/obscorrelation/obscorrelation.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/observations/obscorrelation_create_bulk_params.py">params</a>) -> None</code>
- <code title="get /udl/obscorrelation/queryhelp">client.observations.obscorrelation.<a href="./src/unifieddatalibrary/resources/observations/obscorrelation/obscorrelation.py">query_help</a>() -> <a href="./src/unifieddatalibrary/types/observations/obscorrelation_query_help_response.py">ObscorrelationQueryHelpResponse</a></code>
- <code title="get /udl/obscorrelation/tuple">client.observations.obscorrelation.<a href="./src/unifieddatalibrary/resources/observations/obscorrelation/obscorrelation.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/observations/obscorrelation_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/observations/obscorrelation_tuple_response.py">ObscorrelationTupleResponse</a></code>
- <code title="post /filedrop/udl-obscorrelation">client.observations.obscorrelation.<a href="./src/unifieddatalibrary/resources/observations/obscorrelation/obscorrelation.py">unvalidated_publish</a>(\*\*<a href="src/unifieddatalibrary/types/observations/obscorrelation_unvalidated_publish_params.py">params</a>) -> None</code>

### History

Types:

```python
from unifieddatalibrary.types.observations.obscorrelation import (
    HistoryListResponse,
    HistoryCountResponse,
)
```

Methods:

- <code title="get /udl/obscorrelation/history">client.observations.obscorrelation.history.<a href="./src/unifieddatalibrary/resources/observations/obscorrelation/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/observations/obscorrelation/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/observations/obscorrelation/history_list_response.py">SyncOffsetPage[HistoryListResponse]</a></code>
- <code title="get /udl/obscorrelation/history/aodr">client.observations.obscorrelation.history.<a href="./src/unifieddatalibrary/resources/observations/obscorrelation/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/observations/obscorrelation/history_aodr_params.py">params</a>) -> None</code>
- <code title="get /udl/obscorrelation/history/count">client.observations.obscorrelation.history.<a href="./src/unifieddatalibrary/resources/observations/obscorrelation/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/observations/obscorrelation/history_count_params.py">params</a>) -> str</code>

## PassiveRadarObservation

Types:

```python
from unifieddatalibrary.types.observations import (
    PassiveRadarObservationListResponse,
    PassiveRadarObservationCountResponse,
    PassiveRadarObservationGetResponse,
    PassiveRadarObservationQueryhelpResponse,
    PassiveRadarObservationTupleResponse,
)
```

Methods:

- <code title="post /udl/passiveradarobservation">client.observations.passive_radar_observation.<a href="./src/unifieddatalibrary/resources/observations/passive_radar_observation/passive_radar_observation.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/observations/passive_radar_observation_create_params.py">params</a>) -> None</code>
- <code title="get /udl/passiveradarobservation">client.observations.passive_radar_observation.<a href="./src/unifieddatalibrary/resources/observations/passive_radar_observation/passive_radar_observation.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/observations/passive_radar_observation_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/observations/passive_radar_observation_list_response.py">SyncOffsetPage[PassiveRadarObservationListResponse]</a></code>
- <code title="get /udl/passiveradarobservation/count">client.observations.passive_radar_observation.<a href="./src/unifieddatalibrary/resources/observations/passive_radar_observation/passive_radar_observation.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/observations/passive_radar_observation_count_params.py">params</a>) -> str</code>
- <code title="post /udl/passiveradarobservation/createBulk">client.observations.passive_radar_observation.<a href="./src/unifieddatalibrary/resources/observations/passive_radar_observation/passive_radar_observation.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/observations/passive_radar_observation_create_bulk_params.py">params</a>) -> None</code>
- <code title="post /filedrop/udl-passiveradar">client.observations.passive_radar_observation.<a href="./src/unifieddatalibrary/resources/observations/passive_radar_observation/passive_radar_observation.py">file_create</a>(\*\*<a href="src/unifieddatalibrary/types/observations/passive_radar_observation_file_create_params.py">params</a>) -> None</code>
- <code title="get /udl/passiveradarobservation/{id}">client.observations.passive_radar_observation.<a href="./src/unifieddatalibrary/resources/observations/passive_radar_observation/passive_radar_observation.py">get</a>(id, \*\*<a href="src/unifieddatalibrary/types/observations/passive_radar_observation_get_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/observations/passive_radar_observation_get_response.py">PassiveRadarObservationGetResponse</a></code>
- <code title="get /udl/passiveradarobservation/queryhelp">client.observations.passive_radar_observation.<a href="./src/unifieddatalibrary/resources/observations/passive_radar_observation/passive_radar_observation.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/observations/passive_radar_observation_queryhelp_response.py">PassiveRadarObservationQueryhelpResponse</a></code>
- <code title="get /udl/passiveradarobservation/tuple">client.observations.passive_radar_observation.<a href="./src/unifieddatalibrary/resources/observations/passive_radar_observation/passive_radar_observation.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/observations/passive_radar_observation_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/observations/passive_radar_observation_tuple_response.py">PassiveRadarObservationTupleResponse</a></code>

### History

Types:

```python
from unifieddatalibrary.types.observations.passive_radar_observation import (
    HistoryListResponse,
    HistoryCountResponse,
)
```

Methods:

- <code title="get /udl/passiveradarobservation/history">client.observations.passive_radar_observation.history.<a href="./src/unifieddatalibrary/resources/observations/passive_radar_observation/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/observations/passive_radar_observation/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/observations/passive_radar_observation/history_list_response.py">SyncOffsetPage[HistoryListResponse]</a></code>
- <code title="get /udl/passiveradarobservation/history/aodr">client.observations.passive_radar_observation.history.<a href="./src/unifieddatalibrary/resources/observations/passive_radar_observation/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/observations/passive_radar_observation/history_aodr_params.py">params</a>) -> None</code>
- <code title="get /udl/passiveradarobservation/history/count">client.observations.passive_radar_observation.history.<a href="./src/unifieddatalibrary/resources/observations/passive_radar_observation/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/observations/passive_radar_observation/history_count_params.py">params</a>) -> str</code>

## Radarobservation

Types:

```python
from unifieddatalibrary.types.observations import (
    RadarobservationListResponse,
    RadarobservationCountResponse,
    RadarobservationGetResponse,
    RadarobservationQueryhelpResponse,
    RadarobservationTupleResponse,
)
```

Methods:

- <code title="post /udl/radarobservation">client.observations.radarobservation.<a href="./src/unifieddatalibrary/resources/observations/radarobservation/radarobservation.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/observations/radarobservation_create_params.py">params</a>) -> None</code>
- <code title="get /udl/radarobservation">client.observations.radarobservation.<a href="./src/unifieddatalibrary/resources/observations/radarobservation/radarobservation.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/observations/radarobservation_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/observations/radarobservation_list_response.py">SyncOffsetPage[RadarobservationListResponse]</a></code>
- <code title="get /udl/radarobservation/count">client.observations.radarobservation.<a href="./src/unifieddatalibrary/resources/observations/radarobservation/radarobservation.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/observations/radarobservation_count_params.py">params</a>) -> str</code>
- <code title="post /udl/radarobservation/createBulk">client.observations.radarobservation.<a href="./src/unifieddatalibrary/resources/observations/radarobservation/radarobservation.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/observations/radarobservation_create_bulk_params.py">params</a>) -> None</code>
- <code title="get /udl/radarobservation/{id}">client.observations.radarobservation.<a href="./src/unifieddatalibrary/resources/observations/radarobservation/radarobservation.py">get</a>(id, \*\*<a href="src/unifieddatalibrary/types/observations/radarobservation_get_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/observations/radarobservation_get_response.py">RadarobservationGetResponse</a></code>
- <code title="get /udl/radarobservation/queryhelp">client.observations.radarobservation.<a href="./src/unifieddatalibrary/resources/observations/radarobservation/radarobservation.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/observations/radarobservation_queryhelp_response.py">RadarobservationQueryhelpResponse</a></code>
- <code title="get /udl/radarobservation/tuple">client.observations.radarobservation.<a href="./src/unifieddatalibrary/resources/observations/radarobservation/radarobservation.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/observations/radarobservation_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/observations/radarobservation_tuple_response.py">RadarobservationTupleResponse</a></code>
- <code title="post /filedrop/udl-radar">client.observations.radarobservation.<a href="./src/unifieddatalibrary/resources/observations/radarobservation/radarobservation.py">unvalidated_publish</a>(\*\*<a href="src/unifieddatalibrary/types/observations/radarobservation_unvalidated_publish_params.py">params</a>) -> None</code>

### History

Types:

```python
from unifieddatalibrary.types.observations.radarobservation import (
    HistoryListResponse,
    HistoryCountResponse,
)
```

Methods:

- <code title="get /udl/radarobservation/history">client.observations.radarobservation.history.<a href="./src/unifieddatalibrary/resources/observations/radarobservation/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/observations/radarobservation/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/observations/radarobservation/history_list_response.py">SyncOffsetPage[HistoryListResponse]</a></code>
- <code title="get /udl/radarobservation/history/aodr">client.observations.radarobservation.history.<a href="./src/unifieddatalibrary/resources/observations/radarobservation/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/observations/radarobservation/history_aodr_params.py">params</a>) -> None</code>
- <code title="get /udl/radarobservation/history/count">client.observations.radarobservation.history.<a href="./src/unifieddatalibrary/resources/observations/radarobservation/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/observations/radarobservation/history_count_params.py">params</a>) -> str</code>

## RfObservation

Types:

```python
from unifieddatalibrary.types.observations import (
    RfObservationListResponse,
    RfObservationCountResponse,
    RfObservationGetResponse,
    RfObservationQueryhelpResponse,
    RfObservationTupleResponse,
)
```

Methods:

- <code title="post /udl/rfobservation">client.observations.rf_observation.<a href="./src/unifieddatalibrary/resources/observations/rf_observation/rf_observation.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/observations/rf_observation_create_params.py">params</a>) -> None</code>
- <code title="get /udl/rfobservation">client.observations.rf_observation.<a href="./src/unifieddatalibrary/resources/observations/rf_observation/rf_observation.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/observations/rf_observation_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/observations/rf_observation_list_response.py">SyncOffsetPage[RfObservationListResponse]</a></code>
- <code title="get /udl/rfobservation/count">client.observations.rf_observation.<a href="./src/unifieddatalibrary/resources/observations/rf_observation/rf_observation.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/observations/rf_observation_count_params.py">params</a>) -> str</code>
- <code title="post /udl/rfobservation/createBulk">client.observations.rf_observation.<a href="./src/unifieddatalibrary/resources/observations/rf_observation/rf_observation.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/observations/rf_observation_create_bulk_params.py">params</a>) -> None</code>
- <code title="get /udl/rfobservation/{id}">client.observations.rf_observation.<a href="./src/unifieddatalibrary/resources/observations/rf_observation/rf_observation.py">get</a>(id, \*\*<a href="src/unifieddatalibrary/types/observations/rf_observation_get_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/observations/rf_observation_get_response.py">RfObservationGetResponse</a></code>
- <code title="get /udl/rfobservation/queryhelp">client.observations.rf_observation.<a href="./src/unifieddatalibrary/resources/observations/rf_observation/rf_observation.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/observations/rf_observation_queryhelp_response.py">RfObservationQueryhelpResponse</a></code>
- <code title="get /udl/rfobservation/tuple">client.observations.rf_observation.<a href="./src/unifieddatalibrary/resources/observations/rf_observation/rf_observation.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/observations/rf_observation_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/observations/rf_observation_tuple_response.py">RfObservationTupleResponse</a></code>
- <code title="post /filedrop/udl-rf">client.observations.rf_observation.<a href="./src/unifieddatalibrary/resources/observations/rf_observation/rf_observation.py">unvalidated_publish</a>(\*\*<a href="src/unifieddatalibrary/types/observations/rf_observation_unvalidated_publish_params.py">params</a>) -> None</code>

### History

Types:

```python
from unifieddatalibrary.types.observations.rf_observation import (
    HistoryListResponse,
    HistoryCountResponse,
)
```

Methods:

- <code title="get /udl/rfobservation/history">client.observations.rf_observation.history.<a href="./src/unifieddatalibrary/resources/observations/rf_observation/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/observations/rf_observation/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/observations/rf_observation/history_list_response.py">SyncOffsetPage[HistoryListResponse]</a></code>
- <code title="get /udl/rfobservation/history/aodr">client.observations.rf_observation.history.<a href="./src/unifieddatalibrary/resources/observations/rf_observation/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/observations/rf_observation/history_aodr_params.py">params</a>) -> None</code>
- <code title="get /udl/rfobservation/history/count">client.observations.rf_observation.history.<a href="./src/unifieddatalibrary/resources/observations/rf_observation/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/observations/rf_observation/history_count_params.py">params</a>) -> str</code>

## Swir

Methods:

- <code title="post /filedrop/swir">client.observations.swir.<a href="./src/unifieddatalibrary/resources/observations/swir.py">unvalidated_publish</a>(\*\*<a href="src/unifieddatalibrary/types/observations/swir_unvalidated_publish_params.py">params</a>) -> None</code>

# Onboardnavigation

Types:

```python
from unifieddatalibrary.types import (
    OnboardnavigationListResponse,
    OnboardnavigationCountResponse,
    OnboardnavigationQueryhelpResponse,
    OnboardnavigationTupleResponse,
)
```

Methods:

- <code title="get /udl/onboardnavigation">client.onboardnavigation.<a href="./src/unifieddatalibrary/resources/onboardnavigation/onboardnavigation.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/onboardnavigation_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/onboardnavigation_list_response.py">SyncOffsetPage[OnboardnavigationListResponse]</a></code>
- <code title="get /udl/onboardnavigation/count">client.onboardnavigation.<a href="./src/unifieddatalibrary/resources/onboardnavigation/onboardnavigation.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/onboardnavigation_count_params.py">params</a>) -> str</code>
- <code title="post /udl/onboardnavigation/createBulk">client.onboardnavigation.<a href="./src/unifieddatalibrary/resources/onboardnavigation/onboardnavigation.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/onboardnavigation_create_bulk_params.py">params</a>) -> None</code>
- <code title="get /udl/onboardnavigation/queryhelp">client.onboardnavigation.<a href="./src/unifieddatalibrary/resources/onboardnavigation/onboardnavigation.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/onboardnavigation_queryhelp_response.py">OnboardnavigationQueryhelpResponse</a></code>
- <code title="get /udl/onboardnavigation/tuple">client.onboardnavigation.<a href="./src/unifieddatalibrary/resources/onboardnavigation/onboardnavigation.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/onboardnavigation_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/onboardnavigation_tuple_response.py">OnboardnavigationTupleResponse</a></code>
- <code title="post /filedrop/udl-onboardnavigation">client.onboardnavigation.<a href="./src/unifieddatalibrary/resources/onboardnavigation/onboardnavigation.py">unvalidated_publish</a>(\*\*<a href="src/unifieddatalibrary/types/onboardnavigation_unvalidated_publish_params.py">params</a>) -> None</code>

## History

Types:

```python
from unifieddatalibrary.types.onboardnavigation import HistoryCountResponse
```

Methods:

- <code title="get /udl/onboardnavigation/history">client.onboardnavigation.history.<a href="./src/unifieddatalibrary/resources/onboardnavigation/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/onboardnavigation/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/shared/onboardnavigation_full.py">SyncOffsetPage[OnboardnavigationFull]</a></code>
- <code title="get /udl/onboardnavigation/history/aodr">client.onboardnavigation.history.<a href="./src/unifieddatalibrary/resources/onboardnavigation/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/onboardnavigation/history_aodr_params.py">params</a>) -> None</code>
- <code title="get /udl/onboardnavigation/history/count">client.onboardnavigation.history.<a href="./src/unifieddatalibrary/resources/onboardnavigation/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/onboardnavigation/history_count_params.py">params</a>) -> str</code>

# Onorbit

Types:

```python
from unifieddatalibrary.types import (
    OnorbitIngest,
    OnorbitListResponse,
    OnorbitCountResponse,
    OnorbitGetSignatureResponse,
    OnorbitQueryhelpResponse,
    OnorbitTupleResponse,
)
```

Methods:

- <code title="post /udl/onorbit">client.onorbit.<a href="./src/unifieddatalibrary/resources/onorbit/onorbit.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/onorbit_create_params.py">params</a>) -> None</code>
- <code title="put /udl/onorbit/{id}">client.onorbit.<a href="./src/unifieddatalibrary/resources/onorbit/onorbit.py">update</a>(id, \*\*<a href="src/unifieddatalibrary/types/onorbit_update_params.py">params</a>) -> None</code>
- <code title="get /udl/onorbit">client.onorbit.<a href="./src/unifieddatalibrary/resources/onorbit/onorbit.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/onorbit_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/onorbit_list_response.py">SyncOffsetPage[OnorbitListResponse]</a></code>
- <code title="delete /udl/onorbit/{id}">client.onorbit.<a href="./src/unifieddatalibrary/resources/onorbit/onorbit.py">delete</a>(id) -> None</code>
- <code title="get /udl/onorbit/count">client.onorbit.<a href="./src/unifieddatalibrary/resources/onorbit/onorbit.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/onorbit_count_params.py">params</a>) -> str</code>
- <code title="get /udl/onorbit/{id}">client.onorbit.<a href="./src/unifieddatalibrary/resources/onorbit/onorbit.py">get</a>(id, \*\*<a href="src/unifieddatalibrary/types/onorbit_get_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/shared/onorbit_full.py">OnorbitFull</a></code>
- <code title="get /udl/onorbit/getSignature">client.onorbit.<a href="./src/unifieddatalibrary/resources/onorbit/onorbit.py">get_signature</a>(\*\*<a href="src/unifieddatalibrary/types/onorbit_get_signature_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/onorbit_get_signature_response.py">OnorbitGetSignatureResponse</a></code>
- <code title="get /udl/onorbit/queryhelp">client.onorbit.<a href="./src/unifieddatalibrary/resources/onorbit/onorbit.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/onorbit_queryhelp_response.py">OnorbitQueryhelpResponse</a></code>
- <code title="get /udl/onorbit/tuple">client.onorbit.<a href="./src/unifieddatalibrary/resources/onorbit/onorbit.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/onorbit_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/onorbit_tuple_response.py">OnorbitTupleResponse</a></code>

## AntennaDetails

Types:

```python
from unifieddatalibrary.types.onorbit import AntennaDetailsAbridged
```

Methods:

- <code title="post /udl/antennadetails">client.onorbit.antenna_details.<a href="./src/unifieddatalibrary/resources/onorbit/antenna_details.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/onorbit/antenna_detail_create_params.py">params</a>) -> None</code>
- <code title="get /udl/antennadetails/{id}">client.onorbit.antenna_details.<a href="./src/unifieddatalibrary/resources/onorbit/antenna_details.py">retrieve</a>(id, \*\*<a href="src/unifieddatalibrary/types/onorbit/antenna_detail_retrieve_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/shared/antenna_details_full.py">AntennaDetailsFull</a></code>
- <code title="put /udl/antennadetails/{id}">client.onorbit.antenna_details.<a href="./src/unifieddatalibrary/resources/onorbit/antenna_details.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/onorbit/antenna_detail_update_params.py">params</a>) -> None</code>
- <code title="get /udl/antennadetails">client.onorbit.antenna_details.<a href="./src/unifieddatalibrary/resources/onorbit/antenna_details.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/onorbit/antenna_detail_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/onorbit/antenna_details_abridged.py">SyncOffsetPage[AntennaDetailsAbridged]</a></code>
- <code title="delete /udl/antennadetails/{id}">client.onorbit.antenna_details.<a href="./src/unifieddatalibrary/resources/onorbit/antenna_details.py">delete</a>(id) -> None</code>

# Onorbitantenna

Types:

```python
from unifieddatalibrary.types import OnorbitantennaListResponse
```

Methods:

- <code title="post /udl/onorbitantenna">client.onorbitantenna.<a href="./src/unifieddatalibrary/resources/onorbitantenna.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/onorbitantenna_create_params.py">params</a>) -> None</code>
- <code title="put /udl/onorbitantenna/{id}">client.onorbitantenna.<a href="./src/unifieddatalibrary/resources/onorbitantenna.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/onorbitantenna_update_params.py">params</a>) -> None</code>
- <code title="get /udl/onorbitantenna">client.onorbitantenna.<a href="./src/unifieddatalibrary/resources/onorbitantenna.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/onorbitantenna_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/onorbitantenna_list_response.py">SyncOffsetPage[OnorbitantennaListResponse]</a></code>
- <code title="delete /udl/onorbitantenna/{id}">client.onorbitantenna.<a href="./src/unifieddatalibrary/resources/onorbitantenna.py">delete</a>(id) -> None</code>
- <code title="get /udl/onorbitantenna/{id}">client.onorbitantenna.<a href="./src/unifieddatalibrary/resources/onorbitantenna.py">get</a>(id, \*\*<a href="src/unifieddatalibrary/types/onorbitantenna_get_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/shared/onorbit_antenna_full.py">OnorbitAntennaFull</a></code>

# Onorbitbattery

Types:

```python
from unifieddatalibrary.types import OnorbitbatteryListResponse
```

Methods:

- <code title="post /udl/onorbitbattery">client.onorbitbattery.<a href="./src/unifieddatalibrary/resources/onorbitbattery.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/onorbitbattery_create_params.py">params</a>) -> None</code>
- <code title="put /udl/onorbitbattery/{id}">client.onorbitbattery.<a href="./src/unifieddatalibrary/resources/onorbitbattery.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/onorbitbattery_update_params.py">params</a>) -> None</code>
- <code title="get /udl/onorbitbattery">client.onorbitbattery.<a href="./src/unifieddatalibrary/resources/onorbitbattery.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/onorbitbattery_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/onorbitbattery_list_response.py">SyncOffsetPage[OnorbitbatteryListResponse]</a></code>
- <code title="delete /udl/onorbitbattery/{id}">client.onorbitbattery.<a href="./src/unifieddatalibrary/resources/onorbitbattery.py">delete</a>(id) -> None</code>
- <code title="get /udl/onorbitbattery/{id}">client.onorbitbattery.<a href="./src/unifieddatalibrary/resources/onorbitbattery.py">get</a>(id, \*\*<a href="src/unifieddatalibrary/types/onorbitbattery_get_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/shared/onorbit_battery_full.py">OnorbitBatteryFull</a></code>

# Onorbitdetails

Types:

```python
from unifieddatalibrary.types import OnorbitdetailListResponse
```

Methods:

- <code title="post /udl/onorbitdetails">client.onorbitdetails.<a href="./src/unifieddatalibrary/resources/onorbitdetails.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/onorbitdetail_create_params.py">params</a>) -> None</code>
- <code title="put /udl/onorbitdetails/{id}">client.onorbitdetails.<a href="./src/unifieddatalibrary/resources/onorbitdetails.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/onorbitdetail_update_params.py">params</a>) -> None</code>
- <code title="get /udl/onorbitdetails">client.onorbitdetails.<a href="./src/unifieddatalibrary/resources/onorbitdetails.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/onorbitdetail_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/onorbitdetail_list_response.py">SyncOffsetPage[OnorbitdetailListResponse]</a></code>
- <code title="delete /udl/onorbitdetails/{id}">client.onorbitdetails.<a href="./src/unifieddatalibrary/resources/onorbitdetails.py">delete</a>(id) -> None</code>
- <code title="get /udl/onorbitdetails/{id}">client.onorbitdetails.<a href="./src/unifieddatalibrary/resources/onorbitdetails.py">get</a>(id, \*\*<a href="src/unifieddatalibrary/types/onorbitdetail_get_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/shared/onorbit_details_full.py">OnorbitDetailsFull</a></code>

# Onorbitevent

Types:

```python
from unifieddatalibrary.types import (
    OnorbiteventListResponse,
    OnorbiteventCountResponse,
    OnorbiteventGetResponse,
    OnorbiteventQueryhelpResponse,
    OnorbiteventTupleResponse,
)
```

Methods:

- <code title="post /udl/onorbitevent">client.onorbitevent.<a href="./src/unifieddatalibrary/resources/onorbitevent.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/onorbitevent_create_params.py">params</a>) -> None</code>
- <code title="put /udl/onorbitevent/{id}">client.onorbitevent.<a href="./src/unifieddatalibrary/resources/onorbitevent.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/onorbitevent_update_params.py">params</a>) -> None</code>
- <code title="get /udl/onorbitevent">client.onorbitevent.<a href="./src/unifieddatalibrary/resources/onorbitevent.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/onorbitevent_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/onorbitevent_list_response.py">SyncOffsetPage[OnorbiteventListResponse]</a></code>
- <code title="delete /udl/onorbitevent/{id}">client.onorbitevent.<a href="./src/unifieddatalibrary/resources/onorbitevent.py">delete</a>(id) -> None</code>
- <code title="get /udl/onorbitevent/count">client.onorbitevent.<a href="./src/unifieddatalibrary/resources/onorbitevent.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/onorbitevent_count_params.py">params</a>) -> str</code>
- <code title="get /udl/onorbitevent/{id}">client.onorbitevent.<a href="./src/unifieddatalibrary/resources/onorbitevent.py">get</a>(id, \*\*<a href="src/unifieddatalibrary/types/onorbitevent_get_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/onorbitevent_get_response.py">OnorbiteventGetResponse</a></code>
- <code title="get /udl/onorbitevent/queryhelp">client.onorbitevent.<a href="./src/unifieddatalibrary/resources/onorbitevent.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/onorbitevent_queryhelp_response.py">OnorbiteventQueryhelpResponse</a></code>
- <code title="get /udl/onorbitevent/tuple">client.onorbitevent.<a href="./src/unifieddatalibrary/resources/onorbitevent.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/onorbitevent_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/onorbitevent_tuple_response.py">OnorbiteventTupleResponse</a></code>

# Onorbitlist

Types:

```python
from unifieddatalibrary.types import (
    OnorbitlistListResponse,
    OnorbitlistCountResponse,
    OnorbitlistGetResponse,
    OnorbitlistQueryhelpResponse,
    OnorbitlistTupleResponse,
)
```

Methods:

- <code title="post /udl/onorbitlist">client.onorbitlist.<a href="./src/unifieddatalibrary/resources/onorbitlist.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/onorbitlist_create_params.py">params</a>) -> None</code>
- <code title="put /udl/onorbitlist/{id}">client.onorbitlist.<a href="./src/unifieddatalibrary/resources/onorbitlist.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/onorbitlist_update_params.py">params</a>) -> None</code>
- <code title="get /udl/onorbitlist">client.onorbitlist.<a href="./src/unifieddatalibrary/resources/onorbitlist.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/onorbitlist_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/onorbitlist_list_response.py">SyncOffsetPage[OnorbitlistListResponse]</a></code>
- <code title="delete /udl/onorbitlist/{id}">client.onorbitlist.<a href="./src/unifieddatalibrary/resources/onorbitlist.py">delete</a>(id) -> None</code>
- <code title="get /udl/onorbitlist/count">client.onorbitlist.<a href="./src/unifieddatalibrary/resources/onorbitlist.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/onorbitlist_count_params.py">params</a>) -> str</code>
- <code title="get /udl/onorbitlist/{id}">client.onorbitlist.<a href="./src/unifieddatalibrary/resources/onorbitlist.py">get</a>(id, \*\*<a href="src/unifieddatalibrary/types/onorbitlist_get_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/onorbitlist_get_response.py">OnorbitlistGetResponse</a></code>
- <code title="get /udl/onorbitlist/queryhelp">client.onorbitlist.<a href="./src/unifieddatalibrary/resources/onorbitlist.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/onorbitlist_queryhelp_response.py">OnorbitlistQueryhelpResponse</a></code>
- <code title="get /udl/onorbitlist/tuple">client.onorbitlist.<a href="./src/unifieddatalibrary/resources/onorbitlist.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/onorbitlist_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/onorbitlist_tuple_response.py">OnorbitlistTupleResponse</a></code>

# Onorbitsolararray

Types:

```python
from unifieddatalibrary.types import OnorbitsolararrayListResponse
```

Methods:

- <code title="post /udl/onorbitsolararray">client.onorbitsolararray.<a href="./src/unifieddatalibrary/resources/onorbitsolararray.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/onorbitsolararray_create_params.py">params</a>) -> None</code>
- <code title="put /udl/onorbitsolararray/{id}">client.onorbitsolararray.<a href="./src/unifieddatalibrary/resources/onorbitsolararray.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/onorbitsolararray_update_params.py">params</a>) -> None</code>
- <code title="get /udl/onorbitsolararray">client.onorbitsolararray.<a href="./src/unifieddatalibrary/resources/onorbitsolararray.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/onorbitsolararray_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/onorbitsolararray_list_response.py">SyncOffsetPage[OnorbitsolararrayListResponse]</a></code>
- <code title="delete /udl/onorbitsolararray/{id}">client.onorbitsolararray.<a href="./src/unifieddatalibrary/resources/onorbitsolararray.py">delete</a>(id) -> None</code>
- <code title="get /udl/onorbitsolararray/{id}">client.onorbitsolararray.<a href="./src/unifieddatalibrary/resources/onorbitsolararray.py">get</a>(id, \*\*<a href="src/unifieddatalibrary/types/onorbitsolararray_get_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/shared/onorbit_solar_array_full.py">OnorbitSolarArrayFull</a></code>

# Onorbitthruster

Types:

```python
from unifieddatalibrary.types import OnorbitthrusterListResponse
```

Methods:

- <code title="post /udl/onorbitthruster">client.onorbitthruster.<a href="./src/unifieddatalibrary/resources/onorbitthruster.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/onorbitthruster_create_params.py">params</a>) -> None</code>
- <code title="put /udl/onorbitthruster/{id}">client.onorbitthruster.<a href="./src/unifieddatalibrary/resources/onorbitthruster.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/onorbitthruster_update_params.py">params</a>) -> None</code>
- <code title="get /udl/onorbitthruster">client.onorbitthruster.<a href="./src/unifieddatalibrary/resources/onorbitthruster.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/onorbitthruster_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/onorbitthruster_list_response.py">SyncOffsetPage[OnorbitthrusterListResponse]</a></code>
- <code title="delete /udl/onorbitthruster/{id}">client.onorbitthruster.<a href="./src/unifieddatalibrary/resources/onorbitthruster.py">delete</a>(id) -> None</code>
- <code title="get /udl/onorbitthruster/{id}">client.onorbitthruster.<a href="./src/unifieddatalibrary/resources/onorbitthruster.py">get</a>(id, \*\*<a href="src/unifieddatalibrary/types/onorbitthruster_get_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/shared/onorbit_thruster_full.py">OnorbitThrusterFull</a></code>

# Onorbitthrusterstatus

Types:

```python
from unifieddatalibrary.types import (
    OnorbitthrusterstatusListResponse,
    OnorbitthrusterstatusCountResponse,
    OnorbitthrusterstatusQueryhelpResponse,
    OnorbitthrusterstatusTupleResponse,
)
```

Methods:

- <code title="post /udl/onorbitthrusterstatus">client.onorbitthrusterstatus.<a href="./src/unifieddatalibrary/resources/onorbitthrusterstatus/onorbitthrusterstatus.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/onorbitthrusterstatus_create_params.py">params</a>) -> None</code>
- <code title="get /udl/onorbitthrusterstatus">client.onorbitthrusterstatus.<a href="./src/unifieddatalibrary/resources/onorbitthrusterstatus/onorbitthrusterstatus.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/onorbitthrusterstatus_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/onorbitthrusterstatus_list_response.py">SyncOffsetPage[OnorbitthrusterstatusListResponse]</a></code>
- <code title="delete /udl/onorbitthrusterstatus/{id}">client.onorbitthrusterstatus.<a href="./src/unifieddatalibrary/resources/onorbitthrusterstatus/onorbitthrusterstatus.py">delete</a>(id) -> None</code>
- <code title="get /udl/onorbitthrusterstatus/count">client.onorbitthrusterstatus.<a href="./src/unifieddatalibrary/resources/onorbitthrusterstatus/onorbitthrusterstatus.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/onorbitthrusterstatus_count_params.py">params</a>) -> str</code>
- <code title="post /udl/onorbitthrusterstatus/createBulk">client.onorbitthrusterstatus.<a href="./src/unifieddatalibrary/resources/onorbitthrusterstatus/onorbitthrusterstatus.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/onorbitthrusterstatus_create_bulk_params.py">params</a>) -> None</code>
- <code title="get /udl/onorbitthrusterstatus/{id}">client.onorbitthrusterstatus.<a href="./src/unifieddatalibrary/resources/onorbitthrusterstatus/onorbitthrusterstatus.py">get</a>(id, \*\*<a href="src/unifieddatalibrary/types/onorbitthrusterstatus_get_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/shared/onorbitthrusterstatus_full.py">OnorbitthrusterstatusFull</a></code>
- <code title="get /udl/onorbitthrusterstatus/queryhelp">client.onorbitthrusterstatus.<a href="./src/unifieddatalibrary/resources/onorbitthrusterstatus/onorbitthrusterstatus.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/onorbitthrusterstatus_queryhelp_response.py">OnorbitthrusterstatusQueryhelpResponse</a></code>
- <code title="get /udl/onorbitthrusterstatus/tuple">client.onorbitthrusterstatus.<a href="./src/unifieddatalibrary/resources/onorbitthrusterstatus/onorbitthrusterstatus.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/onorbitthrusterstatus_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/onorbitthrusterstatus_tuple_response.py">OnorbitthrusterstatusTupleResponse</a></code>

## History

Types:

```python
from unifieddatalibrary.types.onorbitthrusterstatus import HistoryCountResponse
```

Methods:

- <code title="get /udl/onorbitthrusterstatus/history">client.onorbitthrusterstatus.history.<a href="./src/unifieddatalibrary/resources/onorbitthrusterstatus/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/onorbitthrusterstatus/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/shared/onorbitthrusterstatus_full.py">SyncOffsetPage[OnorbitthrusterstatusFull]</a></code>
- <code title="get /udl/onorbitthrusterstatus/history/count">client.onorbitthrusterstatus.history.<a href="./src/unifieddatalibrary/resources/onorbitthrusterstatus/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/onorbitthrusterstatus/history_count_params.py">params</a>) -> str</code>

# Operatingunit

Types:

```python
from unifieddatalibrary.types import (
    OperatingunitListResponse,
    OperatingunitCountResponse,
    OperatingunitQueryhelpResponse,
    OperatingunitTupleResponse,
)
```

Methods:

- <code title="post /udl/operatingunit">client.operatingunit.<a href="./src/unifieddatalibrary/resources/operatingunit.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/operatingunit_create_params.py">params</a>) -> None</code>
- <code title="put /udl/operatingunit/{id}">client.operatingunit.<a href="./src/unifieddatalibrary/resources/operatingunit.py">update</a>(id, \*\*<a href="src/unifieddatalibrary/types/operatingunit_update_params.py">params</a>) -> None</code>
- <code title="get /udl/operatingunit">client.operatingunit.<a href="./src/unifieddatalibrary/resources/operatingunit.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/operatingunit_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/operatingunit_list_response.py">SyncOffsetPage[OperatingunitListResponse]</a></code>
- <code title="delete /udl/operatingunit/{id}">client.operatingunit.<a href="./src/unifieddatalibrary/resources/operatingunit.py">delete</a>(id) -> None</code>
- <code title="get /udl/operatingunit/count">client.operatingunit.<a href="./src/unifieddatalibrary/resources/operatingunit.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/operatingunit_count_params.py">params</a>) -> str</code>
- <code title="get /udl/operatingunit/{id}">client.operatingunit.<a href="./src/unifieddatalibrary/resources/operatingunit.py">get</a>(id, \*\*<a href="src/unifieddatalibrary/types/operatingunit_get_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/shared/operatingunit_full.py">OperatingunitFull</a></code>
- <code title="get /udl/operatingunit/queryhelp">client.operatingunit.<a href="./src/unifieddatalibrary/resources/operatingunit.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/operatingunit_queryhelp_response.py">OperatingunitQueryhelpResponse</a></code>
- <code title="get /udl/operatingunit/tuple">client.operatingunit.<a href="./src/unifieddatalibrary/resources/operatingunit.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/operatingunit_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/operatingunit_tuple_response.py">OperatingunitTupleResponse</a></code>

# Operatingunitremark

Types:

```python
from unifieddatalibrary.types import (
    OperatingunitremarkListResponse,
    OperatingunitremarkCountResponse,
    OperatingunitremarkQueryhelpResponse,
    OperatingunitremarkTupleResponse,
)
```

Methods:

- <code title="post /udl/operatingunitremark">client.operatingunitremark.<a href="./src/unifieddatalibrary/resources/operatingunitremark.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/operatingunitremark_create_params.py">params</a>) -> None</code>
- <code title="get /udl/operatingunitremark">client.operatingunitremark.<a href="./src/unifieddatalibrary/resources/operatingunitremark.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/operatingunitremark_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/operatingunitremark_list_response.py">SyncOffsetPage[OperatingunitremarkListResponse]</a></code>
- <code title="get /udl/operatingunitremark/count">client.operatingunitremark.<a href="./src/unifieddatalibrary/resources/operatingunitremark.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/operatingunitremark_count_params.py">params</a>) -> str</code>
- <code title="post /udl/operatingunitremark/createBulk">client.operatingunitremark.<a href="./src/unifieddatalibrary/resources/operatingunitremark.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/operatingunitremark_create_bulk_params.py">params</a>) -> None</code>
- <code title="get /udl/operatingunitremark/{id}">client.operatingunitremark.<a href="./src/unifieddatalibrary/resources/operatingunitremark.py">get</a>(id, \*\*<a href="src/unifieddatalibrary/types/operatingunitremark_get_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/shared/operating_unit_remark_full.py">OperatingUnitRemarkFull</a></code>
- <code title="get /udl/operatingunitremark/queryhelp">client.operatingunitremark.<a href="./src/unifieddatalibrary/resources/operatingunitremark.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/operatingunitremark_queryhelp_response.py">OperatingunitremarkQueryhelpResponse</a></code>
- <code title="get /udl/operatingunitremark/tuple">client.operatingunitremark.<a href="./src/unifieddatalibrary/resources/operatingunitremark.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/operatingunitremark_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/operatingunitremark_tuple_response.py">OperatingunitremarkTupleResponse</a></code>

# Orbitdetermination

Types:

```python
from unifieddatalibrary.types import (
    OrbitdeterminationListResponse,
    OrbitdeterminationCountResponse,
    OrbitdeterminationGetResponse,
    OrbitdeterminationQueryhelpResponse,
    OrbitdeterminationTupleResponse,
)
```

Methods:

- <code title="post /udl/orbitdetermination">client.orbitdetermination.<a href="./src/unifieddatalibrary/resources/orbitdetermination/orbitdetermination.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/orbitdetermination_create_params.py">params</a>) -> None</code>
- <code title="get /udl/orbitdetermination">client.orbitdetermination.<a href="./src/unifieddatalibrary/resources/orbitdetermination/orbitdetermination.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/orbitdetermination_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/orbitdetermination_list_response.py">SyncOffsetPage[OrbitdeterminationListResponse]</a></code>
- <code title="get /udl/orbitdetermination/count">client.orbitdetermination.<a href="./src/unifieddatalibrary/resources/orbitdetermination/orbitdetermination.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/orbitdetermination_count_params.py">params</a>) -> str</code>
- <code title="post /udl/orbitdetermination/createBulk">client.orbitdetermination.<a href="./src/unifieddatalibrary/resources/orbitdetermination/orbitdetermination.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/orbitdetermination_create_bulk_params.py">params</a>) -> None</code>
- <code title="get /udl/orbitdetermination/{id}">client.orbitdetermination.<a href="./src/unifieddatalibrary/resources/orbitdetermination/orbitdetermination.py">get</a>(id, \*\*<a href="src/unifieddatalibrary/types/orbitdetermination_get_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/orbitdetermination_get_response.py">OrbitdeterminationGetResponse</a></code>
- <code title="get /udl/orbitdetermination/queryhelp">client.orbitdetermination.<a href="./src/unifieddatalibrary/resources/orbitdetermination/orbitdetermination.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/orbitdetermination_queryhelp_response.py">OrbitdeterminationQueryhelpResponse</a></code>
- <code title="get /udl/orbitdetermination/tuple">client.orbitdetermination.<a href="./src/unifieddatalibrary/resources/orbitdetermination/orbitdetermination.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/orbitdetermination_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/orbitdetermination_tuple_response.py">OrbitdeterminationTupleResponse</a></code>
- <code title="post /filedrop/udl-orbitdetermination">client.orbitdetermination.<a href="./src/unifieddatalibrary/resources/orbitdetermination/orbitdetermination.py">unvalidated_publish</a>(\*\*<a href="src/unifieddatalibrary/types/orbitdetermination_unvalidated_publish_params.py">params</a>) -> None</code>

## History

Types:

```python
from unifieddatalibrary.types.orbitdetermination import HistoryListResponse, HistoryCountResponse
```

Methods:

- <code title="get /udl/orbitdetermination/history">client.orbitdetermination.history.<a href="./src/unifieddatalibrary/resources/orbitdetermination/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/orbitdetermination/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/orbitdetermination/history_list_response.py">SyncOffsetPage[HistoryListResponse]</a></code>
- <code title="get /udl/orbitdetermination/history/aodr">client.orbitdetermination.history.<a href="./src/unifieddatalibrary/resources/orbitdetermination/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/orbitdetermination/history_aodr_params.py">params</a>) -> None</code>
- <code title="get /udl/orbitdetermination/history/count">client.orbitdetermination.history.<a href="./src/unifieddatalibrary/resources/orbitdetermination/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/orbitdetermination/history_count_params.py">params</a>) -> str</code>

# Orbittrack

Types:

```python
from unifieddatalibrary.types import (
    OrbittrackListResponse,
    OrbittrackCountResponse,
    OrbittrackQueryhelpResponse,
    OrbittrackTupleResponse,
)
```

Methods:

- <code title="get /udl/orbittrack">client.orbittrack.<a href="./src/unifieddatalibrary/resources/orbittrack/orbittrack.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/orbittrack_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/orbittrack_list_response.py">SyncOffsetPage[OrbittrackListResponse]</a></code>
- <code title="get /udl/orbittrack/count">client.orbittrack.<a href="./src/unifieddatalibrary/resources/orbittrack/orbittrack.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/orbittrack_count_params.py">params</a>) -> str</code>
- <code title="post /udl/orbittrack/createBulk">client.orbittrack.<a href="./src/unifieddatalibrary/resources/orbittrack/orbittrack.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/orbittrack_create_bulk_params.py">params</a>) -> None</code>
- <code title="get /udl/orbittrack/queryhelp">client.orbittrack.<a href="./src/unifieddatalibrary/resources/orbittrack/orbittrack.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/orbittrack_queryhelp_response.py">OrbittrackQueryhelpResponse</a></code>
- <code title="get /udl/orbittrack/tuple">client.orbittrack.<a href="./src/unifieddatalibrary/resources/orbittrack/orbittrack.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/orbittrack_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/orbittrack_tuple_response.py">OrbittrackTupleResponse</a></code>
- <code title="post /filedrop/udl-orbittrack">client.orbittrack.<a href="./src/unifieddatalibrary/resources/orbittrack/orbittrack.py">unvalidated_publish</a>(\*\*<a href="src/unifieddatalibrary/types/orbittrack_unvalidated_publish_params.py">params</a>) -> None</code>

## History

Types:

```python
from unifieddatalibrary.types.orbittrack import HistoryListResponse, HistoryCountResponse
```

Methods:

- <code title="get /udl/orbittrack/history">client.orbittrack.history.<a href="./src/unifieddatalibrary/resources/orbittrack/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/orbittrack/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/orbittrack/history_list_response.py">SyncOffsetPage[HistoryListResponse]</a></code>
- <code title="get /udl/orbittrack/history/aodr">client.orbittrack.history.<a href="./src/unifieddatalibrary/resources/orbittrack/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/orbittrack/history_aodr_params.py">params</a>) -> None</code>
- <code title="get /udl/orbittrack/history/count">client.orbittrack.history.<a href="./src/unifieddatalibrary/resources/orbittrack/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/orbittrack/history_count_params.py">params</a>) -> str</code>

# Organization

Types:

```python
from unifieddatalibrary.types import (
    OrganizationListResponse,
    OrganizationCountResponse,
    OrganizationGetOrganizationCategoriesResponse,
    OrganizationGetOrganizationTypesResponse,
    OrganizationQueryhelpResponse,
    OrganizationTupleResponse,
)
```

Methods:

- <code title="post /udl/organization">client.organization.<a href="./src/unifieddatalibrary/resources/organization.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/organization_create_params.py">params</a>) -> None</code>
- <code title="put /udl/organization/{id}">client.organization.<a href="./src/unifieddatalibrary/resources/organization.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/organization_update_params.py">params</a>) -> None</code>
- <code title="get /udl/organization">client.organization.<a href="./src/unifieddatalibrary/resources/organization.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/organization_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/organization_list_response.py">SyncOffsetPage[OrganizationListResponse]</a></code>
- <code title="delete /udl/organization/{id}">client.organization.<a href="./src/unifieddatalibrary/resources/organization.py">delete</a>(id) -> None</code>
- <code title="get /udl/organization/count">client.organization.<a href="./src/unifieddatalibrary/resources/organization.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/organization_count_params.py">params</a>) -> str</code>
- <code title="get /udl/organization/{id}">client.organization.<a href="./src/unifieddatalibrary/resources/organization.py">get</a>(id, \*\*<a href="src/unifieddatalibrary/types/organization_get_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/shared/organization_full.py">OrganizationFull</a></code>
- <code title="get /udl/organization/getOrganizationCategories">client.organization.<a href="./src/unifieddatalibrary/resources/organization.py">get_organization_categories</a>(\*\*<a href="src/unifieddatalibrary/types/organization_get_organization_categories_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/organization_get_organization_categories_response.py">OrganizationGetOrganizationCategoriesResponse</a></code>
- <code title="get /udl/organization/getOrganizationTypes">client.organization.<a href="./src/unifieddatalibrary/resources/organization.py">get_organization_types</a>(\*\*<a href="src/unifieddatalibrary/types/organization_get_organization_types_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/organization_get_organization_types_response.py">OrganizationGetOrganizationTypesResponse</a></code>
- <code title="get /udl/organization/queryhelp">client.organization.<a href="./src/unifieddatalibrary/resources/organization.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/organization_queryhelp_response.py">OrganizationQueryhelpResponse</a></code>
- <code title="get /udl/organization/tuple">client.organization.<a href="./src/unifieddatalibrary/resources/organization.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/organization_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/organization_tuple_response.py">OrganizationTupleResponse</a></code>

# Organizationdetails

Types:

```python
from unifieddatalibrary.types import (
    OrganizationdetailListResponse,
    OrganizationdetailFindBySourceResponse,
)
```

Methods:

- <code title="post /udl/organizationdetails">client.organizationdetails.<a href="./src/unifieddatalibrary/resources/organizationdetails.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/organizationdetail_create_params.py">params</a>) -> None</code>
- <code title="put /udl/organizationdetails/{id}">client.organizationdetails.<a href="./src/unifieddatalibrary/resources/organizationdetails.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/organizationdetail_update_params.py">params</a>) -> None</code>
- <code title="get /udl/organizationdetails">client.organizationdetails.<a href="./src/unifieddatalibrary/resources/organizationdetails.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/organizationdetail_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/organizationdetail_list_response.py">SyncOffsetPage[OrganizationdetailListResponse]</a></code>
- <code title="delete /udl/organizationdetails/{id}">client.organizationdetails.<a href="./src/unifieddatalibrary/resources/organizationdetails.py">delete</a>(id) -> None</code>
- <code title="get /udl/organizationdetails/findBySource">client.organizationdetails.<a href="./src/unifieddatalibrary/resources/organizationdetails.py">find_by_source</a>(\*\*<a href="src/unifieddatalibrary/types/organizationdetail_find_by_source_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/organizationdetail_find_by_source_response.py">OrganizationdetailFindBySourceResponse</a></code>
- <code title="get /udl/organizationdetails/{id}">client.organizationdetails.<a href="./src/unifieddatalibrary/resources/organizationdetails.py">get</a>(id, \*\*<a href="src/unifieddatalibrary/types/organizationdetail_get_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/shared/organization_details_full.py">OrganizationDetailsFull</a></code>

# Personnelrecovery

Types:

```python
from unifieddatalibrary.types import (
    PersonnelRecoveryFullL,
    PersonnelrecoveryListResponse,
    PersonnelrecoveryCountResponse,
    PersonnelrecoveryQueryhelpResponse,
    PersonnelrecoveryTupleResponse,
)
```

Methods:

- <code title="post /udl/personnelrecovery">client.personnelrecovery.<a href="./src/unifieddatalibrary/resources/personnelrecovery/personnelrecovery.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/personnelrecovery_create_params.py">params</a>) -> None</code>
- <code title="get /udl/personnelrecovery">client.personnelrecovery.<a href="./src/unifieddatalibrary/resources/personnelrecovery/personnelrecovery.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/personnelrecovery_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/personnelrecovery_list_response.py">SyncOffsetPage[PersonnelrecoveryListResponse]</a></code>
- <code title="get /udl/personnelrecovery/count">client.personnelrecovery.<a href="./src/unifieddatalibrary/resources/personnelrecovery/personnelrecovery.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/personnelrecovery_count_params.py">params</a>) -> str</code>
- <code title="post /udl/personnelrecovery/createBulk">client.personnelrecovery.<a href="./src/unifieddatalibrary/resources/personnelrecovery/personnelrecovery.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/personnelrecovery_create_bulk_params.py">params</a>) -> None</code>
- <code title="post /filedrop/udl-personnelrecovery">client.personnelrecovery.<a href="./src/unifieddatalibrary/resources/personnelrecovery/personnelrecovery.py">file_create</a>(\*\*<a href="src/unifieddatalibrary/types/personnelrecovery_file_create_params.py">params</a>) -> None</code>
- <code title="get /udl/personnelrecovery/{id}">client.personnelrecovery.<a href="./src/unifieddatalibrary/resources/personnelrecovery/personnelrecovery.py">get</a>(id, \*\*<a href="src/unifieddatalibrary/types/personnelrecovery_get_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/personnel_recovery_full_l.py">PersonnelRecoveryFullL</a></code>
- <code title="get /udl/personnelrecovery/queryhelp">client.personnelrecovery.<a href="./src/unifieddatalibrary/resources/personnelrecovery/personnelrecovery.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/personnelrecovery_queryhelp_response.py">PersonnelrecoveryQueryhelpResponse</a></code>
- <code title="get /udl/personnelrecovery/tuple">client.personnelrecovery.<a href="./src/unifieddatalibrary/resources/personnelrecovery/personnelrecovery.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/personnelrecovery_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/personnelrecovery_tuple_response.py">PersonnelrecoveryTupleResponse</a></code>

## History

Types:

```python
from unifieddatalibrary.types.personnelrecovery import HistoryCountResponse
```

Methods:

- <code title="get /udl/personnelrecovery/history">client.personnelrecovery.history.<a href="./src/unifieddatalibrary/resources/personnelrecovery/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/personnelrecovery/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/personnel_recovery_full_l.py">SyncOffsetPage[PersonnelRecoveryFullL]</a></code>
- <code title="get /udl/personnelrecovery/history/count">client.personnelrecovery.history.<a href="./src/unifieddatalibrary/resources/personnelrecovery/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/personnelrecovery/history_count_params.py">params</a>) -> str</code>

# Poi

Types:

```python
from unifieddatalibrary.types import (
    PoiListResponse,
    PoiCountResponse,
    PoiGetResponse,
    PoiQueryhelpResponse,
    PoiTupleResponse,
)
```

Methods:

- <code title="post /udl/poi">client.poi.<a href="./src/unifieddatalibrary/resources/poi.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/poi_create_params.py">params</a>) -> None</code>
- <code title="get /udl/poi">client.poi.<a href="./src/unifieddatalibrary/resources/poi.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/poi_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/poi_list_response.py">SyncOffsetPage[PoiListResponse]</a></code>
- <code title="get /udl/poi/count">client.poi.<a href="./src/unifieddatalibrary/resources/poi.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/poi_count_params.py">params</a>) -> str</code>
- <code title="post /udl/poi/createBulk">client.poi.<a href="./src/unifieddatalibrary/resources/poi.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/poi_create_bulk_params.py">params</a>) -> None</code>
- <code title="get /udl/poi/{id}">client.poi.<a href="./src/unifieddatalibrary/resources/poi.py">get</a>(id, \*\*<a href="src/unifieddatalibrary/types/poi_get_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/poi_get_response.py">PoiGetResponse</a></code>
- <code title="get /udl/poi/queryhelp">client.poi.<a href="./src/unifieddatalibrary/resources/poi.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/poi_queryhelp_response.py">PoiQueryhelpResponse</a></code>
- <code title="get /udl/poi/tuple">client.poi.<a href="./src/unifieddatalibrary/resources/poi.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/poi_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/poi_tuple_response.py">PoiTupleResponse</a></code>
- <code title="post /filedrop/udl-poi">client.poi.<a href="./src/unifieddatalibrary/resources/poi.py">unvalidated_publish</a>(\*\*<a href="src/unifieddatalibrary/types/poi_unvalidated_publish_params.py">params</a>) -> None</code>

# Port

Types:

```python
from unifieddatalibrary.types import (
    PortListResponse,
    PortCountResponse,
    PortGetResponse,
    PortQueryhelpResponse,
    PortTupleResponse,
)
```

Methods:

- <code title="post /udl/port">client.port.<a href="./src/unifieddatalibrary/resources/port.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/port_create_params.py">params</a>) -> None</code>
- <code title="put /udl/port/{id}">client.port.<a href="./src/unifieddatalibrary/resources/port.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/port_update_params.py">params</a>) -> None</code>
- <code title="get /udl/port">client.port.<a href="./src/unifieddatalibrary/resources/port.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/port_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/port_list_response.py">SyncOffsetPage[PortListResponse]</a></code>
- <code title="get /udl/port/count">client.port.<a href="./src/unifieddatalibrary/resources/port.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/port_count_params.py">params</a>) -> str</code>
- <code title="post /udl/port/createBulk">client.port.<a href="./src/unifieddatalibrary/resources/port.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/port_create_bulk_params.py">params</a>) -> None</code>
- <code title="get /udl/port/{id}">client.port.<a href="./src/unifieddatalibrary/resources/port.py">get</a>(id, \*\*<a href="src/unifieddatalibrary/types/port_get_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/port_get_response.py">PortGetResponse</a></code>
- <code title="get /udl/port/queryhelp">client.port.<a href="./src/unifieddatalibrary/resources/port.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/port_queryhelp_response.py">PortQueryhelpResponse</a></code>
- <code title="get /udl/port/tuple">client.port.<a href="./src/unifieddatalibrary/resources/port.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/port_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/port_tuple_response.py">PortTupleResponse</a></code>

# ReportAndActivities

## Poi

### History

Types:

```python
from unifieddatalibrary.types.report_and_activities.poi import (
    HistoryListResponse,
    HistoryCountResponse,
)
```

Methods:

- <code title="get /udl/poi/history">client.report_and_activities.poi.history.<a href="./src/unifieddatalibrary/resources/report_and_activities/poi/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/report_and_activities/poi/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/report_and_activities/poi/history_list_response.py">SyncOffsetPage[HistoryListResponse]</a></code>
- <code title="get /udl/poi/history/aodr">client.report_and_activities.poi.history.<a href="./src/unifieddatalibrary/resources/report_and_activities/poi/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/report_and_activities/poi/history_aodr_params.py">params</a>) -> None</code>
- <code title="get /udl/poi/history/count">client.report_and_activities.poi.history.<a href="./src/unifieddatalibrary/resources/report_and_activities/poi/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/report_and_activities/poi/history_count_params.py">params</a>) -> str</code>

## UdlH3geo

Methods:

- <code title="post /filedrop/udl-h3geo">client.report_and_activities.udl_h3geo.<a href="./src/unifieddatalibrary/resources/report_and_activities/udl_h3geo.py">unvalidated_publish</a>(\*\*<a href="src/unifieddatalibrary/types/report_and_activities/udl_h3geo_unvalidated_publish_params.py">params</a>) -> None</code>

## UdlSigact

Methods:

- <code title="get /udl/sigact/getFile/{id}">client.report_and_activities.udl_sigact.<a href="./src/unifieddatalibrary/resources/report_and_activities/udl_sigact.py">file_get</a>(id, \*\*<a href="src/unifieddatalibrary/types/report_and_activities/udl_sigact_file_get_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="post /filedrop/udl-sigact">client.report_and_activities.udl_sigact.<a href="./src/unifieddatalibrary/resources/report_and_activities/udl_sigact.py">unvalidated_publish</a>(\*\*<a href="src/unifieddatalibrary/types/report_and_activities/udl_sigact_unvalidated_publish_params.py">params</a>) -> None</code>

# RfBand

Types:

```python
from unifieddatalibrary.types import (
    RfBandListResponse,
    RfBandCountResponse,
    RfBandQueryhelpResponse,
    RfBandTupleResponse,
)
```

Methods:

- <code title="post /udl/rfband">client.rf_band.<a href="./src/unifieddatalibrary/resources/rf_band.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/rf_band_create_params.py">params</a>) -> None</code>
- <code title="put /udl/rfband/{id}">client.rf_band.<a href="./src/unifieddatalibrary/resources/rf_band.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/rf_band_update_params.py">params</a>) -> None</code>
- <code title="get /udl/rfband">client.rf_band.<a href="./src/unifieddatalibrary/resources/rf_band.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/rf_band_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/rf_band_list_response.py">SyncOffsetPage[RfBandListResponse]</a></code>
- <code title="delete /udl/rfband/{id}">client.rf_band.<a href="./src/unifieddatalibrary/resources/rf_band.py">delete</a>(id) -> None</code>
- <code title="get /udl/rfband/count">client.rf_band.<a href="./src/unifieddatalibrary/resources/rf_band.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/rf_band_count_params.py">params</a>) -> str</code>
- <code title="get /udl/rfband/{id}">client.rf_band.<a href="./src/unifieddatalibrary/resources/rf_band.py">get</a>(id, \*\*<a href="src/unifieddatalibrary/types/rf_band_get_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/shared/rf_band_full.py">RfBandFull</a></code>
- <code title="get /udl/rfband/queryhelp">client.rf_band.<a href="./src/unifieddatalibrary/resources/rf_band.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/rf_band_queryhelp_response.py">RfBandQueryhelpResponse</a></code>
- <code title="get /udl/rfband/tuple">client.rf_band.<a href="./src/unifieddatalibrary/resources/rf_band.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/rf_band_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/rf_band_tuple_response.py">RfBandTupleResponse</a></code>

# RfBandType

Types:

```python
from unifieddatalibrary.types import (
    RfBandTypeListResponse,
    RfBandTypeCountResponse,
    RfBandTypeGetResponse,
    RfBandTypeQueryhelpResponse,
    RfBandTypeTupleResponse,
)
```

Methods:

- <code title="post /udl/rfbandtype">client.rf_band_type.<a href="./src/unifieddatalibrary/resources/rf_band_type.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/rf_band_type_create_params.py">params</a>) -> None</code>
- <code title="put /udl/rfbandtype/{id}">client.rf_band_type.<a href="./src/unifieddatalibrary/resources/rf_band_type.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/rf_band_type_update_params.py">params</a>) -> None</code>
- <code title="get /udl/rfbandtype">client.rf_band_type.<a href="./src/unifieddatalibrary/resources/rf_band_type.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/rf_band_type_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/rf_band_type_list_response.py">SyncOffsetPage[RfBandTypeListResponse]</a></code>
- <code title="delete /udl/rfbandtype/{id}">client.rf_band_type.<a href="./src/unifieddatalibrary/resources/rf_band_type.py">delete</a>(id) -> None</code>
- <code title="get /udl/rfbandtype/count">client.rf_band_type.<a href="./src/unifieddatalibrary/resources/rf_band_type.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/rf_band_type_count_params.py">params</a>) -> str</code>
- <code title="get /udl/rfbandtype/{id}">client.rf_band_type.<a href="./src/unifieddatalibrary/resources/rf_band_type.py">get</a>(id, \*\*<a href="src/unifieddatalibrary/types/rf_band_type_get_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/rf_band_type_get_response.py">RfBandTypeGetResponse</a></code>
- <code title="get /udl/rfbandtype/queryhelp">client.rf_band_type.<a href="./src/unifieddatalibrary/resources/rf_band_type.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/rf_band_type_queryhelp_response.py">RfBandTypeQueryhelpResponse</a></code>
- <code title="get /udl/rfbandtype/tuple">client.rf_band_type.<a href="./src/unifieddatalibrary/resources/rf_band_type.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/rf_band_type_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/rf_band_type_tuple_response.py">RfBandTypeTupleResponse</a></code>

# RfEmitter

Types:

```python
from unifieddatalibrary.types import (
    RfEmitterListResponse,
    RfEmitterCountResponse,
    RfEmitterGetResponse,
    RfEmitterQueryhelpResponse,
    RfEmitterTupleResponse,
)
```

Methods:

- <code title="post /udl/rfemitter">client.rf_emitter.<a href="./src/unifieddatalibrary/resources/rf_emitter/rf_emitter.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/rf_emitter_create_params.py">params</a>) -> None</code>
- <code title="put /udl/rfemitter/{id}">client.rf_emitter.<a href="./src/unifieddatalibrary/resources/rf_emitter/rf_emitter.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/rf_emitter_update_params.py">params</a>) -> None</code>
- <code title="get /udl/rfemitter">client.rf_emitter.<a href="./src/unifieddatalibrary/resources/rf_emitter/rf_emitter.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/rf_emitter_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/rf_emitter_list_response.py">SyncOffsetPage[RfEmitterListResponse]</a></code>
- <code title="delete /udl/rfemitter/{id}">client.rf_emitter.<a href="./src/unifieddatalibrary/resources/rf_emitter/rf_emitter.py">delete</a>(id) -> None</code>
- <code title="get /udl/rfemitter/count">client.rf_emitter.<a href="./src/unifieddatalibrary/resources/rf_emitter/rf_emitter.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/rf_emitter_count_params.py">params</a>) -> str</code>
- <code title="get /udl/rfemitter/{id}">client.rf_emitter.<a href="./src/unifieddatalibrary/resources/rf_emitter/rf_emitter.py">get</a>(id, \*\*<a href="src/unifieddatalibrary/types/rf_emitter_get_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/rf_emitter_get_response.py">RfEmitterGetResponse</a></code>
- <code title="get /udl/rfemitter/queryhelp">client.rf_emitter.<a href="./src/unifieddatalibrary/resources/rf_emitter/rf_emitter.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/rf_emitter_queryhelp_response.py">RfEmitterQueryhelpResponse</a></code>
- <code title="get /udl/rfemitter/tuple">client.rf_emitter.<a href="./src/unifieddatalibrary/resources/rf_emitter/rf_emitter.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/rf_emitter_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/rf_emitter_tuple_response.py">RfEmitterTupleResponse</a></code>

## Staging

Types:

```python
from unifieddatalibrary.types.rf_emitter import (
    StagingRetrieveResponse,
    StagingListResponse,
    StagingQueryhelpResponse,
)
```

Methods:

- <code title="post /udl/rfemitterstaging">client.rf_emitter.staging.<a href="./src/unifieddatalibrary/resources/rf_emitter/staging.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/rf_emitter/staging_create_params.py">params</a>) -> None</code>
- <code title="get /udl/rfemitterstaging/{id}">client.rf_emitter.staging.<a href="./src/unifieddatalibrary/resources/rf_emitter/staging.py">retrieve</a>(id, \*\*<a href="src/unifieddatalibrary/types/rf_emitter/staging_retrieve_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/rf_emitter/staging_retrieve_response.py">StagingRetrieveResponse</a></code>
- <code title="put /udl/rfemitterstaging/{id}">client.rf_emitter.staging.<a href="./src/unifieddatalibrary/resources/rf_emitter/staging.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/rf_emitter/staging_update_params.py">params</a>) -> None</code>
- <code title="get /udl/rfemitterstaging">client.rf_emitter.staging.<a href="./src/unifieddatalibrary/resources/rf_emitter/staging.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/rf_emitter/staging_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/rf_emitter/staging_list_response.py">SyncOffsetPage[StagingListResponse]</a></code>
- <code title="delete /udl/rfemitterstaging/{id}">client.rf_emitter.staging.<a href="./src/unifieddatalibrary/resources/rf_emitter/staging.py">delete</a>(id) -> None</code>
- <code title="post /udl/rfemitterstaging/createBulk">client.rf_emitter.staging.<a href="./src/unifieddatalibrary/resources/rf_emitter/staging.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/rf_emitter/staging_create_bulk_params.py">params</a>) -> None</code>
- <code title="get /udl/rfemitterstaging/queryhelp">client.rf_emitter.staging.<a href="./src/unifieddatalibrary/resources/rf_emitter/staging.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/rf_emitter/staging_queryhelp_response.py">StagingQueryhelpResponse</a></code>

## Details

Types:

```python
from unifieddatalibrary.types.rf_emitter import (
    DetailListResponse,
    DetailCountResponse,
    DetailGetResponse,
    DetailQueryhelpResponse,
    DetailTupleResponse,
)
```

Methods:

- <code title="post /udl/rfemitterdetails">client.rf_emitter.details.<a href="./src/unifieddatalibrary/resources/rf_emitter/details.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/rf_emitter/detail_create_params.py">params</a>) -> None</code>
- <code title="put /udl/rfemitterdetails/{id}">client.rf_emitter.details.<a href="./src/unifieddatalibrary/resources/rf_emitter/details.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/rf_emitter/detail_update_params.py">params</a>) -> None</code>
- <code title="get /udl/rfemitterdetails">client.rf_emitter.details.<a href="./src/unifieddatalibrary/resources/rf_emitter/details.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/rf_emitter/detail_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/rf_emitter/detail_list_response.py">SyncOffsetPage[DetailListResponse]</a></code>
- <code title="delete /udl/rfemitterdetails/{id}">client.rf_emitter.details.<a href="./src/unifieddatalibrary/resources/rf_emitter/details.py">delete</a>(id) -> None</code>
- <code title="get /udl/rfemitterdetails/count">client.rf_emitter.details.<a href="./src/unifieddatalibrary/resources/rf_emitter/details.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/rf_emitter/detail_count_params.py">params</a>) -> str</code>
- <code title="get /udl/rfemitterdetails/{id}">client.rf_emitter.details.<a href="./src/unifieddatalibrary/resources/rf_emitter/details.py">get</a>(id, \*\*<a href="src/unifieddatalibrary/types/rf_emitter/detail_get_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/rf_emitter/detail_get_response.py">DetailGetResponse</a></code>
- <code title="get /udl/rfemitterdetails/queryhelp">client.rf_emitter.details.<a href="./src/unifieddatalibrary/resources/rf_emitter/details.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/rf_emitter/detail_queryhelp_response.py">DetailQueryhelpResponse</a></code>
- <code title="get /udl/rfemitterdetails/tuple">client.rf_emitter.details.<a href="./src/unifieddatalibrary/resources/rf_emitter/details.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/rf_emitter/detail_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/rf_emitter/detail_tuple_response.py">DetailTupleResponse</a></code>

# RouteStats

Types:

```python
from unifieddatalibrary.types import (
    RouteStatRetrieveResponse,
    RouteStatListResponse,
    RouteStatCountResponse,
    RouteStatQueryHelpResponse,
    RouteStatTupleResponse,
)
```

Methods:

- <code title="post /udl/routestats">client.route_stats.<a href="./src/unifieddatalibrary/resources/route_stats.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/route_stat_create_params.py">params</a>) -> None</code>
- <code title="get /udl/routestats/{id}">client.route_stats.<a href="./src/unifieddatalibrary/resources/route_stats.py">retrieve</a>(id, \*\*<a href="src/unifieddatalibrary/types/route_stat_retrieve_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/route_stat_retrieve_response.py">RouteStatRetrieveResponse</a></code>
- <code title="put /udl/routestats/{id}">client.route_stats.<a href="./src/unifieddatalibrary/resources/route_stats.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/route_stat_update_params.py">params</a>) -> None</code>
- <code title="get /udl/routestats">client.route_stats.<a href="./src/unifieddatalibrary/resources/route_stats.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/route_stat_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/route_stat_list_response.py">SyncOffsetPage[RouteStatListResponse]</a></code>
- <code title="delete /udl/routestats/{id}">client.route_stats.<a href="./src/unifieddatalibrary/resources/route_stats.py">delete</a>(id) -> None</code>
- <code title="get /udl/routestats/count">client.route_stats.<a href="./src/unifieddatalibrary/resources/route_stats.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/route_stat_count_params.py">params</a>) -> str</code>
- <code title="post /udl/routestats/createBulk">client.route_stats.<a href="./src/unifieddatalibrary/resources/route_stats.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/route_stat_create_bulk_params.py">params</a>) -> None</code>
- <code title="get /udl/routestats/queryhelp">client.route_stats.<a href="./src/unifieddatalibrary/resources/route_stats.py">query_help</a>() -> <a href="./src/unifieddatalibrary/types/route_stat_query_help_response.py">RouteStatQueryHelpResponse</a></code>
- <code title="get /udl/routestats/tuple">client.route_stats.<a href="./src/unifieddatalibrary/resources/route_stats.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/route_stat_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/route_stat_tuple_response.py">RouteStatTupleResponse</a></code>
- <code title="post /filedrop/udl-routestats">client.route_stats.<a href="./src/unifieddatalibrary/resources/route_stats.py">unvalidated_publish</a>(\*\*<a href="src/unifieddatalibrary/types/route_stat_unvalidated_publish_params.py">params</a>) -> None</code>

# SarObservation

Types:

```python
from unifieddatalibrary.types import (
    SarObservationListResponse,
    SarObservationCountResponse,
    SarObservationGetResponse,
    SarObservationQueryhelpResponse,
    SarObservationTupleResponse,
)
```

Methods:

- <code title="post /udl/sarobservation">client.sar_observation.<a href="./src/unifieddatalibrary/resources/sar_observation/sar_observation.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/sar_observation_create_params.py">params</a>) -> None</code>
- <code title="get /udl/sarobservation">client.sar_observation.<a href="./src/unifieddatalibrary/resources/sar_observation/sar_observation.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/sar_observation_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/sar_observation_list_response.py">SyncOffsetPage[SarObservationListResponse]</a></code>
- <code title="get /udl/sarobservation/count">client.sar_observation.<a href="./src/unifieddatalibrary/resources/sar_observation/sar_observation.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/sar_observation_count_params.py">params</a>) -> str</code>
- <code title="post /udl/sarobservation/createBulk">client.sar_observation.<a href="./src/unifieddatalibrary/resources/sar_observation/sar_observation.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/sar_observation_create_bulk_params.py">params</a>) -> None</code>
- <code title="get /udl/sarobservation/{id}">client.sar_observation.<a href="./src/unifieddatalibrary/resources/sar_observation/sar_observation.py">get</a>(id, \*\*<a href="src/unifieddatalibrary/types/sar_observation_get_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/sar_observation_get_response.py">SarObservationGetResponse</a></code>
- <code title="get /udl/sarobservation/queryhelp">client.sar_observation.<a href="./src/unifieddatalibrary/resources/sar_observation/sar_observation.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/sar_observation_queryhelp_response.py">SarObservationQueryhelpResponse</a></code>
- <code title="get /udl/sarobservation/tuple">client.sar_observation.<a href="./src/unifieddatalibrary/resources/sar_observation/sar_observation.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/sar_observation_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/sar_observation_tuple_response.py">SarObservationTupleResponse</a></code>
- <code title="post /filedrop/udl-sar">client.sar_observation.<a href="./src/unifieddatalibrary/resources/sar_observation/sar_observation.py">unvalidated_publish</a>(\*\*<a href="src/unifieddatalibrary/types/sar_observation_unvalidated_publish_params.py">params</a>) -> None</code>

## History

Types:

```python
from unifieddatalibrary.types.sar_observation import HistoryRetrieveResponse, HistoryCountResponse
```

Methods:

- <code title="get /udl/sarobservation/history">client.sar_observation.history.<a href="./src/unifieddatalibrary/resources/sar_observation/history.py">retrieve</a>(\*\*<a href="src/unifieddatalibrary/types/sar_observation/history_retrieve_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/sar_observation/history_retrieve_response.py">HistoryRetrieveResponse</a></code>
- <code title="get /udl/sarobservation/history/aodr">client.sar_observation.history.<a href="./src/unifieddatalibrary/resources/sar_observation/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/sar_observation/history_aodr_params.py">params</a>) -> None</code>
- <code title="get /udl/sarobservation/history/count">client.sar_observation.history.<a href="./src/unifieddatalibrary/resources/sar_observation/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/sar_observation/history_count_params.py">params</a>) -> str</code>

# Scientific

Types:

```python
from unifieddatalibrary.types import (
    ScientificListResponse,
    ScientificCountResponse,
    ScientificGetResponse,
    ScientificQueryhelpResponse,
    ScientificTupleResponse,
)
```

Methods:

- <code title="post /udl/scientific">client.scientific.<a href="./src/unifieddatalibrary/resources/scientific.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/scientific_create_params.py">params</a>) -> None</code>
- <code title="put /udl/scientific/{id}">client.scientific.<a href="./src/unifieddatalibrary/resources/scientific.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/scientific_update_params.py">params</a>) -> None</code>
- <code title="get /udl/scientific">client.scientific.<a href="./src/unifieddatalibrary/resources/scientific.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/scientific_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/scientific_list_response.py">SyncOffsetPage[ScientificListResponse]</a></code>
- <code title="delete /udl/scientific/{id}">client.scientific.<a href="./src/unifieddatalibrary/resources/scientific.py">delete</a>(id) -> None</code>
- <code title="get /udl/scientific/count">client.scientific.<a href="./src/unifieddatalibrary/resources/scientific.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/scientific_count_params.py">params</a>) -> str</code>
- <code title="get /udl/scientific/{id}">client.scientific.<a href="./src/unifieddatalibrary/resources/scientific.py">get</a>(id, \*\*<a href="src/unifieddatalibrary/types/scientific_get_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/scientific_get_response.py">ScientificGetResponse</a></code>
- <code title="get /udl/scientific/queryhelp">client.scientific.<a href="./src/unifieddatalibrary/resources/scientific.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/scientific_queryhelp_response.py">ScientificQueryhelpResponse</a></code>
- <code title="get /udl/scientific/tuple">client.scientific.<a href="./src/unifieddatalibrary/resources/scientific.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/scientific_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/scientific_tuple_response.py">ScientificTupleResponse</a></code>

# Scs

Types:

```python
from unifieddatalibrary.types import (
    SearchCriterion,
    SearchLogicalCriterion,
    ScAllowableFileExtensionsResponse,
    ScAllowableFileMimesResponse,
    ScCopyResponse,
    ScFileUploadResponse,
    ScHasWriteAccessResponse,
    ScMoveResponse,
    ScSearchResponse,
)
```

Methods:

- <code title="delete /scs/delete">client.scs.<a href="./src/unifieddatalibrary/resources/scs/scs.py">delete</a>(\*\*<a href="src/unifieddatalibrary/types/sc_delete_params.py">params</a>) -> None</code>
- <code title="get /scs/allowableFileExtensions">client.scs.<a href="./src/unifieddatalibrary/resources/scs/scs.py">allowable_file_extensions</a>() -> <a href="./src/unifieddatalibrary/types/sc_allowable_file_extensions_response.py">ScAllowableFileExtensionsResponse</a></code>
- <code title="get /scs/allowableFileMimes">client.scs.<a href="./src/unifieddatalibrary/resources/scs/scs.py">allowable_file_mimes</a>() -> <a href="./src/unifieddatalibrary/types/sc_allowable_file_mimes_response.py">ScAllowableFileMimesResponse</a></code>
- <code title="post /scs/copy">client.scs.<a href="./src/unifieddatalibrary/resources/scs/scs.py">copy</a>(\*\*<a href="src/unifieddatalibrary/types/sc_copy_params.py">params</a>) -> str</code>
- <code title="post /scs/download">client.scs.<a href="./src/unifieddatalibrary/resources/scs/scs.py">download</a>(\*\*<a href="src/unifieddatalibrary/types/sc_download_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="get /scs/download">client.scs.<a href="./src/unifieddatalibrary/resources/scs/scs.py">file_download</a>(\*\*<a href="src/unifieddatalibrary/types/sc_file_download_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="post /scs/file">client.scs.<a href="./src/unifieddatalibrary/resources/scs/scs.py">file_upload</a>(file_content, \*\*<a href="src/unifieddatalibrary/types/sc_file_upload_params.py">params</a>) -> str</code>
- <code title="get /scs/userHasWriteAccess">client.scs.<a href="./src/unifieddatalibrary/resources/scs/scs.py">has_write_access</a>(\*\*<a href="src/unifieddatalibrary/types/sc_has_write_access_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/sc_has_write_access_response.py">ScHasWriteAccessResponse</a></code>
- <code title="put /scs/move">client.scs.<a href="./src/unifieddatalibrary/resources/scs/scs.py">move</a>(\*\*<a href="src/unifieddatalibrary/types/sc_move_params.py">params</a>) -> str</code>
- <code title="put /scs/rename">client.scs.<a href="./src/unifieddatalibrary/resources/scs/scs.py">rename</a>(\*\*<a href="src/unifieddatalibrary/types/sc_rename_params.py">params</a>) -> None</code>
- <code title="post /scs/search">client.scs.<a href="./src/unifieddatalibrary/resources/scs/scs.py">search</a>(\*\*<a href="src/unifieddatalibrary/types/sc_search_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/sc_search_response.py">ScSearchResponse</a></code>

## Notifications

Types:

```python
from unifieddatalibrary.types.scs import NotificationListResponse
```

Methods:

- <code title="get /scs/notifications/{offset}">client.scs.notifications.<a href="./src/unifieddatalibrary/resources/scs/notifications/notifications.py">list</a>(offset, \*\*<a href="src/unifieddatalibrary/types/scs/notification_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/scs/notification_list_response.py">SyncOffsetPage[NotificationListResponse]</a></code>

### Offset

Types:

```python
from unifieddatalibrary.types.scs.notifications import OffsetGetResponse
```

Methods:

- <code title="get /scs/notifications/offsets">client.scs.notifications.offset.<a href="./src/unifieddatalibrary/resources/scs/notifications/offset.py">get</a>() -> <a href="./src/unifieddatalibrary/types/scs/notifications/offset_get_response.py">OffsetGetResponse</a></code>
- <code title="get /scs/notifications/getLatestOffset">client.scs.notifications.offset.<a href="./src/unifieddatalibrary/resources/scs/notifications/offset.py">get_latest</a>() -> None</code>

## File

Methods:

- <code title="get /scs/file">client.scs.file.<a href="./src/unifieddatalibrary/resources/scs/file.py">retrieve</a>(\*\*<a href="src/unifieddatalibrary/types/scs/file_retrieve_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/shared/file_data.py">FileData</a></code>
- <code title="patch /scs/file">client.scs.file.<a href="./src/unifieddatalibrary/resources/scs/file.py">update</a>(\*\*<a href="src/unifieddatalibrary/types/scs/file_update_params.py">params</a>) -> None</code>
- <code title="get /scs/list">client.scs.file.<a href="./src/unifieddatalibrary/resources/scs/file.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/scs/file_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/shared/file_data.py">SyncOffsetPage[FileData]</a></code>

## Folders

Types:

```python
from unifieddatalibrary.types.scs import FolderCreateResponse
```

Methods:

- <code title="post /scs/folder">client.scs.folders.<a href="./src/unifieddatalibrary/resources/scs/folders.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/scs/folder_create_params.py">params</a>) -> str</code>
- <code title="get /scs/folder">client.scs.folders.<a href="./src/unifieddatalibrary/resources/scs/folders.py">retrieve</a>(\*\*<a href="src/unifieddatalibrary/types/scs/folder_retrieve_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/shared/file_data.py">FileData</a></code>
- <code title="patch /scs/folder">client.scs.folders.<a href="./src/unifieddatalibrary/resources/scs/folders.py">update</a>(\*\*<a href="src/unifieddatalibrary/types/scs/folder_update_params.py">params</a>) -> None</code>

## Paths

Types:

```python
from unifieddatalibrary.types.scs import PathCreateWithFileResponse
```

Methods:

- <code title="post /scs/path">client.scs.paths.<a href="./src/unifieddatalibrary/resources/scs/paths.py">create_with_file</a>(file_content, \*\*<a href="src/unifieddatalibrary/types/scs/path_create_with_file_params.py">params</a>) -> str</code>

## View

Methods:

- <code title="get /scs/view/{id}">client.scs.view.<a href="./src/unifieddatalibrary/resources/scs/view.py">get</a>(id, \*\*<a href="src/unifieddatalibrary/types/scs/view_get_params.py">params</a>) -> BinaryAPIResponse</code>

## V2

Types:

```python
from unifieddatalibrary.types.scs import Attachment, ScsEntity, V2SearchResponse
```

Methods:

- <code title="patch /scs/v2/update">client.scs.v2.<a href="./src/unifieddatalibrary/resources/scs/v2.py">update</a>(\*\*<a href="src/unifieddatalibrary/types/scs/v2_update_params.py">params</a>) -> None</code>
- <code title="get /scs/v2/list">client.scs.v2.<a href="./src/unifieddatalibrary/resources/scs/v2.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/scs/v2_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/scs/scs_entity.py">SyncOffsetPage[ScsEntity]</a></code>
- <code title="delete /scs/v2/delete">client.scs.v2.<a href="./src/unifieddatalibrary/resources/scs/v2.py">delete</a>(\*\*<a href="src/unifieddatalibrary/types/scs/v2_delete_params.py">params</a>) -> None</code>
- <code title="post /scs/v2/copy">client.scs.v2.<a href="./src/unifieddatalibrary/resources/scs/v2.py">copy</a>(\*\*<a href="src/unifieddatalibrary/types/scs/v2_copy_params.py">params</a>) -> None</code>
- <code title="post /scs/v2/file">client.scs.v2.<a href="./src/unifieddatalibrary/resources/scs/v2.py">file_upload</a>(file_content, \*\*<a href="src/unifieddatalibrary/types/scs/v2_file_upload_params.py">params</a>) -> None</code>
- <code title="post /scs/v2/folder">client.scs.v2.<a href="./src/unifieddatalibrary/resources/scs/v2.py">folder_create</a>(\*\*<a href="src/unifieddatalibrary/types/scs/v2_folder_create_params.py">params</a>) -> None</code>
- <code title="put /scs/v2/move">client.scs.v2.<a href="./src/unifieddatalibrary/resources/scs/v2.py">move</a>(\*\*<a href="src/unifieddatalibrary/types/scs/v2_move_params.py">params</a>) -> None</code>
- <code title="post /scs/v2/search">client.scs.v2.<a href="./src/unifieddatalibrary/resources/scs/v2.py">search</a>(\*\*<a href="src/unifieddatalibrary/types/scs/v2_search_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/scs/v2_search_response.py">V2SearchResponse</a></code>

# SecureMessaging

Types:

```python
from unifieddatalibrary.types import TopicDetails, SecureMessagingListTopicsResponse
```

Methods:

- <code title="get /sm/describeTopic/{topic}">client.secure_messaging.<a href="./src/unifieddatalibrary/resources/secure_messaging.py">describe_topic</a>(topic, \*\*<a href="src/unifieddatalibrary/types/secure_messaging_describe_topic_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/topic_details.py">TopicDetails</a></code>
- <code title="get /sm/getLatestOffset/{topic}">client.secure_messaging.<a href="./src/unifieddatalibrary/resources/secure_messaging.py">get_latest_offset</a>(topic, \*\*<a href="src/unifieddatalibrary/types/secure_messaging_get_latest_offset_params.py">params</a>) -> None</code>
- <code title="get /sm/getMessages/{topic}/{offset}">client.secure_messaging.<a href="./src/unifieddatalibrary/resources/secure_messaging.py">get_messages</a>(offset, \*, topic, \*\*<a href="src/unifieddatalibrary/types/secure_messaging_get_messages_params.py">params</a>) -> None</code>
- <code title="get /sm/listTopics">client.secure_messaging.<a href="./src/unifieddatalibrary/resources/secure_messaging.py">list_topics</a>() -> <a href="./src/unifieddatalibrary/types/secure_messaging_list_topics_response.py">SecureMessagingListTopicsResponse</a></code>

# Sensor

Types:

```python
from unifieddatalibrary.types import (
    SensorListResponse,
    SensorCountResponse,
    SensorGetResponse,
    SensorQueryhelpResponse,
    SensorTupleResponse,
)
```

Methods:

- <code title="post /udl/sensor">client.sensor.<a href="./src/unifieddatalibrary/resources/sensor/sensor.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/sensor_create_params.py">params</a>) -> None</code>
- <code title="put /udl/sensor/{id}">client.sensor.<a href="./src/unifieddatalibrary/resources/sensor/sensor.py">update</a>(id, \*\*<a href="src/unifieddatalibrary/types/sensor_update_params.py">params</a>) -> None</code>
- <code title="get /udl/sensor">client.sensor.<a href="./src/unifieddatalibrary/resources/sensor/sensor.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/sensor_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/sensor_list_response.py">SyncOffsetPage[SensorListResponse]</a></code>
- <code title="delete /udl/sensor/{id}">client.sensor.<a href="./src/unifieddatalibrary/resources/sensor/sensor.py">delete</a>(id) -> None</code>
- <code title="get /udl/sensor/count">client.sensor.<a href="./src/unifieddatalibrary/resources/sensor/sensor.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/sensor_count_params.py">params</a>) -> str</code>
- <code title="get /udl/sensor/{id}">client.sensor.<a href="./src/unifieddatalibrary/resources/sensor/sensor.py">get</a>(id, \*\*<a href="src/unifieddatalibrary/types/sensor_get_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/sensor_get_response.py">SensorGetResponse</a></code>
- <code title="get /udl/sensor/queryhelp">client.sensor.<a href="./src/unifieddatalibrary/resources/sensor/sensor.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/sensor_queryhelp_response.py">SensorQueryhelpResponse</a></code>
- <code title="get /udl/sensor/tuple">client.sensor.<a href="./src/unifieddatalibrary/resources/sensor/sensor.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/sensor_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/sensor_tuple_response.py">SensorTupleResponse</a></code>

## Calibration

Types:

```python
from unifieddatalibrary.types.sensor import (
    CalibrationRetrieveResponse,
    CalibrationListResponse,
    CalibrationCountResponse,
    CalibrationQueryHelpResponse,
    CalibrationTupleResponse,
)
```

Methods:

- <code title="post /udl/sensorcalibration">client.sensor.calibration.<a href="./src/unifieddatalibrary/resources/sensor/calibration/calibration.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/sensor/calibration_create_params.py">params</a>) -> None</code>
- <code title="get /udl/sensorcalibration/{id}">client.sensor.calibration.<a href="./src/unifieddatalibrary/resources/sensor/calibration/calibration.py">retrieve</a>(id, \*\*<a href="src/unifieddatalibrary/types/sensor/calibration_retrieve_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/sensor/calibration_retrieve_response.py">CalibrationRetrieveResponse</a></code>
- <code title="get /udl/sensorcalibration">client.sensor.calibration.<a href="./src/unifieddatalibrary/resources/sensor/calibration/calibration.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/sensor/calibration_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/sensor/calibration_list_response.py">SyncOffsetPage[CalibrationListResponse]</a></code>
- <code title="get /udl/sensorcalibration/count">client.sensor.calibration.<a href="./src/unifieddatalibrary/resources/sensor/calibration/calibration.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/sensor/calibration_count_params.py">params</a>) -> str</code>
- <code title="post /udl/sensorcalibration/createBulk">client.sensor.calibration.<a href="./src/unifieddatalibrary/resources/sensor/calibration/calibration.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/sensor/calibration_create_bulk_params.py">params</a>) -> None</code>
- <code title="get /udl/sensorcalibration/queryhelp">client.sensor.calibration.<a href="./src/unifieddatalibrary/resources/sensor/calibration/calibration.py">query_help</a>() -> <a href="./src/unifieddatalibrary/types/sensor/calibration_query_help_response.py">CalibrationQueryHelpResponse</a></code>
- <code title="get /udl/sensorcalibration/tuple">client.sensor.calibration.<a href="./src/unifieddatalibrary/resources/sensor/calibration/calibration.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/sensor/calibration_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/sensor/calibration_tuple_response.py">CalibrationTupleResponse</a></code>
- <code title="post /filedrop/udl-sensorcalibration">client.sensor.calibration.<a href="./src/unifieddatalibrary/resources/sensor/calibration/calibration.py">unvalidated_publish</a>(\*\*<a href="src/unifieddatalibrary/types/sensor/calibration_unvalidated_publish_params.py">params</a>) -> None</code>

### History

Types:

```python
from unifieddatalibrary.types.sensor.calibration import HistoryListResponse, HistoryCountResponse
```

Methods:

- <code title="get /udl/sensorcalibration/history">client.sensor.calibration.history.<a href="./src/unifieddatalibrary/resources/sensor/calibration/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/sensor/calibration/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/sensor/calibration/history_list_response.py">SyncOffsetPage[HistoryListResponse]</a></code>
- <code title="get /udl/sensorcalibration/history/aodr">client.sensor.calibration.history.<a href="./src/unifieddatalibrary/resources/sensor/calibration/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/sensor/calibration/history_aodr_params.py">params</a>) -> None</code>
- <code title="get /udl/sensorcalibration/history/count">client.sensor.calibration.history.<a href="./src/unifieddatalibrary/resources/sensor/calibration/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/sensor/calibration/history_count_params.py">params</a>) -> str</code>

# SensorMaintenance

Types:

```python
from unifieddatalibrary.types import (
    SensorMaintenanceListResponse,
    SensorMaintenanceCountResponse,
    SensorMaintenanceGetResponse,
    SensorMaintenanceListCurrentResponse,
    SensorMaintenanceQueryHelpResponse,
    SensorMaintenanceTupleResponse,
)
```

Methods:

- <code title="post /udl/sensormaintenance">client.sensor_maintenance.<a href="./src/unifieddatalibrary/resources/sensor_maintenance/sensor_maintenance.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/sensor_maintenance_create_params.py">params</a>) -> None</code>
- <code title="put /udl/sensormaintenance/{id}">client.sensor_maintenance.<a href="./src/unifieddatalibrary/resources/sensor_maintenance/sensor_maintenance.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/sensor_maintenance_update_params.py">params</a>) -> None</code>
- <code title="get /udl/sensormaintenance">client.sensor_maintenance.<a href="./src/unifieddatalibrary/resources/sensor_maintenance/sensor_maintenance.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/sensor_maintenance_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/sensor_maintenance_list_response.py">SyncOffsetPage[SensorMaintenanceListResponse]</a></code>
- <code title="delete /udl/sensormaintenance/{id}">client.sensor_maintenance.<a href="./src/unifieddatalibrary/resources/sensor_maintenance/sensor_maintenance.py">delete</a>(id) -> None</code>
- <code title="get /udl/sensormaintenance/count">client.sensor_maintenance.<a href="./src/unifieddatalibrary/resources/sensor_maintenance/sensor_maintenance.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/sensor_maintenance_count_params.py">params</a>) -> str</code>
- <code title="post /udl/sensormaintenance/createBulk">client.sensor_maintenance.<a href="./src/unifieddatalibrary/resources/sensor_maintenance/sensor_maintenance.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/sensor_maintenance_create_bulk_params.py">params</a>) -> None</code>
- <code title="get /udl/sensormaintenance/{id}">client.sensor_maintenance.<a href="./src/unifieddatalibrary/resources/sensor_maintenance/sensor_maintenance.py">get</a>(id, \*\*<a href="src/unifieddatalibrary/types/sensor_maintenance_get_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/sensor_maintenance_get_response.py">SensorMaintenanceGetResponse</a></code>
- <code title="get /udl/sensormaintenance/current">client.sensor_maintenance.<a href="./src/unifieddatalibrary/resources/sensor_maintenance/sensor_maintenance.py">list_current</a>(\*\*<a href="src/unifieddatalibrary/types/sensor_maintenance_list_current_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/sensor_maintenance_list_current_response.py">SyncOffsetPage[SensorMaintenanceListCurrentResponse]</a></code>
- <code title="get /udl/sensormaintenance/queryhelp">client.sensor_maintenance.<a href="./src/unifieddatalibrary/resources/sensor_maintenance/sensor_maintenance.py">query_help</a>() -> <a href="./src/unifieddatalibrary/types/sensor_maintenance_query_help_response.py">SensorMaintenanceQueryHelpResponse</a></code>
- <code title="get /udl/sensormaintenance/tuple">client.sensor_maintenance.<a href="./src/unifieddatalibrary/resources/sensor_maintenance/sensor_maintenance.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/sensor_maintenance_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/sensor_maintenance_tuple_response.py">SensorMaintenanceTupleResponse</a></code>

## History

Types:

```python
from unifieddatalibrary.types.sensor_maintenance import HistoryListResponse, HistoryCountResponse
```

Methods:

- <code title="get /udl/sensormaintenance/history">client.sensor_maintenance.history.<a href="./src/unifieddatalibrary/resources/sensor_maintenance/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/sensor_maintenance/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/sensor_maintenance/history_list_response.py">SyncOffsetPage[HistoryListResponse]</a></code>
- <code title="get /udl/sensormaintenance/history/aodr">client.sensor_maintenance.history.<a href="./src/unifieddatalibrary/resources/sensor_maintenance/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/sensor_maintenance/history_aodr_params.py">params</a>) -> None</code>
- <code title="get /udl/sensormaintenance/history/count">client.sensor_maintenance.history.<a href="./src/unifieddatalibrary/resources/sensor_maintenance/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/sensor_maintenance/history_count_params.py">params</a>) -> str</code>

# SensorObservationType

Types:

```python
from unifieddatalibrary.types import (
    SensorObservationTypeListResponse,
    SensorObservationTypeGetResponse,
)
```

Methods:

- <code title="get /udl/sensorobservationtype">client.sensor_observation_type.<a href="./src/unifieddatalibrary/resources/sensor_observation_type.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/sensor_observation_type_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/sensor_observation_type_list_response.py">SyncOffsetPage[SensorObservationTypeListResponse]</a></code>
- <code title="get /udl/sensorobservationtype/{id}">client.sensor_observation_type.<a href="./src/unifieddatalibrary/resources/sensor_observation_type.py">get</a>(id, \*\*<a href="src/unifieddatalibrary/types/sensor_observation_type_get_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/sensor_observation_type_get_response.py">SensorObservationTypeGetResponse</a></code>

# SensorPlan

Types:

```python
from unifieddatalibrary.types import (
    SensorPlanListResponse,
    SensorPlanCountResponse,
    SensorPlanGetResponse,
    SensorPlanQueryhelpResponse,
    SensorPlanTupleResponse,
)
```

Methods:

- <code title="post /udl/sensorplan">client.sensor_plan.<a href="./src/unifieddatalibrary/resources/sensor_plan/sensor_plan.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/sensor_plan_create_params.py">params</a>) -> None</code>
- <code title="put /udl/sensorplan/{id}">client.sensor_plan.<a href="./src/unifieddatalibrary/resources/sensor_plan/sensor_plan.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/sensor_plan_update_params.py">params</a>) -> None</code>
- <code title="get /udl/sensorplan">client.sensor_plan.<a href="./src/unifieddatalibrary/resources/sensor_plan/sensor_plan.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/sensor_plan_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/sensor_plan_list_response.py">SyncOffsetPage[SensorPlanListResponse]</a></code>
- <code title="get /udl/sensorplan/count">client.sensor_plan.<a href="./src/unifieddatalibrary/resources/sensor_plan/sensor_plan.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/sensor_plan_count_params.py">params</a>) -> str</code>
- <code title="get /udl/sensorplan/{id}">client.sensor_plan.<a href="./src/unifieddatalibrary/resources/sensor_plan/sensor_plan.py">get</a>(id, \*\*<a href="src/unifieddatalibrary/types/sensor_plan_get_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/sensor_plan_get_response.py">SensorPlanGetResponse</a></code>
- <code title="get /udl/sensorplan/queryhelp">client.sensor_plan.<a href="./src/unifieddatalibrary/resources/sensor_plan/sensor_plan.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/sensor_plan_queryhelp_response.py">SensorPlanQueryhelpResponse</a></code>
- <code title="get /udl/sensorplan/tuple">client.sensor_plan.<a href="./src/unifieddatalibrary/resources/sensor_plan/sensor_plan.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/sensor_plan_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/sensor_plan_tuple_response.py">SensorPlanTupleResponse</a></code>
- <code title="post /filedrop/udl-sensorplan">client.sensor_plan.<a href="./src/unifieddatalibrary/resources/sensor_plan/sensor_plan.py">unvalidated_publish</a>(\*\*<a href="src/unifieddatalibrary/types/sensor_plan_unvalidated_publish_params.py">params</a>) -> None</code>

## History

Types:

```python
from unifieddatalibrary.types.sensor_plan import HistoryListResponse, HistoryCountResponse
```

Methods:

- <code title="get /udl/sensorplan/history">client.sensor_plan.history.<a href="./src/unifieddatalibrary/resources/sensor_plan/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/sensor_plan/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/sensor_plan/history_list_response.py">SyncOffsetPage[HistoryListResponse]</a></code>
- <code title="get /udl/sensorplan/history/aodr">client.sensor_plan.history.<a href="./src/unifieddatalibrary/resources/sensor_plan/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/sensor_plan/history_aodr_params.py">params</a>) -> None</code>
- <code title="get /udl/sensorplan/history/count">client.sensor_plan.history.<a href="./src/unifieddatalibrary/resources/sensor_plan/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/sensor_plan/history_count_params.py">params</a>) -> str</code>

# SensorType

Types:

```python
from unifieddatalibrary.types import SensorTypeListResponse, SensorTypeGetResponse
```

Methods:

- <code title="get /udl/sensortype">client.sensor_type.<a href="./src/unifieddatalibrary/resources/sensor_type.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/sensor_type_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/sensor_type_list_response.py">SyncOffsetPage[SensorTypeListResponse]</a></code>
- <code title="get /udl/sensortype/{id}">client.sensor_type.<a href="./src/unifieddatalibrary/resources/sensor_type.py">get</a>(id, \*\*<a href="src/unifieddatalibrary/types/sensor_type_get_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/sensor_type_get_response.py">SensorTypeGetResponse</a></code>

# SeraDataCommDetails

Types:

```python
from unifieddatalibrary.types import (
    SeraDataCommDetailListResponse,
    SeraDataCommDetailCountResponse,
    SeraDataCommDetailGetResponse,
    SeraDataCommDetailQueryhelpResponse,
    SeraDataCommDetailTupleResponse,
)
```

Methods:

- <code title="post /udl/seradatacommdetails">client.sera_data_comm_details.<a href="./src/unifieddatalibrary/resources/sera_data_comm_details.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/sera_data_comm_detail_create_params.py">params</a>) -> None</code>
- <code title="put /udl/seradatacommdetails/{id}">client.sera_data_comm_details.<a href="./src/unifieddatalibrary/resources/sera_data_comm_details.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/sera_data_comm_detail_update_params.py">params</a>) -> None</code>
- <code title="get /udl/seradatacommdetails">client.sera_data_comm_details.<a href="./src/unifieddatalibrary/resources/sera_data_comm_details.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/sera_data_comm_detail_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/sera_data_comm_detail_list_response.py">SyncOffsetPage[SeraDataCommDetailListResponse]</a></code>
- <code title="delete /udl/seradatacommdetails/{id}">client.sera_data_comm_details.<a href="./src/unifieddatalibrary/resources/sera_data_comm_details.py">delete</a>(id) -> None</code>
- <code title="get /udl/seradatacommdetails/count">client.sera_data_comm_details.<a href="./src/unifieddatalibrary/resources/sera_data_comm_details.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/sera_data_comm_detail_count_params.py">params</a>) -> str</code>
- <code title="get /udl/seradatacommdetails/{id}">client.sera_data_comm_details.<a href="./src/unifieddatalibrary/resources/sera_data_comm_details.py">get</a>(id, \*\*<a href="src/unifieddatalibrary/types/sera_data_comm_detail_get_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/sera_data_comm_detail_get_response.py">SeraDataCommDetailGetResponse</a></code>
- <code title="get /udl/seradatacommdetails/queryhelp">client.sera_data_comm_details.<a href="./src/unifieddatalibrary/resources/sera_data_comm_details.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/sera_data_comm_detail_queryhelp_response.py">SeraDataCommDetailQueryhelpResponse</a></code>
- <code title="get /udl/seradatacommdetails/tuple">client.sera_data_comm_details.<a href="./src/unifieddatalibrary/resources/sera_data_comm_details.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/sera_data_comm_detail_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/sera_data_comm_detail_tuple_response.py">SeraDataCommDetailTupleResponse</a></code>

# SeraDataEarlyWarning

Types:

```python
from unifieddatalibrary.types import (
    SeraDataEarlyWarningListResponse,
    SeraDataEarlyWarningCountResponse,
    SeraDataEarlyWarningGetResponse,
    SeraDataEarlyWarningQueryhelpResponse,
    SeraDataEarlyWarningTupleResponse,
)
```

Methods:

- <code title="post /udl/seradataearlywarning">client.sera_data_early_warning.<a href="./src/unifieddatalibrary/resources/sera_data_early_warning.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/sera_data_early_warning_create_params.py">params</a>) -> None</code>
- <code title="put /udl/seradataearlywarning/{id}">client.sera_data_early_warning.<a href="./src/unifieddatalibrary/resources/sera_data_early_warning.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/sera_data_early_warning_update_params.py">params</a>) -> None</code>
- <code title="get /udl/seradataearlywarning">client.sera_data_early_warning.<a href="./src/unifieddatalibrary/resources/sera_data_early_warning.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/sera_data_early_warning_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/sera_data_early_warning_list_response.py">SyncOffsetPage[SeraDataEarlyWarningListResponse]</a></code>
- <code title="delete /udl/seradataearlywarning/{id}">client.sera_data_early_warning.<a href="./src/unifieddatalibrary/resources/sera_data_early_warning.py">delete</a>(id) -> None</code>
- <code title="get /udl/seradataearlywarning/count">client.sera_data_early_warning.<a href="./src/unifieddatalibrary/resources/sera_data_early_warning.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/sera_data_early_warning_count_params.py">params</a>) -> str</code>
- <code title="get /udl/seradataearlywarning/{id}">client.sera_data_early_warning.<a href="./src/unifieddatalibrary/resources/sera_data_early_warning.py">get</a>(id, \*\*<a href="src/unifieddatalibrary/types/sera_data_early_warning_get_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/sera_data_early_warning_get_response.py">SeraDataEarlyWarningGetResponse</a></code>
- <code title="get /udl/seradataearlywarning/queryhelp">client.sera_data_early_warning.<a href="./src/unifieddatalibrary/resources/sera_data_early_warning.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/sera_data_early_warning_queryhelp_response.py">SeraDataEarlyWarningQueryhelpResponse</a></code>
- <code title="get /udl/seradataearlywarning/tuple">client.sera_data_early_warning.<a href="./src/unifieddatalibrary/resources/sera_data_early_warning.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/sera_data_early_warning_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/sera_data_early_warning_tuple_response.py">SeraDataEarlyWarningTupleResponse</a></code>

# SeraDataNavigation

Types:

```python
from unifieddatalibrary.types import (
    SeraDataNavigationListResponse,
    SeraDataNavigationCountResponse,
    SeraDataNavigationGetResponse,
    SeraDataNavigationQueryhelpResponse,
    SeraDataNavigationTupleResponse,
)
```

Methods:

- <code title="post /udl/seradatanavigation">client.sera_data_navigation.<a href="./src/unifieddatalibrary/resources/sera_data_navigation.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/sera_data_navigation_create_params.py">params</a>) -> None</code>
- <code title="put /udl/seradatanavigation/{id}">client.sera_data_navigation.<a href="./src/unifieddatalibrary/resources/sera_data_navigation.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/sera_data_navigation_update_params.py">params</a>) -> None</code>
- <code title="get /udl/seradatanavigation">client.sera_data_navigation.<a href="./src/unifieddatalibrary/resources/sera_data_navigation.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/sera_data_navigation_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/sera_data_navigation_list_response.py">SyncOffsetPage[SeraDataNavigationListResponse]</a></code>
- <code title="delete /udl/seradatanavigation/{id}">client.sera_data_navigation.<a href="./src/unifieddatalibrary/resources/sera_data_navigation.py">delete</a>(id) -> None</code>
- <code title="get /udl/seradatanavigation/count">client.sera_data_navigation.<a href="./src/unifieddatalibrary/resources/sera_data_navigation.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/sera_data_navigation_count_params.py">params</a>) -> str</code>
- <code title="get /udl/seradatanavigation/{id}">client.sera_data_navigation.<a href="./src/unifieddatalibrary/resources/sera_data_navigation.py">get</a>(id, \*\*<a href="src/unifieddatalibrary/types/sera_data_navigation_get_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/sera_data_navigation_get_response.py">SeraDataNavigationGetResponse</a></code>
- <code title="get /udl/seradatanavigation/queryhelp">client.sera_data_navigation.<a href="./src/unifieddatalibrary/resources/sera_data_navigation.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/sera_data_navigation_queryhelp_response.py">SeraDataNavigationQueryhelpResponse</a></code>
- <code title="get /udl/seradatanavigation/tuple">client.sera_data_navigation.<a href="./src/unifieddatalibrary/resources/sera_data_navigation.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/sera_data_navigation_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/sera_data_navigation_tuple_response.py">SeraDataNavigationTupleResponse</a></code>

# SeradataOpticalPayload

Types:

```python
from unifieddatalibrary.types import (
    SeradataOpticalPayloadListResponse,
    SeradataOpticalPayloadCountResponse,
    SeradataOpticalPayloadGetResponse,
    SeradataOpticalPayloadQueryhelpResponse,
    SeradataOpticalPayloadTupleResponse,
)
```

Methods:

- <code title="post /udl/seradataopticalpayload">client.seradata_optical_payload.<a href="./src/unifieddatalibrary/resources/seradata_optical_payload.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/seradata_optical_payload_create_params.py">params</a>) -> None</code>
- <code title="put /udl/seradataopticalpayload/{id}">client.seradata_optical_payload.<a href="./src/unifieddatalibrary/resources/seradata_optical_payload.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/seradata_optical_payload_update_params.py">params</a>) -> None</code>
- <code title="get /udl/seradataopticalpayload">client.seradata_optical_payload.<a href="./src/unifieddatalibrary/resources/seradata_optical_payload.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/seradata_optical_payload_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/seradata_optical_payload_list_response.py">SyncOffsetPage[SeradataOpticalPayloadListResponse]</a></code>
- <code title="delete /udl/seradataopticalpayload/{id}">client.seradata_optical_payload.<a href="./src/unifieddatalibrary/resources/seradata_optical_payload.py">delete</a>(id) -> None</code>
- <code title="get /udl/seradataopticalpayload/count">client.seradata_optical_payload.<a href="./src/unifieddatalibrary/resources/seradata_optical_payload.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/seradata_optical_payload_count_params.py">params</a>) -> str</code>
- <code title="get /udl/seradataopticalpayload/{id}">client.seradata_optical_payload.<a href="./src/unifieddatalibrary/resources/seradata_optical_payload.py">get</a>(id, \*\*<a href="src/unifieddatalibrary/types/seradata_optical_payload_get_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/seradata_optical_payload_get_response.py">SeradataOpticalPayloadGetResponse</a></code>
- <code title="get /udl/seradataopticalpayload/queryhelp">client.seradata_optical_payload.<a href="./src/unifieddatalibrary/resources/seradata_optical_payload.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/seradata_optical_payload_queryhelp_response.py">SeradataOpticalPayloadQueryhelpResponse</a></code>
- <code title="get /udl/seradataopticalpayload/tuple">client.seradata_optical_payload.<a href="./src/unifieddatalibrary/resources/seradata_optical_payload.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/seradata_optical_payload_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/seradata_optical_payload_tuple_response.py">SeradataOpticalPayloadTupleResponse</a></code>

# SeradataRadarPayload

Types:

```python
from unifieddatalibrary.types import (
    SeradataRadarPayloadListResponse,
    SeradataRadarPayloadCountResponse,
    SeradataRadarPayloadGetResponse,
    SeradataRadarPayloadQueryhelpResponse,
    SeradataRadarPayloadTupleResponse,
)
```

Methods:

- <code title="post /udl/seradataradarpayload">client.seradata_radar_payload.<a href="./src/unifieddatalibrary/resources/seradata_radar_payload.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/seradata_radar_payload_create_params.py">params</a>) -> None</code>
- <code title="put /udl/seradataradarpayload/{id}">client.seradata_radar_payload.<a href="./src/unifieddatalibrary/resources/seradata_radar_payload.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/seradata_radar_payload_update_params.py">params</a>) -> None</code>
- <code title="get /udl/seradataradarpayload">client.seradata_radar_payload.<a href="./src/unifieddatalibrary/resources/seradata_radar_payload.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/seradata_radar_payload_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/seradata_radar_payload_list_response.py">SyncOffsetPage[SeradataRadarPayloadListResponse]</a></code>
- <code title="delete /udl/seradataradarpayload/{id}">client.seradata_radar_payload.<a href="./src/unifieddatalibrary/resources/seradata_radar_payload.py">delete</a>(id) -> None</code>
- <code title="get /udl/seradataradarpayload/count">client.seradata_radar_payload.<a href="./src/unifieddatalibrary/resources/seradata_radar_payload.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/seradata_radar_payload_count_params.py">params</a>) -> str</code>
- <code title="get /udl/seradataradarpayload/{id}">client.seradata_radar_payload.<a href="./src/unifieddatalibrary/resources/seradata_radar_payload.py">get</a>(id, \*\*<a href="src/unifieddatalibrary/types/seradata_radar_payload_get_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/seradata_radar_payload_get_response.py">SeradataRadarPayloadGetResponse</a></code>
- <code title="get /udl/seradataradarpayload/queryhelp">client.seradata_radar_payload.<a href="./src/unifieddatalibrary/resources/seradata_radar_payload.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/seradata_radar_payload_queryhelp_response.py">SeradataRadarPayloadQueryhelpResponse</a></code>
- <code title="get /udl/seradataradarpayload/tuple">client.seradata_radar_payload.<a href="./src/unifieddatalibrary/resources/seradata_radar_payload.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/seradata_radar_payload_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/seradata_radar_payload_tuple_response.py">SeradataRadarPayloadTupleResponse</a></code>

# SeradataSigintPayload

Types:

```python
from unifieddatalibrary.types import (
    SeradataSigintPayloadListResponse,
    SeradataSigintPayloadCountResponse,
    SeradataSigintPayloadGetResponse,
    SeradataSigintPayloadQueryhelpResponse,
    SeradataSigintPayloadTupleResponse,
)
```

Methods:

- <code title="post /udl/seradatasigintpayload">client.seradata_sigint_payload.<a href="./src/unifieddatalibrary/resources/seradata_sigint_payload.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/seradata_sigint_payload_create_params.py">params</a>) -> None</code>
- <code title="put /udl/seradatasigintpayload/{id}">client.seradata_sigint_payload.<a href="./src/unifieddatalibrary/resources/seradata_sigint_payload.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/seradata_sigint_payload_update_params.py">params</a>) -> None</code>
- <code title="get /udl/seradatasigintpayload">client.seradata_sigint_payload.<a href="./src/unifieddatalibrary/resources/seradata_sigint_payload.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/seradata_sigint_payload_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/seradata_sigint_payload_list_response.py">SyncOffsetPage[SeradataSigintPayloadListResponse]</a></code>
- <code title="delete /udl/seradatasigintpayload/{id}">client.seradata_sigint_payload.<a href="./src/unifieddatalibrary/resources/seradata_sigint_payload.py">delete</a>(id) -> None</code>
- <code title="get /udl/seradatasigintpayload/count">client.seradata_sigint_payload.<a href="./src/unifieddatalibrary/resources/seradata_sigint_payload.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/seradata_sigint_payload_count_params.py">params</a>) -> str</code>
- <code title="get /udl/seradatasigintpayload/{id}">client.seradata_sigint_payload.<a href="./src/unifieddatalibrary/resources/seradata_sigint_payload.py">get</a>(id, \*\*<a href="src/unifieddatalibrary/types/seradata_sigint_payload_get_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/seradata_sigint_payload_get_response.py">SeradataSigintPayloadGetResponse</a></code>
- <code title="get /udl/seradatasigintpayload/queryhelp">client.seradata_sigint_payload.<a href="./src/unifieddatalibrary/resources/seradata_sigint_payload.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/seradata_sigint_payload_queryhelp_response.py">SeradataSigintPayloadQueryhelpResponse</a></code>
- <code title="get /udl/seradatasigintpayload/tuple">client.seradata_sigint_payload.<a href="./src/unifieddatalibrary/resources/seradata_sigint_payload.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/seradata_sigint_payload_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/seradata_sigint_payload_tuple_response.py">SeradataSigintPayloadTupleResponse</a></code>

# SeradataSpacecraftDetails

Types:

```python
from unifieddatalibrary.types import (
    SeradataSpacecraftDetailListResponse,
    SeradataSpacecraftDetailCountResponse,
    SeradataSpacecraftDetailGetResponse,
    SeradataSpacecraftDetailQueryhelpResponse,
    SeradataSpacecraftDetailTupleResponse,
)
```

Methods:

- <code title="post /udl/seradataspacecraftdetails">client.seradata_spacecraft_details.<a href="./src/unifieddatalibrary/resources/seradata_spacecraft_details.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/seradata_spacecraft_detail_create_params.py">params</a>) -> None</code>
- <code title="put /udl/seradataspacecraftdetails/{id}">client.seradata_spacecraft_details.<a href="./src/unifieddatalibrary/resources/seradata_spacecraft_details.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/seradata_spacecraft_detail_update_params.py">params</a>) -> None</code>
- <code title="get /udl/seradataspacecraftdetails">client.seradata_spacecraft_details.<a href="./src/unifieddatalibrary/resources/seradata_spacecraft_details.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/seradata_spacecraft_detail_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/seradata_spacecraft_detail_list_response.py">SyncOffsetPage[SeradataSpacecraftDetailListResponse]</a></code>
- <code title="delete /udl/seradataspacecraftdetails/{id}">client.seradata_spacecraft_details.<a href="./src/unifieddatalibrary/resources/seradata_spacecraft_details.py">delete</a>(id) -> None</code>
- <code title="get /udl/seradataspacecraftdetails/count">client.seradata_spacecraft_details.<a href="./src/unifieddatalibrary/resources/seradata_spacecraft_details.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/seradata_spacecraft_detail_count_params.py">params</a>) -> str</code>
- <code title="get /udl/seradataspacecraftdetails/{id}">client.seradata_spacecraft_details.<a href="./src/unifieddatalibrary/resources/seradata_spacecraft_details.py">get</a>(id, \*\*<a href="src/unifieddatalibrary/types/seradata_spacecraft_detail_get_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/seradata_spacecraft_detail_get_response.py">SeradataSpacecraftDetailGetResponse</a></code>
- <code title="get /udl/seradataspacecraftdetails/queryhelp">client.seradata_spacecraft_details.<a href="./src/unifieddatalibrary/resources/seradata_spacecraft_details.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/seradata_spacecraft_detail_queryhelp_response.py">SeradataSpacecraftDetailQueryhelpResponse</a></code>
- <code title="get /udl/seradataspacecraftdetails/tuple">client.seradata_spacecraft_details.<a href="./src/unifieddatalibrary/resources/seradata_spacecraft_details.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/seradata_spacecraft_detail_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/seradata_spacecraft_detail_tuple_response.py">SeradataSpacecraftDetailTupleResponse</a></code>

# Sgi

Types:

```python
from unifieddatalibrary.types import (
    SgiListResponse,
    SgiCountResponse,
    SgiGetResponse,
    SgiGetDataByEffectiveAsOfDateResponse,
    SgiQueryhelpResponse,
    SgiTupleResponse,
)
```

Methods:

- <code title="post /udl/sgi">client.sgi.<a href="./src/unifieddatalibrary/resources/sgi/sgi.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/sgi_create_params.py">params</a>) -> None</code>
- <code title="put /udl/sgi/{id}">client.sgi.<a href="./src/unifieddatalibrary/resources/sgi/sgi.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/sgi_update_params.py">params</a>) -> None</code>
- <code title="get /udl/sgi">client.sgi.<a href="./src/unifieddatalibrary/resources/sgi/sgi.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/sgi_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/sgi_list_response.py">SyncOffsetPage[SgiListResponse]</a></code>
- <code title="delete /udl/sgi/{id}">client.sgi.<a href="./src/unifieddatalibrary/resources/sgi/sgi.py">delete</a>(id) -> None</code>
- <code title="get /udl/sgi/count">client.sgi.<a href="./src/unifieddatalibrary/resources/sgi/sgi.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/sgi_count_params.py">params</a>) -> str</code>
- <code title="post /udl/sgi/createBulk">client.sgi.<a href="./src/unifieddatalibrary/resources/sgi/sgi.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/sgi_create_bulk_params.py">params</a>) -> None</code>
- <code title="get /udl/sgi/{id}">client.sgi.<a href="./src/unifieddatalibrary/resources/sgi/sgi.py">get</a>(id, \*\*<a href="src/unifieddatalibrary/types/sgi_get_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/sgi_get_response.py">SgiGetResponse</a></code>
- <code title="get /udl/sgi/getSGIDataByEffectiveAsOfDate">client.sgi.<a href="./src/unifieddatalibrary/resources/sgi/sgi.py">get_data_by_effective_as_of_date</a>(\*\*<a href="src/unifieddatalibrary/types/sgi_get_data_by_effective_as_of_date_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/sgi_get_data_by_effective_as_of_date_response.py">SgiGetDataByEffectiveAsOfDateResponse</a></code>
- <code title="get /udl/sgi/queryhelp">client.sgi.<a href="./src/unifieddatalibrary/resources/sgi/sgi.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/sgi_queryhelp_response.py">SgiQueryhelpResponse</a></code>
- <code title="get /udl/sgi/tuple">client.sgi.<a href="./src/unifieddatalibrary/resources/sgi/sgi.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/sgi_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/sgi_tuple_response.py">SgiTupleResponse</a></code>
- <code title="post /filedrop/udl-sgi">client.sgi.<a href="./src/unifieddatalibrary/resources/sgi/sgi.py">unvalidated_publish</a>(\*\*<a href="src/unifieddatalibrary/types/sgi_unvalidated_publish_params.py">params</a>) -> None</code>

## History

Types:

```python
from unifieddatalibrary.types.sgi import HistoryListResponse, HistoryCountResponse
```

Methods:

- <code title="get /udl/sgi/history">client.sgi.history.<a href="./src/unifieddatalibrary/resources/sgi/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/sgi/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/sgi/history_list_response.py">SyncOffsetPage[HistoryListResponse]</a></code>
- <code title="get /udl/sgi/history/aodr">client.sgi.history.<a href="./src/unifieddatalibrary/resources/sgi/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/sgi/history_aodr_params.py">params</a>) -> None</code>
- <code title="get /udl/sgi/history/count">client.sgi.history.<a href="./src/unifieddatalibrary/resources/sgi/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/sgi/history_count_params.py">params</a>) -> str</code>

# Sigact

Types:

```python
from unifieddatalibrary.types import (
    SigactListResponse,
    SigactCountResponse,
    SigactQueryhelpResponse,
    SigactTupleResponse,
)
```

Methods:

- <code title="get /udl/sigact">client.sigact.<a href="./src/unifieddatalibrary/resources/sigact/sigact.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/sigact_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/sigact_list_response.py">SyncOffsetPage[SigactListResponse]</a></code>
- <code title="get /udl/sigact/count">client.sigact.<a href="./src/unifieddatalibrary/resources/sigact/sigact.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/sigact_count_params.py">params</a>) -> str</code>
- <code title="post /udl/sigact/createBulk">client.sigact.<a href="./src/unifieddatalibrary/resources/sigact/sigact.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/sigact_create_bulk_params.py">params</a>) -> None</code>
- <code title="get /udl/sigact/queryhelp">client.sigact.<a href="./src/unifieddatalibrary/resources/sigact/sigact.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/sigact_queryhelp_response.py">SigactQueryhelpResponse</a></code>
- <code title="get /udl/sigact/tuple">client.sigact.<a href="./src/unifieddatalibrary/resources/sigact/sigact.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/sigact_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/sigact_tuple_response.py">SigactTupleResponse</a></code>
- <code title="post /filedrop/udl-sigact-text">client.sigact.<a href="./src/unifieddatalibrary/resources/sigact/sigact.py">upload_zip</a>(\*\*<a href="src/unifieddatalibrary/types/sigact_upload_zip_params.py">params</a>) -> None</code>

## History

Types:

```python
from unifieddatalibrary.types.sigact import HistoryListResponse, HistoryCountResponse
```

Methods:

- <code title="get /udl/sigact/history">client.sigact.history.<a href="./src/unifieddatalibrary/resources/sigact/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/sigact/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/sigact/history_list_response.py">SyncOffsetPage[HistoryListResponse]</a></code>
- <code title="get /udl/sigact/history/count">client.sigact.history.<a href="./src/unifieddatalibrary/resources/sigact/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/sigact/history_count_params.py">params</a>) -> str</code>

# Site

Types:

```python
from unifieddatalibrary.types import (
    SiteListResponse,
    SiteCountResponse,
    SiteGetResponse,
    SiteQueryhelpResponse,
    SiteTupleResponse,
)
```

Methods:

- <code title="post /udl/site">client.site.<a href="./src/unifieddatalibrary/resources/site/site.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/site_create_params.py">params</a>) -> None</code>
- <code title="put /udl/site/{id}">client.site.<a href="./src/unifieddatalibrary/resources/site/site.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/site_update_params.py">params</a>) -> None</code>
- <code title="get /udl/site">client.site.<a href="./src/unifieddatalibrary/resources/site/site.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/site_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/site_list_response.py">SyncOffsetPage[SiteListResponse]</a></code>
- <code title="get /udl/site/count">client.site.<a href="./src/unifieddatalibrary/resources/site/site.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/site_count_params.py">params</a>) -> str</code>
- <code title="get /udl/site/{id}">client.site.<a href="./src/unifieddatalibrary/resources/site/site.py">get</a>(id, \*\*<a href="src/unifieddatalibrary/types/site_get_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/site_get_response.py">SiteGetResponse</a></code>
- <code title="get /udl/site/queryhelp">client.site.<a href="./src/unifieddatalibrary/resources/site/site.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/site_queryhelp_response.py">SiteQueryhelpResponse</a></code>
- <code title="get /udl/site/tuple">client.site.<a href="./src/unifieddatalibrary/resources/site/site.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/site_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/site_tuple_response.py">SiteTupleResponse</a></code>

## Operations

Types:

```python
from unifieddatalibrary.types.site import (
    OperationRetrieveResponse,
    OperationListResponse,
    OperationCountResponse,
    OperationQueryHelpResponse,
    OperationTupleResponse,
)
```

Methods:

- <code title="post /udl/siteoperations">client.site.operations.<a href="./src/unifieddatalibrary/resources/site/operations.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/site/operation_create_params.py">params</a>) -> None</code>
- <code title="get /udl/siteoperations/{id}">client.site.operations.<a href="./src/unifieddatalibrary/resources/site/operations.py">retrieve</a>(id, \*\*<a href="src/unifieddatalibrary/types/site/operation_retrieve_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/site/operation_retrieve_response.py">OperationRetrieveResponse</a></code>
- <code title="put /udl/siteoperations/{id}">client.site.operations.<a href="./src/unifieddatalibrary/resources/site/operations.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/site/operation_update_params.py">params</a>) -> None</code>
- <code title="get /udl/siteoperations">client.site.operations.<a href="./src/unifieddatalibrary/resources/site/operations.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/site/operation_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/site/operation_list_response.py">SyncOffsetPage[OperationListResponse]</a></code>
- <code title="delete /udl/siteoperations/{id}">client.site.operations.<a href="./src/unifieddatalibrary/resources/site/operations.py">delete</a>(id) -> None</code>
- <code title="get /udl/siteoperations/count">client.site.operations.<a href="./src/unifieddatalibrary/resources/site/operations.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/site/operation_count_params.py">params</a>) -> str</code>
- <code title="post /udl/siteoperations/createBulk">client.site.operations.<a href="./src/unifieddatalibrary/resources/site/operations.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/site/operation_create_bulk_params.py">params</a>) -> None</code>
- <code title="get /udl/siteoperations/queryhelp">client.site.operations.<a href="./src/unifieddatalibrary/resources/site/operations.py">query_help</a>() -> <a href="./src/unifieddatalibrary/types/site/operation_query_help_response.py">OperationQueryHelpResponse</a></code>
- <code title="get /udl/siteoperations/tuple">client.site.operations.<a href="./src/unifieddatalibrary/resources/site/operations.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/site/operation_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/site/operation_tuple_response.py">OperationTupleResponse</a></code>
- <code title="post /filedrop/udl-siteoperations">client.site.operations.<a href="./src/unifieddatalibrary/resources/site/operations.py">unvalidated_publish</a>(\*\*<a href="src/unifieddatalibrary/types/site/operation_unvalidated_publish_params.py">params</a>) -> None</code>

# SiteRemark

Types:

```python
from unifieddatalibrary.types import (
    SiteRemarkListResponse,
    SiteRemarkCountResponse,
    SiteRemarkGetResponse,
    SiteRemarkQueryhelpResponse,
    SiteRemarkTupleResponse,
)
```

Methods:

- <code title="post /udl/siteremark">client.site_remark.<a href="./src/unifieddatalibrary/resources/site_remark.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/site_remark_create_params.py">params</a>) -> None</code>
- <code title="get /udl/siteremark">client.site_remark.<a href="./src/unifieddatalibrary/resources/site_remark.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/site_remark_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/site_remark_list_response.py">SyncOffsetPage[SiteRemarkListResponse]</a></code>
- <code title="get /udl/siteremark/count">client.site_remark.<a href="./src/unifieddatalibrary/resources/site_remark.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/site_remark_count_params.py">params</a>) -> str</code>
- <code title="get /udl/siteremark/{id}">client.site_remark.<a href="./src/unifieddatalibrary/resources/site_remark.py">get</a>(id, \*\*<a href="src/unifieddatalibrary/types/site_remark_get_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/site_remark_get_response.py">SiteRemarkGetResponse</a></code>
- <code title="get /udl/siteremark/queryhelp">client.site_remark.<a href="./src/unifieddatalibrary/resources/site_remark.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/site_remark_queryhelp_response.py">SiteRemarkQueryhelpResponse</a></code>
- <code title="get /udl/siteremark/tuple">client.site_remark.<a href="./src/unifieddatalibrary/resources/site_remark.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/site_remark_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/site_remark_tuple_response.py">SiteRemarkTupleResponse</a></code>

# SiteStatus

Types:

```python
from unifieddatalibrary.types import (
    SiteStatusListResponse,
    SiteStatusCountResponse,
    SiteStatusGetResponse,
    SiteStatusQueryhelpResponse,
    SiteStatusTupleResponse,
)
```

Methods:

- <code title="post /udl/sitestatus">client.site_status.<a href="./src/unifieddatalibrary/resources/site_status/site_status.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/site_status_create_params.py">params</a>) -> None</code>
- <code title="put /udl/sitestatus/{id}">client.site_status.<a href="./src/unifieddatalibrary/resources/site_status/site_status.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/site_status_update_params.py">params</a>) -> None</code>
- <code title="get /udl/sitestatus">client.site_status.<a href="./src/unifieddatalibrary/resources/site_status/site_status.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/site_status_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/site_status_list_response.py">SyncOffsetPage[SiteStatusListResponse]</a></code>
- <code title="delete /udl/sitestatus/{id}">client.site_status.<a href="./src/unifieddatalibrary/resources/site_status/site_status.py">delete</a>(id) -> None</code>
- <code title="get /udl/sitestatus/count">client.site_status.<a href="./src/unifieddatalibrary/resources/site_status/site_status.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/site_status_count_params.py">params</a>) -> str</code>
- <code title="get /udl/sitestatus/{id}">client.site_status.<a href="./src/unifieddatalibrary/resources/site_status/site_status.py">get</a>(id, \*\*<a href="src/unifieddatalibrary/types/site_status_get_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/site_status_get_response.py">SiteStatusGetResponse</a></code>
- <code title="get /udl/sitestatus/queryhelp">client.site_status.<a href="./src/unifieddatalibrary/resources/site_status/site_status.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/site_status_queryhelp_response.py">SiteStatusQueryhelpResponse</a></code>
- <code title="get /udl/sitestatus/tuple">client.site_status.<a href="./src/unifieddatalibrary/resources/site_status/site_status.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/site_status_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/site_status_tuple_response.py">SiteStatusTupleResponse</a></code>

## History

Types:

```python
from unifieddatalibrary.types.site_status import HistoryListResponse, HistoryCountResponse
```

Methods:

- <code title="get /udl/sitestatus/history">client.site_status.history.<a href="./src/unifieddatalibrary/resources/site_status/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/site_status/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/site_status/history_list_response.py">SyncOffsetPage[HistoryListResponse]</a></code>
- <code title="get /udl/sitestatus/history/count">client.site_status.history.<a href="./src/unifieddatalibrary/resources/site_status/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/site_status/history_count_params.py">params</a>) -> str</code>

# SkyImagery

Types:

```python
from unifieddatalibrary.types import (
    SkyImageryListResponse,
    SkyImageryCountResponse,
    SkyImageryGetResponse,
    SkyImageryQueryhelpResponse,
    SkyImageryTupleResponse,
)
```

Methods:

- <code title="get /udl/skyimagery">client.sky_imagery.<a href="./src/unifieddatalibrary/resources/sky_imagery/sky_imagery.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/sky_imagery_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/sky_imagery_list_response.py">SyncOffsetPage[SkyImageryListResponse]</a></code>
- <code title="get /udl/skyimagery/count">client.sky_imagery.<a href="./src/unifieddatalibrary/resources/sky_imagery/sky_imagery.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/sky_imagery_count_params.py">params</a>) -> str</code>
- <code title="get /udl/skyimagery/getFile/{id}">client.sky_imagery.<a href="./src/unifieddatalibrary/resources/sky_imagery/sky_imagery.py">file_get</a>(id, \*\*<a href="src/unifieddatalibrary/types/sky_imagery_file_get_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="get /udl/skyimagery/{id}">client.sky_imagery.<a href="./src/unifieddatalibrary/resources/sky_imagery/sky_imagery.py">get</a>(id, \*\*<a href="src/unifieddatalibrary/types/sky_imagery_get_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/sky_imagery_get_response.py">SkyImageryGetResponse</a></code>
- <code title="get /udl/skyimagery/queryhelp">client.sky_imagery.<a href="./src/unifieddatalibrary/resources/sky_imagery/sky_imagery.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/sky_imagery_queryhelp_response.py">SkyImageryQueryhelpResponse</a></code>
- <code title="get /udl/skyimagery/tuple">client.sky_imagery.<a href="./src/unifieddatalibrary/resources/sky_imagery/sky_imagery.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/sky_imagery_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/sky_imagery_tuple_response.py">SkyImageryTupleResponse</a></code>
- <code title="post /filedrop/udl-skyimagery">client.sky_imagery.<a href="./src/unifieddatalibrary/resources/sky_imagery/sky_imagery.py">upload_zip</a>(\*\*<a href="src/unifieddatalibrary/types/sky_imagery_upload_zip_params.py">params</a>) -> None</code>

## History

Types:

```python
from unifieddatalibrary.types.sky_imagery import HistoryListResponse, HistoryCountResponse
```

Methods:

- <code title="get /udl/skyimagery/history">client.sky_imagery.history.<a href="./src/unifieddatalibrary/resources/sky_imagery/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/sky_imagery/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/sky_imagery/history_list_response.py">SyncOffsetPage[HistoryListResponse]</a></code>
- <code title="get /udl/skyimagery/history/aodr">client.sky_imagery.history.<a href="./src/unifieddatalibrary/resources/sky_imagery/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/sky_imagery/history_aodr_params.py">params</a>) -> None</code>
- <code title="get /udl/skyimagery/history/count">client.sky_imagery.history.<a href="./src/unifieddatalibrary/resources/sky_imagery/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/sky_imagery/history_count_params.py">params</a>) -> str</code>

# SoiObservationSet

Types:

```python
from unifieddatalibrary.types import (
    SoiObservationSetListResponse,
    SoiObservationSetCountResponse,
    SoiObservationSetQueryhelpResponse,
    SoiObservationSetTupleResponse,
)
```

Methods:

- <code title="post /udl/soiobservationset">client.soi_observation_set.<a href="./src/unifieddatalibrary/resources/soi_observation_set/soi_observation_set.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/soi_observation_set_create_params.py">params</a>) -> None</code>
- <code title="get /udl/soiobservationset">client.soi_observation_set.<a href="./src/unifieddatalibrary/resources/soi_observation_set/soi_observation_set.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/soi_observation_set_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/soi_observation_set_list_response.py">SyncOffsetPage[SoiObservationSetListResponse]</a></code>
- <code title="get /udl/soiobservationset/count">client.soi_observation_set.<a href="./src/unifieddatalibrary/resources/soi_observation_set/soi_observation_set.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/soi_observation_set_count_params.py">params</a>) -> str</code>
- <code title="post /udl/soiobservationset/createBulk">client.soi_observation_set.<a href="./src/unifieddatalibrary/resources/soi_observation_set/soi_observation_set.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/soi_observation_set_create_bulk_params.py">params</a>) -> None</code>
- <code title="get /udl/soiobservationset/{id}">client.soi_observation_set.<a href="./src/unifieddatalibrary/resources/soi_observation_set/soi_observation_set.py">get</a>(id, \*\*<a href="src/unifieddatalibrary/types/soi_observation_set_get_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/soi_observation_set/soi_observation_set_full.py">SoiObservationSetFull</a></code>
- <code title="get /udl/soiobservationset/queryhelp">client.soi_observation_set.<a href="./src/unifieddatalibrary/resources/soi_observation_set/soi_observation_set.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/soi_observation_set_queryhelp_response.py">SoiObservationSetQueryhelpResponse</a></code>
- <code title="get /udl/soiobservationset/tuple">client.soi_observation_set.<a href="./src/unifieddatalibrary/resources/soi_observation_set/soi_observation_set.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/soi_observation_set_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/soi_observation_set_tuple_response.py">SoiObservationSetTupleResponse</a></code>
- <code title="post /filedrop/udl-soiobservationset">client.soi_observation_set.<a href="./src/unifieddatalibrary/resources/soi_observation_set/soi_observation_set.py">unvalidated_publish</a>(\*\*<a href="src/unifieddatalibrary/types/soi_observation_set_unvalidated_publish_params.py">params</a>) -> None</code>

## History

Types:

```python
from unifieddatalibrary.types.soi_observation_set import SoiObservationSetFull, HistoryCountResponse
```

Methods:

- <code title="get /udl/soiobservationset/history">client.soi_observation_set.history.<a href="./src/unifieddatalibrary/resources/soi_observation_set/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/soi_observation_set/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/soi_observation_set/soi_observation_set_full.py">SyncOffsetPage[SoiObservationSetFull]</a></code>
- <code title="get /udl/soiobservationset/history/aodr">client.soi_observation_set.history.<a href="./src/unifieddatalibrary/resources/soi_observation_set/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/soi_observation_set/history_aodr_params.py">params</a>) -> None</code>
- <code title="get /udl/soiobservationset/history/count">client.soi_observation_set.history.<a href="./src/unifieddatalibrary/resources/soi_observation_set/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/soi_observation_set/history_count_params.py">params</a>) -> str</code>

# SolarArray

Types:

```python
from unifieddatalibrary.types import (
    SolarArrayListResponse,
    SolarArrayCountResponse,
    SolarArrayQueryhelpResponse,
    SolarArrayTupleResponse,
)
```

Methods:

- <code title="post /udl/solararray">client.solar_array.<a href="./src/unifieddatalibrary/resources/solar_array.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/solar_array_create_params.py">params</a>) -> None</code>
- <code title="put /udl/solararray/{id}">client.solar_array.<a href="./src/unifieddatalibrary/resources/solar_array.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/solar_array_update_params.py">params</a>) -> None</code>
- <code title="get /udl/solararray">client.solar_array.<a href="./src/unifieddatalibrary/resources/solar_array.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/solar_array_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/solar_array_list_response.py">SyncOffsetPage[SolarArrayListResponse]</a></code>
- <code title="delete /udl/solararray/{id}">client.solar_array.<a href="./src/unifieddatalibrary/resources/solar_array.py">delete</a>(id) -> None</code>
- <code title="get /udl/solararray/count">client.solar_array.<a href="./src/unifieddatalibrary/resources/solar_array.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/solar_array_count_params.py">params</a>) -> str</code>
- <code title="get /udl/solararray/{id}">client.solar_array.<a href="./src/unifieddatalibrary/resources/solar_array.py">get</a>(id, \*\*<a href="src/unifieddatalibrary/types/solar_array_get_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/shared/solar_array_full.py">SolarArrayFull</a></code>
- <code title="get /udl/solararray/queryhelp">client.solar_array.<a href="./src/unifieddatalibrary/resources/solar_array.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/solar_array_queryhelp_response.py">SolarArrayQueryhelpResponse</a></code>
- <code title="get /udl/solararray/tuple">client.solar_array.<a href="./src/unifieddatalibrary/resources/solar_array.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/solar_array_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/solar_array_tuple_response.py">SolarArrayTupleResponse</a></code>

# SolarArrayDetails

Types:

```python
from unifieddatalibrary.types import SolarArrayDetailListResponse
```

Methods:

- <code title="post /udl/solararraydetails">client.solar_array_details.<a href="./src/unifieddatalibrary/resources/solar_array_details.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/solar_array_detail_create_params.py">params</a>) -> None</code>
- <code title="put /udl/solararraydetails/{id}">client.solar_array_details.<a href="./src/unifieddatalibrary/resources/solar_array_details.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/solar_array_detail_update_params.py">params</a>) -> None</code>
- <code title="get /udl/solararraydetails">client.solar_array_details.<a href="./src/unifieddatalibrary/resources/solar_array_details.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/solar_array_detail_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/solar_array_detail_list_response.py">SyncOffsetPage[SolarArrayDetailListResponse]</a></code>
- <code title="delete /udl/solararraydetails/{id}">client.solar_array_details.<a href="./src/unifieddatalibrary/resources/solar_array_details.py">delete</a>(id) -> None</code>
- <code title="get /udl/solararraydetails/{id}">client.solar_array_details.<a href="./src/unifieddatalibrary/resources/solar_array_details.py">get</a>(id, \*\*<a href="src/unifieddatalibrary/types/solar_array_detail_get_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/shared/solar_array_details_full.py">SolarArrayDetailsFull</a></code>

# SortiePpr

Types:

```python
from unifieddatalibrary.types import (
    SortiePprListResponse,
    SortiePprCountResponse,
    SortiePprQueryhelpResponse,
    SortiePprTupleResponse,
)
```

Methods:

- <code title="post /udl/sortieppr">client.sortie_ppr.<a href="./src/unifieddatalibrary/resources/sortie_ppr/sortie_ppr.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/sortie_ppr_create_params.py">params</a>) -> None</code>
- <code title="put /udl/sortieppr/{id}">client.sortie_ppr.<a href="./src/unifieddatalibrary/resources/sortie_ppr/sortie_ppr.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/sortie_ppr_update_params.py">params</a>) -> None</code>
- <code title="get /udl/sortieppr">client.sortie_ppr.<a href="./src/unifieddatalibrary/resources/sortie_ppr/sortie_ppr.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/sortie_ppr_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/sortie_ppr_list_response.py">SyncOffsetPage[SortiePprListResponse]</a></code>
- <code title="delete /udl/sortieppr/{id}">client.sortie_ppr.<a href="./src/unifieddatalibrary/resources/sortie_ppr/sortie_ppr.py">delete</a>(id) -> None</code>
- <code title="get /udl/sortieppr/count">client.sortie_ppr.<a href="./src/unifieddatalibrary/resources/sortie_ppr/sortie_ppr.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/sortie_ppr_count_params.py">params</a>) -> str</code>
- <code title="post /udl/sortieppr/createBulk">client.sortie_ppr.<a href="./src/unifieddatalibrary/resources/sortie_ppr/sortie_ppr.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/sortie_ppr_create_bulk_params.py">params</a>) -> None</code>
- <code title="get /udl/sortieppr/{id}">client.sortie_ppr.<a href="./src/unifieddatalibrary/resources/sortie_ppr/sortie_ppr.py">get</a>(id, \*\*<a href="src/unifieddatalibrary/types/sortie_ppr_get_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/shared/sortie_ppr_full.py">SortiePprFull</a></code>
- <code title="get /udl/sortieppr/queryhelp">client.sortie_ppr.<a href="./src/unifieddatalibrary/resources/sortie_ppr/sortie_ppr.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/sortie_ppr_queryhelp_response.py">SortiePprQueryhelpResponse</a></code>
- <code title="get /udl/sortieppr/tuple">client.sortie_ppr.<a href="./src/unifieddatalibrary/resources/sortie_ppr/sortie_ppr.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/sortie_ppr_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/sortie_ppr_tuple_response.py">SortiePprTupleResponse</a></code>
- <code title="post /filedrop/udl-sortieppr">client.sortie_ppr.<a href="./src/unifieddatalibrary/resources/sortie_ppr/sortie_ppr.py">unvalidated_publish</a>(\*\*<a href="src/unifieddatalibrary/types/sortie_ppr_unvalidated_publish_params.py">params</a>) -> None</code>

## History

Types:

```python
from unifieddatalibrary.types.sortie_ppr import HistoryCountResponse
```

Methods:

- <code title="get /udl/sortieppr/history">client.sortie_ppr.history.<a href="./src/unifieddatalibrary/resources/sortie_ppr/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/sortie_ppr/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/shared/sortie_ppr_full.py">SyncOffsetPage[SortiePprFull]</a></code>
- <code title="get /udl/sortieppr/history/aodr">client.sortie_ppr.history.<a href="./src/unifieddatalibrary/resources/sortie_ppr/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/sortie_ppr/history_aodr_params.py">params</a>) -> None</code>
- <code title="get /udl/sortieppr/history/count">client.sortie_ppr.history.<a href="./src/unifieddatalibrary/resources/sortie_ppr/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/sortie_ppr/history_count_params.py">params</a>) -> str</code>

# SpaceEnvObservation

Types:

```python
from unifieddatalibrary.types import (
    SpaceEnvObservationListResponse,
    SpaceEnvObservationCountResponse,
    SpaceEnvObservationQueryhelpResponse,
    SpaceEnvObservationTupleResponse,
)
```

Methods:

- <code title="get /udl/spaceenvobservation">client.space_env_observation.<a href="./src/unifieddatalibrary/resources/space_env_observation/space_env_observation.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/space_env_observation_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/space_env_observation_list_response.py">SyncOffsetPage[SpaceEnvObservationListResponse]</a></code>
- <code title="get /udl/spaceenvobservation/count">client.space_env_observation.<a href="./src/unifieddatalibrary/resources/space_env_observation/space_env_observation.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/space_env_observation_count_params.py">params</a>) -> str</code>
- <code title="post /udl/spaceenvobservation/createBulk">client.space_env_observation.<a href="./src/unifieddatalibrary/resources/space_env_observation/space_env_observation.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/space_env_observation_create_bulk_params.py">params</a>) -> None</code>
- <code title="get /udl/spaceenvobservation/queryhelp">client.space_env_observation.<a href="./src/unifieddatalibrary/resources/space_env_observation/space_env_observation.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/space_env_observation_queryhelp_response.py">SpaceEnvObservationQueryhelpResponse</a></code>
- <code title="get /udl/spaceenvobservation/tuple">client.space_env_observation.<a href="./src/unifieddatalibrary/resources/space_env_observation/space_env_observation.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/space_env_observation_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/space_env_observation_tuple_response.py">SpaceEnvObservationTupleResponse</a></code>
- <code title="post /filedrop/udl-spaceenvobs">client.space_env_observation.<a href="./src/unifieddatalibrary/resources/space_env_observation/space_env_observation.py">unvalidated_publish</a>(\*\*<a href="src/unifieddatalibrary/types/space_env_observation_unvalidated_publish_params.py">params</a>) -> None</code>

## History

Types:

```python
from unifieddatalibrary.types.space_env_observation import (
    SpaceEnvObservationFull,
    HistoryCountResponse,
)
```

Methods:

- <code title="get /udl/spaceenvobservation/history">client.space_env_observation.history.<a href="./src/unifieddatalibrary/resources/space_env_observation/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/space_env_observation/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/space_env_observation/space_env_observation_full.py">SyncOffsetPage[SpaceEnvObservationFull]</a></code>
- <code title="get /udl/spaceenvobservation/history/aodr">client.space_env_observation.history.<a href="./src/unifieddatalibrary/resources/space_env_observation/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/space_env_observation/history_aodr_params.py">params</a>) -> None</code>
- <code title="get /udl/spaceenvobservation/history/count">client.space_env_observation.history.<a href="./src/unifieddatalibrary/resources/space_env_observation/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/space_env_observation/history_count_params.py">params</a>) -> str</code>

# Stage

Types:

```python
from unifieddatalibrary.types import (
    StageListResponse,
    StageCountResponse,
    StageGetResponse,
    StageQueryhelpResponse,
    StageTupleResponse,
)
```

Methods:

- <code title="post /udl/stage">client.stage.<a href="./src/unifieddatalibrary/resources/stage.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/stage_create_params.py">params</a>) -> None</code>
- <code title="put /udl/stage/{id}">client.stage.<a href="./src/unifieddatalibrary/resources/stage.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/stage_update_params.py">params</a>) -> None</code>
- <code title="get /udl/stage">client.stage.<a href="./src/unifieddatalibrary/resources/stage.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/stage_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/stage_list_response.py">SyncOffsetPage[StageListResponse]</a></code>
- <code title="delete /udl/stage/{id}">client.stage.<a href="./src/unifieddatalibrary/resources/stage.py">delete</a>(id) -> None</code>
- <code title="get /udl/stage/count">client.stage.<a href="./src/unifieddatalibrary/resources/stage.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/stage_count_params.py">params</a>) -> str</code>
- <code title="get /udl/stage/{id}">client.stage.<a href="./src/unifieddatalibrary/resources/stage.py">get</a>(id, \*\*<a href="src/unifieddatalibrary/types/stage_get_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/stage_get_response.py">StageGetResponse</a></code>
- <code title="get /udl/stage/queryhelp">client.stage.<a href="./src/unifieddatalibrary/resources/stage.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/stage_queryhelp_response.py">StageQueryhelpResponse</a></code>
- <code title="get /udl/stage/tuple">client.stage.<a href="./src/unifieddatalibrary/resources/stage.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/stage_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/stage_tuple_response.py">StageTupleResponse</a></code>

# StarCatalog

Types:

```python
from unifieddatalibrary.types import (
    StarCatalogListResponse,
    StarCatalogCountResponse,
    StarCatalogGetResponse,
    StarCatalogQueryhelpResponse,
    StarCatalogTupleResponse,
)
```

Methods:

- <code title="post /udl/starcatalog">client.star_catalog.<a href="./src/unifieddatalibrary/resources/star_catalog/star_catalog.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/star_catalog_create_params.py">params</a>) -> None</code>
- <code title="put /udl/starcatalog/{id}">client.star_catalog.<a href="./src/unifieddatalibrary/resources/star_catalog/star_catalog.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/star_catalog_update_params.py">params</a>) -> None</code>
- <code title="get /udl/starcatalog">client.star_catalog.<a href="./src/unifieddatalibrary/resources/star_catalog/star_catalog.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/star_catalog_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/star_catalog_list_response.py">SyncOffsetPage[StarCatalogListResponse]</a></code>
- <code title="delete /udl/starcatalog/{id}">client.star_catalog.<a href="./src/unifieddatalibrary/resources/star_catalog/star_catalog.py">delete</a>(id) -> None</code>
- <code title="get /udl/starcatalog/count">client.star_catalog.<a href="./src/unifieddatalibrary/resources/star_catalog/star_catalog.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/star_catalog_count_params.py">params</a>) -> str</code>
- <code title="post /udl/starcatalog/createBulk">client.star_catalog.<a href="./src/unifieddatalibrary/resources/star_catalog/star_catalog.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/star_catalog_create_bulk_params.py">params</a>) -> None</code>
- <code title="get /udl/starcatalog/{id}">client.star_catalog.<a href="./src/unifieddatalibrary/resources/star_catalog/star_catalog.py">get</a>(id, \*\*<a href="src/unifieddatalibrary/types/star_catalog_get_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/star_catalog_get_response.py">StarCatalogGetResponse</a></code>
- <code title="get /udl/starcatalog/queryhelp">client.star_catalog.<a href="./src/unifieddatalibrary/resources/star_catalog/star_catalog.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/star_catalog_queryhelp_response.py">StarCatalogQueryhelpResponse</a></code>
- <code title="get /udl/starcatalog/tuple">client.star_catalog.<a href="./src/unifieddatalibrary/resources/star_catalog/star_catalog.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/star_catalog_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/star_catalog_tuple_response.py">StarCatalogTupleResponse</a></code>
- <code title="post /filedrop/udl-starcatalog">client.star_catalog.<a href="./src/unifieddatalibrary/resources/star_catalog/star_catalog.py">unvalidated_publish</a>(\*\*<a href="src/unifieddatalibrary/types/star_catalog_unvalidated_publish_params.py">params</a>) -> None</code>

## History

Methods:

- <code title="get /udl/starcatalog/history/aodr">client.star_catalog.history.<a href="./src/unifieddatalibrary/resources/star_catalog/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/star_catalog/history_aodr_params.py">params</a>) -> None</code>

# StateVector

Types:

```python
from unifieddatalibrary.types import (
    StateVectorAbridged,
    StateVectorIngest,
    StateVectorCountResponse,
    StateVectorQueryhelpResponse,
    StateVectorTupleResponse,
)
```

Methods:

- <code title="post /udl/statevector">client.state_vector.<a href="./src/unifieddatalibrary/resources/state_vector/state_vector.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/state_vector_create_params.py">params</a>) -> None</code>
- <code title="get /udl/statevector">client.state_vector.<a href="./src/unifieddatalibrary/resources/state_vector/state_vector.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/state_vector_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/state_vector_abridged.py">SyncOffsetPage[StateVectorAbridged]</a></code>
- <code title="get /udl/statevector/count">client.state_vector.<a href="./src/unifieddatalibrary/resources/state_vector/state_vector.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/state_vector_count_params.py">params</a>) -> str</code>
- <code title="post /udl/statevector/createBulk">client.state_vector.<a href="./src/unifieddatalibrary/resources/state_vector/state_vector.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/state_vector_create_bulk_params.py">params</a>) -> None</code>
- <code title="get /udl/statevector/{id}">client.state_vector.<a href="./src/unifieddatalibrary/resources/state_vector/state_vector.py">get</a>(id, \*\*<a href="src/unifieddatalibrary/types/state_vector_get_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/shared/state_vector_full.py">StateVectorFull</a></code>
- <code title="get /udl/statevector/queryhelp">client.state_vector.<a href="./src/unifieddatalibrary/resources/state_vector/state_vector.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/state_vector_queryhelp_response.py">StateVectorQueryhelpResponse</a></code>
- <code title="get /udl/statevector/tuple">client.state_vector.<a href="./src/unifieddatalibrary/resources/state_vector/state_vector.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/state_vector_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/state_vector_tuple_response.py">StateVectorTupleResponse</a></code>
- <code title="post /filedrop/udl-sv">client.state_vector.<a href="./src/unifieddatalibrary/resources/state_vector/state_vector.py">unvalidated_publish</a>(\*\*<a href="src/unifieddatalibrary/types/state_vector_unvalidated_publish_params.py">params</a>) -> None</code>

## Current

Types:

```python
from unifieddatalibrary.types.state_vector import CurrentTupleResponse
```

Methods:

- <code title="get /udl/statevector/current">client.state_vector.current.<a href="./src/unifieddatalibrary/resources/state_vector/current.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/state_vector/current_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/state_vector_abridged.py">SyncOffsetPage[StateVectorAbridged]</a></code>
- <code title="get /udl/statevector/current/tuple">client.state_vector.current.<a href="./src/unifieddatalibrary/resources/state_vector/current.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/state_vector/current_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/state_vector/current_tuple_response.py">CurrentTupleResponse</a></code>

## History

Types:

```python
from unifieddatalibrary.types.state_vector import HistoryCountResponse
```

Methods:

- <code title="get /udl/statevector/history">client.state_vector.history.<a href="./src/unifieddatalibrary/resources/state_vector/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/state_vector/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/shared/state_vector_full.py">SyncOffsetPage[StateVectorFull]</a></code>
- <code title="get /udl/statevector/history/aodr">client.state_vector.history.<a href="./src/unifieddatalibrary/resources/state_vector/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/state_vector/history_aodr_params.py">params</a>) -> None</code>
- <code title="get /udl/statevector/history/count">client.state_vector.history.<a href="./src/unifieddatalibrary/resources/state_vector/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/state_vector/history_count_params.py">params</a>) -> str</code>

# Status

Types:

```python
from unifieddatalibrary.types import (
    StatusListResponse,
    StatusCountResponse,
    StatusGetByEntityIDResponse,
    StatusGetByEntityTypeResponse,
    StatusQueryhelpResponse,
    StatusTupleResponse,
)
```

Methods:

- <code title="post /udl/status">client.status.<a href="./src/unifieddatalibrary/resources/status.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/status_create_params.py">params</a>) -> None</code>
- <code title="put /udl/status/{id}">client.status.<a href="./src/unifieddatalibrary/resources/status.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/status_update_params.py">params</a>) -> None</code>
- <code title="get /udl/status">client.status.<a href="./src/unifieddatalibrary/resources/status.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/status_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/status_list_response.py">SyncOffsetPage[StatusListResponse]</a></code>
- <code title="delete /udl/status/{id}">client.status.<a href="./src/unifieddatalibrary/resources/status.py">delete</a>(id) -> None</code>
- <code title="get /udl/status/count">client.status.<a href="./src/unifieddatalibrary/resources/status.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/status_count_params.py">params</a>) -> str</code>
- <code title="get /udl/status/{id}">client.status.<a href="./src/unifieddatalibrary/resources/status.py">get</a>(id, \*\*<a href="src/unifieddatalibrary/types/status_get_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/shared/status_full.py">StatusFull</a></code>
- <code title="get /udl/status/byIdEntity/{idEntity}">client.status.<a href="./src/unifieddatalibrary/resources/status.py">get_by_entity_id</a>(id_entity, \*\*<a href="src/unifieddatalibrary/types/status_get_by_entity_id_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/status_get_by_entity_id_response.py">StatusGetByEntityIDResponse</a></code>
- <code title="get /udl/status/byEntityType/{entityType}">client.status.<a href="./src/unifieddatalibrary/resources/status.py">get_by_entity_type</a>(entity_type, \*\*<a href="src/unifieddatalibrary/types/status_get_by_entity_type_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/status_get_by_entity_type_response.py">StatusGetByEntityTypeResponse</a></code>
- <code title="get /udl/status/queryhelp">client.status.<a href="./src/unifieddatalibrary/resources/status.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/status_queryhelp_response.py">StatusQueryhelpResponse</a></code>
- <code title="get /udl/status/tuple">client.status.<a href="./src/unifieddatalibrary/resources/status.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/status_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/status_tuple_response.py">StatusTupleResponse</a></code>

# Substatus

Types:

```python
from unifieddatalibrary.types import (
    SubstatusListResponse,
    SubstatusCountResponse,
    SubstatusQueryhelpResponse,
    SubstatusTupleResponse,
)
```

Methods:

- <code title="post /udl/substatus">client.substatus.<a href="./src/unifieddatalibrary/resources/substatus.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/substatus_create_params.py">params</a>) -> None</code>
- <code title="put /udl/substatus/{id}">client.substatus.<a href="./src/unifieddatalibrary/resources/substatus.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/substatus_update_params.py">params</a>) -> None</code>
- <code title="get /udl/substatus">client.substatus.<a href="./src/unifieddatalibrary/resources/substatus.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/substatus_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/substatus_list_response.py">SyncOffsetPage[SubstatusListResponse]</a></code>
- <code title="delete /udl/substatus/{id}">client.substatus.<a href="./src/unifieddatalibrary/resources/substatus.py">delete</a>(id) -> None</code>
- <code title="get /udl/substatus/count">client.substatus.<a href="./src/unifieddatalibrary/resources/substatus.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/substatus_count_params.py">params</a>) -> str</code>
- <code title="get /udl/substatus/{id}">client.substatus.<a href="./src/unifieddatalibrary/resources/substatus.py">get</a>(id, \*\*<a href="src/unifieddatalibrary/types/substatus_get_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/shared/sub_status_full.py">SubStatusFull</a></code>
- <code title="get /udl/substatus/queryhelp">client.substatus.<a href="./src/unifieddatalibrary/resources/substatus.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/substatus_queryhelp_response.py">SubstatusQueryhelpResponse</a></code>
- <code title="get /udl/substatus/tuple">client.substatus.<a href="./src/unifieddatalibrary/resources/substatus.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/substatus_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/substatus_tuple_response.py">SubstatusTupleResponse</a></code>

# SupportingData

## DataTypes

Types:

```python
from unifieddatalibrary.types.supporting_data import DataTypeListResponse
```

Methods:

- <code title="get /udl/dataowner/getDataTypes">client.supporting_data.data_types.<a href="./src/unifieddatalibrary/resources/supporting_data/data_types.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/supporting_data/data_type_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/supporting_data/data_type_list_response.py">SyncOffsetPage[DataTypeListResponse]</a></code>

## Dataowner

Types:

```python
from unifieddatalibrary.types.supporting_data import (
    DataownerAbridged,
    DataownerRetrieveResponse,
    DataownerCountResponse,
    DataownerQueryHelpResponse,
    DataownerRetrieveDataOwnerTypesResponse,
    DataownerRetrieveProviderMetadataResponse,
)
```

Methods:

- <code title="get /udl/dataowner">client.supporting_data.dataowner.<a href="./src/unifieddatalibrary/resources/supporting_data/dataowner.py">retrieve</a>(\*\*<a href="src/unifieddatalibrary/types/supporting_data/dataowner_retrieve_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/supporting_data/dataowner_retrieve_response.py">DataownerRetrieveResponse</a></code>
- <code title="get /udl/dataowner/count">client.supporting_data.dataowner.<a href="./src/unifieddatalibrary/resources/supporting_data/dataowner.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/supporting_data/dataowner_count_params.py">params</a>) -> str</code>
- <code title="get /udl/dataowner/queryhelp">client.supporting_data.dataowner.<a href="./src/unifieddatalibrary/resources/supporting_data/dataowner.py">query_help</a>() -> <a href="./src/unifieddatalibrary/types/supporting_data/dataowner_query_help_response.py">DataownerQueryHelpResponse</a></code>
- <code title="get /udl/dataowner/getDataOwnerTypes">client.supporting_data.dataowner.<a href="./src/unifieddatalibrary/resources/supporting_data/dataowner.py">retrieve_data_owner_types</a>(\*\*<a href="src/unifieddatalibrary/types/supporting_data/dataowner_retrieve_data_owner_types_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/supporting_data/dataowner_retrieve_data_owner_types_response.py">DataownerRetrieveDataOwnerTypesResponse</a></code>
- <code title="get /udl/dataowner/providerMetadata">client.supporting_data.dataowner.<a href="./src/unifieddatalibrary/resources/supporting_data/dataowner.py">retrieve_provider_metadata</a>(\*\*<a href="src/unifieddatalibrary/types/supporting_data/dataowner_retrieve_provider_metadata_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/supporting_data/dataowner_retrieve_provider_metadata_response.py">DataownerRetrieveProviderMetadataResponse</a></code>

# Surface

Types:

```python
from unifieddatalibrary.types import (
    SurfaceListResponse,
    SurfaceCountResponse,
    SurfaceGetResponse,
    SurfaceQueryhelpResponse,
    SurfaceTupleResponse,
)
```

Methods:

- <code title="post /udl/surface">client.surface.<a href="./src/unifieddatalibrary/resources/surface.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/surface_create_params.py">params</a>) -> None</code>
- <code title="put /udl/surface/{id}">client.surface.<a href="./src/unifieddatalibrary/resources/surface.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/surface_update_params.py">params</a>) -> None</code>
- <code title="get /udl/surface">client.surface.<a href="./src/unifieddatalibrary/resources/surface.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/surface_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/surface_list_response.py">SyncOffsetPage[SurfaceListResponse]</a></code>
- <code title="delete /udl/surface/{id}">client.surface.<a href="./src/unifieddatalibrary/resources/surface.py">delete</a>(id) -> None</code>
- <code title="get /udl/surface/count">client.surface.<a href="./src/unifieddatalibrary/resources/surface.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/surface_count_params.py">params</a>) -> str</code>
- <code title="get /udl/surface/{id}">client.surface.<a href="./src/unifieddatalibrary/resources/surface.py">get</a>(id, \*\*<a href="src/unifieddatalibrary/types/surface_get_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/surface_get_response.py">SurfaceGetResponse</a></code>
- <code title="get /udl/surface/queryhelp">client.surface.<a href="./src/unifieddatalibrary/resources/surface.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/surface_queryhelp_response.py">SurfaceQueryhelpResponse</a></code>
- <code title="get /udl/surface/tuple">client.surface.<a href="./src/unifieddatalibrary/resources/surface.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/surface_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/surface_tuple_response.py">SurfaceTupleResponse</a></code>

# SurfaceObstruction

Types:

```python
from unifieddatalibrary.types import (
    SurfaceObstructionListResponse,
    SurfaceObstructionCountResponse,
    SurfaceObstructionGetResponse,
    SurfaceObstructionQueryhelpResponse,
    SurfaceObstructionTupleResponse,
)
```

Methods:

- <code title="post /udl/surfaceobstruction">client.surface_obstruction.<a href="./src/unifieddatalibrary/resources/surface_obstruction.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/surface_obstruction_create_params.py">params</a>) -> None</code>
- <code title="put /udl/surfaceobstruction/{id}">client.surface_obstruction.<a href="./src/unifieddatalibrary/resources/surface_obstruction.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/surface_obstruction_update_params.py">params</a>) -> None</code>
- <code title="get /udl/surfaceobstruction">client.surface_obstruction.<a href="./src/unifieddatalibrary/resources/surface_obstruction.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/surface_obstruction_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/surface_obstruction_list_response.py">SyncOffsetPage[SurfaceObstructionListResponse]</a></code>
- <code title="delete /udl/surfaceobstruction/{id}">client.surface_obstruction.<a href="./src/unifieddatalibrary/resources/surface_obstruction.py">delete</a>(id) -> None</code>
- <code title="get /udl/surfaceobstruction/count">client.surface_obstruction.<a href="./src/unifieddatalibrary/resources/surface_obstruction.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/surface_obstruction_count_params.py">params</a>) -> str</code>
- <code title="get /udl/surfaceobstruction/{id}">client.surface_obstruction.<a href="./src/unifieddatalibrary/resources/surface_obstruction.py">get</a>(id, \*\*<a href="src/unifieddatalibrary/types/surface_obstruction_get_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/surface_obstruction_get_response.py">SurfaceObstructionGetResponse</a></code>
- <code title="get /udl/surfaceobstruction/queryhelp">client.surface_obstruction.<a href="./src/unifieddatalibrary/resources/surface_obstruction.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/surface_obstruction_queryhelp_response.py">SurfaceObstructionQueryhelpResponse</a></code>
- <code title="get /udl/surfaceobstruction/tuple">client.surface_obstruction.<a href="./src/unifieddatalibrary/resources/surface_obstruction.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/surface_obstruction_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/surface_obstruction_tuple_response.py">SurfaceObstructionTupleResponse</a></code>
- <code title="post /filedrop/udl-surfaceobstruction">client.surface_obstruction.<a href="./src/unifieddatalibrary/resources/surface_obstruction.py">unvalidated_publish</a>(\*\*<a href="src/unifieddatalibrary/types/surface_obstruction_unvalidated_publish_params.py">params</a>) -> None</code>

# Swir

Types:

```python
from unifieddatalibrary.types import (
    SwirListResponse,
    SwirCountResponse,
    SwirQueryhelpResponse,
    SwirTupleResponse,
)
```

Methods:

- <code title="post /udl/swir">client.swir.<a href="./src/unifieddatalibrary/resources/swir/swir.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/swir_create_params.py">params</a>) -> None</code>
- <code title="get /udl/swir">client.swir.<a href="./src/unifieddatalibrary/resources/swir/swir.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/swir_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/swir_list_response.py">SyncOffsetPage[SwirListResponse]</a></code>
- <code title="get /udl/swir/count">client.swir.<a href="./src/unifieddatalibrary/resources/swir/swir.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/swir_count_params.py">params</a>) -> str</code>
- <code title="post /udl/swir/createBulk">client.swir.<a href="./src/unifieddatalibrary/resources/swir/swir.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/swir_create_bulk_params.py">params</a>) -> None</code>
- <code title="get /udl/swir/{id}">client.swir.<a href="./src/unifieddatalibrary/resources/swir/swir.py">get</a>(id, \*\*<a href="src/unifieddatalibrary/types/swir_get_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/swir/swir_full.py">SwirFull</a></code>
- <code title="get /udl/swir/queryhelp">client.swir.<a href="./src/unifieddatalibrary/resources/swir/swir.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/swir_queryhelp_response.py">SwirQueryhelpResponse</a></code>
- <code title="get /udl/swir/tuple">client.swir.<a href="./src/unifieddatalibrary/resources/swir/swir.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/swir_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/swir_tuple_response.py">SwirTupleResponse</a></code>

## History

Types:

```python
from unifieddatalibrary.types.swir import SwirFull, HistoryCountResponse
```

Methods:

- <code title="get /udl/swir/history">client.swir.history.<a href="./src/unifieddatalibrary/resources/swir/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/swir/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/swir/swir_full.py">SyncOffsetPage[SwirFull]</a></code>
- <code title="get /udl/swir/history/aodr">client.swir.history.<a href="./src/unifieddatalibrary/resources/swir/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/swir/history_aodr_params.py">params</a>) -> None</code>
- <code title="get /udl/swir/history/count">client.swir.history.<a href="./src/unifieddatalibrary/resources/swir/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/swir/history_count_params.py">params</a>) -> str</code>

# TaiUtc

Types:

```python
from unifieddatalibrary.types import (
    TaiUtcListResponse,
    TaiUtcCountResponse,
    TaiUtcQueryhelpResponse,
    TaiUtcTupleResponse,
)
```

Methods:

- <code title="post /udl/taiutc">client.tai_utc.<a href="./src/unifieddatalibrary/resources/tai_utc/tai_utc.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/tai_utc_create_params.py">params</a>) -> None</code>
- <code title="put /udl/taiutc/{id}">client.tai_utc.<a href="./src/unifieddatalibrary/resources/tai_utc/tai_utc.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/tai_utc_update_params.py">params</a>) -> None</code>
- <code title="get /udl/taiutc">client.tai_utc.<a href="./src/unifieddatalibrary/resources/tai_utc/tai_utc.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/tai_utc_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/tai_utc_list_response.py">SyncOffsetPage[TaiUtcListResponse]</a></code>
- <code title="delete /udl/taiutc/{id}">client.tai_utc.<a href="./src/unifieddatalibrary/resources/tai_utc/tai_utc.py">delete</a>(id) -> None</code>
- <code title="get /udl/taiutc/count">client.tai_utc.<a href="./src/unifieddatalibrary/resources/tai_utc/tai_utc.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/tai_utc_count_params.py">params</a>) -> str</code>
- <code title="get /udl/taiutc/{id}">client.tai_utc.<a href="./src/unifieddatalibrary/resources/tai_utc/tai_utc.py">get</a>(id, \*\*<a href="src/unifieddatalibrary/types/tai_utc_get_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/tai_utc/taiutc_full.py">TaiutcFull</a></code>
- <code title="get /udl/taiutc/queryhelp">client.tai_utc.<a href="./src/unifieddatalibrary/resources/tai_utc/tai_utc.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/tai_utc_queryhelp_response.py">TaiUtcQueryhelpResponse</a></code>
- <code title="get /udl/taiutc/tuple">client.tai_utc.<a href="./src/unifieddatalibrary/resources/tai_utc/tai_utc.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/tai_utc_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/tai_utc_tuple_response.py">TaiUtcTupleResponse</a></code>

## History

Types:

```python
from unifieddatalibrary.types.tai_utc import TaiutcFull, HistoryCountResponse
```

Methods:

- <code title="get /udl/taiutc/history">client.tai_utc.history.<a href="./src/unifieddatalibrary/resources/tai_utc/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/tai_utc/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/tai_utc/taiutc_full.py">SyncOffsetPage[TaiutcFull]</a></code>
- <code title="get /udl/taiutc/history/aodr">client.tai_utc.history.<a href="./src/unifieddatalibrary/resources/tai_utc/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/tai_utc/history_aodr_params.py">params</a>) -> None</code>
- <code title="get /udl/taiutc/history/count">client.tai_utc.history.<a href="./src/unifieddatalibrary/resources/tai_utc/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/tai_utc/history_count_params.py">params</a>) -> str</code>

# TdoaFdoa

## Diffofarrival

Types:

```python
from unifieddatalibrary.types.tdoa_fdoa import (
    DiffofarrivalAbridged,
    DiffofarrivalFull,
    DiffofarrivalCountResponse,
)
```

Methods:

- <code title="post /udl/diffofarrival">client.tdoa_fdoa.diffofarrival.<a href="./src/unifieddatalibrary/resources/tdoa_fdoa/diffofarrival/diffofarrival.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/tdoa_fdoa/diffofarrival_create_params.py">params</a>) -> None</code>
- <code title="get /udl/diffofarrival">client.tdoa_fdoa.diffofarrival.<a href="./src/unifieddatalibrary/resources/tdoa_fdoa/diffofarrival/diffofarrival.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/tdoa_fdoa/diffofarrival_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/tdoa_fdoa/diffofarrival_abridged.py">SyncOffsetPage[DiffofarrivalAbridged]</a></code>
- <code title="get /udl/diffofarrival/count">client.tdoa_fdoa.diffofarrival.<a href="./src/unifieddatalibrary/resources/tdoa_fdoa/diffofarrival/diffofarrival.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/tdoa_fdoa/diffofarrival_count_params.py">params</a>) -> str</code>
- <code title="post /udl/diffofarrival/createBulk">client.tdoa_fdoa.diffofarrival.<a href="./src/unifieddatalibrary/resources/tdoa_fdoa/diffofarrival/diffofarrival.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/tdoa_fdoa/diffofarrival_create_bulk_params.py">params</a>) -> None</code>

### History

Methods:

- <code title="get /udl/diffofarrival/history">client.tdoa_fdoa.diffofarrival.history.<a href="./src/unifieddatalibrary/resources/tdoa_fdoa/diffofarrival/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/tdoa_fdoa/diffofarrival/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/tdoa_fdoa/diffofarrival_full.py">SyncOffsetPage[DiffofarrivalFull]</a></code>
- <code title="get /udl/diffofarrival/history/aodr">client.tdoa_fdoa.diffofarrival.history.<a href="./src/unifieddatalibrary/resources/tdoa_fdoa/diffofarrival/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/tdoa_fdoa/diffofarrival/history_aodr_params.py">params</a>) -> None</code>

# Track

Types:

```python
from unifieddatalibrary.types import (
    TrackListResponse,
    TrackCountResponse,
    TrackQueryhelpResponse,
    TrackTupleResponse,
)
```

Methods:

- <code title="get /udl/track">client.track.<a href="./src/unifieddatalibrary/resources/track/track.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/track_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/track_list_response.py">SyncOffsetPage[TrackListResponse]</a></code>
- <code title="get /udl/track/count">client.track.<a href="./src/unifieddatalibrary/resources/track/track.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/track_count_params.py">params</a>) -> str</code>
- <code title="post /udl/track/createBulk">client.track.<a href="./src/unifieddatalibrary/resources/track/track.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/track_create_bulk_params.py">params</a>) -> None</code>
- <code title="get /udl/track/queryhelp">client.track.<a href="./src/unifieddatalibrary/resources/track/track.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/track_queryhelp_response.py">TrackQueryhelpResponse</a></code>
- <code title="get /udl/track/tuple">client.track.<a href="./src/unifieddatalibrary/resources/track/track.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/track_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/track_tuple_response.py">TrackTupleResponse</a></code>
- <code title="post /filedrop/udl-tracks">client.track.<a href="./src/unifieddatalibrary/resources/track/track.py">unvalidated_publish</a>(\*\*<a href="src/unifieddatalibrary/types/track_unvalidated_publish_params.py">params</a>) -> None</code>

## History

Types:

```python
from unifieddatalibrary.types.track import TrackFull, HistoryCountResponse
```

Methods:

- <code title="get /udl/track/history">client.track.history.<a href="./src/unifieddatalibrary/resources/track/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/track/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/track/track_full.py">SyncOffsetPage[TrackFull]</a></code>
- <code title="get /udl/track/history/aodr">client.track.history.<a href="./src/unifieddatalibrary/resources/track/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/track/history_aodr_params.py">params</a>) -> None</code>
- <code title="get /udl/track/history/count">client.track.history.<a href="./src/unifieddatalibrary/resources/track/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/track/history_count_params.py">params</a>) -> str</code>

# TrackDetails

Types:

```python
from unifieddatalibrary.types import (
    TrackDetailListResponse,
    TrackDetailCountResponse,
    TrackDetailQueryhelpResponse,
    TrackDetailTupleResponse,
)
```

Methods:

- <code title="get /udl/trackdetails">client.track_details.<a href="./src/unifieddatalibrary/resources/track_details/track_details.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/track_detail_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/track_detail_list_response.py">SyncOffsetPage[TrackDetailListResponse]</a></code>
- <code title="get /udl/trackdetails/count">client.track_details.<a href="./src/unifieddatalibrary/resources/track_details/track_details.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/track_detail_count_params.py">params</a>) -> str</code>
- <code title="post /udl/trackdetails/createBulk">client.track_details.<a href="./src/unifieddatalibrary/resources/track_details/track_details.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/track_detail_create_bulk_params.py">params</a>) -> None</code>
- <code title="get /udl/trackdetails/queryhelp">client.track_details.<a href="./src/unifieddatalibrary/resources/track_details/track_details.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/track_detail_queryhelp_response.py">TrackDetailQueryhelpResponse</a></code>
- <code title="get /udl/trackdetails/tuple">client.track_details.<a href="./src/unifieddatalibrary/resources/track_details/track_details.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/track_detail_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/track_detail_tuple_response.py">TrackDetailTupleResponse</a></code>

## History

Types:

```python
from unifieddatalibrary.types.track_details import TrackDetailsFull, HistoryCountResponse
```

Methods:

- <code title="get /udl/trackdetails/history">client.track_details.history.<a href="./src/unifieddatalibrary/resources/track_details/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/track_details/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/track_details/track_details_full.py">SyncOffsetPage[TrackDetailsFull]</a></code>
- <code title="get /udl/trackdetails/history/aodr">client.track_details.history.<a href="./src/unifieddatalibrary/resources/track_details/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/track_details/history_aodr_params.py">params</a>) -> None</code>
- <code title="get /udl/trackdetails/history/count">client.track_details.history.<a href="./src/unifieddatalibrary/resources/track_details/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/track_details/history_count_params.py">params</a>) -> str</code>

# TrackRoute

Types:

```python
from unifieddatalibrary.types import (
    AltitudeBlocksIngest,
    PointOfContactIngest,
    RoutePointsIngest,
    TrackRouteIngest,
    TrackRouteListResponse,
    TrackRouteCountResponse,
    TrackRouteQueryhelpResponse,
    TrackRouteTupleResponse,
)
```

Methods:

- <code title="post /udl/trackroute">client.track_route.<a href="./src/unifieddatalibrary/resources/track_route/track_route.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/track_route_create_params.py">params</a>) -> None</code>
- <code title="put /udl/trackroute/{id}">client.track_route.<a href="./src/unifieddatalibrary/resources/track_route/track_route.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/track_route_update_params.py">params</a>) -> None</code>
- <code title="get /udl/trackroute">client.track_route.<a href="./src/unifieddatalibrary/resources/track_route/track_route.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/track_route_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/track_route_list_response.py">SyncOffsetPage[TrackRouteListResponse]</a></code>
- <code title="delete /udl/trackroute/{id}">client.track_route.<a href="./src/unifieddatalibrary/resources/track_route/track_route.py">delete</a>(id) -> None</code>
- <code title="get /udl/trackroute/count">client.track_route.<a href="./src/unifieddatalibrary/resources/track_route/track_route.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/track_route_count_params.py">params</a>) -> str</code>
- <code title="post /udl/trackroute/createBulk">client.track_route.<a href="./src/unifieddatalibrary/resources/track_route/track_route.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/track_route_create_bulk_params.py">params</a>) -> None</code>
- <code title="get /udl/trackroute/{id}">client.track_route.<a href="./src/unifieddatalibrary/resources/track_route/track_route.py">get</a>(id, \*\*<a href="src/unifieddatalibrary/types/track_route_get_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/track_route/track_route_full.py">TrackRouteFull</a></code>
- <code title="get /udl/trackroute/queryhelp">client.track_route.<a href="./src/unifieddatalibrary/resources/track_route/track_route.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/track_route_queryhelp_response.py">TrackRouteQueryhelpResponse</a></code>
- <code title="get /udl/trackroute/tuple">client.track_route.<a href="./src/unifieddatalibrary/resources/track_route/track_route.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/track_route_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/track_route_tuple_response.py">TrackRouteTupleResponse</a></code>
- <code title="post /filedrop/udl-trackroute">client.track_route.<a href="./src/unifieddatalibrary/resources/track_route/track_route.py">unvalidated_publish</a>(\*\*<a href="src/unifieddatalibrary/types/track_route_unvalidated_publish_params.py">params</a>) -> None</code>

## History

Types:

```python
from unifieddatalibrary.types.track_route import TrackRouteFull, HistoryCountResponse
```

Methods:

- <code title="get /udl/trackroute/history">client.track_route.history.<a href="./src/unifieddatalibrary/resources/track_route/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/track_route/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/track_route/track_route_full.py">SyncOffsetPage[TrackRouteFull]</a></code>
- <code title="get /udl/trackroute/history/aodr">client.track_route.history.<a href="./src/unifieddatalibrary/resources/track_route/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/track_route/history_aodr_params.py">params</a>) -> None</code>
- <code title="get /udl/trackroute/history/count">client.track_route.history.<a href="./src/unifieddatalibrary/resources/track_route/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/track_route/history_count_params.py">params</a>) -> str</code>

# Transponder

Types:

```python
from unifieddatalibrary.types import (
    TransponderListResponse,
    TransponderCountResponse,
    TransponderGetResponse,
    TransponderQueryhelpResponse,
    TransponderTupleResponse,
)
```

Methods:

- <code title="post /udl/transponder">client.transponder.<a href="./src/unifieddatalibrary/resources/transponder.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/transponder_create_params.py">params</a>) -> None</code>
- <code title="put /udl/transponder/{id}">client.transponder.<a href="./src/unifieddatalibrary/resources/transponder.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/transponder_update_params.py">params</a>) -> None</code>
- <code title="get /udl/transponder">client.transponder.<a href="./src/unifieddatalibrary/resources/transponder.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/transponder_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/transponder_list_response.py">SyncOffsetPage[TransponderListResponse]</a></code>
- <code title="delete /udl/transponder/{id}">client.transponder.<a href="./src/unifieddatalibrary/resources/transponder.py">delete</a>(id) -> None</code>
- <code title="get /udl/transponder/count">client.transponder.<a href="./src/unifieddatalibrary/resources/transponder.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/transponder_count_params.py">params</a>) -> str</code>
- <code title="get /udl/transponder/{id}">client.transponder.<a href="./src/unifieddatalibrary/resources/transponder.py">get</a>(id, \*\*<a href="src/unifieddatalibrary/types/transponder_get_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/transponder_get_response.py">TransponderGetResponse</a></code>
- <code title="get /udl/transponder/queryhelp">client.transponder.<a href="./src/unifieddatalibrary/resources/transponder.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/transponder_queryhelp_response.py">TransponderQueryhelpResponse</a></code>
- <code title="get /udl/transponder/tuple">client.transponder.<a href="./src/unifieddatalibrary/resources/transponder.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/transponder_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/transponder_tuple_response.py">TransponderTupleResponse</a></code>

# User

Types:

```python
from unifieddatalibrary.types import UserAuthResponse
```

Methods:

- <code title="get /basicAuth">client.user.<a href="./src/unifieddatalibrary/resources/user.py">auth</a>() -> <a href="./src/unifieddatalibrary/types/user_auth_response.py">UserAuthResponse</a></code>

# Vessel

Types:

```python
from unifieddatalibrary.types import (
    VesselListResponse,
    VesselCountResponse,
    VesselGetResponse,
    VesselQueryhelpResponse,
    VesselTupleResponse,
)
```

Methods:

- <code title="post /udl/vessel">client.vessel.<a href="./src/unifieddatalibrary/resources/vessel.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/vessel_create_params.py">params</a>) -> None</code>
- <code title="put /udl/vessel/{id}">client.vessel.<a href="./src/unifieddatalibrary/resources/vessel.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/vessel_update_params.py">params</a>) -> None</code>
- <code title="get /udl/vessel">client.vessel.<a href="./src/unifieddatalibrary/resources/vessel.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/vessel_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/vessel_list_response.py">SyncOffsetPage[VesselListResponse]</a></code>
- <code title="get /udl/vessel/count">client.vessel.<a href="./src/unifieddatalibrary/resources/vessel.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/vessel_count_params.py">params</a>) -> str</code>
- <code title="post /udl/vessel/createBulk">client.vessel.<a href="./src/unifieddatalibrary/resources/vessel.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/vessel_create_bulk_params.py">params</a>) -> None</code>
- <code title="get /udl/vessel/{id}">client.vessel.<a href="./src/unifieddatalibrary/resources/vessel.py">get</a>(id, \*\*<a href="src/unifieddatalibrary/types/vessel_get_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/vessel_get_response.py">VesselGetResponse</a></code>
- <code title="get /udl/vessel/queryhelp">client.vessel.<a href="./src/unifieddatalibrary/resources/vessel.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/vessel_queryhelp_response.py">VesselQueryhelpResponse</a></code>
- <code title="get /udl/vessel/tuple">client.vessel.<a href="./src/unifieddatalibrary/resources/vessel.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/vessel_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/vessel_tuple_response.py">VesselTupleResponse</a></code>

# Video

Types:

```python
from unifieddatalibrary.types import (
    VideoListResponse,
    VideoCountResponse,
    VideoGetPlayerStreamingInfoResponse,
    VideoGetPublisherStreamingInfoResponse,
    VideoGetStreamFileResponse,
    VideoQueryhelpResponse,
    VideoTupleResponse,
)
```

Methods:

- <code title="post /udl/video">client.video.<a href="./src/unifieddatalibrary/resources/video/video.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/video_create_params.py">params</a>) -> None</code>
- <code title="get /udl/video">client.video.<a href="./src/unifieddatalibrary/resources/video/video.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/video_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/video_list_response.py">SyncOffsetPage[VideoListResponse]</a></code>
- <code title="get /udl/video/count">client.video.<a href="./src/unifieddatalibrary/resources/video/video.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/video_count_params.py">params</a>) -> str</code>
- <code title="get /udl/video/{id}">client.video.<a href="./src/unifieddatalibrary/resources/video/video.py">get</a>(id, \*\*<a href="src/unifieddatalibrary/types/video_get_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/video/video_streams_full.py">VideoStreamsFull</a></code>
- <code title="get /udl/video/getPlayerStreamingInfo">client.video.<a href="./src/unifieddatalibrary/resources/video/video.py">get_player_streaming_info</a>(\*\*<a href="src/unifieddatalibrary/types/video_get_player_streaming_info_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/video_get_player_streaming_info_response.py">VideoGetPlayerStreamingInfoResponse</a></code>
- <code title="get /udl/video/getPublisherStreamingInfo">client.video.<a href="./src/unifieddatalibrary/resources/video/video.py">get_publisher_streaming_info</a>(\*\*<a href="src/unifieddatalibrary/types/video_get_publisher_streaming_info_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/video_get_publisher_streaming_info_response.py">VideoGetPublisherStreamingInfoResponse</a></code>
- <code title="get /udl/video/getStreamFile">client.video.<a href="./src/unifieddatalibrary/resources/video/video.py">get_stream_file</a>(\*\*<a href="src/unifieddatalibrary/types/video_get_stream_file_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/video_get_stream_file_response.py">VideoGetStreamFileResponse</a></code>
- <code title="get /udl/video/queryhelp">client.video.<a href="./src/unifieddatalibrary/resources/video/video.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/video_queryhelp_response.py">VideoQueryhelpResponse</a></code>
- <code title="get /udl/video/tuple">client.video.<a href="./src/unifieddatalibrary/resources/video/video.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/video_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/video_tuple_response.py">VideoTupleResponse</a></code>

## History

Types:

```python
from unifieddatalibrary.types.video import VideoStreamsFull, HistoryCountResponse
```

Methods:

- <code title="get /udl/video/history">client.video.history.<a href="./src/unifieddatalibrary/resources/video/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/video/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/video/video_streams_full.py">SyncOffsetPage[VideoStreamsFull]</a></code>
- <code title="get /udl/video/history/count">client.video.history.<a href="./src/unifieddatalibrary/resources/video/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/video/history_count_params.py">params</a>) -> str</code>

# WeatherData

Types:

```python
from unifieddatalibrary.types import (
    WeatherDataListResponse,
    WeatherDataCountResponse,
    WeatherDataQueryhelpResponse,
    WeatherDataTupleResponse,
)
```

Methods:

- <code title="post /udl/weatherdata">client.weather_data.<a href="./src/unifieddatalibrary/resources/weather_data/weather_data.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/weather_data_create_params.py">params</a>) -> None</code>
- <code title="get /udl/weatherdata">client.weather_data.<a href="./src/unifieddatalibrary/resources/weather_data/weather_data.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/weather_data_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/weather_data_list_response.py">SyncOffsetPage[WeatherDataListResponse]</a></code>
- <code title="get /udl/weatherdata/count">client.weather_data.<a href="./src/unifieddatalibrary/resources/weather_data/weather_data.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/weather_data_count_params.py">params</a>) -> str</code>
- <code title="post /udl/weatherdata/createBulk">client.weather_data.<a href="./src/unifieddatalibrary/resources/weather_data/weather_data.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/weather_data_create_bulk_params.py">params</a>) -> None</code>
- <code title="get /udl/weatherdata/{id}">client.weather_data.<a href="./src/unifieddatalibrary/resources/weather_data/weather_data.py">get</a>(id, \*\*<a href="src/unifieddatalibrary/types/weather_data_get_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/weather_data/weather_data_full.py">WeatherDataFull</a></code>
- <code title="get /udl/weatherdata/queryhelp">client.weather_data.<a href="./src/unifieddatalibrary/resources/weather_data/weather_data.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/weather_data_queryhelp_response.py">WeatherDataQueryhelpResponse</a></code>
- <code title="get /udl/weatherdata/tuple">client.weather_data.<a href="./src/unifieddatalibrary/resources/weather_data/weather_data.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/weather_data_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/weather_data_tuple_response.py">WeatherDataTupleResponse</a></code>
- <code title="post /filedrop/udl-weatherdata">client.weather_data.<a href="./src/unifieddatalibrary/resources/weather_data/weather_data.py">unvalidated_publish</a>(\*\*<a href="src/unifieddatalibrary/types/weather_data_unvalidated_publish_params.py">params</a>) -> None</code>

## History

Types:

```python
from unifieddatalibrary.types.weather_data import WeatherDataFull, HistoryCountResponse
```

Methods:

- <code title="get /udl/weatherdata/history">client.weather_data.history.<a href="./src/unifieddatalibrary/resources/weather_data/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/weather_data/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/weather_data/weather_data_full.py">SyncOffsetPage[WeatherDataFull]</a></code>
- <code title="get /udl/weatherdata/history/aodr">client.weather_data.history.<a href="./src/unifieddatalibrary/resources/weather_data/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/weather_data/history_aodr_params.py">params</a>) -> None</code>
- <code title="get /udl/weatherdata/history/count">client.weather_data.history.<a href="./src/unifieddatalibrary/resources/weather_data/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/weather_data/history_count_params.py">params</a>) -> str</code>

# WeatherReport

Types:

```python
from unifieddatalibrary.types import (
    WeatherReportListResponse,
    WeatherReportCountResponse,
    WeatherReportQueryhelpResponse,
    WeatherReportTupleResponse,
)
```

Methods:

- <code title="post /udl/weatherreport">client.weather_report.<a href="./src/unifieddatalibrary/resources/weather_report/weather_report.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/weather_report_create_params.py">params</a>) -> None</code>
- <code title="get /udl/weatherreport">client.weather_report.<a href="./src/unifieddatalibrary/resources/weather_report/weather_report.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/weather_report_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/weather_report_list_response.py">SyncOffsetPage[WeatherReportListResponse]</a></code>
- <code title="get /udl/weatherreport/count">client.weather_report.<a href="./src/unifieddatalibrary/resources/weather_report/weather_report.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/weather_report_count_params.py">params</a>) -> str</code>
- <code title="get /udl/weatherreport/{id}">client.weather_report.<a href="./src/unifieddatalibrary/resources/weather_report/weather_report.py">get</a>(id, \*\*<a href="src/unifieddatalibrary/types/weather_report_get_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/weather_report/weather_report_full.py">WeatherReportFull</a></code>
- <code title="get /udl/weatherreport/queryhelp">client.weather_report.<a href="./src/unifieddatalibrary/resources/weather_report/weather_report.py">queryhelp</a>() -> <a href="./src/unifieddatalibrary/types/weather_report_queryhelp_response.py">WeatherReportQueryhelpResponse</a></code>
- <code title="get /udl/weatherreport/tuple">client.weather_report.<a href="./src/unifieddatalibrary/resources/weather_report/weather_report.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/weather_report_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/weather_report_tuple_response.py">WeatherReportTupleResponse</a></code>
- <code title="post /filedrop/udl-weatherreport">client.weather_report.<a href="./src/unifieddatalibrary/resources/weather_report/weather_report.py">unvalidated_publish</a>(\*\*<a href="src/unifieddatalibrary/types/weather_report_unvalidated_publish_params.py">params</a>) -> None</code>

## History

Types:

```python
from unifieddatalibrary.types.weather_report import WeatherReportFull, HistoryCountResponse
```

Methods:

- <code title="get /udl/weatherreport/history">client.weather_report.history.<a href="./src/unifieddatalibrary/resources/weather_report/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/weather_report/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/weather_report/weather_report_full.py">SyncOffsetPage[WeatherReportFull]</a></code>
- <code title="get /udl/weatherreport/history/aodr">client.weather_report.history.<a href="./src/unifieddatalibrary/resources/weather_report/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/weather_report/history_aodr_params.py">params</a>) -> None</code>
- <code title="get /udl/weatherreport/history/count">client.weather_report.history.<a href="./src/unifieddatalibrary/resources/weather_report/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/weather_report/history_count_params.py">params</a>) -> str</code>
