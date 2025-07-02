# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime
from typing_extensions import Literal

import httpx

from ...types import (
    mission_assignment_get_params,
    mission_assignment_list_params,
    mission_assignment_count_params,
    mission_assignment_tuple_params,
    mission_assignment_create_params,
    mission_assignment_update_params,
    mission_assignment_create_bulk_params,
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
from ...pagination import SyncOffsetPage, AsyncOffsetPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.mission_assignment_get_response import MissionAssignmentGetResponse
from ...types.mission_assignment_list_response import MissionAssignmentListResponse
from ...types.mission_assignment_tuple_response import MissionAssignmentTupleResponse
from ...types.mission_assignment_queryhelp_response import MissionAssignmentQueryhelpResponse

__all__ = ["MissionAssignmentResource", "AsyncMissionAssignmentResource"]


class MissionAssignmentResource(SyncAPIResource):
    @cached_property
    def history(self) -> HistoryResource:
        return HistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> MissionAssignmentResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return MissionAssignmentResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MissionAssignmentResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return MissionAssignmentResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        mad: str,
        source: str,
        ts: Union[str, datetime],
        id: str | NotGiven = NOT_GIVEN,
        c1associateddmpis: int | NotGiven = NOT_GIVEN,
        c2air: str | NotGiven = NOT_GIVEN,
        c2alt: int | NotGiven = NOT_GIVEN,
        c2crs: int | NotGiven = NOT_GIVEN,
        c2exerciseindicator: str | NotGiven = NOT_GIVEN,
        c2exercisemof: str | NotGiven = NOT_GIVEN,
        c2id: str | NotGiven = NOT_GIVEN,
        c2idamplifyingdescriptor: str | NotGiven = NOT_GIVEN,
        c2lnd: str | NotGiven = NOT_GIVEN,
        c2spc: str | NotGiven = NOT_GIVEN,
        c2spd: int | NotGiven = NOT_GIVEN,
        c2specialinterestindicator: str | NotGiven = NOT_GIVEN,
        c2sur: str | NotGiven = NOT_GIVEN,
        c3elv: float | NotGiven = NOT_GIVEN,
        c3lat: float | NotGiven = NOT_GIVEN,
        c3lon: float | NotGiven = NOT_GIVEN,
        c3ptl: str | NotGiven = NOT_GIVEN,
        c3ptnum: str | NotGiven = NOT_GIVEN,
        c4colon: int | NotGiven = NOT_GIVEN,
        c4def: str | NotGiven = NOT_GIVEN,
        c4egress: int | NotGiven = NOT_GIVEN,
        c4mod: int | NotGiven = NOT_GIVEN,
        c4numberofstores: int | NotGiven = NOT_GIVEN,
        c4runin: int | NotGiven = NOT_GIVEN,
        c4tgt: str | NotGiven = NOT_GIVEN,
        c4timediscrete: str | NotGiven = NOT_GIVEN,
        c4tm: int | NotGiven = NOT_GIVEN,
        c4typeofstores: int | NotGiven = NOT_GIVEN,
        c5colon: int | NotGiven = NOT_GIVEN,
        c5elevationlsbs: int | NotGiven = NOT_GIVEN,
        c5haeadj: int | NotGiven = NOT_GIVEN,
        c5latlsb: int | NotGiven = NOT_GIVEN,
        c5lonlsb: int | NotGiven = NOT_GIVEN,
        c5tgtbrng: int | NotGiven = NOT_GIVEN,
        c5tw: int | NotGiven = NOT_GIVEN,
        c6dspc: str | NotGiven = NOT_GIVEN,
        c6dspct: str | NotGiven = NOT_GIVEN,
        c6fplpm: str | NotGiven = NOT_GIVEN,
        c6intel: int | NotGiven = NOT_GIVEN,
        c6laser: int | NotGiven = NOT_GIVEN,
        c6longpm: str | NotGiven = NOT_GIVEN,
        c6tnr3: int | NotGiven = NOT_GIVEN,
        c7elang2: float | NotGiven = NOT_GIVEN,
        c7in3p: int | NotGiven = NOT_GIVEN,
        c7tnor: str | NotGiven = NOT_GIVEN,
        env: str | NotGiven = NOT_GIVEN,
        index: int | NotGiven = NOT_GIVEN,
        lat: float | NotGiven = NOT_GIVEN,
        lon: float | NotGiven = NOT_GIVEN,
        orginx: str | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        rc: str | NotGiven = NOT_GIVEN,
        rr: int | NotGiven = NOT_GIVEN,
        sz: str | NotGiven = NOT_GIVEN,
        tno: str | NotGiven = NOT_GIVEN,
        trk_id: str | NotGiven = NOT_GIVEN,
        twenv: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single MissionAssignment as a POST body and ingest
        into the database. A specific role is required to perform this service
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

          mad: The mission assignment discrete value.

          source: Source of the data.

          ts: The timestamp of the mission data, in ISO 8601 UTC format.

          id: Unique identifier of the record, auto-generated by the system.

          c1associateddmpis: TARGET POSITION CONTINUATION WORD - number of associated dmpis.

          c2air: TARGET DATA CONTINUATION WORD - air specific type, see TABLE B-21.

          c2alt: TARGET DATA CONTINUATION WORD - altitude, 100 FT, 2047=NS.

          c2crs: TARGET DATA CONTINUATION WORD - course in increments of 1 degree.

          c2exerciseindicator: TARGET DATA CONTINUATION WORD - exercise indicator.

          c2exercisemof: TARGET DATA CONTINUATION WORD - method of fire.

          c2id: TARGET DATA CONTINUATION WORD - identity.

          c2idamplifyingdescriptor: TARGET DATA CONTINUATION WORD - identity amplifying descriptor.

          c2lnd: TARGET DATA CONTINUATION WORD - land specific type, see TABLE B-21.

          c2spc: TARGET DATA CONTINUATION WORD - space specific type, see TABLE B-39.

          c2spd: TARGET DATA CONTINUATION WORD - speed in 2 DM/HR, 2047=NS.

          c2specialinterestindicator: TARGET DATA CONTINUATION WORD - special interest indicator.

          c2sur: TARGET DATA CONTINUATION WORD - surface specific type, see TABLE B-21.

          c3elv: POINT LOCATION CONTINUATION WORD - elevation, 25 FT, 1023=NS.

          c3lat: POINT LOCATION CONTINUATION WORD - latitude, 0.0013 MINUTE.

          c3lon: POINT LOCATION CONTINUATION WORD - longitude, 0.0013 MINUTE.

          c3ptl: TARGET DATA CONTINUATION WORD - point type 1.

          c3ptnum: TARGET DATA CONTINUATION WORD - point number.

          c4colon: SURFACE ATTACK CONTINUATION WORD - minute.

          c4def: SURFACE ATTACK CONTINUATION WORD - target defenses.

          c4egress: SURFACE ATTACK CONTINUATION WORD - run in heading, NS=511.

          c4mod: SURFACE ATTACK CONTINUATION WORD - mode of delivery.

          c4numberofstores: SURFACE ATTACK CONTINUATION WORD - number of stores, NS=63.

          c4runin: SURFACE ATTACK CONTINUATION WORD - run in heading, NS=511.

          c4tgt: SURFACE ATTACK CONTINUATION WORD - target type - see TABLE B-32.

          c4timediscrete: SURFACE ATTACK CONTINUATION WORD - time discrete.

          c4tm: SURFACE ATTACK CONTINUATION WORD - hour.

          c4typeofstores: SURFACE ATTACK CONTINUATION WORD - type of stores.

          c5colon: SURFACE ATTACK CONTINUATION WORD - seconds in increments of 1 sec.

          c5elevationlsbs: CONTINUATION WORD - used with c3_elv to double precision to approx 3 ft.

          c5haeadj: CONTINUATION WORD - hae adjustment, measured in 3.125 FT.

          c5latlsb: CONTINUATION WORD - used with c3_lat to double precision to approx 4 ft.

          c5lonlsb: CONTINUATION WORD - used with c3_lon to double precision to approx 4 ft.

          c5tgtbrng: CONTINUATION WORD - target bearing.

          c5tw: CONTINUATION WORD - time window.

          c6dspc: TARGETING CONTINUATION WORD - designator/seeker pulse code.

          c6dspct: TARGETING CONTINUATION WORD - designator/seeker pulse code type.

          c6fplpm: TARGETING CONTINUATION WORD - first pulse/last pulse mode.

          c6intel: TARGETING CONTINUATION WORD - index number, related, 0=NS.

          c6laser: TARGETING CONTINUATION WORD - laser illuminator code.

          c6longpm: TARGETING CONTINUATION WORD - long pulse mode.

          c6tnr3: TARGETING CONTINUATION WORD - track number, related to 3.

          c7elang2: THIRD PARTY CONTINUATION WORD - elevation angle, 2.

          c7in3p: THIRD PARTY CONTINUATION WORD - index number, third party.

          c7tnor: THIRD PARTY CONTINUATION WORD - track number, index originator.

          env: Environment.

          index: Index number.

          lat: WGS84 latitude, in degrees. -90 to 90 degrees (negative values south of
              equator).

          lon: WGS84 longitude, in degrees. -180 to 180 degrees (negative values west of Prime
              Meridian).

          orginx: Origin of index number.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          rc: Receipt/Compliance, values from TABLE B-9.

          rr: Recurrence rate, receipt/compliance.

          sz: Strength.

          tno: Track number objective.

          trk_id: The track ID that the status is referencing, addressee.

          twenv: Threat warning environment.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/udl/missionassignment",
            body=maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "mad": mad,
                    "source": source,
                    "ts": ts,
                    "id": id,
                    "c1associateddmpis": c1associateddmpis,
                    "c2air": c2air,
                    "c2alt": c2alt,
                    "c2crs": c2crs,
                    "c2exerciseindicator": c2exerciseindicator,
                    "c2exercisemof": c2exercisemof,
                    "c2id": c2id,
                    "c2idamplifyingdescriptor": c2idamplifyingdescriptor,
                    "c2lnd": c2lnd,
                    "c2spc": c2spc,
                    "c2spd": c2spd,
                    "c2specialinterestindicator": c2specialinterestindicator,
                    "c2sur": c2sur,
                    "c3elv": c3elv,
                    "c3lat": c3lat,
                    "c3lon": c3lon,
                    "c3ptl": c3ptl,
                    "c3ptnum": c3ptnum,
                    "c4colon": c4colon,
                    "c4def": c4def,
                    "c4egress": c4egress,
                    "c4mod": c4mod,
                    "c4numberofstores": c4numberofstores,
                    "c4runin": c4runin,
                    "c4tgt": c4tgt,
                    "c4timediscrete": c4timediscrete,
                    "c4tm": c4tm,
                    "c4typeofstores": c4typeofstores,
                    "c5colon": c5colon,
                    "c5elevationlsbs": c5elevationlsbs,
                    "c5haeadj": c5haeadj,
                    "c5latlsb": c5latlsb,
                    "c5lonlsb": c5lonlsb,
                    "c5tgtbrng": c5tgtbrng,
                    "c5tw": c5tw,
                    "c6dspc": c6dspc,
                    "c6dspct": c6dspct,
                    "c6fplpm": c6fplpm,
                    "c6intel": c6intel,
                    "c6laser": c6laser,
                    "c6longpm": c6longpm,
                    "c6tnr3": c6tnr3,
                    "c7elang2": c7elang2,
                    "c7in3p": c7in3p,
                    "c7tnor": c7tnor,
                    "env": env,
                    "index": index,
                    "lat": lat,
                    "lon": lon,
                    "orginx": orginx,
                    "origin": origin,
                    "rc": rc,
                    "rr": rr,
                    "sz": sz,
                    "tno": tno,
                    "trk_id": trk_id,
                    "twenv": twenv,
                },
                mission_assignment_create_params.MissionAssignmentCreateParams,
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
        mad: str,
        source: str,
        ts: Union[str, datetime],
        body_id: str | NotGiven = NOT_GIVEN,
        c1associateddmpis: int | NotGiven = NOT_GIVEN,
        c2air: str | NotGiven = NOT_GIVEN,
        c2alt: int | NotGiven = NOT_GIVEN,
        c2crs: int | NotGiven = NOT_GIVEN,
        c2exerciseindicator: str | NotGiven = NOT_GIVEN,
        c2exercisemof: str | NotGiven = NOT_GIVEN,
        c2id: str | NotGiven = NOT_GIVEN,
        c2idamplifyingdescriptor: str | NotGiven = NOT_GIVEN,
        c2lnd: str | NotGiven = NOT_GIVEN,
        c2spc: str | NotGiven = NOT_GIVEN,
        c2spd: int | NotGiven = NOT_GIVEN,
        c2specialinterestindicator: str | NotGiven = NOT_GIVEN,
        c2sur: str | NotGiven = NOT_GIVEN,
        c3elv: float | NotGiven = NOT_GIVEN,
        c3lat: float | NotGiven = NOT_GIVEN,
        c3lon: float | NotGiven = NOT_GIVEN,
        c3ptl: str | NotGiven = NOT_GIVEN,
        c3ptnum: str | NotGiven = NOT_GIVEN,
        c4colon: int | NotGiven = NOT_GIVEN,
        c4def: str | NotGiven = NOT_GIVEN,
        c4egress: int | NotGiven = NOT_GIVEN,
        c4mod: int | NotGiven = NOT_GIVEN,
        c4numberofstores: int | NotGiven = NOT_GIVEN,
        c4runin: int | NotGiven = NOT_GIVEN,
        c4tgt: str | NotGiven = NOT_GIVEN,
        c4timediscrete: str | NotGiven = NOT_GIVEN,
        c4tm: int | NotGiven = NOT_GIVEN,
        c4typeofstores: int | NotGiven = NOT_GIVEN,
        c5colon: int | NotGiven = NOT_GIVEN,
        c5elevationlsbs: int | NotGiven = NOT_GIVEN,
        c5haeadj: int | NotGiven = NOT_GIVEN,
        c5latlsb: int | NotGiven = NOT_GIVEN,
        c5lonlsb: int | NotGiven = NOT_GIVEN,
        c5tgtbrng: int | NotGiven = NOT_GIVEN,
        c5tw: int | NotGiven = NOT_GIVEN,
        c6dspc: str | NotGiven = NOT_GIVEN,
        c6dspct: str | NotGiven = NOT_GIVEN,
        c6fplpm: str | NotGiven = NOT_GIVEN,
        c6intel: int | NotGiven = NOT_GIVEN,
        c6laser: int | NotGiven = NOT_GIVEN,
        c6longpm: str | NotGiven = NOT_GIVEN,
        c6tnr3: int | NotGiven = NOT_GIVEN,
        c7elang2: float | NotGiven = NOT_GIVEN,
        c7in3p: int | NotGiven = NOT_GIVEN,
        c7tnor: str | NotGiven = NOT_GIVEN,
        env: str | NotGiven = NOT_GIVEN,
        index: int | NotGiven = NOT_GIVEN,
        lat: float | NotGiven = NOT_GIVEN,
        lon: float | NotGiven = NOT_GIVEN,
        orginx: str | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        rc: str | NotGiven = NOT_GIVEN,
        rr: int | NotGiven = NOT_GIVEN,
        sz: str | NotGiven = NOT_GIVEN,
        tno: str | NotGiven = NOT_GIVEN,
        trk_id: str | NotGiven = NOT_GIVEN,
        twenv: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Service operation to update a single MissionAssignment.

        A specific role is
        required to perform this service operation. Please contact the UDL team for
        assistance.

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

          mad: The mission assignment discrete value.

          source: Source of the data.

          ts: The timestamp of the mission data, in ISO 8601 UTC format.

          body_id: Unique identifier of the record, auto-generated by the system.

          c1associateddmpis: TARGET POSITION CONTINUATION WORD - number of associated dmpis.

          c2air: TARGET DATA CONTINUATION WORD - air specific type, see TABLE B-21.

          c2alt: TARGET DATA CONTINUATION WORD - altitude, 100 FT, 2047=NS.

          c2crs: TARGET DATA CONTINUATION WORD - course in increments of 1 degree.

          c2exerciseindicator: TARGET DATA CONTINUATION WORD - exercise indicator.

          c2exercisemof: TARGET DATA CONTINUATION WORD - method of fire.

          c2id: TARGET DATA CONTINUATION WORD - identity.

          c2idamplifyingdescriptor: TARGET DATA CONTINUATION WORD - identity amplifying descriptor.

          c2lnd: TARGET DATA CONTINUATION WORD - land specific type, see TABLE B-21.

          c2spc: TARGET DATA CONTINUATION WORD - space specific type, see TABLE B-39.

          c2spd: TARGET DATA CONTINUATION WORD - speed in 2 DM/HR, 2047=NS.

          c2specialinterestindicator: TARGET DATA CONTINUATION WORD - special interest indicator.

          c2sur: TARGET DATA CONTINUATION WORD - surface specific type, see TABLE B-21.

          c3elv: POINT LOCATION CONTINUATION WORD - elevation, 25 FT, 1023=NS.

          c3lat: POINT LOCATION CONTINUATION WORD - latitude, 0.0013 MINUTE.

          c3lon: POINT LOCATION CONTINUATION WORD - longitude, 0.0013 MINUTE.

          c3ptl: TARGET DATA CONTINUATION WORD - point type 1.

          c3ptnum: TARGET DATA CONTINUATION WORD - point number.

          c4colon: SURFACE ATTACK CONTINUATION WORD - minute.

          c4def: SURFACE ATTACK CONTINUATION WORD - target defenses.

          c4egress: SURFACE ATTACK CONTINUATION WORD - run in heading, NS=511.

          c4mod: SURFACE ATTACK CONTINUATION WORD - mode of delivery.

          c4numberofstores: SURFACE ATTACK CONTINUATION WORD - number of stores, NS=63.

          c4runin: SURFACE ATTACK CONTINUATION WORD - run in heading, NS=511.

          c4tgt: SURFACE ATTACK CONTINUATION WORD - target type - see TABLE B-32.

          c4timediscrete: SURFACE ATTACK CONTINUATION WORD - time discrete.

          c4tm: SURFACE ATTACK CONTINUATION WORD - hour.

          c4typeofstores: SURFACE ATTACK CONTINUATION WORD - type of stores.

          c5colon: SURFACE ATTACK CONTINUATION WORD - seconds in increments of 1 sec.

          c5elevationlsbs: CONTINUATION WORD - used with c3_elv to double precision to approx 3 ft.

          c5haeadj: CONTINUATION WORD - hae adjustment, measured in 3.125 FT.

          c5latlsb: CONTINUATION WORD - used with c3_lat to double precision to approx 4 ft.

          c5lonlsb: CONTINUATION WORD - used with c3_lon to double precision to approx 4 ft.

          c5tgtbrng: CONTINUATION WORD - target bearing.

          c5tw: CONTINUATION WORD - time window.

          c6dspc: TARGETING CONTINUATION WORD - designator/seeker pulse code.

          c6dspct: TARGETING CONTINUATION WORD - designator/seeker pulse code type.

          c6fplpm: TARGETING CONTINUATION WORD - first pulse/last pulse mode.

          c6intel: TARGETING CONTINUATION WORD - index number, related, 0=NS.

          c6laser: TARGETING CONTINUATION WORD - laser illuminator code.

          c6longpm: TARGETING CONTINUATION WORD - long pulse mode.

          c6tnr3: TARGETING CONTINUATION WORD - track number, related to 3.

          c7elang2: THIRD PARTY CONTINUATION WORD - elevation angle, 2.

          c7in3p: THIRD PARTY CONTINUATION WORD - index number, third party.

          c7tnor: THIRD PARTY CONTINUATION WORD - track number, index originator.

          env: Environment.

          index: Index number.

          lat: WGS84 latitude, in degrees. -90 to 90 degrees (negative values south of
              equator).

          lon: WGS84 longitude, in degrees. -180 to 180 degrees (negative values west of Prime
              Meridian).

          orginx: Origin of index number.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          rc: Receipt/Compliance, values from TABLE B-9.

          rr: Recurrence rate, receipt/compliance.

          sz: Strength.

          tno: Track number objective.

          trk_id: The track ID that the status is referencing, addressee.

          twenv: Threat warning environment.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            f"/udl/missionassignment/{path_id}",
            body=maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "mad": mad,
                    "source": source,
                    "ts": ts,
                    "body_id": body_id,
                    "c1associateddmpis": c1associateddmpis,
                    "c2air": c2air,
                    "c2alt": c2alt,
                    "c2crs": c2crs,
                    "c2exerciseindicator": c2exerciseindicator,
                    "c2exercisemof": c2exercisemof,
                    "c2id": c2id,
                    "c2idamplifyingdescriptor": c2idamplifyingdescriptor,
                    "c2lnd": c2lnd,
                    "c2spc": c2spc,
                    "c2spd": c2spd,
                    "c2specialinterestindicator": c2specialinterestindicator,
                    "c2sur": c2sur,
                    "c3elv": c3elv,
                    "c3lat": c3lat,
                    "c3lon": c3lon,
                    "c3ptl": c3ptl,
                    "c3ptnum": c3ptnum,
                    "c4colon": c4colon,
                    "c4def": c4def,
                    "c4egress": c4egress,
                    "c4mod": c4mod,
                    "c4numberofstores": c4numberofstores,
                    "c4runin": c4runin,
                    "c4tgt": c4tgt,
                    "c4timediscrete": c4timediscrete,
                    "c4tm": c4tm,
                    "c4typeofstores": c4typeofstores,
                    "c5colon": c5colon,
                    "c5elevationlsbs": c5elevationlsbs,
                    "c5haeadj": c5haeadj,
                    "c5latlsb": c5latlsb,
                    "c5lonlsb": c5lonlsb,
                    "c5tgtbrng": c5tgtbrng,
                    "c5tw": c5tw,
                    "c6dspc": c6dspc,
                    "c6dspct": c6dspct,
                    "c6fplpm": c6fplpm,
                    "c6intel": c6intel,
                    "c6laser": c6laser,
                    "c6longpm": c6longpm,
                    "c6tnr3": c6tnr3,
                    "c7elang2": c7elang2,
                    "c7in3p": c7in3p,
                    "c7tnor": c7tnor,
                    "env": env,
                    "index": index,
                    "lat": lat,
                    "lon": lon,
                    "orginx": orginx,
                    "origin": origin,
                    "rc": rc,
                    "rr": rr,
                    "sz": sz,
                    "tno": tno,
                    "trk_id": trk_id,
                    "twenv": twenv,
                },
                mission_assignment_update_params.MissionAssignmentUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        *,
        ts: Union[str, datetime],
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncOffsetPage[MissionAssignmentListResponse]:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          ts: the timestamp of the mission data, in ISO 8601 UTC format.
              (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/missionassignment",
            page=SyncOffsetPage[MissionAssignmentListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "ts": ts,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    mission_assignment_list_params.MissionAssignmentListParams,
                ),
            ),
            model=MissionAssignmentListResponse,
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
        Service operation to delete a MissionAssignment object specified by the passed
        ID path parameter. A specific role is required to perform this service
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
            f"/udl/missionassignment/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def count(
        self,
        *,
        ts: Union[str, datetime],
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
          ts: the timestamp of the mission data, in ISO 8601 UTC format.
              (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return self._get(
            "/udl/missionassignment/count",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "ts": ts,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    mission_assignment_count_params.MissionAssignmentCountParams,
                ),
            ),
            cast_to=str,
        )

    def create_bulk(
        self,
        *,
        body: Iterable[mission_assignment_create_bulk_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take multiple MissionAssignments as a POST body and ingest
        into the database. A specific role is required to perform this service
        operation. Please contact the UDL team for assistance.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/udl/missionassignment/createBulk",
            body=maybe_transform(body, Iterable[mission_assignment_create_bulk_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
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
    ) -> MissionAssignmentGetResponse:
        """
        Service operation to get a single MissionAssignment record by its unique ID
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
            f"/udl/missionassignment/{id}",
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
                    mission_assignment_get_params.MissionAssignmentGetParams,
                ),
            ),
            cast_to=MissionAssignmentGetResponse,
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
    ) -> MissionAssignmentQueryhelpResponse:
        """
        Service operation to provide detailed information on available dynamic query
        parameters for a particular data type.
        """
        return self._get(
            "/udl/missionassignment/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MissionAssignmentQueryhelpResponse,
        )

    def tuple(
        self,
        *,
        columns: str,
        ts: Union[str, datetime],
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MissionAssignmentTupleResponse:
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

          ts: the timestamp of the mission data, in ISO 8601 UTC format.
              (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/udl/missionassignment/tuple",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "columns": columns,
                        "ts": ts,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    mission_assignment_tuple_params.MissionAssignmentTupleParams,
                ),
            ),
            cast_to=MissionAssignmentTupleResponse,
        )


class AsyncMissionAssignmentResource(AsyncAPIResource):
    @cached_property
    def history(self) -> AsyncHistoryResource:
        return AsyncHistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncMissionAssignmentResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncMissionAssignmentResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMissionAssignmentResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncMissionAssignmentResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        mad: str,
        source: str,
        ts: Union[str, datetime],
        id: str | NotGiven = NOT_GIVEN,
        c1associateddmpis: int | NotGiven = NOT_GIVEN,
        c2air: str | NotGiven = NOT_GIVEN,
        c2alt: int | NotGiven = NOT_GIVEN,
        c2crs: int | NotGiven = NOT_GIVEN,
        c2exerciseindicator: str | NotGiven = NOT_GIVEN,
        c2exercisemof: str | NotGiven = NOT_GIVEN,
        c2id: str | NotGiven = NOT_GIVEN,
        c2idamplifyingdescriptor: str | NotGiven = NOT_GIVEN,
        c2lnd: str | NotGiven = NOT_GIVEN,
        c2spc: str | NotGiven = NOT_GIVEN,
        c2spd: int | NotGiven = NOT_GIVEN,
        c2specialinterestindicator: str | NotGiven = NOT_GIVEN,
        c2sur: str | NotGiven = NOT_GIVEN,
        c3elv: float | NotGiven = NOT_GIVEN,
        c3lat: float | NotGiven = NOT_GIVEN,
        c3lon: float | NotGiven = NOT_GIVEN,
        c3ptl: str | NotGiven = NOT_GIVEN,
        c3ptnum: str | NotGiven = NOT_GIVEN,
        c4colon: int | NotGiven = NOT_GIVEN,
        c4def: str | NotGiven = NOT_GIVEN,
        c4egress: int | NotGiven = NOT_GIVEN,
        c4mod: int | NotGiven = NOT_GIVEN,
        c4numberofstores: int | NotGiven = NOT_GIVEN,
        c4runin: int | NotGiven = NOT_GIVEN,
        c4tgt: str | NotGiven = NOT_GIVEN,
        c4timediscrete: str | NotGiven = NOT_GIVEN,
        c4tm: int | NotGiven = NOT_GIVEN,
        c4typeofstores: int | NotGiven = NOT_GIVEN,
        c5colon: int | NotGiven = NOT_GIVEN,
        c5elevationlsbs: int | NotGiven = NOT_GIVEN,
        c5haeadj: int | NotGiven = NOT_GIVEN,
        c5latlsb: int | NotGiven = NOT_GIVEN,
        c5lonlsb: int | NotGiven = NOT_GIVEN,
        c5tgtbrng: int | NotGiven = NOT_GIVEN,
        c5tw: int | NotGiven = NOT_GIVEN,
        c6dspc: str | NotGiven = NOT_GIVEN,
        c6dspct: str | NotGiven = NOT_GIVEN,
        c6fplpm: str | NotGiven = NOT_GIVEN,
        c6intel: int | NotGiven = NOT_GIVEN,
        c6laser: int | NotGiven = NOT_GIVEN,
        c6longpm: str | NotGiven = NOT_GIVEN,
        c6tnr3: int | NotGiven = NOT_GIVEN,
        c7elang2: float | NotGiven = NOT_GIVEN,
        c7in3p: int | NotGiven = NOT_GIVEN,
        c7tnor: str | NotGiven = NOT_GIVEN,
        env: str | NotGiven = NOT_GIVEN,
        index: int | NotGiven = NOT_GIVEN,
        lat: float | NotGiven = NOT_GIVEN,
        lon: float | NotGiven = NOT_GIVEN,
        orginx: str | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        rc: str | NotGiven = NOT_GIVEN,
        rr: int | NotGiven = NOT_GIVEN,
        sz: str | NotGiven = NOT_GIVEN,
        tno: str | NotGiven = NOT_GIVEN,
        trk_id: str | NotGiven = NOT_GIVEN,
        twenv: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single MissionAssignment as a POST body and ingest
        into the database. A specific role is required to perform this service
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

          mad: The mission assignment discrete value.

          source: Source of the data.

          ts: The timestamp of the mission data, in ISO 8601 UTC format.

          id: Unique identifier of the record, auto-generated by the system.

          c1associateddmpis: TARGET POSITION CONTINUATION WORD - number of associated dmpis.

          c2air: TARGET DATA CONTINUATION WORD - air specific type, see TABLE B-21.

          c2alt: TARGET DATA CONTINUATION WORD - altitude, 100 FT, 2047=NS.

          c2crs: TARGET DATA CONTINUATION WORD - course in increments of 1 degree.

          c2exerciseindicator: TARGET DATA CONTINUATION WORD - exercise indicator.

          c2exercisemof: TARGET DATA CONTINUATION WORD - method of fire.

          c2id: TARGET DATA CONTINUATION WORD - identity.

          c2idamplifyingdescriptor: TARGET DATA CONTINUATION WORD - identity amplifying descriptor.

          c2lnd: TARGET DATA CONTINUATION WORD - land specific type, see TABLE B-21.

          c2spc: TARGET DATA CONTINUATION WORD - space specific type, see TABLE B-39.

          c2spd: TARGET DATA CONTINUATION WORD - speed in 2 DM/HR, 2047=NS.

          c2specialinterestindicator: TARGET DATA CONTINUATION WORD - special interest indicator.

          c2sur: TARGET DATA CONTINUATION WORD - surface specific type, see TABLE B-21.

          c3elv: POINT LOCATION CONTINUATION WORD - elevation, 25 FT, 1023=NS.

          c3lat: POINT LOCATION CONTINUATION WORD - latitude, 0.0013 MINUTE.

          c3lon: POINT LOCATION CONTINUATION WORD - longitude, 0.0013 MINUTE.

          c3ptl: TARGET DATA CONTINUATION WORD - point type 1.

          c3ptnum: TARGET DATA CONTINUATION WORD - point number.

          c4colon: SURFACE ATTACK CONTINUATION WORD - minute.

          c4def: SURFACE ATTACK CONTINUATION WORD - target defenses.

          c4egress: SURFACE ATTACK CONTINUATION WORD - run in heading, NS=511.

          c4mod: SURFACE ATTACK CONTINUATION WORD - mode of delivery.

          c4numberofstores: SURFACE ATTACK CONTINUATION WORD - number of stores, NS=63.

          c4runin: SURFACE ATTACK CONTINUATION WORD - run in heading, NS=511.

          c4tgt: SURFACE ATTACK CONTINUATION WORD - target type - see TABLE B-32.

          c4timediscrete: SURFACE ATTACK CONTINUATION WORD - time discrete.

          c4tm: SURFACE ATTACK CONTINUATION WORD - hour.

          c4typeofstores: SURFACE ATTACK CONTINUATION WORD - type of stores.

          c5colon: SURFACE ATTACK CONTINUATION WORD - seconds in increments of 1 sec.

          c5elevationlsbs: CONTINUATION WORD - used with c3_elv to double precision to approx 3 ft.

          c5haeadj: CONTINUATION WORD - hae adjustment, measured in 3.125 FT.

          c5latlsb: CONTINUATION WORD - used with c3_lat to double precision to approx 4 ft.

          c5lonlsb: CONTINUATION WORD - used with c3_lon to double precision to approx 4 ft.

          c5tgtbrng: CONTINUATION WORD - target bearing.

          c5tw: CONTINUATION WORD - time window.

          c6dspc: TARGETING CONTINUATION WORD - designator/seeker pulse code.

          c6dspct: TARGETING CONTINUATION WORD - designator/seeker pulse code type.

          c6fplpm: TARGETING CONTINUATION WORD - first pulse/last pulse mode.

          c6intel: TARGETING CONTINUATION WORD - index number, related, 0=NS.

          c6laser: TARGETING CONTINUATION WORD - laser illuminator code.

          c6longpm: TARGETING CONTINUATION WORD - long pulse mode.

          c6tnr3: TARGETING CONTINUATION WORD - track number, related to 3.

          c7elang2: THIRD PARTY CONTINUATION WORD - elevation angle, 2.

          c7in3p: THIRD PARTY CONTINUATION WORD - index number, third party.

          c7tnor: THIRD PARTY CONTINUATION WORD - track number, index originator.

          env: Environment.

          index: Index number.

          lat: WGS84 latitude, in degrees. -90 to 90 degrees (negative values south of
              equator).

          lon: WGS84 longitude, in degrees. -180 to 180 degrees (negative values west of Prime
              Meridian).

          orginx: Origin of index number.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          rc: Receipt/Compliance, values from TABLE B-9.

          rr: Recurrence rate, receipt/compliance.

          sz: Strength.

          tno: Track number objective.

          trk_id: The track ID that the status is referencing, addressee.

          twenv: Threat warning environment.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/udl/missionassignment",
            body=await async_maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "mad": mad,
                    "source": source,
                    "ts": ts,
                    "id": id,
                    "c1associateddmpis": c1associateddmpis,
                    "c2air": c2air,
                    "c2alt": c2alt,
                    "c2crs": c2crs,
                    "c2exerciseindicator": c2exerciseindicator,
                    "c2exercisemof": c2exercisemof,
                    "c2id": c2id,
                    "c2idamplifyingdescriptor": c2idamplifyingdescriptor,
                    "c2lnd": c2lnd,
                    "c2spc": c2spc,
                    "c2spd": c2spd,
                    "c2specialinterestindicator": c2specialinterestindicator,
                    "c2sur": c2sur,
                    "c3elv": c3elv,
                    "c3lat": c3lat,
                    "c3lon": c3lon,
                    "c3ptl": c3ptl,
                    "c3ptnum": c3ptnum,
                    "c4colon": c4colon,
                    "c4def": c4def,
                    "c4egress": c4egress,
                    "c4mod": c4mod,
                    "c4numberofstores": c4numberofstores,
                    "c4runin": c4runin,
                    "c4tgt": c4tgt,
                    "c4timediscrete": c4timediscrete,
                    "c4tm": c4tm,
                    "c4typeofstores": c4typeofstores,
                    "c5colon": c5colon,
                    "c5elevationlsbs": c5elevationlsbs,
                    "c5haeadj": c5haeadj,
                    "c5latlsb": c5latlsb,
                    "c5lonlsb": c5lonlsb,
                    "c5tgtbrng": c5tgtbrng,
                    "c5tw": c5tw,
                    "c6dspc": c6dspc,
                    "c6dspct": c6dspct,
                    "c6fplpm": c6fplpm,
                    "c6intel": c6intel,
                    "c6laser": c6laser,
                    "c6longpm": c6longpm,
                    "c6tnr3": c6tnr3,
                    "c7elang2": c7elang2,
                    "c7in3p": c7in3p,
                    "c7tnor": c7tnor,
                    "env": env,
                    "index": index,
                    "lat": lat,
                    "lon": lon,
                    "orginx": orginx,
                    "origin": origin,
                    "rc": rc,
                    "rr": rr,
                    "sz": sz,
                    "tno": tno,
                    "trk_id": trk_id,
                    "twenv": twenv,
                },
                mission_assignment_create_params.MissionAssignmentCreateParams,
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
        mad: str,
        source: str,
        ts: Union[str, datetime],
        body_id: str | NotGiven = NOT_GIVEN,
        c1associateddmpis: int | NotGiven = NOT_GIVEN,
        c2air: str | NotGiven = NOT_GIVEN,
        c2alt: int | NotGiven = NOT_GIVEN,
        c2crs: int | NotGiven = NOT_GIVEN,
        c2exerciseindicator: str | NotGiven = NOT_GIVEN,
        c2exercisemof: str | NotGiven = NOT_GIVEN,
        c2id: str | NotGiven = NOT_GIVEN,
        c2idamplifyingdescriptor: str | NotGiven = NOT_GIVEN,
        c2lnd: str | NotGiven = NOT_GIVEN,
        c2spc: str | NotGiven = NOT_GIVEN,
        c2spd: int | NotGiven = NOT_GIVEN,
        c2specialinterestindicator: str | NotGiven = NOT_GIVEN,
        c2sur: str | NotGiven = NOT_GIVEN,
        c3elv: float | NotGiven = NOT_GIVEN,
        c3lat: float | NotGiven = NOT_GIVEN,
        c3lon: float | NotGiven = NOT_GIVEN,
        c3ptl: str | NotGiven = NOT_GIVEN,
        c3ptnum: str | NotGiven = NOT_GIVEN,
        c4colon: int | NotGiven = NOT_GIVEN,
        c4def: str | NotGiven = NOT_GIVEN,
        c4egress: int | NotGiven = NOT_GIVEN,
        c4mod: int | NotGiven = NOT_GIVEN,
        c4numberofstores: int | NotGiven = NOT_GIVEN,
        c4runin: int | NotGiven = NOT_GIVEN,
        c4tgt: str | NotGiven = NOT_GIVEN,
        c4timediscrete: str | NotGiven = NOT_GIVEN,
        c4tm: int | NotGiven = NOT_GIVEN,
        c4typeofstores: int | NotGiven = NOT_GIVEN,
        c5colon: int | NotGiven = NOT_GIVEN,
        c5elevationlsbs: int | NotGiven = NOT_GIVEN,
        c5haeadj: int | NotGiven = NOT_GIVEN,
        c5latlsb: int | NotGiven = NOT_GIVEN,
        c5lonlsb: int | NotGiven = NOT_GIVEN,
        c5tgtbrng: int | NotGiven = NOT_GIVEN,
        c5tw: int | NotGiven = NOT_GIVEN,
        c6dspc: str | NotGiven = NOT_GIVEN,
        c6dspct: str | NotGiven = NOT_GIVEN,
        c6fplpm: str | NotGiven = NOT_GIVEN,
        c6intel: int | NotGiven = NOT_GIVEN,
        c6laser: int | NotGiven = NOT_GIVEN,
        c6longpm: str | NotGiven = NOT_GIVEN,
        c6tnr3: int | NotGiven = NOT_GIVEN,
        c7elang2: float | NotGiven = NOT_GIVEN,
        c7in3p: int | NotGiven = NOT_GIVEN,
        c7tnor: str | NotGiven = NOT_GIVEN,
        env: str | NotGiven = NOT_GIVEN,
        index: int | NotGiven = NOT_GIVEN,
        lat: float | NotGiven = NOT_GIVEN,
        lon: float | NotGiven = NOT_GIVEN,
        orginx: str | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        rc: str | NotGiven = NOT_GIVEN,
        rr: int | NotGiven = NOT_GIVEN,
        sz: str | NotGiven = NOT_GIVEN,
        tno: str | NotGiven = NOT_GIVEN,
        trk_id: str | NotGiven = NOT_GIVEN,
        twenv: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Service operation to update a single MissionAssignment.

        A specific role is
        required to perform this service operation. Please contact the UDL team for
        assistance.

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

          mad: The mission assignment discrete value.

          source: Source of the data.

          ts: The timestamp of the mission data, in ISO 8601 UTC format.

          body_id: Unique identifier of the record, auto-generated by the system.

          c1associateddmpis: TARGET POSITION CONTINUATION WORD - number of associated dmpis.

          c2air: TARGET DATA CONTINUATION WORD - air specific type, see TABLE B-21.

          c2alt: TARGET DATA CONTINUATION WORD - altitude, 100 FT, 2047=NS.

          c2crs: TARGET DATA CONTINUATION WORD - course in increments of 1 degree.

          c2exerciseindicator: TARGET DATA CONTINUATION WORD - exercise indicator.

          c2exercisemof: TARGET DATA CONTINUATION WORD - method of fire.

          c2id: TARGET DATA CONTINUATION WORD - identity.

          c2idamplifyingdescriptor: TARGET DATA CONTINUATION WORD - identity amplifying descriptor.

          c2lnd: TARGET DATA CONTINUATION WORD - land specific type, see TABLE B-21.

          c2spc: TARGET DATA CONTINUATION WORD - space specific type, see TABLE B-39.

          c2spd: TARGET DATA CONTINUATION WORD - speed in 2 DM/HR, 2047=NS.

          c2specialinterestindicator: TARGET DATA CONTINUATION WORD - special interest indicator.

          c2sur: TARGET DATA CONTINUATION WORD - surface specific type, see TABLE B-21.

          c3elv: POINT LOCATION CONTINUATION WORD - elevation, 25 FT, 1023=NS.

          c3lat: POINT LOCATION CONTINUATION WORD - latitude, 0.0013 MINUTE.

          c3lon: POINT LOCATION CONTINUATION WORD - longitude, 0.0013 MINUTE.

          c3ptl: TARGET DATA CONTINUATION WORD - point type 1.

          c3ptnum: TARGET DATA CONTINUATION WORD - point number.

          c4colon: SURFACE ATTACK CONTINUATION WORD - minute.

          c4def: SURFACE ATTACK CONTINUATION WORD - target defenses.

          c4egress: SURFACE ATTACK CONTINUATION WORD - run in heading, NS=511.

          c4mod: SURFACE ATTACK CONTINUATION WORD - mode of delivery.

          c4numberofstores: SURFACE ATTACK CONTINUATION WORD - number of stores, NS=63.

          c4runin: SURFACE ATTACK CONTINUATION WORD - run in heading, NS=511.

          c4tgt: SURFACE ATTACK CONTINUATION WORD - target type - see TABLE B-32.

          c4timediscrete: SURFACE ATTACK CONTINUATION WORD - time discrete.

          c4tm: SURFACE ATTACK CONTINUATION WORD - hour.

          c4typeofstores: SURFACE ATTACK CONTINUATION WORD - type of stores.

          c5colon: SURFACE ATTACK CONTINUATION WORD - seconds in increments of 1 sec.

          c5elevationlsbs: CONTINUATION WORD - used with c3_elv to double precision to approx 3 ft.

          c5haeadj: CONTINUATION WORD - hae adjustment, measured in 3.125 FT.

          c5latlsb: CONTINUATION WORD - used with c3_lat to double precision to approx 4 ft.

          c5lonlsb: CONTINUATION WORD - used with c3_lon to double precision to approx 4 ft.

          c5tgtbrng: CONTINUATION WORD - target bearing.

          c5tw: CONTINUATION WORD - time window.

          c6dspc: TARGETING CONTINUATION WORD - designator/seeker pulse code.

          c6dspct: TARGETING CONTINUATION WORD - designator/seeker pulse code type.

          c6fplpm: TARGETING CONTINUATION WORD - first pulse/last pulse mode.

          c6intel: TARGETING CONTINUATION WORD - index number, related, 0=NS.

          c6laser: TARGETING CONTINUATION WORD - laser illuminator code.

          c6longpm: TARGETING CONTINUATION WORD - long pulse mode.

          c6tnr3: TARGETING CONTINUATION WORD - track number, related to 3.

          c7elang2: THIRD PARTY CONTINUATION WORD - elevation angle, 2.

          c7in3p: THIRD PARTY CONTINUATION WORD - index number, third party.

          c7tnor: THIRD PARTY CONTINUATION WORD - track number, index originator.

          env: Environment.

          index: Index number.

          lat: WGS84 latitude, in degrees. -90 to 90 degrees (negative values south of
              equator).

          lon: WGS84 longitude, in degrees. -180 to 180 degrees (negative values west of Prime
              Meridian).

          orginx: Origin of index number.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          rc: Receipt/Compliance, values from TABLE B-9.

          rr: Recurrence rate, receipt/compliance.

          sz: Strength.

          tno: Track number objective.

          trk_id: The track ID that the status is referencing, addressee.

          twenv: Threat warning environment.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            f"/udl/missionassignment/{path_id}",
            body=await async_maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "mad": mad,
                    "source": source,
                    "ts": ts,
                    "body_id": body_id,
                    "c1associateddmpis": c1associateddmpis,
                    "c2air": c2air,
                    "c2alt": c2alt,
                    "c2crs": c2crs,
                    "c2exerciseindicator": c2exerciseindicator,
                    "c2exercisemof": c2exercisemof,
                    "c2id": c2id,
                    "c2idamplifyingdescriptor": c2idamplifyingdescriptor,
                    "c2lnd": c2lnd,
                    "c2spc": c2spc,
                    "c2spd": c2spd,
                    "c2specialinterestindicator": c2specialinterestindicator,
                    "c2sur": c2sur,
                    "c3elv": c3elv,
                    "c3lat": c3lat,
                    "c3lon": c3lon,
                    "c3ptl": c3ptl,
                    "c3ptnum": c3ptnum,
                    "c4colon": c4colon,
                    "c4def": c4def,
                    "c4egress": c4egress,
                    "c4mod": c4mod,
                    "c4numberofstores": c4numberofstores,
                    "c4runin": c4runin,
                    "c4tgt": c4tgt,
                    "c4timediscrete": c4timediscrete,
                    "c4tm": c4tm,
                    "c4typeofstores": c4typeofstores,
                    "c5colon": c5colon,
                    "c5elevationlsbs": c5elevationlsbs,
                    "c5haeadj": c5haeadj,
                    "c5latlsb": c5latlsb,
                    "c5lonlsb": c5lonlsb,
                    "c5tgtbrng": c5tgtbrng,
                    "c5tw": c5tw,
                    "c6dspc": c6dspc,
                    "c6dspct": c6dspct,
                    "c6fplpm": c6fplpm,
                    "c6intel": c6intel,
                    "c6laser": c6laser,
                    "c6longpm": c6longpm,
                    "c6tnr3": c6tnr3,
                    "c7elang2": c7elang2,
                    "c7in3p": c7in3p,
                    "c7tnor": c7tnor,
                    "env": env,
                    "index": index,
                    "lat": lat,
                    "lon": lon,
                    "orginx": orginx,
                    "origin": origin,
                    "rc": rc,
                    "rr": rr,
                    "sz": sz,
                    "tno": tno,
                    "trk_id": trk_id,
                    "twenv": twenv,
                },
                mission_assignment_update_params.MissionAssignmentUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        *,
        ts: Union[str, datetime],
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[MissionAssignmentListResponse, AsyncOffsetPage[MissionAssignmentListResponse]]:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          ts: the timestamp of the mission data, in ISO 8601 UTC format.
              (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/missionassignment",
            page=AsyncOffsetPage[MissionAssignmentListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "ts": ts,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    mission_assignment_list_params.MissionAssignmentListParams,
                ),
            ),
            model=MissionAssignmentListResponse,
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
        Service operation to delete a MissionAssignment object specified by the passed
        ID path parameter. A specific role is required to perform this service
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
            f"/udl/missionassignment/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def count(
        self,
        *,
        ts: Union[str, datetime],
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
          ts: the timestamp of the mission data, in ISO 8601 UTC format.
              (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return await self._get(
            "/udl/missionassignment/count",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "ts": ts,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    mission_assignment_count_params.MissionAssignmentCountParams,
                ),
            ),
            cast_to=str,
        )

    async def create_bulk(
        self,
        *,
        body: Iterable[mission_assignment_create_bulk_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take multiple MissionAssignments as a POST body and ingest
        into the database. A specific role is required to perform this service
        operation. Please contact the UDL team for assistance.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/udl/missionassignment/createBulk",
            body=await async_maybe_transform(body, Iterable[mission_assignment_create_bulk_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
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
    ) -> MissionAssignmentGetResponse:
        """
        Service operation to get a single MissionAssignment record by its unique ID
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
            f"/udl/missionassignment/{id}",
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
                    mission_assignment_get_params.MissionAssignmentGetParams,
                ),
            ),
            cast_to=MissionAssignmentGetResponse,
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
    ) -> MissionAssignmentQueryhelpResponse:
        """
        Service operation to provide detailed information on available dynamic query
        parameters for a particular data type.
        """
        return await self._get(
            "/udl/missionassignment/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MissionAssignmentQueryhelpResponse,
        )

    async def tuple(
        self,
        *,
        columns: str,
        ts: Union[str, datetime],
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MissionAssignmentTupleResponse:
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

          ts: the timestamp of the mission data, in ISO 8601 UTC format.
              (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/udl/missionassignment/tuple",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "columns": columns,
                        "ts": ts,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    mission_assignment_tuple_params.MissionAssignmentTupleParams,
                ),
            ),
            cast_to=MissionAssignmentTupleResponse,
        )


class MissionAssignmentResourceWithRawResponse:
    def __init__(self, mission_assignment: MissionAssignmentResource) -> None:
        self._mission_assignment = mission_assignment

        self.create = to_raw_response_wrapper(
            mission_assignment.create,
        )
        self.update = to_raw_response_wrapper(
            mission_assignment.update,
        )
        self.list = to_raw_response_wrapper(
            mission_assignment.list,
        )
        self.delete = to_raw_response_wrapper(
            mission_assignment.delete,
        )
        self.count = to_raw_response_wrapper(
            mission_assignment.count,
        )
        self.create_bulk = to_raw_response_wrapper(
            mission_assignment.create_bulk,
        )
        self.get = to_raw_response_wrapper(
            mission_assignment.get,
        )
        self.queryhelp = to_raw_response_wrapper(
            mission_assignment.queryhelp,
        )
        self.tuple = to_raw_response_wrapper(
            mission_assignment.tuple,
        )

    @cached_property
    def history(self) -> HistoryResourceWithRawResponse:
        return HistoryResourceWithRawResponse(self._mission_assignment.history)


class AsyncMissionAssignmentResourceWithRawResponse:
    def __init__(self, mission_assignment: AsyncMissionAssignmentResource) -> None:
        self._mission_assignment = mission_assignment

        self.create = async_to_raw_response_wrapper(
            mission_assignment.create,
        )
        self.update = async_to_raw_response_wrapper(
            mission_assignment.update,
        )
        self.list = async_to_raw_response_wrapper(
            mission_assignment.list,
        )
        self.delete = async_to_raw_response_wrapper(
            mission_assignment.delete,
        )
        self.count = async_to_raw_response_wrapper(
            mission_assignment.count,
        )
        self.create_bulk = async_to_raw_response_wrapper(
            mission_assignment.create_bulk,
        )
        self.get = async_to_raw_response_wrapper(
            mission_assignment.get,
        )
        self.queryhelp = async_to_raw_response_wrapper(
            mission_assignment.queryhelp,
        )
        self.tuple = async_to_raw_response_wrapper(
            mission_assignment.tuple,
        )

    @cached_property
    def history(self) -> AsyncHistoryResourceWithRawResponse:
        return AsyncHistoryResourceWithRawResponse(self._mission_assignment.history)


class MissionAssignmentResourceWithStreamingResponse:
    def __init__(self, mission_assignment: MissionAssignmentResource) -> None:
        self._mission_assignment = mission_assignment

        self.create = to_streamed_response_wrapper(
            mission_assignment.create,
        )
        self.update = to_streamed_response_wrapper(
            mission_assignment.update,
        )
        self.list = to_streamed_response_wrapper(
            mission_assignment.list,
        )
        self.delete = to_streamed_response_wrapper(
            mission_assignment.delete,
        )
        self.count = to_streamed_response_wrapper(
            mission_assignment.count,
        )
        self.create_bulk = to_streamed_response_wrapper(
            mission_assignment.create_bulk,
        )
        self.get = to_streamed_response_wrapper(
            mission_assignment.get,
        )
        self.queryhelp = to_streamed_response_wrapper(
            mission_assignment.queryhelp,
        )
        self.tuple = to_streamed_response_wrapper(
            mission_assignment.tuple,
        )

    @cached_property
    def history(self) -> HistoryResourceWithStreamingResponse:
        return HistoryResourceWithStreamingResponse(self._mission_assignment.history)


class AsyncMissionAssignmentResourceWithStreamingResponse:
    def __init__(self, mission_assignment: AsyncMissionAssignmentResource) -> None:
        self._mission_assignment = mission_assignment

        self.create = async_to_streamed_response_wrapper(
            mission_assignment.create,
        )
        self.update = async_to_streamed_response_wrapper(
            mission_assignment.update,
        )
        self.list = async_to_streamed_response_wrapper(
            mission_assignment.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            mission_assignment.delete,
        )
        self.count = async_to_streamed_response_wrapper(
            mission_assignment.count,
        )
        self.create_bulk = async_to_streamed_response_wrapper(
            mission_assignment.create_bulk,
        )
        self.get = async_to_streamed_response_wrapper(
            mission_assignment.get,
        )
        self.queryhelp = async_to_streamed_response_wrapper(
            mission_assignment.queryhelp,
        )
        self.tuple = async_to_streamed_response_wrapper(
            mission_assignment.tuple,
        )

    @cached_property
    def history(self) -> AsyncHistoryResourceWithStreamingResponse:
        return AsyncHistoryResourceWithStreamingResponse(self._mission_assignment.history)
