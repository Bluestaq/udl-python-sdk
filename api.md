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
    FlightPlanFull,
)
```

# Conjunctions

Types:

```python
from unifieddatalibrary.types import (
    ConjunctionAbridged,
    ConjunctionFull,
    Onorbit,
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
- <code title="post /filedrop/udl-conjunction">client.conjunctions.<a href="./src/unifieddatalibrary/resources/conjunctions/conjunctions.py">create_filedrop</a>(\*\*<a href="src/unifieddatalibrary/types/conjunction_create_filedrop_params.py">params</a>) -> None</code>
- <code title="post /udl/conjunction">client.conjunctions.<a href="./src/unifieddatalibrary/resources/conjunctions/conjunctions.py">create_udl</a>(\*\*<a href="src/unifieddatalibrary/types/conjunction_create_udl_params.py">params</a>) -> None</code>
- <code title="post /udl/conjunction/createBulk">client.conjunctions.<a href="./src/unifieddatalibrary/resources/conjunctions/conjunctions.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/conjunction_create_bulk_params.py">params</a>) -> None</code>
- <code title="get /udl/conjunction/history">client.conjunctions.<a href="./src/unifieddatalibrary/resources/conjunctions/conjunctions.py">get_history</a>(\*\*<a href="src/unifieddatalibrary/types/conjunction_get_history_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/conjunction_get_history_response.py">ConjunctionGetHistoryResponse</a></code>
- <code title="get /udl/conjunction/queryhelp">client.conjunctions.<a href="./src/unifieddatalibrary/resources/conjunctions/conjunctions.py">queryhelp</a>() -> None</code>
- <code title="get /udl/conjunction/tuple">client.conjunctions.<a href="./src/unifieddatalibrary/resources/conjunctions/conjunctions.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/conjunction_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/conjunction_tuple_response.py">ConjunctionTupleResponse</a></code>

## History

Types:

```python
from unifieddatalibrary.types.conjunctions import HistoryCountResponse
```

Methods:

- <code title="get /udl/conjunction/history/aodr">client.conjunctions.history.<a href="./src/unifieddatalibrary/resources/conjunctions/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/conjunctions/history_aodr_params.py">params</a>) -> None</code>
- <code title="get /udl/conjunction/history/count">client.conjunctions.history.<a href="./src/unifieddatalibrary/resources/conjunctions/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/conjunctions/history_count_params.py">params</a>) -> str</code>

# AirOperations

## Crewpapers

Methods:

- <code title="post /filedrop/crewpapers">client.air_operations.crewpapers.<a href="./src/unifieddatalibrary/resources/air_operations/crewpapers.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/air_operations/crewpaper_create_params.py">params</a>) -> None</code>
- <code title="post /udl/crewpapers/unpublish">client.air_operations.crewpapers.<a href="./src/unifieddatalibrary/resources/air_operations/crewpapers.py">unpublish</a>(\*\*<a href="src/unifieddatalibrary/types/air_operations/crewpaper_unpublish_params.py">params</a>) -> None</code>

## AircraftSorties

Methods:

- <code title="post /filedrop/udl-aircraftsortie">client.air_operations.aircraft_sorties.<a href="./src/unifieddatalibrary/resources/air_operations/aircraft_sorties.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/air_operations/aircraft_sorty_create_params.py">params</a>) -> None</code>

## AirEvents

Methods:

- <code title="post /filedrop/udl-airevent">client.air_operations.air_events.<a href="./src/unifieddatalibrary/resources/air_operations/air_events.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/air_operations/air_event_create_params.py">params</a>) -> None</code>

## AirspaceControlOrders

Methods:

- <code title="post /filedrop/udl-airspacecontrolorder">client.air_operations.airspace_control_orders.<a href="./src/unifieddatalibrary/resources/air_operations/airspace_control_orders.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/air_operations/airspace_control_order_create_params.py">params</a>) -> None</code>

## AirTaskingOrders

Methods:

- <code title="post /filedrop/udl-airtaskingorder">client.air_operations.air_tasking_orders.<a href="./src/unifieddatalibrary/resources/air_operations/air_tasking_orders.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/air_operations/air_tasking_order_create_params.py">params</a>) -> None</code>

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

## DiplomaticClearance

Types:

```python
from unifieddatalibrary.types.air_operations import (
    DiplomaticclearanceAbridged,
    DiplomaticclearanceFull,
)
```

Methods:

- <code title="post /filedrop/udl-diplomaticclearance">client.air_operations.diplomatic_clearance.<a href="./src/unifieddatalibrary/resources/air_operations/diplomatic_clearance/diplomatic_clearance.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/air_operations/diplomatic_clearance_create_params.py">params</a>) -> None</code>

# Ephemerides

Methods:

- <code title="post /filedrop/ephem">client.ephemerides.<a href="./src/unifieddatalibrary/resources/ephemerides.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/ephemeride_create_params.py">params</a>) -> None</code>

# Observations

## Monoradar

Methods:

- <code title="post /filedrop/monoradar">client.observations.monoradar.<a href="./src/unifieddatalibrary/resources/observations/monoradar.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/observations/monoradar_create_params.py">params</a>) -> None</code>

## Swir

Methods:

- <code title="post /filedrop/swir">client.observations.swir.<a href="./src/unifieddatalibrary/resources/observations/swir.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/observations/swir_create_params.py">params</a>) -> None</code>

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

# AIsObjects

Methods:

- <code title="post /filedrop/udl-ais">client.ais_objects.<a href="./src/unifieddatalibrary/resources/ais_objects.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/ais_object_create_params.py">params</a>) -> None</code>

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

- <code title="post /filedrop/udl-analyticimagery">client.analytic_imagery.<a href="./src/unifieddatalibrary/resources/analytic_imagery.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/analytic_imagery_create_params.py">params</a>) -> None</code>
- <code title="get /udl/analyticimagery/{id}">client.analytic_imagery.<a href="./src/unifieddatalibrary/resources/analytic_imagery.py">retrieve</a>(id) -> <a href="./src/unifieddatalibrary/types/analytic_imagery_full.py">AnalyticImageryFull</a></code>
- <code title="get /udl/analyticimagery">client.analytic_imagery.<a href="./src/unifieddatalibrary/resources/analytic_imagery.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/analytic_imagery_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/analytic_imagery_list_response.py">AnalyticImageryListResponse</a></code>
- <code title="get /udl/analyticimagery/count">client.analytic_imagery.<a href="./src/unifieddatalibrary/resources/analytic_imagery.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/analytic_imagery_count_params.py">params</a>) -> str</code>
- <code title="get /udl/analyticimagery/history">client.analytic_imagery.<a href="./src/unifieddatalibrary/resources/analytic_imagery.py">history</a>(\*\*<a href="src/unifieddatalibrary/types/analytic_imagery_history_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/analytic_imagery_history_response.py">AnalyticImageryHistoryResponse</a></code>
- <code title="get /udl/analyticimagery/history/aodr">client.analytic_imagery.<a href="./src/unifieddatalibrary/resources/analytic_imagery.py">history_aodr</a>(\*\*<a href="src/unifieddatalibrary/types/analytic_imagery_history_aodr_params.py">params</a>) -> None</code>
- <code title="get /udl/analyticimagery/history/count">client.analytic_imagery.<a href="./src/unifieddatalibrary/resources/analytic_imagery.py">history_count</a>(\*\*<a href="src/unifieddatalibrary/types/analytic_imagery_history_count_params.py">params</a>) -> str</code>
- <code title="get /udl/analyticimagery/queryhelp">client.analytic_imagery.<a href="./src/unifieddatalibrary/resources/analytic_imagery.py">queryhelp</a>() -> None</code>
- <code title="get /udl/analyticimagery/tuple">client.analytic_imagery.<a href="./src/unifieddatalibrary/resources/analytic_imagery.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/analytic_imagery_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/analytic_imagery_tuple_response.py">AnalyticImageryTupleResponse</a></code>

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
- <code title="put /udl/crew/{id}">client.crew.<a href="./src/unifieddatalibrary/resources/crew.py">update</a>(id_1, \*\*<a href="src/unifieddatalibrary/types/crew_update_params.py">params</a>) -> None</code>
- <code title="get /udl/crew">client.crew.<a href="./src/unifieddatalibrary/resources/crew.py">list</a>() -> <a href="./src/unifieddatalibrary/types/crew_list_response.py">CrewListResponse</a></code>
- <code title="get /udl/crew/count">client.crew.<a href="./src/unifieddatalibrary/resources/crew.py">count</a>() -> str</code>
- <code title="get /udl/crew/queryhelp">client.crew.<a href="./src/unifieddatalibrary/resources/crew.py">queryhelp</a>() -> None</code>
- <code title="get /udl/crew/tuple">client.crew.<a href="./src/unifieddatalibrary/resources/crew.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/crew_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/crew_tuple_response.py">CrewTupleResponse</a></code>

# Diffofarrival

Types:

```python
from unifieddatalibrary.types import DiffofarrivalTupleResponse
```

Methods:

- <code title="post /filedrop/udl-diffofarrival">client.diffofarrival.<a href="./src/unifieddatalibrary/resources/diffofarrival/diffofarrival.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/diffofarrival_create_params.py">params</a>) -> None</code>
- <code title="get /udl/diffofarrival/{id}">client.diffofarrival.<a href="./src/unifieddatalibrary/resources/diffofarrival/diffofarrival.py">retrieve</a>(id) -> <a href="./src/unifieddatalibrary/types/tdoa_fdoa/diffofarrival_full.py">DiffofarrivalFull</a></code>
- <code title="get /udl/diffofarrival/queryhelp">client.diffofarrival.<a href="./src/unifieddatalibrary/resources/diffofarrival/diffofarrival.py">queryhelp</a>() -> None</code>
- <code title="get /udl/diffofarrival/tuple">client.diffofarrival.<a href="./src/unifieddatalibrary/resources/diffofarrival/diffofarrival.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/diffofarrival_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/diffofarrival_tuple_response.py">DiffofarrivalTupleResponse</a></code>

## History

Types:

```python
from unifieddatalibrary.types.diffofarrival import HistoryCountResponse
```

Methods:

- <code title="get /udl/diffofarrival/history/count">client.diffofarrival.history.<a href="./src/unifieddatalibrary/resources/diffofarrival/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/diffofarrival/history_count_params.py">params</a>) -> str</code>

# Ecpsdr

Methods:

- <code title="post /filedrop/udl-ecpsdr">client.ecpsdr.<a href="./src/unifieddatalibrary/resources/ecpsdr.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/ecpsdr_create_params.py">params</a>) -> None</code>

# Filedrop

## Effectrequests

Methods:

- <code title="post /filedrop/udl-effectrequest">client.filedrop.effectrequests.<a href="./src/unifieddatalibrary/resources/filedrop/effectrequests.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/filedrop/effectrequest_create_params.py">params</a>) -> None</code>

## Effectresponses

Methods:

- <code title="post /filedrop/udl-effectresponse">client.filedrop.effectresponses.<a href="./src/unifieddatalibrary/resources/filedrop/effectresponses.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/filedrop/effectresponse_create_params.py">params</a>) -> None</code>

## Elsets

Methods:

- <code title="post /filedrop/udl-elset">client.filedrop.elsets.<a href="./src/unifieddatalibrary/resources/filedrop/elsets.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/filedrop/elset_create_params.py">params</a>) -> None</code>

## Eo

Methods:

- <code title="post /filedrop/udl-eo">client.filedrop.eo.<a href="./src/unifieddatalibrary/resources/filedrop/eo.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/filedrop/eo_create_params.py">params</a>) -> None</code>

## Ephemeris

Methods:

- <code title="post /filedrop/udl-ephset">client.filedrop.ephemeris.<a href="./src/unifieddatalibrary/resources/filedrop/ephemeris.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/filedrop/ephemeris_create_params.py">params</a>) -> None</code>

## Evac

Methods:

- <code title="post /filedrop/udl-evac">client.filedrop.evac.<a href="./src/unifieddatalibrary/resources/filedrop/evac.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/filedrop/evac_create_params.py">params</a>) -> None</code>

## Eventevolutions

Methods:

- <code title="post /filedrop/udl-eventevolution">client.filedrop.eventevolutions.<a href="./src/unifieddatalibrary/resources/filedrop/eventevolutions.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/filedrop/eventevolution_create_params.py">params</a>) -> None</code>

## Flightplans

Methods:

- <code title="post /filedrop/udl-flightplan">client.filedrop.flightplans.<a href="./src/unifieddatalibrary/resources/filedrop/flightplans.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/filedrop/flightplan_create_params.py">params</a>) -> None</code>

## Gnssobservations

Methods:

- <code title="post /filedrop/udl-gnssobset">client.filedrop.gnssobservations.<a href="./src/unifieddatalibrary/resources/filedrop/gnssobservations.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/filedrop/gnssobservation_create_params.py">params</a>) -> None</code>

## Gnssrawif

Methods:

- <code title="post /filedrop/udl-gnssrawif">client.filedrop.gnssrawif.<a href="./src/unifieddatalibrary/resources/filedrop/gnssrawif.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/filedrop/gnssrawif_create_params.py">params</a>) -> None</code>

## Mti

Methods:

- <code title="post /filedrop/udl-mti">client.filedrop.mti.<a href="./src/unifieddatalibrary/resources/filedrop/mti.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/filedrop/mti_create_params.py">params</a>) -> None</code>

## Observation

### Onboardnavigation

Methods:

- <code title="post /filedrop/udl-onboardnavigation">client.filedrop.observation.onboardnavigation.<a href="./src/unifieddatalibrary/resources/filedrop/observation/onboardnavigation.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/filedrop/observation/onboardnavigation_create_params.py">params</a>) -> None</code>

### PassiveRadar

Methods:

- <code title="post /filedrop/udl-passiveradar">client.filedrop.observation.passive_radar.<a href="./src/unifieddatalibrary/resources/filedrop/observation/passive_radar.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/filedrop/observation/passive_radar_create_params.py">params</a>) -> None</code>

### Radar

Methods:

- <code title="post /filedrop/udl-radar">client.filedrop.observation.radar.<a href="./src/unifieddatalibrary/resources/filedrop/observation/radar.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/filedrop/observation/radar_create_params.py">params</a>) -> None</code>

### Rf

Methods:

- <code title="post /filedrop/udl-rf">client.filedrop.observation.rf.<a href="./src/unifieddatalibrary/resources/filedrop/observation/rf.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/filedrop/observation/rf_create_params.py">params</a>) -> None</code>

## OrbitDetermination

Methods:

- <code title="post /filedrop/udl-orbitdetermination">client.filedrop.orbit_determination.<a href="./src/unifieddatalibrary/resources/filedrop/orbit_determination.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/filedrop/orbit_determination_create_params.py">params</a>) -> None</code>

## OrbitTrack

Methods:

- <code title="post /filedrop/udl-orbittrack">client.filedrop.orbit_track.<a href="./src/unifieddatalibrary/resources/filedrop/orbit_track.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/filedrop/orbit_track_create_params.py">params</a>) -> None</code>

## MissionOps

### PersonnelRecovery

Methods:

- <code title="post /filedrop/udl-personnelrecovery">client.filedrop.mission_ops.personnel_recovery.<a href="./src/unifieddatalibrary/resources/filedrop/mission_ops/personnel_recovery.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/filedrop/mission_ops/personnel_recovery_create_params.py">params</a>) -> None</code>

## ReportAndActivity

### Poi

Methods:

- <code title="post /filedrop/udl-poi">client.filedrop.report_and_activity.poi.<a href="./src/unifieddatalibrary/resources/filedrop/report_and_activity/poi.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/filedrop/report_and_activity/poi_create_params.py">params</a>) -> None</code>

### RfGeolocation

Methods:

- <code title="post /filedrop/udl-rfgeolocation">client.filedrop.report_and_activity.rf_geolocation.<a href="./src/unifieddatalibrary/resources/filedrop/report_and_activity/rf_geolocation.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/filedrop/report_and_activity/rf_geolocation_create_params.py">params</a>) -> None</code>

## Surfaceobstructions

Methods:

- <code title="post /filedrop/udl-surfaceobstruction">client.filedrop.surfaceobstructions.<a href="./src/unifieddatalibrary/resources/filedrop/surfaceobstructions.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/filedrop/surfaceobstruction_create_params.py">params</a>) -> None</code>

## StateVectors

Methods:

- <code title="post /filedrop/udl-sv">client.filedrop.state_vectors.<a href="./src/unifieddatalibrary/resources/filedrop/state_vectors.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/filedrop/state_vector_create_params.py">params</a>) -> None</code>

## Trackroutes

Methods:

- <code title="post /filedrop/udl-trackroute">client.filedrop.trackroutes.<a href="./src/unifieddatalibrary/resources/filedrop/trackroutes.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/filedrop/trackroute_create_params.py">params</a>) -> None</code>

## Tracks

Methods:

- <code title="post /filedrop/udl-tracks">client.filedrop.tracks.<a href="./src/unifieddatalibrary/resources/filedrop/tracks.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/filedrop/track_create_params.py">params</a>) -> None</code>

## WeatherData

Methods:

- <code title="post /filedrop/udl-weatherdata">client.filedrop.weather_data.<a href="./src/unifieddatalibrary/resources/filedrop/weather_data.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/filedrop/weather_data_create_params.py">params</a>) -> None</code>

## WeatherReports

Methods:

- <code title="post /filedrop/udl-weatherreport">client.filedrop.weather_reports.<a href="./src/unifieddatalibrary/resources/filedrop/weather_reports.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/filedrop/weather_report_create_params.py">params</a>) -> None</code>

# GroundImagery

Methods:

- <code title="post /filedrop/udl-groundimagery">client.ground_imagery.<a href="./src/unifieddatalibrary/resources/ground_imagery.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/ground_imagery_create_params.py">params</a>) -> None</code>

# H3geo

Methods:

- <code title="post /filedrop/udl-h3geo">client.h3geo.<a href="./src/unifieddatalibrary/resources/h3geo.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/h3geo_create_params.py">params</a>) -> None</code>

# IonoObservations

Methods:

- <code title="post /filedrop/udl-ionoobs">client.iono_observations.<a href="./src/unifieddatalibrary/resources/iono_observations.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/iono_observation_create_params.py">params</a>) -> None</code>

# IsrCollections

Methods:

- <code title="post /filedrop/udl-isrcollection">client.isr_collections.<a href="./src/unifieddatalibrary/resources/isr_collections.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/isr_collection_create_params.py">params</a>) -> None</code>

# Items

Methods:

- <code title="post /filedrop/udl-item">client.items.<a href="./src/unifieddatalibrary/resources/items.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/item_create_params.py">params</a>) -> None</code>

# ItemTrackings

Methods:

- <code title="post /filedrop/udl-itemtracking">client.item_trackings.<a href="./src/unifieddatalibrary/resources/item_trackings.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/item_tracking_create_params.py">params</a>) -> None</code>

# LaunchEvents

Methods:

- <code title="post /filedrop/udl-launchevent">client.launch_events.<a href="./src/unifieddatalibrary/resources/launch_events.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/launch_event_create_params.py">params</a>) -> None</code>

# LogisticsSupports

Methods:

- <code title="post /filedrop/udl-logisticssupport">client.logistics_supports.<a href="./src/unifieddatalibrary/resources/logistics_supports.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/logistics_support_create_params.py">params</a>) -> None</code>

# Maneuvers

Methods:

- <code title="post /filedrop/udl-maneuver">client.maneuvers.<a href="./src/unifieddatalibrary/resources/maneuvers.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/maneuver_create_params.py">params</a>) -> None</code>

# MissileTracks

Methods:

- <code title="post /filedrop/udl-missiletrack">client.missile_tracks.<a href="./src/unifieddatalibrary/resources/missile_tracks.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/missile_track_create_params.py">params</a>) -> None</code>

# UdlSar

Methods:

- <code title="post /filedrop/udl-sar">client.udl_sar.<a href="./src/unifieddatalibrary/resources/udl_sar.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/udl_sar_create_params.py">params</a>) -> None</code>

# UdlSensorplan

Methods:

- <code title="post /filedrop/udl-sensorplan">client.udl_sensorplan.<a href="./src/unifieddatalibrary/resources/udl_sensorplan.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/udl_sensorplan_create_params.py">params</a>) -> None</code>

# UdlSgi

Methods:

- <code title="post /filedrop/udl-sgi">client.udl_sgi.<a href="./src/unifieddatalibrary/resources/udl_sgi.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/udl_sgi_create_params.py">params</a>) -> None</code>

# UdlSigact

Methods:

- <code title="post /filedrop/udl-sigact">client.udl_sigact.<a href="./src/unifieddatalibrary/resources/udl_sigact.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/udl_sigact_create_params.py">params</a>) -> None</code>

# UdlSigactText

Methods:

- <code title="post /filedrop/udl-sigact-text">client.udl_sigact_text.<a href="./src/unifieddatalibrary/resources/udl_sigact_text.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/udl_sigact_text_create_params.py">params</a>) -> None</code>

# UdlSkyimagery

Methods:

- <code title="post /filedrop/udl-skyimagery">client.udl_skyimagery.<a href="./src/unifieddatalibrary/resources/udl_skyimagery.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/udl_skyimagery_create_params.py">params</a>) -> None</code>

# UdlSoiobservationset

Methods:

- <code title="post /filedrop/udl-soiobservationset">client.udl_soiobservationset.<a href="./src/unifieddatalibrary/resources/udl_soiobservationset.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/udl_soiobservationset_create_params.py">params</a>) -> None</code>

# UdlSortieppr

Methods:

- <code title="post /filedrop/udl-sortieppr">client.udl_sortieppr.<a href="./src/unifieddatalibrary/resources/udl_sortieppr.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/udl_sortieppr_create_params.py">params</a>) -> None</code>

# UdlSpaceenvobs

Methods:

- <code title="post /filedrop/udl-spaceenvobs">client.udl_spaceenvobs.<a href="./src/unifieddatalibrary/resources/udl_spaceenvobs.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/udl_spaceenvob_create_params.py">params</a>) -> None</code>

# UdlStarcatalog

Methods:

- <code title="post /filedrop/udl-starcatalog">client.udl_starcatalog.<a href="./src/unifieddatalibrary/resources/udl_starcatalog.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/udl_starcatalog_create_params.py">params</a>) -> None</code>

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
- <code title="put /udl/aircraft/{id}">client.aircraft.<a href="./src/unifieddatalibrary/resources/aircraft.py">update</a>(id_1, \*\*<a href="src/unifieddatalibrary/types/aircraft_update_params.py">params</a>) -> None</code>
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
- <code title="put /udl/aircraftsortie/{id}">client.aircraft_sorties.<a href="./src/unifieddatalibrary/resources/aircraft_sorties.py">update</a>(id_1, \*\*<a href="src/unifieddatalibrary/types/aircraft_sorty_update_params.py">params</a>) -> None</code>
- <code title="get /udl/aircraftsortie/queryhelp">client.aircraft_sorties.<a href="./src/unifieddatalibrary/resources/aircraft_sorties.py">queryhelp</a>() -> None</code>
- <code title="get /udl/aircraftsortie/tuple">client.aircraft_sorties.<a href="./src/unifieddatalibrary/resources/aircraft_sorties.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/aircraft_sorty_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/aircraft_sorty_tuple_response.py">AircraftSortyTupleResponse</a></code>

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
- <code title="put /udl/aircraftstatus/{id}">client.aircraft_statuses.<a href="./src/unifieddatalibrary/resources/aircraft_statuses/aircraft_statuses.py">update</a>(id_1, \*\*<a href="src/unifieddatalibrary/types/aircraft_status_update_params.py">params</a>) -> None</code>
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

# AirEvents

Methods:

- <code title="delete /udl/airevent/{id}">client.air_events.<a href="./src/unifieddatalibrary/resources/air_events.py">delete</a>(id) -> None</code>

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
- <code title="put /udl/airfield/{id}">client.airfields.<a href="./src/unifieddatalibrary/resources/airfields.py">update</a>(id_1, \*\*<a href="src/unifieddatalibrary/types/airfield_update_params.py">params</a>) -> None</code>
- <code title="get /udl/airfield">client.airfields.<a href="./src/unifieddatalibrary/resources/airfields.py">list</a>() -> <a href="./src/unifieddatalibrary/types/airfield_list_response.py">AirfieldListResponse</a></code>
- <code title="get /udl/airfield/count">client.airfields.<a href="./src/unifieddatalibrary/resources/airfields.py">count</a>() -> str</code>
- <code title="get /udl/airfield/queryhelp">client.airfields.<a href="./src/unifieddatalibrary/resources/airfields.py">queryhelp</a>() -> None</code>
- <code title="get /udl/airfield/tuple">client.airfields.<a href="./src/unifieddatalibrary/resources/airfields.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/airfield_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/airfield_tuple_response.py">AirfieldTupleResponse</a></code>

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

# Airfieldslots

Types:

```python
from unifieddatalibrary.types import AirfieldslotCountResponse, AirfieldslotTupleResponse
```

Methods:

- <code title="get /udl/airfieldslot/{id}">client.airfieldslots.<a href="./src/unifieddatalibrary/resources/airfieldslots.py">retrieve</a>(id) -> <a href="./src/unifieddatalibrary/types/airfieldslot_full.py">AirfieldslotFull</a></code>
- <code title="put /udl/airfieldslot/{id}">client.airfieldslots.<a href="./src/unifieddatalibrary/resources/airfieldslots.py">update</a>(id_1, \*\*<a href="src/unifieddatalibrary/types/airfieldslot_update_params.py">params</a>) -> None</code>
- <code title="delete /udl/airfieldslot/{id}">client.airfieldslots.<a href="./src/unifieddatalibrary/resources/airfieldslots.py">delete</a>(id) -> None</code>
- <code title="get /udl/airfieldslot/count">client.airfieldslots.<a href="./src/unifieddatalibrary/resources/airfieldslots.py">count</a>() -> str</code>
- <code title="get /udl/airfieldslot/queryhelp">client.airfieldslots.<a href="./src/unifieddatalibrary/resources/airfieldslots.py">queryhelp</a>() -> None</code>
- <code title="get /udl/airfieldslot/tuple">client.airfieldslots.<a href="./src/unifieddatalibrary/resources/airfieldslots.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/airfieldslot_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/airfieldslot_tuple_response.py">AirfieldslotTupleResponse</a></code>

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
- <code title="put /udl/airfieldslotconsumption/{id}">client.airfieldslotconsumptions.<a href="./src/unifieddatalibrary/resources/airfieldslotconsumptions.py">update</a>(id_1, \*\*<a href="src/unifieddatalibrary/types/airfieldslotconsumption_update_params.py">params</a>) -> None</code>
- <code title="get /udl/airfieldslotconsumption">client.airfieldslotconsumptions.<a href="./src/unifieddatalibrary/resources/airfieldslotconsumptions.py">list</a>() -> <a href="./src/unifieddatalibrary/types/airfieldslotconsumption_list_response.py">AirfieldslotconsumptionListResponse</a></code>
- <code title="delete /udl/airfieldslotconsumption/{id}">client.airfieldslotconsumptions.<a href="./src/unifieddatalibrary/resources/airfieldslotconsumptions.py">delete</a>(id) -> None</code>
- <code title="get /udl/airfieldslotconsumption/count">client.airfieldslotconsumptions.<a href="./src/unifieddatalibrary/resources/airfieldslotconsumptions.py">count</a>() -> str</code>
- <code title="get /udl/airfieldslotconsumption/queryhelp">client.airfieldslotconsumptions.<a href="./src/unifieddatalibrary/resources/airfieldslotconsumptions.py">queryhelp</a>() -> None</code>
- <code title="get /udl/airfieldslotconsumption/tuple">client.airfieldslotconsumptions.<a href="./src/unifieddatalibrary/resources/airfieldslotconsumptions.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/airfieldslotconsumption_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/airfieldslotconsumption_tuple_response.py">AirfieldslotconsumptionTupleResponse</a></code>

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

# AirfieldStatus

Types:

```python
from unifieddatalibrary.types import AirfieldStatusTupleResponse
```

Methods:

- <code title="get /udl/airfieldstatus/{id}">client.airfield_status.<a href="./src/unifieddatalibrary/resources/airfield_status.py">retrieve</a>(id) -> <a href="./src/unifieddatalibrary/types/airfieldstatus_full.py">AirfieldstatusFull</a></code>
- <code title="put /udl/airfieldstatus/{id}">client.airfield_status.<a href="./src/unifieddatalibrary/resources/airfield_status.py">update</a>(id_1, \*\*<a href="src/unifieddatalibrary/types/airfield_status_update_params.py">params</a>) -> None</code>
- <code title="delete /udl/airfieldstatus/{id}">client.airfield_status.<a href="./src/unifieddatalibrary/resources/airfield_status.py">delete</a>(id) -> None</code>
- <code title="get /udl/airfieldstatus/tuple">client.airfield_status.<a href="./src/unifieddatalibrary/resources/airfield_status.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/airfield_status_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/airfield_status_tuple_response.py">AirfieldStatusTupleResponse</a></code>

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

# Airloadplans

Methods:

- <code title="put /udl/airloadplan/{id}">client.airloadplans.<a href="./src/unifieddatalibrary/resources/airloadplans.py">update</a>(id_1, \*\*<a href="src/unifieddatalibrary/types/airloadplan_update_params.py">params</a>) -> None</code>
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
- <code title="put /udl/airtransportmission/{id}">client.air_transport_missions.<a href="./src/unifieddatalibrary/resources/air_transport_missions/air_transport_missions.py">update</a>(id_1, \*\*<a href="src/unifieddatalibrary/types/air_transport_mission_update_params.py">params</a>) -> None</code>
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
- <code title="put /udl/antenna/{id}">client.antennas.<a href="./src/unifieddatalibrary/resources/antennas.py">update</a>(id_1, \*\*<a href="src/unifieddatalibrary/types/antenna_update_params.py">params</a>) -> None</code>
- <code title="get /udl/antenna">client.antennas.<a href="./src/unifieddatalibrary/resources/antennas.py">list</a>() -> <a href="./src/unifieddatalibrary/types/antenna_list_response.py">AntennaListResponse</a></code>
- <code title="delete /udl/antenna/{id}">client.antennas.<a href="./src/unifieddatalibrary/resources/antennas.py">delete</a>(id) -> None</code>
- <code title="get /udl/antenna/count">client.antennas.<a href="./src/unifieddatalibrary/resources/antennas.py">count</a>() -> str</code>
- <code title="get /udl/antenna/queryhelp">client.antennas.<a href="./src/unifieddatalibrary/resources/antennas.py">queryhelp</a>() -> None</code>
- <code title="get /udl/antenna/tuple">client.antennas.<a href="./src/unifieddatalibrary/resources/antennas.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/antenna_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/antenna_tuple_response.py">AntennaTupleResponse</a></code>

# Onorbit

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
- <code title="put /udl/antennadetails/{id}">client.onorbit.antenna_details.<a href="./src/unifieddatalibrary/resources/onorbit/antenna_details.py">update</a>(id_1, \*\*<a href="src/unifieddatalibrary/types/onorbit/antenna_detail_update_params.py">params</a>) -> None</code>
- <code title="get /udl/antennadetails">client.onorbit.antenna_details.<a href="./src/unifieddatalibrary/resources/onorbit/antenna_details.py">list</a>() -> <a href="./src/unifieddatalibrary/types/onorbit/antenna_detail_list_response.py">AntennaDetailListResponse</a></code>
- <code title="delete /udl/antennadetails/{id}">client.onorbit.antenna_details.<a href="./src/unifieddatalibrary/resources/onorbit/antenna_details.py">delete</a>(id) -> None</code>

# Ephemeris

Types:

```python
from unifieddatalibrary.types import (
    EphemerisAbridged,
    EphemerisListResponse,
    EphemerisCountResponse,
)
```

Methods:

- <code title="get /udl/ephemeris">client.ephemeris.<a href="./src/unifieddatalibrary/resources/ephemeris/ephemeris.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/ephemeris_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/ephemeris_list_response.py">EphemerisListResponse</a></code>
- <code title="get /udl/ephemeris/count">client.ephemeris.<a href="./src/unifieddatalibrary/resources/ephemeris/ephemeris.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/ephemeris_count_params.py">params</a>) -> str</code>
- <code title="get /udl/ephemeris/queryhelp">client.ephemeris.<a href="./src/unifieddatalibrary/resources/ephemeris/ephemeris.py">queryhelp</a>() -> None</code>

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
- <code title="post /filedrop/udl-attitudeset">client.attitude_sets.<a href="./src/unifieddatalibrary/resources/attitude_sets/attitude_sets.py">create_filedrop</a>(\*\*<a href="src/unifieddatalibrary/types/attitude_set_create_filedrop_params.py">params</a>) -> None</code>
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
- <code title="put /udl/battery/{id}">client.batteries.<a href="./src/unifieddatalibrary/resources/batteries.py">update</a>(id_1, \*\*<a href="src/unifieddatalibrary/types/battery_update_params.py">params</a>) -> None</code>
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
- <code title="put /udl/batterydetails/{id}">client.batterydetails.<a href="./src/unifieddatalibrary/resources/batterydetails.py">update</a>(id_1, \*\*<a href="src/unifieddatalibrary/types/batterydetail_update_params.py">params</a>) -> None</code>
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
- <code title="put /udl/beam/{id}">client.beam.<a href="./src/unifieddatalibrary/resources/beam.py">update</a>(id_1, \*\*<a href="src/unifieddatalibrary/types/beam_update_params.py">params</a>) -> None</code>
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
- <code title="put /udl/beamcontour/{id}">client.beam_contours.<a href="./src/unifieddatalibrary/resources/beam_contours.py">update</a>(id_1, \*\*<a href="src/unifieddatalibrary/types/beam_contour_update_params.py">params</a>) -> None</code>
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
- <code title="put /udl/bus/{id}">client.buses.<a href="./src/unifieddatalibrary/resources/buses.py">update</a>(id_1, \*\*<a href="src/unifieddatalibrary/types/bus_update_params.py">params</a>) -> None</code>
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
- <code title="put /udl/channel/{id}">client.channels.<a href="./src/unifieddatalibrary/resources/channels.py">update</a>(id_1, \*\*<a href="src/unifieddatalibrary/types/channel_update_params.py">params</a>) -> None</code>
- <code title="get /udl/channel">client.channels.<a href="./src/unifieddatalibrary/resources/channels.py">list</a>() -> <a href="./src/unifieddatalibrary/types/channel_list_response.py">ChannelListResponse</a></code>
- <code title="delete /udl/channel/{id}">client.channels.<a href="./src/unifieddatalibrary/resources/channels.py">delete</a>(id) -> None</code>
- <code title="get /udl/channel/count">client.channels.<a href="./src/unifieddatalibrary/resources/channels.py">count</a>() -> str</code>
- <code title="get /udl/channel/queryhelp">client.channels.<a href="./src/unifieddatalibrary/resources/channels.py">queryhelp</a>() -> None</code>
- <code title="get /udl/channel/tuple">client.channels.<a href="./src/unifieddatalibrary/resources/channels.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/channel_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/channel_tuple_response.py">ChannelTupleResponse</a></code>

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
- <code title="put /udl/comm/{id}">client.comm.<a href="./src/unifieddatalibrary/resources/comm.py">update</a>(id_1, \*\*<a href="src/unifieddatalibrary/types/comm_update_params.py">params</a>) -> None</code>
- <code title="get /udl/comm">client.comm.<a href="./src/unifieddatalibrary/resources/comm.py">list</a>() -> <a href="./src/unifieddatalibrary/types/comm_list_response.py">CommListResponse</a></code>
- <code title="delete /udl/comm/{id}">client.comm.<a href="./src/unifieddatalibrary/resources/comm.py">delete</a>(id) -> None</code>
- <code title="get /udl/comm/count">client.comm.<a href="./src/unifieddatalibrary/resources/comm.py">count</a>() -> str</code>
- <code title="get /udl/comm/queryhelp">client.comm.<a href="./src/unifieddatalibrary/resources/comm.py">queryhelp</a>() -> None</code>
- <code title="get /udl/comm/tuple">client.comm.<a href="./src/unifieddatalibrary/resources/comm.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/comm_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/comm_tuple_response.py">CommTupleResponse</a></code>

# Cots

Methods:

- <code title="post /udl/cot">client.cots.<a href="./src/unifieddatalibrary/resources/cots.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/cot_create_params.py">params</a>) -> None</code>

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
- <code title="put /udl/country/{code}">client.countries.<a href="./src/unifieddatalibrary/resources/countries.py">update</a>(code_1, \*\*<a href="src/unifieddatalibrary/types/country_update_params.py">params</a>) -> None</code>
- <code title="get /udl/country">client.countries.<a href="./src/unifieddatalibrary/resources/countries.py">list</a>() -> <a href="./src/unifieddatalibrary/types/country_list_response.py">CountryListResponse</a></code>
- <code title="delete /udl/country/{code}">client.countries.<a href="./src/unifieddatalibrary/resources/countries.py">delete</a>(code) -> None</code>
- <code title="get /udl/country/count">client.countries.<a href="./src/unifieddatalibrary/resources/countries.py">count</a>() -> str</code>
- <code title="get /udl/country/queryhelp">client.countries.<a href="./src/unifieddatalibrary/resources/countries.py">queryhelp</a>() -> None</code>
- <code title="get /udl/country/tuple">client.countries.<a href="./src/unifieddatalibrary/resources/countries.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/country_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/country_tuple_response.py">CountryTupleResponse</a></code>

# LinkStatus

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
- <code title="post /filedrop/udl-datalink">client.link_status.datalink.<a href="./src/unifieddatalibrary/resources/link_status/datalink.py">create_file_drop</a>(\*\*<a href="src/unifieddatalibrary/types/link_status/datalink_create_file_drop_params.py">params</a>) -> None</code>
- <code title="get /udl/datalink/queryhelp">client.link_status.datalink.<a href="./src/unifieddatalibrary/resources/link_status/datalink.py">queryhelp</a>() -> None</code>
- <code title="get /udl/datalink/tuple">client.link_status.datalink.<a href="./src/unifieddatalibrary/resources/link_status/datalink.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/link_status/datalink_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/link_status/datalink_tuple_response.py">DatalinkTupleResponse</a></code>

# SupportingData

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

## DataTypes

Types:

```python
from unifieddatalibrary.types.supporting_data import DataTypeListResponse
```

Methods:

- <code title="get /udl/dataowner/getDataTypes">client.supporting_data.data_types.<a href="./src/unifieddatalibrary/resources/supporting_data/data_types.py">list</a>() -> <a href="./src/unifieddatalibrary/types/supporting_data/data_type_list_response.py">DataTypeListResponse</a></code>

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
- <code title="put /udl/diplomaticclearance/{id}">client.diplomatic_clearance.<a href="./src/unifieddatalibrary/resources/diplomatic_clearance/diplomatic_clearance.py">update</a>(id_1, \*\*<a href="src/unifieddatalibrary/types/diplomatic_clearance_update_params.py">params</a>) -> None</code>
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

# MissionOps

## EffectRequests

Types:

```python
from unifieddatalibrary.types.mission_ops import (
    EffectRequest,
    EffectRequestAbridged,
    EffectRequestListResponse,
)
```

Methods:

- <code title="post /udl/effectrequest">client.mission_ops.effect_requests.<a href="./src/unifieddatalibrary/resources/mission_ops/effect_requests.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/mission_ops/effect_request_create_params.py">params</a>) -> None</code>
- <code title="get /udl/effectrequest">client.mission_ops.effect_requests.<a href="./src/unifieddatalibrary/resources/mission_ops/effect_requests.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/mission_ops/effect_request_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/mission_ops/effect_request_list_response.py">EffectRequestListResponse</a></code>

# EffectRequests

Types:

```python
from unifieddatalibrary.types import (
    EffectRequestCountResponse,
    EffectRequestHistoryCountResponse,
    EffectRequestTupleResponse,
)
```

Methods:

- <code title="get /udl/effectrequest/{id}">client.effect_requests.<a href="./src/unifieddatalibrary/resources/effect_requests/effect_requests.py">retrieve</a>(id) -> <a href="./src/unifieddatalibrary/types/mission_ops/effect_request.py">EffectRequest</a></code>
- <code title="get /udl/effectrequest/count">client.effect_requests.<a href="./src/unifieddatalibrary/resources/effect_requests/effect_requests.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/effect_request_count_params.py">params</a>) -> str</code>
- <code title="post /udl/effectrequest/createBulk">client.effect_requests.<a href="./src/unifieddatalibrary/resources/effect_requests/effect_requests.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/effect_request_create_bulk_params.py">params</a>) -> None</code>
- <code title="get /udl/effectrequest/history/count">client.effect_requests.<a href="./src/unifieddatalibrary/resources/effect_requests/effect_requests.py">history_count</a>(\*\*<a href="src/unifieddatalibrary/types/effect_request_history_count_params.py">params</a>) -> str</code>
- <code title="get /udl/effectrequest/queryhelp">client.effect_requests.<a href="./src/unifieddatalibrary/resources/effect_requests/effect_requests.py">query_help</a>() -> None</code>
- <code title="get /udl/effectrequest/tuple">client.effect_requests.<a href="./src/unifieddatalibrary/resources/effect_requests/effect_requests.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/effect_request_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/effect_request_tuple_response.py">EffectRequestTupleResponse</a></code>

## History

Types:

```python
from unifieddatalibrary.types.effect_requests import HistoryListResponse
```

Methods:

- <code title="get /udl/effectrequest/history">client.effect_requests.history.<a href="./src/unifieddatalibrary/resources/effect_requests/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/effect_requests/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/effect_requests/history_list_response.py">HistoryListResponse</a></code>
- <code title="get /udl/effectrequest/history/aodr">client.effect_requests.history.<a href="./src/unifieddatalibrary/resources/effect_requests/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/effect_requests/history_aodr_params.py">params</a>) -> None</code>

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
- <code title="put /udl/engine/{id}">client.engines.<a href="./src/unifieddatalibrary/resources/engines.py">update</a>(id_1, \*\*<a href="src/unifieddatalibrary/types/engine_update_params.py">params</a>) -> None</code>
- <code title="get /udl/engine">client.engines.<a href="./src/unifieddatalibrary/resources/engines.py">list</a>() -> <a href="./src/unifieddatalibrary/types/engine_list_response.py">EngineListResponse</a></code>
- <code title="delete /udl/engine/{id}">client.engines.<a href="./src/unifieddatalibrary/resources/engines.py">delete</a>(id) -> None</code>
- <code title="get /udl/engine/count">client.engines.<a href="./src/unifieddatalibrary/resources/engines.py">count</a>() -> str</code>
- <code title="get /udl/engine/queryhelp">client.engines.<a href="./src/unifieddatalibrary/resources/engines.py">queryhelp</a>() -> None</code>
- <code title="get /udl/engine/tuple">client.engines.<a href="./src/unifieddatalibrary/resources/engines.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/engine_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/engine_tuple_response.py">EngineTupleResponse</a></code>

# Enginedetails

Types:

```python
from unifieddatalibrary.types import EngineDetailsAbridged, EnginedetailListResponse
```

Methods:

- <code title="get /udl/enginedetails">client.enginedetails.<a href="./src/unifieddatalibrary/resources/enginedetails.py">list</a>() -> <a href="./src/unifieddatalibrary/types/enginedetail_list_response.py">EnginedetailListResponse</a></code>

# EngineDetails

Types:

```python
from unifieddatalibrary.types import EngineDetailsFull
```

Methods:

- <code title="post /udl/enginedetails">client.engine_details.<a href="./src/unifieddatalibrary/resources/engine_details.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/engine_detail_create_params.py">params</a>) -> None</code>
- <code title="get /udl/enginedetails/{id}">client.engine_details.<a href="./src/unifieddatalibrary/resources/engine_details.py">retrieve</a>(id) -> <a href="./src/unifieddatalibrary/types/engine_details_full.py">EngineDetailsFull</a></code>
- <code title="put /udl/enginedetails/{id}">client.engine_details.<a href="./src/unifieddatalibrary/resources/engine_details.py">update</a>(id_1, \*\*<a href="src/unifieddatalibrary/types/engine_detail_update_params.py">params</a>) -> None</code>
- <code title="delete /udl/enginedetails/{id}">client.engine_details.<a href="./src/unifieddatalibrary/resources/engine_details.py">delete</a>(id) -> None</code>

# Entities

Types:

```python
from unifieddatalibrary.types import (
    EntityAbridged,
    EntityFull,
    EntityCountResponse,
    EntityGetAllTypesResponse,
    EntityTupleResponse,
)
```

Methods:

- <code title="post /udl/entity">client.entities.<a href="./src/unifieddatalibrary/resources/entities.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/entity_create_params.py">params</a>) -> None</code>
- <code title="get /udl/entity/{id}">client.entities.<a href="./src/unifieddatalibrary/resources/entities.py">retrieve</a>(id) -> <a href="./src/unifieddatalibrary/types/entity_full.py">EntityFull</a></code>
- <code title="put /udl/entity/{id}">client.entities.<a href="./src/unifieddatalibrary/resources/entities.py">update</a>(id, \*\*<a href="src/unifieddatalibrary/types/entity_update_params.py">params</a>) -> None</code>
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
- <code title="put /udl/eop/{id}">client.eop.<a href="./src/unifieddatalibrary/resources/eop/eop.py">update</a>(id_1, \*\*<a href="src/unifieddatalibrary/types/eop_update_params.py">params</a>) -> None</code>
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
- <code title="put /udl/equipment/{id}">client.equipment.<a href="./src/unifieddatalibrary/resources/equipment.py">update</a>(id_1, \*\*<a href="src/unifieddatalibrary/types/equipment_update_params.py">params</a>) -> None</code>
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
from unifieddatalibrary.types import EventEvolutionListResponse, EventEvolutionCountResponse
```

Methods:

- <code title="post /udl/eventevolution">client.event_evolution.<a href="./src/unifieddatalibrary/resources/event_evolution.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/event_evolution_create_params.py">params</a>) -> None</code>
- <code title="get /udl/eventevolution">client.event_evolution.<a href="./src/unifieddatalibrary/resources/event_evolution.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/event_evolution_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/event_evolution_list_response.py">EventEvolutionListResponse</a></code>
- <code title="get /udl/eventevolution/count">client.event_evolution.<a href="./src/unifieddatalibrary/resources/event_evolution.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/event_evolution_count_params.py">params</a>) -> str</code>
- <code title="post /udl/eventevolution/createBulk">client.event_evolution.<a href="./src/unifieddatalibrary/resources/event_evolution.py">create_bulk</a>(\*\*<a href="src/unifieddatalibrary/types/event_evolution_create_bulk_params.py">params</a>) -> None</code>

# Eventevolutions

Types:

```python
from unifieddatalibrary.types import EventEvolutionAbridged, EventevolutionTupleResponse
```

Methods:

- <code title="get /udl/eventevolution/{id}">client.eventevolutions.<a href="./src/unifieddatalibrary/resources/eventevolutions/eventevolutions.py">retrieve</a>(id) -> <a href="./src/unifieddatalibrary/types/shared/event_evolution_full.py">EventEvolutionFull</a></code>
- <code title="get /udl/eventevolution/queryhelp">client.eventevolutions.<a href="./src/unifieddatalibrary/resources/eventevolutions/eventevolutions.py">queryhelp</a>() -> None</code>
- <code title="get /udl/eventevolution/tuple">client.eventevolutions.<a href="./src/unifieddatalibrary/resources/eventevolutions/eventevolutions.py">tuple</a>(\*\*<a href="src/unifieddatalibrary/types/eventevolution_tuple_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/eventevolution_tuple_response.py">EventevolutionTupleResponse</a></code>

## History

Types:

```python
from unifieddatalibrary.types.eventevolutions import HistoryListResponse, HistoryCountResponse
```

Methods:

- <code title="get /udl/eventevolution/history">client.eventevolutions.history.<a href="./src/unifieddatalibrary/resources/eventevolutions/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/eventevolutions/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/eventevolutions/history_list_response.py">HistoryListResponse</a></code>
- <code title="get /udl/eventevolution/history/aodr">client.eventevolutions.history.<a href="./src/unifieddatalibrary/resources/eventevolutions/history.py">aodr</a>(\*\*<a href="src/unifieddatalibrary/types/eventevolutions/history_aodr_params.py">params</a>) -> None</code>
- <code title="get /udl/eventevolution/history/count">client.eventevolutions.history.<a href="./src/unifieddatalibrary/resources/eventevolutions/history.py">count</a>(\*\*<a href="src/unifieddatalibrary/types/eventevolutions/history_count_params.py">params</a>) -> str</code>

# Flightplans

Types:

```python
from unifieddatalibrary.types import (
    FlightPlanAbridged,
    FlightplanListResponse,
    FlightplanCountResponse,
)
```

Methods:

- <code title="post /udl/flightplan">client.flightplans.<a href="./src/unifieddatalibrary/resources/flightplans/flightplans.py">create</a>(\*\*<a href="src/unifieddatalibrary/types/flightplan_create_params.py">params</a>) -> None</code>
- <code title="get /udl/flightplan">client.flightplans.<a href="./src/unifieddatalibrary/resources/flightplans/flightplans.py">list</a>() -> <a href="./src/unifieddatalibrary/types/flightplan_list_response.py">FlightplanListResponse</a></code>
- <code title="get /udl/flightplan/count">client.flightplans.<a href="./src/unifieddatalibrary/resources/flightplans/flightplans.py">count</a>() -> str</code>

## History

Types:

```python
from unifieddatalibrary.types.flightplans import HistoryListResponse
```

Methods:

- <code title="get /udl/flightplan/history">client.flightplans.history.<a href="./src/unifieddatalibrary/resources/flightplans/history.py">list</a>(\*\*<a href="src/unifieddatalibrary/types/flightplans/history_list_params.py">params</a>) -> <a href="./src/unifieddatalibrary/types/flightplans/history_list_response.py">HistoryListResponse</a></code>
