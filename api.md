# Shared Types

```python
from unifieddatalibrary.types import (
    AirTransportMissionFull,
    AircraftstatusFull,
    AIsFull,
    AttitudesetFull,
    CollectRequestFull,
    CollectResponseFull,
    DriftHistory,
    DrifthistoryAbridged,
    EopFull,
    EphemerisFull,
    EvacFull,
    EventEvolutionFull,
    FileData,
    FlightPlanFull,
    Onorbit,
)
```

# AirEvents

Types:

```python
from unifieddatalibrary.types import (
    AirEventListResponse,
    AirEventCountResponse,
    AirEventGetResponse,
    AirEventTupleResponse,
)
```

Methods:

- <code title="post /udl/airevent">client.air_events.<a href="./src/unifieddatalibrary/resources/air_events.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/air_event_create_params.py">params</a>) -> None</code>
- <code title="put /udl/airevent/{id}">client.air_events.<a href="./src/unifieddatalibrary/resources/air_events.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/air_event_update_params.py">params</a>) -> None</code>
- <code title="get /udl/airevent">client.air_events.<a href="./src/unifieddatalibrary/resources/air_events.py">list</a>() -> <a href="./src/unifieddatalibrary/types/air_event_list_response.py">AirEventListResponse</a></code>
- <code title="delete /udl/airevent/{id}">client.air_events.<a href="./src/unifieddatalibrary/resources/air_events.py">delete</a>(id) -> None</code>
- <code title="get /udl/airevent/count">client.air_events.<a href="./src/unifieddatalibrary/resources/air_events.py">count</a>() -> str</code>
- <code title="post /udl/airevent/createBulk">client.air_events.<a href="./src/unifieddatalibrary/resources/air_events.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/air_event_create_bulk_params.py">params</a>) -> None</code>
- <code title="post /filedrop/udl-airevent">client.air_events.<a href="./src/unifieddatalibrary/resources/air_events.py">create_bulk_v2</a>(\*\*<a href="src/unifieddatalibrary/types/air_event_create_bulk_v2_params.py">params</a>) -> None</code>
- <code title="get /udl/airevent/{id}">client.air_events.<a href="./src/unifieddatalibrary/resources/air_events.py">get</a>(id) -> <a href="./src/unifieddatalibrary/types/air_event_get_response.py">AirEventGetResponse</a></code>
- <code title="get /udl/airevent/queryhelp">client.air_events.<a href="./src/unifieddatalibrary/resources/air_events.py">queryhelp</a>() -> None</code>
- <code title="get /udl/airevent/tuple">client.air_events.<a href="./src/unifieddatalibrary/resources/air_events.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/air_event_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/air_event_tuple_response.py">AirEventTupleResponse</a></code>

# AirLoadPlans

Types:

```python
from unifieddatalibrary.types import (
    AirloadplanAbridged,
    AirloadplanFull,
    AirLoadPlanListResponse,
    AirLoadPlanCountResponse,
    AirLoadPlanTupleResponse,
)
```

Methods:

- <code title="post /udl/airloadplan">client.air_load_plans.<a href="./src/unifieddatalibrary/resources/air_load_plans.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/air_load_plan_create_params.py">params</a>) -> None</code>
- <code title="get /udl/airloadplan/{id}">client.air_load_plans.<a href="./src/unifieddatalibrary/resources/air_load_plans.py">retrieve</a>(id) -> <a href="./src/unifieddatalibrary/types/airloadplan_full.py">AirloadplanFull</a></code>
- <code title="get /udl/airloadplan">client.air_load_plans.<a href="./src/unifieddatalibrary/resources/air_load_plans.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/air_load_plan_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/air_load_plan_list_response.py">AirLoadPlanListResponse</a></code>
- <code title="get /udl/airloadplan/count">client.air_load_plans.<a href="./src/unifieddatalibrary/resources/air_load_plans.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/air_load_plan_count_params.py">params</a>) -> str</code>
- <code title="get /udl/airloadplan/queryhelp">client.air_load_plans.<a href="./src/unifieddatalibrary/resources/air_load_plans.py">queryhelp</a>() -> None</code>
- <code title="get /udl/airloadplan/tuple">client.air_load_plans.<a href="./src/unifieddatalibrary/resources/air_load_plans.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/air_load_plan_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/air_load_plan_tuple_response.py">AirLoadPlanTupleResponse</a></code>

# AirOperations

## AirTaskingOrders

Methods:

- <code title="post /filedrop/udl-airtaskingorder">client.air_operations.air_tasking_orders.<a href="./src/unifieddatalibrary/resources/air_operations/air_tasking_orders.py">create_bulk_v2</a>(\*\*<a href="src/unifieddatalibrary/types/air_operations/air_tasking_order_create_bulk_v2_params.py">params</a>) -> None</code>

## AircraftSortie

Types:

```python
from unifieddatalibrary.types.air_operations import (
    AircraftsortieAbridged,
    AircraftsortieFull,
    AircraftSortieListResponse,
    AircraftSortieCountResponse,
    AircraftSortieHistoryCountResponse,
    AircraftSortieHistoryQueryResponse,
)
```

Methods:

- <code title="post /udl/aircraftsortie">client.air_operations.aircraft_sortie.<a href="./src/unifieddatalibrary/resources/air_operations/aircraft_sortie.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/air_operations/aircraft_sortie_create_params.py">params</a>) -> None</code>
- <code title="get /udl/aircraftsortie">client.air_operations.aircraft_sortie.<a href="./src/unifieddatalibrary/resources/air_operations/aircraft_sortie.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/air_operations/aircraft_sortie_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/air_operations/aircraft_sortie_list_response.py">AircraftSortieListResponse</a></code>
- <code title="get /udl/aircraftsortie/count">client.air_operations.aircraft_sortie.<a href="./src/unifieddatalibrary/resources/air_operations/aircraft_sortie.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/air_operations/aircraft_sortie_count_params.py">params</a>) -> str</code>
- <code title="post /udl/aircraftsortie/createBulk">client.air_operations.aircraft_sortie.<a href="./src/unifieddatalibrary/resources/air_operations/aircraft_sortie.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/air_operations/aircraft_sortie_create_bulk_params.py">params</a>) -> None</code>
- <code title="get /udl/aircraftsortie/history/aodr">client.air_operations.aircraft_sortie.<a href="./src/unifieddatalibrary/resources/air_operations/aircraft_sortie.py">history_aodr</a>(\*\*<a href="src/unifieddatalibrary/types/air_operations/aircraft_sortie_history_aodr_params.py">params</a>) -> None</code>
- <code title="get /udl/aircraftsortie/history/count">client.air_operations.aircraft_sortie.<a href="./src/unifieddatalibrary/resources/air_operations/aircraft_sortie.py">history_count</a>(\*\*<a href="src/unifieddatalibrary/types/air_operations/aircraft_sortie_history_count_params.py">params</a>) -> str</code>
- <code title="get /udl/aircraftsortie/history">client.air_operations.aircraft_sortie.<a href="./src/unifieddatalibrary/resources/air_operations/aircraft_sortie.py">history_query</a>(\*\*<a href="src/unifieddatalibrary/types/air_operations/aircraft_sortie_history_query_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/air_operations/aircraft_sortie_history_query_response.py">AircraftSortieHistoryQueryResponse</a></code>

## AircraftSorties

Methods:

- <code title="post /filedrop/udl-aircraftsortie">client.air_operations.aircraft_sorties.<a href="./src/unifieddatalibrary/resources/air_operations/aircraft_sorties.py">create_bulk_v2</a>(\*\*<a href="src/unifieddatalibrary/types/air_operations/aircraft_sorty_create_bulk_v2_params.py">params</a>) -> None</code>

## AirspaceControlOrders

Methods:

- <code title="post /filedrop/udl-airspacecontrolorder">client.air_operations.airspace_control_orders.<a href="./src/unifieddatalibrary/resources/air_operations/airspace_control_orders.py">create_bulk_v2</a>(\*\*<a href="src/unifieddatalibrary/types/air_operations/airspace_control_order_create_bulk_v2_params.py">params</a>) -> None</code>

## Crewpapers

Methods:

- <code title="post /udl/crewpapers/unpublish">client.air_operations.crewpapers.<a href="./src/unifieddatalibrary/resources/air_operations/crewpapers.py">unpublish</a>(\*\*<a href="src/unifieddatalibrary/types/air_operations/crewpaper_unpublish_params.py">params</a>) -> None</code>
- <code title="post /filedrop/crewpapers">client.air_operations.crewpapers.<a href="./src/unifieddatalibrary/resources/air_operations/crewpapers.py">upload_pdf</a>(\*\*<a href="src/unifieddatalibrary/types/air_operations/crewpaper_upload_pdf_params.py">params</a>) -> None</code>

## DiplomaticClearance

Types:

```python
from unifieddatalibrary.types.air_operations import (
    DiplomaticclearanceAbridged,
    DiplomaticclearanceFull,
)
```

Methods:

- <code title="post /filedrop/udl-diplomaticclearance">client.air_operations.diplomatic_clearance.<a href="./src/unifieddatalibrary/resources/air_operations/diplomatic_clearance.py">create_bulk_v2</a>(\*\*<a href="src/unifieddatalibrary/types/air_operations/diplomatic_clearance_create_bulk_v2_params.py">params</a>) -> None</code>

# AirTaskingOrders

Types:

```python
from unifieddatalibrary.types import (
    AirTaskingOrderFull,
    AirTaskingOrderCountResponse,
    AirTaskingOrderTupleResponse,
)
```

Methods:

- <code title="post /udl/airtaskingorder">client.air_tasking_orders.<a href="./src/unifieddatalibrary/resources/air_tasking_orders.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/air_tasking_order_create_params.py">params</a>) -> None</code>
- <code title="get /udl/airtaskingorder/{id}">client.air_tasking_orders.<a href="./src/unifieddatalibrary/resources/air_tasking_orders.py">retrieve</a>(id) -> <a href="./src/unifieddatalibrary/types/air_tasking_order_full.py">AirTaskingOrderFull</a></code>
- <code title="get /udl/airtaskingorder/count">client.air_tasking_orders.<a href="./src/unifieddatalibrary/resources/air_tasking_orders.py">count</a>() -> str</code>
- <code title="get /udl/airtaskingorder/queryhelp">client.air_tasking_orders.<a href="./src/unifieddatalibrary/resources/air_tasking_orders.py">query_help</a>() -> None</code>
- <code title="get /udl/airtaskingorder/tuple">client.air_tasking_orders.<a href="./src/unifieddatalibrary/resources/air_tasking_orders.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/air_tasking_order_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/air_tasking_order_tuple_response.py">AirTaskingOrderTupleResponse</a></code>

# AirTransportMissions

Types:

```python
from unifieddatalibrary.types import (
    AirTransportMissionAbridged,
    AirTransportMissionListResponse,
    AirTransportMissionCountResponse,
    AirTransportMissionTupleResponse,
)
```

Methods:

- <code title="post /udl/airtransportmission">client.air_transport_missions.<a href="./src/unifieddatalibrary/resources/air_transport_missions/air_transport_missions.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/air_transport_mission_create_params.py">params</a>) -> None</code>
- <code title="get /udl/airtransportmission/{id}">client.air_transport_missions.<a href="./src/unifieddatalibrary/resources/air_transport_missions/air_transport_missions.py">retrieve</a>(id) -> <a href="./src/unifieddatalibrary/types/shared/air_transport_mission_full.py">AirTransportMissionFull</a></code>
- <code title="put /udl/airtransportmission/{id}">client.air_transport_missions.<a href="./src/unifieddatalibrary/resources/air_transport_missions/air_transport_missions.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/air_transport_mission_update_params.py">params</a>) -> None</code>
- <code title="get /udl/airtransportmission">client.air_transport_missions.<a href="./src/unifieddatalibrary/resources/air_transport_missions/air_transport_missions.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/air_transport_mission_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/air_transport_mission_list_response.py">AirTransportMissionListResponse</a></code>
- <code title="get /udl/airtransportmission/count">client.air_transport_missions.<a href="./src/unifieddatalibrary/resources/air_transport_missions/air_transport_missions.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/air_transport_mission_count_params.py">params</a>) -> str</code>
- <code title="get /udl/airtransportmission/queryhelp">client.air_transport_missions.<a href="./src/unifieddatalibrary/resources/air_transport_missions/air_transport_missions.py">queryhelp</a>() -> None</code>
- <code title="get /udl/airtransportmission/tuple">client.air_transport_missions.<a href="./src/unifieddatalibrary/resources/air_transport_missions/air_transport_missions.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/air_transport_mission_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/air_transport_mission_tuple_response.py">AirTransportMissionTupleResponse</a></code>

## History

Types:

```python
from unifieddatalibrary.types.air_transport_missions import (
    HistoryListResponse,
    HistoryCountResponse,
)
```

Methods:

- <code title="get /udl/airtransportmission/history">client.air_transport_missions.history.<a href="./src/unifieddatalibrary/resources/air_transport_missions/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/air_transport_missions/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/air_transport_missions/history_list_response.py">HistoryListResponse</a></code>
- <code title="get /udl/airtransportmission/history/aodr">client.air_transport_missions.history.<a href="./src/unifieddatalibrary/resources/air_transport_missions/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/air_transport_missions/history_aodr_params.py">params</a>) -> None</code>
- <code title="get /udl/airtransportmission/history/count">client.air_transport_missions.history.<a href="./src/unifieddatalibrary/resources/air_transport_missions/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/air_transport_missions/history_count_params.py">params</a>) -> str</code>

# Aircraft

Types:

```python
from unifieddatalibrary.types import (
    AircraftAbridged,
    AircraftFull,
    AircraftListResponse,
    AircraftCountResponse,
    AircraftTupleQueryResponse,
)
```

Methods:

- <code title="post /udl/aircraft">client.aircraft.<a href="./src/unifieddatalibrary/resources/aircraft.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/aircraft_create_params.py">params</a>) -> None</code>
- <code title="get /udl/aircraft/{id}">client.aircraft.<a href="./src/unifieddatalibrary/resources/aircraft.py">retrieve</a>(id) -> <a href="./src/unifieddatalibrary/types/aircraft_full.py">AircraftFull</a></code>
- <code title="put /udl/aircraft/{id}">client.aircraft.<a href="./src/unifieddatalibrary/resources/aircraft.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/aircraft_update_params.py">params</a>) -> None</code>
- <code title="get /udl/aircraft">client.aircraft.<a href="./src/unifieddatalibrary/resources/aircraft.py">list</a>() -> <a href="./src/unifieddatalibrary/types/aircraft_list_response.py">AircraftListResponse</a></code>
- <code title="get /udl/aircraft/count">client.aircraft.<a href="./src/unifieddatalibrary/resources/aircraft.py">count</a>() -> str</code>
- <code title="get /udl/aircraft/queryhelp">client.aircraft.<a href="./src/unifieddatalibrary/resources/aircraft.py">queryhelp</a>() -> None</code>
- <code title="get /udl/aircraft/tuple">client.aircraft.<a href="./src/unifieddatalibrary/resources/aircraft.py">tuple_query</a>(\*\*<a href="src/unifieddatalibrary/types/aircraft_tuple_query_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/aircraft_tuple_query_response.py">AircraftTupleQueryResponse</a></code>

# AircraftSorties

Types:

```python
from unifieddatalibrary.types import AircraftSortyTupleResponse
```

Methods:

- <code title="get /udl/aircraftsortie/{id}">client.aircraft_sorties.<a href="./src/unifieddatalibrary/resources/aircraft_sorties.py">retrieve</a>(id) -> <a href="./src/unifieddatalibrary/types/air_operations/aircraftsortie_full.py">AircraftsortieFull</a></code>
- <code title="put /udl/aircraftsortie/{id}">client.aircraft_sorties.<a href="./src/unifieddatalibrary/resources/aircraft_sorties.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/aircraft_sorty_update_params.py">params</a>) -> None</code>
- <code title="get /udl/aircraftsortie/queryhelp">client.aircraft_sorties.<a href="./src/unifieddatalibrary/resources/aircraft_sorties.py">queryhelp</a>() -> None</code>
- <code title="get /udl/aircraftsortie/tuple">client.aircraft_sorties.<a href="./src/unifieddatalibrary/resources/aircraft_sorties.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/aircraft_sorty_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/aircraft_sorty_tuple_response.py">AircraftSortyTupleResponse</a></code>

# AircraftStatusRemarks

Types:

```python
from unifieddatalibrary.types import (
    AircraftstatusremarkAbridged,
    AircraftstatusremarkFull,
    AircraftStatusRemarkListResponse,
    AircraftStatusRemarkCountResponse,
    AircraftStatusRemarkTupleResponse,
)
```

Methods:

- <code title="post /udl/aircraftstatusremark">client.aircraft_status_remarks.<a href="./src/unifieddatalibrary/resources/aircraft_status_remarks.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/aircraft_status_remark_create_params.py">params</a>) -> None</code>
- <code title="get /udl/aircraftstatusremark/{id}">client.aircraft_status_remarks.<a href="./src/unifieddatalibrary/resources/aircraft_status_remarks.py">retrieve</a>(id) -> <a href="./src/unifieddatalibrary/types/aircraftstatusremark_full.py">AircraftstatusremarkFull</a></code>
- <code title="get /udl/aircraftstatusremark">client.aircraft_status_remarks.<a href="./src/unifieddatalibrary/resources/aircraft_status_remarks.py">list</a>() -> <a href="./src/unifieddatalibrary/types/aircraft_status_remark_list_response.py">AircraftStatusRemarkListResponse</a></code>
- <code title="get /udl/aircraftstatusremark/count">client.aircraft_status_remarks.<a href="./src/unifieddatalibrary/resources/aircraft_status_remarks.py">count</a>() -> str</code>
- <code title="get /udl/aircraftstatusremark/queryhelp">client.aircraft_status_remarks.<a href="./src/unifieddatalibrary/resources/aircraft_status_remarks.py">queryhelp</a>() -> None</code>
- <code title="get /udl/aircraftstatusremark/tuple">client.aircraft_status_remarks.<a href="./src/unifieddatalibrary/resources/aircraft_status_remarks.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/aircraft_status_remark_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/aircraft_status_remark_tuple_response.py">AircraftStatusRemarkTupleResponse</a></code>

# AircraftStatuses

Types:

```python
from unifieddatalibrary.types import (
    AircraftstatusAbridged,
    AircraftStatusListResponse,
    AircraftStatusCountResponse,
    AircraftStatusTupleResponse,
)
```

Methods:

- <code title="post /udl/aircraftstatus">client.aircraft_statuses.<a href="./src/unifieddatalibrary/resources/aircraft_statuses/aircraft_statuses.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/aircraft_status_create_params.py">params</a>) -> None</code>
- <code title="get /udl/aircraftstatus/{id}">client.aircraft_statuses.<a href="./src/unifieddatalibrary/resources/aircraft_statuses/aircraft_statuses.py">retrieve</a>(id) -> <a href="./src/unifieddatalibrary/types/shared/aircraftstatus_full.py">AircraftstatusFull</a></code>
- <code title="put /udl/aircraftstatus/{id}">client.aircraft_statuses.<a href="./src/unifieddatalibrary/resources/aircraft_statuses/aircraft_statuses.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/aircraft_status_update_params.py">params</a>) -> None</code>
- <code title="get /udl/aircraftstatus">client.aircraft_statuses.<a href="./src/unifieddatalibrary/resources/aircraft_statuses/aircraft_statuses.py">list</a>() -> <a href="./src/unifieddatalibrary/types/aircraft_status_list_response.py">AircraftStatusListResponse</a></code>
- <code title="delete /udl/aircraftstatus/{id}">client.aircraft_statuses.<a href="./src/unifieddatalibrary/resources/aircraft_statuses/aircraft_statuses.py">delete</a>(id) -> None</code>
- <code title="get /udl/aircraftstatus/count">client.aircraft_statuses.<a href="./src/unifieddatalibrary/resources/aircraft_statuses/aircraft_statuses.py">count</a>() -> str</code>
- <code title="get /udl/aircraftstatus/queryhelp">client.aircraft_statuses.<a href="./src/unifieddatalibrary/resources/aircraft_statuses/aircraft_statuses.py">queryhelp</a>() -> None</code>
- <code title="get /udl/aircraftstatus/tuple">client.aircraft_statuses.<a href="./src/unifieddatalibrary/resources/aircraft_statuses/aircraft_statuses.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/aircraft_status_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/aircraft_status_tuple_response.py">AircraftStatusTupleResponse</a></code>

## History

Types:

```python
from unifieddatalibrary.types.aircraft_statuses import HistoryListResponse, HistoryCountResponse
```

Methods:

- <code title="get /udl/aircraftstatus/history">client.aircraft_statuses.history.<a href="./src/unifieddatalibrary/resources/aircraft_statuses/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/aircraft_statuses/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/aircraft_statuses/history_list_response.py">HistoryListResponse</a></code>
- <code title="get /udl/aircraftstatus/history/count">client.aircraft_statuses.history.<a href="./src/unifieddatalibrary/resources/aircraft_statuses/history.py">count</a>() -> str</code>

# Aircraftstatusremark

Methods:

- <code title="put /udl/aircraftstatusremark/{id}">client.aircraftstatusremark.<a href="./src/unifieddatalibrary/resources/aircraftstatusremark.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/aircraftstatusremark_update_params.py">params</a>) -> None</code>
- <code title="delete /udl/aircraftstatusremark/{id}">client.aircraftstatusremark.<a href="./src/unifieddatalibrary/resources/aircraftstatusremark.py">delete</a>(id) -> None</code>

# AirfieldSlots

Types:

```python
from unifieddatalibrary.types import (
    AirfieldslotAbridged,
    AirfieldslotFull,
    AirfieldSlotListResponse,
)
```

Methods:

- <code title="post /udl/airfieldslot">client.airfield_slots.<a href="./src/unifieddatalibrary/resources/airfield_slots.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/airfield_slot_create_params.py">params</a>) -> None</code>
- <code title="get /udl/airfieldslot">client.airfield_slots.<a href="./src/unifieddatalibrary/resources/airfield_slots.py">list</a>() -> <a href="./src/unifieddatalibrary/types/airfield_slot_list_response.py">AirfieldSlotListResponse</a></code>

# AirfieldStatus

Types:

```python
from unifieddatalibrary.types import AirfieldStatusTupleResponse
```

Methods:

- <code title="get /udl/airfieldstatus/{id}">client.airfield_status.<a href="./src/unifieddatalibrary/resources/airfield_status.py">retrieve</a>(id) -> <a href="./src/unifieddatalibrary/types/airfieldstatus_full.py">AirfieldstatusFull</a></code>
- <code title="put /udl/airfieldstatus/{id}">client.airfield_status.<a href="./src/unifieddatalibrary/resources/airfield_status.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/airfield_status_update_params.py">params</a>) -> None</code>
- <code title="delete /udl/airfieldstatus/{id}">client.airfield_status.<a href="./src/unifieddatalibrary/resources/airfield_status.py">delete</a>(id) -> None</code>
- <code title="get /udl/airfieldstatus/tuple">client.airfield_status.<a href="./src/unifieddatalibrary/resources/airfield_status.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/airfield_status_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/airfield_status_tuple_response.py">AirfieldStatusTupleResponse</a></code>

# Airfields

Types:

```python
from unifieddatalibrary.types import (
    AirfieldAbridged,
    AirfieldFull,
    AirfieldListResponse,
    AirfieldCountResponse,
    AirfieldTupleResponse,
)
```

Methods:

- <code title="post /udl/airfield">client.airfields.<a href="./src/unifieddatalibrary/resources/airfields.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/airfield_create_params.py">params</a>) -> None</code>
- <code title="get /udl/airfield/{id}">client.airfields.<a href="./src/unifieddatalibrary/resources/airfields.py">retrieve</a>(id) -> <a href="./src/unifieddatalibrary/types/airfield_full.py">AirfieldFull</a></code>
- <code title="put /udl/airfield/{id}">client.airfields.<a href="./src/unifieddatalibrary/resources/airfields.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/airfield_update_params.py">params</a>) -> None</code>
- <code title="get /udl/airfield">client.airfields.<a href="./src/unifieddatalibrary/resources/airfields.py">list</a>() -> <a href="./src/unifieddatalibrary/types/airfield_list_response.py">AirfieldListResponse</a></code>
- <code title="get /udl/airfield/count">client.airfields.<a href="./src/unifieddatalibrary/resources/airfields.py">count</a>() -> str</code>
- <code title="get /udl/airfield/queryhelp">client.airfields.<a href="./src/unifieddatalibrary/resources/airfields.py">queryhelp</a>() -> None</code>
- <code title="get /udl/airfield/tuple">client.airfields.<a href="./src/unifieddatalibrary/resources/airfields.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/airfield_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/airfield_tuple_response.py">AirfieldTupleResponse</a></code>

# Airfieldslotconsumptions

Types:

```python
from unifieddatalibrary.types import (
    AirfieldslotconsumptionAbridged,
    AirfieldslotconsumptionFull,
    AirfieldslotconsumptionListResponse,
    AirfieldslotconsumptionCountResponse,
    AirfieldslotconsumptionTupleResponse,
)
```

Methods:

- <code title="post /udl/airfieldslotconsumption">client.airfieldslotconsumptions.<a href="./src/unifieddatalibrary/resources/airfieldslotconsumptions.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/airfieldslotconsumption_create_params.py">params</a>) -> None</code>
- <code title="get /udl/airfieldslotconsumption/{id}">client.airfieldslotconsumptions.<a href="./src/unifieddatalibrary/resources/airfieldslotconsumptions.py">retrieve</a>(id) -> <a href="./src/unifieddatalibrary/types/airfieldslotconsumption_full.py">AirfieldslotconsumptionFull</a></code>
- <code title="put /udl/airfieldslotconsumption/{id}">client.airfieldslotconsumptions.<a href="./src/unifieddatalibrary/resources/airfieldslotconsumptions.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/airfieldslotconsumption_update_params.py">params</a>) -> None</code>
- <code title="get /udl/airfieldslotconsumption">client.airfieldslotconsumptions.<a href="./src/unifieddatalibrary/resources/airfieldslotconsumptions.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/airfieldslotconsumption_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/airfieldslotconsumption_list_response.py">AirfieldslotconsumptionListResponse</a></code>
- <code title="delete /udl/airfieldslotconsumption/{id}">client.airfieldslotconsumptions.<a href="./src/unifieddatalibrary/resources/airfieldslotconsumptions.py">delete</a>(id) -> None</code>
- <code title="get /udl/airfieldslotconsumption/count">client.airfieldslotconsumptions.<a href="./src/unifieddatalibrary/resources/airfieldslotconsumptions.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/airfieldslotconsumption_count_params.py">params</a>) -> str</code>
- <code title="get /udl/airfieldslotconsumption/queryhelp">client.airfieldslotconsumptions.<a href="./src/unifieddatalibrary/resources/airfieldslotconsumptions.py">queryhelp</a>() -> None</code>
- <code title="get /udl/airfieldslotconsumption/tuple">client.airfieldslotconsumptions.<a href="./src/unifieddatalibrary/resources/airfieldslotconsumptions.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/airfieldslotconsumption_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/airfieldslotconsumption_tuple_response.py">AirfieldslotconsumptionTupleResponse</a></code>

# Airfieldslots

Types:

```python
from unifieddatalibrary.types import AirfieldslotCountResponse, AirfieldslotTupleResponse
```

Methods:

- <code title="get /udl/airfieldslot/{id}">client.airfieldslots.<a href="./src/unifieddatalibrary/resources/airfieldslots.py">retrieve</a>(id) -> <a href="./src/unifieddatalibrary/types/airfieldslot_full.py">AirfieldslotFull</a></code>
- <code title="put /udl/airfieldslot/{id}">client.airfieldslots.<a href="./src/unifieddatalibrary/resources/airfieldslots.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/airfieldslot_update_params.py">params</a>) -> None</code>
- <code title="delete /udl/airfieldslot/{id}">client.airfieldslots.<a href="./src/unifieddatalibrary/resources/airfieldslots.py">delete</a>(id) -> None</code>
- <code title="get /udl/airfieldslot/count">client.airfieldslots.<a href="./src/unifieddatalibrary/resources/airfieldslots.py">count</a>() -> str</code>
- <code title="get /udl/airfieldslot/queryhelp">client.airfieldslots.<a href="./src/unifieddatalibrary/resources/airfieldslots.py">queryhelp</a>() -> None</code>
- <code title="get /udl/airfieldslot/tuple">client.airfieldslots.<a href="./src/unifieddatalibrary/resources/airfieldslots.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/airfieldslot_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/airfieldslot_tuple_response.py">AirfieldslotTupleResponse</a></code>

# Airfieldstatus

Types:

```python
from unifieddatalibrary.types import (
    AirfieldstatusAbridged,
    AirfieldstatusFull,
    AirfieldstatusListResponse,
    AirfieldstatusCountResponse,
)
```

Methods:

- <code title="post /udl/airfieldstatus">client.airfieldstatus.<a href="./src/unifieddatalibrary/resources/airfieldstatus/airfieldstatus.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/airfieldstatus_create_params.py">params</a>) -> None</code>
- <code title="get /udl/airfieldstatus">client.airfieldstatus.<a href="./src/unifieddatalibrary/resources/airfieldstatus/airfieldstatus.py">list</a>() -> <a href="./src/unifieddatalibrary/types/airfieldstatus_list_response.py">AirfieldstatusListResponse</a></code>
- <code title="get /udl/airfieldstatus/count">client.airfieldstatus.<a href="./src/unifieddatalibrary/resources/airfieldstatus/airfieldstatus.py">count</a>() -> str</code>
- <code title="get /udl/airfieldstatus/queryhelp">client.airfieldstatus.<a href="./src/unifieddatalibrary/resources/airfieldstatus/airfieldstatus.py">queryhelp</a>() -> None</code>

## History

Types:

```python
from unifieddatalibrary.types.airfieldstatus import HistoryListResponse, HistoryCountResponse
```

Methods:

- <code title="get /udl/airfieldstatus/history">client.airfieldstatus.history.<a href="./src/unifieddatalibrary/resources/airfieldstatus/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/airfieldstatus/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/airfieldstatus/history_list_response.py">HistoryListResponse</a></code>
- <code title="get /udl/airfieldstatus/history/count">client.airfieldstatus.history.<a href="./src/unifieddatalibrary/resources/airfieldstatus/history.py">count</a>() -> str</code>

# Airloadplans

Methods:

- <code title="put /udl/airloadplan/{id}">client.airloadplans.<a href="./src/unifieddatalibrary/resources/airloadplans.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/airloadplan_update_params.py">params</a>) -> None</code>
- <code title="delete /udl/airloadplan/{id}">client.airloadplans.<a href="./src/unifieddatalibrary/resources/airloadplans.py">delete</a>(id) -> None</code>

# AirspaceControlOrders

Types:

```python
from unifieddatalibrary.types import (
    AirspacecontrolorderAbridged,
    AirspacecontrolorderFull,
    AirspaceControlOrderListResponse,
    AirspaceControlOrderCountResponse,
    AirspaceControlOrderTupleResponse,
)
```

Methods:

- <code title="post /udl/airspacecontrolorder">client.airspace_control_orders.<a href="./src/unifieddatalibrary/resources/airspace_control_orders.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/airspace_control_order_create_params.py">params</a>) -> None</code>
- <code title="get /udl/airspacecontrolorder/{id}">client.airspace_control_orders.<a href="./src/unifieddatalibrary/resources/airspace_control_orders.py">retrieve</a>(id) -> <a href="./src/unifieddatalibrary/types/airspacecontrolorder_full.py">AirspacecontrolorderFull</a></code>
- <code title="get /udl/airspacecontrolorder">client.airspace_control_orders.<a href="./src/unifieddatalibrary/resources/airspace_control_orders.py">list</a>() -> <a href="./src/unifieddatalibrary/types/airspace_control_order_list_response.py">AirspaceControlOrderListResponse</a></code>
- <code title="get /udl/airspacecontrolorder/count">client.airspace_control_orders.<a href="./src/unifieddatalibrary/resources/airspace_control_orders.py">count</a>() -> str</code>
- <code title="post /udl/airspacecontrolorder/createBulk">client.airspace_control_orders.<a href="./src/unifieddatalibrary/resources/airspace_control_orders.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/airspace_control_order_create_bulk_params.py">params</a>) -> None</code>
- <code title="get /udl/airspacecontrolorder/queryhelp">client.airspace_control_orders.<a href="./src/unifieddatalibrary/resources/airspace_control_orders.py">query_help</a>() -> None</code>
- <code title="get /udl/airspacecontrolorder/tuple">client.airspace_control_orders.<a href="./src/unifieddatalibrary/resources/airspace_control_orders.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/airspace_control_order_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/airspace_control_order_tuple_response.py">AirspaceControlOrderTupleResponse</a></code>

# Airtaskingorders

Types:

```python
from unifieddatalibrary.types import AirtaskingorderAbridged, AirtaskingorderListResponse
```

Methods:

- <code title="get /udl/airtaskingorder">client.airtaskingorders.<a href="./src/unifieddatalibrary/resources/airtaskingorders.py">list</a>() -> <a href="./src/unifieddatalibrary/types/airtaskingorder_list_response.py">AirtaskingorderListResponse</a></code>

# AIs

Types:

```python
from unifieddatalibrary.types import (
    AIsAbridged,
    AIListResponse,
    AICountResponse,
    AIHistoryCountResponse,
    AITupleResponse,
)
```

Methods:

- <code title="get /udl/ais">client.ais.<a href="./src/unifieddatalibrary/resources/ais/ais.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/ai_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/ai_list_response.py">AIListResponse</a></code>
- <code title="get /udl/ais/count">client.ais.<a href="./src/unifieddatalibrary/resources/ais/ais.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/ai_count_params.py">params</a>) -> str</code>
- <code title="post /udl/ais/createBulk">client.ais.<a href="./src/unifieddatalibrary/resources/ais/ais.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/ai_create_bulk_params.py">params</a>) -> None</code>
- <code title="get /udl/ais/history/count">client.ais.<a href="./src/unifieddatalibrary/resources/ais/ais.py">history_count</a>(\*\*<a href="src/unifieddatalibrary/types/ai_history_count_params.py">params</a>) -> str</code>
- <code title="get /udl/ais/queryhelp">client.ais.<a href="./src/unifieddatalibrary/resources/ais/ais.py">queryhelp</a>() -> None</code>
- <code title="get /udl/ais/tuple">client.ais.<a href="./src/unifieddatalibrary/resources/ais/ais.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/ai_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/ai_tuple_response.py">AITupleResponse</a></code>

## History

Types:

```python
from unifieddatalibrary.types.ais import HistoryListResponse
```

Methods:

- <code title="get /udl/ais/history">client.ais.history.<a href="./src/unifieddatalibrary/resources/ais/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/ais/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/ais/history_list_response.py">HistoryListResponse</a></code>
- <code title="get /udl/ais/history/aodr">client.ais.history.<a href="./src/unifieddatalibrary/resources/ais/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/ais/history_aodr_params.py">params</a>) -> None</code>

# AIsObjects

Methods:

- <code title="post /filedrop/udl-ais">client.ais_objects.<a href="./src/unifieddatalibrary/resources/ais_objects.py">create_bulk_v2</a>(\*\*<a href="src/unifieddatalibrary/types/ais_object_create_bulk_v2_params.py">params</a>) -> None</code>

# AnalyticImagery

Types:

```python
from unifieddatalibrary.types import (
    AnalyticImageryAbridged,
    AnalyticImageryFull,
    AnalyticImageryListResponse,
    AnalyticImageryCountResponse,
    AnalyticImageryHistoryResponse,
    AnalyticImageryHistoryCountResponse,
    AnalyticImageryTupleResponse,
)
```

Methods:

- <code title="get /udl/analyticimagery/{id}">client.analytic_imagery.<a href="./src/unifieddatalibrary/resources/analytic_imagery.py">retrieve</a>(id) -> <a href="./src/unifieddatalibrary/types/analytic_imagery_full.py">AnalyticImageryFull</a></code>
- <code title="get /udl/analyticimagery">client.analytic_imagery.<a href="./src/unifieddatalibrary/resources/analytic_imagery.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/analytic_imagery_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/analytic_imagery_list_response.py">AnalyticImageryListResponse</a></code>
- <code title="get /udl/analyticimagery/count">client.analytic_imagery.<a href="./src/unifieddatalibrary/resources/analytic_imagery.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/analytic_imagery_count_params.py">params</a>) -> str</code>
- <code title="post /filedrop/udl-analyticimagery">client.analytic_imagery.<a href="./src/unifieddatalibrary/resources/analytic_imagery.py">create_bulk_v2</a>(\*\*<a href="src/unifieddatalibrary/types/analytic_imagery_create_bulk_v2_params.py">params</a>) -> None</code>
- <code title="get /udl/analyticimagery/getFile/{id}">client.analytic_imagery.<a href="./src/unifieddatalibrary/resources/analytic_imagery.py">file_get</a>(id) -> BinaryAPIResponse</code>
- <code title="get /udl/analyticimagery/history">client.analytic_imagery.<a href="./src/unifieddatalibrary/resources/analytic_imagery.py">history</a>(\*\*<a href="src/unifieddatalibrary/types/analytic_imagery_history_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/analytic_imagery_history_response.py">AnalyticImageryHistoryResponse</a></code>
- <code title="get /udl/analyticimagery/history/aodr">client.analytic_imagery.<a href="./src/unifieddatalibrary/resources/analytic_imagery.py">history_aodr</a>(\*\*<a href="src/unifieddatalibrary/types/analytic_imagery_history_aodr_params.py">params</a>) -> None</code>
- <code title="get /udl/analyticimagery/history/count">client.analytic_imagery.<a href="./src/unifieddatalibrary/resources/analytic_imagery.py">history_count</a>(\*\*<a href="src/unifieddatalibrary/types/analytic_imagery_history_count_params.py">params</a>) -> str</code>
- <code title="get /udl/analyticimagery/queryhelp">client.analytic_imagery.<a href="./src/unifieddatalibrary/resources/analytic_imagery.py">queryhelp</a>() -> None</code>
- <code title="get /udl/analyticimagery/tuple">client.analytic_imagery.<a href="./src/unifieddatalibrary/resources/analytic_imagery.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/analytic_imagery_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/analytic_imagery_tuple_response.py">AnalyticImageryTupleResponse</a></code>

# Antennas

Types:

```python
from unifieddatalibrary.types import (
    AntennaAbridged,
    AntennaFull,
    AntennaListResponse,
    AntennaCountResponse,
    AntennaTupleResponse,
)
```

Methods:

- <code title="post /udl/antenna">client.antennas.<a href="./src/unifieddatalibrary/resources/antennas.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/antenna_create_params.py">params</a>) -> None</code>
- <code title="get /udl/antenna/{id}">client.antennas.<a href="./src/unifieddatalibrary/resources/antennas.py">retrieve</a>(id) -> <a href="./src/unifieddatalibrary/types/antenna_full.py">AntennaFull</a></code>
- <code title="put /udl/antenna/{id}">client.antennas.<a href="./src/unifieddatalibrary/resources/antennas.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/antenna_update_params.py">params</a>) -> None</code>
- <code title="get /udl/antenna">client.antennas.<a href="./src/unifieddatalibrary/resources/antennas.py">list</a>() -> <a href="./src/unifieddatalibrary/types/antenna_list_response.py">AntennaListResponse</a></code>
- <code title="delete /udl/antenna/{id}">client.antennas.<a href="./src/unifieddatalibrary/resources/antennas.py">delete</a>(id) -> None</code>
- <code title="get /udl/antenna/count">client.antennas.<a href="./src/unifieddatalibrary/resources/antennas.py">count</a>() -> str</code>
- <code title="get /udl/antenna/queryhelp">client.antennas.<a href="./src/unifieddatalibrary/resources/antennas.py">queryhelp</a>() -> None</code>
- <code title="get /udl/antenna/tuple">client.antennas.<a href="./src/unifieddatalibrary/resources/antennas.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/antenna_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/antenna_tuple_response.py">AntennaTupleResponse</a></code>

# AttitudeData

Types:

```python
from unifieddatalibrary.types import AttitudedataFull, AttitudeDataTupleResponse
```

Methods:

- <code title="get /udl/attitudedata/queryhelp">client.attitude_data.<a href="./src/unifieddatalibrary/resources/attitude_data.py">query_help</a>() -> None</code>
- <code title="get /udl/attitudedata/tuple">client.attitude_data.<a href="./src/unifieddatalibrary/resources/attitude_data.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/attitude_data_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/attitude_data_tuple_response.py">AttitudeDataTupleResponse</a></code>

# AttitudeSets

Types:

```python
from unifieddatalibrary.types import (
    AttitudesetAbridged,
    AttitudeSetListResponse,
    AttitudeSetCountResponse,
    AttitudeSetTupleResponse,
)
```

Methods:

- <code title="post /udl/attitudeset">client.attitude_sets.<a href="./src/unifieddatalibrary/resources/attitude_sets/attitude_sets.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/attitude_set_create_params.py">params</a>) -> None</code>
- <code title="get /udl/attitudeset">client.attitude_sets.<a href="./src/unifieddatalibrary/resources/attitude_sets/attitude_sets.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/attitude_set_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/attitude_set_list_response.py">AttitudeSetListResponse</a></code>
- <code title="get /udl/attitudeset/count">client.attitude_sets.<a href="./src/unifieddatalibrary/resources/attitude_sets/attitude_sets.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/attitude_set_count_params.py">params</a>) -> str</code>
- <code title="post /filedrop/udl-attitudeset">client.attitude_sets.<a href="./src/unifieddatalibrary/resources/attitude_sets/attitude_sets.py">create_bulk_v2</a>(\*\*<a href="src/unifieddatalibrary/types/attitude_set_create_bulk_v2_params.py">params</a>) -> None</code>
- <code title="get /udl/attitudeset/queryhelp">client.attitude_sets.<a href="./src/unifieddatalibrary/resources/attitude_sets/attitude_sets.py">query_help</a>() -> None</code>
- <code title="get /udl/attitudeset/tuple">client.attitude_sets.<a href="./src/unifieddatalibrary/resources/attitude_sets/attitude_sets.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/attitude_set_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/attitude_set_tuple_response.py">AttitudeSetTupleResponse</a></code>

## History

Types:

```python
from unifieddatalibrary.types.attitude_sets import HistoryListResponse, HistoryCountResponse
```

Methods:

- <code title="get /udl/attitudeset/history">client.attitude_sets.history.<a href="./src/unifieddatalibrary/resources/attitude_sets/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/attitude_sets/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/attitude_sets/history_list_response.py">HistoryListResponse</a></code>
- <code title="get /udl/attitudeset/history/aodr">client.attitude_sets.history.<a href="./src/unifieddatalibrary/resources/attitude_sets/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/attitude_sets/history_aodr_params.py">params</a>) -> None</code>
- <code title="get /udl/attitudeset/history/count">client.attitude_sets.history.<a href="./src/unifieddatalibrary/resources/attitude_sets/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/attitude_sets/history_count_params.py">params</a>) -> str</code>

# Attitudesets

Methods:

- <code title="get /udl/attitudeset/{id}">client.attitudesets.<a href="./src/unifieddatalibrary/resources/attitudesets.py">retrieve</a>(id) -> <a href="./src/unifieddatalibrary/types/shared/attitudeset_full.py">AttitudesetFull</a></code>

# Batteries

Types:

```python
from unifieddatalibrary.types import (
    BatteryAbridged,
    BatteryFull,
    BatteryListResponse,
    BatteryCountResponse,
    BatteryTupleResponse,
)
```

Methods:

- <code title="post /udl/battery">client.batteries.<a href="./src/unifieddatalibrary/resources/batteries.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/battery_create_params.py">params</a>) -> None</code>
- <code title="get /udl/battery/{id}">client.batteries.<a href="./src/unifieddatalibrary/resources/batteries.py">retrieve</a>(id) -> <a href="./src/unifieddatalibrary/types/battery_full.py">BatteryFull</a></code>
- <code title="put /udl/battery/{id}">client.batteries.<a href="./src/unifieddatalibrary/resources/batteries.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/battery_update_params.py">params</a>) -> None</code>
- <code title="get /udl/battery">client.batteries.<a href="./src/unifieddatalibrary/resources/batteries.py">list</a>() -> <a href="./src/unifieddatalibrary/types/battery_list_response.py">BatteryListResponse</a></code>
- <code title="delete /udl/battery/{id}">client.batteries.<a href="./src/unifieddatalibrary/resources/batteries.py">delete</a>(id) -> None</code>
- <code title="get /udl/battery/count">client.batteries.<a href="./src/unifieddatalibrary/resources/batteries.py">count</a>() -> str</code>
- <code title="get /udl/battery/queryhelp">client.batteries.<a href="./src/unifieddatalibrary/resources/batteries.py">queryhelp</a>() -> None</code>
- <code title="get /udl/battery/tuple">client.batteries.<a href="./src/unifieddatalibrary/resources/batteries.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/battery_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/battery_tuple_response.py">BatteryTupleResponse</a></code>

# Batterydetails

Types:

```python
from unifieddatalibrary.types import (
    BatterydetailsAbridged,
    BatterydetailsFull,
    BatterydetailListResponse,
)
```

Methods:

- <code title="post /udl/batterydetails">client.batterydetails.<a href="./src/unifieddatalibrary/resources/batterydetails.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/batterydetail_create_params.py">params</a>) -> None</code>
- <code title="get /udl/batterydetails/{id}">client.batterydetails.<a href="./src/unifieddatalibrary/resources/batterydetails.py">retrieve</a>(id) -> <a href="./src/unifieddatalibrary/types/batterydetails_full.py">BatterydetailsFull</a></code>
- <code title="put /udl/batterydetails/{id}">client.batterydetails.<a href="./src/unifieddatalibrary/resources/batterydetails.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/batterydetail_update_params.py">params</a>) -> None</code>
- <code title="get /udl/batterydetails">client.batterydetails.<a href="./src/unifieddatalibrary/resources/batterydetails.py">list</a>() -> <a href="./src/unifieddatalibrary/types/batterydetail_list_response.py">BatterydetailListResponse</a></code>
- <code title="delete /udl/batterydetails/{id}">client.batterydetails.<a href="./src/unifieddatalibrary/resources/batterydetails.py">delete</a>(id) -> None</code>

# Beam

Types:

```python
from unifieddatalibrary.types import (
    BeamAbridged,
    BeamFull,
    BeamListResponse,
    BeamCountResponse,
    BeamTupleResponse,
)
```

Methods:

- <code title="post /udl/beam">client.beam.<a href="./src/unifieddatalibrary/resources/beam.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/beam_create_params.py">params</a>) -> None</code>
- <code title="get /udl/beam/{id}">client.beam.<a href="./src/unifieddatalibrary/resources/beam.py">retrieve</a>(id) -> <a href="./src/unifieddatalibrary/types/beam_full.py">BeamFull</a></code>
- <code title="put /udl/beam/{id}">client.beam.<a href="./src/unifieddatalibrary/resources/beam.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/beam_update_params.py">params</a>) -> None</code>
- <code title="get /udl/beam">client.beam.<a href="./src/unifieddatalibrary/resources/beam.py">list</a>() -> <a href="./src/unifieddatalibrary/types/beam_list_response.py">BeamListResponse</a></code>
- <code title="delete /udl/beam/{id}">client.beam.<a href="./src/unifieddatalibrary/resources/beam.py">delete</a>(id) -> None</code>
- <code title="get /udl/beam/count">client.beam.<a href="./src/unifieddatalibrary/resources/beam.py">count</a>() -> str</code>
- <code title="get /udl/beam/queryhelp">client.beam.<a href="./src/unifieddatalibrary/resources/beam.py">query_help</a>() -> None</code>
- <code title="get /udl/beam/tuple">client.beam.<a href="./src/unifieddatalibrary/resources/beam.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/beam_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/beam_tuple_response.py">BeamTupleResponse</a></code>

# BeamContours

Types:

```python
from unifieddatalibrary.types import (
    BeamcontourAbridged,
    BeamcontourFull,
    BeamContourListResponse,
    BeamContourCountResponse,
    BeamContourTupleResponse,
)
```

Methods:

- <code title="post /udl/beamcontour">client.beam_contours.<a href="./src/unifieddatalibrary/resources/beam_contours.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/beam_contour_create_params.py">params</a>) -> None</code>
- <code title="get /udl/beamcontour/{id}">client.beam_contours.<a href="./src/unifieddatalibrary/resources/beam_contours.py">retrieve</a>(id) -> <a href="./src/unifieddatalibrary/types/beamcontour_full.py">BeamcontourFull</a></code>
- <code title="put /udl/beamcontour/{id}">client.beam_contours.<a href="./src/unifieddatalibrary/resources/beam_contours.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/beam_contour_update_params.py">params</a>) -> None</code>
- <code title="get /udl/beamcontour">client.beam_contours.<a href="./src/unifieddatalibrary/resources/beam_contours.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/beam_contour_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/beam_contour_list_response.py">BeamContourListResponse</a></code>
- <code title="delete /udl/beamcontour/{id}">client.beam_contours.<a href="./src/unifieddatalibrary/resources/beam_contours.py">delete</a>(id) -> None</code>
- <code title="get /udl/beamcontour/count">client.beam_contours.<a href="./src/unifieddatalibrary/resources/beam_contours.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/beam_contour_count_params.py">params</a>) -> str</code>
- <code title="post /udl/beamcontour/createBulk">client.beam_contours.<a href="./src/unifieddatalibrary/resources/beam_contours.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/beam_contour_create_bulk_params.py">params</a>) -> None</code>
- <code title="get /udl/beamcontour/queryhelp">client.beam_contours.<a href="./src/unifieddatalibrary/resources/beam_contours.py">query_help</a>() -> None</code>
- <code title="get /udl/beamcontour/tuple">client.beam_contours.<a href="./src/unifieddatalibrary/resources/beam_contours.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/beam_contour_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/beam_contour_tuple_response.py">BeamContourTupleResponse</a></code>

# Buses

Types:

```python
from unifieddatalibrary.types import (
    BusAbridged,
    BusFull,
    BusListResponse,
    BusCountResponse,
    BusTupleResponse,
)
```

Methods:

- <code title="post /udl/bus">client.buses.<a href="./src/unifieddatalibrary/resources/buses.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/bus_create_params.py">params</a>) -> None</code>
- <code title="get /udl/bus/{id}">client.buses.<a href="./src/unifieddatalibrary/resources/buses.py">retrieve</a>(id) -> <a href="./src/unifieddatalibrary/types/bus_full.py">BusFull</a></code>
- <code title="put /udl/bus/{id}">client.buses.<a href="./src/unifieddatalibrary/resources/buses.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/bus_update_params.py">params</a>) -> None</code>
- <code title="get /udl/bus">client.buses.<a href="./src/unifieddatalibrary/resources/buses.py">list</a>() -> <a href="./src/unifieddatalibrary/types/bus_list_response.py">BusListResponse</a></code>
- <code title="delete /udl/bus/{id}">client.buses.<a href="./src/unifieddatalibrary/resources/buses.py">delete</a>(id) -> None</code>
- <code title="get /udl/bus/count">client.buses.<a href="./src/unifieddatalibrary/resources/buses.py">count</a>() -> str</code>
- <code title="get /udl/bus/queryhelp">client.buses.<a href="./src/unifieddatalibrary/resources/buses.py">query_help</a>() -> None</code>
- <code title="get /udl/bus/tuple">client.buses.<a href="./src/unifieddatalibrary/resources/buses.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/bus_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/bus_tuple_response.py">BusTupleResponse</a></code>

# Channels

Types:

```python
from unifieddatalibrary.types import (
    ChannelAbridged,
    ChannelFull,
    ChannelListResponse,
    ChannelCountResponse,
    ChannelTupleResponse,
)
```

Methods:

- <code title="post /udl/channel">client.channels.<a href="./src/unifieddatalibrary/resources/channels.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/channel_create_params.py">params</a>) -> None</code>
- <code title="get /udl/channel/{id}">client.channels.<a href="./src/unifieddatalibrary/resources/channels.py">retrieve</a>(id) -> <a href="./src/unifieddatalibrary/types/channel_full.py">ChannelFull</a></code>
- <code title="put /udl/channel/{id}">client.channels.<a href="./src/unifieddatalibrary/resources/channels.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/channel_update_params.py">params</a>) -> None</code>
- <code title="get /udl/channel">client.channels.<a href="./src/unifieddatalibrary/resources/channels.py">list</a>() -> <a href="./src/unifieddatalibrary/types/channel_list_response.py">ChannelListResponse</a></code>
- <code title="delete /udl/channel/{id}">client.channels.<a href="./src/unifieddatalibrary/resources/channels.py">delete</a>(id) -> None</code>
- <code title="get /udl/channel/count">client.channels.<a href="./src/unifieddatalibrary/resources/channels.py">count</a>() -> str</code>
- <code title="get /udl/channel/queryhelp">client.channels.<a href="./src/unifieddatalibrary/resources/channels.py">queryhelp</a>() -> None</code>
- <code title="get /udl/channel/tuple">client.channels.<a href="./src/unifieddatalibrary/resources/channels.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/channel_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/channel_tuple_response.py">ChannelTupleResponse</a></code>

# CollectRequests

Types:

```python
from unifieddatalibrary.types import (
    CollectRequestAbridged,
    CollectRequestListResponse,
    CollectRequestCountResponse,
    CollectRequestTupleResponse,
)
```

Methods:

- <code title="post /udl/collectrequest">client.collect_requests.<a href="./src/unifieddatalibrary/resources/collect_requests/collect_requests.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/collect_request_create_params.py">params</a>) -> None</code>
- <code title="get /udl/collectrequest/{id}">client.collect_requests.<a href="./src/unifieddatalibrary/resources/collect_requests/collect_requests.py">retrieve</a>(id) -> <a href="./src/unifieddatalibrary/types/shared/collect_request_full.py">CollectRequestFull</a></code>
- <code title="get /udl/collectrequest">client.collect_requests.<a href="./src/unifieddatalibrary/resources/collect_requests/collect_requests.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/collect_request_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/collect_request_list_response.py">CollectRequestListResponse</a></code>
- <code title="get /udl/collectrequest/count">client.collect_requests.<a href="./src/unifieddatalibrary/resources/collect_requests/collect_requests.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/collect_request_count_params.py">params</a>) -> str</code>
- <code title="post /udl/collectrequest/createBulk">client.collect_requests.<a href="./src/unifieddatalibrary/resources/collect_requests/collect_requests.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/collect_request_create_bulk_params.py">params</a>) -> None</code>
- <code title="post /filedrop/udl-collectrequest">client.collect_requests.<a href="./src/unifieddatalibrary/resources/collect_requests/collect_requests.py">create_bulk_v2</a>(\*\*<a href="src/unifieddatalibrary/types/collect_request_create_bulk_v2_params.py">params</a>) -> None</code>
- <code title="get /udl/collectrequest/queryhelp">client.collect_requests.<a href="./src/unifieddatalibrary/resources/collect_requests/collect_requests.py">query_help</a>() -> None</code>
- <code title="get /udl/collectrequest/tuple">client.collect_requests.<a href="./src/unifieddatalibrary/resources/collect_requests/collect_requests.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/collect_request_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/collect_request_tuple_response.py">CollectRequestTupleResponse</a></code>

## History

Types:

```python
from unifieddatalibrary.types.collect_requests import HistoryListResponse, HistoryCountResponse
```

Methods:

- <code title="get /udl/collectrequest/history">client.collect_requests.history.<a href="./src/unifieddatalibrary/resources/collect_requests/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/collect_requests/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/collect_requests/history_list_response.py">HistoryListResponse</a></code>
- <code title="get /udl/collectrequest/history/aodr">client.collect_requests.history.<a href="./src/unifieddatalibrary/resources/collect_requests/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/collect_requests/history_aodr_params.py">params</a>) -> None</code>
- <code title="get /udl/collectrequest/history/count">client.collect_requests.history.<a href="./src/unifieddatalibrary/resources/collect_requests/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/collect_requests/history_count_params.py">params</a>) -> str</code>

# CollectResponses

Types:

```python
from unifieddatalibrary.types import (
    CollectResponseAbridged,
    CollectResponseListResponse,
    CollectResponseCountResponse,
)
```

Methods:

- <code title="post /udl/collectresponse">client.collect_responses.<a href="./src/unifieddatalibrary/resources/collect_responses/collect_responses.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/collect_response_create_params.py">params</a>) -> None</code>
- <code title="get /udl/collectresponse/{id}">client.collect_responses.<a href="./src/unifieddatalibrary/resources/collect_responses/collect_responses.py">retrieve</a>(id) -> <a href="./src/unifieddatalibrary/types/shared/collect_response_full.py">CollectResponseFull</a></code>
- <code title="get /udl/collectresponse">client.collect_responses.<a href="./src/unifieddatalibrary/resources/collect_responses/collect_responses.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/collect_response_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/collect_response_list_response.py">CollectResponseListResponse</a></code>
- <code title="get /udl/collectresponse/count">client.collect_responses.<a href="./src/unifieddatalibrary/resources/collect_responses/collect_responses.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/collect_response_count_params.py">params</a>) -> str</code>
- <code title="post /udl/collectresponse/createBulk">client.collect_responses.<a href="./src/unifieddatalibrary/resources/collect_responses/collect_responses.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/collect_response_create_bulk_params.py">params</a>) -> None</code>
- <code title="post /filedrop/udl-collectresponse">client.collect_responses.<a href="./src/unifieddatalibrary/resources/collect_responses/collect_responses.py">create_bulk_v2</a>(\*\*<a href="src/unifieddatalibrary/types/collect_response_create_bulk_v2_params.py">params</a>) -> None</code>
- <code title="get /udl/collectresponse/queryhelp">client.collect_responses.<a href="./src/unifieddatalibrary/resources/collect_responses/collect_responses.py">query_help</a>() -> None</code>

## History

Types:

```python
from unifieddatalibrary.types.collect_responses import HistoryListResponse, HistoryCountResponse
```

Methods:

- <code title="get /udl/collectresponse/history">client.collect_responses.history.<a href="./src/unifieddatalibrary/resources/collect_responses/history/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/collect_responses/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/collect_responses/history_list_response.py">HistoryListResponse</a></code>
- <code title="get /udl/collectresponse/history/count">client.collect_responses.history.<a href="./src/unifieddatalibrary/resources/collect_responses/history/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/collect_responses/history_count_params.py">params</a>) -> str</code>

### Aodr

Methods:

- <code title="get /udl/collectresponse/history/aodr">client.collect_responses.history.aodr.<a href="./src/unifieddatalibrary/resources/collect_responses/history/aodr.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/collect_responses/history/aodr_list_params.py">params</a>) -> None</code>

## Tuple

Types:

```python
from unifieddatalibrary.types.collect_responses import TupleListResponse
```

Methods:

- <code title="get /udl/collectresponse/tuple">client.collect_responses.tuple.<a href="./src/unifieddatalibrary/resources/collect_responses/tuple.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/collect_responses/tuple_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/collect_responses/tuple_list_response.py">TupleListResponse</a></code>

# Comm

Types:

```python
from unifieddatalibrary.types import (
    CommAbridged,
    CommFull,
    CommListResponse,
    CommCountResponse,
    CommTupleResponse,
)
```

Methods:

- <code title="post /udl/comm">client.comm.<a href="./src/unifieddatalibrary/resources/comm.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/comm_create_params.py">params</a>) -> None</code>
- <code title="get /udl/comm/{id}">client.comm.<a href="./src/unifieddatalibrary/resources/comm.py">retrieve</a>(id) -> <a href="./src/unifieddatalibrary/types/comm_full.py">CommFull</a></code>
- <code title="put /udl/comm/{id}">client.comm.<a href="./src/unifieddatalibrary/resources/comm.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/comm_update_params.py">params</a>) -> None</code>
- <code title="get /udl/comm">client.comm.<a href="./src/unifieddatalibrary/resources/comm.py">list</a>() -> <a href="./src/unifieddatalibrary/types/comm_list_response.py">CommListResponse</a></code>
- <code title="delete /udl/comm/{id}">client.comm.<a href="./src/unifieddatalibrary/resources/comm.py">delete</a>(id) -> None</code>
- <code title="get /udl/comm/count">client.comm.<a href="./src/unifieddatalibrary/resources/comm.py">count</a>() -> str</code>
- <code title="get /udl/comm/queryhelp">client.comm.<a href="./src/unifieddatalibrary/resources/comm.py">queryhelp</a>() -> None</code>
- <code title="get /udl/comm/tuple">client.comm.<a href="./src/unifieddatalibrary/resources/comm.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/comm_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/comm_tuple_response.py">CommTupleResponse</a></code>

# Conjunctions

Types:

```python
from unifieddatalibrary.types import (
    ConjunctionAbridged,
    ConjunctionFull,
    ConjunctionListResponse,
    ConjunctionCountResponse,
    ConjunctionGetHistoryResponse,
    ConjunctionTupleResponse,
)
```

Methods:

- <code title="get /udl/conjunction/{id}">client.conjunctions.<a href="./src/unifieddatalibrary/resources/conjunctions/conjunctions.py">retrieve</a>(id) -> <a href="./src/unifieddatalibrary/types/conjunction_full.py">ConjunctionFull</a></code>
- <code title="get /udl/conjunction">client.conjunctions.<a href="./src/unifieddatalibrary/resources/conjunctions/conjunctions.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/conjunction_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/conjunction_list_response.py">ConjunctionListResponse</a></code>
- <code title="get /udl/conjunction/count">client.conjunctions.<a href="./src/unifieddatalibrary/resources/conjunctions/conjunctions.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/conjunction_count_params.py">params</a>) -> str</code>
- <code title="post /filedrop/udl-conjunction">client.conjunctions.<a href="./src/unifieddatalibrary/resources/conjunctions/conjunctions.py">create_bulk_v2</a>(\*\*<a href="src/unifieddatalibrary/types/conjunction_create_bulk_v2_params.py">params</a>) -> None</code>
- <code title="post /udl/conjunction">client.conjunctions.<a href="./src/unifieddatalibrary/resources/conjunctions/conjunctions.py">create_udl</a>(\*\*<a href="src/unifieddatalibrary/types/conjunction_create_udl_params.py">params</a>) -> None</code>
- <code title="post /udl/conjunction/createBulk">client.conjunctions.<a href="./src/unifieddatalibrary/resources/conjunctions/conjunctions.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/conjunction_create_bulk_params.py">params</a>) -> None</code>
- <code title="get /udl/conjunction/history">client.conjunctions.<a href="./src/unifieddatalibrary/resources/conjunctions/conjunctions.py">get_history</a>(\*\*<a href="src/unifieddatalibrary/types/conjunction_get_history_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/conjunction_get_history_response.py">ConjunctionGetHistoryResponse</a></code>
- <code title="get /udl/conjunction/queryhelp">client.conjunctions.<a href="./src/unifieddatalibrary/resources/conjunctions/conjunctions.py">queryhelp</a>() -> None</code>
- <code title="get /udl/conjunction/tuple">client.conjunctions.<a href="./src/unifieddatalibrary/resources/conjunctions/conjunctions.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/conjunction_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/conjunction_tuple_response.py">ConjunctionTupleResponse</a></code>
- <code title="post /filedrop/cdms">client.conjunctions.<a href="./src/unifieddatalibrary/resources/conjunctions/conjunctions.py">upload_conjunction_data_message</a>(\*\*<a href="src/unifieddatalibrary/types/conjunction_upload_conjunction_data_message_params.py">params</a>) -> None</code>

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

# Aviationriskmanagement

Types:

```python
from unifieddatalibrary.types import (
    AviationriskmanagementRetrieveResponse,
    AviationriskmanagementCountResponse,
    AviationriskmanagementQueryResponse,
    AviationriskmanagementTupleResponse,
)
```

Methods:

- <code title="post /udl/aviationriskmanagement">client.aviationriskmanagement.<a href="./src/unifieddatalibrary/resources/aviationriskmanagement.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/aviationriskmanagement_create_params.py">params</a>) -> None</code>
- <code title="get /udl/aviationriskmanagement/{id}">client.aviationriskmanagement.<a href="./src/unifieddatalibrary/resources/aviationriskmanagement.py">retrieve</a>(id) -> <a href="./src/unifieddatalibrary/types/aviationriskmanagement_retrieve_response.py">AviationriskmanagementRetrieveResponse</a></code>
- <code title="put /udl/aviationriskmanagement/{id}">client.aviationriskmanagement.<a href="./src/unifieddatalibrary/resources/aviationriskmanagement.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/aviationriskmanagement_update_params.py">params</a>) -> None</code>
- <code title="delete /udl/aviationriskmanagement/{id}">client.aviationriskmanagement.<a href="./src/unifieddatalibrary/resources/aviationriskmanagement.py">delete</a>(id) -> None</code>
- <code title="get /udl/aviationriskmanagement/count">client.aviationriskmanagement.<a href="./src/unifieddatalibrary/resources/aviationriskmanagement.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/aviationriskmanagement_count_params.py">params</a>) -> str</code>
- <code title="post /udl/aviationriskmanagement/createBulk">client.aviationriskmanagement.<a href="./src/unifieddatalibrary/resources/aviationriskmanagement.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/aviationriskmanagement_create_bulk_params.py">params</a>) -> None</code>
- <code title="post /filedrop/udl-aviationriskmanagement">client.aviationriskmanagement.<a href="./src/unifieddatalibrary/resources/aviationriskmanagement.py">create_bulk_v2</a>(\*\*<a href="src/unifieddatalibrary/types/aviationriskmanagement_create_bulk_v2_params.py">params</a>) -> None</code>
- <code title="get /udl/aviationriskmanagement">client.aviationriskmanagement.<a href="./src/unifieddatalibrary/resources/aviationriskmanagement.py">query</a>(\*\*<a href="src/unifieddatalibrary/types/aviationriskmanagement_query_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/aviationriskmanagement_query_response.py">AviationriskmanagementQueryResponse</a></code>
- <code title="get /udl/aviationriskmanagement/queryhelp">client.aviationriskmanagement.<a href="./src/unifieddatalibrary/resources/aviationriskmanagement.py">query_help</a>() -> None</code>
- <code title="get /udl/aviationriskmanagement/tuple">client.aviationriskmanagement.<a href="./src/unifieddatalibrary/resources/aviationriskmanagement.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/aviationriskmanagement_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/aviationriskmanagement_tuple_response.py">AviationriskmanagementTupleResponse</a></code>

# Dropzone

Types:

```python
from unifieddatalibrary.types import (
    DropzoneRetrieveResponse,
    DropzoneCountResponse,
    DropzoneQueryResponse,
    DropzoneTupleResponse,
)
```

Methods:

- <code title="post /udl/dropzone">client.dropzone.<a href="./src/unifieddatalibrary/resources/dropzone.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/dropzone_create_params.py">params</a>) -> None</code>
- <code title="get /udl/dropzone/{id}">client.dropzone.<a href="./src/unifieddatalibrary/resources/dropzone.py">retrieve</a>(id) -> <a href="./src/unifieddatalibrary/types/dropzone_retrieve_response.py">DropzoneRetrieveResponse</a></code>
- <code title="put /udl/dropzone/{id}">client.dropzone.<a href="./src/unifieddatalibrary/resources/dropzone.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/dropzone_update_params.py">params</a>) -> None</code>
- <code title="delete /udl/dropzone/{id}">client.dropzone.<a href="./src/unifieddatalibrary/resources/dropzone.py">delete</a>(id) -> None</code>
- <code title="get /udl/dropzone/count">client.dropzone.<a href="./src/unifieddatalibrary/resources/dropzone.py">count</a>() -> str</code>
- <code title="post /udl/dropzone/createBulk">client.dropzone.<a href="./src/unifieddatalibrary/resources/dropzone.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/dropzone_create_bulk_params.py">params</a>) -> None</code>
- <code title="post /filedrop/udl-dropzone">client.dropzone.<a href="./src/unifieddatalibrary/resources/dropzone.py">create_bulk_v2</a>(\*\*<a href="src/unifieddatalibrary/types/dropzone_create_bulk_v2_params.py">params</a>) -> None</code>
- <code title="get /udl/dropzone">client.dropzone.<a href="./src/unifieddatalibrary/resources/dropzone.py">query</a>() -> <a href="./src/unifieddatalibrary/types/dropzone_query_response.py">DropzoneQueryResponse</a></code>
- <code title="get /udl/dropzone/queryhelp">client.dropzone.<a href="./src/unifieddatalibrary/resources/dropzone.py">query_help</a>() -> None</code>
- <code title="get /udl/dropzone/tuple">client.dropzone.<a href="./src/unifieddatalibrary/resources/dropzone.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/dropzone_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/dropzone_tuple_response.py">DropzoneTupleResponse</a></code>

# Emittergeolocation

Types:

```python
from unifieddatalibrary.types import (
    EmittergeolocationRetrieveResponse,
    EmittergeolocationCountResponse,
    EmittergeolocationQueryResponse,
    EmittergeolocationTupleResponse,
)
```

Methods:

- <code title="post /udl/emittergeolocation">client.emittergeolocation.<a href="./src/unifieddatalibrary/resources/emittergeolocation.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/emittergeolocation_create_params.py">params</a>) -> None</code>
- <code title="get /udl/emittergeolocation/{id}">client.emittergeolocation.<a href="./src/unifieddatalibrary/resources/emittergeolocation.py">retrieve</a>(id) -> <a href="./src/unifieddatalibrary/types/emittergeolocation_retrieve_response.py">EmittergeolocationRetrieveResponse</a></code>
- <code title="delete /udl/emittergeolocation/{id}">client.emittergeolocation.<a href="./src/unifieddatalibrary/resources/emittergeolocation.py">delete</a>(id) -> None</code>
- <code title="get /udl/emittergeolocation/count">client.emittergeolocation.<a href="./src/unifieddatalibrary/resources/emittergeolocation.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/emittergeolocation_count_params.py">params</a>) -> str</code>
- <code title="post /udl/emittergeolocation/createBulk">client.emittergeolocation.<a href="./src/unifieddatalibrary/resources/emittergeolocation.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/emittergeolocation_create_bulk_params.py">params</a>) -> None</code>
- <code title="post /filedrop/udl-emittergeolocation">client.emittergeolocation.<a href="./src/unifieddatalibrary/resources/emittergeolocation.py">create_bulk_v2</a>(\*\*<a href="src/unifieddatalibrary/types/emittergeolocation_create_bulk_v2_params.py">params</a>) -> None</code>
- <code title="get /udl/emittergeolocation">client.emittergeolocation.<a href="./src/unifieddatalibrary/resources/emittergeolocation.py">query</a>(\*\*<a href="src/unifieddatalibrary/types/emittergeolocation_query_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/emittergeolocation_query_response.py">EmittergeolocationQueryResponse</a></code>
- <code title="get /udl/emittergeolocation/queryhelp">client.emittergeolocation.<a href="./src/unifieddatalibrary/resources/emittergeolocation.py">query_help</a>() -> None</code>
- <code title="get /udl/emittergeolocation/tuple">client.emittergeolocation.<a href="./src/unifieddatalibrary/resources/emittergeolocation.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/emittergeolocation_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/emittergeolocation_tuple_response.py">EmittergeolocationTupleResponse</a></code>

# Featureassessment

Types:

```python
from unifieddatalibrary.types import (
    FeatureassessmentRetrieveResponse,
    FeatureassessmentCountResponse,
    FeatureassessmentQueryResponse,
    FeatureassessmentTupleResponse,
)
```

Methods:

- <code title="post /udl/featureassessment">client.featureassessment.<a href="./src/unifieddatalibrary/resources/featureassessment/featureassessment.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/featureassessment_create_params.py">params</a>) -> None</code>
- <code title="get /udl/featureassessment/{id}">client.featureassessment.<a href="./src/unifieddatalibrary/resources/featureassessment/featureassessment.py">retrieve</a>(id) -> <a href="./src/unifieddatalibrary/types/featureassessment_retrieve_response.py">FeatureassessmentRetrieveResponse</a></code>
- <code title="get /udl/featureassessment/count">client.featureassessment.<a href="./src/unifieddatalibrary/resources/featureassessment/featureassessment.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/featureassessment_count_params.py">params</a>) -> str</code>
- <code title="post /udl/featureassessment/createBulk">client.featureassessment.<a href="./src/unifieddatalibrary/resources/featureassessment/featureassessment.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/featureassessment_create_bulk_params.py">params</a>) -> None</code>
- <code title="post /filedrop/udl-featureassessment">client.featureassessment.<a href="./src/unifieddatalibrary/resources/featureassessment/featureassessment.py">create_bulk_v2</a>(\*\*<a href="src/unifieddatalibrary/types/featureassessment_create_bulk_v2_params.py">params</a>) -> None</code>
- <code title="get /udl/featureassessment">client.featureassessment.<a href="./src/unifieddatalibrary/resources/featureassessment/featureassessment.py">query</a>(\*\*<a href="src/unifieddatalibrary/types/featureassessment_query_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/featureassessment_query_response.py">FeatureassessmentQueryResponse</a></code>
- <code title="get /udl/featureassessment/queryhelp">client.featureassessment.<a href="./src/unifieddatalibrary/resources/featureassessment/featureassessment.py">query_help</a>() -> None</code>
- <code title="get /udl/featureassessment/tuple">client.featureassessment.<a href="./src/unifieddatalibrary/resources/featureassessment/featureassessment.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/featureassessment_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/featureassessment_tuple_response.py">FeatureassessmentTupleResponse</a></code>

## History

Types:

```python
from unifieddatalibrary.types.featureassessment import HistoryCountResponse, HistoryQueryResponse
```

Methods:

- <code title="get /udl/featureassessment/history/count">client.featureassessment.history.<a href="./src/unifieddatalibrary/resources/featureassessment/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/featureassessment/history_count_params.py">params</a>) -> str</code>
- <code title="get /udl/featureassessment/history">client.featureassessment.history.<a href="./src/unifieddatalibrary/resources/featureassessment/history.py">query</a>(\*\*<a href="src/unifieddatalibrary/types/featureassessment/history_query_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/featureassessment/history_query_response.py">HistoryQueryResponse</a></code>
- <code title="get /udl/featureassessment/history/aodr">client.featureassessment.history.<a href="./src/unifieddatalibrary/resources/featureassessment/history.py">write_aodr</a>(\*\*<a href="src/unifieddatalibrary/types/featureassessment/history_write_aodr_params.py">params</a>) -> None</code>

# Globalatmosphericmodel

Types:

```python
from unifieddatalibrary.types import (
    GlobalatmosphericmodelRetrieveResponse,
    GlobalatmosphericmodelCountResponse,
    GlobalatmosphericmodelQueryResponse,
    GlobalatmosphericmodelTupleResponse,
)
```

Methods:

- <code title="get /udl/globalatmosphericmodel/{id}">client.globalatmosphericmodel.<a href="./src/unifieddatalibrary/resources/globalatmosphericmodel/globalatmosphericmodel.py">retrieve</a>(id) -> <a href="./src/unifieddatalibrary/types/globalatmosphericmodel_retrieve_response.py">GlobalatmosphericmodelRetrieveResponse</a></code>
- <code title="get /udl/globalatmosphericmodel/count">client.globalatmosphericmodel.<a href="./src/unifieddatalibrary/resources/globalatmosphericmodel/globalatmosphericmodel.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/globalatmosphericmodel_count_params.py">params</a>) -> str</code>
- <code title="post /filedrop/udl-globalatmosphericmodel">client.globalatmosphericmodel.<a href="./src/unifieddatalibrary/resources/globalatmosphericmodel/globalatmosphericmodel.py">create_bulk_v2</a>(\*\*<a href="src/unifieddatalibrary/types/globalatmosphericmodel_create_bulk_v2_params.py">params</a>) -> None</code>
- <code title="get /udl/globalatmosphericmodel/getFile/{id}">client.globalatmosphericmodel.<a href="./src/unifieddatalibrary/resources/globalatmosphericmodel/globalatmosphericmodel.py">get_file</a>(id) -> BinaryAPIResponse</code>
- <code title="get /udl/globalatmosphericmodel">client.globalatmosphericmodel.<a href="./src/unifieddatalibrary/resources/globalatmosphericmodel/globalatmosphericmodel.py">query</a>(\*\*<a href="src/unifieddatalibrary/types/globalatmosphericmodel_query_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/globalatmosphericmodel_query_response.py">GlobalatmosphericmodelQueryResponse</a></code>
- <code title="get /udl/globalatmosphericmodel/queryhelp">client.globalatmosphericmodel.<a href="./src/unifieddatalibrary/resources/globalatmosphericmodel/globalatmosphericmodel.py">query_help</a>() -> None</code>
- <code title="get /udl/globalatmosphericmodel/tuple">client.globalatmosphericmodel.<a href="./src/unifieddatalibrary/resources/globalatmosphericmodel/globalatmosphericmodel.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/globalatmosphericmodel_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/globalatmosphericmodel_tuple_response.py">GlobalatmosphericmodelTupleResponse</a></code>

## History

Types:

```python
from unifieddatalibrary.types.globalatmosphericmodel import (
    HistoryCountResponse,
    HistoryQueryResponse,
)
```

Methods:

- <code title="get /udl/globalatmosphericmodel/history/count">client.globalatmosphericmodel.history.<a href="./src/unifieddatalibrary/resources/globalatmosphericmodel/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/globalatmosphericmodel/history_count_params.py">params</a>) -> str</code>
- <code title="get /udl/globalatmosphericmodel/history">client.globalatmosphericmodel.history.<a href="./src/unifieddatalibrary/resources/globalatmosphericmodel/history.py">query</a>(\*\*<a href="src/unifieddatalibrary/types/globalatmosphericmodel/history_query_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/globalatmosphericmodel/history_query_response.py">HistoryQueryResponse</a></code>
- <code title="get /udl/globalatmosphericmodel/history/aodr">client.globalatmosphericmodel.history.<a href="./src/unifieddatalibrary/resources/globalatmosphericmodel/history.py">write_aodr</a>(\*\*<a href="src/unifieddatalibrary/types/globalatmosphericmodel/history_write_aodr_params.py">params</a>) -> None</code>

# Routestats

Types:

```python
from unifieddatalibrary.types import (
    RoutestatRetrieveResponse,
    RoutestatCountResponse,
    RoutestatQueryResponse,
    RoutestatTupleResponse,
)
```

Methods:

- <code title="post /udl/routestats">client.routestats.<a href="./src/unifieddatalibrary/resources/routestats.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/routestat_create_params.py">params</a>) -> None</code>
- <code title="get /udl/routestats/{id}">client.routestats.<a href="./src/unifieddatalibrary/resources/routestats.py">retrieve</a>(id) -> <a href="./src/unifieddatalibrary/types/routestat_retrieve_response.py">RoutestatRetrieveResponse</a></code>
- <code title="put /udl/routestats/{id}">client.routestats.<a href="./src/unifieddatalibrary/resources/routestats.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/routestat_update_params.py">params</a>) -> None</code>
- <code title="delete /udl/routestats/{id}">client.routestats.<a href="./src/unifieddatalibrary/resources/routestats.py">delete</a>(id) -> None</code>
- <code title="get /udl/routestats/count">client.routestats.<a href="./src/unifieddatalibrary/resources/routestats.py">count</a>() -> str</code>
- <code title="post /udl/routestats/createBulk">client.routestats.<a href="./src/unifieddatalibrary/resources/routestats.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/routestat_create_bulk_params.py">params</a>) -> None</code>
- <code title="post /filedrop/udl-routestats">client.routestats.<a href="./src/unifieddatalibrary/resources/routestats.py">create_bulk_v2</a>(\*\*<a href="src/unifieddatalibrary/types/routestat_create_bulk_v2_params.py">params</a>) -> None</code>
- <code title="get /udl/routestats">client.routestats.<a href="./src/unifieddatalibrary/resources/routestats.py">query</a>() -> <a href="./src/unifieddatalibrary/types/routestat_query_response.py">RoutestatQueryResponse</a></code>
- <code title="get /udl/routestats/queryhelp">client.routestats.<a href="./src/unifieddatalibrary/resources/routestats.py">query_help</a>() -> None</code>
- <code title="get /udl/routestats/tuple">client.routestats.<a href="./src/unifieddatalibrary/resources/routestats.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/routestat_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/routestat_tuple_response.py">RoutestatTupleResponse</a></code>

# Countries

Types:

```python
from unifieddatalibrary.types import (
    CountryAbridged,
    CountryFull,
    CountryListResponse,
    CountryCountResponse,
    CountryTupleResponse,
)
```

Methods:

- <code title="post /udl/country">client.countries.<a href="./src/unifieddatalibrary/resources/countries.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/country_create_params.py">params</a>) -> None</code>
- <code title="get /udl/country/{code}">client.countries.<a href="./src/unifieddatalibrary/resources/countries.py">retrieve</a>(code) -> <a href="./src/unifieddatalibrary/types/country_full.py">CountryFull</a></code>
- <code title="put /udl/country/{code}">client.countries.<a href="./src/unifieddatalibrary/resources/countries.py">update</a>(path_code, \*\*<a href="src/unifieddatalibrary/types/country_update_params.py">params</a>) -> None</code>
- <code title="get /udl/country">client.countries.<a href="./src/unifieddatalibrary/resources/countries.py">list</a>() -> <a href="./src/unifieddatalibrary/types/country_list_response.py">CountryListResponse</a></code>
- <code title="delete /udl/country/{code}">client.countries.<a href="./src/unifieddatalibrary/resources/countries.py">delete</a>(code) -> None</code>
- <code title="get /udl/country/count">client.countries.<a href="./src/unifieddatalibrary/resources/countries.py">count</a>() -> str</code>
- <code title="get /udl/country/queryhelp">client.countries.<a href="./src/unifieddatalibrary/resources/countries.py">queryhelp</a>() -> None</code>
- <code title="get /udl/country/tuple">client.countries.<a href="./src/unifieddatalibrary/resources/countries.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/country_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/country_tuple_response.py">CountryTupleResponse</a></code>

# Crew

Types:

```python
from unifieddatalibrary.types import (
    CrewAbridged,
    CrewFull,
    CrewListResponse,
    CrewCountResponse,
    CrewTupleResponse,
)
```

Methods:

- <code title="post /udl/crew">client.crew.<a href="./src/unifieddatalibrary/resources/crew.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/crew_create_params.py">params</a>) -> None</code>
- <code title="get /udl/crew/{id}">client.crew.<a href="./src/unifieddatalibrary/resources/crew.py">retrieve</a>(id) -> <a href="./src/unifieddatalibrary/types/crew_full.py">CrewFull</a></code>
- <code title="put /udl/crew/{id}">client.crew.<a href="./src/unifieddatalibrary/resources/crew.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/crew_update_params.py">params</a>) -> None</code>
- <code title="get /udl/crew">client.crew.<a href="./src/unifieddatalibrary/resources/crew.py">list</a>() -> <a href="./src/unifieddatalibrary/types/crew_list_response.py">CrewListResponse</a></code>
- <code title="get /udl/crew/count">client.crew.<a href="./src/unifieddatalibrary/resources/crew.py">count</a>() -> str</code>
- <code title="post /filedrop/udl-crew">client.crew.<a href="./src/unifieddatalibrary/resources/crew.py">create_bulk_v2</a>(\*\*<a href="src/unifieddatalibrary/types/crew_create_bulk_v2_params.py">params</a>) -> None</code>
- <code title="get /udl/crew/queryhelp">client.crew.<a href="./src/unifieddatalibrary/resources/crew.py">queryhelp</a>() -> None</code>
- <code title="get /udl/crew/tuple">client.crew.<a href="./src/unifieddatalibrary/resources/crew.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/crew_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/crew_tuple_response.py">CrewTupleResponse</a></code>

# Diffofarrival

Types:

```python
from unifieddatalibrary.types import DiffofarrivalTupleResponse
```

Methods:

- <code title="get /udl/diffofarrival/{id}">client.diffofarrival.<a href="./src/unifieddatalibrary/resources/diffofarrival/diffofarrival.py">retrieve</a>(id) -> <a href="./src/unifieddatalibrary/types/tdoa_fdoa/diffofarrival_full.py">DiffofarrivalFull</a></code>
- <code title="post /filedrop/udl-diffofarrival">client.diffofarrival.<a href="./src/unifieddatalibrary/resources/diffofarrival/diffofarrival.py">create_bulk_v2</a>(\*\*<a href="src/unifieddatalibrary/types/diffofarrival_create_bulk_v2_params.py">params</a>) -> None</code>
- <code title="get /udl/diffofarrival/queryhelp">client.diffofarrival.<a href="./src/unifieddatalibrary/resources/diffofarrival/diffofarrival.py">queryhelp</a>() -> None</code>
- <code title="get /udl/diffofarrival/tuple">client.diffofarrival.<a href="./src/unifieddatalibrary/resources/diffofarrival/diffofarrival.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/diffofarrival_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/diffofarrival_tuple_response.py">DiffofarrivalTupleResponse</a></code>

## History

Types:

```python
from unifieddatalibrary.types.diffofarrival import HistoryCountResponse
```

Methods:

- <code title="get /udl/diffofarrival/history/count">client.diffofarrival.history.<a href="./src/unifieddatalibrary/resources/diffofarrival/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/diffofarrival/history_count_params.py">params</a>) -> str</code>

# DiplomaticClearance

Types:

```python
from unifieddatalibrary.types import (
    DiplomaticClearanceListResponse,
    DiplomaticClearanceCountResponse,
    DiplomaticClearanceTupleResponse,
)
```

Methods:

- <code title="post /udl/diplomaticclearance">client.diplomatic_clearance.<a href="./src/unifieddatalibrary/resources/diplomatic_clearance/diplomatic_clearance.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/diplomatic_clearance_create_params.py">params</a>) -> None</code>
- <code title="get /udl/diplomaticclearance/{id}">client.diplomatic_clearance.<a href="./src/unifieddatalibrary/resources/diplomatic_clearance/diplomatic_clearance.py">retrieve</a>(id) -> <a href="./src/unifieddatalibrary/types/air_operations/diplomaticclearance_full.py">DiplomaticclearanceFull</a></code>
- <code title="put /udl/diplomaticclearance/{id}">client.diplomatic_clearance.<a href="./src/unifieddatalibrary/resources/diplomatic_clearance/diplomatic_clearance.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/diplomatic_clearance_update_params.py">params</a>) -> None</code>
- <code title="get /udl/diplomaticclearance">client.diplomatic_clearance.<a href="./src/unifieddatalibrary/resources/diplomatic_clearance/diplomatic_clearance.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/diplomatic_clearance_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/diplomatic_clearance_list_response.py">DiplomaticClearanceListResponse</a></code>
- <code title="delete /udl/diplomaticclearance/{id}">client.diplomatic_clearance.<a href="./src/unifieddatalibrary/resources/diplomatic_clearance/diplomatic_clearance.py">delete</a>(id) -> None</code>
- <code title="get /udl/diplomaticclearance/count">client.diplomatic_clearance.<a href="./src/unifieddatalibrary/resources/diplomatic_clearance/diplomatic_clearance.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/diplomatic_clearance_count_params.py">params</a>) -> str</code>
- <code title="post /udl/diplomaticclearance/createBulk">client.diplomatic_clearance.<a href="./src/unifieddatalibrary/resources/diplomatic_clearance/diplomatic_clearance.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/diplomatic_clearance_create_bulk_params.py">params</a>) -> None</code>
- <code title="get /udl/diplomaticclearance/queryhelp">client.diplomatic_clearance.<a href="./src/unifieddatalibrary/resources/diplomatic_clearance/diplomatic_clearance.py">queryhelp</a>() -> None</code>
- <code title="get /udl/diplomaticclearance/tuple">client.diplomatic_clearance.<a href="./src/unifieddatalibrary/resources/diplomatic_clearance/diplomatic_clearance.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/diplomatic_clearance_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/diplomatic_clearance_tuple_response.py">DiplomaticClearanceTupleResponse</a></code>

## History

Types:

```python
from unifieddatalibrary.types.diplomatic_clearance import HistoryListResponse, HistoryCountResponse
```

Methods:

- <code title="get /udl/diplomaticclearance/history">client.diplomatic_clearance.history.<a href="./src/unifieddatalibrary/resources/diplomatic_clearance/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/diplomatic_clearance/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/diplomatic_clearance/history_list_response.py">HistoryListResponse</a></code>
- <code title="get /udl/diplomaticclearance/history/aodr">client.diplomatic_clearance.history.<a href="./src/unifieddatalibrary/resources/diplomatic_clearance/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/diplomatic_clearance/history_aodr_params.py">params</a>) -> None</code>
- <code title="get /udl/diplomaticclearance/history/count">client.diplomatic_clearance.history.<a href="./src/unifieddatalibrary/resources/diplomatic_clearance/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/diplomatic_clearance/history_count_params.py">params</a>) -> str</code>

## Country

Types:

```python
from unifieddatalibrary.types.diplomatic_clearance import (
    CountryRetrieveResponse,
    CountryListResponse,
    CountryCountResponse,
    CountryTupleResponse,
)
```

Methods:

- <code title="post /udl/diplomaticclearancecountry">client.diplomatic_clearance.country.<a href="./src/unifieddatalibrary/resources/diplomatic_clearance/country.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/diplomatic_clearance/country_create_params.py">params</a>) -> None</code>
- <code title="get /udl/diplomaticclearancecountry/{id}">client.diplomatic_clearance.country.<a href="./src/unifieddatalibrary/resources/diplomatic_clearance/country.py">retrieve</a>(id) -> <a href="./src/unifieddatalibrary/types/diplomatic_clearance/country_retrieve_response.py">CountryRetrieveResponse</a></code>
- <code title="put /udl/diplomaticclearancecountry/{id}">client.diplomatic_clearance.country.<a href="./src/unifieddatalibrary/resources/diplomatic_clearance/country.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/diplomatic_clearance/country_update_params.py">params</a>) -> None</code>
- <code title="get /udl/diplomaticclearancecountry">client.diplomatic_clearance.country.<a href="./src/unifieddatalibrary/resources/diplomatic_clearance/country.py">list</a>() -> <a href="./src/unifieddatalibrary/types/diplomatic_clearance/country_list_response.py">CountryListResponse</a></code>
- <code title="delete /udl/diplomaticclearancecountry/{id}">client.diplomatic_clearance.country.<a href="./src/unifieddatalibrary/resources/diplomatic_clearance/country.py">delete</a>(id) -> None</code>
- <code title="get /udl/diplomaticclearancecountry/count">client.diplomatic_clearance.country.<a href="./src/unifieddatalibrary/resources/diplomatic_clearance/country.py">count</a>() -> str</code>
- <code title="post /udl/diplomaticclearancecountry/createBulk">client.diplomatic_clearance.country.<a href="./src/unifieddatalibrary/resources/diplomatic_clearance/country.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/diplomatic_clearance/country_create_bulk_params.py">params</a>) -> None</code>
- <code title="post /filedrop/udl-diplomaticclearancecountry">client.diplomatic_clearance.country.<a href="./src/unifieddatalibrary/resources/diplomatic_clearance/country.py">create_bulk_v2</a>(\*\*<a href="src/unifieddatalibrary/types/diplomatic_clearance/country_create_bulk_v2_params.py">params</a>) -> None</code>
- <code title="get /udl/diplomaticclearancecountry/queryhelp">client.diplomatic_clearance.country.<a href="./src/unifieddatalibrary/resources/diplomatic_clearance/country.py">query_help</a>() -> None</code>
- <code title="get /udl/diplomaticclearancecountry/tuple">client.diplomatic_clearance.country.<a href="./src/unifieddatalibrary/resources/diplomatic_clearance/country.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/diplomatic_clearance/country_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/diplomatic_clearance/country_tuple_response.py">CountryTupleResponse</a></code>

# DriftHistory

Types:

```python
from unifieddatalibrary.types import (
    DriftHistoryListResponse,
    DriftHistoryCountResponse,
    DriftHistoryTupleResponse,
)
```

Methods:

- <code title="get /udl/drifthistory/{id}">client.drift_history.<a href="./src/unifieddatalibrary/resources/drift_history.py">retrieve</a>(id) -> <a href="./src/unifieddatalibrary/types/shared/drift_history.py">DriftHistory</a></code>
- <code title="get /udl/drifthistory">client.drift_history.<a href="./src/unifieddatalibrary/resources/drift_history.py">list</a>() -> <a href="./src/unifieddatalibrary/types/drift_history_list_response.py">DriftHistoryListResponse</a></code>
- <code title="get /udl/drifthistory/count">client.drift_history.<a href="./src/unifieddatalibrary/resources/drift_history.py">count</a>() -> str</code>
- <code title="get /udl/drifthistory/queryhelp">client.drift_history.<a href="./src/unifieddatalibrary/resources/drift_history.py">queryhelp</a>() -> None</code>
- <code title="get /udl/drifthistory/tuple">client.drift_history.<a href="./src/unifieddatalibrary/resources/drift_history.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/drift_history_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/drift_history_tuple_response.py">DriftHistoryTupleResponse</a></code>

# Ecpsdr

Methods:

- <code title="post /filedrop/udl-ecpsdr">client.ecpsdr.<a href="./src/unifieddatalibrary/resources/ecpsdr.py">create_bulk_v2</a>(\*\*<a href="src/unifieddatalibrary/types/ecpsdr_create_bulk_v2_params.py">params</a>) -> None</code>

# EffectRequests

Types:

```python
from unifieddatalibrary.types import (
    EffectRequestRetrieveResponse,
    EffectRequestListResponse,
    EffectRequestCountResponse,
    EffectRequestTupleResponse,
)
```

Methods:

- <code title="post /udl/effectrequest">client.effect_requests.<a href="./src/unifieddatalibrary/resources/effect_requests/effect_requests.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/effect_request_create_params.py">params</a>) -> None</code>
- <code title="get /udl/effectrequest/{id}">client.effect_requests.<a href="./src/unifieddatalibrary/resources/effect_requests/effect_requests.py">retrieve</a>(id) -> <a href="./src/unifieddatalibrary/types/effect_request_retrieve_response.py">EffectRequestRetrieveResponse</a></code>
- <code title="get /udl/effectrequest">client.effect_requests.<a href="./src/unifieddatalibrary/resources/effect_requests/effect_requests.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/effect_request_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/effect_request_list_response.py">EffectRequestListResponse</a></code>
- <code title="get /udl/effectrequest/count">client.effect_requests.<a href="./src/unifieddatalibrary/resources/effect_requests/effect_requests.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/effect_request_count_params.py">params</a>) -> str</code>
- <code title="post /udl/effectrequest/createBulk">client.effect_requests.<a href="./src/unifieddatalibrary/resources/effect_requests/effect_requests.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/effect_request_create_bulk_params.py">params</a>) -> None</code>
- <code title="post /filedrop/udl-effectrequest">client.effect_requests.<a href="./src/unifieddatalibrary/resources/effect_requests/effect_requests.py">create_bulk_v2</a>(\*\*<a href="src/unifieddatalibrary/types/effect_request_create_bulk_v2_params.py">params</a>) -> None</code>
- <code title="get /udl/effectrequest/queryhelp">client.effect_requests.<a href="./src/unifieddatalibrary/resources/effect_requests/effect_requests.py">query_help</a>() -> None</code>
- <code title="get /udl/effectrequest/tuple">client.effect_requests.<a href="./src/unifieddatalibrary/resources/effect_requests/effect_requests.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/effect_request_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/effect_request_tuple_response.py">EffectRequestTupleResponse</a></code>

## History

Types:

```python
from unifieddatalibrary.types.effect_requests import HistoryListResponse, HistoryCountResponse
```

Methods:

- <code title="get /udl/effectrequest/history">client.effect_requests.history.<a href="./src/unifieddatalibrary/resources/effect_requests/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/effect_requests/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/effect_requests/history_list_response.py">HistoryListResponse</a></code>
- <code title="get /udl/effectrequest/history/aodr">client.effect_requests.history.<a href="./src/unifieddatalibrary/resources/effect_requests/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/effect_requests/history_aodr_params.py">params</a>) -> None</code>
- <code title="get /udl/effectrequest/history/count">client.effect_requests.history.<a href="./src/unifieddatalibrary/resources/effect_requests/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/effect_requests/history_count_params.py">params</a>) -> str</code>

# EffectResponses

Types:

```python
from unifieddatalibrary.types import (
    EffectResponseRetrieveResponse,
    EffectResponseListResponse,
    EffectResponseCountResponse,
    EffectResponseTupleResponse,
)
```

Methods:

- <code title="post /udl/effectresponse">client.effect_responses.<a href="./src/unifieddatalibrary/resources/effect_responses/effect_responses.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/effect_response_create_params.py">params</a>) -> None</code>
- <code title="get /udl/effectresponse/{id}">client.effect_responses.<a href="./src/unifieddatalibrary/resources/effect_responses/effect_responses.py">retrieve</a>(id) -> <a href="./src/unifieddatalibrary/types/effect_response_retrieve_response.py">EffectResponseRetrieveResponse</a></code>
- <code title="get /udl/effectresponse">client.effect_responses.<a href="./src/unifieddatalibrary/resources/effect_responses/effect_responses.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/effect_response_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/effect_response_list_response.py">EffectResponseListResponse</a></code>
- <code title="get /udl/effectresponse/count">client.effect_responses.<a href="./src/unifieddatalibrary/resources/effect_responses/effect_responses.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/effect_response_count_params.py">params</a>) -> str</code>
- <code title="post /udl/effectresponse/createBulk">client.effect_responses.<a href="./src/unifieddatalibrary/resources/effect_responses/effect_responses.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/effect_response_create_bulk_params.py">params</a>) -> None</code>
- <code title="post /filedrop/udl-effectresponse">client.effect_responses.<a href="./src/unifieddatalibrary/resources/effect_responses/effect_responses.py">create_bulk_v2</a>(\*\*<a href="src/unifieddatalibrary/types/effect_response_create_bulk_v2_params.py">params</a>) -> None</code>
- <code title="get /udl/effectresponse/queryhelp">client.effect_responses.<a href="./src/unifieddatalibrary/resources/effect_responses/effect_responses.py">query_help</a>() -> None</code>
- <code title="get /udl/effectresponse/tuple">client.effect_responses.<a href="./src/unifieddatalibrary/resources/effect_responses/effect_responses.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/effect_response_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/effect_response_tuple_response.py">EffectResponseTupleResponse</a></code>

## History

Types:

```python
from unifieddatalibrary.types.effect_responses import HistoryListResponse, HistoryCountResponse
```

Methods:

- <code title="get /udl/effectresponse/history">client.effect_responses.history.<a href="./src/unifieddatalibrary/resources/effect_responses/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/effect_responses/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/effect_responses/history_list_response.py">HistoryListResponse</a></code>
- <code title="get /udl/effectresponse/history/aodr">client.effect_responses.history.<a href="./src/unifieddatalibrary/resources/effect_responses/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/effect_responses/history_aodr_params.py">params</a>) -> None</code>
- <code title="get /udl/effectresponse/history/count">client.effect_responses.history.<a href="./src/unifieddatalibrary/resources/effect_responses/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/effect_responses/history_count_params.py">params</a>) -> str</code>

# Elsets

Types:

```python
from unifieddatalibrary.types import (
    Elset,
    ElsetIngest,
    ElsetAbridged,
    ElsetListResponse,
    ElsetCountResponse,
    ElsetTupleResponse,
)
```

Methods:

- <code title="post /udl/elset">client.elsets.<a href="./src/unifieddatalibrary/resources/elsets/elsets.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/elset_create_params.py">params</a>) -> None</code>
- <code title="get /udl/elset/{id}">client.elsets.<a href="./src/unifieddatalibrary/resources/elsets/elsets.py">retrieve</a>(id) -> <a href="./src/unifieddatalibrary/types/elset.py">Elset</a></code>
- <code title="get /udl/elset">client.elsets.<a href="./src/unifieddatalibrary/resources/elsets/elsets.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/elset_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/elset_list_response.py">ElsetListResponse</a></code>
- <code title="get /udl/elset/count">client.elsets.<a href="./src/unifieddatalibrary/resources/elsets/elsets.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/elset_count_params.py">params</a>) -> str</code>
- <code title="post /udl/elset/createBulk">client.elsets.<a href="./src/unifieddatalibrary/resources/elsets/elsets.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/elset_create_bulk_params.py">params</a>) -> None</code>
- <code title="post /udl/elset/createBulkFromTLE">client.elsets.<a href="./src/unifieddatalibrary/resources/elsets/elsets.py">create_bulk_from_tle</a>(\*\*<a href="src/unifieddatalibrary/types/elset_create_bulk_from_tle_params.py">params</a>) -> None</code>
- <code title="post /filedrop/udl-elset">client.elsets.<a href="./src/unifieddatalibrary/resources/elsets/elsets.py">create_bulk_v2</a>(\*\*<a href="src/unifieddatalibrary/types/elset_create_bulk_v2_params.py">params</a>) -> None</code>
- <code title="get /udl/currentelset/queryhelp">client.elsets.<a href="./src/unifieddatalibrary/resources/elsets/elsets.py">query_current_elset_help</a>() -> None</code>
- <code title="get /udl/elset/queryhelp">client.elsets.<a href="./src/unifieddatalibrary/resources/elsets/elsets.py">queryhelp</a>() -> None</code>
- <code title="get /udl/elset/tuple">client.elsets.<a href="./src/unifieddatalibrary/resources/elsets/elsets.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/elset_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/elset_tuple_response.py">ElsetTupleResponse</a></code>

## Current

Types:

```python
from unifieddatalibrary.types.elsets import CurrentListResponse, CurrentTupleResponse
```

Methods:

- <code title="get /udl/elset/current">client.elsets.current.<a href="./src/unifieddatalibrary/resources/elsets/current.py">list</a>() -> <a href="./src/unifieddatalibrary/types/elsets/current_list_response.py">CurrentListResponse</a></code>
- <code title="get /udl/elset/current/tuple">client.elsets.current.<a href="./src/unifieddatalibrary/resources/elsets/current.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/elsets/current_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/elsets/current_tuple_response.py">CurrentTupleResponse</a></code>

## History

Types:

```python
from unifieddatalibrary.types.elsets import HistoryListResponse, HistoryCountResponse
```

Methods:

- <code title="get /udl/elset/history">client.elsets.history.<a href="./src/unifieddatalibrary/resources/elsets/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/elsets/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/elsets/history_list_response.py">HistoryListResponse</a></code>
- <code title="get /udl/elset/history/aodr">client.elsets.history.<a href="./src/unifieddatalibrary/resources/elsets/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/elsets/history_aodr_params.py">params</a>) -> None</code>
- <code title="get /udl/elset/history/count">client.elsets.history.<a href="./src/unifieddatalibrary/resources/elsets/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/elsets/history_count_params.py">params</a>) -> str</code>

# EngineDetails

Types:

```python
from unifieddatalibrary.types import EngineDetailsFull
```

Methods:

- <code title="post /udl/enginedetails">client.engine_details.<a href="./src/unifieddatalibrary/resources/engine_details.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/engine_detail_create_params.py">params</a>) -> None</code>
- <code title="get /udl/enginedetails/{id}">client.engine_details.<a href="./src/unifieddatalibrary/resources/engine_details.py">retrieve</a>(id) -> <a href="./src/unifieddatalibrary/types/engine_details_full.py">EngineDetailsFull</a></code>
- <code title="put /udl/enginedetails/{id}">client.engine_details.<a href="./src/unifieddatalibrary/resources/engine_details.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/engine_detail_update_params.py">params</a>) -> None</code>
- <code title="delete /udl/enginedetails/{id}">client.engine_details.<a href="./src/unifieddatalibrary/resources/engine_details.py">delete</a>(id) -> None</code>

# Enginedetails

Types:

```python
from unifieddatalibrary.types import EngineDetailsAbridged, EnginedetailListResponse
```

Methods:

- <code title="get /udl/enginedetails">client.enginedetails.<a href="./src/unifieddatalibrary/resources/enginedetails.py">list</a>() -> <a href="./src/unifieddatalibrary/types/enginedetail_list_response.py">EnginedetailListResponse</a></code>

# Engines

Types:

```python
from unifieddatalibrary.types import (
    Engine,
    EngineAbridged,
    EngineListResponse,
    EngineCountResponse,
    EngineTupleResponse,
)
```

Methods:

- <code title="post /udl/engine">client.engines.<a href="./src/unifieddatalibrary/resources/engines.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/engine_create_params.py">params</a>) -> None</code>
- <code title="get /udl/engine/{id}">client.engines.<a href="./src/unifieddatalibrary/resources/engines.py">retrieve</a>(id) -> <a href="./src/unifieddatalibrary/types/engine.py">Engine</a></code>
- <code title="put /udl/engine/{id}">client.engines.<a href="./src/unifieddatalibrary/resources/engines.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/engine_update_params.py">params</a>) -> None</code>
- <code title="get /udl/engine">client.engines.<a href="./src/unifieddatalibrary/resources/engines.py">list</a>() -> <a href="./src/unifieddatalibrary/types/engine_list_response.py">EngineListResponse</a></code>
- <code title="delete /udl/engine/{id}">client.engines.<a href="./src/unifieddatalibrary/resources/engines.py">delete</a>(id) -> None</code>
- <code title="get /udl/engine/count">client.engines.<a href="./src/unifieddatalibrary/resources/engines.py">count</a>() -> str</code>
- <code title="get /udl/engine/queryhelp">client.engines.<a href="./src/unifieddatalibrary/resources/engines.py">queryhelp</a>() -> None</code>
- <code title="get /udl/engine/tuple">client.engines.<a href="./src/unifieddatalibrary/resources/engines.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/engine_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/engine_tuple_response.py">EngineTupleResponse</a></code>

# Entities

Types:

```python
from unifieddatalibrary.types import (
    EntityAbridged,
    EntityFull,
    EntityIngest,
    EntityListResponse,
    EntityCountResponse,
    EntityGetAllTypesResponse,
    EntityTupleResponse,
)
```

Methods:

- <code title="post /udl/entity">client.entities.<a href="./src/unifieddatalibrary/resources/entities.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/entity_create_params.py">params</a>) -> None</code>
- <code title="get /udl/entity/{id}">client.entities.<a href="./src/unifieddatalibrary/resources/entities.py">retrieve</a>(id) -> <a href="./src/unifieddatalibrary/types/entity_full.py">EntityFull</a></code>
- <code title="put /udl/entity/{id}">client.entities.<a href="./src/unifieddatalibrary/resources/entities.py">update</a>(id, \*\*<a href="src/unifieddatalibrary/types/entity_update_params.py">params</a>) -> None</code>
- <code title="get /udl/entity">client.entities.<a href="./src/unifieddatalibrary/resources/entities.py">list</a>() -> <a href="./src/unifieddatalibrary/types/entity_list_response.py">EntityListResponse</a></code>
- <code title="delete /udl/entity/{id}">client.entities.<a href="./src/unifieddatalibrary/resources/entities.py">delete</a>(id) -> None</code>
- <code title="get /udl/entity/count">client.entities.<a href="./src/unifieddatalibrary/resources/entities.py">count</a>() -> str</code>
- <code title="get /udl/entity/getAllTypes">client.entities.<a href="./src/unifieddatalibrary/resources/entities.py">get_all_types</a>() -> <a href="./src/unifieddatalibrary/types/entity_get_all_types_response.py">EntityGetAllTypesResponse</a></code>
- <code title="get /udl/entity/queryhelp">client.entities.<a href="./src/unifieddatalibrary/resources/entities.py">query_help</a>() -> None</code>
- <code title="get /udl/entity/tuple">client.entities.<a href="./src/unifieddatalibrary/resources/entities.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/entity_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/entity_tuple_response.py">EntityTupleResponse</a></code>

# EoObservations

Types:

```python
from unifieddatalibrary.types import (
    EoObservationAbridged,
    EoObservationListResponse,
    EoObservationCountResponse,
)
```

Methods:

- <code title="post /udl/eoobservation">client.eo_observations.<a href="./src/unifieddatalibrary/resources/eo_observations/eo_observations.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/eo_observation_create_params.py">params</a>) -> None</code>
- <code title="get /udl/eoobservation">client.eo_observations.<a href="./src/unifieddatalibrary/resources/eo_observations/eo_observations.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/eo_observation_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/eo_observation_list_response.py">EoObservationListResponse</a></code>
- <code title="get /udl/eoobservation/count">client.eo_observations.<a href="./src/unifieddatalibrary/resources/eo_observations/eo_observations.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/eo_observation_count_params.py">params</a>) -> str</code>
- <code title="post /udl/eoobservation/createBulk">client.eo_observations.<a href="./src/unifieddatalibrary/resources/eo_observations/eo_observations.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/eo_observation_create_bulk_params.py">params</a>) -> None</code>
- <code title="post /filedrop/udl-eo">client.eo_observations.<a href="./src/unifieddatalibrary/resources/eo_observations/eo_observations.py">create_bulk_v2</a>(\*\*<a href="src/unifieddatalibrary/types/eo_observation_create_bulk_v2_params.py">params</a>) -> None</code>

## History

Types:

```python
from unifieddatalibrary.types.eo_observations import (
    EoObservationFull,
    HistoryListResponse,
    HistoryCountResponse,
)
```

Methods:

- <code title="get /udl/eoobservation/history">client.eo_observations.history.<a href="./src/unifieddatalibrary/resources/eo_observations/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/eo_observations/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/eo_observations/history_list_response.py">HistoryListResponse</a></code>
- <code title="get /udl/eoobservation/history/aodr">client.eo_observations.history.<a href="./src/unifieddatalibrary/resources/eo_observations/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/eo_observations/history_aodr_params.py">params</a>) -> None</code>
- <code title="get /udl/eoobservation/history/count">client.eo_observations.history.<a href="./src/unifieddatalibrary/resources/eo_observations/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/eo_observations/history_count_params.py">params</a>) -> str</code>

# Eoobservations

Types:

```python
from unifieddatalibrary.types import EoobservationTupleResponse
```

Methods:

- <code title="get /udl/eoobservation/{id}">client.eoobservations.<a href="./src/unifieddatalibrary/resources/eoobservations.py">retrieve</a>(id) -> <a href="./src/unifieddatalibrary/types/eo_observations/eo_observation_full.py">EoObservationFull</a></code>
- <code title="get /udl/eoobservation/queryhelp">client.eoobservations.<a href="./src/unifieddatalibrary/resources/eoobservations.py">queryhelp</a>() -> None</code>
- <code title="get /udl/eoobservation/tuple">client.eoobservations.<a href="./src/unifieddatalibrary/resources/eoobservations.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/eoobservation_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/eoobservation_tuple_response.py">EoobservationTupleResponse</a></code>

# Eop

Types:

```python
from unifieddatalibrary.types import (
    EopAbridged,
    EopListResponse,
    EopCountResponse,
    EopListTupleResponse,
)
```

Methods:

- <code title="post /udl/eop">client.eop.<a href="./src/unifieddatalibrary/resources/eop/eop.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/eop_create_params.py">params</a>) -> None</code>
- <code title="get /udl/eop/{id}">client.eop.<a href="./src/unifieddatalibrary/resources/eop/eop.py">retrieve</a>(id) -> <a href="./src/unifieddatalibrary/types/shared/eop_full.py">EopFull</a></code>
- <code title="put /udl/eop/{id}">client.eop.<a href="./src/unifieddatalibrary/resources/eop/eop.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/eop_update_params.py">params</a>) -> None</code>
- <code title="get /udl/eop">client.eop.<a href="./src/unifieddatalibrary/resources/eop/eop.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/eop_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/eop_list_response.py">EopListResponse</a></code>
- <code title="delete /udl/eop/{id}">client.eop.<a href="./src/unifieddatalibrary/resources/eop/eop.py">delete</a>(id) -> None</code>
- <code title="get /udl/eop/count">client.eop.<a href="./src/unifieddatalibrary/resources/eop/eop.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/eop_count_params.py">params</a>) -> str</code>
- <code title="get /udl/eop/tuple">client.eop.<a href="./src/unifieddatalibrary/resources/eop/eop.py">list_tuple</a>(\*\*<a href="src/unifieddatalibrary/types/eop_list_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/eop_list_tuple_response.py">EopListTupleResponse</a></code>
- <code title="get /udl/eop/queryhelp">client.eop.<a href="./src/unifieddatalibrary/resources/eop/eop.py">queryhelp</a>() -> None</code>

## History

Types:

```python
from unifieddatalibrary.types.eop import HistoryListResponse, HistoryCountResponse
```

Methods:

- <code title="get /udl/eop/history">client.eop.history.<a href="./src/unifieddatalibrary/resources/eop/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/eop/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/eop/history_list_response.py">HistoryListResponse</a></code>
- <code title="get /udl/eop/history/aodr">client.eop.history.<a href="./src/unifieddatalibrary/resources/eop/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/eop/history_aodr_params.py">params</a>) -> None</code>
- <code title="get /udl/eop/history/count">client.eop.history.<a href="./src/unifieddatalibrary/resources/eop/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/eop/history_count_params.py">params</a>) -> str</code>

# Ephemeris

Types:

```python
from unifieddatalibrary.types import (
    EphemerisAbridged,
    EphemerisListResponse,
    EphemerisCountResponse,
    EphemerisTupleResponse,
)
```

Methods:

- <code title="get /udl/ephemeris">client.ephemeris.<a href="./src/unifieddatalibrary/resources/ephemeris/ephemeris.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/ephemeris_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/ephemeris_list_response.py">EphemerisListResponse</a></code>
- <code title="get /udl/ephemeris/count">client.ephemeris.<a href="./src/unifieddatalibrary/resources/ephemeris/ephemeris.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/ephemeris_count_params.py">params</a>) -> str</code>
- <code title="post /filedrop/udl-ephset">client.ephemeris.<a href="./src/unifieddatalibrary/resources/ephemeris/ephemeris.py">create_bulk_v2</a>(\*\*<a href="src/unifieddatalibrary/types/ephemeris_create_bulk_v2_params.py">params</a>) -> None</code>
- <code title="post /filedrop/ephem">client.ephemeris.<a href="./src/unifieddatalibrary/resources/ephemeris/ephemeris.py">file_upload</a>(\*\*<a href="src/unifieddatalibrary/types/ephemeris_file_upload_params.py">params</a>) -> None</code>
- <code title="get /udl/ephemeris/queryhelp">client.ephemeris.<a href="./src/unifieddatalibrary/resources/ephemeris/ephemeris.py">queryhelp</a>() -> None</code>
- <code title="get /udl/ephemeris/tuple">client.ephemeris.<a href="./src/unifieddatalibrary/resources/ephemeris/ephemeris.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/ephemeris_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/ephemeris_tuple_response.py">EphemerisTupleResponse</a></code>

## AttitudeData

Types:

```python
from unifieddatalibrary.types.ephemeris import (
    AttitudeDataAbridged,
    AttitudeDataListResponse,
    AttitudeDataCountResponse,
)
```

Methods:

- <code title="get /udl/attitudedata">client.ephemeris.attitude_data.<a href="./src/unifieddatalibrary/resources/ephemeris/attitude_data/attitude_data.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/ephemeris/attitude_data_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/ephemeris/attitude_data_list_response.py">AttitudeDataListResponse</a></code>
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
from unifieddatalibrary.types.ephemeris import HistoryListResponse, HistoryCountResponse
```

Methods:

- <code title="get /udl/ephemeris/history">client.ephemeris.history.<a href="./src/unifieddatalibrary/resources/ephemeris/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/ephemeris/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/ephemeris/history_list_response.py">HistoryListResponse</a></code>
- <code title="get /udl/ephemeris/history/aodr">client.ephemeris.history.<a href="./src/unifieddatalibrary/resources/ephemeris/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/ephemeris/history_aodr_params.py">params</a>) -> None</code>
- <code title="get /udl/ephemeris/history/count">client.ephemeris.history.<a href="./src/unifieddatalibrary/resources/ephemeris/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/ephemeris/history_count_params.py">params</a>) -> str</code>

# EphemerisSets

Types:

```python
from unifieddatalibrary.types import (
    EphemerisSet,
    EphemerisSetAbridged,
    EphemerisSetListResponse,
    EphemerisSetCountResponse,
    EphemerisSetTupleResponse,
)
```

Methods:

- <code title="post /udl/ephemerisset">client.ephemeris_sets.<a href="./src/unifieddatalibrary/resources/ephemeris_sets/ephemeris_sets.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/ephemeris_set_create_params.py">params</a>) -> None</code>
- <code title="get /udl/ephemerisset/{id}">client.ephemeris_sets.<a href="./src/unifieddatalibrary/resources/ephemeris_sets/ephemeris_sets.py">retrieve</a>(id) -> <a href="./src/unifieddatalibrary/types/ephemeris_set.py">EphemerisSet</a></code>
- <code title="get /udl/ephemerisset">client.ephemeris_sets.<a href="./src/unifieddatalibrary/resources/ephemeris_sets/ephemeris_sets.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/ephemeris_set_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/ephemeris_set_list_response.py">EphemerisSetListResponse</a></code>
- <code title="get /udl/ephemerisset/count">client.ephemeris_sets.<a href="./src/unifieddatalibrary/resources/ephemeris_sets/ephemeris_sets.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/ephemeris_set_count_params.py">params</a>) -> str</code>
- <code title="get /udl/ephemerisset/getFile/{id}">client.ephemeris_sets.<a href="./src/unifieddatalibrary/resources/ephemeris_sets/ephemeris_sets.py">file_retrieve</a>(id) -> BinaryAPIResponse</code>
- <code title="get /udl/ephemerisset/queryhelp">client.ephemeris_sets.<a href="./src/unifieddatalibrary/resources/ephemeris_sets/ephemeris_sets.py">queryhelp</a>() -> None</code>
- <code title="get /udl/ephemerisset/tuple">client.ephemeris_sets.<a href="./src/unifieddatalibrary/resources/ephemeris_sets/ephemeris_sets.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/ephemeris_set_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/ephemeris_set_tuple_response.py">EphemerisSetTupleResponse</a></code>

## History

Types:

```python
from unifieddatalibrary.types.ephemeris_sets import HistoryListResponse, HistoryCountResponse
```

Methods:

- <code title="get /udl/ephemerisset/history">client.ephemeris_sets.history.<a href="./src/unifieddatalibrary/resources/ephemeris_sets/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/ephemeris_sets/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/ephemeris_sets/history_list_response.py">HistoryListResponse</a></code>
- <code title="get /udl/ephemerisset/history/aodr">client.ephemeris_sets.history.<a href="./src/unifieddatalibrary/resources/ephemeris_sets/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/ephemeris_sets/history_aodr_params.py">params</a>) -> None</code>
- <code title="get /udl/ephemerisset/history/count">client.ephemeris_sets.history.<a href="./src/unifieddatalibrary/resources/ephemeris_sets/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/ephemeris_sets/history_count_params.py">params</a>) -> str</code>

# Equipment

Types:

```python
from unifieddatalibrary.types import (
    EquipmentAbridged,
    EquipmentFull,
    EquipmentListResponse,
    EquipmentCountResponse,
    EquipmentTupleResponse,
)
```

Methods:

- <code title="post /udl/equipment">client.equipment.<a href="./src/unifieddatalibrary/resources/equipment.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/equipment_create_params.py">params</a>) -> None</code>
- <code title="get /udl/equipment/{id}">client.equipment.<a href="./src/unifieddatalibrary/resources/equipment.py">retrieve</a>(id) -> <a href="./src/unifieddatalibrary/types/equipment_full.py">EquipmentFull</a></code>
- <code title="put /udl/equipment/{id}">client.equipment.<a href="./src/unifieddatalibrary/resources/equipment.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/equipment_update_params.py">params</a>) -> None</code>
- <code title="get /udl/equipment">client.equipment.<a href="./src/unifieddatalibrary/resources/equipment.py">list</a>() -> <a href="./src/unifieddatalibrary/types/equipment_list_response.py">EquipmentListResponse</a></code>
- <code title="delete /udl/equipment/{id}">client.equipment.<a href="./src/unifieddatalibrary/resources/equipment.py">delete</a>(id) -> None</code>
- <code title="get /udl/equipment/count">client.equipment.<a href="./src/unifieddatalibrary/resources/equipment.py">count</a>() -> str</code>
- <code title="post /udl/equipment/createBulk">client.equipment.<a href="./src/unifieddatalibrary/resources/equipment.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/equipment_create_bulk_params.py">params</a>) -> None</code>
- <code title="get /udl/equipment/queryhelp">client.equipment.<a href="./src/unifieddatalibrary/resources/equipment.py">query_help</a>() -> None</code>
- <code title="get /udl/equipment/tuple">client.equipment.<a href="./src/unifieddatalibrary/resources/equipment.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/equipment_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/equipment_tuple_response.py">EquipmentTupleResponse</a></code>

# Equipmentremarks

Types:

```python
from unifieddatalibrary.types import (
    EquipmentRemarkAbridged,
    EquipmentRemarkFull,
    EquipmentremarkListResponse,
    EquipmentremarkCountResponse,
    EquipmentremarkTupleResponse,
)
```

Methods:

- <code title="post /udl/equipmentremark">client.equipmentremarks.<a href="./src/unifieddatalibrary/resources/equipmentremarks.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/equipmentremark_create_params.py">params</a>) -> None</code>
- <code title="get /udl/equipmentremark/{id}">client.equipmentremarks.<a href="./src/unifieddatalibrary/resources/equipmentremarks.py">retrieve</a>(id) -> <a href="./src/unifieddatalibrary/types/equipment_remark_full.py">EquipmentRemarkFull</a></code>
- <code title="get /udl/equipmentremark">client.equipmentremarks.<a href="./src/unifieddatalibrary/resources/equipmentremarks.py">list</a>() -> <a href="./src/unifieddatalibrary/types/equipmentremark_list_response.py">EquipmentremarkListResponse</a></code>
- <code title="get /udl/equipmentremark/count">client.equipmentremarks.<a href="./src/unifieddatalibrary/resources/equipmentremarks.py">count</a>() -> str</code>
- <code title="post /udl/equipmentremark/createBulk">client.equipmentremarks.<a href="./src/unifieddatalibrary/resources/equipmentremarks.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/equipmentremark_create_bulk_params.py">params</a>) -> None</code>
- <code title="get /udl/equipmentremark/queryhelp">client.equipmentremarks.<a href="./src/unifieddatalibrary/resources/equipmentremarks.py">query_help</a>() -> None</code>
- <code title="get /udl/equipmentremark/tuple">client.equipmentremarks.<a href="./src/unifieddatalibrary/resources/equipmentremarks.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/equipmentremark_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/equipmentremark_tuple_response.py">EquipmentremarkTupleResponse</a></code>

# Evac

Types:

```python
from unifieddatalibrary.types import EvacAbridged, EvacListResponse, EvacCountResponse
```

Methods:

- <code title="post /udl/evac">client.evac.<a href="./src/unifieddatalibrary/resources/evac/evac.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/evac_create_params.py">params</a>) -> None</code>
- <code title="get /udl/evac/{id}">client.evac.<a href="./src/unifieddatalibrary/resources/evac/evac.py">retrieve</a>(id) -> <a href="./src/unifieddatalibrary/types/shared/evac_full.py">EvacFull</a></code>
- <code title="get /udl/evac">client.evac.<a href="./src/unifieddatalibrary/resources/evac/evac.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/evac_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/evac_list_response.py">EvacListResponse</a></code>
- <code title="get /udl/evac/count">client.evac.<a href="./src/unifieddatalibrary/resources/evac/evac.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/evac_count_params.py">params</a>) -> str</code>
- <code title="post /udl/evac/createBulk">client.evac.<a href="./src/unifieddatalibrary/resources/evac/evac.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/evac_create_bulk_params.py">params</a>) -> None</code>
- <code title="post /filedrop/udl-evac">client.evac.<a href="./src/unifieddatalibrary/resources/evac/evac.py">create_bulk_v2</a>(\*\*<a href="src/unifieddatalibrary/types/evac_create_bulk_v2_params.py">params</a>) -> None</code>
- <code title="get /udl/evac/queryhelp">client.evac.<a href="./src/unifieddatalibrary/resources/evac/evac.py">query_help</a>() -> None</code>

## History

Types:

```python
from unifieddatalibrary.types.evac import HistoryListResponse, HistoryCountResponse
```

Methods:

- <code title="get /udl/evac/history">client.evac.history.<a href="./src/unifieddatalibrary/resources/evac/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/evac/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/evac/history_list_response.py">HistoryListResponse</a></code>
- <code title="get /udl/evac/history/count">client.evac.history.<a href="./src/unifieddatalibrary/resources/evac/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/evac/history_count_params.py">params</a>) -> str</code>

## Tuple

Types:

```python
from unifieddatalibrary.types.evac import TupleListResponse
```

Methods:

- <code title="get /udl/evac/tuple">client.evac.tuple.<a href="./src/unifieddatalibrary/resources/evac/tuple.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/evac/tuple_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/evac/tuple_list_response.py">TupleListResponse</a></code>

# EventEvolution

Types:

```python
from unifieddatalibrary.types import (
    EventEvolutionListResponse,
    EventEvolutionCountResponse,
    EventEvolutionTupleResponse,
)
```

Methods:

- <code title="post /udl/eventevolution">client.event_evolution.<a href="./src/unifieddatalibrary/resources/event_evolution/event_evolution.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/event_evolution_create_params.py">params</a>) -> None</code>
- <code title="get /udl/eventevolution/{id}">client.event_evolution.<a href="./src/unifieddatalibrary/resources/event_evolution/event_evolution.py">retrieve</a>(id) -> <a href="./src/unifieddatalibrary/types/shared/event_evolution_full.py">EventEvolutionFull</a></code>
- <code title="get /udl/eventevolution">client.event_evolution.<a href="./src/unifieddatalibrary/resources/event_evolution/event_evolution.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/event_evolution_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/event_evolution_list_response.py">EventEvolutionListResponse</a></code>
- <code title="get /udl/eventevolution/count">client.event_evolution.<a href="./src/unifieddatalibrary/resources/event_evolution/event_evolution.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/event_evolution_count_params.py">params</a>) -> str</code>
- <code title="post /udl/eventevolution/createBulk">client.event_evolution.<a href="./src/unifieddatalibrary/resources/event_evolution/event_evolution.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/event_evolution_create_bulk_params.py">params</a>) -> None</code>
- <code title="post /filedrop/udl-eventevolution">client.event_evolution.<a href="./src/unifieddatalibrary/resources/event_evolution/event_evolution.py">create_bulk_v2</a>(\*\*<a href="src/unifieddatalibrary/types/event_evolution_create_bulk_v2_params.py">params</a>) -> None</code>
- <code title="get /udl/eventevolution/queryhelp">client.event_evolution.<a href="./src/unifieddatalibrary/resources/event_evolution/event_evolution.py">queryhelp</a>() -> None</code>
- <code title="get /udl/eventevolution/tuple">client.event_evolution.<a href="./src/unifieddatalibrary/resources/event_evolution/event_evolution.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/event_evolution_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/event_evolution_tuple_response.py">EventEvolutionTupleResponse</a></code>

## History

Types:

```python
from unifieddatalibrary.types.event_evolution import HistoryListResponse, HistoryCountResponse
```

Methods:

- <code title="get /udl/eventevolution/history">client.event_evolution.history.<a href="./src/unifieddatalibrary/resources/event_evolution/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/event_evolution/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/event_evolution/history_list_response.py">HistoryListResponse</a></code>
- <code title="get /udl/eventevolution/history/aodr">client.event_evolution.history.<a href="./src/unifieddatalibrary/resources/event_evolution/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/event_evolution/history_aodr_params.py">params</a>) -> None</code>
- <code title="get /udl/eventevolution/history/count">client.event_evolution.history.<a href="./src/unifieddatalibrary/resources/event_evolution/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/event_evolution/history_count_params.py">params</a>) -> str</code>

# Flightplan

Types:

```python
from unifieddatalibrary.types import (
    FlightPlanAbridged,
    FlightplanListResponse,
    FlightplanCountResponse,
    FlightplanTupleResponse,
)
```

Methods:

- <code title="post /udl/flightplan">client.flightplan.<a href="./src/unifieddatalibrary/resources/flightplan.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/flightplan_create_params.py">params</a>) -> None</code>
- <code title="get /udl/flightplan/{id}">client.flightplan.<a href="./src/unifieddatalibrary/resources/flightplan.py">retrieve</a>(id) -> <a href="./src/unifieddatalibrary/types/shared/flight_plan_full.py">FlightPlanFull</a></code>
- <code title="put /udl/flightplan/{id}">client.flightplan.<a href="./src/unifieddatalibrary/resources/flightplan.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/flightplan_update_params.py">params</a>) -> None</code>
- <code title="get /udl/flightplan">client.flightplan.<a href="./src/unifieddatalibrary/resources/flightplan.py">list</a>() -> <a href="./src/unifieddatalibrary/types/flightplan_list_response.py">FlightplanListResponse</a></code>
- <code title="delete /udl/flightplan/{id}">client.flightplan.<a href="./src/unifieddatalibrary/resources/flightplan.py">delete</a>(id) -> None</code>
- <code title="get /udl/flightplan/count">client.flightplan.<a href="./src/unifieddatalibrary/resources/flightplan.py">count</a>() -> str</code>
- <code title="post /filedrop/udl-flightplan">client.flightplan.<a href="./src/unifieddatalibrary/resources/flightplan.py">create_bulk_v2</a>(\*\*<a href="src/unifieddatalibrary/types/flightplan_create_bulk_v2_params.py">params</a>) -> None</code>
- <code title="get /udl/flightplan/queryhelp">client.flightplan.<a href="./src/unifieddatalibrary/resources/flightplan.py">queryhelp</a>() -> None</code>
- <code title="get /udl/flightplan/tuple">client.flightplan.<a href="./src/unifieddatalibrary/resources/flightplan.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/flightplan_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/flightplan_tuple_response.py">FlightplanTupleResponse</a></code>

# Geostatus

Types:

```python
from unifieddatalibrary.types import (
    GeostatusListResponse,
    GeostatusCountResponse,
    GeostatusTupleResponse,
)
```

Methods:

- <code title="post /udl/geostatus">client.geostatus.<a href="./src/unifieddatalibrary/resources/geostatus.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/geostatus_create_params.py">params</a>) -> None</code>
- <code title="get /udl/geostatus">client.geostatus.<a href="./src/unifieddatalibrary/resources/geostatus.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/geostatus_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/geostatus_list_response.py">GeostatusListResponse</a></code>
- <code title="get /udl/geostatus/count">client.geostatus.<a href="./src/unifieddatalibrary/resources/geostatus.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/geostatus_count_params.py">params</a>) -> str</code>
- <code title="post /udl/geostatus/createBulk">client.geostatus.<a href="./src/unifieddatalibrary/resources/geostatus.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/geostatus_create_bulk_params.py">params</a>) -> None</code>
- <code title="get /udl/geostatus/{id}">client.geostatus.<a href="./src/unifieddatalibrary/resources/geostatus.py">get</a>(id) -> <a href="./src/unifieddatalibrary/types/udl/geostatus/geo_status_full.py">GeoStatusFull</a></code>
- <code title="get /udl/geostatus/queryhelp">client.geostatus.<a href="./src/unifieddatalibrary/resources/geostatus.py">queryhelp</a>() -> None</code>
- <code title="get /udl/geostatus/tuple">client.geostatus.<a href="./src/unifieddatalibrary/resources/geostatus.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/geostatus_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/geostatus_tuple_response.py">GeostatusTupleResponse</a></code>

# Gnssobservationset

Types:

```python
from unifieddatalibrary.types import (
    GnssobservationsetListResponse,
    GnssobservationsetCountResponse,
    GnssobservationsetTupleResponse,
)
```

Methods:

- <code title="get /udl/gnssobservationset">client.gnssobservationset.<a href="./src/unifieddatalibrary/resources/gnssobservationset.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/gnssobservationset_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/gnssobservationset_list_response.py">GnssobservationsetListResponse</a></code>
- <code title="get /udl/gnssobservationset/count">client.gnssobservationset.<a href="./src/unifieddatalibrary/resources/gnssobservationset.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/gnssobservationset_count_params.py">params</a>) -> str</code>
- <code title="post /udl/gnssobservationset/createBulk">client.gnssobservationset.<a href="./src/unifieddatalibrary/resources/gnssobservationset.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/gnssobservationset_create_bulk_params.py">params</a>) -> None</code>
- <code title="post /filedrop/udl-gnssobset">client.gnssobservationset.<a href="./src/unifieddatalibrary/resources/gnssobservationset.py">create_bulk_v2</a>(\*\*<a href="src/unifieddatalibrary/types/gnssobservationset_create_bulk_v2_params.py">params</a>) -> None</code>
- <code title="get /udl/gnssobservationset/queryhelp">client.gnssobservationset.<a href="./src/unifieddatalibrary/resources/gnssobservationset.py">queryhelp</a>() -> None</code>
- <code title="get /udl/gnssobservationset/tuple">client.gnssobservationset.<a href="./src/unifieddatalibrary/resources/gnssobservationset.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/gnssobservationset_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/gnssobservationset_tuple_response.py">GnssobservationsetTupleResponse</a></code>

# Gnssrawif

Types:

```python
from unifieddatalibrary.types import (
    GnssrawifListResponse,
    GnssrawifCountResponse,
    GnssrawifTupleResponse,
)
```

Methods:

- <code title="get /udl/gnssrawif">client.gnssrawif.<a href="./src/unifieddatalibrary/resources/gnssrawif.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/gnssrawif_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/gnssrawif_list_response.py">GnssrawifListResponse</a></code>
- <code title="get /udl/gnssrawif/count">client.gnssrawif.<a href="./src/unifieddatalibrary/resources/gnssrawif.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/gnssrawif_count_params.py">params</a>) -> str</code>
- <code title="get /udl/gnssrawif/getFile/{id}">client.gnssrawif.<a href="./src/unifieddatalibrary/resources/gnssrawif.py">file_get</a>(id) -> BinaryAPIResponse</code>
- <code title="get /udl/gnssrawif/{id}">client.gnssrawif.<a href="./src/unifieddatalibrary/resources/gnssrawif.py">get</a>(id) -> <a href="./src/unifieddatalibrary/types/udl/gnssrawif/gnss_raw_if_full.py">GnssRawIfFull</a></code>
- <code title="get /udl/gnssrawif/queryhelp">client.gnssrawif.<a href="./src/unifieddatalibrary/resources/gnssrawif.py">queryhelp</a>() -> None</code>
- <code title="get /udl/gnssrawif/tuple">client.gnssrawif.<a href="./src/unifieddatalibrary/resources/gnssrawif.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/gnssrawif_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/gnssrawif_tuple_response.py">GnssrawifTupleResponse</a></code>
- <code title="post /filedrop/udl-gnssrawif">client.gnssrawif.<a href="./src/unifieddatalibrary/resources/gnssrawif.py">upload_zip</a>(\*\*<a href="src/unifieddatalibrary/types/gnssrawif_upload_zip_params.py">params</a>) -> None</code>

# GroundImagery

Methods:

- <code title="get /udl/groundimagery/history/aodr">client.ground_imagery.<a href="./src/unifieddatalibrary/resources/ground_imagery/ground_imagery.py">history_aodr</a>(\*\*<a href="src/unifieddatalibrary/types/ground_imagery_history_aodr_params.py">params</a>) -> None</code>
- <code title="post /filedrop/udl-groundimagery">client.ground_imagery.<a href="./src/unifieddatalibrary/resources/ground_imagery/ground_imagery.py">upload_zip</a>(\*\*<a href="src/unifieddatalibrary/types/ground_imagery_upload_zip_params.py">params</a>) -> None</code>

## History

Types:

```python
from unifieddatalibrary.types.ground_imagery import HistoryCountResponse, HistoryQueryResponse
```

Methods:

- <code title="get /udl/groundimagery/history/count">client.ground_imagery.history.<a href="./src/unifieddatalibrary/resources/ground_imagery/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/ground_imagery/history_count_params.py">params</a>) -> str</code>
- <code title="get /udl/groundimagery/history">client.ground_imagery.history.<a href="./src/unifieddatalibrary/resources/ground_imagery/history.py">query</a>(\*\*<a href="src/unifieddatalibrary/types/ground_imagery/history_query_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/ground_imagery/history_query_response.py">HistoryQueryResponse</a></code>

# Groundimagery

Types:

```python
from unifieddatalibrary.types import (
    GroundimageryListResponse,
    GroundimageryCountResponse,
    GroundimageryTupleResponse,
)
```

Methods:

- <code title="post /udl/groundimagery">client.groundimagery.<a href="./src/unifieddatalibrary/resources/groundimagery.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/groundimagery_create_params.py">params</a>) -> None</code>
- <code title="get /udl/groundimagery">client.groundimagery.<a href="./src/unifieddatalibrary/resources/groundimagery.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/groundimagery_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/groundimagery_list_response.py">GroundimageryListResponse</a></code>
- <code title="get /udl/groundimagery/count">client.groundimagery.<a href="./src/unifieddatalibrary/resources/groundimagery.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/groundimagery_count_params.py">params</a>) -> str</code>
- <code title="get /udl/groundimagery/{id}">client.groundimagery.<a href="./src/unifieddatalibrary/resources/groundimagery.py">get</a>(id) -> <a href="./src/unifieddatalibrary/types/udl/groundimagery/ground_imagery_full.py">GroundImageryFull</a></code>
- <code title="get /udl/groundimagery/getFile/{id}">client.groundimagery.<a href="./src/unifieddatalibrary/resources/groundimagery.py">get_file</a>(id) -> BinaryAPIResponse</code>
- <code title="get /udl/groundimagery/queryhelp">client.groundimagery.<a href="./src/unifieddatalibrary/resources/groundimagery.py">queryhelp</a>() -> None</code>
- <code title="get /udl/groundimagery/tuple">client.groundimagery.<a href="./src/unifieddatalibrary/resources/groundimagery.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/groundimagery_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/groundimagery_tuple_response.py">GroundimageryTupleResponse</a></code>

# H3geo

Types:

```python
from unifieddatalibrary.types import (
    H3geoListResponse,
    H3geoCountResponse,
    H3geoGetResponse,
    H3geoTupleResponse,
)
```

Methods:

- <code title="post /udl/h3geo">client.h3geo.<a href="./src/unifieddatalibrary/resources/h3geo/h3geo.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/h3geo_create_params.py">params</a>) -> None</code>
- <code title="get /udl/h3geo">client.h3geo.<a href="./src/unifieddatalibrary/resources/h3geo/h3geo.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/h3geo_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/h3geo_list_response.py">H3geoListResponse</a></code>
- <code title="get /udl/h3geo/count">client.h3geo.<a href="./src/unifieddatalibrary/resources/h3geo/h3geo.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/h3geo_count_params.py">params</a>) -> str</code>
- <code title="get /udl/h3geo/{id}">client.h3geo.<a href="./src/unifieddatalibrary/resources/h3geo/h3geo.py">get</a>(id) -> <a href="./src/unifieddatalibrary/types/h3geo_get_response.py">H3geoGetResponse</a></code>
- <code title="get /udl/h3geo/queryhelp">client.h3geo.<a href="./src/unifieddatalibrary/resources/h3geo/h3geo.py">queryhelp</a>() -> None</code>
- <code title="get /udl/h3geo/tuple">client.h3geo.<a href="./src/unifieddatalibrary/resources/h3geo/h3geo.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/h3geo_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/h3geo_tuple_response.py">H3geoTupleResponse</a></code>

## History

Types:

```python
from unifieddatalibrary.types.h3geo import HistoryCountResponse, HistoryQueryResponse
```

Methods:

- <code title="get /udl/h3geo/history/aodr">client.h3geo.history.<a href="./src/unifieddatalibrary/resources/h3geo/history.py">ador</a>(\*\*<a href="src/unifieddatalibrary/types/h3geo/history_ador_params.py">params</a>) -> None</code>
- <code title="get /udl/h3geo/history/count">client.h3geo.history.<a href="./src/unifieddatalibrary/resources/h3geo/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/h3geo/history_count_params.py">params</a>) -> str</code>
- <code title="get /udl/h3geo/history">client.h3geo.history.<a href="./src/unifieddatalibrary/resources/h3geo/history.py">query</a>(\*\*<a href="src/unifieddatalibrary/types/h3geo/history_query_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/h3geo/history_query_response.py">HistoryQueryResponse</a></code>

# H3geohexcell

Types:

```python
from unifieddatalibrary.types import (
    H3geohexcellListResponse,
    H3geohexcellCountResponse,
    H3geohexcellTupleResponse,
)
```

Methods:

- <code title="get /udl/h3geohexcell">client.h3geohexcell.<a href="./src/unifieddatalibrary/resources/h3geohexcell.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/h3geohexcell_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/h3geohexcell_list_response.py">H3geohexcellListResponse</a></code>
- <code title="get /udl/h3geohexcell/count">client.h3geohexcell.<a href="./src/unifieddatalibrary/resources/h3geohexcell.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/h3geohexcell_count_params.py">params</a>) -> str</code>
- <code title="get /udl/h3geohexcell/queryhelp">client.h3geohexcell.<a href="./src/unifieddatalibrary/resources/h3geohexcell.py">queryhelp</a>() -> None</code>
- <code title="get /udl/h3geohexcell/tuple">client.h3geohexcell.<a href="./src/unifieddatalibrary/resources/h3geohexcell.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/h3geohexcell_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/h3geohexcell_tuple_response.py">H3geohexcellTupleResponse</a></code>

# Hazard

Types:

```python
from unifieddatalibrary.types import HazardListResponse, HazardCountResponse, HazardTupleResponse
```

Methods:

- <code title="post /udl/hazard">client.hazard.<a href="./src/unifieddatalibrary/resources/hazard/hazard.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/hazard_create_params.py">params</a>) -> None</code>
- <code title="get /udl/hazard">client.hazard.<a href="./src/unifieddatalibrary/resources/hazard/hazard.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/hazard_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/hazard_list_response.py">HazardListResponse</a></code>
- <code title="get /udl/hazard/count">client.hazard.<a href="./src/unifieddatalibrary/resources/hazard/hazard.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/hazard_count_params.py">params</a>) -> str</code>
- <code title="post /udl/hazard/createBulk">client.hazard.<a href="./src/unifieddatalibrary/resources/hazard/hazard.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/hazard_create_bulk_params.py">params</a>) -> None</code>
- <code title="get /udl/hazard/{id}">client.hazard.<a href="./src/unifieddatalibrary/resources/hazard/hazard.py">get</a>(id) -> <a href="./src/unifieddatalibrary/types/udl/hazard/hazard_full.py">HazardFull</a></code>
- <code title="get /udl/hazard/queryhelp">client.hazard.<a href="./src/unifieddatalibrary/resources/hazard/hazard.py">queryhelp</a>() -> None</code>
- <code title="get /udl/hazard/tuple">client.hazard.<a href="./src/unifieddatalibrary/resources/hazard/hazard.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/hazard_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/hazard_tuple_response.py">HazardTupleResponse</a></code>

## History

Types:

```python
from unifieddatalibrary.types.hazard import HistoryCountResponse, HistoryQueryResponse
```

Methods:

- <code title="get /udl/hazard/history/aodr">client.hazard.history.<a href="./src/unifieddatalibrary/resources/hazard/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/hazard/history_aodr_params.py">params</a>) -> None</code>
- <code title="get /udl/hazard/history/count">client.hazard.history.<a href="./src/unifieddatalibrary/resources/hazard/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/hazard/history_count_params.py">params</a>) -> str</code>
- <code title="get /udl/hazard/history">client.hazard.history.<a href="./src/unifieddatalibrary/resources/hazard/history.py">query</a>(\*\*<a href="src/unifieddatalibrary/types/hazard/history_query_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/hazard/history_query_response.py">HistoryQueryResponse</a></code>

# Ionoobservation

Types:

```python
from unifieddatalibrary.types import (
    IonoobservationListResponse,
    IonoobservationCountResponse,
    IonoobservationTupleResponse,
)
```

Methods:

- <code title="get /udl/ionoobservation">client.ionoobservation.<a href="./src/unifieddatalibrary/resources/ionoobservation.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/ionoobservation_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/ionoobservation_list_response.py">IonoobservationListResponse</a></code>
- <code title="get /udl/ionoobservation/count">client.ionoobservation.<a href="./src/unifieddatalibrary/resources/ionoobservation.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/ionoobservation_count_params.py">params</a>) -> str</code>
- <code title="post /udl/ionoobservation/createBulk">client.ionoobservation.<a href="./src/unifieddatalibrary/resources/ionoobservation.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/ionoobservation_create_bulk_params.py">params</a>) -> None</code>
- <code title="post /filedrop/udl-ionoobs">client.ionoobservation.<a href="./src/unifieddatalibrary/resources/ionoobservation.py">create_bulk_v2</a>(\*\*<a href="src/unifieddatalibrary/types/ionoobservation_create_bulk_v2_params.py">params</a>) -> None</code>
- <code title="get /udl/ionoobservation/queryhelp">client.ionoobservation.<a href="./src/unifieddatalibrary/resources/ionoobservation.py">queryhelp</a>() -> None</code>
- <code title="get /udl/ionoobservation/tuple">client.ionoobservation.<a href="./src/unifieddatalibrary/resources/ionoobservation.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/ionoobservation_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/ionoobservation_tuple_response.py">IonoobservationTupleResponse</a></code>

# Ir

Types:

```python
from unifieddatalibrary.types import IrListResponse, IrCountResponse, IrGetResponse, IrTupleResponse
```

Methods:

- <code title="post /udl/ir">client.ir.<a href="./src/unifieddatalibrary/resources/ir.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/ir_create_params.py">params</a>) -> None</code>
- <code title="put /udl/ir/{id}">client.ir.<a href="./src/unifieddatalibrary/resources/ir.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/ir_update_params.py">params</a>) -> None</code>
- <code title="get /udl/ir">client.ir.<a href="./src/unifieddatalibrary/resources/ir.py">list</a>() -> <a href="./src/unifieddatalibrary/types/ir_list_response.py">IrListResponse</a></code>
- <code title="delete /udl/ir/{id}">client.ir.<a href="./src/unifieddatalibrary/resources/ir.py">delete</a>(id) -> None</code>
- <code title="get /udl/ir/count">client.ir.<a href="./src/unifieddatalibrary/resources/ir.py">count</a>() -> str</code>
- <code title="get /udl/ir/{id}">client.ir.<a href="./src/unifieddatalibrary/resources/ir.py">get</a>(id) -> <a href="./src/unifieddatalibrary/types/ir_get_response.py">IrGetResponse</a></code>
- <code title="get /udl/ir/queryhelp">client.ir.<a href="./src/unifieddatalibrary/resources/ir.py">queryhelp</a>() -> None</code>
- <code title="get /udl/ir/tuple">client.ir.<a href="./src/unifieddatalibrary/resources/ir.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/ir_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/ir_tuple_response.py">IrTupleResponse</a></code>

# IsrCollections

Types:

```python
from unifieddatalibrary.types import (
    IsrCollectionListResponse,
    IsrCollectionCountResponse,
    IsrCollectionTupleResponse,
)
```

Methods:

- <code title="get /udl/isrcollection">client.isr_collections.<a href="./src/unifieddatalibrary/resources/isr_collections/isr_collections.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/isr_collection_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/isr_collection_list_response.py">IsrCollectionListResponse</a></code>
- <code title="get /udl/isrcollection/count">client.isr_collections.<a href="./src/unifieddatalibrary/resources/isr_collections/isr_collections.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/isr_collection_count_params.py">params</a>) -> str</code>
- <code title="post /udl/isrcollection/createBulk">client.isr_collections.<a href="./src/unifieddatalibrary/resources/isr_collections/isr_collections.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/isr_collection_create_bulk_params.py">params</a>) -> None</code>
- <code title="post /filedrop/udl-isrcollection">client.isr_collections.<a href="./src/unifieddatalibrary/resources/isr_collections/isr_collections.py">create_bulk_v2</a>(\*\*<a href="src/unifieddatalibrary/types/isr_collection_create_bulk_v2_params.py">params</a>) -> None</code>
- <code title="get /udl/isrcollection/queryhelp">client.isr_collections.<a href="./src/unifieddatalibrary/resources/isr_collections/isr_collections.py">queryhelp</a>() -> None</code>
- <code title="get /udl/isrcollection/tuple">client.isr_collections.<a href="./src/unifieddatalibrary/resources/isr_collections/isr_collections.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/isr_collection_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/isr_collection_tuple_response.py">IsrCollectionTupleResponse</a></code>

## History

Types:

```python
from unifieddatalibrary.types.isr_collections import HistoryListResponse, HistoryCountResponse
```

Methods:

- <code title="get /udl/isrcollection/history">client.isr_collections.history.<a href="./src/unifieddatalibrary/resources/isr_collections/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/isr_collections/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/isr_collections/history_list_response.py">HistoryListResponse</a></code>
- <code title="get /udl/isrcollection/history/aodr">client.isr_collections.history.<a href="./src/unifieddatalibrary/resources/isr_collections/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/isr_collections/history_aodr_params.py">params</a>) -> None</code>
- <code title="get /udl/isrcollection/history/count">client.isr_collections.history.<a href="./src/unifieddatalibrary/resources/isr_collections/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/isr_collections/history_count_params.py">params</a>) -> str</code>

# Item

Types:

```python
from unifieddatalibrary.types import (
    ItemListResponse,
    ItemCountResponse,
    ItemGetResponse,
    ItemTupleResponse,
)
```

Methods:

- <code title="post /udl/item">client.item.<a href="./src/unifieddatalibrary/resources/item.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/item_create_params.py">params</a>) -> None</code>
- <code title="put /udl/item/{id}">client.item.<a href="./src/unifieddatalibrary/resources/item.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/item_update_params.py">params</a>) -> None</code>
- <code title="get /udl/item">client.item.<a href="./src/unifieddatalibrary/resources/item.py">list</a>() -> <a href="./src/unifieddatalibrary/types/item_list_response.py">ItemListResponse</a></code>
- <code title="delete /udl/item/{id}">client.item.<a href="./src/unifieddatalibrary/resources/item.py">delete</a>(id) -> None</code>
- <code title="get /udl/item/count">client.item.<a href="./src/unifieddatalibrary/resources/item.py">count</a>() -> str</code>
- <code title="post /filedrop/udl-item">client.item.<a href="./src/unifieddatalibrary/resources/item.py">create_bulk_v2</a>(\*\*<a href="src/unifieddatalibrary/types/item_create_bulk_v2_params.py">params</a>) -> None</code>
- <code title="get /udl/item/{id}">client.item.<a href="./src/unifieddatalibrary/resources/item.py">get</a>(id) -> <a href="./src/unifieddatalibrary/types/item_get_response.py">ItemGetResponse</a></code>
- <code title="get /udl/item/queryhelp">client.item.<a href="./src/unifieddatalibrary/resources/item.py">queryhelp</a>() -> None</code>
- <code title="get /udl/item/tuple">client.item.<a href="./src/unifieddatalibrary/resources/item.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/item_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/item_tuple_response.py">ItemTupleResponse</a></code>

# ItemTrackings

Types:

```python
from unifieddatalibrary.types import (
    ItemTrackingListResponse,
    ItemTrackingCountResponse,
    ItemTrackingTupleResponse,
)
```

Methods:

- <code title="post /udl/itemtracking">client.item_trackings.<a href="./src/unifieddatalibrary/resources/item_trackings/item_trackings.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/item_tracking_create_params.py">params</a>) -> None</code>
- <code title="get /udl/itemtracking">client.item_trackings.<a href="./src/unifieddatalibrary/resources/item_trackings/item_trackings.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/item_tracking_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/item_tracking_list_response.py">ItemTrackingListResponse</a></code>
- <code title="delete /udl/itemtracking/{id}">client.item_trackings.<a href="./src/unifieddatalibrary/resources/item_trackings/item_trackings.py">delete</a>(id) -> None</code>
- <code title="get /udl/itemtracking/count">client.item_trackings.<a href="./src/unifieddatalibrary/resources/item_trackings/item_trackings.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/item_tracking_count_params.py">params</a>) -> str</code>
- <code title="post /filedrop/udl-itemtracking">client.item_trackings.<a href="./src/unifieddatalibrary/resources/item_trackings/item_trackings.py">create_bulk_v2</a>(\*\*<a href="src/unifieddatalibrary/types/item_tracking_create_bulk_v2_params.py">params</a>) -> None</code>
- <code title="get /udl/itemtracking/{id}">client.item_trackings.<a href="./src/unifieddatalibrary/resources/item_trackings/item_trackings.py">get</a>(id) -> <a href="./src/unifieddatalibrary/types/udl/itemtracking/item_tracking_full.py">ItemTrackingFull</a></code>
- <code title="get /udl/itemtracking/queryhelp">client.item_trackings.<a href="./src/unifieddatalibrary/resources/item_trackings/item_trackings.py">queryhelp</a>() -> None</code>
- <code title="get /udl/itemtracking/tuple">client.item_trackings.<a href="./src/unifieddatalibrary/resources/item_trackings/item_trackings.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/item_tracking_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/item_tracking_tuple_response.py">ItemTrackingTupleResponse</a></code>

## History

Types:

```python
from unifieddatalibrary.types.item_trackings import HistoryListResponse, HistoryCountResponse
```

Methods:

- <code title="get /udl/itemtracking/history">client.item_trackings.history.<a href="./src/unifieddatalibrary/resources/item_trackings/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/item_trackings/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/item_trackings/history_list_response.py">HistoryListResponse</a></code>
- <code title="get /udl/itemtracking/history/count">client.item_trackings.history.<a href="./src/unifieddatalibrary/resources/item_trackings/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/item_trackings/history_count_params.py">params</a>) -> str</code>

# Launchdetection

Types:

```python
from unifieddatalibrary.types import (
    LaunchdetectionListResponse,
    LaunchdetectionCountResponse,
    LaunchdetectionGetResponse,
    LaunchdetectionTupleResponse,
)
```

Methods:

- <code title="post /udl/launchdetection">client.launchdetection.<a href="./src/unifieddatalibrary/resources/launchdetection.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/launchdetection_create_params.py">params</a>) -> None</code>
- <code title="put /udl/launchdetection/{id}">client.launchdetection.<a href="./src/unifieddatalibrary/resources/launchdetection.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/launchdetection_update_params.py">params</a>) -> None</code>
- <code title="get /udl/launchdetection">client.launchdetection.<a href="./src/unifieddatalibrary/resources/launchdetection.py">list</a>() -> <a href="./src/unifieddatalibrary/types/launchdetection_list_response.py">LaunchdetectionListResponse</a></code>
- <code title="delete /udl/launchdetection/{id}">client.launchdetection.<a href="./src/unifieddatalibrary/resources/launchdetection.py">delete</a>(id) -> None</code>
- <code title="get /udl/launchdetection/count">client.launchdetection.<a href="./src/unifieddatalibrary/resources/launchdetection.py">count</a>() -> str</code>
- <code title="get /udl/launchdetection/{id}">client.launchdetection.<a href="./src/unifieddatalibrary/resources/launchdetection.py">get</a>(id) -> <a href="./src/unifieddatalibrary/types/launchdetection_get_response.py">LaunchdetectionGetResponse</a></code>
- <code title="get /udl/launchdetection/queryhelp">client.launchdetection.<a href="./src/unifieddatalibrary/resources/launchdetection.py">queryhelp</a>() -> None</code>
- <code title="get /udl/launchdetection/tuple">client.launchdetection.<a href="./src/unifieddatalibrary/resources/launchdetection.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/launchdetection_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/launchdetection_tuple_response.py">LaunchdetectionTupleResponse</a></code>

# Launchevent

Types:

```python
from unifieddatalibrary.types import (
    LauncheventListResponse,
    LauncheventCountResponse,
    LauncheventGetResponse,
    LauncheventTupleResponse,
)
```

Methods:

- <code title="post /udl/launchevent">client.launchevent.<a href="./src/unifieddatalibrary/resources/launchevent.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/launchevent_create_params.py">params</a>) -> None</code>
- <code title="get /udl/launchevent">client.launchevent.<a href="./src/unifieddatalibrary/resources/launchevent.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/launchevent_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/launchevent_list_response.py">LauncheventListResponse</a></code>
- <code title="get /udl/launchevent/count">client.launchevent.<a href="./src/unifieddatalibrary/resources/launchevent.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/launchevent_count_params.py">params</a>) -> str</code>
- <code title="post /udl/launchevent/createBulk">client.launchevent.<a href="./src/unifieddatalibrary/resources/launchevent.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/launchevent_create_bulk_params.py">params</a>) -> None</code>
- <code title="post /filedrop/udl-launchevent">client.launchevent.<a href="./src/unifieddatalibrary/resources/launchevent.py">create_bulk_v2</a>(\*\*<a href="src/unifieddatalibrary/types/launchevent_create_bulk_v2_params.py">params</a>) -> None</code>
- <code title="get /udl/launchevent/{id}">client.launchevent.<a href="./src/unifieddatalibrary/resources/launchevent.py">get</a>(id) -> <a href="./src/unifieddatalibrary/types/launchevent_get_response.py">LauncheventGetResponse</a></code>
- <code title="get /udl/launchevent/queryhelp">client.launchevent.<a href="./src/unifieddatalibrary/resources/launchevent.py">queryhelp</a>() -> None</code>
- <code title="get /udl/launchevent/tuple">client.launchevent.<a href="./src/unifieddatalibrary/resources/launchevent.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/launchevent_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/launchevent_tuple_response.py">LauncheventTupleResponse</a></code>

# Launchsite

Types:

```python
from unifieddatalibrary.types import (
    LaunchsiteListResponse,
    LaunchsiteCountResponse,
    LaunchsiteGetResponse,
    LaunchsiteTupleResponse,
)
```

Methods:

- <code title="post /udl/launchsite">client.launchsite.<a href="./src/unifieddatalibrary/resources/launchsite.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/launchsite_create_params.py">params</a>) -> None</code>
- <code title="put /udl/launchsite/{id}">client.launchsite.<a href="./src/unifieddatalibrary/resources/launchsite.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/launchsite_update_params.py">params</a>) -> None</code>
- <code title="get /udl/launchsite">client.launchsite.<a href="./src/unifieddatalibrary/resources/launchsite.py">list</a>() -> <a href="./src/unifieddatalibrary/types/launchsite_list_response.py">LaunchsiteListResponse</a></code>
- <code title="delete /udl/launchsite/{id}">client.launchsite.<a href="./src/unifieddatalibrary/resources/launchsite.py">delete</a>(id) -> None</code>
- <code title="get /udl/launchsite/count">client.launchsite.<a href="./src/unifieddatalibrary/resources/launchsite.py">count</a>() -> str</code>
- <code title="get /udl/launchsite/{id}">client.launchsite.<a href="./src/unifieddatalibrary/resources/launchsite.py">get</a>(id) -> <a href="./src/unifieddatalibrary/types/launchsite_get_response.py">LaunchsiteGetResponse</a></code>
- <code title="get /udl/launchsite/queryhelp">client.launchsite.<a href="./src/unifieddatalibrary/resources/launchsite.py">queryhelp</a>() -> None</code>
- <code title="get /udl/launchsite/tuple">client.launchsite.<a href="./src/unifieddatalibrary/resources/launchsite.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/launchsite_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/launchsite_tuple_response.py">LaunchsiteTupleResponse</a></code>

# Launchsitedetails

Types:

```python
from unifieddatalibrary.types import (
    LaunchsitedetailListResponse,
    LaunchsitedetailFindBySourceResponse,
    LaunchsitedetailGetResponse,
)
```

Methods:

- <code title="post /udl/launchsitedetails">client.launchsitedetails.<a href="./src/unifieddatalibrary/resources/launchsitedetails.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/launchsitedetail_create_params.py">params</a>) -> None</code>
- <code title="put /udl/launchsitedetails/{id}">client.launchsitedetails.<a href="./src/unifieddatalibrary/resources/launchsitedetails.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/launchsitedetail_update_params.py">params</a>) -> None</code>
- <code title="get /udl/launchsitedetails">client.launchsitedetails.<a href="./src/unifieddatalibrary/resources/launchsitedetails.py">list</a>() -> <a href="./src/unifieddatalibrary/types/launchsitedetail_list_response.py">LaunchsitedetailListResponse</a></code>
- <code title="delete /udl/launchsitedetails/{id}">client.launchsitedetails.<a href="./src/unifieddatalibrary/resources/launchsitedetails.py">delete</a>(id) -> None</code>
- <code title="get /udl/launchsitedetails/findBySource">client.launchsitedetails.<a href="./src/unifieddatalibrary/resources/launchsitedetails.py">find_by_source</a>(\*\*<a href="src/unifieddatalibrary/types/launchsitedetail_find_by_source_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/launchsitedetail_find_by_source_response.py">LaunchsitedetailFindBySourceResponse</a></code>
- <code title="get /udl/launchsitedetails/{id}">client.launchsitedetails.<a href="./src/unifieddatalibrary/resources/launchsitedetails.py">get</a>(id) -> <a href="./src/unifieddatalibrary/types/launchsitedetail_get_response.py">LaunchsitedetailGetResponse</a></code>

# Launchvehicle

Types:

```python
from unifieddatalibrary.types import (
    LaunchvehicleListResponse,
    LaunchvehicleCountResponse,
    LaunchvehicleGetResponse,
    LaunchvehicleTupleResponse,
)
```

Methods:

- <code title="post /udl/launchvehicle">client.launchvehicle.<a href="./src/unifieddatalibrary/resources/launchvehicle.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/launchvehicle_create_params.py">params</a>) -> None</code>
- <code title="put /udl/launchvehicle/{id}">client.launchvehicle.<a href="./src/unifieddatalibrary/resources/launchvehicle.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/launchvehicle_update_params.py">params</a>) -> None</code>
- <code title="get /udl/launchvehicle">client.launchvehicle.<a href="./src/unifieddatalibrary/resources/launchvehicle.py">list</a>() -> <a href="./src/unifieddatalibrary/types/launchvehicle_list_response.py">LaunchvehicleListResponse</a></code>
- <code title="delete /udl/launchvehicle/{id}">client.launchvehicle.<a href="./src/unifieddatalibrary/resources/launchvehicle.py">delete</a>(id) -> None</code>
- <code title="get /udl/launchvehicle/count">client.launchvehicle.<a href="./src/unifieddatalibrary/resources/launchvehicle.py">count</a>() -> str</code>
- <code title="get /udl/launchvehicle/{id}">client.launchvehicle.<a href="./src/unifieddatalibrary/resources/launchvehicle.py">get</a>(id) -> <a href="./src/unifieddatalibrary/types/launchvehicle_get_response.py">LaunchvehicleGetResponse</a></code>
- <code title="get /udl/launchvehicle/queryhelp">client.launchvehicle.<a href="./src/unifieddatalibrary/resources/launchvehicle.py">queryhelp</a>() -> None</code>
- <code title="get /udl/launchvehicle/tuple">client.launchvehicle.<a href="./src/unifieddatalibrary/resources/launchvehicle.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/launchvehicle_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/launchvehicle_tuple_response.py">LaunchvehicleTupleResponse</a></code>

# Launchvehicledetails

Types:

```python
from unifieddatalibrary.types import LaunchvehicledetailListResponse, LaunchvehicledetailGetResponse
```

Methods:

- <code title="post /udl/launchvehicledetails">client.launchvehicledetails.<a href="./src/unifieddatalibrary/resources/launchvehicledetails.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/launchvehicledetail_create_params.py">params</a>) -> None</code>
- <code title="put /udl/launchvehicledetails/{id}">client.launchvehicledetails.<a href="./src/unifieddatalibrary/resources/launchvehicledetails.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/launchvehicledetail_update_params.py">params</a>) -> None</code>
- <code title="get /udl/launchvehicledetails">client.launchvehicledetails.<a href="./src/unifieddatalibrary/resources/launchvehicledetails.py">list</a>() -> <a href="./src/unifieddatalibrary/types/launchvehicledetail_list_response.py">LaunchvehicledetailListResponse</a></code>
- <code title="delete /udl/launchvehicledetails/{id}">client.launchvehicledetails.<a href="./src/unifieddatalibrary/resources/launchvehicledetails.py">delete</a>(id) -> None</code>
- <code title="get /udl/launchvehicledetails/{id}">client.launchvehicledetails.<a href="./src/unifieddatalibrary/resources/launchvehicledetails.py">get</a>(id) -> <a href="./src/unifieddatalibrary/types/launchvehicledetail_get_response.py">LaunchvehicledetailGetResponse</a></code>

# LinkStatus

Types:

```python
from unifieddatalibrary.types import (
    LinkStatusListResponse,
    LinkStatusCountResponse,
    LinkStatusTupleResponse,
)
```

Methods:

- <code title="post /udl/linkstatus">client.link_status.<a href="./src/unifieddatalibrary/resources/link_status/link_status.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/link_status_create_params.py">params</a>) -> None</code>
- <code title="get /udl/linkstatus">client.link_status.<a href="./src/unifieddatalibrary/resources/link_status/link_status.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/link_status_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/link_status_list_response.py">LinkStatusListResponse</a></code>
- <code title="get /udl/linkstatus/count">client.link_status.<a href="./src/unifieddatalibrary/resources/link_status/link_status.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/link_status_count_params.py">params</a>) -> str</code>
- <code title="get /udl/linkstatus/{id}">client.link_status.<a href="./src/unifieddatalibrary/resources/link_status/link_status.py">get</a>(id) -> <a href="./src/unifieddatalibrary/types/udl/linkstatus/link_status_full.py">LinkStatusFull</a></code>
- <code title="get /udl/linkstatus/queryhelp">client.link_status.<a href="./src/unifieddatalibrary/resources/link_status/link_status.py">queryhelp</a>() -> None</code>
- <code title="get /udl/linkstatus/tuple">client.link_status.<a href="./src/unifieddatalibrary/resources/link_status/link_status.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/link_status_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/link_status_tuple_response.py">LinkStatusTupleResponse</a></code>

## Datalink

Types:

```python
from unifieddatalibrary.types.link_status import (
    DatalinkIngest,
    DatalinkListResponse,
    DatalinkCountResponse,
    DatalinkTupleResponse,
)
```

Methods:

- <code title="post /udl/datalink">client.link_status.datalink.<a href="./src/unifieddatalibrary/resources/link_status/datalink.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/link_status/datalink_create_params.py">params</a>) -> None</code>
- <code title="get /udl/datalink">client.link_status.datalink.<a href="./src/unifieddatalibrary/resources/link_status/datalink.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/link_status/datalink_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/link_status/datalink_list_response.py">DatalinkListResponse</a></code>
- <code title="get /udl/datalink/count">client.link_status.datalink.<a href="./src/unifieddatalibrary/resources/link_status/datalink.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/link_status/datalink_count_params.py">params</a>) -> str</code>
- <code title="post /filedrop/udl-datalink">client.link_status.datalink.<a href="./src/unifieddatalibrary/resources/link_status/datalink.py">create_bulk_v2</a>(\*\*<a href="src/unifieddatalibrary/types/link_status/datalink_create_bulk_v2_params.py">params</a>) -> None</code>
- <code title="get /udl/datalink/queryhelp">client.link_status.datalink.<a href="./src/unifieddatalibrary/resources/link_status/datalink.py">queryhelp</a>() -> None</code>
- <code title="get /udl/datalink/tuple">client.link_status.datalink.<a href="./src/unifieddatalibrary/resources/link_status/datalink.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/link_status/datalink_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/link_status/datalink_tuple_response.py">DatalinkTupleResponse</a></code>

## History

Types:

```python
from unifieddatalibrary.types.link_status import HistoryListResponse, HistoryCountResponse
```

Methods:

- <code title="get /udl/linkstatus/history">client.link_status.history.<a href="./src/unifieddatalibrary/resources/link_status/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/link_status/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/link_status/history_list_response.py">HistoryListResponse</a></code>
- <code title="get /udl/linkstatus/history/aodr">client.link_status.history.<a href="./src/unifieddatalibrary/resources/link_status/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/link_status/history_aodr_params.py">params</a>) -> None</code>
- <code title="get /udl/linkstatus/history/count">client.link_status.history.<a href="./src/unifieddatalibrary/resources/link_status/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/link_status/history_count_params.py">params</a>) -> str</code>

# Location

Types:

```python
from unifieddatalibrary.types import (
    LocationFull,
    LocationIngest,
    LocationListResponse,
    LocationCountResponse,
    LocationTupleResponse,
)
```

Methods:

- <code title="post /udl/location">client.location.<a href="./src/unifieddatalibrary/resources/location.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/location_create_params.py">params</a>) -> None</code>
- <code title="put /udl/location/{id}">client.location.<a href="./src/unifieddatalibrary/resources/location.py">update</a>(id, \*\*<a href="src/unifieddatalibrary/types/location_update_params.py">params</a>) -> None</code>
- <code title="get /udl/location">client.location.<a href="./src/unifieddatalibrary/resources/location.py">list</a>() -> <a href="./src/unifieddatalibrary/types/location_list_response.py">LocationListResponse</a></code>
- <code title="delete /udl/location/{id}">client.location.<a href="./src/unifieddatalibrary/resources/location.py">delete</a>(id) -> None</code>
- <code title="get /udl/location/count">client.location.<a href="./src/unifieddatalibrary/resources/location.py">count</a>() -> str</code>
- <code title="get /udl/location/{id}">client.location.<a href="./src/unifieddatalibrary/resources/location.py">get</a>(id) -> <a href="./src/unifieddatalibrary/types/location_full.py">LocationFull</a></code>
- <code title="get /udl/location/queryhelp">client.location.<a href="./src/unifieddatalibrary/resources/location.py">queryhelp</a>() -> None</code>
- <code title="get /udl/location/tuple">client.location.<a href="./src/unifieddatalibrary/resources/location.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/location_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/location_tuple_response.py">LocationTupleResponse</a></code>

# Logisticssupport

Types:

```python
from unifieddatalibrary.types import (
    LogisticsRemarksFull,
    LogisticssupportListResponse,
    LogisticssupportCountResponse,
    LogisticssupportGetResponse,
    LogisticssupportTupleResponse,
)
```

Methods:

- <code title="post /udl/logisticssupport">client.logisticssupport.<a href="./src/unifieddatalibrary/resources/logisticssupport/logisticssupport.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/logisticssupport_create_params.py">params</a>) -> None</code>
- <code title="put /udl/logisticssupport/{id}">client.logisticssupport.<a href="./src/unifieddatalibrary/resources/logisticssupport/logisticssupport.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/logisticssupport_update_params.py">params</a>) -> None</code>
- <code title="get /udl/logisticssupport">client.logisticssupport.<a href="./src/unifieddatalibrary/resources/logisticssupport/logisticssupport.py">list</a>() -> <a href="./src/unifieddatalibrary/types/logisticssupport_list_response.py">LogisticssupportListResponse</a></code>
- <code title="get /udl/logisticssupport/count">client.logisticssupport.<a href="./src/unifieddatalibrary/resources/logisticssupport/logisticssupport.py">count</a>() -> str</code>
- <code title="post /udl/logisticssupport/createBulk">client.logisticssupport.<a href="./src/unifieddatalibrary/resources/logisticssupport/logisticssupport.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/logisticssupport_create_bulk_params.py">params</a>) -> None</code>
- <code title="post /filedrop/udl-logisticssupport">client.logisticssupport.<a href="./src/unifieddatalibrary/resources/logisticssupport/logisticssupport.py">create_bulk_v2</a>(\*\*<a href="src/unifieddatalibrary/types/logisticssupport_create_bulk_v2_params.py">params</a>) -> None</code>
- <code title="get /udl/logisticssupport/{id}">client.logisticssupport.<a href="./src/unifieddatalibrary/resources/logisticssupport/logisticssupport.py">get</a>(id) -> <a href="./src/unifieddatalibrary/types/logisticssupport_get_response.py">LogisticssupportGetResponse</a></code>
- <code title="get /udl/logisticssupport/queryhelp">client.logisticssupport.<a href="./src/unifieddatalibrary/resources/logisticssupport/logisticssupport.py">queryhelp</a>() -> None</code>
- <code title="get /udl/logisticssupport/tuple">client.logisticssupport.<a href="./src/unifieddatalibrary/resources/logisticssupport/logisticssupport.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/logisticssupport_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/logisticssupport_tuple_response.py">LogisticssupportTupleResponse</a></code>

## History

Types:

```python
from unifieddatalibrary.types.logisticssupport import HistoryListResponse, HistoryCountResponse
```

Methods:

- <code title="get /udl/logisticssupport/history">client.logisticssupport.history.<a href="./src/unifieddatalibrary/resources/logisticssupport/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/logisticssupport/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/logisticssupport/history_list_response.py">HistoryListResponse</a></code>
- <code title="get /udl/logisticssupport/history/aodr">client.logisticssupport.history.<a href="./src/unifieddatalibrary/resources/logisticssupport/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/logisticssupport/history_aodr_params.py">params</a>) -> None</code>
- <code title="get /udl/logisticssupport/history/count">client.logisticssupport.history.<a href="./src/unifieddatalibrary/resources/logisticssupport/history.py">count</a>() -> str</code>

# Maneuvers

Types:

```python
from unifieddatalibrary.types import (
    ManeuverListResponse,
    ManeuverCountResponse,
    ManeuverTupleResponse,
)
```

Methods:

- <code title="post /udl/maneuver">client.maneuvers.<a href="./src/unifieddatalibrary/resources/maneuvers/maneuvers.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/maneuver_create_params.py">params</a>) -> None</code>
- <code title="get /udl/maneuver">client.maneuvers.<a href="./src/unifieddatalibrary/resources/maneuvers/maneuvers.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/maneuver_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/maneuver_list_response.py">ManeuverListResponse</a></code>
- <code title="get /udl/maneuver/count">client.maneuvers.<a href="./src/unifieddatalibrary/resources/maneuvers/maneuvers.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/maneuver_count_params.py">params</a>) -> str</code>
- <code title="post /udl/maneuver/createBulk">client.maneuvers.<a href="./src/unifieddatalibrary/resources/maneuvers/maneuvers.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/maneuver_create_bulk_params.py">params</a>) -> None</code>
- <code title="post /filedrop/udl-maneuver">client.maneuvers.<a href="./src/unifieddatalibrary/resources/maneuvers/maneuvers.py">create_bulk_v2</a>(\*\*<a href="src/unifieddatalibrary/types/maneuver_create_bulk_v2_params.py">params</a>) -> None</code>
- <code title="get /udl/maneuver/{id}">client.maneuvers.<a href="./src/unifieddatalibrary/resources/maneuvers/maneuvers.py">get</a>(id) -> <a href="./src/unifieddatalibrary/types/udl/maneuver/maneuver_full.py">ManeuverFull</a></code>
- <code title="get /udl/maneuver/queryhelp">client.maneuvers.<a href="./src/unifieddatalibrary/resources/maneuvers/maneuvers.py">queryhelp</a>() -> None</code>
- <code title="get /udl/maneuver/tuple">client.maneuvers.<a href="./src/unifieddatalibrary/resources/maneuvers/maneuvers.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/maneuver_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/maneuver_tuple_response.py">ManeuverTupleResponse</a></code>

## History

Types:

```python
from unifieddatalibrary.types.maneuvers import HistoryListResponse, HistoryCountResponse
```

Methods:

- <code title="get /udl/maneuver/history">client.maneuvers.history.<a href="./src/unifieddatalibrary/resources/maneuvers/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/maneuvers/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/maneuvers/history_list_response.py">HistoryListResponse</a></code>
- <code title="get /udl/maneuver/history/aodr">client.maneuvers.history.<a href="./src/unifieddatalibrary/resources/maneuvers/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/maneuvers/history_aodr_params.py">params</a>) -> None</code>
- <code title="get /udl/maneuver/history/count">client.maneuvers.history.<a href="./src/unifieddatalibrary/resources/maneuvers/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/maneuvers/history_count_params.py">params</a>) -> str</code>

# Manifold

Types:

```python
from unifieddatalibrary.types import (
    ManifoldListResponse,
    ManifoldCountResponse,
    ManifoldGetResponse,
    ManifoldTupleResponse,
)
```

Methods:

- <code title="post /udl/manifold">client.manifold.<a href="./src/unifieddatalibrary/resources/manifold.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/manifold_create_params.py">params</a>) -> None</code>
- <code title="put /udl/manifold/{id}">client.manifold.<a href="./src/unifieddatalibrary/resources/manifold.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/manifold_update_params.py">params</a>) -> None</code>
- <code title="get /udl/manifold">client.manifold.<a href="./src/unifieddatalibrary/resources/manifold.py">list</a>() -> <a href="./src/unifieddatalibrary/types/manifold_list_response.py">ManifoldListResponse</a></code>
- <code title="delete /udl/manifold/{id}">client.manifold.<a href="./src/unifieddatalibrary/resources/manifold.py">delete</a>(id) -> None</code>
- <code title="get /udl/manifold/count">client.manifold.<a href="./src/unifieddatalibrary/resources/manifold.py">count</a>() -> str</code>
- <code title="post /udl/manifold/createBulk">client.manifold.<a href="./src/unifieddatalibrary/resources/manifold.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/manifold_create_bulk_params.py">params</a>) -> None</code>
- <code title="get /udl/manifold/{id}">client.manifold.<a href="./src/unifieddatalibrary/resources/manifold.py">get</a>(id) -> <a href="./src/unifieddatalibrary/types/manifold_get_response.py">ManifoldGetResponse</a></code>
- <code title="get /udl/manifold/queryhelp">client.manifold.<a href="./src/unifieddatalibrary/resources/manifold.py">queryhelp</a>() -> None</code>
- <code title="get /udl/manifold/tuple">client.manifold.<a href="./src/unifieddatalibrary/resources/manifold.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/manifold_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/manifold_tuple_response.py">ManifoldTupleResponse</a></code>

# Manifoldelset

Types:

```python
from unifieddatalibrary.types import (
    ManifoldelsetListResponse,
    ManifoldelsetCountResponse,
    ManifoldelsetGetResponse,
    ManifoldelsetTupleResponse,
)
```

Methods:

- <code title="post /udl/manifoldelset">client.manifoldelset.<a href="./src/unifieddatalibrary/resources/manifoldelset.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/manifoldelset_create_params.py">params</a>) -> None</code>
- <code title="put /udl/manifoldelset/{id}">client.manifoldelset.<a href="./src/unifieddatalibrary/resources/manifoldelset.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/manifoldelset_update_params.py">params</a>) -> None</code>
- <code title="get /udl/manifoldelset">client.manifoldelset.<a href="./src/unifieddatalibrary/resources/manifoldelset.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/manifoldelset_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/manifoldelset_list_response.py">ManifoldelsetListResponse</a></code>
- <code title="delete /udl/manifoldelset/{id}">client.manifoldelset.<a href="./src/unifieddatalibrary/resources/manifoldelset.py">delete</a>(id) -> None</code>
- <code title="get /udl/manifoldelset/count">client.manifoldelset.<a href="./src/unifieddatalibrary/resources/manifoldelset.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/manifoldelset_count_params.py">params</a>) -> str</code>
- <code title="post /udl/manifoldelset/createBulk">client.manifoldelset.<a href="./src/unifieddatalibrary/resources/manifoldelset.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/manifoldelset_create_bulk_params.py">params</a>) -> None</code>
- <code title="get /udl/manifoldelset/{id}">client.manifoldelset.<a href="./src/unifieddatalibrary/resources/manifoldelset.py">get</a>(id) -> <a href="./src/unifieddatalibrary/types/manifoldelset_get_response.py">ManifoldelsetGetResponse</a></code>
- <code title="get /udl/manifoldelset/queryhelp">client.manifoldelset.<a href="./src/unifieddatalibrary/resources/manifoldelset.py">queryhelp</a>() -> None</code>
- <code title="get /udl/manifoldelset/tuple">client.manifoldelset.<a href="./src/unifieddatalibrary/resources/manifoldelset.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/manifoldelset_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/manifoldelset_tuple_response.py">ManifoldelsetTupleResponse</a></code>

# MissileTracks

Types:

```python
from unifieddatalibrary.types import (
    MissileTrackListResponse,
    MissileTrackCountResponse,
    MissileTrackTupleResponse,
)
```

Methods:

- <code title="get /udl/missiletrack">client.missile_tracks.<a href="./src/unifieddatalibrary/resources/missile_tracks/missile_tracks.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/missile_track_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/missile_track_list_response.py">MissileTrackListResponse</a></code>
- <code title="get /udl/missiletrack/count">client.missile_tracks.<a href="./src/unifieddatalibrary/resources/missile_tracks/missile_tracks.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/missile_track_count_params.py">params</a>) -> str</code>
- <code title="post /udl/missiletrack/createBulk">client.missile_tracks.<a href="./src/unifieddatalibrary/resources/missile_tracks/missile_tracks.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/missile_track_create_bulk_params.py">params</a>) -> None</code>
- <code title="post /filedrop/udl-missiletrack">client.missile_tracks.<a href="./src/unifieddatalibrary/resources/missile_tracks/missile_tracks.py">create_bulk_v2</a>(\*\*<a href="src/unifieddatalibrary/types/missile_track_create_bulk_v2_params.py">params</a>) -> None</code>
- <code title="get /udl/missiletrack/queryhelp">client.missile_tracks.<a href="./src/unifieddatalibrary/resources/missile_tracks/missile_tracks.py">queryhelp</a>() -> None</code>
- <code title="get /udl/missiletrack/tuple">client.missile_tracks.<a href="./src/unifieddatalibrary/resources/missile_tracks/missile_tracks.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/missile_track_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/missile_track_tuple_response.py">MissileTrackTupleResponse</a></code>

## History

Types:

```python
from unifieddatalibrary.types.missile_tracks import HistoryCountResponse, HistoryQueryResponse
```

Methods:

- <code title="get /udl/missiletrack/history/aodr">client.missile_tracks.history.<a href="./src/unifieddatalibrary/resources/missile_tracks/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/missile_tracks/history_aodr_params.py">params</a>) -> None</code>
- <code title="get /udl/missiletrack/history/count">client.missile_tracks.history.<a href="./src/unifieddatalibrary/resources/missile_tracks/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/missile_tracks/history_count_params.py">params</a>) -> str</code>
- <code title="get /udl/missiletrack/history">client.missile_tracks.history.<a href="./src/unifieddatalibrary/resources/missile_tracks/history.py">query</a>(\*\*<a href="src/unifieddatalibrary/types/missile_tracks/history_query_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/missile_tracks/history_query_response.py">HistoryQueryResponse</a></code>

# Missionassignment

Types:

```python
from unifieddatalibrary.types import (
    MissionassignmentListResponse,
    MissionassignmentCountResponse,
    MissionassignmentTupleResponse,
)
```

Methods:

- <code title="post /udl/missionassignment">client.missionassignment.<a href="./src/unifieddatalibrary/resources/missionassignment/missionassignment.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/missionassignment_create_params.py">params</a>) -> None</code>
- <code title="put /udl/missionassignment/{id}">client.missionassignment.<a href="./src/unifieddatalibrary/resources/missionassignment/missionassignment.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/missionassignment_update_params.py">params</a>) -> None</code>
- <code title="get /udl/missionassignment">client.missionassignment.<a href="./src/unifieddatalibrary/resources/missionassignment/missionassignment.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/missionassignment_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/missionassignment_list_response.py">MissionassignmentListResponse</a></code>
- <code title="delete /udl/missionassignment/{id}">client.missionassignment.<a href="./src/unifieddatalibrary/resources/missionassignment/missionassignment.py">delete</a>(id) -> None</code>
- <code title="get /udl/missionassignment/count">client.missionassignment.<a href="./src/unifieddatalibrary/resources/missionassignment/missionassignment.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/missionassignment_count_params.py">params</a>) -> str</code>
- <code title="post /udl/missionassignment/createBulk">client.missionassignment.<a href="./src/unifieddatalibrary/resources/missionassignment/missionassignment.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/missionassignment_create_bulk_params.py">params</a>) -> None</code>
- <code title="get /udl/missionassignment/{id}">client.missionassignment.<a href="./src/unifieddatalibrary/resources/missionassignment/missionassignment.py">get</a>(id) -> <a href="./src/unifieddatalibrary/types/udl/missionassignment/mission_assignment_full.py">MissionAssignmentFull</a></code>
- <code title="get /udl/missionassignment/queryhelp">client.missionassignment.<a href="./src/unifieddatalibrary/resources/missionassignment/missionassignment.py">queryhelp</a>() -> None</code>
- <code title="get /udl/missionassignment/tuple">client.missionassignment.<a href="./src/unifieddatalibrary/resources/missionassignment/missionassignment.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/missionassignment_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/missionassignment_tuple_response.py">MissionassignmentTupleResponse</a></code>

## History

Types:

```python
from unifieddatalibrary.types.missionassignment import HistoryCountResponse, HistoryQueryResponse
```

Methods:

- <code title="get /udl/missionassignment/history/aodr">client.missionassignment.history.<a href="./src/unifieddatalibrary/resources/missionassignment/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/missionassignment/history_aodr_params.py">params</a>) -> None</code>
- <code title="get /udl/missionassignment/history/count">client.missionassignment.history.<a href="./src/unifieddatalibrary/resources/missionassignment/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/missionassignment/history_count_params.py">params</a>) -> str</code>
- <code title="get /udl/missionassignment/history">client.missionassignment.history.<a href="./src/unifieddatalibrary/resources/missionassignment/history.py">query</a>(\*\*<a href="src/unifieddatalibrary/types/missionassignment/history_query_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/missionassignment/history_query_response.py">HistoryQueryResponse</a></code>

# Monoradar

Types:

```python
from unifieddatalibrary.types import (
    MonoradarListResponse,
    MonoradarCountResponse,
    MonoradarTupleResponse,
)
```

Methods:

- <code title="get /udl/monoradar">client.monoradar.<a href="./src/unifieddatalibrary/resources/monoradar.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/monoradar_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/monoradar_list_response.py">MonoradarListResponse</a></code>
- <code title="get /udl/monoradar/count">client.monoradar.<a href="./src/unifieddatalibrary/resources/monoradar.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/monoradar_count_params.py">params</a>) -> str</code>
- <code title="post /udl/monoradar/createBulk">client.monoradar.<a href="./src/unifieddatalibrary/resources/monoradar.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/monoradar_create_bulk_params.py">params</a>) -> None</code>
- <code title="get /udl/monoradar/queryhelp">client.monoradar.<a href="./src/unifieddatalibrary/resources/monoradar.py">queryhelp</a>() -> None</code>
- <code title="get /udl/monoradar/tuple">client.monoradar.<a href="./src/unifieddatalibrary/resources/monoradar.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/monoradar_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/monoradar_tuple_response.py">MonoradarTupleResponse</a></code>

# Mti

Types:

```python
from unifieddatalibrary.types import MtiListResponse, MtiCountResponse, MtiTupleResponse
```

Methods:

- <code title="get /udl/mti">client.mti.<a href="./src/unifieddatalibrary/resources/mti.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/mti_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/mti_list_response.py">MtiListResponse</a></code>
- <code title="get /udl/mti/count">client.mti.<a href="./src/unifieddatalibrary/resources/mti.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/mti_count_params.py">params</a>) -> str</code>
- <code title="post /udl/mti/createBulk">client.mti.<a href="./src/unifieddatalibrary/resources/mti.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/mti_create_bulk_params.py">params</a>) -> None</code>
- <code title="post /filedrop/udl-mti">client.mti.<a href="./src/unifieddatalibrary/resources/mti.py">create_bulk_v2</a>(\*\*<a href="src/unifieddatalibrary/types/mti_create_bulk_v2_params.py">params</a>) -> None</code>
- <code title="get /udl/mti/queryhelp">client.mti.<a href="./src/unifieddatalibrary/resources/mti.py">queryhelp</a>() -> None</code>
- <code title="get /udl/mti/tuple">client.mti.<a href="./src/unifieddatalibrary/resources/mti.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/mti_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/mti_tuple_response.py">MtiTupleResponse</a></code>

# Navigation

Types:

```python
from unifieddatalibrary.types import (
    NavigationListResponse,
    NavigationCountResponse,
    NavigationGetResponse,
    NavigationTupleResponse,
)
```

Methods:

- <code title="post /udl/navigation">client.navigation.<a href="./src/unifieddatalibrary/resources/navigation.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/navigation_create_params.py">params</a>) -> None</code>
- <code title="put /udl/navigation/{id}">client.navigation.<a href="./src/unifieddatalibrary/resources/navigation.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/navigation_update_params.py">params</a>) -> None</code>
- <code title="get /udl/navigation">client.navigation.<a href="./src/unifieddatalibrary/resources/navigation.py">list</a>() -> <a href="./src/unifieddatalibrary/types/navigation_list_response.py">NavigationListResponse</a></code>
- <code title="delete /udl/navigation/{id}">client.navigation.<a href="./src/unifieddatalibrary/resources/navigation.py">delete</a>(id) -> None</code>
- <code title="get /udl/navigation/count">client.navigation.<a href="./src/unifieddatalibrary/resources/navigation.py">count</a>() -> str</code>
- <code title="get /udl/navigation/{id}">client.navigation.<a href="./src/unifieddatalibrary/resources/navigation.py">get</a>(id) -> <a href="./src/unifieddatalibrary/types/navigation_get_response.py">NavigationGetResponse</a></code>
- <code title="get /udl/navigation/queryhelp">client.navigation.<a href="./src/unifieddatalibrary/resources/navigation.py">queryhelp</a>() -> None</code>
- <code title="get /udl/navigation/tuple">client.navigation.<a href="./src/unifieddatalibrary/resources/navigation.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/navigation_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/navigation_tuple_response.py">NavigationTupleResponse</a></code>

# Navigationalobstruction

Types:

```python
from unifieddatalibrary.types import (
    NavigationalobstructionListResponse,
    NavigationalobstructionCountResponse,
    NavigationalobstructionGetResponse,
    NavigationalobstructionTupleResponse,
)
```

Methods:

- <code title="post /udl/navigationalobstruction">client.navigationalobstruction.<a href="./src/unifieddatalibrary/resources/navigationalobstruction.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/navigationalobstruction_create_params.py">params</a>) -> None</code>
- <code title="put /udl/navigationalobstruction/{id}">client.navigationalobstruction.<a href="./src/unifieddatalibrary/resources/navigationalobstruction.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/navigationalobstruction_update_params.py">params</a>) -> None</code>
- <code title="get /udl/navigationalobstruction">client.navigationalobstruction.<a href="./src/unifieddatalibrary/resources/navigationalobstruction.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/navigationalobstruction_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/navigationalobstruction_list_response.py">NavigationalobstructionListResponse</a></code>
- <code title="get /udl/navigationalobstruction/count">client.navigationalobstruction.<a href="./src/unifieddatalibrary/resources/navigationalobstruction.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/navigationalobstruction_count_params.py">params</a>) -> str</code>
- <code title="post /udl/navigationalobstruction/createBulk">client.navigationalobstruction.<a href="./src/unifieddatalibrary/resources/navigationalobstruction.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/navigationalobstruction_create_bulk_params.py">params</a>) -> None</code>
- <code title="get /udl/navigationalobstruction/{id}">client.navigationalobstruction.<a href="./src/unifieddatalibrary/resources/navigationalobstruction.py">get</a>(id) -> <a href="./src/unifieddatalibrary/types/navigationalobstruction_get_response.py">NavigationalobstructionGetResponse</a></code>
- <code title="get /udl/navigationalobstruction/queryhelp">client.navigationalobstruction.<a href="./src/unifieddatalibrary/resources/navigationalobstruction.py">queryhelp</a>() -> None</code>
- <code title="get /udl/navigationalobstruction/tuple">client.navigationalobstruction.<a href="./src/unifieddatalibrary/resources/navigationalobstruction.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/navigationalobstruction_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/navigationalobstruction_tuple_response.py">NavigationalobstructionTupleResponse</a></code>

# Notification

Types:

```python
from unifieddatalibrary.types import (
    NotificationListResponse,
    NotificationCountResponse,
    NotificationTupleResponse,
)
```

Methods:

- <code title="post /udl/notification">client.notification.<a href="./src/unifieddatalibrary/resources/notification.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/notification_create_params.py">params</a>) -> None</code>
- <code title="get /udl/notification">client.notification.<a href="./src/unifieddatalibrary/resources/notification.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/notification_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/notification_list_response.py">NotificationListResponse</a></code>
- <code title="get /udl/notification/count">client.notification.<a href="./src/unifieddatalibrary/resources/notification.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/notification_count_params.py">params</a>) -> str</code>
- <code title="post /udl/notification/createRaw">client.notification.<a href="./src/unifieddatalibrary/resources/notification.py">create_raw</a>(\*\*<a href="src/unifieddatalibrary/types/notification_create_raw_params.py">params</a>) -> None</code>
- <code title="get /udl/notification/{id}">client.notification.<a href="./src/unifieddatalibrary/resources/notification.py">get</a>(id) -> <a href="./src/unifieddatalibrary/types/udl/notification/notification_full.py">NotificationFull</a></code>
- <code title="get /udl/notification/queryhelp">client.notification.<a href="./src/unifieddatalibrary/resources/notification.py">queryhelp</a>() -> None</code>
- <code title="get /udl/notification/tuple">client.notification.<a href="./src/unifieddatalibrary/resources/notification.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/notification_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/notification_tuple_response.py">NotificationTupleResponse</a></code>

# Objectofinterest

Types:

```python
from unifieddatalibrary.types import (
    ObjectofinterestListResponse,
    ObjectofinterestCountResponse,
    ObjectofinterestGetResponse,
    ObjectofinterestTupleResponse,
)
```

Methods:

- <code title="post /udl/objectofinterest">client.objectofinterest.<a href="./src/unifieddatalibrary/resources/objectofinterest.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/objectofinterest_create_params.py">params</a>) -> None</code>
- <code title="put /udl/objectofinterest/{id}">client.objectofinterest.<a href="./src/unifieddatalibrary/resources/objectofinterest.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/objectofinterest_update_params.py">params</a>) -> None</code>
- <code title="get /udl/objectofinterest">client.objectofinterest.<a href="./src/unifieddatalibrary/resources/objectofinterest.py">list</a>() -> <a href="./src/unifieddatalibrary/types/objectofinterest_list_response.py">ObjectofinterestListResponse</a></code>
- <code title="delete /udl/objectofinterest/{id}">client.objectofinterest.<a href="./src/unifieddatalibrary/resources/objectofinterest.py">delete</a>(id) -> None</code>
- <code title="get /udl/objectofinterest/count">client.objectofinterest.<a href="./src/unifieddatalibrary/resources/objectofinterest.py">count</a>() -> str</code>
- <code title="get /udl/objectofinterest/{id}">client.objectofinterest.<a href="./src/unifieddatalibrary/resources/objectofinterest.py">get</a>(id) -> <a href="./src/unifieddatalibrary/types/objectofinterest_get_response.py">ObjectofinterestGetResponse</a></code>
- <code title="get /udl/objectofinterest/queryhelp">client.objectofinterest.<a href="./src/unifieddatalibrary/resources/objectofinterest.py">queryhelp</a>() -> None</code>
- <code title="get /udl/objectofinterest/tuple">client.objectofinterest.<a href="./src/unifieddatalibrary/resources/objectofinterest.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/objectofinterest_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/objectofinterest_tuple_response.py">ObjectofinterestTupleResponse</a></code>

# Observations

## Ecpsdr

Types:

```python
from unifieddatalibrary.types.observations import (
    Ecpsdr,
    EcpsdrAbridged,
    EcpsdrListResponse,
    EcpsdrCountResponse,
    EcpsdrTupleResponse,
)
```

Methods:

- <code title="post /udl/ecpsdr">client.observations.ecpsdr.<a href="./src/unifieddatalibrary/resources/observations/ecpsdr.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/observations/ecpsdr_create_params.py">params</a>) -> None</code>
- <code title="get /udl/ecpsdr/{id}">client.observations.ecpsdr.<a href="./src/unifieddatalibrary/resources/observations/ecpsdr.py">retrieve</a>(id) -> <a href="./src/unifieddatalibrary/types/observations/ecpsdr.py">Ecpsdr</a></code>
- <code title="get /udl/ecpsdr">client.observations.ecpsdr.<a href="./src/unifieddatalibrary/resources/observations/ecpsdr.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/observations/ecpsdr_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/observations/ecpsdr_list_response.py">EcpsdrListResponse</a></code>
- <code title="get /udl/ecpsdr/count">client.observations.ecpsdr.<a href="./src/unifieddatalibrary/resources/observations/ecpsdr.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/observations/ecpsdr_count_params.py">params</a>) -> str</code>
- <code title="post /udl/ecpsdr/createBulk">client.observations.ecpsdr.<a href="./src/unifieddatalibrary/resources/observations/ecpsdr.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/observations/ecpsdr_create_bulk_params.py">params</a>) -> None</code>
- <code title="get /udl/ecpsdr/queryhelp">client.observations.ecpsdr.<a href="./src/unifieddatalibrary/resources/observations/ecpsdr.py">query_help</a>() -> None</code>
- <code title="get /udl/ecpsdr/tuple">client.observations.ecpsdr.<a href="./src/unifieddatalibrary/resources/observations/ecpsdr.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/observations/ecpsdr_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/observations/ecpsdr_tuple_response.py">EcpsdrTupleResponse</a></code>

## Monoradar

Methods:

- <code title="post /filedrop/monoradar">client.observations.monoradar.<a href="./src/unifieddatalibrary/resources/observations/monoradar/monoradar.py">create_bulk_v2</a>(\*\*<a href="src/unifieddatalibrary/types/observations/monoradar_create_bulk_v2_params.py">params</a>) -> None</code>

### History

Types:

```python
from unifieddatalibrary.types.observations.monoradar import (
    HistoryCountResponse,
    HistoryQueryResponse,
)
```

Methods:

- <code title="get /udl/monoradar/history/aodr">client.observations.monoradar.history.<a href="./src/unifieddatalibrary/resources/observations/monoradar/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/observations/monoradar/history_aodr_params.py">params</a>) -> None</code>
- <code title="get /udl/monoradar/history/count">client.observations.monoradar.history.<a href="./src/unifieddatalibrary/resources/observations/monoradar/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/observations/monoradar/history_count_params.py">params</a>) -> str</code>
- <code title="get /udl/monoradar/history">client.observations.monoradar.history.<a href="./src/unifieddatalibrary/resources/observations/monoradar/history.py">query</a>(\*\*<a href="src/unifieddatalibrary/types/observations/monoradar/history_query_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/observations/monoradar/history_query_response.py">HistoryQueryResponse</a></code>

## Swir

Methods:

- <code title="post /filedrop/swir">client.observations.swir.<a href="./src/unifieddatalibrary/resources/observations/swir.py">create_bulk_v2</a>(\*\*<a href="src/unifieddatalibrary/types/observations/swir_create_bulk_v2_params.py">params</a>) -> None</code>

## Radarobservation

### History

Types:

```python
from unifieddatalibrary.types.observations.radarobservation import (
    HistoryListResponse,
    HistoryCountResponse,
)
```

Methods:

- <code title="get /udl/radarobservation/history">client.observations.radarobservation.history.<a href="./src/unifieddatalibrary/resources/observations/radarobservation/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/observations/radarobservation/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/observations/radarobservation/history_list_response.py">HistoryListResponse</a></code>
- <code title="get /udl/radarobservation/history/aodr">client.observations.radarobservation.history.<a href="./src/unifieddatalibrary/resources/observations/radarobservation/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/observations/radarobservation/history_aodr_params.py">params</a>) -> None</code>
- <code title="get /udl/radarobservation/history/count">client.observations.radarobservation.history.<a href="./src/unifieddatalibrary/resources/observations/radarobservation/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/observations/radarobservation/history_count_params.py">params</a>) -> str</code>

## Rfobservation

### History

Types:

```python
from unifieddatalibrary.types.observations.rfobservation import HistoryListResponse
```

Methods:

- <code title="get /udl/rfobservation/history">client.observations.rfobservation.history.<a href="./src/unifieddatalibrary/resources/observations/rfobservation/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/observations/rfobservation/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/observations/rfobservation/history_list_response.py">HistoryListResponse</a></code>
- <code title="get /udl/rfobservation/history/aodr">client.observations.rfobservation.history.<a href="./src/unifieddatalibrary/resources/observations/rfobservation/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/observations/rfobservation/history_aodr_params.py">params</a>) -> None</code>

# Onboardnavigation

Types:

```python
from unifieddatalibrary.types import (
    OnboardnavigationListResponse,
    OnboardnavigationCountResponse,
    OnboardnavigationTupleResponse,
)
```

Methods:

- <code title="get /udl/onboardnavigation">client.onboardnavigation.<a href="./src/unifieddatalibrary/resources/onboardnavigation.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/onboardnavigation_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/onboardnavigation_list_response.py">OnboardnavigationListResponse</a></code>
- <code title="get /udl/onboardnavigation/count">client.onboardnavigation.<a href="./src/unifieddatalibrary/resources/onboardnavigation.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/onboardnavigation_count_params.py">params</a>) -> str</code>
- <code title="post /udl/onboardnavigation/createBulk">client.onboardnavigation.<a href="./src/unifieddatalibrary/resources/onboardnavigation.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/onboardnavigation_create_bulk_params.py">params</a>) -> None</code>
- <code title="post /filedrop/udl-onboardnavigation">client.onboardnavigation.<a href="./src/unifieddatalibrary/resources/onboardnavigation.py">create_bulk_v2</a>(\*\*<a href="src/unifieddatalibrary/types/onboardnavigation_create_bulk_v2_params.py">params</a>) -> None</code>
- <code title="get /udl/onboardnavigation/queryhelp">client.onboardnavigation.<a href="./src/unifieddatalibrary/resources/onboardnavigation.py">queryhelp</a>() -> None</code>
- <code title="get /udl/onboardnavigation/tuple">client.onboardnavigation.<a href="./src/unifieddatalibrary/resources/onboardnavigation.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/onboardnavigation_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/onboardnavigation_tuple_response.py">OnboardnavigationTupleResponse</a></code>

# Onorbit

Types:

```python
from unifieddatalibrary.types import (
    OnorbitIngest,
    OnorbitListResponse,
    OnorbitCountResponse,
    OnorbitGetSignatureResponse,
    OnorbitTupleResponse,
)
```

Methods:

- <code title="post /udl/onorbit">client.onorbit.<a href="./src/unifieddatalibrary/resources/onorbit/onorbit.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/onorbit_create_params.py">params</a>) -> None</code>
- <code title="put /udl/onorbit/{id}">client.onorbit.<a href="./src/unifieddatalibrary/resources/onorbit/onorbit.py">update</a>(id, \*\*<a href="src/unifieddatalibrary/types/onorbit_update_params.py">params</a>) -> None</code>
- <code title="get /udl/onorbit">client.onorbit.<a href="./src/unifieddatalibrary/resources/onorbit/onorbit.py">list</a>() -> <a href="./src/unifieddatalibrary/types/onorbit_list_response.py">OnorbitListResponse</a></code>
- <code title="delete /udl/onorbit/{id}">client.onorbit.<a href="./src/unifieddatalibrary/resources/onorbit/onorbit.py">delete</a>(id) -> None</code>
- <code title="get /udl/onorbit/count">client.onorbit.<a href="./src/unifieddatalibrary/resources/onorbit/onorbit.py">count</a>() -> str</code>
- <code title="get /udl/onorbit/{id}">client.onorbit.<a href="./src/unifieddatalibrary/resources/onorbit/onorbit.py">get</a>(id) -> <a href="./src/unifieddatalibrary/types/shared/onorbit.py">Onorbit</a></code>
- <code title="get /udl/onorbit/getSignature">client.onorbit.<a href="./src/unifieddatalibrary/resources/onorbit/onorbit.py">get_signature</a>(\*\*<a href="src/unifieddatalibrary/types/onorbit_get_signature_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/onorbit_get_signature_response.py">OnorbitGetSignatureResponse</a></code>
- <code title="get /udl/onorbit/queryhelp">client.onorbit.<a href="./src/unifieddatalibrary/resources/onorbit/onorbit.py">queryhelp</a>() -> None</code>
- <code title="get /udl/onorbit/tuple">client.onorbit.<a href="./src/unifieddatalibrary/resources/onorbit/onorbit.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/onorbit_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/onorbit_tuple_response.py">OnorbitTupleResponse</a></code>

## AntennaDetails

Types:

```python
from unifieddatalibrary.types.onorbit import (
    AntennaDetailsAbridged,
    AntennaDetailsFull,
    AntennaDetailListResponse,
)
```

Methods:

- <code title="post /udl/antennadetails">client.onorbit.antenna_details.<a href="./src/unifieddatalibrary/resources/onorbit/antenna_details.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/onorbit/antenna_detail_create_params.py">params</a>) -> None</code>
- <code title="get /udl/antennadetails/{id}">client.onorbit.antenna_details.<a href="./src/unifieddatalibrary/resources/onorbit/antenna_details.py">retrieve</a>(id) -> <a href="./src/unifieddatalibrary/types/onorbit/antenna_details_full.py">AntennaDetailsFull</a></code>
- <code title="put /udl/antennadetails/{id}">client.onorbit.antenna_details.<a href="./src/unifieddatalibrary/resources/onorbit/antenna_details.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/onorbit/antenna_detail_update_params.py">params</a>) -> None</code>
- <code title="get /udl/antennadetails">client.onorbit.antenna_details.<a href="./src/unifieddatalibrary/resources/onorbit/antenna_details.py">list</a>() -> <a href="./src/unifieddatalibrary/types/onorbit/antenna_detail_list_response.py">AntennaDetailListResponse</a></code>
- <code title="delete /udl/antennadetails/{id}">client.onorbit.antenna_details.<a href="./src/unifieddatalibrary/resources/onorbit/antenna_details.py">delete</a>(id) -> None</code>

# Onorbitantenna

Types:

```python
from unifieddatalibrary.types import OnorbitantennaListResponse, OnorbitantennaGetResponse
```

Methods:

- <code title="post /udl/onorbitantenna">client.onorbitantenna.<a href="./src/unifieddatalibrary/resources/onorbitantenna.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/onorbitantenna_create_params.py">params</a>) -> None</code>
- <code title="put /udl/onorbitantenna/{id}">client.onorbitantenna.<a href="./src/unifieddatalibrary/resources/onorbitantenna.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/onorbitantenna_update_params.py">params</a>) -> None</code>
- <code title="get /udl/onorbitantenna">client.onorbitantenna.<a href="./src/unifieddatalibrary/resources/onorbitantenna.py">list</a>() -> <a href="./src/unifieddatalibrary/types/onorbitantenna_list_response.py">OnorbitantennaListResponse</a></code>
- <code title="delete /udl/onorbitantenna/{id}">client.onorbitantenna.<a href="./src/unifieddatalibrary/resources/onorbitantenna.py">delete</a>(id) -> None</code>
- <code title="get /udl/onorbitantenna/{id}">client.onorbitantenna.<a href="./src/unifieddatalibrary/resources/onorbitantenna.py">get</a>(id) -> <a href="./src/unifieddatalibrary/types/onorbitantenna_get_response.py">OnorbitantennaGetResponse</a></code>

# Onorbitbattery

Types:

```python
from unifieddatalibrary.types import OnorbitbatteryListResponse, OnorbitbatteryGetResponse
```

Methods:

- <code title="post /udl/onorbitbattery">client.onorbitbattery.<a href="./src/unifieddatalibrary/resources/onorbitbattery.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/onorbitbattery_create_params.py">params</a>) -> None</code>
- <code title="put /udl/onorbitbattery/{id}">client.onorbitbattery.<a href="./src/unifieddatalibrary/resources/onorbitbattery.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/onorbitbattery_update_params.py">params</a>) -> None</code>
- <code title="get /udl/onorbitbattery">client.onorbitbattery.<a href="./src/unifieddatalibrary/resources/onorbitbattery.py">list</a>() -> <a href="./src/unifieddatalibrary/types/onorbitbattery_list_response.py">OnorbitbatteryListResponse</a></code>
- <code title="delete /udl/onorbitbattery/{id}">client.onorbitbattery.<a href="./src/unifieddatalibrary/resources/onorbitbattery.py">delete</a>(id) -> None</code>
- <code title="get /udl/onorbitbattery/{id}">client.onorbitbattery.<a href="./src/unifieddatalibrary/resources/onorbitbattery.py">get</a>(id) -> <a href="./src/unifieddatalibrary/types/onorbitbattery_get_response.py">OnorbitbatteryGetResponse</a></code>

# Onorbitdetails

Types:

```python
from unifieddatalibrary.types import OnorbitdetailListResponse, OnorbitdetailGetResponse
```

Methods:

- <code title="post /udl/onorbitdetails">client.onorbitdetails.<a href="./src/unifieddatalibrary/resources/onorbitdetails.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/onorbitdetail_create_params.py">params</a>) -> None</code>
- <code title="put /udl/onorbitdetails/{id}">client.onorbitdetails.<a href="./src/unifieddatalibrary/resources/onorbitdetails.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/onorbitdetail_update_params.py">params</a>) -> None</code>
- <code title="get /udl/onorbitdetails">client.onorbitdetails.<a href="./src/unifieddatalibrary/resources/onorbitdetails.py">list</a>() -> <a href="./src/unifieddatalibrary/types/onorbitdetail_list_response.py">OnorbitdetailListResponse</a></code>
- <code title="delete /udl/onorbitdetails/{id}">client.onorbitdetails.<a href="./src/unifieddatalibrary/resources/onorbitdetails.py">delete</a>(id) -> None</code>
- <code title="get /udl/onorbitdetails/{id}">client.onorbitdetails.<a href="./src/unifieddatalibrary/resources/onorbitdetails.py">get</a>(id) -> <a href="./src/unifieddatalibrary/types/onorbitdetail_get_response.py">OnorbitdetailGetResponse</a></code>

# Onorbitevent

Types:

```python
from unifieddatalibrary.types import (
    OnorbiteventListResponse,
    OnorbiteventCountResponse,
    OnorbiteventGetResponse,
    OnorbiteventTupleResponse,
)
```

Methods:

- <code title="post /udl/onorbitevent">client.onorbitevent.<a href="./src/unifieddatalibrary/resources/onorbitevent.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/onorbitevent_create_params.py">params</a>) -> None</code>
- <code title="put /udl/onorbitevent/{id}">client.onorbitevent.<a href="./src/unifieddatalibrary/resources/onorbitevent.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/onorbitevent_update_params.py">params</a>) -> None</code>
- <code title="get /udl/onorbitevent">client.onorbitevent.<a href="./src/unifieddatalibrary/resources/onorbitevent.py">list</a>() -> <a href="./src/unifieddatalibrary/types/onorbitevent_list_response.py">OnorbiteventListResponse</a></code>
- <code title="delete /udl/onorbitevent/{id}">client.onorbitevent.<a href="./src/unifieddatalibrary/resources/onorbitevent.py">delete</a>(id) -> None</code>
- <code title="get /udl/onorbitevent/count">client.onorbitevent.<a href="./src/unifieddatalibrary/resources/onorbitevent.py">count</a>() -> str</code>
- <code title="get /udl/onorbitevent/{id}">client.onorbitevent.<a href="./src/unifieddatalibrary/resources/onorbitevent.py">get</a>(id) -> <a href="./src/unifieddatalibrary/types/onorbitevent_get_response.py">OnorbiteventGetResponse</a></code>
- <code title="get /udl/onorbitevent/queryhelp">client.onorbitevent.<a href="./src/unifieddatalibrary/resources/onorbitevent.py">queryhelp</a>() -> None</code>
- <code title="get /udl/onorbitevent/tuple">client.onorbitevent.<a href="./src/unifieddatalibrary/resources/onorbitevent.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/onorbitevent_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/onorbitevent_tuple_response.py">OnorbiteventTupleResponse</a></code>

# Onorbitlist

Types:

```python
from unifieddatalibrary.types import (
    OnorbitlistListResponse,
    OnorbitlistCountResponse,
    OnorbitlistGetResponse,
    OnorbitlistTupleResponse,
)
```

Methods:

- <code title="post /udl/onorbitlist">client.onorbitlist.<a href="./src/unifieddatalibrary/resources/onorbitlist.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/onorbitlist_create_params.py">params</a>) -> None</code>
- <code title="put /udl/onorbitlist/{id}">client.onorbitlist.<a href="./src/unifieddatalibrary/resources/onorbitlist.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/onorbitlist_update_params.py">params</a>) -> None</code>
- <code title="get /udl/onorbitlist">client.onorbitlist.<a href="./src/unifieddatalibrary/resources/onorbitlist.py">list</a>() -> <a href="./src/unifieddatalibrary/types/onorbitlist_list_response.py">OnorbitlistListResponse</a></code>
- <code title="delete /udl/onorbitlist/{id}">client.onorbitlist.<a href="./src/unifieddatalibrary/resources/onorbitlist.py">delete</a>(id) -> None</code>
- <code title="get /udl/onorbitlist/count">client.onorbitlist.<a href="./src/unifieddatalibrary/resources/onorbitlist.py">count</a>() -> str</code>
- <code title="get /udl/onorbitlist/{id}">client.onorbitlist.<a href="./src/unifieddatalibrary/resources/onorbitlist.py">get</a>(id) -> <a href="./src/unifieddatalibrary/types/onorbitlist_get_response.py">OnorbitlistGetResponse</a></code>
- <code title="get /udl/onorbitlist/queryhelp">client.onorbitlist.<a href="./src/unifieddatalibrary/resources/onorbitlist.py">queryhelp</a>() -> None</code>
- <code title="get /udl/onorbitlist/tuple">client.onorbitlist.<a href="./src/unifieddatalibrary/resources/onorbitlist.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/onorbitlist_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/onorbitlist_tuple_response.py">OnorbitlistTupleResponse</a></code>

# Onorbitsolararray

Types:

```python
from unifieddatalibrary.types import OnorbitsolararrayListResponse, OnorbitsolararrayGetResponse
```

Methods:

- <code title="post /udl/onorbitsolararray">client.onorbitsolararray.<a href="./src/unifieddatalibrary/resources/onorbitsolararray.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/onorbitsolararray_create_params.py">params</a>) -> None</code>
- <code title="put /udl/onorbitsolararray/{id}">client.onorbitsolararray.<a href="./src/unifieddatalibrary/resources/onorbitsolararray.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/onorbitsolararray_update_params.py">params</a>) -> None</code>
- <code title="get /udl/onorbitsolararray">client.onorbitsolararray.<a href="./src/unifieddatalibrary/resources/onorbitsolararray.py">list</a>() -> <a href="./src/unifieddatalibrary/types/onorbitsolararray_list_response.py">OnorbitsolararrayListResponse</a></code>
- <code title="delete /udl/onorbitsolararray/{id}">client.onorbitsolararray.<a href="./src/unifieddatalibrary/resources/onorbitsolararray.py">delete</a>(id) -> None</code>
- <code title="get /udl/onorbitsolararray/{id}">client.onorbitsolararray.<a href="./src/unifieddatalibrary/resources/onorbitsolararray.py">get</a>(id) -> <a href="./src/unifieddatalibrary/types/onorbitsolararray_get_response.py">OnorbitsolararrayGetResponse</a></code>

# Onorbitthruster

Types:

```python
from unifieddatalibrary.types import OnorbitthrusterListResponse, OnorbitthrusterGetResponse
```

Methods:

- <code title="post /udl/onorbitthruster">client.onorbitthruster.<a href="./src/unifieddatalibrary/resources/onorbitthruster.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/onorbitthruster_create_params.py">params</a>) -> None</code>
- <code title="put /udl/onorbitthruster/{id}">client.onorbitthruster.<a href="./src/unifieddatalibrary/resources/onorbitthruster.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/onorbitthruster_update_params.py">params</a>) -> None</code>
- <code title="get /udl/onorbitthruster">client.onorbitthruster.<a href="./src/unifieddatalibrary/resources/onorbitthruster.py">list</a>() -> <a href="./src/unifieddatalibrary/types/onorbitthruster_list_response.py">OnorbitthrusterListResponse</a></code>
- <code title="delete /udl/onorbitthruster/{id}">client.onorbitthruster.<a href="./src/unifieddatalibrary/resources/onorbitthruster.py">delete</a>(id) -> None</code>
- <code title="get /udl/onorbitthruster/{id}">client.onorbitthruster.<a href="./src/unifieddatalibrary/resources/onorbitthruster.py">get</a>(id) -> <a href="./src/unifieddatalibrary/types/onorbitthruster_get_response.py">OnorbitthrusterGetResponse</a></code>

# Onorbitthrusterstatus

Types:

```python
from unifieddatalibrary.types import (
    OnorbitthrusterstatusListResponse,
    OnorbitthrusterstatusCountResponse,
    OnorbitthrusterstatusTupleResponse,
)
```

Methods:

- <code title="post /udl/onorbitthrusterstatus">client.onorbitthrusterstatus.<a href="./src/unifieddatalibrary/resources/onorbitthrusterstatus/onorbitthrusterstatus.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/onorbitthrusterstatus_create_params.py">params</a>) -> None</code>
- <code title="get /udl/onorbitthrusterstatus">client.onorbitthrusterstatus.<a href="./src/unifieddatalibrary/resources/onorbitthrusterstatus/onorbitthrusterstatus.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/onorbitthrusterstatus_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/onorbitthrusterstatus_list_response.py">OnorbitthrusterstatusListResponse</a></code>
- <code title="delete /udl/onorbitthrusterstatus/{id}">client.onorbitthrusterstatus.<a href="./src/unifieddatalibrary/resources/onorbitthrusterstatus/onorbitthrusterstatus.py">delete</a>(id) -> None</code>
- <code title="get /udl/onorbitthrusterstatus/count">client.onorbitthrusterstatus.<a href="./src/unifieddatalibrary/resources/onorbitthrusterstatus/onorbitthrusterstatus.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/onorbitthrusterstatus_count_params.py">params</a>) -> str</code>
- <code title="post /udl/onorbitthrusterstatus/createBulk">client.onorbitthrusterstatus.<a href="./src/unifieddatalibrary/resources/onorbitthrusterstatus/onorbitthrusterstatus.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/onorbitthrusterstatus_create_bulk_params.py">params</a>) -> None</code>
- <code title="get /udl/onorbitthrusterstatus/{id}">client.onorbitthrusterstatus.<a href="./src/unifieddatalibrary/resources/onorbitthrusterstatus/onorbitthrusterstatus.py">get</a>(id) -> <a href="./src/unifieddatalibrary/types/udl/onorbitthrusterstatus/onorbitthrusterstatus_full.py">OnorbitthrusterstatusFull</a></code>
- <code title="get /udl/onorbitthrusterstatus/queryhelp">client.onorbitthrusterstatus.<a href="./src/unifieddatalibrary/resources/onorbitthrusterstatus/onorbitthrusterstatus.py">queryhelp</a>() -> None</code>
- <code title="get /udl/onorbitthrusterstatus/tuple">client.onorbitthrusterstatus.<a href="./src/unifieddatalibrary/resources/onorbitthrusterstatus/onorbitthrusterstatus.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/onorbitthrusterstatus_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/onorbitthrusterstatus_tuple_response.py">OnorbitthrusterstatusTupleResponse</a></code>

## History

Types:

```python
from unifieddatalibrary.types.onorbitthrusterstatus import HistoryCountResponse
```

Methods:

- <code title="get /udl/onorbitthrusterstatus/history/count">client.onorbitthrusterstatus.history.<a href="./src/unifieddatalibrary/resources/onorbitthrusterstatus/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/onorbitthrusterstatus/history_count_params.py">params</a>) -> str</code>

# Operatingunit

Types:

```python
from unifieddatalibrary.types import (
    OperatingunitListResponse,
    OperatingunitCountResponse,
    OperatingunitGetResponse,
    OperatingunitTupleResponse,
)
```

Methods:

- <code title="post /udl/operatingunit">client.operatingunit.<a href="./src/unifieddatalibrary/resources/operatingunit.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/operatingunit_create_params.py">params</a>) -> None</code>
- <code title="put /udl/operatingunit/{id}">client.operatingunit.<a href="./src/unifieddatalibrary/resources/operatingunit.py">update</a>(id, \*\*<a href="src/unifieddatalibrary/types/operatingunit_update_params.py">params</a>) -> None</code>
- <code title="get /udl/operatingunit">client.operatingunit.<a href="./src/unifieddatalibrary/resources/operatingunit.py">list</a>() -> <a href="./src/unifieddatalibrary/types/operatingunit_list_response.py">OperatingunitListResponse</a></code>
- <code title="delete /udl/operatingunit/{id}">client.operatingunit.<a href="./src/unifieddatalibrary/resources/operatingunit.py">delete</a>(id) -> None</code>
- <code title="get /udl/operatingunit/count">client.operatingunit.<a href="./src/unifieddatalibrary/resources/operatingunit.py">count</a>() -> str</code>
- <code title="get /udl/operatingunit/{id}">client.operatingunit.<a href="./src/unifieddatalibrary/resources/operatingunit.py">get</a>(id) -> <a href="./src/unifieddatalibrary/types/operatingunit_get_response.py">OperatingunitGetResponse</a></code>
- <code title="get /udl/operatingunit/queryhelp">client.operatingunit.<a href="./src/unifieddatalibrary/resources/operatingunit.py">queryhelp</a>() -> None</code>
- <code title="get /udl/operatingunit/tuple">client.operatingunit.<a href="./src/unifieddatalibrary/resources/operatingunit.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/operatingunit_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/operatingunit_tuple_response.py">OperatingunitTupleResponse</a></code>

# Operatingunitremark

Types:

```python
from unifieddatalibrary.types import (
    OperatingunitremarkListResponse,
    OperatingunitremarkCountResponse,
    OperatingunitremarkGetResponse,
    OperatingunitremarkTupleResponse,
)
```

Methods:

- <code title="post /udl/operatingunitremark">client.operatingunitremark.<a href="./src/unifieddatalibrary/resources/operatingunitremark.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/operatingunitremark_create_params.py">params</a>) -> None</code>
- <code title="get /udl/operatingunitremark">client.operatingunitremark.<a href="./src/unifieddatalibrary/resources/operatingunitremark.py">list</a>() -> <a href="./src/unifieddatalibrary/types/operatingunitremark_list_response.py">OperatingunitremarkListResponse</a></code>
- <code title="get /udl/operatingunitremark/count">client.operatingunitremark.<a href="./src/unifieddatalibrary/resources/operatingunitremark.py">count</a>() -> str</code>
- <code title="post /udl/operatingunitremark/createBulk">client.operatingunitremark.<a href="./src/unifieddatalibrary/resources/operatingunitremark.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/operatingunitremark_create_bulk_params.py">params</a>) -> None</code>
- <code title="get /udl/operatingunitremark/{id}">client.operatingunitremark.<a href="./src/unifieddatalibrary/resources/operatingunitremark.py">get</a>(id) -> <a href="./src/unifieddatalibrary/types/operatingunitremark_get_response.py">OperatingunitremarkGetResponse</a></code>
- <code title="get /udl/operatingunitremark/queryhelp">client.operatingunitremark.<a href="./src/unifieddatalibrary/resources/operatingunitremark.py">queryhelp</a>() -> None</code>
- <code title="get /udl/operatingunitremark/tuple">client.operatingunitremark.<a href="./src/unifieddatalibrary/resources/operatingunitremark.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/operatingunitremark_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/operatingunitremark_tuple_response.py">OperatingunitremarkTupleResponse</a></code>

# Orbitdetermination

Types:

```python
from unifieddatalibrary.types import (
    OrbitdeterminationListResponse,
    OrbitdeterminationCountResponse,
    OrbitdeterminationTupleResponse,
)
```

Methods:

- <code title="post /udl/orbitdetermination">client.orbitdetermination.<a href="./src/unifieddatalibrary/resources/orbitdetermination/orbitdetermination.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/orbitdetermination_create_params.py">params</a>) -> None</code>
- <code title="get /udl/orbitdetermination">client.orbitdetermination.<a href="./src/unifieddatalibrary/resources/orbitdetermination/orbitdetermination.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/orbitdetermination_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/orbitdetermination_list_response.py">OrbitdeterminationListResponse</a></code>
- <code title="get /udl/orbitdetermination/count">client.orbitdetermination.<a href="./src/unifieddatalibrary/resources/orbitdetermination/orbitdetermination.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/orbitdetermination_count_params.py">params</a>) -> str</code>
- <code title="post /udl/orbitdetermination/createBulk">client.orbitdetermination.<a href="./src/unifieddatalibrary/resources/orbitdetermination/orbitdetermination.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/orbitdetermination_create_bulk_params.py">params</a>) -> None</code>
- <code title="post /filedrop/udl-orbitdetermination">client.orbitdetermination.<a href="./src/unifieddatalibrary/resources/orbitdetermination/orbitdetermination.py">create_bulk_v2</a>(\*\*<a href="src/unifieddatalibrary/types/orbitdetermination_create_bulk_v2_params.py">params</a>) -> None</code>
- <code title="get /udl/orbitdetermination/{id}">client.orbitdetermination.<a href="./src/unifieddatalibrary/resources/orbitdetermination/orbitdetermination.py">get</a>(id) -> <a href="./src/unifieddatalibrary/types/udl/orbitdetermination/orbitdetermination_full.py">OrbitdeterminationFull</a></code>
- <code title="get /udl/orbitdetermination/queryhelp">client.orbitdetermination.<a href="./src/unifieddatalibrary/resources/orbitdetermination/orbitdetermination.py">queryhelp</a>() -> None</code>
- <code title="get /udl/orbitdetermination/tuple">client.orbitdetermination.<a href="./src/unifieddatalibrary/resources/orbitdetermination/orbitdetermination.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/orbitdetermination_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/orbitdetermination_tuple_response.py">OrbitdeterminationTupleResponse</a></code>

## History

Types:

```python
from unifieddatalibrary.types.orbitdetermination import HistoryListResponse, HistoryCountResponse
```

Methods:

- <code title="get /udl/orbitdetermination/history">client.orbitdetermination.history.<a href="./src/unifieddatalibrary/resources/orbitdetermination/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/orbitdetermination/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/orbitdetermination/history_list_response.py">HistoryListResponse</a></code>
- <code title="get /udl/orbitdetermination/history/aodr">client.orbitdetermination.history.<a href="./src/unifieddatalibrary/resources/orbitdetermination/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/orbitdetermination/history_aodr_params.py">params</a>) -> None</code>
- <code title="get /udl/orbitdetermination/history/count">client.orbitdetermination.history.<a href="./src/unifieddatalibrary/resources/orbitdetermination/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/orbitdetermination/history_count_params.py">params</a>) -> str</code>

# Orbittrack

Types:

```python
from unifieddatalibrary.types import (
    OrbittrackListResponse,
    OrbittrackCountResponse,
    OrbittrackTupleResponse,
)
```

Methods:

- <code title="get /udl/orbittrack">client.orbittrack.<a href="./src/unifieddatalibrary/resources/orbittrack/orbittrack.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/orbittrack_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/orbittrack_list_response.py">OrbittrackListResponse</a></code>
- <code title="get /udl/orbittrack/count">client.orbittrack.<a href="./src/unifieddatalibrary/resources/orbittrack/orbittrack.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/orbittrack_count_params.py">params</a>) -> str</code>
- <code title="post /udl/orbittrack/createBulk">client.orbittrack.<a href="./src/unifieddatalibrary/resources/orbittrack/orbittrack.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/orbittrack_create_bulk_params.py">params</a>) -> None</code>
- <code title="post /filedrop/udl-orbittrack">client.orbittrack.<a href="./src/unifieddatalibrary/resources/orbittrack/orbittrack.py">create_bulk_v2</a>(\*\*<a href="src/unifieddatalibrary/types/orbittrack_create_bulk_v2_params.py">params</a>) -> None</code>
- <code title="get /udl/orbittrack/queryhelp">client.orbittrack.<a href="./src/unifieddatalibrary/resources/orbittrack/orbittrack.py">queryhelp</a>() -> None</code>
- <code title="get /udl/orbittrack/tuple">client.orbittrack.<a href="./src/unifieddatalibrary/resources/orbittrack/orbittrack.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/orbittrack_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/orbittrack_tuple_response.py">OrbittrackTupleResponse</a></code>

## History

Types:

```python
from unifieddatalibrary.types.orbittrack import HistoryListResponse, HistoryCountResponse
```

Methods:

- <code title="get /udl/orbittrack/history">client.orbittrack.history.<a href="./src/unifieddatalibrary/resources/orbittrack/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/orbittrack/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/orbittrack/history_list_response.py">HistoryListResponse</a></code>
- <code title="get /udl/orbittrack/history/aodr">client.orbittrack.history.<a href="./src/unifieddatalibrary/resources/orbittrack/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/orbittrack/history_aodr_params.py">params</a>) -> None</code>
- <code title="get /udl/orbittrack/history/count">client.orbittrack.history.<a href="./src/unifieddatalibrary/resources/orbittrack/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/orbittrack/history_count_params.py">params</a>) -> str</code>

# Organization

Types:

```python
from unifieddatalibrary.types import (
    OrganizationFull,
    OrganizationListResponse,
    OrganizationCountResponse,
    OrganizationGetOrganizationCategoriesResponse,
    OrganizationGetOrganizationTypesResponse,
    OrganizationTupleResponse,
)
```

Methods:

- <code title="post /udl/organization">client.organization.<a href="./src/unifieddatalibrary/resources/organization.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/organization_create_params.py">params</a>) -> None</code>
- <code title="put /udl/organization/{id}">client.organization.<a href="./src/unifieddatalibrary/resources/organization.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/organization_update_params.py">params</a>) -> None</code>
- <code title="get /udl/organization">client.organization.<a href="./src/unifieddatalibrary/resources/organization.py">list</a>() -> <a href="./src/unifieddatalibrary/types/organization_list_response.py">OrganizationListResponse</a></code>
- <code title="delete /udl/organization/{id}">client.organization.<a href="./src/unifieddatalibrary/resources/organization.py">delete</a>(id) -> None</code>
- <code title="get /udl/organization/count">client.organization.<a href="./src/unifieddatalibrary/resources/organization.py">count</a>() -> str</code>
- <code title="get /udl/organization/{id}">client.organization.<a href="./src/unifieddatalibrary/resources/organization.py">get</a>(id) -> <a href="./src/unifieddatalibrary/types/organization_full.py">OrganizationFull</a></code>
- <code title="get /udl/organization/getOrganizationCategories">client.organization.<a href="./src/unifieddatalibrary/resources/organization.py">get_organization_categories</a>() -> <a href="./src/unifieddatalibrary/types/organization_get_organization_categories_response.py">OrganizationGetOrganizationCategoriesResponse</a></code>
- <code title="get /udl/organization/getOrganizationTypes">client.organization.<a href="./src/unifieddatalibrary/resources/organization.py">get_organization_types</a>() -> <a href="./src/unifieddatalibrary/types/organization_get_organization_types_response.py">OrganizationGetOrganizationTypesResponse</a></code>
- <code title="get /udl/organization/queryhelp">client.organization.<a href="./src/unifieddatalibrary/resources/organization.py">queryhelp</a>() -> None</code>
- <code title="get /udl/organization/tuple">client.organization.<a href="./src/unifieddatalibrary/resources/organization.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/organization_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/organization_tuple_response.py">OrganizationTupleResponse</a></code>

# Organizationdetails

Types:

```python
from unifieddatalibrary.types import (
    OrganizationDetailsFull,
    OrganizationdetailListResponse,
    OrganizationdetailFindBySourceResponse,
)
```

Methods:

- <code title="post /udl/organizationdetails">client.organizationdetails.<a href="./src/unifieddatalibrary/resources/organizationdetails.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/organizationdetail_create_params.py">params</a>) -> None</code>
- <code title="put /udl/organizationdetails/{id}">client.organizationdetails.<a href="./src/unifieddatalibrary/resources/organizationdetails.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/organizationdetail_update_params.py">params</a>) -> None</code>
- <code title="get /udl/organizationdetails">client.organizationdetails.<a href="./src/unifieddatalibrary/resources/organizationdetails.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/organizationdetail_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/organizationdetail_list_response.py">OrganizationdetailListResponse</a></code>
- <code title="delete /udl/organizationdetails/{id}">client.organizationdetails.<a href="./src/unifieddatalibrary/resources/organizationdetails.py">delete</a>(id) -> None</code>
- <code title="get /udl/organizationdetails/findBySource">client.organizationdetails.<a href="./src/unifieddatalibrary/resources/organizationdetails.py">find_by_source</a>(\*\*<a href="src/unifieddatalibrary/types/organizationdetail_find_by_source_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/organizationdetail_find_by_source_response.py">OrganizationdetailFindBySourceResponse</a></code>
- <code title="get /udl/organizationdetails/{id}">client.organizationdetails.<a href="./src/unifieddatalibrary/resources/organizationdetails.py">get</a>(id) -> <a href="./src/unifieddatalibrary/types/organization_details_full.py">OrganizationDetailsFull</a></code>

# Passiveradarobservation

Types:

```python
from unifieddatalibrary.types import (
    PassiveradarobservationListResponse,
    PassiveradarobservationCountResponse,
    PassiveradarobservationTupleResponse,
)
```

Methods:

- <code title="post /udl/passiveradarobservation">client.passiveradarobservation.<a href="./src/unifieddatalibrary/resources/passiveradarobservation/passiveradarobservation.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/passiveradarobservation_create_params.py">params</a>) -> None</code>
- <code title="get /udl/passiveradarobservation">client.passiveradarobservation.<a href="./src/unifieddatalibrary/resources/passiveradarobservation/passiveradarobservation.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/passiveradarobservation_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/passiveradarobservation_list_response.py">PassiveradarobservationListResponse</a></code>
- <code title="get /udl/passiveradarobservation/count">client.passiveradarobservation.<a href="./src/unifieddatalibrary/resources/passiveradarobservation/passiveradarobservation.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/passiveradarobservation_count_params.py">params</a>) -> str</code>
- <code title="post /udl/passiveradarobservation/createBulk">client.passiveradarobservation.<a href="./src/unifieddatalibrary/resources/passiveradarobservation/passiveradarobservation.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/passiveradarobservation_create_bulk_params.py">params</a>) -> None</code>
- <code title="post /filedrop/udl-passiveradar">client.passiveradarobservation.<a href="./src/unifieddatalibrary/resources/passiveradarobservation/passiveradarobservation.py">file_create</a>(\*\*<a href="src/unifieddatalibrary/types/passiveradarobservation_file_create_params.py">params</a>) -> None</code>
- <code title="get /udl/passiveradarobservation/{id}">client.passiveradarobservation.<a href="./src/unifieddatalibrary/resources/passiveradarobservation/passiveradarobservation.py">get</a>(id) -> <a href="./src/unifieddatalibrary/types/udl/passiveradarobservation/passiveradarobservation_full.py">PassiveradarobservationFull</a></code>
- <code title="get /udl/passiveradarobservation/queryhelp">client.passiveradarobservation.<a href="./src/unifieddatalibrary/resources/passiveradarobservation/passiveradarobservation.py">queryhelp</a>() -> None</code>
- <code title="get /udl/passiveradarobservation/tuple">client.passiveradarobservation.<a href="./src/unifieddatalibrary/resources/passiveradarobservation/passiveradarobservation.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/passiveradarobservation_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/passiveradarobservation_tuple_response.py">PassiveradarobservationTupleResponse</a></code>

## History

Types:

```python
from unifieddatalibrary.types.passiveradarobservation import (
    HistoryListResponse,
    HistoryCountResponse,
)
```

Methods:

- <code title="get /udl/passiveradarobservation/history">client.passiveradarobservation.history.<a href="./src/unifieddatalibrary/resources/passiveradarobservation/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/passiveradarobservation/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/passiveradarobservation/history_list_response.py">HistoryListResponse</a></code>
- <code title="get /udl/passiveradarobservation/history/aodr">client.passiveradarobservation.history.<a href="./src/unifieddatalibrary/resources/passiveradarobservation/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/passiveradarobservation/history_aodr_params.py">params</a>) -> None</code>
- <code title="get /udl/passiveradarobservation/history/count">client.passiveradarobservation.history.<a href="./src/unifieddatalibrary/resources/passiveradarobservation/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/passiveradarobservation/history_count_params.py">params</a>) -> str</code>

# Personnelrecovery

Types:

```python
from unifieddatalibrary.types import (
    PersonnelRecoveryFullL,
    PersonnelrecoveryListResponse,
    PersonnelrecoveryCountResponse,
    PersonnelrecoveryTupleResponse,
)
```

Methods:

- <code title="post /udl/personnelrecovery">client.personnelrecovery.<a href="./src/unifieddatalibrary/resources/personnelrecovery/personnelrecovery.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/personnelrecovery_create_params.py">params</a>) -> None</code>
- <code title="get /udl/personnelrecovery">client.personnelrecovery.<a href="./src/unifieddatalibrary/resources/personnelrecovery/personnelrecovery.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/personnelrecovery_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/personnelrecovery_list_response.py">PersonnelrecoveryListResponse</a></code>
- <code title="get /udl/personnelrecovery/count">client.personnelrecovery.<a href="./src/unifieddatalibrary/resources/personnelrecovery/personnelrecovery.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/personnelrecovery_count_params.py">params</a>) -> str</code>
- <code title="post /udl/personnelrecovery/createBulk">client.personnelrecovery.<a href="./src/unifieddatalibrary/resources/personnelrecovery/personnelrecovery.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/personnelrecovery_create_bulk_params.py">params</a>) -> None</code>
- <code title="post /filedrop/udl-personnelrecovery">client.personnelrecovery.<a href="./src/unifieddatalibrary/resources/personnelrecovery/personnelrecovery.py">file_create</a>(\*\*<a href="src/unifieddatalibrary/types/personnelrecovery_file_create_params.py">params</a>) -> None</code>
- <code title="get /udl/personnelrecovery/{id}">client.personnelrecovery.<a href="./src/unifieddatalibrary/resources/personnelrecovery/personnelrecovery.py">get</a>(id) -> <a href="./src/unifieddatalibrary/types/personnel_recovery_full_l.py">PersonnelRecoveryFullL</a></code>
- <code title="get /udl/personnelrecovery/queryhelp">client.personnelrecovery.<a href="./src/unifieddatalibrary/resources/personnelrecovery/personnelrecovery.py">queryhelp</a>() -> None</code>
- <code title="get /udl/personnelrecovery/tuple">client.personnelrecovery.<a href="./src/unifieddatalibrary/resources/personnelrecovery/personnelrecovery.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/personnelrecovery_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/personnelrecovery_tuple_response.py">PersonnelrecoveryTupleResponse</a></code>

## History

Types:

```python
from unifieddatalibrary.types.personnelrecovery import HistoryListResponse, HistoryCountResponse
```

Methods:

- <code title="get /udl/personnelrecovery/history">client.personnelrecovery.history.<a href="./src/unifieddatalibrary/resources/personnelrecovery/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/personnelrecovery/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/personnelrecovery/history_list_response.py">HistoryListResponse</a></code>
- <code title="get /udl/personnelrecovery/history/count">client.personnelrecovery.history.<a href="./src/unifieddatalibrary/resources/personnelrecovery/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/personnelrecovery/history_count_params.py">params</a>) -> str</code>

# Poi

Types:

```python
from unifieddatalibrary.types import PoiListResponse, PoiCountResponse, PoiTupleResponse
```

Methods:

- <code title="post /udl/poi">client.poi.<a href="./src/unifieddatalibrary/resources/poi.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/poi_create_params.py">params</a>) -> None</code>
- <code title="get /udl/poi">client.poi.<a href="./src/unifieddatalibrary/resources/poi.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/poi_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/poi_list_response.py">PoiListResponse</a></code>
- <code title="get /udl/poi/count">client.poi.<a href="./src/unifieddatalibrary/resources/poi.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/poi_count_params.py">params</a>) -> str</code>
- <code title="post /udl/poi/createBulk">client.poi.<a href="./src/unifieddatalibrary/resources/poi.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/poi_create_bulk_params.py">params</a>) -> None</code>
- <code title="post /filedrop/udl-poi">client.poi.<a href="./src/unifieddatalibrary/resources/poi.py">create_bulk_v2</a>(\*\*<a href="src/unifieddatalibrary/types/poi_create_bulk_v2_params.py">params</a>) -> None</code>
- <code title="get /udl/poi/{id}">client.poi.<a href="./src/unifieddatalibrary/resources/poi.py">get</a>(id) -> <a href="./src/unifieddatalibrary/types/udl/poi/poi_full.py">PoiFull</a></code>
- <code title="get /udl/poi/queryhelp">client.poi.<a href="./src/unifieddatalibrary/resources/poi.py">queryhelp</a>() -> None</code>
- <code title="get /udl/poi/tuple">client.poi.<a href="./src/unifieddatalibrary/resources/poi.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/poi_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/poi_tuple_response.py">PoiTupleResponse</a></code>

# Port

Types:

```python
from unifieddatalibrary.types import (
    PortListResponse,
    PortCountResponse,
    PortGetResponse,
    PortTupleResponse,
)
```

Methods:

- <code title="post /udl/port">client.port.<a href="./src/unifieddatalibrary/resources/port.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/port_create_params.py">params</a>) -> None</code>
- <code title="put /udl/port/{id}">client.port.<a href="./src/unifieddatalibrary/resources/port.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/port_update_params.py">params</a>) -> None</code>
- <code title="get /udl/port">client.port.<a href="./src/unifieddatalibrary/resources/port.py">list</a>() -> <a href="./src/unifieddatalibrary/types/port_list_response.py">PortListResponse</a></code>
- <code title="get /udl/port/count">client.port.<a href="./src/unifieddatalibrary/resources/port.py">count</a>() -> str</code>
- <code title="post /udl/port/createBulk">client.port.<a href="./src/unifieddatalibrary/resources/port.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/port_create_bulk_params.py">params</a>) -> None</code>
- <code title="get /udl/port/{id}">client.port.<a href="./src/unifieddatalibrary/resources/port.py">get</a>(id) -> <a href="./src/unifieddatalibrary/types/port_get_response.py">PortGetResponse</a></code>
- <code title="get /udl/port/queryhelp">client.port.<a href="./src/unifieddatalibrary/resources/port.py">queryhelp</a>() -> None</code>
- <code title="get /udl/port/tuple">client.port.<a href="./src/unifieddatalibrary/resources/port.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/port_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/port_tuple_response.py">PortTupleResponse</a></code>

# Radarobservation

Types:

```python
from unifieddatalibrary.types import (
    RadarobservationListResponse,
    RadarobservationCountResponse,
    RadarobservationTupleResponse,
)
```

Methods:

- <code title="post /udl/radarobservation">client.radarobservation.<a href="./src/unifieddatalibrary/resources/radarobservation.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/radarobservation_create_params.py">params</a>) -> None</code>
- <code title="get /udl/radarobservation">client.radarobservation.<a href="./src/unifieddatalibrary/resources/radarobservation.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/radarobservation_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/radarobservation_list_response.py">RadarobservationListResponse</a></code>
- <code title="get /udl/radarobservation/count">client.radarobservation.<a href="./src/unifieddatalibrary/resources/radarobservation.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/radarobservation_count_params.py">params</a>) -> str</code>
- <code title="post /udl/radarobservation/createBulk">client.radarobservation.<a href="./src/unifieddatalibrary/resources/radarobservation.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/radarobservation_create_bulk_params.py">params</a>) -> None</code>
- <code title="post /filedrop/udl-radar">client.radarobservation.<a href="./src/unifieddatalibrary/resources/radarobservation.py">create_bulk_v2</a>(\*\*<a href="src/unifieddatalibrary/types/radarobservation_create_bulk_v2_params.py">params</a>) -> None</code>
- <code title="get /udl/radarobservation/{id}">client.radarobservation.<a href="./src/unifieddatalibrary/resources/radarobservation.py">get</a>(id) -> <a href="./src/unifieddatalibrary/types/udl/radarobservation/radarobservation_full.py">RadarobservationFull</a></code>
- <code title="get /udl/radarobservation/queryhelp">client.radarobservation.<a href="./src/unifieddatalibrary/resources/radarobservation.py">queryhelp</a>() -> None</code>
- <code title="get /udl/radarobservation/tuple">client.radarobservation.<a href="./src/unifieddatalibrary/resources/radarobservation.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/radarobservation_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/radarobservation_tuple_response.py">RadarobservationTupleResponse</a></code>

# Rfband

Types:

```python
from unifieddatalibrary.types import (
    RfbandListResponse,
    RfbandCountResponse,
    RfbandGetResponse,
    RfbandTupleResponse,
)
```

Methods:

- <code title="post /udl/rfband">client.rfband.<a href="./src/unifieddatalibrary/resources/rfband.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/rfband_create_params.py">params</a>) -> None</code>
- <code title="put /udl/rfband/{id}">client.rfband.<a href="./src/unifieddatalibrary/resources/rfband.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/rfband_update_params.py">params</a>) -> None</code>
- <code title="get /udl/rfband">client.rfband.<a href="./src/unifieddatalibrary/resources/rfband.py">list</a>() -> <a href="./src/unifieddatalibrary/types/rfband_list_response.py">RfbandListResponse</a></code>
- <code title="delete /udl/rfband/{id}">client.rfband.<a href="./src/unifieddatalibrary/resources/rfband.py">delete</a>(id) -> None</code>
- <code title="get /udl/rfband/count">client.rfband.<a href="./src/unifieddatalibrary/resources/rfband.py">count</a>() -> str</code>
- <code title="get /udl/rfband/{id}">client.rfband.<a href="./src/unifieddatalibrary/resources/rfband.py">get</a>(id) -> <a href="./src/unifieddatalibrary/types/rfband_get_response.py">RfbandGetResponse</a></code>
- <code title="get /udl/rfband/queryhelp">client.rfband.<a href="./src/unifieddatalibrary/resources/rfband.py">queryhelp</a>() -> None</code>
- <code title="get /udl/rfband/tuple">client.rfband.<a href="./src/unifieddatalibrary/resources/rfband.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/rfband_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/rfband_tuple_response.py">RfbandTupleResponse</a></code>

# Rfbandtype

Types:

```python
from unifieddatalibrary.types import (
    RfbandtypeListResponse,
    RfbandtypeCountResponse,
    RfbandtypeGetResponse,
    RfbandtypeTupleResponse,
)
```

Methods:

- <code title="post /udl/rfbandtype">client.rfbandtype.<a href="./src/unifieddatalibrary/resources/rfbandtype.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/rfbandtype_create_params.py">params</a>) -> None</code>
- <code title="put /udl/rfbandtype/{id}">client.rfbandtype.<a href="./src/unifieddatalibrary/resources/rfbandtype.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/rfbandtype_update_params.py">params</a>) -> None</code>
- <code title="get /udl/rfbandtype">client.rfbandtype.<a href="./src/unifieddatalibrary/resources/rfbandtype.py">list</a>() -> <a href="./src/unifieddatalibrary/types/rfbandtype_list_response.py">RfbandtypeListResponse</a></code>
- <code title="delete /udl/rfbandtype/{id}">client.rfbandtype.<a href="./src/unifieddatalibrary/resources/rfbandtype.py">delete</a>(id) -> None</code>
- <code title="get /udl/rfbandtype/count">client.rfbandtype.<a href="./src/unifieddatalibrary/resources/rfbandtype.py">count</a>() -> str</code>
- <code title="get /udl/rfbandtype/{id}">client.rfbandtype.<a href="./src/unifieddatalibrary/resources/rfbandtype.py">get</a>(id) -> <a href="./src/unifieddatalibrary/types/rfbandtype_get_response.py">RfbandtypeGetResponse</a></code>
- <code title="get /udl/rfbandtype/queryhelp">client.rfbandtype.<a href="./src/unifieddatalibrary/resources/rfbandtype.py">queryhelp</a>() -> None</code>
- <code title="get /udl/rfbandtype/tuple">client.rfbandtype.<a href="./src/unifieddatalibrary/resources/rfbandtype.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/rfbandtype_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/rfbandtype_tuple_response.py">RfbandtypeTupleResponse</a></code>

# Rfemitter

Types:

```python
from unifieddatalibrary.types import (
    RfemitterListResponse,
    RfemitterCountResponse,
    RfemitterGetResponse,
    RfemitterTupleResponse,
)
```

Methods:

- <code title="post /udl/rfemitter">client.rfemitter.<a href="./src/unifieddatalibrary/resources/rfemitter.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/rfemitter_create_params.py">params</a>) -> None</code>
- <code title="put /udl/rfemitter/{id}">client.rfemitter.<a href="./src/unifieddatalibrary/resources/rfemitter.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/rfemitter_update_params.py">params</a>) -> None</code>
- <code title="get /udl/rfemitter">client.rfemitter.<a href="./src/unifieddatalibrary/resources/rfemitter.py">list</a>() -> <a href="./src/unifieddatalibrary/types/rfemitter_list_response.py">RfemitterListResponse</a></code>
- <code title="delete /udl/rfemitter/{id}">client.rfemitter.<a href="./src/unifieddatalibrary/resources/rfemitter.py">delete</a>(id) -> None</code>
- <code title="get /udl/rfemitter/count">client.rfemitter.<a href="./src/unifieddatalibrary/resources/rfemitter.py">count</a>() -> str</code>
- <code title="get /udl/rfemitter/{id}">client.rfemitter.<a href="./src/unifieddatalibrary/resources/rfemitter.py">get</a>(id) -> <a href="./src/unifieddatalibrary/types/rfemitter_get_response.py">RfemitterGetResponse</a></code>
- <code title="get /udl/rfemitter/queryhelp">client.rfemitter.<a href="./src/unifieddatalibrary/resources/rfemitter.py">queryhelp</a>() -> None</code>
- <code title="get /udl/rfemitter/tuple">client.rfemitter.<a href="./src/unifieddatalibrary/resources/rfemitter.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/rfemitter_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/rfemitter_tuple_response.py">RfemitterTupleResponse</a></code>

# Rfemitterdetails

Types:

```python
from unifieddatalibrary.types import (
    RfemitterdetailListResponse,
    RfemitterdetailCountResponse,
    RfemitterdetailGetResponse,
    RfemitterdetailTupleResponse,
)
```

Methods:

- <code title="post /udl/rfemitterdetails">client.rfemitterdetails.<a href="./src/unifieddatalibrary/resources/rfemitterdetails.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/rfemitterdetail_create_params.py">params</a>) -> None</code>
- <code title="put /udl/rfemitterdetails/{id}">client.rfemitterdetails.<a href="./src/unifieddatalibrary/resources/rfemitterdetails.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/rfemitterdetail_update_params.py">params</a>) -> None</code>
- <code title="get /udl/rfemitterdetails">client.rfemitterdetails.<a href="./src/unifieddatalibrary/resources/rfemitterdetails.py">list</a>() -> <a href="./src/unifieddatalibrary/types/rfemitterdetail_list_response.py">RfemitterdetailListResponse</a></code>
- <code title="delete /udl/rfemitterdetails/{id}">client.rfemitterdetails.<a href="./src/unifieddatalibrary/resources/rfemitterdetails.py">delete</a>(id) -> None</code>
- <code title="get /udl/rfemitterdetails/count">client.rfemitterdetails.<a href="./src/unifieddatalibrary/resources/rfemitterdetails.py">count</a>() -> str</code>
- <code title="get /udl/rfemitterdetails/{id}">client.rfemitterdetails.<a href="./src/unifieddatalibrary/resources/rfemitterdetails.py">get</a>(id) -> <a href="./src/unifieddatalibrary/types/rfemitterdetail_get_response.py">RfemitterdetailGetResponse</a></code>
- <code title="get /udl/rfemitterdetails/queryhelp">client.rfemitterdetails.<a href="./src/unifieddatalibrary/resources/rfemitterdetails.py">queryhelp</a>() -> None</code>
- <code title="get /udl/rfemitterdetails/tuple">client.rfemitterdetails.<a href="./src/unifieddatalibrary/resources/rfemitterdetails.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/rfemitterdetail_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/rfemitterdetail_tuple_response.py">RfemitterdetailTupleResponse</a></code>

# Rfobservation

Types:

```python
from unifieddatalibrary.types import (
    RfobservationListResponse,
    RfobservationCountResponse,
    RfobservationTupleResponse,
)
```

Methods:

- <code title="post /udl/rfobservation">client.rfobservation.<a href="./src/unifieddatalibrary/resources/rfobservation/rfobservation.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/rfobservation_create_params.py">params</a>) -> None</code>
- <code title="get /udl/rfobservation">client.rfobservation.<a href="./src/unifieddatalibrary/resources/rfobservation/rfobservation.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/rfobservation_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/rfobservation_list_response.py">RfobservationListResponse</a></code>
- <code title="get /udl/rfobservation/count">client.rfobservation.<a href="./src/unifieddatalibrary/resources/rfobservation/rfobservation.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/rfobservation_count_params.py">params</a>) -> str</code>
- <code title="post /udl/rfobservation/createBulk">client.rfobservation.<a href="./src/unifieddatalibrary/resources/rfobservation/rfobservation.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/rfobservation_create_bulk_params.py">params</a>) -> None</code>
- <code title="post /filedrop/udl-rf">client.rfobservation.<a href="./src/unifieddatalibrary/resources/rfobservation/rfobservation.py">create_bulk_v2</a>(\*\*<a href="src/unifieddatalibrary/types/rfobservation_create_bulk_v2_params.py">params</a>) -> None</code>
- <code title="get /udl/rfobservation/{id}">client.rfobservation.<a href="./src/unifieddatalibrary/resources/rfobservation/rfobservation.py">get</a>(id) -> <a href="./src/unifieddatalibrary/types/udl/rfobservation/rfobservationdetails_full.py">RfobservationdetailsFull</a></code>
- <code title="get /udl/rfobservation/queryhelp">client.rfobservation.<a href="./src/unifieddatalibrary/resources/rfobservation/rfobservation.py">queryhelp</a>() -> None</code>
- <code title="get /udl/rfobservation/tuple">client.rfobservation.<a href="./src/unifieddatalibrary/resources/rfobservation/rfobservation.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/rfobservation_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/rfobservation_tuple_response.py">RfobservationTupleResponse</a></code>

## History

Types:

```python
from unifieddatalibrary.types.rfobservation import HistoryCountResponse
```

Methods:

- <code title="get /udl/rfobservation/history/count">client.rfobservation.history.<a href="./src/unifieddatalibrary/resources/rfobservation/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/rfobservation/history_count_params.py">params</a>) -> str</code>

# Sarobservation

Types:

```python
from unifieddatalibrary.types import (
    SarobservationListResponse,
    SarobservationCountResponse,
    SarobservationTupleResponse,
)
```

Methods:

- <code title="post /udl/sarobservation">client.sarobservation.<a href="./src/unifieddatalibrary/resources/sarobservation/sarobservation.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/sarobservation_create_params.py">params</a>) -> None</code>
- <code title="get /udl/sarobservation">client.sarobservation.<a href="./src/unifieddatalibrary/resources/sarobservation/sarobservation.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/sarobservation_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/sarobservation_list_response.py">SarobservationListResponse</a></code>
- <code title="get /udl/sarobservation/count">client.sarobservation.<a href="./src/unifieddatalibrary/resources/sarobservation/sarobservation.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/sarobservation_count_params.py">params</a>) -> str</code>
- <code title="post /udl/sarobservation/createBulk">client.sarobservation.<a href="./src/unifieddatalibrary/resources/sarobservation/sarobservation.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/sarobservation_create_bulk_params.py">params</a>) -> None</code>
- <code title="post /filedrop/udl-sar">client.sarobservation.<a href="./src/unifieddatalibrary/resources/sarobservation/sarobservation.py">create_bulk_v2</a>(\*\*<a href="src/unifieddatalibrary/types/sarobservation_create_bulk_v2_params.py">params</a>) -> None</code>
- <code title="get /udl/sarobservation/{id}">client.sarobservation.<a href="./src/unifieddatalibrary/resources/sarobservation/sarobservation.py">get</a>(id) -> <a href="./src/unifieddatalibrary/types/udl/sarobservation/sarobservation_full.py">SarobservationFull</a></code>
- <code title="get /udl/sarobservation/queryhelp">client.sarobservation.<a href="./src/unifieddatalibrary/resources/sarobservation/sarobservation.py">queryhelp</a>() -> None</code>
- <code title="get /udl/sarobservation/tuple">client.sarobservation.<a href="./src/unifieddatalibrary/resources/sarobservation/sarobservation.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/sarobservation_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/sarobservation_tuple_response.py">SarobservationTupleResponse</a></code>

## History

Types:

```python
from unifieddatalibrary.types.sarobservation import HistoryRetrieveResponse, HistoryCountResponse
```

Methods:

- <code title="get /udl/sarobservation/history">client.sarobservation.history.<a href="./src/unifieddatalibrary/resources/sarobservation/history.py">retrieve</a>(\*\*<a href="src/unifieddatalibrary/types/sarobservation/history_retrieve_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/sarobservation/history_retrieve_response.py">HistoryRetrieveResponse</a></code>
- <code title="get /udl/sarobservation/history/aodr">client.sarobservation.history.<a href="./src/unifieddatalibrary/resources/sarobservation/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/sarobservation/history_aodr_params.py">params</a>) -> None</code>
- <code title="get /udl/sarobservation/history/count">client.sarobservation.history.<a href="./src/unifieddatalibrary/resources/sarobservation/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/sarobservation/history_count_params.py">params</a>) -> str</code>

# Scientific

Types:

```python
from unifieddatalibrary.types import (
    ScientificListResponse,
    ScientificCountResponse,
    ScientificGetResponse,
    ScientificTupleResponse,
)
```

Methods:

- <code title="post /udl/scientific">client.scientific.<a href="./src/unifieddatalibrary/resources/scientific.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/scientific_create_params.py">params</a>) -> None</code>
- <code title="put /udl/scientific/{id}">client.scientific.<a href="./src/unifieddatalibrary/resources/scientific.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/scientific_update_params.py">params</a>) -> None</code>
- <code title="get /udl/scientific">client.scientific.<a href="./src/unifieddatalibrary/resources/scientific.py">list</a>() -> <a href="./src/unifieddatalibrary/types/scientific_list_response.py">ScientificListResponse</a></code>
- <code title="delete /udl/scientific/{id}">client.scientific.<a href="./src/unifieddatalibrary/resources/scientific.py">delete</a>(id) -> None</code>
- <code title="get /udl/scientific/count">client.scientific.<a href="./src/unifieddatalibrary/resources/scientific.py">count</a>() -> str</code>
- <code title="get /udl/scientific/{id}">client.scientific.<a href="./src/unifieddatalibrary/resources/scientific.py">get</a>(id) -> <a href="./src/unifieddatalibrary/types/scientific_get_response.py">ScientificGetResponse</a></code>
- <code title="get /udl/scientific/queryhelp">client.scientific.<a href="./src/unifieddatalibrary/resources/scientific.py">queryhelp</a>() -> None</code>
- <code title="get /udl/scientific/tuple">client.scientific.<a href="./src/unifieddatalibrary/resources/scientific.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/scientific_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/scientific_tuple_response.py">ScientificTupleResponse</a></code>

# Sensor

Types:

```python
from unifieddatalibrary.types import (
    SensorListResponse,
    SensorCountResponse,
    SensorGetResponse,
    SensorTupleResponse,
)
```

Methods:

- <code title="post /udl/sensor">client.sensor.<a href="./src/unifieddatalibrary/resources/sensor/sensor.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/sensor_create_params.py">params</a>) -> None</code>
- <code title="put /udl/sensor/{id}">client.sensor.<a href="./src/unifieddatalibrary/resources/sensor/sensor.py">update</a>(id, \*\*<a href="src/unifieddatalibrary/types/sensor_update_params.py">params</a>) -> None</code>
- <code title="get /udl/sensor">client.sensor.<a href="./src/unifieddatalibrary/resources/sensor/sensor.py">list</a>() -> <a href="./src/unifieddatalibrary/types/sensor_list_response.py">SensorListResponse</a></code>
- <code title="delete /udl/sensor/{id}">client.sensor.<a href="./src/unifieddatalibrary/resources/sensor/sensor.py">delete</a>(id) -> None</code>
- <code title="get /udl/sensor/count">client.sensor.<a href="./src/unifieddatalibrary/resources/sensor/sensor.py">count</a>() -> str</code>
- <code title="get /udl/sensor/{id}">client.sensor.<a href="./src/unifieddatalibrary/resources/sensor/sensor.py">get</a>(id) -> <a href="./src/unifieddatalibrary/types/sensor_get_response.py">SensorGetResponse</a></code>
- <code title="get /udl/sensor/queryhelp">client.sensor.<a href="./src/unifieddatalibrary/resources/sensor/sensor.py">queryhelp</a>() -> None</code>
- <code title="get /udl/sensor/tuple">client.sensor.<a href="./src/unifieddatalibrary/resources/sensor/sensor.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/sensor_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/sensor_tuple_response.py">SensorTupleResponse</a></code>

## Calibration

Types:

```python
from unifieddatalibrary.types.sensor import (
    CalibrationRetrieveResponse,
    CalibrationCountResponse,
    CalibrationQueryResponse,
    CalibrationTupleResponse,
)
```

Methods:

- <code title="post /udl/sensorcalibration">client.sensor.calibration.<a href="./src/unifieddatalibrary/resources/sensor/calibration/calibration.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/sensor/calibration_create_params.py">params</a>) -> None</code>
- <code title="get /udl/sensorcalibration/{id}">client.sensor.calibration.<a href="./src/unifieddatalibrary/resources/sensor/calibration/calibration.py">retrieve</a>(id) -> <a href="./src/unifieddatalibrary/types/sensor/calibration_retrieve_response.py">CalibrationRetrieveResponse</a></code>
- <code title="get /udl/sensorcalibration/count">client.sensor.calibration.<a href="./src/unifieddatalibrary/resources/sensor/calibration/calibration.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/sensor/calibration_count_params.py">params</a>) -> str</code>
- <code title="post /udl/sensorcalibration/createBulk">client.sensor.calibration.<a href="./src/unifieddatalibrary/resources/sensor/calibration/calibration.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/sensor/calibration_create_bulk_params.py">params</a>) -> None</code>
- <code title="post /filedrop/udl-sensorcalibration">client.sensor.calibration.<a href="./src/unifieddatalibrary/resources/sensor/calibration/calibration.py">create_bulk_v2</a>(\*\*<a href="src/unifieddatalibrary/types/sensor/calibration_create_bulk_v2_params.py">params</a>) -> None</code>
- <code title="get /udl/sensorcalibration">client.sensor.calibration.<a href="./src/unifieddatalibrary/resources/sensor/calibration/calibration.py">query</a>(\*\*<a href="src/unifieddatalibrary/types/sensor/calibration_query_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/sensor/calibration_query_response.py">CalibrationQueryResponse</a></code>
- <code title="get /udl/sensorcalibration/queryhelp">client.sensor.calibration.<a href="./src/unifieddatalibrary/resources/sensor/calibration/calibration.py">query_help</a>() -> None</code>
- <code title="get /udl/sensorcalibration/tuple">client.sensor.calibration.<a href="./src/unifieddatalibrary/resources/sensor/calibration/calibration.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/sensor/calibration_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/sensor/calibration_tuple_response.py">CalibrationTupleResponse</a></code>

### History

Types:

```python
from unifieddatalibrary.types.sensor.calibration import HistoryCountResponse, HistoryQueryResponse
```

Methods:

- <code title="get /udl/sensorcalibration/history/count">client.sensor.calibration.history.<a href="./src/unifieddatalibrary/resources/sensor/calibration/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/sensor/calibration/history_count_params.py">params</a>) -> str</code>
- <code title="get /udl/sensorcalibration/history">client.sensor.calibration.history.<a href="./src/unifieddatalibrary/resources/sensor/calibration/history.py">query</a>(\*\*<a href="src/unifieddatalibrary/types/sensor/calibration/history_query_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/sensor/calibration/history_query_response.py">HistoryQueryResponse</a></code>
- <code title="get /udl/sensorcalibration/history/aodr">client.sensor.calibration.history.<a href="./src/unifieddatalibrary/resources/sensor/calibration/history.py">write_aodr</a>(\*\*<a href="src/unifieddatalibrary/types/sensor/calibration/history_write_aodr_params.py">params</a>) -> None</code>

# Sensormaintenance

Types:

```python
from unifieddatalibrary.types import (
    SensormaintenanceListResponse,
    SensormaintenanceCountResponse,
    SensormaintenanceCurrentResponse,
    SensormaintenanceTupleResponse,
)
```

Methods:

- <code title="post /udl/sensormaintenance">client.sensormaintenance.<a href="./src/unifieddatalibrary/resources/sensormaintenance/sensormaintenance.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/sensormaintenance_create_params.py">params</a>) -> None</code>
- <code title="put /udl/sensormaintenance/{id}">client.sensormaintenance.<a href="./src/unifieddatalibrary/resources/sensormaintenance/sensormaintenance.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/sensormaintenance_update_params.py">params</a>) -> None</code>
- <code title="get /udl/sensormaintenance">client.sensormaintenance.<a href="./src/unifieddatalibrary/resources/sensormaintenance/sensormaintenance.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/sensormaintenance_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/sensormaintenance_list_response.py">SensormaintenanceListResponse</a></code>
- <code title="delete /udl/sensormaintenance/{id}">client.sensormaintenance.<a href="./src/unifieddatalibrary/resources/sensormaintenance/sensormaintenance.py">delete</a>(id) -> None</code>
- <code title="get /udl/sensormaintenance/count">client.sensormaintenance.<a href="./src/unifieddatalibrary/resources/sensormaintenance/sensormaintenance.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/sensormaintenance_count_params.py">params</a>) -> str</code>
- <code title="post /udl/sensormaintenance/createBulk">client.sensormaintenance.<a href="./src/unifieddatalibrary/resources/sensormaintenance/sensormaintenance.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/sensormaintenance_create_bulk_params.py">params</a>) -> None</code>
- <code title="get /udl/sensormaintenance/current">client.sensormaintenance.<a href="./src/unifieddatalibrary/resources/sensormaintenance/sensormaintenance.py">current</a>() -> <a href="./src/unifieddatalibrary/types/sensormaintenance_current_response.py">SensormaintenanceCurrentResponse</a></code>
- <code title="get /udl/sensormaintenance/{id}">client.sensormaintenance.<a href="./src/unifieddatalibrary/resources/sensormaintenance/sensormaintenance.py">get</a>(id) -> <a href="./src/unifieddatalibrary/types/udl/sensormaintenance/sensormaintenance_full.py">SensormaintenanceFull</a></code>
- <code title="get /udl/sensormaintenance/queryhelp">client.sensormaintenance.<a href="./src/unifieddatalibrary/resources/sensormaintenance/sensormaintenance.py">queryhelp</a>() -> None</code>
- <code title="get /udl/sensormaintenance/tuple">client.sensormaintenance.<a href="./src/unifieddatalibrary/resources/sensormaintenance/sensormaintenance.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/sensormaintenance_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/sensormaintenance_tuple_response.py">SensormaintenanceTupleResponse</a></code>

## History

Types:

```python
from unifieddatalibrary.types.sensormaintenance import HistoryRetrieveResponse, HistoryCountResponse
```

Methods:

- <code title="get /udl/sensormaintenance/history">client.sensormaintenance.history.<a href="./src/unifieddatalibrary/resources/sensormaintenance/history.py">retrieve</a>(\*\*<a href="src/unifieddatalibrary/types/sensormaintenance/history_retrieve_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/sensormaintenance/history_retrieve_response.py">HistoryRetrieveResponse</a></code>
- <code title="get /udl/sensormaintenance/history/aodr">client.sensormaintenance.history.<a href="./src/unifieddatalibrary/resources/sensormaintenance/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/sensormaintenance/history_aodr_params.py">params</a>) -> None</code>
- <code title="get /udl/sensormaintenance/history/count">client.sensormaintenance.history.<a href="./src/unifieddatalibrary/resources/sensormaintenance/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/sensormaintenance/history_count_params.py">params</a>) -> str</code>

# Sensorobservationtype

Types:

```python
from unifieddatalibrary.types import (
    SensorobservationtypeListResponse,
    SensorobservationtypeGetResponse,
)
```

Methods:

- <code title="get /udl/sensorobservationtype">client.sensorobservationtype.<a href="./src/unifieddatalibrary/resources/sensorobservationtype.py">list</a>() -> <a href="./src/unifieddatalibrary/types/sensorobservationtype_list_response.py">SensorobservationtypeListResponse</a></code>
- <code title="get /udl/sensorobservationtype/{id}">client.sensorobservationtype.<a href="./src/unifieddatalibrary/resources/sensorobservationtype.py">get</a>(id) -> <a href="./src/unifieddatalibrary/types/sensorobservationtype_get_response.py">SensorobservationtypeGetResponse</a></code>
- <code title="get /udl/sensorobservationtype/queryhelp">client.sensorobservationtype.<a href="./src/unifieddatalibrary/resources/sensorobservationtype.py">queryhelp</a>() -> None</code>

# Sensorplan

Types:

```python
from unifieddatalibrary.types import (
    SensorplanListResponse,
    SensorplanCountResponse,
    SensorplanTupleResponse,
)
```

Methods:

- <code title="post /udl/sensorplan">client.sensorplan.<a href="./src/unifieddatalibrary/resources/sensorplan/sensorplan.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/sensorplan_create_params.py">params</a>) -> None</code>
- <code title="put /udl/sensorplan/{id}">client.sensorplan.<a href="./src/unifieddatalibrary/resources/sensorplan/sensorplan.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/sensorplan_update_params.py">params</a>) -> None</code>
- <code title="get /udl/sensorplan">client.sensorplan.<a href="./src/unifieddatalibrary/resources/sensorplan/sensorplan.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/sensorplan_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/sensorplan_list_response.py">SensorplanListResponse</a></code>
- <code title="get /udl/sensorplan/count">client.sensorplan.<a href="./src/unifieddatalibrary/resources/sensorplan/sensorplan.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/sensorplan_count_params.py">params</a>) -> str</code>
- <code title="post /filedrop/udl-sensorplan">client.sensorplan.<a href="./src/unifieddatalibrary/resources/sensorplan/sensorplan.py">create_bulk_v2</a>(\*\*<a href="src/unifieddatalibrary/types/sensorplan_create_bulk_v2_params.py">params</a>) -> None</code>
- <code title="get /udl/sensorplan/{id}">client.sensorplan.<a href="./src/unifieddatalibrary/resources/sensorplan/sensorplan.py">get</a>(id) -> <a href="./src/unifieddatalibrary/types/udl/sensorplan/sensorplan_full.py">SensorplanFull</a></code>
- <code title="get /udl/sensorplan/queryhelp">client.sensorplan.<a href="./src/unifieddatalibrary/resources/sensorplan/sensorplan.py">queryhelp</a>() -> None</code>
- <code title="get /udl/sensorplan/tuple">client.sensorplan.<a href="./src/unifieddatalibrary/resources/sensorplan/sensorplan.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/sensorplan_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/sensorplan_tuple_response.py">SensorplanTupleResponse</a></code>

## History

Types:

```python
from unifieddatalibrary.types.sensorplan import HistoryRetrieveResponse, HistoryCountResponse
```

Methods:

- <code title="get /udl/sensorplan/history">client.sensorplan.history.<a href="./src/unifieddatalibrary/resources/sensorplan/history.py">retrieve</a>(\*\*<a href="src/unifieddatalibrary/types/sensorplan/history_retrieve_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/sensorplan/history_retrieve_response.py">HistoryRetrieveResponse</a></code>
- <code title="get /udl/sensorplan/history/aodr">client.sensorplan.history.<a href="./src/unifieddatalibrary/resources/sensorplan/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/sensorplan/history_aodr_params.py">params</a>) -> None</code>
- <code title="get /udl/sensorplan/history/count">client.sensorplan.history.<a href="./src/unifieddatalibrary/resources/sensorplan/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/sensorplan/history_count_params.py">params</a>) -> str</code>

# Sensortype

Types:

```python
from unifieddatalibrary.types import SensortypeListResponse, SensortypeGetResponse
```

Methods:

- <code title="get /udl/sensortype">client.sensortype.<a href="./src/unifieddatalibrary/resources/sensortype.py">list</a>() -> <a href="./src/unifieddatalibrary/types/sensortype_list_response.py">SensortypeListResponse</a></code>
- <code title="get /udl/sensortype/{id}">client.sensortype.<a href="./src/unifieddatalibrary/resources/sensortype.py">get</a>(id) -> <a href="./src/unifieddatalibrary/types/sensortype_get_response.py">SensortypeGetResponse</a></code>
- <code title="get /udl/sensortype/queryhelp">client.sensortype.<a href="./src/unifieddatalibrary/resources/sensortype.py">queryhelp</a>() -> None</code>

# Seradatacommdetails

Types:

```python
from unifieddatalibrary.types import (
    SeradatacommdetailListResponse,
    SeradatacommdetailCountResponse,
    SeradatacommdetailGetResponse,
    SeradatacommdetailTupleResponse,
)
```

Methods:

- <code title="post /udl/seradatacommdetails">client.seradatacommdetails.<a href="./src/unifieddatalibrary/resources/seradatacommdetails.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/seradatacommdetail_create_params.py">params</a>) -> None</code>
- <code title="put /udl/seradatacommdetails/{id}">client.seradatacommdetails.<a href="./src/unifieddatalibrary/resources/seradatacommdetails.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/seradatacommdetail_update_params.py">params</a>) -> None</code>
- <code title="get /udl/seradatacommdetails">client.seradatacommdetails.<a href="./src/unifieddatalibrary/resources/seradatacommdetails.py">list</a>() -> <a href="./src/unifieddatalibrary/types/seradatacommdetail_list_response.py">SeradatacommdetailListResponse</a></code>
- <code title="delete /udl/seradatacommdetails/{id}">client.seradatacommdetails.<a href="./src/unifieddatalibrary/resources/seradatacommdetails.py">delete</a>(id) -> None</code>
- <code title="get /udl/seradatacommdetails/count">client.seradatacommdetails.<a href="./src/unifieddatalibrary/resources/seradatacommdetails.py">count</a>() -> str</code>
- <code title="get /udl/seradatacommdetails/{id}">client.seradatacommdetails.<a href="./src/unifieddatalibrary/resources/seradatacommdetails.py">get</a>(id) -> <a href="./src/unifieddatalibrary/types/seradatacommdetail_get_response.py">SeradatacommdetailGetResponse</a></code>
- <code title="get /udl/seradatacommdetails/queryhelp">client.seradatacommdetails.<a href="./src/unifieddatalibrary/resources/seradatacommdetails.py">queryhelp</a>() -> None</code>
- <code title="get /udl/seradatacommdetails/tuple">client.seradatacommdetails.<a href="./src/unifieddatalibrary/resources/seradatacommdetails.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/seradatacommdetail_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/seradatacommdetail_tuple_response.py">SeradatacommdetailTupleResponse</a></code>

# Seradataearlywarning

Types:

```python
from unifieddatalibrary.types import (
    SeradataearlywarningListResponse,
    SeradataearlywarningCountResponse,
    SeradataearlywarningGetResponse,
    SeradataearlywarningTupleResponse,
)
```

Methods:

- <code title="post /udl/seradataearlywarning">client.seradataearlywarning.<a href="./src/unifieddatalibrary/resources/seradataearlywarning.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/seradataearlywarning_create_params.py">params</a>) -> None</code>
- <code title="put /udl/seradataearlywarning/{id}">client.seradataearlywarning.<a href="./src/unifieddatalibrary/resources/seradataearlywarning.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/seradataearlywarning_update_params.py">params</a>) -> None</code>
- <code title="get /udl/seradataearlywarning">client.seradataearlywarning.<a href="./src/unifieddatalibrary/resources/seradataearlywarning.py">list</a>() -> <a href="./src/unifieddatalibrary/types/seradataearlywarning_list_response.py">SeradataearlywarningListResponse</a></code>
- <code title="delete /udl/seradataearlywarning/{id}">client.seradataearlywarning.<a href="./src/unifieddatalibrary/resources/seradataearlywarning.py">delete</a>(id) -> None</code>
- <code title="get /udl/seradataearlywarning/count">client.seradataearlywarning.<a href="./src/unifieddatalibrary/resources/seradataearlywarning.py">count</a>() -> str</code>
- <code title="get /udl/seradataearlywarning/{id}">client.seradataearlywarning.<a href="./src/unifieddatalibrary/resources/seradataearlywarning.py">get</a>(id) -> <a href="./src/unifieddatalibrary/types/seradataearlywarning_get_response.py">SeradataearlywarningGetResponse</a></code>
- <code title="get /udl/seradataearlywarning/queryhelp">client.seradataearlywarning.<a href="./src/unifieddatalibrary/resources/seradataearlywarning.py">queryhelp</a>() -> None</code>
- <code title="get /udl/seradataearlywarning/tuple">client.seradataearlywarning.<a href="./src/unifieddatalibrary/resources/seradataearlywarning.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/seradataearlywarning_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/seradataearlywarning_tuple_response.py">SeradataearlywarningTupleResponse</a></code>

# Seradatanavigation

Types:

```python
from unifieddatalibrary.types import (
    SeradatanavigationListResponse,
    SeradatanavigationCountResponse,
    SeradatanavigationGetResponse,
    SeradatanavigationTupleResponse,
)
```

Methods:

- <code title="post /udl/seradatanavigation">client.seradatanavigation.<a href="./src/unifieddatalibrary/resources/seradatanavigation.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/seradatanavigation_create_params.py">params</a>) -> None</code>
- <code title="put /udl/seradatanavigation/{id}">client.seradatanavigation.<a href="./src/unifieddatalibrary/resources/seradatanavigation.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/seradatanavigation_update_params.py">params</a>) -> None</code>
- <code title="get /udl/seradatanavigation">client.seradatanavigation.<a href="./src/unifieddatalibrary/resources/seradatanavigation.py">list</a>() -> <a href="./src/unifieddatalibrary/types/seradatanavigation_list_response.py">SeradatanavigationListResponse</a></code>
- <code title="delete /udl/seradatanavigation/{id}">client.seradatanavigation.<a href="./src/unifieddatalibrary/resources/seradatanavigation.py">delete</a>(id) -> None</code>
- <code title="get /udl/seradatanavigation/count">client.seradatanavigation.<a href="./src/unifieddatalibrary/resources/seradatanavigation.py">count</a>() -> str</code>
- <code title="get /udl/seradatanavigation/{id}">client.seradatanavigation.<a href="./src/unifieddatalibrary/resources/seradatanavigation.py">get</a>(id) -> <a href="./src/unifieddatalibrary/types/seradatanavigation_get_response.py">SeradatanavigationGetResponse</a></code>
- <code title="get /udl/seradatanavigation/queryhelp">client.seradatanavigation.<a href="./src/unifieddatalibrary/resources/seradatanavigation.py">queryhelp</a>() -> None</code>
- <code title="get /udl/seradatanavigation/tuple">client.seradatanavigation.<a href="./src/unifieddatalibrary/resources/seradatanavigation.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/seradatanavigation_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/seradatanavigation_tuple_response.py">SeradatanavigationTupleResponse</a></code>

# Seradataopticalpayload

Types:

```python
from unifieddatalibrary.types import (
    SeradataopticalpayloadListResponse,
    SeradataopticalpayloadCountResponse,
    SeradataopticalpayloadGetResponse,
    SeradataopticalpayloadTupleResponse,
)
```

Methods:

- <code title="post /udl/seradataopticalpayload">client.seradataopticalpayload.<a href="./src/unifieddatalibrary/resources/seradataopticalpayload.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/seradataopticalpayload_create_params.py">params</a>) -> None</code>
- <code title="put /udl/seradataopticalpayload/{id}">client.seradataopticalpayload.<a href="./src/unifieddatalibrary/resources/seradataopticalpayload.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/seradataopticalpayload_update_params.py">params</a>) -> None</code>
- <code title="get /udl/seradataopticalpayload">client.seradataopticalpayload.<a href="./src/unifieddatalibrary/resources/seradataopticalpayload.py">list</a>() -> <a href="./src/unifieddatalibrary/types/seradataopticalpayload_list_response.py">SeradataopticalpayloadListResponse</a></code>
- <code title="delete /udl/seradataopticalpayload/{id}">client.seradataopticalpayload.<a href="./src/unifieddatalibrary/resources/seradataopticalpayload.py">delete</a>(id) -> None</code>
- <code title="get /udl/seradataopticalpayload/count">client.seradataopticalpayload.<a href="./src/unifieddatalibrary/resources/seradataopticalpayload.py">count</a>() -> str</code>
- <code title="get /udl/seradataopticalpayload/{id}">client.seradataopticalpayload.<a href="./src/unifieddatalibrary/resources/seradataopticalpayload.py">get</a>(id) -> <a href="./src/unifieddatalibrary/types/seradataopticalpayload_get_response.py">SeradataopticalpayloadGetResponse</a></code>
- <code title="get /udl/seradataopticalpayload/queryhelp">client.seradataopticalpayload.<a href="./src/unifieddatalibrary/resources/seradataopticalpayload.py">queryhelp</a>() -> None</code>
- <code title="get /udl/seradataopticalpayload/tuple">client.seradataopticalpayload.<a href="./src/unifieddatalibrary/resources/seradataopticalpayload.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/seradataopticalpayload_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/seradataopticalpayload_tuple_response.py">SeradataopticalpayloadTupleResponse</a></code>

# Seradataradarpayload

Types:

```python
from unifieddatalibrary.types import (
    SeradataradarpayloadListResponse,
    SeradataradarpayloadCountResponse,
    SeradataradarpayloadGetResponse,
    SeradataradarpayloadTupleResponse,
)
```

Methods:

- <code title="post /udl/seradataradarpayload">client.seradataradarpayload.<a href="./src/unifieddatalibrary/resources/seradataradarpayload.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/seradataradarpayload_create_params.py">params</a>) -> None</code>
- <code title="put /udl/seradataradarpayload/{id}">client.seradataradarpayload.<a href="./src/unifieddatalibrary/resources/seradataradarpayload.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/seradataradarpayload_update_params.py">params</a>) -> None</code>
- <code title="get /udl/seradataradarpayload">client.seradataradarpayload.<a href="./src/unifieddatalibrary/resources/seradataradarpayload.py">list</a>() -> <a href="./src/unifieddatalibrary/types/seradataradarpayload_list_response.py">SeradataradarpayloadListResponse</a></code>
- <code title="delete /udl/seradataradarpayload/{id}">client.seradataradarpayload.<a href="./src/unifieddatalibrary/resources/seradataradarpayload.py">delete</a>(id) -> None</code>
- <code title="get /udl/seradataradarpayload/count">client.seradataradarpayload.<a href="./src/unifieddatalibrary/resources/seradataradarpayload.py">count</a>() -> str</code>
- <code title="get /udl/seradataradarpayload/{id}">client.seradataradarpayload.<a href="./src/unifieddatalibrary/resources/seradataradarpayload.py">get</a>(id) -> <a href="./src/unifieddatalibrary/types/seradataradarpayload_get_response.py">SeradataradarpayloadGetResponse</a></code>
- <code title="get /udl/seradataradarpayload/queryhelp">client.seradataradarpayload.<a href="./src/unifieddatalibrary/resources/seradataradarpayload.py">queryhelp</a>() -> None</code>
- <code title="get /udl/seradataradarpayload/tuple">client.seradataradarpayload.<a href="./src/unifieddatalibrary/resources/seradataradarpayload.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/seradataradarpayload_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/seradataradarpayload_tuple_response.py">SeradataradarpayloadTupleResponse</a></code>

# Seradatasigintpayload

Types:

```python
from unifieddatalibrary.types import (
    SeradatasigintpayloadListResponse,
    SeradatasigintpayloadCountResponse,
    SeradatasigintpayloadGetResponse,
    SeradatasigintpayloadTupleResponse,
)
```

Methods:

- <code title="post /udl/seradatasigintpayload">client.seradatasigintpayload.<a href="./src/unifieddatalibrary/resources/seradatasigintpayload.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/seradatasigintpayload_create_params.py">params</a>) -> None</code>
- <code title="put /udl/seradatasigintpayload/{id}">client.seradatasigintpayload.<a href="./src/unifieddatalibrary/resources/seradatasigintpayload.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/seradatasigintpayload_update_params.py">params</a>) -> None</code>
- <code title="get /udl/seradatasigintpayload">client.seradatasigintpayload.<a href="./src/unifieddatalibrary/resources/seradatasigintpayload.py">list</a>() -> <a href="./src/unifieddatalibrary/types/seradatasigintpayload_list_response.py">SeradatasigintpayloadListResponse</a></code>
- <code title="delete /udl/seradatasigintpayload/{id}">client.seradatasigintpayload.<a href="./src/unifieddatalibrary/resources/seradatasigintpayload.py">delete</a>(id) -> None</code>
- <code title="get /udl/seradatasigintpayload/count">client.seradatasigintpayload.<a href="./src/unifieddatalibrary/resources/seradatasigintpayload.py">count</a>() -> str</code>
- <code title="get /udl/seradatasigintpayload/{id}">client.seradatasigintpayload.<a href="./src/unifieddatalibrary/resources/seradatasigintpayload.py">get</a>(id) -> <a href="./src/unifieddatalibrary/types/seradatasigintpayload_get_response.py">SeradatasigintpayloadGetResponse</a></code>
- <code title="get /udl/seradatasigintpayload/queryhelp">client.seradatasigintpayload.<a href="./src/unifieddatalibrary/resources/seradatasigintpayload.py">queryhelp</a>() -> None</code>
- <code title="get /udl/seradatasigintpayload/tuple">client.seradatasigintpayload.<a href="./src/unifieddatalibrary/resources/seradatasigintpayload.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/seradatasigintpayload_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/seradatasigintpayload_tuple_response.py">SeradatasigintpayloadTupleResponse</a></code>

# Seradataspacecraftdetails

Types:

```python
from unifieddatalibrary.types import (
    SeradataspacecraftdetailListResponse,
    SeradataspacecraftdetailCountResponse,
    SeradataspacecraftdetailGetResponse,
    SeradataspacecraftdetailTupleResponse,
)
```

Methods:

- <code title="post /udl/seradataspacecraftdetails">client.seradataspacecraftdetails.<a href="./src/unifieddatalibrary/resources/seradataspacecraftdetails.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/seradataspacecraftdetail_create_params.py">params</a>) -> None</code>
- <code title="put /udl/seradataspacecraftdetails/{id}">client.seradataspacecraftdetails.<a href="./src/unifieddatalibrary/resources/seradataspacecraftdetails.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/seradataspacecraftdetail_update_params.py">params</a>) -> None</code>
- <code title="get /udl/seradataspacecraftdetails">client.seradataspacecraftdetails.<a href="./src/unifieddatalibrary/resources/seradataspacecraftdetails.py">list</a>() -> <a href="./src/unifieddatalibrary/types/seradataspacecraftdetail_list_response.py">SeradataspacecraftdetailListResponse</a></code>
- <code title="delete /udl/seradataspacecraftdetails/{id}">client.seradataspacecraftdetails.<a href="./src/unifieddatalibrary/resources/seradataspacecraftdetails.py">delete</a>(id) -> None</code>
- <code title="get /udl/seradataspacecraftdetails/count">client.seradataspacecraftdetails.<a href="./src/unifieddatalibrary/resources/seradataspacecraftdetails.py">count</a>() -> str</code>
- <code title="get /udl/seradataspacecraftdetails/{id}">client.seradataspacecraftdetails.<a href="./src/unifieddatalibrary/resources/seradataspacecraftdetails.py">get</a>(id) -> <a href="./src/unifieddatalibrary/types/seradataspacecraftdetail_get_response.py">SeradataspacecraftdetailGetResponse</a></code>
- <code title="get /udl/seradataspacecraftdetails/queryhelp">client.seradataspacecraftdetails.<a href="./src/unifieddatalibrary/resources/seradataspacecraftdetails.py">queryhelp</a>() -> None</code>
- <code title="get /udl/seradataspacecraftdetails/tuple">client.seradataspacecraftdetails.<a href="./src/unifieddatalibrary/resources/seradataspacecraftdetails.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/seradataspacecraftdetail_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/seradataspacecraftdetail_tuple_response.py">SeradataspacecraftdetailTupleResponse</a></code>

# Sgi

Types:

```python
from unifieddatalibrary.types import SgiListResponse, SgiCountResponse, SgiTupleResponse
```

Methods:

- <code title="post /udl/sgi">client.sgi.<a href="./src/unifieddatalibrary/resources/sgi/sgi.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/sgi_create_params.py">params</a>) -> None</code>
- <code title="put /udl/sgi/{id}">client.sgi.<a href="./src/unifieddatalibrary/resources/sgi/sgi.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/sgi_update_params.py">params</a>) -> None</code>
- <code title="get /udl/sgi">client.sgi.<a href="./src/unifieddatalibrary/resources/sgi/sgi.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/sgi_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/sgi_list_response.py">SgiListResponse</a></code>
- <code title="delete /udl/sgi/{id}">client.sgi.<a href="./src/unifieddatalibrary/resources/sgi/sgi.py">delete</a>(id) -> None</code>
- <code title="get /udl/sgi/count">client.sgi.<a href="./src/unifieddatalibrary/resources/sgi/sgi.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/sgi_count_params.py">params</a>) -> str</code>
- <code title="post /udl/sgi/createBulk">client.sgi.<a href="./src/unifieddatalibrary/resources/sgi/sgi.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/sgi_create_bulk_params.py">params</a>) -> None</code>
- <code title="post /filedrop/udl-sgi">client.sgi.<a href="./src/unifieddatalibrary/resources/sgi/sgi.py">create_bulk_v2</a>(\*\*<a href="src/unifieddatalibrary/types/sgi_create_bulk_v2_params.py">params</a>) -> None</code>
- <code title="get /udl/sgi/{id}">client.sgi.<a href="./src/unifieddatalibrary/resources/sgi/sgi.py">get</a>(id) -> <a href="./src/unifieddatalibrary/types/udl/sgi/sgi_full.py">SgiFull</a></code>
- <code title="get /udl/sgi/getSGIDataByEffectiveAsOfDate">client.sgi.<a href="./src/unifieddatalibrary/resources/sgi/sgi.py">get_data_by_effective_as_of_date</a>(\*\*<a href="src/unifieddatalibrary/types/sgi_get_data_by_effective_as_of_date_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/udl/sgi/sgi_full.py">SgiFull</a></code>
- <code title="get /udl/sgi/queryhelp">client.sgi.<a href="./src/unifieddatalibrary/resources/sgi/sgi.py">queryhelp</a>() -> None</code>
- <code title="get /udl/sgi/tuple">client.sgi.<a href="./src/unifieddatalibrary/resources/sgi/sgi.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/sgi_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/sgi_tuple_response.py">SgiTupleResponse</a></code>

## History

Types:

```python
from unifieddatalibrary.types.sgi import HistoryListResponse, HistoryCountResponse
```

Methods:

- <code title="get /udl/sgi/history">client.sgi.history.<a href="./src/unifieddatalibrary/resources/sgi/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/sgi/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/sgi/history_list_response.py">HistoryListResponse</a></code>
- <code title="get /udl/sgi/history/aodr">client.sgi.history.<a href="./src/unifieddatalibrary/resources/sgi/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/sgi/history_aodr_params.py">params</a>) -> None</code>
- <code title="get /udl/sgi/history/count">client.sgi.history.<a href="./src/unifieddatalibrary/resources/sgi/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/sgi/history_count_params.py">params</a>) -> str</code>

# Sigact

Types:

```python
from unifieddatalibrary.types import SigactListResponse, SigactCountResponse, SigactTupleResponse
```

Methods:

- <code title="get /udl/sigact">client.sigact.<a href="./src/unifieddatalibrary/resources/sigact/sigact.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/sigact_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/sigact_list_response.py">SigactListResponse</a></code>
- <code title="get /udl/sigact/count">client.sigact.<a href="./src/unifieddatalibrary/resources/sigact/sigact.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/sigact_count_params.py">params</a>) -> str</code>
- <code title="post /udl/sigact/createBulk">client.sigact.<a href="./src/unifieddatalibrary/resources/sigact/sigact.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/sigact_create_bulk_params.py">params</a>) -> None</code>
- <code title="get /udl/sigact/queryhelp">client.sigact.<a href="./src/unifieddatalibrary/resources/sigact/sigact.py">queryhelp</a>() -> None</code>
- <code title="get /udl/sigact/tuple">client.sigact.<a href="./src/unifieddatalibrary/resources/sigact/sigact.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/sigact_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/sigact_tuple_response.py">SigactTupleResponse</a></code>
- <code title="post /filedrop/udl-sigact-text">client.sigact.<a href="./src/unifieddatalibrary/resources/sigact/sigact.py">upload_zip</a>(\*\*<a href="src/unifieddatalibrary/types/sigact_upload_zip_params.py">params</a>) -> None</code>

## History

Types:

```python
from unifieddatalibrary.types.sigact import HistoryListResponse, HistoryCountResponse
```

Methods:

- <code title="get /udl/sigact/history">client.sigact.history.<a href="./src/unifieddatalibrary/resources/sigact/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/sigact/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/sigact/history_list_response.py">HistoryListResponse</a></code>
- <code title="get /udl/sigact/history/count">client.sigact.history.<a href="./src/unifieddatalibrary/resources/sigact/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/sigact/history_count_params.py">params</a>) -> str</code>

# Site

Types:

```python
from unifieddatalibrary.types import (
    SiteListResponse,
    SiteCountResponse,
    SiteGetResponse,
    SiteTupleResponse,
)
```

Methods:

- <code title="post /udl/site">client.site.<a href="./src/unifieddatalibrary/resources/site/site.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/site_create_params.py">params</a>) -> None</code>
- <code title="put /udl/site/{id}">client.site.<a href="./src/unifieddatalibrary/resources/site/site.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/site_update_params.py">params</a>) -> None</code>
- <code title="get /udl/site">client.site.<a href="./src/unifieddatalibrary/resources/site/site.py">list</a>() -> <a href="./src/unifieddatalibrary/types/site_list_response.py">SiteListResponse</a></code>
- <code title="get /udl/site/count">client.site.<a href="./src/unifieddatalibrary/resources/site/site.py">count</a>() -> str</code>
- <code title="get /udl/site/{id}">client.site.<a href="./src/unifieddatalibrary/resources/site/site.py">get</a>(id) -> <a href="./src/unifieddatalibrary/types/site_get_response.py">SiteGetResponse</a></code>
- <code title="get /udl/site/queryhelp">client.site.<a href="./src/unifieddatalibrary/resources/site/site.py">queryhelp</a>() -> None</code>
- <code title="get /udl/site/tuple">client.site.<a href="./src/unifieddatalibrary/resources/site/site.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/site_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/site_tuple_response.py">SiteTupleResponse</a></code>

## Operations

Types:

```python
from unifieddatalibrary.types.site import (
    OperationRetrieveResponse,
    OperationListResponse,
    OperationCountResponse,
    OperationTupleResponse,
)
```

Methods:

- <code title="post /udl/siteoperations">client.site.operations.<a href="./src/unifieddatalibrary/resources/site/operations.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/site/operation_create_params.py">params</a>) -> None</code>
- <code title="get /udl/siteoperations/{id}">client.site.operations.<a href="./src/unifieddatalibrary/resources/site/operations.py">retrieve</a>(id) -> <a href="./src/unifieddatalibrary/types/site/operation_retrieve_response.py">OperationRetrieveResponse</a></code>
- <code title="put /udl/siteoperations/{id}">client.site.operations.<a href="./src/unifieddatalibrary/resources/site/operations.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/site/operation_update_params.py">params</a>) -> None</code>
- <code title="get /udl/siteoperations">client.site.operations.<a href="./src/unifieddatalibrary/resources/site/operations.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/site/operation_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/site/operation_list_response.py">OperationListResponse</a></code>
- <code title="delete /udl/siteoperations/{id}">client.site.operations.<a href="./src/unifieddatalibrary/resources/site/operations.py">delete</a>(id) -> None</code>
- <code title="get /udl/siteoperations/count">client.site.operations.<a href="./src/unifieddatalibrary/resources/site/operations.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/site/operation_count_params.py">params</a>) -> str</code>
- <code title="post /udl/siteoperations/createBulk">client.site.operations.<a href="./src/unifieddatalibrary/resources/site/operations.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/site/operation_create_bulk_params.py">params</a>) -> None</code>
- <code title="post /filedrop/udl-siteoperations">client.site.operations.<a href="./src/unifieddatalibrary/resources/site/operations.py">create_bulk_v2</a>(\*\*<a href="src/unifieddatalibrary/types/site/operation_create_bulk_v2_params.py">params</a>) -> None</code>
- <code title="get /udl/siteoperations/queryhelp">client.site.operations.<a href="./src/unifieddatalibrary/resources/site/operations.py">query_help</a>() -> None</code>
- <code title="get /udl/siteoperations/tuple">client.site.operations.<a href="./src/unifieddatalibrary/resources/site/operations.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/site/operation_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/site/operation_tuple_response.py">OperationTupleResponse</a></code>

# Siteremark

Types:

```python
from unifieddatalibrary.types import (
    SiteremarkListResponse,
    SiteremarkCountResponse,
    SiteremarkGetResponse,
    SiteremarkTupleResponse,
)
```

Methods:

- <code title="post /udl/siteremark">client.siteremark.<a href="./src/unifieddatalibrary/resources/siteremark.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/siteremark_create_params.py">params</a>) -> None</code>
- <code title="get /udl/siteremark">client.siteremark.<a href="./src/unifieddatalibrary/resources/siteremark.py">list</a>() -> <a href="./src/unifieddatalibrary/types/siteremark_list_response.py">SiteremarkListResponse</a></code>
- <code title="get /udl/siteremark/count">client.siteremark.<a href="./src/unifieddatalibrary/resources/siteremark.py">count</a>() -> str</code>
- <code title="get /udl/siteremark/{id}">client.siteremark.<a href="./src/unifieddatalibrary/resources/siteremark.py">get</a>(id) -> <a href="./src/unifieddatalibrary/types/siteremark_get_response.py">SiteremarkGetResponse</a></code>
- <code title="get /udl/siteremark/queryhelp">client.siteremark.<a href="./src/unifieddatalibrary/resources/siteremark.py">queryhelp</a>() -> None</code>
- <code title="get /udl/siteremark/tuple">client.siteremark.<a href="./src/unifieddatalibrary/resources/siteremark.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/siteremark_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/siteremark_tuple_response.py">SiteremarkTupleResponse</a></code>

# Sitestatus

Types:

```python
from unifieddatalibrary.types import (
    SitestatusListResponse,
    SitestatusCountResponse,
    SitestatusTupleResponse,
)
```

Methods:

- <code title="post /udl/sitestatus">client.sitestatus.<a href="./src/unifieddatalibrary/resources/sitestatus/sitestatus.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/sitestatus_create_params.py">params</a>) -> None</code>
- <code title="put /udl/sitestatus/{id}">client.sitestatus.<a href="./src/unifieddatalibrary/resources/sitestatus/sitestatus.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/sitestatus_update_params.py">params</a>) -> None</code>
- <code title="get /udl/sitestatus">client.sitestatus.<a href="./src/unifieddatalibrary/resources/sitestatus/sitestatus.py">list</a>() -> <a href="./src/unifieddatalibrary/types/sitestatus_list_response.py">SitestatusListResponse</a></code>
- <code title="delete /udl/sitestatus/{id}">client.sitestatus.<a href="./src/unifieddatalibrary/resources/sitestatus/sitestatus.py">delete</a>(id) -> None</code>
- <code title="get /udl/sitestatus/count">client.sitestatus.<a href="./src/unifieddatalibrary/resources/sitestatus/sitestatus.py">count</a>() -> str</code>
- <code title="get /udl/sitestatus/{id}">client.sitestatus.<a href="./src/unifieddatalibrary/resources/sitestatus/sitestatus.py">get</a>(id) -> <a href="./src/unifieddatalibrary/types/udl/sitestatus/sitestatus_full.py">SitestatusFull</a></code>
- <code title="get /udl/sitestatus/queryhelp">client.sitestatus.<a href="./src/unifieddatalibrary/resources/sitestatus/sitestatus.py">queryhelp</a>() -> None</code>
- <code title="get /udl/sitestatus/tuple">client.sitestatus.<a href="./src/unifieddatalibrary/resources/sitestatus/sitestatus.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/sitestatus_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/sitestatus_tuple_response.py">SitestatusTupleResponse</a></code>

## History

Types:

```python
from unifieddatalibrary.types.sitestatus import HistoryListResponse, HistoryCountResponse
```

Methods:

- <code title="get /udl/sitestatus/history">client.sitestatus.history.<a href="./src/unifieddatalibrary/resources/sitestatus/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/sitestatus/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/sitestatus/history_list_response.py">HistoryListResponse</a></code>
- <code title="get /udl/sitestatus/history/count">client.sitestatus.history.<a href="./src/unifieddatalibrary/resources/sitestatus/history.py">count</a>() -> str</code>

# Skyimagery

Types:

```python
from unifieddatalibrary.types import (
    SkyimageryListResponse,
    SkyimageryCountResponse,
    SkyimageryTupleResponse,
)
```

Methods:

- <code title="get /udl/skyimagery">client.skyimagery.<a href="./src/unifieddatalibrary/resources/skyimagery/skyimagery.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/skyimagery_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/skyimagery_list_response.py">SkyimageryListResponse</a></code>
- <code title="get /udl/skyimagery/count">client.skyimagery.<a href="./src/unifieddatalibrary/resources/skyimagery/skyimagery.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/skyimagery_count_params.py">params</a>) -> str</code>
- <code title="get /udl/skyimagery/getFile/{id}">client.skyimagery.<a href="./src/unifieddatalibrary/resources/skyimagery/skyimagery.py">file_get</a>(id) -> BinaryAPIResponse</code>
- <code title="get /udl/skyimagery/{id}">client.skyimagery.<a href="./src/unifieddatalibrary/resources/skyimagery/skyimagery.py">get</a>(id) -> <a href="./src/unifieddatalibrary/types/udl/skyimagery/skyimagery_full.py">SkyimageryFull</a></code>
- <code title="get /udl/skyimagery/queryhelp">client.skyimagery.<a href="./src/unifieddatalibrary/resources/skyimagery/skyimagery.py">queryhelp</a>() -> None</code>
- <code title="get /udl/skyimagery/tuple">client.skyimagery.<a href="./src/unifieddatalibrary/resources/skyimagery/skyimagery.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/skyimagery_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/skyimagery_tuple_response.py">SkyimageryTupleResponse</a></code>
- <code title="post /filedrop/udl-skyimagery">client.skyimagery.<a href="./src/unifieddatalibrary/resources/skyimagery/skyimagery.py">upload_zip</a>(\*\*<a href="src/unifieddatalibrary/types/skyimagery_upload_zip_params.py">params</a>) -> None</code>

## History

Types:

```python
from unifieddatalibrary.types.skyimagery import HistoryListResponse, HistoryCountResponse
```

Methods:

- <code title="get /udl/skyimagery/history">client.skyimagery.history.<a href="./src/unifieddatalibrary/resources/skyimagery/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/skyimagery/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/skyimagery/history_list_response.py">HistoryListResponse</a></code>
- <code title="get /udl/skyimagery/history/aodr">client.skyimagery.history.<a href="./src/unifieddatalibrary/resources/skyimagery/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/skyimagery/history_aodr_params.py">params</a>) -> None</code>
- <code title="get /udl/skyimagery/history/count">client.skyimagery.history.<a href="./src/unifieddatalibrary/resources/skyimagery/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/skyimagery/history_count_params.py">params</a>) -> str</code>

# Soiobservationset

Types:

```python
from unifieddatalibrary.types import (
    SoiobservationsetListResponse,
    SoiobservationsetCountResponse,
    SoiobservationsetTupleResponse,
)
```

Methods:

- <code title="post /udl/soiobservationset">client.soiobservationset.<a href="./src/unifieddatalibrary/resources/soiobservationset/soiobservationset.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/soiobservationset_create_params.py">params</a>) -> None</code>
- <code title="get /udl/soiobservationset">client.soiobservationset.<a href="./src/unifieddatalibrary/resources/soiobservationset/soiobservationset.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/soiobservationset_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/soiobservationset_list_response.py">SoiobservationsetListResponse</a></code>
- <code title="get /udl/soiobservationset/count">client.soiobservationset.<a href="./src/unifieddatalibrary/resources/soiobservationset/soiobservationset.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/soiobservationset_count_params.py">params</a>) -> str</code>
- <code title="post /udl/soiobservationset/createBulk">client.soiobservationset.<a href="./src/unifieddatalibrary/resources/soiobservationset/soiobservationset.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/soiobservationset_create_bulk_params.py">params</a>) -> None</code>
- <code title="post /filedrop/udl-soiobservationset">client.soiobservationset.<a href="./src/unifieddatalibrary/resources/soiobservationset/soiobservationset.py">create_bulk_v2</a>(\*\*<a href="src/unifieddatalibrary/types/soiobservationset_create_bulk_v2_params.py">params</a>) -> None</code>
- <code title="get /udl/soiobservationset/{id}">client.soiobservationset.<a href="./src/unifieddatalibrary/resources/soiobservationset/soiobservationset.py">get</a>(id) -> <a href="./src/unifieddatalibrary/types/soiobservationset/soi_observation_set_full.py">SoiObservationSetFull</a></code>
- <code title="get /udl/soiobservationset/queryhelp">client.soiobservationset.<a href="./src/unifieddatalibrary/resources/soiobservationset/soiobservationset.py">queryhelp</a>() -> None</code>
- <code title="get /udl/soiobservationset/tuple">client.soiobservationset.<a href="./src/unifieddatalibrary/resources/soiobservationset/soiobservationset.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/soiobservationset_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/soiobservationset_tuple_response.py">SoiobservationsetTupleResponse</a></code>

## History

Types:

```python
from unifieddatalibrary.types.soiobservationset import (
    SoiObservationSetFull,
    HistoryListResponse,
    HistoryCountResponse,
)
```

Methods:

- <code title="get /udl/soiobservationset/history">client.soiobservationset.history.<a href="./src/unifieddatalibrary/resources/soiobservationset/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/soiobservationset/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/soiobservationset/history_list_response.py">HistoryListResponse</a></code>
- <code title="get /udl/soiobservationset/history/aodr">client.soiobservationset.history.<a href="./src/unifieddatalibrary/resources/soiobservationset/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/soiobservationset/history_aodr_params.py">params</a>) -> None</code>
- <code title="get /udl/soiobservationset/history/count">client.soiobservationset.history.<a href="./src/unifieddatalibrary/resources/soiobservationset/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/soiobservationset/history_count_params.py">params</a>) -> str</code>

# Solararray

Types:

```python
from unifieddatalibrary.types import (
    SolararrayListResponse,
    SolararrayCountResponse,
    SolararrayGetResponse,
    SolararrayTupleResponse,
)
```

Methods:

- <code title="post /udl/solararray">client.solararray.<a href="./src/unifieddatalibrary/resources/solararray.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/solararray_create_params.py">params</a>) -> None</code>
- <code title="put /udl/solararray/{id}">client.solararray.<a href="./src/unifieddatalibrary/resources/solararray.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/solararray_update_params.py">params</a>) -> None</code>
- <code title="get /udl/solararray">client.solararray.<a href="./src/unifieddatalibrary/resources/solararray.py">list</a>() -> <a href="./src/unifieddatalibrary/types/solararray_list_response.py">SolararrayListResponse</a></code>
- <code title="delete /udl/solararray/{id}">client.solararray.<a href="./src/unifieddatalibrary/resources/solararray.py">delete</a>(id) -> None</code>
- <code title="get /udl/solararray/count">client.solararray.<a href="./src/unifieddatalibrary/resources/solararray.py">count</a>() -> str</code>
- <code title="get /udl/solararray/{id}">client.solararray.<a href="./src/unifieddatalibrary/resources/solararray.py">get</a>(id) -> <a href="./src/unifieddatalibrary/types/solararray_get_response.py">SolararrayGetResponse</a></code>
- <code title="get /udl/solararray/queryhelp">client.solararray.<a href="./src/unifieddatalibrary/resources/solararray.py">queryhelp</a>() -> None</code>
- <code title="get /udl/solararray/tuple">client.solararray.<a href="./src/unifieddatalibrary/resources/solararray.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/solararray_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/solararray_tuple_response.py">SolararrayTupleResponse</a></code>

# Solararraydetails

Types:

```python
from unifieddatalibrary.types import SolarArrayDetailsFull, SolararraydetailListResponse
```

Methods:

- <code title="post /udl/solararraydetails">client.solararraydetails.<a href="./src/unifieddatalibrary/resources/solararraydetails.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/solararraydetail_create_params.py">params</a>) -> None</code>
- <code title="put /udl/solararraydetails/{id}">client.solararraydetails.<a href="./src/unifieddatalibrary/resources/solararraydetails.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/solararraydetail_update_params.py">params</a>) -> None</code>
- <code title="get /udl/solararraydetails">client.solararraydetails.<a href="./src/unifieddatalibrary/resources/solararraydetails.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/solararraydetail_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/solararraydetail_list_response.py">SolararraydetailListResponse</a></code>
- <code title="delete /udl/solararraydetails/{id}">client.solararraydetails.<a href="./src/unifieddatalibrary/resources/solararraydetails.py">delete</a>(id) -> None</code>
- <code title="get /udl/solararraydetails/{id}">client.solararraydetails.<a href="./src/unifieddatalibrary/resources/solararraydetails.py">get</a>(id) -> <a href="./src/unifieddatalibrary/types/solar_array_details_full.py">SolarArrayDetailsFull</a></code>

# Sortieppr

Types:

```python
from unifieddatalibrary.types import (
    SortiepprListResponse,
    SortiepprCountResponse,
    SortiepprTupleResponse,
)
```

Methods:

- <code title="post /udl/sortieppr">client.sortieppr.<a href="./src/unifieddatalibrary/resources/sortieppr/sortieppr.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/sortieppr_create_params.py">params</a>) -> None</code>
- <code title="put /udl/sortieppr/{id}">client.sortieppr.<a href="./src/unifieddatalibrary/resources/sortieppr/sortieppr.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/sortieppr_update_params.py">params</a>) -> None</code>
- <code title="get /udl/sortieppr">client.sortieppr.<a href="./src/unifieddatalibrary/resources/sortieppr/sortieppr.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/sortieppr_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/sortieppr_list_response.py">SortiepprListResponse</a></code>
- <code title="delete /udl/sortieppr/{id}">client.sortieppr.<a href="./src/unifieddatalibrary/resources/sortieppr/sortieppr.py">delete</a>(id) -> None</code>
- <code title="get /udl/sortieppr/count">client.sortieppr.<a href="./src/unifieddatalibrary/resources/sortieppr/sortieppr.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/sortieppr_count_params.py">params</a>) -> str</code>
- <code title="post /udl/sortieppr/createBulk">client.sortieppr.<a href="./src/unifieddatalibrary/resources/sortieppr/sortieppr.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/sortieppr_create_bulk_params.py">params</a>) -> None</code>
- <code title="post /filedrop/udl-sortieppr">client.sortieppr.<a href="./src/unifieddatalibrary/resources/sortieppr/sortieppr.py">create_bulk_v2</a>(\*\*<a href="src/unifieddatalibrary/types/sortieppr_create_bulk_v2_params.py">params</a>) -> None</code>
- <code title="get /udl/sortieppr/{id}">client.sortieppr.<a href="./src/unifieddatalibrary/resources/sortieppr/sortieppr.py">get</a>(id) -> <a href="./src/unifieddatalibrary/types/sortieppr/sortie_ppr_full.py">SortiePprFull</a></code>
- <code title="get /udl/sortieppr/queryhelp">client.sortieppr.<a href="./src/unifieddatalibrary/resources/sortieppr/sortieppr.py">queryhelp</a>() -> None</code>
- <code title="get /udl/sortieppr/tuple">client.sortieppr.<a href="./src/unifieddatalibrary/resources/sortieppr/sortieppr.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/sortieppr_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/sortieppr_tuple_response.py">SortiepprTupleResponse</a></code>

## History

Types:

```python
from unifieddatalibrary.types.sortieppr import (
    SortiePprFull,
    HistoryListResponse,
    HistoryCountResponse,
)
```

Methods:

- <code title="get /udl/sortieppr/history">client.sortieppr.history.<a href="./src/unifieddatalibrary/resources/sortieppr/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/sortieppr/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/sortieppr/history_list_response.py">HistoryListResponse</a></code>
- <code title="get /udl/sortieppr/history/aodr">client.sortieppr.history.<a href="./src/unifieddatalibrary/resources/sortieppr/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/sortieppr/history_aodr_params.py">params</a>) -> None</code>
- <code title="get /udl/sortieppr/history/count">client.sortieppr.history.<a href="./src/unifieddatalibrary/resources/sortieppr/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/sortieppr/history_count_params.py">params</a>) -> str</code>

# Spaceenvobservation

Types:

```python
from unifieddatalibrary.types import (
    SpaceenvobservationListResponse,
    SpaceenvobservationCountResponse,
    SpaceenvobservationTupleResponse,
)
```

Methods:

- <code title="get /udl/spaceenvobservation">client.spaceenvobservation.<a href="./src/unifieddatalibrary/resources/spaceenvobservation/spaceenvobservation.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/spaceenvobservation_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/spaceenvobservation_list_response.py">SpaceenvobservationListResponse</a></code>
- <code title="get /udl/spaceenvobservation/count">client.spaceenvobservation.<a href="./src/unifieddatalibrary/resources/spaceenvobservation/spaceenvobservation.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/spaceenvobservation_count_params.py">params</a>) -> str</code>
- <code title="post /udl/spaceenvobservation/createBulk">client.spaceenvobservation.<a href="./src/unifieddatalibrary/resources/spaceenvobservation/spaceenvobservation.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/spaceenvobservation_create_bulk_params.py">params</a>) -> None</code>
- <code title="post /filedrop/udl-spaceenvobs">client.spaceenvobservation.<a href="./src/unifieddatalibrary/resources/spaceenvobservation/spaceenvobservation.py">create_bulk_v2</a>(\*\*<a href="src/unifieddatalibrary/types/spaceenvobservation_create_bulk_v2_params.py">params</a>) -> None</code>
- <code title="get /udl/spaceenvobservation/queryhelp">client.spaceenvobservation.<a href="./src/unifieddatalibrary/resources/spaceenvobservation/spaceenvobservation.py">queryhelp</a>() -> None</code>
- <code title="get /udl/spaceenvobservation/tuple">client.spaceenvobservation.<a href="./src/unifieddatalibrary/resources/spaceenvobservation/spaceenvobservation.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/spaceenvobservation_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/spaceenvobservation_tuple_response.py">SpaceenvobservationTupleResponse</a></code>

## History

Types:

```python
from unifieddatalibrary.types.spaceenvobservation import (
    SpaceEnvObservationFull,
    HistoryListResponse,
    HistoryCountResponse,
)
```

Methods:

- <code title="get /udl/spaceenvobservation/history">client.spaceenvobservation.history.<a href="./src/unifieddatalibrary/resources/spaceenvobservation/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/spaceenvobservation/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/spaceenvobservation/history_list_response.py">HistoryListResponse</a></code>
- <code title="get /udl/spaceenvobservation/history/aodr">client.spaceenvobservation.history.<a href="./src/unifieddatalibrary/resources/spaceenvobservation/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/spaceenvobservation/history_aodr_params.py">params</a>) -> None</code>
- <code title="get /udl/spaceenvobservation/history/count">client.spaceenvobservation.history.<a href="./src/unifieddatalibrary/resources/spaceenvobservation/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/spaceenvobservation/history_count_params.py">params</a>) -> str</code>

# Stage

Types:

```python
from unifieddatalibrary.types import (
    StageListResponse,
    StageCountResponse,
    StageGetResponse,
    StageTupleResponse,
)
```

Methods:

- <code title="post /udl/stage">client.stage.<a href="./src/unifieddatalibrary/resources/stage.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/stage_create_params.py">params</a>) -> None</code>
- <code title="put /udl/stage/{id}">client.stage.<a href="./src/unifieddatalibrary/resources/stage.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/stage_update_params.py">params</a>) -> None</code>
- <code title="get /udl/stage">client.stage.<a href="./src/unifieddatalibrary/resources/stage.py">list</a>() -> <a href="./src/unifieddatalibrary/types/stage_list_response.py">StageListResponse</a></code>
- <code title="delete /udl/stage/{id}">client.stage.<a href="./src/unifieddatalibrary/resources/stage.py">delete</a>(id) -> None</code>
- <code title="get /udl/stage/count">client.stage.<a href="./src/unifieddatalibrary/resources/stage.py">count</a>() -> str</code>
- <code title="get /udl/stage/{id}">client.stage.<a href="./src/unifieddatalibrary/resources/stage.py">get</a>(id) -> <a href="./src/unifieddatalibrary/types/stage_get_response.py">StageGetResponse</a></code>
- <code title="get /udl/stage/queryhelp">client.stage.<a href="./src/unifieddatalibrary/resources/stage.py">queryhelp</a>() -> None</code>
- <code title="get /udl/stage/tuple">client.stage.<a href="./src/unifieddatalibrary/resources/stage.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/stage_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/stage_tuple_response.py">StageTupleResponse</a></code>

# Starcatalog

Types:

```python
from unifieddatalibrary.types import (
    StarcatalogListResponse,
    StarcatalogCountResponse,
    StarcatalogGetResponse,
    StarcatalogTupleResponse,
)
```

Methods:

- <code title="post /udl/starcatalog">client.starcatalog.<a href="./src/unifieddatalibrary/resources/starcatalog/starcatalog.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/starcatalog_create_params.py">params</a>) -> None</code>
- <code title="put /udl/starcatalog/{id}">client.starcatalog.<a href="./src/unifieddatalibrary/resources/starcatalog/starcatalog.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/starcatalog_update_params.py">params</a>) -> None</code>
- <code title="get /udl/starcatalog">client.starcatalog.<a href="./src/unifieddatalibrary/resources/starcatalog/starcatalog.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/starcatalog_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/starcatalog_list_response.py">StarcatalogListResponse</a></code>
- <code title="delete /udl/starcatalog/{id}">client.starcatalog.<a href="./src/unifieddatalibrary/resources/starcatalog/starcatalog.py">delete</a>(id) -> None</code>
- <code title="get /udl/starcatalog/count">client.starcatalog.<a href="./src/unifieddatalibrary/resources/starcatalog/starcatalog.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/starcatalog_count_params.py">params</a>) -> str</code>
- <code title="post /udl/starcatalog/createBulk">client.starcatalog.<a href="./src/unifieddatalibrary/resources/starcatalog/starcatalog.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/starcatalog_create_bulk_params.py">params</a>) -> None</code>
- <code title="post /filedrop/udl-starcatalog">client.starcatalog.<a href="./src/unifieddatalibrary/resources/starcatalog/starcatalog.py">create_bulk_v2</a>(\*\*<a href="src/unifieddatalibrary/types/starcatalog_create_bulk_v2_params.py">params</a>) -> None</code>
- <code title="get /udl/starcatalog/{id}">client.starcatalog.<a href="./src/unifieddatalibrary/resources/starcatalog/starcatalog.py">get</a>(id) -> <a href="./src/unifieddatalibrary/types/starcatalog_get_response.py">StarcatalogGetResponse</a></code>
- <code title="get /udl/starcatalog/queryhelp">client.starcatalog.<a href="./src/unifieddatalibrary/resources/starcatalog/starcatalog.py">queryhelp</a>() -> None</code>
- <code title="get /udl/starcatalog/tuple">client.starcatalog.<a href="./src/unifieddatalibrary/resources/starcatalog/starcatalog.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/starcatalog_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/starcatalog_tuple_response.py">StarcatalogTupleResponse</a></code>

## History

Methods:

- <code title="get /udl/starcatalog/history/aodr">client.starcatalog.history.<a href="./src/unifieddatalibrary/resources/starcatalog/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/starcatalog/history_aodr_params.py">params</a>) -> None</code>

# Statevector

Types:

```python
from unifieddatalibrary.types import (
    StateVectorAbridged,
    StateVectorFull,
    StateVectorIngest,
    StatevectorListResponse,
    StatevectorCountResponse,
    StatevectorTupleResponse,
)
```

Methods:

- <code title="post /udl/statevector">client.statevector.<a href="./src/unifieddatalibrary/resources/statevector/statevector.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/statevector_create_params.py">params</a>) -> None</code>
- <code title="get /udl/statevector">client.statevector.<a href="./src/unifieddatalibrary/resources/statevector/statevector.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/statevector_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/statevector_list_response.py">StatevectorListResponse</a></code>
- <code title="get /udl/statevector/count">client.statevector.<a href="./src/unifieddatalibrary/resources/statevector/statevector.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/statevector_count_params.py">params</a>) -> str</code>
- <code title="post /udl/statevector/createBulk">client.statevector.<a href="./src/unifieddatalibrary/resources/statevector/statevector.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/statevector_create_bulk_params.py">params</a>) -> None</code>
- <code title="post /filedrop/udl-sv">client.statevector.<a href="./src/unifieddatalibrary/resources/statevector/statevector.py">create_bulk_v2</a>(\*\*<a href="src/unifieddatalibrary/types/statevector_create_bulk_v2_params.py">params</a>) -> None</code>
- <code title="get /udl/statevector/{id}">client.statevector.<a href="./src/unifieddatalibrary/resources/statevector/statevector.py">get</a>(id) -> <a href="./src/unifieddatalibrary/types/state_vector_full.py">StateVectorFull</a></code>
- <code title="get /udl/statevector/queryhelp">client.statevector.<a href="./src/unifieddatalibrary/resources/statevector/statevector.py">queryhelp</a>() -> None</code>
- <code title="get /udl/statevector/tuple">client.statevector.<a href="./src/unifieddatalibrary/resources/statevector/statevector.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/statevector_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/statevector_tuple_response.py">StatevectorTupleResponse</a></code>

## History

Types:

```python
from unifieddatalibrary.types.statevector import HistoryListResponse, HistoryCountResponse
```

Methods:

- <code title="get /udl/statevector/history">client.statevector.history.<a href="./src/unifieddatalibrary/resources/statevector/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/statevector/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/statevector/history_list_response.py">HistoryListResponse</a></code>
- <code title="get /udl/statevector/history/aodr">client.statevector.history.<a href="./src/unifieddatalibrary/resources/statevector/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/statevector/history_aodr_params.py">params</a>) -> None</code>
- <code title="get /udl/statevector/history/count">client.statevector.history.<a href="./src/unifieddatalibrary/resources/statevector/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/statevector/history_count_params.py">params</a>) -> str</code>

## Current

Types:

```python
from unifieddatalibrary.types.statevector import CurrentListResponse, CurrentTupleResponse
```

Methods:

- <code title="get /udl/statevector/current">client.statevector.current.<a href="./src/unifieddatalibrary/resources/statevector/current.py">list</a>() -> <a href="./src/unifieddatalibrary/types/statevector/current_list_response.py">CurrentListResponse</a></code>
- <code title="get /udl/statevector/current/tuple">client.statevector.current.<a href="./src/unifieddatalibrary/resources/statevector/current.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/statevector/current_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/statevector/current_tuple_response.py">CurrentTupleResponse</a></code>

# Status

Types:

```python
from unifieddatalibrary.types import (
    StatusListResponse,
    StatusCountResponse,
    StatusGetResponse,
    StatusGetByEntityIDResponse,
    StatusGetByEntityTypeResponse,
    StatusTupleResponse,
)
```

Methods:

- <code title="post /udl/status">client.status.<a href="./src/unifieddatalibrary/resources/status.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/status_create_params.py">params</a>) -> None</code>
- <code title="put /udl/status/{id}">client.status.<a href="./src/unifieddatalibrary/resources/status.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/status_update_params.py">params</a>) -> None</code>
- <code title="get /udl/status">client.status.<a href="./src/unifieddatalibrary/resources/status.py">list</a>() -> <a href="./src/unifieddatalibrary/types/status_list_response.py">StatusListResponse</a></code>
- <code title="delete /udl/status/{id}">client.status.<a href="./src/unifieddatalibrary/resources/status.py">delete</a>(id) -> None</code>
- <code title="get /udl/status/count">client.status.<a href="./src/unifieddatalibrary/resources/status.py">count</a>() -> str</code>
- <code title="get /udl/status/{id}">client.status.<a href="./src/unifieddatalibrary/resources/status.py">get</a>(id) -> <a href="./src/unifieddatalibrary/types/status_get_response.py">StatusGetResponse</a></code>
- <code title="get /udl/status/byIdEntity/{idEntity}">client.status.<a href="./src/unifieddatalibrary/resources/status.py">get_by_entity_id</a>(id_entity) -> <a href="./src/unifieddatalibrary/types/status_get_by_entity_id_response.py">StatusGetByEntityIDResponse</a></code>
- <code title="get /udl/status/byEntityType/{entityType}">client.status.<a href="./src/unifieddatalibrary/resources/status.py">get_by_entity_type</a>(entity_type) -> <a href="./src/unifieddatalibrary/types/status_get_by_entity_type_response.py">StatusGetByEntityTypeResponse</a></code>
- <code title="get /udl/status/queryhelp">client.status.<a href="./src/unifieddatalibrary/resources/status.py">queryhelp</a>() -> None</code>
- <code title="get /udl/status/tuple">client.status.<a href="./src/unifieddatalibrary/resources/status.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/status_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/status_tuple_response.py">StatusTupleResponse</a></code>

# Substatus

Types:

```python
from unifieddatalibrary.types import (
    SubstatusListResponse,
    SubstatusCountResponse,
    SubstatusGetResponse,
    SubstatusTupleResponse,
)
```

Methods:

- <code title="post /udl/substatus">client.substatus.<a href="./src/unifieddatalibrary/resources/substatus.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/substatus_create_params.py">params</a>) -> None</code>
- <code title="put /udl/substatus/{id}">client.substatus.<a href="./src/unifieddatalibrary/resources/substatus.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/substatus_update_params.py">params</a>) -> None</code>
- <code title="get /udl/substatus">client.substatus.<a href="./src/unifieddatalibrary/resources/substatus.py">list</a>() -> <a href="./src/unifieddatalibrary/types/substatus_list_response.py">SubstatusListResponse</a></code>
- <code title="delete /udl/substatus/{id}">client.substatus.<a href="./src/unifieddatalibrary/resources/substatus.py">delete</a>(id) -> None</code>
- <code title="get /udl/substatus/count">client.substatus.<a href="./src/unifieddatalibrary/resources/substatus.py">count</a>() -> str</code>
- <code title="get /udl/substatus/{id}">client.substatus.<a href="./src/unifieddatalibrary/resources/substatus.py">get</a>(id) -> <a href="./src/unifieddatalibrary/types/substatus_get_response.py">SubstatusGetResponse</a></code>
- <code title="get /udl/substatus/queryhelp">client.substatus.<a href="./src/unifieddatalibrary/resources/substatus.py">queryhelp</a>() -> None</code>
- <code title="get /udl/substatus/tuple">client.substatus.<a href="./src/unifieddatalibrary/resources/substatus.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/substatus_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/substatus_tuple_response.py">SubstatusTupleResponse</a></code>

# SupportingData

## DataTypes

Types:

```python
from unifieddatalibrary.types.supporting_data import DataTypeListResponse
```

Methods:

- <code title="get /udl/dataowner/getDataTypes">client.supporting_data.data_types.<a href="./src/unifieddatalibrary/resources/supporting_data/data_types.py">list</a>() -> <a href="./src/unifieddatalibrary/types/supporting_data/data_type_list_response.py">DataTypeListResponse</a></code>

## Dataowner

Types:

```python
from unifieddatalibrary.types.supporting_data import (
    DataownerAbridged,
    DataownerRetrieveResponse,
    DataownerCountResponse,
)
```

Methods:

- <code title="get /udl/dataowner">client.supporting_data.dataowner.<a href="./src/unifieddatalibrary/resources/supporting_data/dataowner.py">retrieve</a>() -> <a href="./src/unifieddatalibrary/types/supporting_data/dataowner_retrieve_response.py">DataownerRetrieveResponse</a></code>
- <code title="get /udl/dataowner/count">client.supporting_data.dataowner.<a href="./src/unifieddatalibrary/resources/supporting_data/dataowner.py">count</a>() -> str</code>

## DataownerTypes

Types:

```python
from unifieddatalibrary.types.supporting_data import DataownerTypeListResponse
```

Methods:

- <code title="get /udl/dataowner/getDataOwnerTypes">client.supporting_data.dataowner_types.<a href="./src/unifieddatalibrary/resources/supporting_data/dataowner_types.py">list</a>() -> <a href="./src/unifieddatalibrary/types/supporting_data/dataowner_type_list_response.py">DataownerTypeListResponse</a></code>

## ProviderMetadata

Types:

```python
from unifieddatalibrary.types.supporting_data import ProviderMetadataRetrieveResponse
```

Methods:

- <code title="get /udl/dataowner/providerMetadata">client.supporting_data.provider_metadata.<a href="./src/unifieddatalibrary/resources/supporting_data/provider_metadata.py">retrieve</a>() -> <a href="./src/unifieddatalibrary/types/supporting_data/provider_metadata_retrieve_response.py">ProviderMetadataRetrieveResponse</a></code>

## QueryHelp

Methods:

- <code title="get /udl/dataowner/queryhelp">client.supporting_data.query_help.<a href="./src/unifieddatalibrary/resources/supporting_data/query_help.py">retrieve</a>() -> None</code>

# Surface

Types:

```python
from unifieddatalibrary.types import (
    SurfaceListResponse,
    SurfaceCountResponse,
    SurfaceGetResponse,
    SurfaceTupleResponse,
)
```

Methods:

- <code title="post /udl/surface">client.surface.<a href="./src/unifieddatalibrary/resources/surface.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/surface_create_params.py">params</a>) -> None</code>
- <code title="put /udl/surface/{id}">client.surface.<a href="./src/unifieddatalibrary/resources/surface.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/surface_update_params.py">params</a>) -> None</code>
- <code title="get /udl/surface">client.surface.<a href="./src/unifieddatalibrary/resources/surface.py">list</a>() -> <a href="./src/unifieddatalibrary/types/surface_list_response.py">SurfaceListResponse</a></code>
- <code title="delete /udl/surface/{id}">client.surface.<a href="./src/unifieddatalibrary/resources/surface.py">delete</a>(id) -> None</code>
- <code title="get /udl/surface/count">client.surface.<a href="./src/unifieddatalibrary/resources/surface.py">count</a>() -> str</code>
- <code title="get /udl/surface/{id}">client.surface.<a href="./src/unifieddatalibrary/resources/surface.py">get</a>(id) -> <a href="./src/unifieddatalibrary/types/surface_get_response.py">SurfaceGetResponse</a></code>
- <code title="get /udl/surface/queryhelp">client.surface.<a href="./src/unifieddatalibrary/resources/surface.py">queryhelp</a>() -> None</code>
- <code title="get /udl/surface/tuple">client.surface.<a href="./src/unifieddatalibrary/resources/surface.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/surface_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/surface_tuple_response.py">SurfaceTupleResponse</a></code>

# Surfaceobstruction

Types:

```python
from unifieddatalibrary.types import (
    SurfaceobstructionListResponse,
    SurfaceobstructionCountResponse,
    SurfaceobstructionGetResponse,
    SurfaceobstructionTupleResponse,
)
```

Methods:

- <code title="post /udl/surfaceobstruction">client.surfaceobstruction.<a href="./src/unifieddatalibrary/resources/surfaceobstruction.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/surfaceobstruction_create_params.py">params</a>) -> None</code>
- <code title="put /udl/surfaceobstruction/{id}">client.surfaceobstruction.<a href="./src/unifieddatalibrary/resources/surfaceobstruction.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/surfaceobstruction_update_params.py">params</a>) -> None</code>
- <code title="get /udl/surfaceobstruction">client.surfaceobstruction.<a href="./src/unifieddatalibrary/resources/surfaceobstruction.py">list</a>() -> <a href="./src/unifieddatalibrary/types/surfaceobstruction_list_response.py">SurfaceobstructionListResponse</a></code>
- <code title="delete /udl/surfaceobstruction/{id}">client.surfaceobstruction.<a href="./src/unifieddatalibrary/resources/surfaceobstruction.py">delete</a>(id) -> None</code>
- <code title="get /udl/surfaceobstruction/count">client.surfaceobstruction.<a href="./src/unifieddatalibrary/resources/surfaceobstruction.py">count</a>() -> str</code>
- <code title="post /filedrop/udl-surfaceobstruction">client.surfaceobstruction.<a href="./src/unifieddatalibrary/resources/surfaceobstruction.py">create_bulk_v2</a>(\*\*<a href="src/unifieddatalibrary/types/surfaceobstruction_create_bulk_v2_params.py">params</a>) -> None</code>
- <code title="get /udl/surfaceobstruction/{id}">client.surfaceobstruction.<a href="./src/unifieddatalibrary/resources/surfaceobstruction.py">get</a>(id) -> <a href="./src/unifieddatalibrary/types/surfaceobstruction_get_response.py">SurfaceobstructionGetResponse</a></code>
- <code title="get /udl/surfaceobstruction/queryhelp">client.surfaceobstruction.<a href="./src/unifieddatalibrary/resources/surfaceobstruction.py">queryhelp</a>() -> None</code>
- <code title="get /udl/surfaceobstruction/tuple">client.surfaceobstruction.<a href="./src/unifieddatalibrary/resources/surfaceobstruction.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/surfaceobstruction_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/surfaceobstruction_tuple_response.py">SurfaceobstructionTupleResponse</a></code>

# Swir

Types:

```python
from unifieddatalibrary.types import SwirListResponse, SwirCountResponse, SwirTupleResponse
```

Methods:

- <code title="post /udl/swir">client.swir.<a href="./src/unifieddatalibrary/resources/swir/swir.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/swir_create_params.py">params</a>) -> None</code>
- <code title="get /udl/swir">client.swir.<a href="./src/unifieddatalibrary/resources/swir/swir.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/swir_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/swir_list_response.py">SwirListResponse</a></code>
- <code title="get /udl/swir/count">client.swir.<a href="./src/unifieddatalibrary/resources/swir/swir.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/swir_count_params.py">params</a>) -> str</code>
- <code title="post /udl/swir/createBulk">client.swir.<a href="./src/unifieddatalibrary/resources/swir/swir.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/swir_create_bulk_params.py">params</a>) -> None</code>
- <code title="get /udl/swir/{id}">client.swir.<a href="./src/unifieddatalibrary/resources/swir/swir.py">get</a>(id) -> <a href="./src/unifieddatalibrary/types/swir/swir_full.py">SwirFull</a></code>
- <code title="get /udl/swir/queryhelp">client.swir.<a href="./src/unifieddatalibrary/resources/swir/swir.py">queryhelp</a>() -> None</code>
- <code title="get /udl/swir/tuple">client.swir.<a href="./src/unifieddatalibrary/resources/swir/swir.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/swir_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/swir_tuple_response.py">SwirTupleResponse</a></code>

## History

Types:

```python
from unifieddatalibrary.types.swir import SwirFull, HistoryListResponse, HistoryCountResponse
```

Methods:

- <code title="get /udl/swir/history">client.swir.history.<a href="./src/unifieddatalibrary/resources/swir/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/swir/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/swir/history_list_response.py">HistoryListResponse</a></code>
- <code title="get /udl/swir/history/aodr">client.swir.history.<a href="./src/unifieddatalibrary/resources/swir/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/swir/history_aodr_params.py">params</a>) -> None</code>
- <code title="get /udl/swir/history/count">client.swir.history.<a href="./src/unifieddatalibrary/resources/swir/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/swir/history_count_params.py">params</a>) -> str</code>

# Taiutc

Types:

```python
from unifieddatalibrary.types import TaiutcListResponse, TaiutcCountResponse, TaiutcTupleResponse
```

Methods:

- <code title="post /udl/taiutc">client.taiutc.<a href="./src/unifieddatalibrary/resources/taiutc/taiutc.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/taiutc_create_params.py">params</a>) -> None</code>
- <code title="put /udl/taiutc/{id}">client.taiutc.<a href="./src/unifieddatalibrary/resources/taiutc/taiutc.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/taiutc_update_params.py">params</a>) -> None</code>
- <code title="get /udl/taiutc">client.taiutc.<a href="./src/unifieddatalibrary/resources/taiutc/taiutc.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/taiutc_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/taiutc_list_response.py">TaiutcListResponse</a></code>
- <code title="delete /udl/taiutc/{id}">client.taiutc.<a href="./src/unifieddatalibrary/resources/taiutc/taiutc.py">delete</a>(id) -> None</code>
- <code title="get /udl/taiutc/count">client.taiutc.<a href="./src/unifieddatalibrary/resources/taiutc/taiutc.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/taiutc_count_params.py">params</a>) -> str</code>
- <code title="get /udl/taiutc/{id}">client.taiutc.<a href="./src/unifieddatalibrary/resources/taiutc/taiutc.py">get</a>(id) -> <a href="./src/unifieddatalibrary/types/taiutc/taiutc_full.py">TaiutcFull</a></code>
- <code title="get /udl/taiutc/queryhelp">client.taiutc.<a href="./src/unifieddatalibrary/resources/taiutc/taiutc.py">queryhelp</a>() -> None</code>
- <code title="get /udl/taiutc/tuple">client.taiutc.<a href="./src/unifieddatalibrary/resources/taiutc/taiutc.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/taiutc_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/taiutc_tuple_response.py">TaiutcTupleResponse</a></code>

## History

Types:

```python
from unifieddatalibrary.types.taiutc import TaiutcFull, HistoryListResponse, HistoryCountResponse
```

Methods:

- <code title="get /udl/taiutc/history">client.taiutc.history.<a href="./src/unifieddatalibrary/resources/taiutc/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/taiutc/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/taiutc/history_list_response.py">HistoryListResponse</a></code>
- <code title="get /udl/taiutc/history/aodr">client.taiutc.history.<a href="./src/unifieddatalibrary/resources/taiutc/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/taiutc/history_aodr_params.py">params</a>) -> None</code>
- <code title="get /udl/taiutc/history/count">client.taiutc.history.<a href="./src/unifieddatalibrary/resources/taiutc/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/taiutc/history_count_params.py">params</a>) -> str</code>

# TdoaFdoa

## Diffofarrival

Types:

```python
from unifieddatalibrary.types.tdoa_fdoa import (
    DiffofarrivalAbridged,
    DiffofarrivalFull,
    DiffofarrivalListResponse,
    DiffofarrivalCountResponse,
)
```

Methods:

- <code title="post /udl/diffofarrival">client.tdoa_fdoa.diffofarrival.<a href="./src/unifieddatalibrary/resources/tdoa_fdoa/diffofarrival/diffofarrival.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/tdoa_fdoa/diffofarrival_create_params.py">params</a>) -> None</code>
- <code title="get /udl/diffofarrival">client.tdoa_fdoa.diffofarrival.<a href="./src/unifieddatalibrary/resources/tdoa_fdoa/diffofarrival/diffofarrival.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/tdoa_fdoa/diffofarrival_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/tdoa_fdoa/diffofarrival_list_response.py">DiffofarrivalListResponse</a></code>
- <code title="get /udl/diffofarrival/count">client.tdoa_fdoa.diffofarrival.<a href="./src/unifieddatalibrary/resources/tdoa_fdoa/diffofarrival/diffofarrival.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/tdoa_fdoa/diffofarrival_count_params.py">params</a>) -> str</code>
- <code title="post /udl/diffofarrival/createBulk">client.tdoa_fdoa.diffofarrival.<a href="./src/unifieddatalibrary/resources/tdoa_fdoa/diffofarrival/diffofarrival.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/tdoa_fdoa/diffofarrival_create_bulk_params.py">params</a>) -> None</code>

### History

Types:

```python
from unifieddatalibrary.types.tdoa_fdoa.diffofarrival import HistoryListResponse
```

Methods:

- <code title="get /udl/diffofarrival/history">client.tdoa_fdoa.diffofarrival.history.<a href="./src/unifieddatalibrary/resources/tdoa_fdoa/diffofarrival/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/tdoa_fdoa/diffofarrival/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/tdoa_fdoa/diffofarrival/history_list_response.py">HistoryListResponse</a></code>
- <code title="get /udl/diffofarrival/history/aodr">client.tdoa_fdoa.diffofarrival.history.<a href="./src/unifieddatalibrary/resources/tdoa_fdoa/diffofarrival/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/tdoa_fdoa/diffofarrival/history_aodr_params.py">params</a>) -> None</code>

# Track

Types:

```python
from unifieddatalibrary.types import TrackListResponse, TrackCountResponse, TrackTupleResponse
```

Methods:

- <code title="get /udl/track">client.track.<a href="./src/unifieddatalibrary/resources/track/track.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/track_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/track_list_response.py">TrackListResponse</a></code>
- <code title="get /udl/track/count">client.track.<a href="./src/unifieddatalibrary/resources/track/track.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/track_count_params.py">params</a>) -> str</code>
- <code title="post /udl/track/createBulk">client.track.<a href="./src/unifieddatalibrary/resources/track/track.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/track_create_bulk_params.py">params</a>) -> None</code>
- <code title="post /filedrop/udl-tracks">client.track.<a href="./src/unifieddatalibrary/resources/track/track.py">create_bulk_v2</a>(\*\*<a href="src/unifieddatalibrary/types/track_create_bulk_v2_params.py">params</a>) -> None</code>
- <code title="get /udl/track/queryhelp">client.track.<a href="./src/unifieddatalibrary/resources/track/track.py">queryhelp</a>() -> None</code>
- <code title="get /udl/track/tuple">client.track.<a href="./src/unifieddatalibrary/resources/track/track.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/track_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/track_tuple_response.py">TrackTupleResponse</a></code>

## History

Types:

```python
from unifieddatalibrary.types.track import TrackFull, HistoryListResponse, HistoryCountResponse
```

Methods:

- <code title="get /udl/track/history">client.track.history.<a href="./src/unifieddatalibrary/resources/track/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/track/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/track/history_list_response.py">HistoryListResponse</a></code>
- <code title="get /udl/track/history/aodr">client.track.history.<a href="./src/unifieddatalibrary/resources/track/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/track/history_aodr_params.py">params</a>) -> None</code>
- <code title="get /udl/track/history/count">client.track.history.<a href="./src/unifieddatalibrary/resources/track/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/track/history_count_params.py">params</a>) -> str</code>

# Trackdetails

Types:

```python
from unifieddatalibrary.types import (
    TrackdetailListResponse,
    TrackdetailCountResponse,
    TrackdetailTupleResponse,
)
```

Methods:

- <code title="get /udl/trackdetails">client.trackdetails.<a href="./src/unifieddatalibrary/resources/trackdetails/trackdetails.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/trackdetail_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/trackdetail_list_response.py">TrackdetailListResponse</a></code>
- <code title="get /udl/trackdetails/count">client.trackdetails.<a href="./src/unifieddatalibrary/resources/trackdetails/trackdetails.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/trackdetail_count_params.py">params</a>) -> str</code>
- <code title="post /udl/trackdetails/createBulk">client.trackdetails.<a href="./src/unifieddatalibrary/resources/trackdetails/trackdetails.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/trackdetail_create_bulk_params.py">params</a>) -> None</code>
- <code title="get /udl/trackdetails/queryhelp">client.trackdetails.<a href="./src/unifieddatalibrary/resources/trackdetails/trackdetails.py">queryhelp</a>() -> None</code>
- <code title="get /udl/trackdetails/tuple">client.trackdetails.<a href="./src/unifieddatalibrary/resources/trackdetails/trackdetails.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/trackdetail_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/trackdetail_tuple_response.py">TrackdetailTupleResponse</a></code>

## History

Types:

```python
from unifieddatalibrary.types.trackdetails import (
    TrackDetailsFull,
    HistoryListResponse,
    HistoryCountResponse,
)
```

Methods:

- <code title="get /udl/trackdetails/history">client.trackdetails.history.<a href="./src/unifieddatalibrary/resources/trackdetails/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/trackdetails/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/trackdetails/history_list_response.py">HistoryListResponse</a></code>
- <code title="get /udl/trackdetails/history/aodr">client.trackdetails.history.<a href="./src/unifieddatalibrary/resources/trackdetails/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/trackdetails/history_aodr_params.py">params</a>) -> None</code>
- <code title="get /udl/trackdetails/history/count">client.trackdetails.history.<a href="./src/unifieddatalibrary/resources/trackdetails/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/trackdetails/history_count_params.py">params</a>) -> str</code>

# Trackroute

Types:

```python
from unifieddatalibrary.types import (
    TrackrouteListResponse,
    TrackrouteCountResponse,
    TrackrouteTupleResponse,
)
```

Methods:

- <code title="post /udl/trackroute">client.trackroute.<a href="./src/unifieddatalibrary/resources/trackroute/trackroute.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/trackroute_create_params.py">params</a>) -> None</code>
- <code title="put /udl/trackroute/{id}">client.trackroute.<a href="./src/unifieddatalibrary/resources/trackroute/trackroute.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/trackroute_update_params.py">params</a>) -> None</code>
- <code title="get /udl/trackroute">client.trackroute.<a href="./src/unifieddatalibrary/resources/trackroute/trackroute.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/trackroute_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/trackroute_list_response.py">TrackrouteListResponse</a></code>
- <code title="delete /udl/trackroute/{id}">client.trackroute.<a href="./src/unifieddatalibrary/resources/trackroute/trackroute.py">delete</a>(id) -> None</code>
- <code title="get /udl/trackroute/count">client.trackroute.<a href="./src/unifieddatalibrary/resources/trackroute/trackroute.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/trackroute_count_params.py">params</a>) -> str</code>
- <code title="post /udl/trackroute/createBulk">client.trackroute.<a href="./src/unifieddatalibrary/resources/trackroute/trackroute.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/trackroute_create_bulk_params.py">params</a>) -> None</code>
- <code title="post /filedrop/udl-trackroute">client.trackroute.<a href="./src/unifieddatalibrary/resources/trackroute/trackroute.py">create_bulk_v2</a>(\*\*<a href="src/unifieddatalibrary/types/trackroute_create_bulk_v2_params.py">params</a>) -> None</code>
- <code title="get /udl/trackroute/{id}">client.trackroute.<a href="./src/unifieddatalibrary/resources/trackroute/trackroute.py">get</a>(id) -> <a href="./src/unifieddatalibrary/types/trackroute/track_route_full.py">TrackRouteFull</a></code>
- <code title="get /udl/trackroute/queryhelp">client.trackroute.<a href="./src/unifieddatalibrary/resources/trackroute/trackroute.py">queryhelp</a>() -> None</code>
- <code title="get /udl/trackroute/tuple">client.trackroute.<a href="./src/unifieddatalibrary/resources/trackroute/trackroute.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/trackroute_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/trackroute_tuple_response.py">TrackrouteTupleResponse</a></code>

## History

Types:

```python
from unifieddatalibrary.types.trackroute import (
    TrackRouteFull,
    HistoryListResponse,
    HistoryCountResponse,
)
```

Methods:

- <code title="get /udl/trackroute/history">client.trackroute.history.<a href="./src/unifieddatalibrary/resources/trackroute/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/trackroute/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/trackroute/history_list_response.py">HistoryListResponse</a></code>
- <code title="get /udl/trackroute/history/aodr">client.trackroute.history.<a href="./src/unifieddatalibrary/resources/trackroute/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/trackroute/history_aodr_params.py">params</a>) -> None</code>
- <code title="get /udl/trackroute/history/count">client.trackroute.history.<a href="./src/unifieddatalibrary/resources/trackroute/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/trackroute/history_count_params.py">params</a>) -> str</code>

# Transponder

Types:

```python
from unifieddatalibrary.types import (
    TransponderListResponse,
    TransponderCountResponse,
    TransponderGetResponse,
    TransponderTupleResponse,
)
```

Methods:

- <code title="post /udl/transponder">client.transponder.<a href="./src/unifieddatalibrary/resources/transponder.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/transponder_create_params.py">params</a>) -> None</code>
- <code title="put /udl/transponder/{id}">client.transponder.<a href="./src/unifieddatalibrary/resources/transponder.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/transponder_update_params.py">params</a>) -> None</code>
- <code title="get /udl/transponder">client.transponder.<a href="./src/unifieddatalibrary/resources/transponder.py">list</a>() -> <a href="./src/unifieddatalibrary/types/transponder_list_response.py">TransponderListResponse</a></code>
- <code title="delete /udl/transponder/{id}">client.transponder.<a href="./src/unifieddatalibrary/resources/transponder.py">delete</a>(id) -> None</code>
- <code title="get /udl/transponder/count">client.transponder.<a href="./src/unifieddatalibrary/resources/transponder.py">count</a>() -> str</code>
- <code title="get /udl/transponder/{id}">client.transponder.<a href="./src/unifieddatalibrary/resources/transponder.py">get</a>(id) -> <a href="./src/unifieddatalibrary/types/transponder_get_response.py">TransponderGetResponse</a></code>
- <code title="get /udl/transponder/queryhelp">client.transponder.<a href="./src/unifieddatalibrary/resources/transponder.py">queryhelp</a>() -> None</code>
- <code title="get /udl/transponder/tuple">client.transponder.<a href="./src/unifieddatalibrary/resources/transponder.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/transponder_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/transponder_tuple_response.py">TransponderTupleResponse</a></code>

# Vessel

Types:

```python
from unifieddatalibrary.types import (
    VesselListResponse,
    VesselCountResponse,
    VesselGetResponse,
    VesselTupleResponse,
)
```

Methods:

- <code title="post /udl/vessel">client.vessel.<a href="./src/unifieddatalibrary/resources/vessel.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/vessel_create_params.py">params</a>) -> None</code>
- <code title="put /udl/vessel/{id}">client.vessel.<a href="./src/unifieddatalibrary/resources/vessel.py">update</a>(path_id, \*\*<a href="src/unifieddatalibrary/types/vessel_update_params.py">params</a>) -> None</code>
- <code title="get /udl/vessel">client.vessel.<a href="./src/unifieddatalibrary/resources/vessel.py">list</a>() -> <a href="./src/unifieddatalibrary/types/vessel_list_response.py">VesselListResponse</a></code>
- <code title="get /udl/vessel/count">client.vessel.<a href="./src/unifieddatalibrary/resources/vessel.py">count</a>() -> str</code>
- <code title="post /udl/vessel/createBulk">client.vessel.<a href="./src/unifieddatalibrary/resources/vessel.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/vessel_create_bulk_params.py">params</a>) -> None</code>
- <code title="get /udl/vessel/{id}">client.vessel.<a href="./src/unifieddatalibrary/resources/vessel.py">get</a>(id) -> <a href="./src/unifieddatalibrary/types/vessel_get_response.py">VesselGetResponse</a></code>
- <code title="get /udl/vessel/queryhelp">client.vessel.<a href="./src/unifieddatalibrary/resources/vessel.py">queryhelp</a>() -> None</code>
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
    VideoTupleResponse,
)
```

Methods:

- <code title="post /udl/video">client.video.<a href="./src/unifieddatalibrary/resources/video/video.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/video_create_params.py">params</a>) -> None</code>
- <code title="get /udl/video">client.video.<a href="./src/unifieddatalibrary/resources/video/video.py">list</a>() -> <a href="./src/unifieddatalibrary/types/video_list_response.py">VideoListResponse</a></code>
- <code title="get /udl/video/count">client.video.<a href="./src/unifieddatalibrary/resources/video/video.py">count</a>() -> str</code>
- <code title="get /udl/video/{id}">client.video.<a href="./src/unifieddatalibrary/resources/video/video.py">get</a>(id) -> <a href="./src/unifieddatalibrary/types/video/video_streams_full.py">VideoStreamsFull</a></code>
- <code title="get /udl/video/getPlayerStreamingInfo">client.video.<a href="./src/unifieddatalibrary/resources/video/video.py">get_player_streaming_info</a>(\*\*<a href="src/unifieddatalibrary/types/video_get_player_streaming_info_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/video_get_player_streaming_info_response.py">VideoGetPlayerStreamingInfoResponse</a></code>
- <code title="get /udl/video/getPublisherStreamingInfo">client.video.<a href="./src/unifieddatalibrary/resources/video/video.py">get_publisher_streaming_info</a>(\*\*<a href="src/unifieddatalibrary/types/video_get_publisher_streaming_info_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/video_get_publisher_streaming_info_response.py">VideoGetPublisherStreamingInfoResponse</a></code>
- <code title="get /udl/video/getStreamFile">client.video.<a href="./src/unifieddatalibrary/resources/video/video.py">get_stream_file</a>(\*\*<a href="src/unifieddatalibrary/types/video_get_stream_file_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/video_get_stream_file_response.py">VideoGetStreamFileResponse</a></code>
- <code title="get /udl/video/queryhelp">client.video.<a href="./src/unifieddatalibrary/resources/video/video.py">queryhelp</a>() -> None</code>
- <code title="get /udl/video/tuple">client.video.<a href="./src/unifieddatalibrary/resources/video/video.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/video_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/video_tuple_response.py">VideoTupleResponse</a></code>

## History

Types:

```python
from unifieddatalibrary.types.video import (
    VideoStreamsFull,
    HistoryListResponse,
    HistoryCountResponse,
)
```

Methods:

- <code title="get /udl/video/history">client.video.history.<a href="./src/unifieddatalibrary/resources/video/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/video/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/video/history_list_response.py">HistoryListResponse</a></code>
- <code title="get /udl/video/history/count">client.video.history.<a href="./src/unifieddatalibrary/resources/video/history.py">count</a>() -> str</code>

# Weatherdata

Types:

```python
from unifieddatalibrary.types import (
    WeatherdataListResponse,
    WeatherdataCountResponse,
    WeatherdataTupleResponse,
)
```

Methods:

- <code title="post /udl/weatherdata">client.weatherdata.<a href="./src/unifieddatalibrary/resources/weatherdata/weatherdata.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/weatherdata_create_params.py">params</a>) -> None</code>
- <code title="get /udl/weatherdata">client.weatherdata.<a href="./src/unifieddatalibrary/resources/weatherdata/weatherdata.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/weatherdata_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/weatherdata_list_response.py">WeatherdataListResponse</a></code>
- <code title="get /udl/weatherdata/count">client.weatherdata.<a href="./src/unifieddatalibrary/resources/weatherdata/weatherdata.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/weatherdata_count_params.py">params</a>) -> str</code>
- <code title="post /udl/weatherdata/createBulk">client.weatherdata.<a href="./src/unifieddatalibrary/resources/weatherdata/weatherdata.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/weatherdata_create_bulk_params.py">params</a>) -> None</code>
- <code title="post /filedrop/udl-weatherdata">client.weatherdata.<a href="./src/unifieddatalibrary/resources/weatherdata/weatherdata.py">create_bulk_v2</a>(\*\*<a href="src/unifieddatalibrary/types/weatherdata_create_bulk_v2_params.py">params</a>) -> None</code>
- <code title="get /udl/weatherdata/{id}">client.weatherdata.<a href="./src/unifieddatalibrary/resources/weatherdata/weatherdata.py">get</a>(id) -> <a href="./src/unifieddatalibrary/types/weatherdata/weather_data_full.py">WeatherDataFull</a></code>
- <code title="get /udl/weatherdata/queryhelp">client.weatherdata.<a href="./src/unifieddatalibrary/resources/weatherdata/weatherdata.py">queryhelp</a>() -> None</code>
- <code title="get /udl/weatherdata/tuple">client.weatherdata.<a href="./src/unifieddatalibrary/resources/weatherdata/weatherdata.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/weatherdata_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/weatherdata_tuple_response.py">WeatherdataTupleResponse</a></code>

## History

Types:

```python
from unifieddatalibrary.types.weatherdata import (
    WeatherDataFull,
    HistoryListResponse,
    HistoryCountResponse,
)
```

Methods:

- <code title="get /udl/weatherdata/history">client.weatherdata.history.<a href="./src/unifieddatalibrary/resources/weatherdata/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/weatherdata/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/weatherdata/history_list_response.py">HistoryListResponse</a></code>
- <code title="get /udl/weatherdata/history/aodr">client.weatherdata.history.<a href="./src/unifieddatalibrary/resources/weatherdata/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/weatherdata/history_aodr_params.py">params</a>) -> None</code>
- <code title="get /udl/weatherdata/history/count">client.weatherdata.history.<a href="./src/unifieddatalibrary/resources/weatherdata/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/weatherdata/history_count_params.py">params</a>) -> str</code>

# Weatherreport

Types:

```python
from unifieddatalibrary.types import (
    WeatherreportListResponse,
    WeatherreportCountResponse,
    WeatherreportTupleResponse,
)
```

Methods:

- <code title="post /udl/weatherreport">client.weatherreport.<a href="./src/unifieddatalibrary/resources/weatherreport/weatherreport.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/weatherreport_create_params.py">params</a>) -> None</code>
- <code title="get /udl/weatherreport">client.weatherreport.<a href="./src/unifieddatalibrary/resources/weatherreport/weatherreport.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/weatherreport_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/weatherreport_list_response.py">WeatherreportListResponse</a></code>
- <code title="get /udl/weatherreport/count">client.weatherreport.<a href="./src/unifieddatalibrary/resources/weatherreport/weatherreport.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/weatherreport_count_params.py">params</a>) -> str</code>
- <code title="post /filedrop/udl-weatherreport">client.weatherreport.<a href="./src/unifieddatalibrary/resources/weatherreport/weatherreport.py">create_bulk_v2</a>(\*\*<a href="src/unifieddatalibrary/types/weatherreport_create_bulk_v2_params.py">params</a>) -> None</code>
- <code title="get /udl/weatherreport/{id}">client.weatherreport.<a href="./src/unifieddatalibrary/resources/weatherreport/weatherreport.py">get</a>(id) -> <a href="./src/unifieddatalibrary/types/weatherreport/weather_report_full.py">WeatherReportFull</a></code>
- <code title="get /udl/weatherreport/queryhelp">client.weatherreport.<a href="./src/unifieddatalibrary/resources/weatherreport/weatherreport.py">queryhelp</a>() -> None</code>
- <code title="get /udl/weatherreport/tuple">client.weatherreport.<a href="./src/unifieddatalibrary/resources/weatherreport/weatherreport.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/weatherreport_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/weatherreport_tuple_response.py">WeatherreportTupleResponse</a></code>

## History

Types:

```python
from unifieddatalibrary.types.weatherreport import (
    WeatherReportFull,
    HistoryListResponse,
    HistoryCountResponse,
)
```

Methods:

- <code title="get /udl/weatherreport/history">client.weatherreport.history.<a href="./src/unifieddatalibrary/resources/weatherreport/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/weatherreport/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/weatherreport/history_list_response.py">HistoryListResponse</a></code>
- <code title="get /udl/weatherreport/history/aodr">client.weatherreport.history.<a href="./src/unifieddatalibrary/resources/weatherreport/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/weatherreport/history_aodr_params.py">params</a>) -> None</code>
- <code title="get /udl/weatherreport/history/count">client.weatherreport.history.<a href="./src/unifieddatalibrary/resources/weatherreport/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/weatherreport/history_count_params.py">params</a>) -> str</code>

# Udl

## Geostatus

### History

Types:

```python
from unifieddatalibrary.types.udl.geostatus import (
    GeoStatusFull,
    HistoryListResponse,
    HistoryCountResponse,
)
```

Methods:

- <code title="get /udl/geostatus/history">client.udl.geostatus.history.<a href="./src/unifieddatalibrary/resources/udl/geostatus/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/udl/geostatus/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/udl/geostatus/history_list_response.py">HistoryListResponse</a></code>
- <code title="get /udl/geostatus/history/aodr">client.udl.geostatus.history.<a href="./src/unifieddatalibrary/resources/udl/geostatus/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/udl/geostatus/history_aodr_params.py">params</a>) -> None</code>
- <code title="get /udl/geostatus/history/count">client.udl.geostatus.history.<a href="./src/unifieddatalibrary/resources/udl/geostatus/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/udl/geostatus/history_count_params.py">params</a>) -> str</code>

## Gnssobservationset

### History

Types:

```python
from unifieddatalibrary.types.udl.gnssobservationset import (
    GnssObservationSetFull,
    HistoryListResponse,
)
```

Methods:

- <code title="get /udl/gnssobservationset/history">client.udl.gnssobservationset.history.<a href="./src/unifieddatalibrary/resources/udl/gnssobservationset/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/udl/gnssobservationset/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/udl/gnssobservationset/history_list_response.py">HistoryListResponse</a></code>
- <code title="get /udl/gnssobservationset/history/aodr">client.udl.gnssobservationset.history.<a href="./src/unifieddatalibrary/resources/udl/gnssobservationset/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/udl/gnssobservationset/history_aodr_params.py">params</a>) -> None</code>

## Mti

### History

Types:

```python
from unifieddatalibrary.types.udl.mti import MtiFull, HistoryListResponse, HistoryCountResponse
```

Methods:

- <code title="get /udl/mti/history">client.udl.mti.history.<a href="./src/unifieddatalibrary/resources/udl/mti/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/udl/mti/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/udl/mti/history_list_response.py">HistoryListResponse</a></code>
- <code title="get /udl/mti/history/aodr">client.udl.mti.history.<a href="./src/unifieddatalibrary/resources/udl/mti/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/udl/mti/history_aodr_params.py">params</a>) -> None</code>
- <code title="get /udl/mti/history/count">client.udl.mti.history.<a href="./src/unifieddatalibrary/resources/udl/mti/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/udl/mti/history_count_params.py">params</a>) -> str</code>

## Notification

### History

Types:

```python
from unifieddatalibrary.types.udl.notification import (
    NotificationFull,
    HistoryListResponse,
    HistoryCountResponse,
)
```

Methods:

- <code title="get /udl/notification/history">client.udl.notification.history.<a href="./src/unifieddatalibrary/resources/udl/notification/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/udl/notification/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/udl/notification/history_list_response.py">HistoryListResponse</a></code>
- <code title="get /udl/notification/history/aodr">client.udl.notification.history.<a href="./src/unifieddatalibrary/resources/udl/notification/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/udl/notification/history_aodr_params.py">params</a>) -> None</code>
- <code title="get /udl/notification/history/count">client.udl.notification.history.<a href="./src/unifieddatalibrary/resources/udl/notification/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/udl/notification/history_count_params.py">params</a>) -> str</code>

## Onboardnavigation

### History

Types:

```python
from unifieddatalibrary.types.udl.onboardnavigation import (
    OnboardnavigationFull,
    HistoryListResponse,
    HistoryCountResponse,
)
```

Methods:

- <code title="get /udl/onboardnavigation/history">client.udl.onboardnavigation.history.<a href="./src/unifieddatalibrary/resources/udl/onboardnavigation/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/udl/onboardnavigation/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/udl/onboardnavigation/history_list_response.py">HistoryListResponse</a></code>
- <code title="get /udl/onboardnavigation/history/aodr">client.udl.onboardnavigation.history.<a href="./src/unifieddatalibrary/resources/udl/onboardnavigation/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/udl/onboardnavigation/history_aodr_params.py">params</a>) -> None</code>
- <code title="get /udl/onboardnavigation/history/count">client.udl.onboardnavigation.history.<a href="./src/unifieddatalibrary/resources/udl/onboardnavigation/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/udl/onboardnavigation/history_count_params.py">params</a>) -> str</code>

## Onorbitthrusterstatus

### History

Types:

```python
from unifieddatalibrary.types.udl.onorbitthrusterstatus import (
    OnorbitthrusterstatusFull,
    HistoryListResponse,
)
```

Methods:

- <code title="get /udl/onorbitthrusterstatus/history">client.udl.onorbitthrusterstatus.history.<a href="./src/unifieddatalibrary/resources/udl/onorbitthrusterstatus/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/udl/onorbitthrusterstatus/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/udl/onorbitthrusterstatus/history_list_response.py">HistoryListResponse</a></code>

## Gnssrawif

### History

Types:

```python
from unifieddatalibrary.types.udl.gnssrawif import GnssRawIfFull
```

## Groundimagery

### History

Types:

```python
from unifieddatalibrary.types.udl.groundimagery import GroundImageryFull
```

## Hazard

### History

Types:

```python
from unifieddatalibrary.types.udl.hazard import HazardFull
```

## Ionoobservation

### History

Types:

```python
from unifieddatalibrary.types.udl.ionoobservation import IonoObservationFull
```

## Isrcollection

### History

Types:

```python
from unifieddatalibrary.types.udl.isrcollection import IsrCollectionFull
```

## Itemtracking

### History

Types:

```python
from unifieddatalibrary.types.udl.itemtracking import ItemTrackingFull
```

## Linkstatus

### History

Types:

```python
from unifieddatalibrary.types.udl.linkstatus import LinkStatusFull
```

## Maneuver

### History

Types:

```python
from unifieddatalibrary.types.udl.maneuver import ManeuverFull
```

## Missiletrack

### History

Types:

```python
from unifieddatalibrary.types.udl.missiletrack import MissileTrackFull
```

## Missionassignment

### History

Types:

```python
from unifieddatalibrary.types.udl.missionassignment import MissionAssignmentFull
```

## Monoradar

### History

Types:

```python
from unifieddatalibrary.types.udl.monoradar import MonoRadarFull
```

## Orbitdetermination

### History

Types:

```python
from unifieddatalibrary.types.udl.orbitdetermination import OrbitdeterminationFull
```

## Orbittrack

### History

Types:

```python
from unifieddatalibrary.types.udl.orbittrack import OrbittrackFull
```

## Passiveradarobservation

### History

Types:

```python
from unifieddatalibrary.types.udl.passiveradarobservation import PassiveradarobservationFull
```

## Poi

### History

Types:

```python
from unifieddatalibrary.types.udl.poi import PoiFull
```

## Radarobservation

### History

Types:

```python
from unifieddatalibrary.types.udl.radarobservation import RadarobservationFull
```

## Rfobservation

### History

Types:

```python
from unifieddatalibrary.types.udl.rfobservation import RfobservationdetailsFull
```

## Sarobservation

### History

Types:

```python
from unifieddatalibrary.types.udl.sarobservation import SarobservationFull
```

## Sensormaintenance

### History

Types:

```python
from unifieddatalibrary.types.udl.sensormaintenance import SensormaintenanceFull
```

## Sensorplan

### History

Types:

```python
from unifieddatalibrary.types.udl.sensorplan import SensorplanFull
```

## Sgi

### History

Types:

```python
from unifieddatalibrary.types.udl.sgi import SgiFull
```

## Sigact

### History

Types:

```python
from unifieddatalibrary.types.udl.sigact import SigactFull
```

## Sitestatus

### History

Types:

```python
from unifieddatalibrary.types.udl.sitestatus import SitestatusFull
```

## Skyimagery

### History

Types:

```python
from unifieddatalibrary.types.udl.skyimagery import SkyimageryFull
```

# GnssObservations

## History

Types:

```python
from unifieddatalibrary.types.gnss_observations import HistoryCountResponse
```

Methods:

- <code title="get /udl/gnssobservationset/history/count">client.gnss_observations.history.<a href="./src/unifieddatalibrary/resources/gnss_observations/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/gnss_observations/history_count_params.py">params</a>) -> str</code>

# GnssRawIf

## History

Types:

```python
from unifieddatalibrary.types.gnss_raw_if import HistoryCountResponse, HistoryQueryResponse
```

Methods:

- <code title="get /udl/gnssrawif/history/aodr">client.gnss_raw_if.history.<a href="./src/unifieddatalibrary/resources/gnss_raw_if/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/gnss_raw_if/history_aodr_params.py">params</a>) -> None</code>
- <code title="get /udl/gnssrawif/history/count">client.gnss_raw_if.history.<a href="./src/unifieddatalibrary/resources/gnss_raw_if/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/gnss_raw_if/history_count_params.py">params</a>) -> str</code>
- <code title="get /udl/gnssrawif/history">client.gnss_raw_if.history.<a href="./src/unifieddatalibrary/resources/gnss_raw_if/history.py">query</a>(\*\*<a href="src/unifieddatalibrary/types/gnss_raw_if/history_query_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/gnss_raw_if/history_query_response.py">HistoryQueryResponse</a></code>

# IonoObservation

## History

Types:

```python
from unifieddatalibrary.types.iono_observation import HistoryListResponse, HistoryCountResponse
```

Methods:

- <code title="get /udl/ionoobservation/history">client.iono_observation.history.<a href="./src/unifieddatalibrary/resources/iono_observation/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/iono_observation/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/iono_observation/history_list_response.py">HistoryListResponse</a></code>
- <code title="get /udl/ionoobservation/history/aodr">client.iono_observation.history.<a href="./src/unifieddatalibrary/resources/iono_observation/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/iono_observation/history_aodr_params.py">params</a>) -> None</code>
- <code title="get /udl/ionoobservation/history/count">client.iono_observation.history.<a href="./src/unifieddatalibrary/resources/iono_observation/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/iono_observation/history_count_params.py">params</a>) -> str</code>

# LaunchEvent

Methods:

- <code title="post /filedrop/udl-launchevent">client.launch_event.<a href="./src/unifieddatalibrary/resources/launch_event/launch_event.py">create_bulk_v2</a>(\*\*<a href="src/unifieddatalibrary/types/launch_event_create_bulk_v2_params.py">params</a>) -> None</code>

## History

Types:

```python
from unifieddatalibrary.types.launch_event import HistoryListResponse, HistoryCountResponse
```

Methods:

- <code title="get /udl/launchevent/history">client.launch_event.history.<a href="./src/unifieddatalibrary/resources/launch_event/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/launch_event/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/launch_event/history_list_response.py">HistoryListResponse</a></code>
- <code title="get /udl/launchevent/history/aodr">client.launch_event.history.<a href="./src/unifieddatalibrary/resources/launch_event/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/launch_event/history_aodr_params.py">params</a>) -> None</code>
- <code title="get /udl/launchevent/history/count">client.launch_event.history.<a href="./src/unifieddatalibrary/resources/launch_event/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/launch_event/history_count_params.py">params</a>) -> str</code>

# ReportAndActivity

## Poi

### History

Types:

```python
from unifieddatalibrary.types.report_and_activity.poi import (
    HistoryListResponse,
    HistoryCountResponse,
)
```

Methods:

- <code title="get /udl/poi/history">client.report_and_activity.poi.history.<a href="./src/unifieddatalibrary/resources/report_and_activity/poi/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/report_and_activity/poi/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/report_and_activity/poi/history_list_response.py">HistoryListResponse</a></code>
- <code title="get /udl/poi/history/aodr">client.report_and_activity.poi.history.<a href="./src/unifieddatalibrary/resources/report_and_activity/poi/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/report_and_activity/poi/history_aodr_params.py">params</a>) -> None</code>
- <code title="get /udl/poi/history/count">client.report_and_activity.poi.history.<a href="./src/unifieddatalibrary/resources/report_and_activity/poi/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/report_and_activity/poi/history_count_params.py">params</a>) -> str</code>

## UdlH3geo

Methods:

- <code title="post /filedrop/udl-h3geo">client.report_and_activity.udl_h3geo.<a href="./src/unifieddatalibrary/resources/report_and_activity/udl_h3geo.py">create_bulk_v2</a>(\*\*<a href="src/unifieddatalibrary/types/report_and_activity/udl_h3geo_create_bulk_v2_params.py">params</a>) -> None</code>

## UdlSigact

Methods:

- <code title="post /filedrop/udl-sigact">client.report_and_activity.udl_sigact.<a href="./src/unifieddatalibrary/resources/report_and_activity/udl_sigact.py">create_bulk_v2</a>(\*\*<a href="src/unifieddatalibrary/types/report_and_activity/udl_sigact_create_bulk_v2_params.py">params</a>) -> None</code>
- <code title="get /udl/sigact/getFile/{id}">client.report_and_activity.udl_sigact.<a href="./src/unifieddatalibrary/resources/report_and_activity/udl_sigact.py">file_get</a>(id) -> BinaryAPIResponse</code>

# SecureMessaging

Types:

```python
from unifieddatalibrary.types import TopicDetails, SecureMessagingListTopicsResponse
```

Methods:

- <code title="get /sm/describeTopic/{topic}">client.secure_messaging.<a href="./src/unifieddatalibrary/resources/secure_messaging.py">describe_topic</a>(topic) -> <a href="./src/unifieddatalibrary/types/topic_details.py">TopicDetails</a></code>
- <code title="get /sm/getLatestOffset/{topic}">client.secure_messaging.<a href="./src/unifieddatalibrary/resources/secure_messaging.py">get_latest_offset</a>(topic) -> None</code>
- <code title="get /sm/getMessages/{topic}/{offset}">client.secure_messaging.<a href="./src/unifieddatalibrary/resources/secure_messaging.py">get_messages</a>(offset, \*, topic) -> None</code>
- <code title="get /sm/listTopics">client.secure_messaging.<a href="./src/unifieddatalibrary/resources/secure_messaging.py">list_topics</a>() -> <a href="./src/unifieddatalibrary/types/secure_messaging_list_topics_response.py">SecureMessagingListTopicsResponse</a></code>

# Scs

Types:

```python
from unifieddatalibrary.types import (
    ScAggregateDocTypeResponse,
    ScAllowableFileExtensionsResponse,
    ScAllowableFileMimesResponse,
    ScCopyResponse,
    ScFileUploadResponse,
    ScMoveResponse,
    ScSearchResponse,
)
```

Methods:

- <code title="delete /scs/delete">client.scs.<a href="./src/unifieddatalibrary/resources/scs/scs.py">delete</a>(\*\*<a href="src/unifieddatalibrary/types/sc_delete_params.py">params</a>) -> None</code>
- <code title="get /scs/aggregateDocType">client.scs.<a href="./src/unifieddatalibrary/resources/scs/scs.py">aggregate_doc_type</a>() -> <a href="./src/unifieddatalibrary/types/sc_aggregate_doc_type_response.py">ScAggregateDocTypeResponse</a></code>
- <code title="get /scs/allowableFileExtensions">client.scs.<a href="./src/unifieddatalibrary/resources/scs/scs.py">allowable_file_extensions</a>() -> <a href="./src/unifieddatalibrary/types/sc_allowable_file_extensions_response.py">ScAllowableFileExtensionsResponse</a></code>
- <code title="get /scs/allowableFileMimes">client.scs.<a href="./src/unifieddatalibrary/resources/scs/scs.py">allowable_file_mimes</a>() -> <a href="./src/unifieddatalibrary/types/sc_allowable_file_mimes_response.py">ScAllowableFileMimesResponse</a></code>
- <code title="post /scs/copy">client.scs.<a href="./src/unifieddatalibrary/resources/scs/scs.py">copy</a>(\*\*<a href="src/unifieddatalibrary/types/sc_copy_params.py">params</a>) -> str</code>
- <code title="post /scs/download">client.scs.<a href="./src/unifieddatalibrary/resources/scs/scs.py">download</a>(\*\*<a href="src/unifieddatalibrary/types/sc_download_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="get /scs/download">client.scs.<a href="./src/unifieddatalibrary/resources/scs/scs.py">file_download</a>(\*\*<a href="src/unifieddatalibrary/types/sc_file_download_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="post /scs/file">client.scs.<a href="./src/unifieddatalibrary/resources/scs/scs.py">file_upload</a>(\*\*<a href="src/unifieddatalibrary/types/sc_file_upload_params.py">params</a>) -> str</code>
- <code title="put /scs/move">client.scs.<a href="./src/unifieddatalibrary/resources/scs/scs.py">move</a>(\*\*<a href="src/unifieddatalibrary/types/sc_move_params.py">params</a>) -> str</code>
- <code title="put /scs/rename">client.scs.<a href="./src/unifieddatalibrary/resources/scs/scs.py">rename</a>(\*\*<a href="src/unifieddatalibrary/types/sc_rename_params.py">params</a>) -> None</code>
- <code title="post /scs/search">client.scs.<a href="./src/unifieddatalibrary/resources/scs/scs.py">search</a>(\*\*<a href="src/unifieddatalibrary/types/sc_search_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/sc_search_response.py">ScSearchResponse</a></code>
- <code title="put /scs/updateTagsForFilesInFolder">client.scs.<a href="./src/unifieddatalibrary/resources/scs/scs.py">update_tags</a>(\*\*<a href="src/unifieddatalibrary/types/sc_update_tags_params.py">params</a>) -> None</code>

## Folders

Types:

```python
from unifieddatalibrary.types.scs import FolderCreateResponse
```

Methods:

- <code title="post /scs/folder">client.scs.folders.<a href="./src/unifieddatalibrary/resources/scs/folders.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/scs/folder_create_params.py">params</a>) -> str</code>
- <code title="get /scs/folder">client.scs.folders.<a href="./src/unifieddatalibrary/resources/scs/folders.py">retrieve</a>(\*\*<a href="src/unifieddatalibrary/types/scs/folder_retrieve_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/shared/file_data.py">FileData</a></code>
- <code title="patch /scs/folder">client.scs.folders.<a href="./src/unifieddatalibrary/resources/scs/folders.py">update</a>(\*\*<a href="src/unifieddatalibrary/types/scs/folder_update_params.py">params</a>) -> None</code>

## ClassificationMarkings

Types:

```python
from unifieddatalibrary.types.scs import ClassificationMarkingListResponse
```

Methods:

- <code title="get /scs/getClassificationMarkings">client.scs.classification_markings.<a href="./src/unifieddatalibrary/resources/scs/classification_markings.py">list</a>() -> <a href="./src/unifieddatalibrary/types/scs/classification_marking_list_response.py">ClassificationMarkingListResponse</a></code>

## Groups

Types:

```python
from unifieddatalibrary.types.scs import GroupListResponse
```

Methods:

- <code title="get /scs/groups">client.scs.groups.<a href="./src/unifieddatalibrary/resources/scs/groups.py">list</a>() -> <a href="./src/unifieddatalibrary/types/scs/group_list_response.py">GroupListResponse</a></code>

## FileMetadata

Types:

```python
from unifieddatalibrary.types.scs import FileMetadataListResponse
```

Methods:

- <code title="get /scs/listFileMetadata">client.scs.file_metadata.<a href="./src/unifieddatalibrary/resources/scs/file_metadata.py">list</a>() -> <a href="./src/unifieddatalibrary/types/scs/file_metadata_list_response.py">FileMetadataListResponse</a></code>

## RangeParameters

Types:

```python
from unifieddatalibrary.types.scs import RangeParameterListResponse
```

Methods:

- <code title="get /scs/listRangeParameters">client.scs.range_parameters.<a href="./src/unifieddatalibrary/resources/scs/range_parameters.py">list</a>() -> <a href="./src/unifieddatalibrary/types/scs/range_parameter_list_response.py">RangeParameterListResponse</a></code>

## Paths

Types:

```python
from unifieddatalibrary.types.scs import PathCreateResponse
```

Methods:

- <code title="post /scs/path">client.scs.paths.<a href="./src/unifieddatalibrary/resources/scs/paths.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/scs/path_create_params.py">params</a>) -> str</code>

## V2

Types:

```python
from unifieddatalibrary.types.scs import Attachment, ScsEntity, V2ListResponse
```

Methods:

- <code title="patch /scs/v2/update">client.scs.v2.<a href="./src/unifieddatalibrary/resources/scs/v2.py">update</a>(\*\*<a href="src/unifieddatalibrary/types/scs/v2_update_params.py">params</a>) -> None</code>
- <code title="get /scs/v2/list">client.scs.v2.<a href="./src/unifieddatalibrary/resources/scs/v2.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/scs/v2_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/scs/v2_list_response.py">V2ListResponse</a></code>
- <code title="delete /scs/v2/delete">client.scs.v2.<a href="./src/unifieddatalibrary/resources/scs/v2.py">delete</a>(\*\*<a href="src/unifieddatalibrary/types/scs/v2_delete_params.py">params</a>) -> None</code>
- <code title="post /scs/v2/copy">client.scs.v2.<a href="./src/unifieddatalibrary/resources/scs/v2.py">copy</a>(\*\*<a href="src/unifieddatalibrary/types/scs/v2_copy_params.py">params</a>) -> None</code>
- <code title="post /scs/v2/file">client.scs.v2.<a href="./src/unifieddatalibrary/resources/scs/v2.py">file_upload</a>(\*\*<a href="src/unifieddatalibrary/types/scs/v2_file_upload_params.py">params</a>) -> None</code>
- <code title="post /scs/v2/folder">client.scs.v2.<a href="./src/unifieddatalibrary/resources/scs/v2.py">folder_create</a>(\*\*<a href="src/unifieddatalibrary/types/scs/v2_folder_create_params.py">params</a>) -> None</code>
- <code title="put /scs/v2/move">client.scs.v2.<a href="./src/unifieddatalibrary/resources/scs/v2.py">move</a>(\*\*<a href="src/unifieddatalibrary/types/scs/v2_move_params.py">params</a>) -> None</code>

## File

Methods:

- <code title="get /scs/file">client.scs.file.<a href="./src/unifieddatalibrary/resources/scs/file.py">retrieve</a>(\*\*<a href="src/unifieddatalibrary/types/scs/file_retrieve_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/shared/file_data.py">FileData</a></code>
- <code title="patch /scs/file">client.scs.file.<a href="./src/unifieddatalibrary/resources/scs/file.py">update</a>(\*\*<a href="src/unifieddatalibrary/types/scs/file_update_params.py">params</a>) -> None</code>
- <code title="get /scs/list">client.scs.file.<a href="./src/unifieddatalibrary/resources/scs/file.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/scs/file_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/shared/file_data.py">SyncOffsetPage[FileData]</a></code>

# ScsViews

Methods:

- <code title="get /scs/view/{id}">client.scs_views.<a href="./src/unifieddatalibrary/resources/scs_views.py">retrieve</a>(id) -> BinaryAPIResponse</code>
