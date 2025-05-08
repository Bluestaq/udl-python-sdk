# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from datetime import datetime
from typing_extensions import Literal

import httpx

from ...types import (
    elset_list_params,
    elset_count_params,
    elset_tuple_params,
    elset_create_params,
    elset_retrieve_params,
    elset_create_bulk_params,
    elset_create_bulk_from_tle_params,
)
from .current import (
    CurrentResource,
    AsyncCurrentResource,
    CurrentResourceWithRawResponse,
    AsyncCurrentResourceWithRawResponse,
    CurrentResourceWithStreamingResponse,
    AsyncCurrentResourceWithStreamingResponse,
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
from ...types.elset import Elset
from ..._base_client import AsyncPaginator, make_request_options
from ...types.elset_abridged import ElsetAbridged
from ...types.elset_ingest_param import ElsetIngestParam
from ...types.elset_tuple_response import ElsetTupleResponse

__all__ = ["ElsetsResource", "AsyncElsetsResource"]


class ElsetsResource(SyncAPIResource):
    @cached_property
    def current(self) -> CurrentResource:
        return CurrentResource(self._client)

    @cached_property
    def history(self) -> HistoryResource:
        return HistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> ElsetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return ElsetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ElsetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return ElsetsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        epoch: Union[str, datetime],
        source: str,
        agom: float | NotGiven = NOT_GIVEN,
        algorithm: str | NotGiven = NOT_GIVEN,
        apogee: float | NotGiven = NOT_GIVEN,
        arg_of_perigee: float | NotGiven = NOT_GIVEN,
        ballistic_coeff: float | NotGiven = NOT_GIVEN,
        b_star: float | NotGiven = NOT_GIVEN,
        descriptor: str | NotGiven = NOT_GIVEN,
        eccentricity: float | NotGiven = NOT_GIVEN,
        ephem_type: int | NotGiven = NOT_GIVEN,
        id_elset: str | NotGiven = NOT_GIVEN,
        id_orbit_determination: str | NotGiven = NOT_GIVEN,
        inclination: float | NotGiven = NOT_GIVEN,
        mean_anomaly: float | NotGiven = NOT_GIVEN,
        mean_motion: float | NotGiven = NOT_GIVEN,
        mean_motion_d_dot: float | NotGiven = NOT_GIVEN,
        mean_motion_dot: float | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        orig_object_id: str | NotGiven = NOT_GIVEN,
        perigee: float | NotGiven = NOT_GIVEN,
        period: float | NotGiven = NOT_GIVEN,
        raan: float | NotGiven = NOT_GIVEN,
        raw_file_uri: str | NotGiven = NOT_GIVEN,
        rev_no: int | NotGiven = NOT_GIVEN,
        sat_no: int | NotGiven = NOT_GIVEN,
        semi_major_axis: float | NotGiven = NOT_GIVEN,
        sourced_data: List[str] | NotGiven = NOT_GIVEN,
        sourced_data_types: List[Literal["EO", "RADAR", "RF", "DOA", "ELSET", "SV"]] | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        transaction_id: str | NotGiven = NOT_GIVEN,
        uct: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single elset as a POST body and ingest into the
        database. This operation is not intended to be used for automated feeds into
        UDL. Data providers should contact the UDL team for specific role assignments
        and for instructions on setting up a permanent feed through an alternate
        mechanism.

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

          epoch: Elset epoch time in ISO 8601 UTC format, with microsecond precision.

          source: Source of the data.

          agom: AGOM, expressed in m^2/kg, is the value of the (averaged) object Area times the
              solar radiation pressure coefficient(Gamma) over the object Mass. Applicable
              only with ephemType4.

          algorithm: Optional algorithm used to produce this record.

          apogee: The orbit point furthest from the center of the earth in kilometers. If not
              provided, apogee will be computed from the TLE according to the following. Using
              mu, the standard gravitational parameter for the earth (398600.4418), semi-major
              axis A = (mu/(n _ 2 _ pi/(24*3600))^2)(1/3). Using semi-major axis A,
              eccentricity E, apogee = (A * (1 + E)) in km. Note that the calculations are for
              computing the apogee radius from the center of the earth, to compute apogee
              altitude the radius of the earth should be subtracted (6378.135 km).

          arg_of_perigee: The argument of perigee is the angle in degrees formed between the perigee and
              the ascending node. If the perigee would occur at the ascending node, the
              argument of perigee would be 0.

          ballistic_coeff: Ballistic coefficient, in m^2/kg. Applicable only with ephemType4.

          b_star: The drag term for SGP4 orbital model, used for calculating decay constants for
              altitude, eccentricity etc, measured in inverse earth radii.

          descriptor: Optional source-provided and searchable metadata or descriptor of the data.

          eccentricity: The orbital eccentricity of an astronomical object is a parameter that
              determines the amount by which its orbit around another body deviates from a
              perfect circle. A value of 0 is a circular orbit, values between 0 and 1 form an
              elliptic orbit, 1 is a parabolic escape orbit, and greater than 1 is a
              hyperbolic escape orbit.

          ephem_type:
              The ephemeris type associated with this TLE:

              0:&nbsp;SGP (or SGP4 with Kozai mean motion)

              1:&nbsp;SGP (Kozai mean motion)

              2:&nbsp;SGP4 (Brouver mean motion)

              3:&nbsp;SDP4

              4:&nbsp;SGP4-XP

              5:&nbsp;SDP8

              6:&nbsp;SP (osculating mean motion)

          id_elset: Unique identifier of the record, auto-generated by the system.

          id_orbit_determination: Unique identifier of the OD solution record that produced this elset. This ID
              can be used to obtain additional information on an OrbitDetermination object
              using the 'get by ID' operation (e.g. /udl/orbitdetermination/{id}). For
              example, the OrbitDetermination with idOrbitDetermination = abc would be queried
              as /udl/orbitdetermination/abc.

          inclination: The angle between the equator and the orbit when looking from the center of the
              Earth. If the orbit went exactly around the equator from left to right, then the
              inclination would be 0. The inclination ranges from 0 to 180 degrees.

          mean_anomaly: Where the satellite is in its orbital path. The mean anomaly ranges from 0 to
              360 degrees. The mean anomaly is referenced to the perigee. If the satellite
              were at the perigee, the mean anomaly would be 0.

          mean_motion: Mean motion is the angular speed required for a body to complete one orbit,
              assuming constant speed in a circular orbit which completes in the same time as
              the variable speed, elliptical orbit of the actual body. Measured in revolutions
              per day.

          mean_motion_d_dot: 2nd derivative of the mean motion with respect to time. Units are revolutions
              per day cubed.

          mean_motion_dot: 1st derivative of the mean motion with respect to time. Units are revolutions
              per day squared.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          orig_object_id: Optional identifier provided by elset source to indicate the target onorbit
              object of this elset. This may be an internal identifier and not necessarily map
              to a valid satellite number.

          perigee: The orbit point nearest to the center of the earth in kilometers. If not
              provided, perigee will be computed from the TLE according to the following.
              Using mu, the standard gravitational parameter for the earth (398600.4418),
              semi-major axis A = (mu/(n _ 2 _ pi/(24*3600))^2)(1/3). Using semi-major axis A,
              eccentricity E, perigee = (A * (1 - E)) in km. Note that the calculations are
              for computing the perigee radius from the center of the earth, to compute
              perigee altitude the radius of the earth should be subtracted (6378.135 km).

          period: Period of the orbit equal to inverse of mean motion, in minutes.

          raan: Right ascension of the ascending node, or RAAN is the angle as measured in
              degrees eastwards (or, as seen from the north, counterclockwise) from the First
              Point of Aries to the ascending node, which is where the orbit crosses the
              equator when traveling north.

          raw_file_uri: Optional URI location in the document repository of the raw file parsed by the
              system to produce this record. To download the raw file, prepend
              https://udl-hostname/scs/download?id= to this value.

          rev_no: The current revolution number. The value is incremented when a satellite crosses
              the equator on an ascending pass.

          sat_no: Satellite/catalog number of the target on-orbit object.

          semi_major_axis: The sum of the periapsis and apoapsis distances divided by two. For circular
              orbits, the semimajor axis is the distance between the centers of the bodies,
              not the distance of the bodies from the center of mass. Units are kilometers.

          sourced_data: Optional array of UDL data (observation) UUIDs used to build this element set.
              See the associated sourcedDataTypes array for the specific types of observations
              for the positionally corresponding UUIDs in this array (the two arrays must
              match in size).

          sourced_data_types: Optional array of UDL observation data types used to build this element set
              (e.g. EO, RADAR, RF, DOA). See the associated sourcedData array for the specific
              UUIDs of observations for the positionally corresponding data types in this
              array (the two arrays must match in size).

          tags: Optional array of provider/source specific tags for this data, where each
              element is no longer than 32 characters, used for implementing data owner
              conditional access controls to restrict access to the data. Should be left null
              by data providers unless conditional access controls are coordinated with the
              UDL team.

          transaction_id: Optional identifier to track a commercial or marketplace transaction executed to
              produce this data.

          uct: Boolean indicating this Elset was unable to be correlated to a known object.
              This flag should only be set to true by data providers after an attempt to
              correlate to an on-orbit object was made and failed. If unable to correlate, the
              'origObjectId' field may be populated with an internal data provider specific
              identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/udl/elset",
            body=maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "epoch": epoch,
                    "source": source,
                    "agom": agom,
                    "algorithm": algorithm,
                    "apogee": apogee,
                    "arg_of_perigee": arg_of_perigee,
                    "ballistic_coeff": ballistic_coeff,
                    "b_star": b_star,
                    "descriptor": descriptor,
                    "eccentricity": eccentricity,
                    "ephem_type": ephem_type,
                    "id_elset": id_elset,
                    "id_orbit_determination": id_orbit_determination,
                    "inclination": inclination,
                    "mean_anomaly": mean_anomaly,
                    "mean_motion": mean_motion,
                    "mean_motion_d_dot": mean_motion_d_dot,
                    "mean_motion_dot": mean_motion_dot,
                    "origin": origin,
                    "orig_object_id": orig_object_id,
                    "perigee": perigee,
                    "period": period,
                    "raan": raan,
                    "raw_file_uri": raw_file_uri,
                    "rev_no": rev_no,
                    "sat_no": sat_no,
                    "semi_major_axis": semi_major_axis,
                    "sourced_data": sourced_data,
                    "sourced_data_types": sourced_data_types,
                    "tags": tags,
                    "transaction_id": transaction_id,
                    "uct": uct,
                },
                elset_create_params.ElsetCreateParams,
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
    ) -> Elset:
        """
        Service operation to get a single elset by its unique ID passed as a path
        parameter.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/udl/elset/{id}",
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
                    elset_retrieve_params.ElsetRetrieveParams,
                ),
            ),
            cast_to=Elset,
        )

    def list(
        self,
        *,
        epoch: Union[str, datetime],
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncOffsetPage[ElsetAbridged]:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          epoch: Elset epoch time in ISO 8601 UTC format, with microsecond precision.
              (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/elset",
            page=SyncOffsetPage[ElsetAbridged],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "epoch": epoch,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    elset_list_params.ElsetListParams,
                ),
            ),
            model=ElsetAbridged,
        )

    def count(
        self,
        *,
        epoch: Union[str, datetime],
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
          epoch: Elset epoch time in ISO 8601 UTC format, with microsecond precision.
              (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return self._get(
            "/udl/elset/count",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "epoch": epoch,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    elset_count_params.ElsetCountParams,
                ),
            ),
            cast_to=str,
        )

    def create_bulk(
        self,
        *,
        body: Iterable[ElsetIngestParam],
        dupe_check: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation intended for initial integration only, to take a list of
        elsets as a POST body and ingest into the database with or without dupe
        detection. Default is no dupe checking. This operation is not intended to be
        used for automated feeds into UDL. Data providers should contact the UDL team
        for specific role assignments and for instructions on setting up a permanent
        feed through an alternate mechanism.

        Args:
          dupe_check: Boolean indicating if these elsets should be checked for duplicates, default is
              not to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/udl/elset/createBulk",
            body=maybe_transform(body, Iterable[ElsetIngestParam]),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"dupe_check": dupe_check}, elset_create_bulk_params.ElsetCreateBulkParams),
            ),
            cast_to=NoneType,
        )

    def create_bulk_from_tle(
        self,
        *,
        data_mode: str,
        make_current: bool,
        source: str,
        body: str,
        auto_create_sats: bool | NotGiven = NOT_GIVEN,
        control: str | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        tags: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a multiple TLEs as a POST body and ingest into the
        database. This operation is not intended to be used for automated feeds into
        UDL. Data providers should contact the UDL team for specific role assignments
        and for instructions on setting up a permanent feed through an alternate
        mechanism.

        Args:
          data_mode: Data mode of the passed elsets (REAL, TEST, etc).

          make_current: Boolean indicating if these elsets should be set as the 'current' for their
              corresponding on-orbit/satellite numbers.

          source: Source of the elset data.

          auto_create_sats: Boolean indicating if a shell Onorbit/satellite should be created if the passed
              satellite number doesn't exist.

          control: Dissemination control of the passed elsets (e.g. to support tagging with
              proprietary markings).

          origin: Origin of the elset data.

          tags: Optional comma-delineated list of provider/source specific tags for this data,
              where each element is no longer than 32 characters, used for implementing data
              owner conditional access controls to restrict access to the data. Should be left
              null by data providers unless conditional access controls are coordinated with
              the UDL team.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/udl/elset/createBulkFromTLE",
            body=maybe_transform(body, elset_create_bulk_from_tle_params.ElsetCreateBulkFromTleParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "data_mode": data_mode,
                        "make_current": make_current,
                        "source": source,
                        "auto_create_sats": auto_create_sats,
                        "control": control,
                        "origin": origin,
                        "tags": tags,
                    },
                    elset_create_bulk_from_tle_params.ElsetCreateBulkFromTleParams,
                ),
            ),
            cast_to=NoneType,
        )

    def query_current_elset_help(
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
            "/udl/currentelset/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
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
            "/udl/elset/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def tuple(
        self,
        *,
        columns: str,
        epoch: Union[str, datetime],
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ElsetTupleResponse:
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

          epoch: Elset epoch time in ISO 8601 UTC format, with microsecond precision.
              (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/udl/elset/tuple",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "columns": columns,
                        "epoch": epoch,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    elset_tuple_params.ElsetTupleParams,
                ),
            ),
            cast_to=ElsetTupleResponse,
        )

    def unvalidated_publish(
        self,
        *,
        body: Iterable[ElsetIngestParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take elsets as a POST body and ingest into the database
        with or without dupe detection. Default is no dupe checking. This operation is
        intended to be used for automated feeds into UDL.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/filedrop/udl-elset",
            body=maybe_transform(body, Iterable[ElsetIngestParam]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncElsetsResource(AsyncAPIResource):
    @cached_property
    def current(self) -> AsyncCurrentResource:
        return AsyncCurrentResource(self._client)

    @cached_property
    def history(self) -> AsyncHistoryResource:
        return AsyncHistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncElsetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncElsetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncElsetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncElsetsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        epoch: Union[str, datetime],
        source: str,
        agom: float | NotGiven = NOT_GIVEN,
        algorithm: str | NotGiven = NOT_GIVEN,
        apogee: float | NotGiven = NOT_GIVEN,
        arg_of_perigee: float | NotGiven = NOT_GIVEN,
        ballistic_coeff: float | NotGiven = NOT_GIVEN,
        b_star: float | NotGiven = NOT_GIVEN,
        descriptor: str | NotGiven = NOT_GIVEN,
        eccentricity: float | NotGiven = NOT_GIVEN,
        ephem_type: int | NotGiven = NOT_GIVEN,
        id_elset: str | NotGiven = NOT_GIVEN,
        id_orbit_determination: str | NotGiven = NOT_GIVEN,
        inclination: float | NotGiven = NOT_GIVEN,
        mean_anomaly: float | NotGiven = NOT_GIVEN,
        mean_motion: float | NotGiven = NOT_GIVEN,
        mean_motion_d_dot: float | NotGiven = NOT_GIVEN,
        mean_motion_dot: float | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        orig_object_id: str | NotGiven = NOT_GIVEN,
        perigee: float | NotGiven = NOT_GIVEN,
        period: float | NotGiven = NOT_GIVEN,
        raan: float | NotGiven = NOT_GIVEN,
        raw_file_uri: str | NotGiven = NOT_GIVEN,
        rev_no: int | NotGiven = NOT_GIVEN,
        sat_no: int | NotGiven = NOT_GIVEN,
        semi_major_axis: float | NotGiven = NOT_GIVEN,
        sourced_data: List[str] | NotGiven = NOT_GIVEN,
        sourced_data_types: List[Literal["EO", "RADAR", "RF", "DOA", "ELSET", "SV"]] | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        transaction_id: str | NotGiven = NOT_GIVEN,
        uct: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single elset as a POST body and ingest into the
        database. This operation is not intended to be used for automated feeds into
        UDL. Data providers should contact the UDL team for specific role assignments
        and for instructions on setting up a permanent feed through an alternate
        mechanism.

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

          epoch: Elset epoch time in ISO 8601 UTC format, with microsecond precision.

          source: Source of the data.

          agom: AGOM, expressed in m^2/kg, is the value of the (averaged) object Area times the
              solar radiation pressure coefficient(Gamma) over the object Mass. Applicable
              only with ephemType4.

          algorithm: Optional algorithm used to produce this record.

          apogee: The orbit point furthest from the center of the earth in kilometers. If not
              provided, apogee will be computed from the TLE according to the following. Using
              mu, the standard gravitational parameter for the earth (398600.4418), semi-major
              axis A = (mu/(n _ 2 _ pi/(24*3600))^2)(1/3). Using semi-major axis A,
              eccentricity E, apogee = (A * (1 + E)) in km. Note that the calculations are for
              computing the apogee radius from the center of the earth, to compute apogee
              altitude the radius of the earth should be subtracted (6378.135 km).

          arg_of_perigee: The argument of perigee is the angle in degrees formed between the perigee and
              the ascending node. If the perigee would occur at the ascending node, the
              argument of perigee would be 0.

          ballistic_coeff: Ballistic coefficient, in m^2/kg. Applicable only with ephemType4.

          b_star: The drag term for SGP4 orbital model, used for calculating decay constants for
              altitude, eccentricity etc, measured in inverse earth radii.

          descriptor: Optional source-provided and searchable metadata or descriptor of the data.

          eccentricity: The orbital eccentricity of an astronomical object is a parameter that
              determines the amount by which its orbit around another body deviates from a
              perfect circle. A value of 0 is a circular orbit, values between 0 and 1 form an
              elliptic orbit, 1 is a parabolic escape orbit, and greater than 1 is a
              hyperbolic escape orbit.

          ephem_type:
              The ephemeris type associated with this TLE:

              0:&nbsp;SGP (or SGP4 with Kozai mean motion)

              1:&nbsp;SGP (Kozai mean motion)

              2:&nbsp;SGP4 (Brouver mean motion)

              3:&nbsp;SDP4

              4:&nbsp;SGP4-XP

              5:&nbsp;SDP8

              6:&nbsp;SP (osculating mean motion)

          id_elset: Unique identifier of the record, auto-generated by the system.

          id_orbit_determination: Unique identifier of the OD solution record that produced this elset. This ID
              can be used to obtain additional information on an OrbitDetermination object
              using the 'get by ID' operation (e.g. /udl/orbitdetermination/{id}). For
              example, the OrbitDetermination with idOrbitDetermination = abc would be queried
              as /udl/orbitdetermination/abc.

          inclination: The angle between the equator and the orbit when looking from the center of the
              Earth. If the orbit went exactly around the equator from left to right, then the
              inclination would be 0. The inclination ranges from 0 to 180 degrees.

          mean_anomaly: Where the satellite is in its orbital path. The mean anomaly ranges from 0 to
              360 degrees. The mean anomaly is referenced to the perigee. If the satellite
              were at the perigee, the mean anomaly would be 0.

          mean_motion: Mean motion is the angular speed required for a body to complete one orbit,
              assuming constant speed in a circular orbit which completes in the same time as
              the variable speed, elliptical orbit of the actual body. Measured in revolutions
              per day.

          mean_motion_d_dot: 2nd derivative of the mean motion with respect to time. Units are revolutions
              per day cubed.

          mean_motion_dot: 1st derivative of the mean motion with respect to time. Units are revolutions
              per day squared.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          orig_object_id: Optional identifier provided by elset source to indicate the target onorbit
              object of this elset. This may be an internal identifier and not necessarily map
              to a valid satellite number.

          perigee: The orbit point nearest to the center of the earth in kilometers. If not
              provided, perigee will be computed from the TLE according to the following.
              Using mu, the standard gravitational parameter for the earth (398600.4418),
              semi-major axis A = (mu/(n _ 2 _ pi/(24*3600))^2)(1/3). Using semi-major axis A,
              eccentricity E, perigee = (A * (1 - E)) in km. Note that the calculations are
              for computing the perigee radius from the center of the earth, to compute
              perigee altitude the radius of the earth should be subtracted (6378.135 km).

          period: Period of the orbit equal to inverse of mean motion, in minutes.

          raan: Right ascension of the ascending node, or RAAN is the angle as measured in
              degrees eastwards (or, as seen from the north, counterclockwise) from the First
              Point of Aries to the ascending node, which is where the orbit crosses the
              equator when traveling north.

          raw_file_uri: Optional URI location in the document repository of the raw file parsed by the
              system to produce this record. To download the raw file, prepend
              https://udl-hostname/scs/download?id= to this value.

          rev_no: The current revolution number. The value is incremented when a satellite crosses
              the equator on an ascending pass.

          sat_no: Satellite/catalog number of the target on-orbit object.

          semi_major_axis: The sum of the periapsis and apoapsis distances divided by two. For circular
              orbits, the semimajor axis is the distance between the centers of the bodies,
              not the distance of the bodies from the center of mass. Units are kilometers.

          sourced_data: Optional array of UDL data (observation) UUIDs used to build this element set.
              See the associated sourcedDataTypes array for the specific types of observations
              for the positionally corresponding UUIDs in this array (the two arrays must
              match in size).

          sourced_data_types: Optional array of UDL observation data types used to build this element set
              (e.g. EO, RADAR, RF, DOA). See the associated sourcedData array for the specific
              UUIDs of observations for the positionally corresponding data types in this
              array (the two arrays must match in size).

          tags: Optional array of provider/source specific tags for this data, where each
              element is no longer than 32 characters, used for implementing data owner
              conditional access controls to restrict access to the data. Should be left null
              by data providers unless conditional access controls are coordinated with the
              UDL team.

          transaction_id: Optional identifier to track a commercial or marketplace transaction executed to
              produce this data.

          uct: Boolean indicating this Elset was unable to be correlated to a known object.
              This flag should only be set to true by data providers after an attempt to
              correlate to an on-orbit object was made and failed. If unable to correlate, the
              'origObjectId' field may be populated with an internal data provider specific
              identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/udl/elset",
            body=await async_maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "epoch": epoch,
                    "source": source,
                    "agom": agom,
                    "algorithm": algorithm,
                    "apogee": apogee,
                    "arg_of_perigee": arg_of_perigee,
                    "ballistic_coeff": ballistic_coeff,
                    "b_star": b_star,
                    "descriptor": descriptor,
                    "eccentricity": eccentricity,
                    "ephem_type": ephem_type,
                    "id_elset": id_elset,
                    "id_orbit_determination": id_orbit_determination,
                    "inclination": inclination,
                    "mean_anomaly": mean_anomaly,
                    "mean_motion": mean_motion,
                    "mean_motion_d_dot": mean_motion_d_dot,
                    "mean_motion_dot": mean_motion_dot,
                    "origin": origin,
                    "orig_object_id": orig_object_id,
                    "perigee": perigee,
                    "period": period,
                    "raan": raan,
                    "raw_file_uri": raw_file_uri,
                    "rev_no": rev_no,
                    "sat_no": sat_no,
                    "semi_major_axis": semi_major_axis,
                    "sourced_data": sourced_data,
                    "sourced_data_types": sourced_data_types,
                    "tags": tags,
                    "transaction_id": transaction_id,
                    "uct": uct,
                },
                elset_create_params.ElsetCreateParams,
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
    ) -> Elset:
        """
        Service operation to get a single elset by its unique ID passed as a path
        parameter.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/udl/elset/{id}",
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
                    elset_retrieve_params.ElsetRetrieveParams,
                ),
            ),
            cast_to=Elset,
        )

    def list(
        self,
        *,
        epoch: Union[str, datetime],
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[ElsetAbridged, AsyncOffsetPage[ElsetAbridged]]:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          epoch: Elset epoch time in ISO 8601 UTC format, with microsecond precision.
              (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/elset",
            page=AsyncOffsetPage[ElsetAbridged],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "epoch": epoch,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    elset_list_params.ElsetListParams,
                ),
            ),
            model=ElsetAbridged,
        )

    async def count(
        self,
        *,
        epoch: Union[str, datetime],
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
          epoch: Elset epoch time in ISO 8601 UTC format, with microsecond precision.
              (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return await self._get(
            "/udl/elset/count",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "epoch": epoch,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    elset_count_params.ElsetCountParams,
                ),
            ),
            cast_to=str,
        )

    async def create_bulk(
        self,
        *,
        body: Iterable[ElsetIngestParam],
        dupe_check: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation intended for initial integration only, to take a list of
        elsets as a POST body and ingest into the database with or without dupe
        detection. Default is no dupe checking. This operation is not intended to be
        used for automated feeds into UDL. Data providers should contact the UDL team
        for specific role assignments and for instructions on setting up a permanent
        feed through an alternate mechanism.

        Args:
          dupe_check: Boolean indicating if these elsets should be checked for duplicates, default is
              not to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/udl/elset/createBulk",
            body=await async_maybe_transform(body, Iterable[ElsetIngestParam]),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"dupe_check": dupe_check}, elset_create_bulk_params.ElsetCreateBulkParams
                ),
            ),
            cast_to=NoneType,
        )

    async def create_bulk_from_tle(
        self,
        *,
        data_mode: str,
        make_current: bool,
        source: str,
        body: str,
        auto_create_sats: bool | NotGiven = NOT_GIVEN,
        control: str | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        tags: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a multiple TLEs as a POST body and ingest into the
        database. This operation is not intended to be used for automated feeds into
        UDL. Data providers should contact the UDL team for specific role assignments
        and for instructions on setting up a permanent feed through an alternate
        mechanism.

        Args:
          data_mode: Data mode of the passed elsets (REAL, TEST, etc).

          make_current: Boolean indicating if these elsets should be set as the 'current' for their
              corresponding on-orbit/satellite numbers.

          source: Source of the elset data.

          auto_create_sats: Boolean indicating if a shell Onorbit/satellite should be created if the passed
              satellite number doesn't exist.

          control: Dissemination control of the passed elsets (e.g. to support tagging with
              proprietary markings).

          origin: Origin of the elset data.

          tags: Optional comma-delineated list of provider/source specific tags for this data,
              where each element is no longer than 32 characters, used for implementing data
              owner conditional access controls to restrict access to the data. Should be left
              null by data providers unless conditional access controls are coordinated with
              the UDL team.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/udl/elset/createBulkFromTLE",
            body=await async_maybe_transform(body, elset_create_bulk_from_tle_params.ElsetCreateBulkFromTleParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "data_mode": data_mode,
                        "make_current": make_current,
                        "source": source,
                        "auto_create_sats": auto_create_sats,
                        "control": control,
                        "origin": origin,
                        "tags": tags,
                    },
                    elset_create_bulk_from_tle_params.ElsetCreateBulkFromTleParams,
                ),
            ),
            cast_to=NoneType,
        )

    async def query_current_elset_help(
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
            "/udl/currentelset/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
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
            "/udl/elset/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def tuple(
        self,
        *,
        columns: str,
        epoch: Union[str, datetime],
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ElsetTupleResponse:
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

          epoch: Elset epoch time in ISO 8601 UTC format, with microsecond precision.
              (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/udl/elset/tuple",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "columns": columns,
                        "epoch": epoch,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    elset_tuple_params.ElsetTupleParams,
                ),
            ),
            cast_to=ElsetTupleResponse,
        )

    async def unvalidated_publish(
        self,
        *,
        body: Iterable[ElsetIngestParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take elsets as a POST body and ingest into the database
        with or without dupe detection. Default is no dupe checking. This operation is
        intended to be used for automated feeds into UDL.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/filedrop/udl-elset",
            body=await async_maybe_transform(body, Iterable[ElsetIngestParam]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class ElsetsResourceWithRawResponse:
    def __init__(self, elsets: ElsetsResource) -> None:
        self._elsets = elsets

        self.create = to_raw_response_wrapper(
            elsets.create,
        )
        self.retrieve = to_raw_response_wrapper(
            elsets.retrieve,
        )
        self.list = to_raw_response_wrapper(
            elsets.list,
        )
        self.count = to_raw_response_wrapper(
            elsets.count,
        )
        self.create_bulk = to_raw_response_wrapper(
            elsets.create_bulk,
        )
        self.create_bulk_from_tle = to_raw_response_wrapper(
            elsets.create_bulk_from_tle,
        )
        self.query_current_elset_help = to_raw_response_wrapper(
            elsets.query_current_elset_help,
        )
        self.queryhelp = to_raw_response_wrapper(
            elsets.queryhelp,
        )
        self.tuple = to_raw_response_wrapper(
            elsets.tuple,
        )
        self.unvalidated_publish = to_raw_response_wrapper(
            elsets.unvalidated_publish,
        )

    @cached_property
    def current(self) -> CurrentResourceWithRawResponse:
        return CurrentResourceWithRawResponse(self._elsets.current)

    @cached_property
    def history(self) -> HistoryResourceWithRawResponse:
        return HistoryResourceWithRawResponse(self._elsets.history)


class AsyncElsetsResourceWithRawResponse:
    def __init__(self, elsets: AsyncElsetsResource) -> None:
        self._elsets = elsets

        self.create = async_to_raw_response_wrapper(
            elsets.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            elsets.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            elsets.list,
        )
        self.count = async_to_raw_response_wrapper(
            elsets.count,
        )
        self.create_bulk = async_to_raw_response_wrapper(
            elsets.create_bulk,
        )
        self.create_bulk_from_tle = async_to_raw_response_wrapper(
            elsets.create_bulk_from_tle,
        )
        self.query_current_elset_help = async_to_raw_response_wrapper(
            elsets.query_current_elset_help,
        )
        self.queryhelp = async_to_raw_response_wrapper(
            elsets.queryhelp,
        )
        self.tuple = async_to_raw_response_wrapper(
            elsets.tuple,
        )
        self.unvalidated_publish = async_to_raw_response_wrapper(
            elsets.unvalidated_publish,
        )

    @cached_property
    def current(self) -> AsyncCurrentResourceWithRawResponse:
        return AsyncCurrentResourceWithRawResponse(self._elsets.current)

    @cached_property
    def history(self) -> AsyncHistoryResourceWithRawResponse:
        return AsyncHistoryResourceWithRawResponse(self._elsets.history)


class ElsetsResourceWithStreamingResponse:
    def __init__(self, elsets: ElsetsResource) -> None:
        self._elsets = elsets

        self.create = to_streamed_response_wrapper(
            elsets.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            elsets.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            elsets.list,
        )
        self.count = to_streamed_response_wrapper(
            elsets.count,
        )
        self.create_bulk = to_streamed_response_wrapper(
            elsets.create_bulk,
        )
        self.create_bulk_from_tle = to_streamed_response_wrapper(
            elsets.create_bulk_from_tle,
        )
        self.query_current_elset_help = to_streamed_response_wrapper(
            elsets.query_current_elset_help,
        )
        self.queryhelp = to_streamed_response_wrapper(
            elsets.queryhelp,
        )
        self.tuple = to_streamed_response_wrapper(
            elsets.tuple,
        )
        self.unvalidated_publish = to_streamed_response_wrapper(
            elsets.unvalidated_publish,
        )

    @cached_property
    def current(self) -> CurrentResourceWithStreamingResponse:
        return CurrentResourceWithStreamingResponse(self._elsets.current)

    @cached_property
    def history(self) -> HistoryResourceWithStreamingResponse:
        return HistoryResourceWithStreamingResponse(self._elsets.history)


class AsyncElsetsResourceWithStreamingResponse:
    def __init__(self, elsets: AsyncElsetsResource) -> None:
        self._elsets = elsets

        self.create = async_to_streamed_response_wrapper(
            elsets.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            elsets.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            elsets.list,
        )
        self.count = async_to_streamed_response_wrapper(
            elsets.count,
        )
        self.create_bulk = async_to_streamed_response_wrapper(
            elsets.create_bulk,
        )
        self.create_bulk_from_tle = async_to_streamed_response_wrapper(
            elsets.create_bulk_from_tle,
        )
        self.query_current_elset_help = async_to_streamed_response_wrapper(
            elsets.query_current_elset_help,
        )
        self.queryhelp = async_to_streamed_response_wrapper(
            elsets.queryhelp,
        )
        self.tuple = async_to_streamed_response_wrapper(
            elsets.tuple,
        )
        self.unvalidated_publish = async_to_streamed_response_wrapper(
            elsets.unvalidated_publish,
        )

    @cached_property
    def current(self) -> AsyncCurrentResourceWithStreamingResponse:
        return AsyncCurrentResourceWithStreamingResponse(self._elsets.current)

    @cached_property
    def history(self) -> AsyncHistoryResourceWithStreamingResponse:
        return AsyncHistoryResourceWithStreamingResponse(self._elsets.history)
