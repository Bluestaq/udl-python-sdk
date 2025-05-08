# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from datetime import datetime
from typing_extensions import Literal

import httpx

from ...types import (
    weather_report_get_params,
    weather_report_list_params,
    weather_report_count_params,
    weather_report_tuple_params,
    weather_report_create_params,
    weather_report_unvalidated_publish_params,
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
from ...types.weather_report_list_response import WeatherReportListResponse
from ...types.weather_report_tuple_response import WeatherReportTupleResponse
from ...types.weather_report.weather_report_full import WeatherReportFull

__all__ = ["WeatherReportResource", "AsyncWeatherReportResource"]


class WeatherReportResource(SyncAPIResource):
    @cached_property
    def history(self) -> HistoryResource:
        return HistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> WeatherReportResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return WeatherReportResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WeatherReportResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return WeatherReportResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        lat: float,
        lon: float,
        ob_time: Union[str, datetime],
        report_type: str,
        source: str,
        id: str | NotGiven = NOT_GIVEN,
        act_weather: str | NotGiven = NOT_GIVEN,
        agjson: str | NotGiven = NOT_GIVEN,
        alt: float | NotGiven = NOT_GIVEN,
        andims: int | NotGiven = NOT_GIVEN,
        area: str | NotGiven = NOT_GIVEN,
        asrid: int | NotGiven = NOT_GIVEN,
        atext: str | NotGiven = NOT_GIVEN,
        atype: str | NotGiven = NOT_GIVEN,
        bar_press: float | NotGiven = NOT_GIVEN,
        cc_event: bool | NotGiven = NOT_GIVEN,
        cloud_cover: List[str] | NotGiven = NOT_GIVEN,
        cloud_hght: Iterable[float] | NotGiven = NOT_GIVEN,
        contrail_hght_lower: float | NotGiven = NOT_GIVEN,
        contrail_hght_upper: float | NotGiven = NOT_GIVEN,
        data_level: str | NotGiven = NOT_GIVEN,
        dew_point: float | NotGiven = NOT_GIVEN,
        dif_rad: float | NotGiven = NOT_GIVEN,
        dir_dev: float | NotGiven = NOT_GIVEN,
        en_route_weather: str | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        external_location_id: str | NotGiven = NOT_GIVEN,
        forecast_end_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        forecast_start_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        geo_potential_alt: float | NotGiven = NOT_GIVEN,
        hshear: float | NotGiven = NOT_GIVEN,
        icao: str | NotGiven = NOT_GIVEN,
        icing_lower_limit: float | NotGiven = NOT_GIVEN,
        icing_upper_limit: float | NotGiven = NOT_GIVEN,
        id_airfield: str | NotGiven = NOT_GIVEN,
        id_ground_imagery: str | NotGiven = NOT_GIVEN,
        id_sensor: str | NotGiven = NOT_GIVEN,
        id_site: str | NotGiven = NOT_GIVEN,
        index_refraction: float | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        orig_sensor_id: str | NotGiven = NOT_GIVEN,
        precip_rate: float | NotGiven = NOT_GIVEN,
        qnh: float | NotGiven = NOT_GIVEN,
        rad_vel: float | NotGiven = NOT_GIVEN,
        rad_vel_beam1: float | NotGiven = NOT_GIVEN,
        rad_vel_beam2: float | NotGiven = NOT_GIVEN,
        rad_vel_beam3: float | NotGiven = NOT_GIVEN,
        rad_vel_beam4: float | NotGiven = NOT_GIVEN,
        rad_vel_beam5: float | NotGiven = NOT_GIVEN,
        rain_hour: float | NotGiven = NOT_GIVEN,
        raw_metar: str | NotGiven = NOT_GIVEN,
        raw_taf: str | NotGiven = NOT_GIVEN,
        ref_rad: float | NotGiven = NOT_GIVEN,
        rel_humidity: float | NotGiven = NOT_GIVEN,
        senalt: float | NotGiven = NOT_GIVEN,
        senlat: float | NotGiven = NOT_GIVEN,
        senlon: float | NotGiven = NOT_GIVEN,
        soil_moisture: float | NotGiven = NOT_GIVEN,
        soil_temp: float | NotGiven = NOT_GIVEN,
        solar_rad: float | NotGiven = NOT_GIVEN,
        src_ids: List[str] | NotGiven = NOT_GIVEN,
        src_typs: List[str] | NotGiven = NOT_GIVEN,
        surrounding_weather: str | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        visibility: float | NotGiven = NOT_GIVEN,
        vshear: float | NotGiven = NOT_GIVEN,
        weather_amp: str | NotGiven = NOT_GIVEN,
        weather_desc: str | NotGiven = NOT_GIVEN,
        weather_id: str | NotGiven = NOT_GIVEN,
        weather_int: str | NotGiven = NOT_GIVEN,
        wind_chill: float | NotGiven = NOT_GIVEN,
        wind_cov: Iterable[float] | NotGiven = NOT_GIVEN,
        wind_dir: float | NotGiven = NOT_GIVEN,
        wind_dir_avg: float | NotGiven = NOT_GIVEN,
        wind_dir_peak: float | NotGiven = NOT_GIVEN,
        wind_dir_peak10: float | NotGiven = NOT_GIVEN,
        wind_gust: float | NotGiven = NOT_GIVEN,
        wind_gust10: float | NotGiven = NOT_GIVEN,
        wind_spd: float | NotGiven = NOT_GIVEN,
        wind_spd_avg: float | NotGiven = NOT_GIVEN,
        wind_var: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single WeatherReport as a POST body and ingest into
        the database. A specific role is required to perform this service operation.
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

          lat: The central WGS-84 latitude of the weather report, in degrees. -90 to 90 degrees
              (negative values south of equator).

          lon: The central WGS-84 longitude of the weather report, in degrees. -180 to 180
              degrees (negative values west of Prime Meridian).

          ob_time: Datetime when a weather observation was made or forecast was issued in ISO 8601
              UTC datetime format with microsecond precision.

          report_type: Identifies the type of weather report (e.g. OBSERVATION, FORECAST, etc.).

          source: Source of the data.

          id: Unique identifier of the record, auto-generated by the system.

          act_weather: Describes the actual weather at position. Intended as, but not constrained to,
              MIL-STD-6016 actual weather (e.g. NO STATEMENT, NO SIGNIFICANT WEATHER, DRIZZLE,
              RAIN, SNOW, SNOW GRAINS, DIAMOND DUST, ICE PELLETS, HAIL, SMALL HAIL, MIST, FOG,
              SMOKE, VOLCANIC ASH, WIDESPREAD DUST, SAND, HAZE, WELL DEVELOPED DUST, SQUALLS,
              FUNNEL CLOUDS, SANDSTORM, DUSTSTORM, LOW CLOUDS, CLOUDY, GROUND FOG, DUST, HEAVY
              RAIN, THUNDERSTORMS AWT, HEAVY THUNDERSTORMS, HURRICANE TYPHOON CYCLONE,
              TROPICAL STORM, TORNADO, HIGH WINDS, LIGHTNING, FREEZING DRIZZLE, FREEZING RAIN,
              HEAVY SNOW, ICING, SNOW OR RAIN AND SNOW MIXED, SHOWERS, CLEAR).

          agjson: Geographical region or polygon (lat/lon pairs), as depicted by the GeoJSON
              representation of the geometry/geography, of the image as projected on the
              ground. GeoJSON Reference: https://geojson.org/. Ignored if included with a POST
              or PUT request that also specifies a valid 'area' or 'atext' field.

          alt: Point height above ellipsoid (WGS-84), in meters.

          andims: Number of dimensions of the geometry depicted by region.

          area: Optional geographical region or polygon (lat/lon pairs) of the area surrounding
              the point of interest as projected on the ground.

          asrid: Geographical spatial_ref_sys for region.

          atext: Geographical region or polygon (lon/lat pairs), as depicted by the Well-Known
              Text representation of the geometry/geography, of the image as projected on the
              ground. WKT reference: https://www.opengeospatial.org/standards/wkt-crs. Ignored
              if included with a POST or PUT request that also specifies a valid 'area' field.

          atype: Type of region as projected on the ground.

          bar_press: The measurement of air pressure in the atmosphere in kilopascals.

          cc_event: Flag indicating detection of a cloud-to-cloud lightning event.

          cloud_cover: Array of cloud cover descriptions - each element can be maximum of 16 characters
              long. Intended as, but not constrained to, MIL-STD-6016 cloud cover designations
              (e.g. SKY CLEAR, SCATTERED, BROKEN, OVERCAST, SKY OBSCURED). Each element of the
              array corresponds to the elements in the cloudHght array specified respectively.

          cloud_hght: Array of cloud base heights in meters described by the cloudHght array. Each
              element of the array corresponds to the elements in the cloudCover array
              specified respectively.

          contrail_hght_lower: Reports the lowest altitude at which contrails are occurring, in meters.

          contrail_hght_upper: Reports the highest altitude at which contrails are occurring, in meters.

          data_level: Specific pressures or heights where measurements are taken, labeled as either
              MANDATORY or SIGNIFICANT levels. Mandatory levels are at particular pressures at
              geopotential heights. Significant levels are at particular geometric heights.

          dew_point: The temperature at which air is saturated with water vapor, in degrees C.

          dif_rad: The amount of radiation that reaches earth's surface after being scattered by
              the atmosphere, in Watts per square meter.

          dir_dev: The difference in wind direction recorded over a period of time, in degrees.

          en_route_weather: Describes the flight conditions in route to the target (NO STATEMENT, MAINLY
              IFR, MAINLY VFR, THUNDERSTORMS).

              MAINLY IFR:&nbsp;&nbsp;Predominantly Instrument Flight Rules.

              MAINLY VFR:&nbsp;&nbsp;Predominantly Visual Flight Rules.

              THUNDERSTORMS:&nbsp;&nbsp;Thunderstorms expected in route.

          external_id: Optional observation or forecast ID from external systems. This field has no
              meaning within UDL and is provided as a convenience for systems that require
              tracking of an internal system generated ID.

          external_location_id: Optional location ID from external systems. This field has no meaning within UDL
              and is provided as a convenience for systems that require tracking of an
              internal system generated ID.

          forecast_end_time: Valid end time of a weather forecast in ISO 8601 UTC datetime format with
              millisecond precision.

          forecast_start_time: Valid start time of a weather forecast in ISO 8601 UTC datetime format with
              millisecond precision.

          geo_potential_alt: Altitude of a pressure surface in the atmosphere above mean sea level, in
              meters.

          hshear: The change in wind speed between two different lateral positions at a given
              altitude divided by the horizontal distance between them, in units of 1/sec.

          icao: The International Civil Aviation Organization (ICAO) code of the airfield
              associated with this weather report.

          icing_lower_limit: Reports the lowest altitude at which icing or freezing rain is occurring, in
              meters.

          icing_upper_limit: Reports the highest altitude at which icing or freezing rain is occurring, in
              meters.

          id_airfield: Identifier of the Airfield associated with this weather report.

          id_ground_imagery: Identifier of the ground imagery associated for this weather over target report.

          id_sensor: Unique identifier of the sensor making the weather measurement.

          id_site: Identifier of the Site that is associated with this weather report.

          index_refraction: An indication of how much the atmosphere refracts light.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          orig_sensor_id: Optional identifier provided by the record source. This may be an internal
              identifier and not necessarily a valid sensor ID.

          precip_rate: The speed at which water is being applied to a specific area in millimeters per
              hour.

          qnh: Altimeter set to read zero at mean sea level in kilopascals.

          rad_vel: Average radial velocity of wind as measured by radar with multi-beam
              configurations. Radial velocity is the component of wind velocity moving
              directly toward or away from a sensor's radar beam, in meters per second. Values
              can either be positive (wind is moving away from the radar) or negative (wind is
              moving toward the radar).

          rad_vel_beam1: Component of wind velocity moving directly toward or away from radar beam 1, in
              meters per second. Radial velocity values can either be positive (wind is moving
              away from the radar) or negative (wind is moving toward the radar). The beam
              number designation is defined by the data source.

          rad_vel_beam2: Component of wind velocity moving directly toward or away from radar beam 2, in
              meters per second. Radial velocity values can either be positive (wind is moving
              away from the radar) or negative (wind is moving toward the radar). The beam
              number designation is defined by the data source.

          rad_vel_beam3: Component of wind velocity moving directly toward or away from radar beam 3, in
              meters per second. Radial velocity values can either be positive (wind is moving
              away from the radar) or negative (wind is moving toward the radar). The beam
              number designation is defined by the data source.

          rad_vel_beam4: Component of wind velocity moving directly toward or away from radar beam 4, in
              meters per second. Radial velocity values can either be positive (wind is moving
              away from the radar) or negative (wind is moving toward the radar). The beam
              number designation is defined by the data source.

          rad_vel_beam5: Component of wind velocity moving directly toward or away from radar beam 5, in
              meters per second. Radial velocity values can either be positive (wind is moving
              away from the radar) or negative (wind is moving toward the radar). The beam
              number designation is defined by the data source.

          rain_hour: The amount of rain that has fallen in the past hour, in centimeters.

          raw_metar: The Raw Meteorological Aerodrome Report (METAR) string.

          raw_taf: Terminal Aerodrome Forecast (TAF) containing detailed weather predictions for a
              specific airport or aerodrome.

          ref_rad: The amount of radiation that changes direction as a function of atmospheric
              density, in Watts per square meter.

          rel_humidity: The percentage of water vapor in the atmosphere.

          senalt: Sensor altitude at obTime in km. This includes pilot reports or other means of
              weather observation.

          senlat: Sensor WGS84 latitude at obTime in degrees. -90 to 90 degrees (negative values
              south of equator). This includes pilot reports or other means of weather
              observation.

          senlon: Sensor WGS84 longitude at obTime in degrees. -180 to 180 degrees (negative
              values west of Prime Meridian). This includes pilot reports or other means of
              weather observation.

          soil_moisture: The volumetric percentage of soil water contained in a given volume of soil.

          soil_temp: The measurement of soil temperature in degrees C.

          solar_rad: The power per unit area received from the Sun in the form of electromagnetic
              radiation as measured in the wavelength range of the measuring instrument. The
              solar irradiance is measured in watt per square meter (W/m2).

          src_ids: Array of UUID(s) of the UDL data record(s) that are related to this
              WeatherReport record. See the associated 'srcTyps' array for the specific types
              of data, positionally corresponding to the UUIDs in this array. The 'srcTyps'
              and 'srcIds' arrays must match in size. See the corresponding srcTyps array
              element for the data type of the UUID and use the appropriate API operation to
              retrieve that object.

          src_typs: Array of UDL record types (SENSOR, WEATHERDATA) that are related to this
              WeatherReport record. See the associated 'srcIds' array for the record UUIDs,
              positionally corresponding to the record types in this array. The 'srcTyps' and
              'srcIds' arrays must match in size.

          surrounding_weather: Describes in which direction (if any) that better weather conditions exist.
              Intended as, but not constrained to, MIL-STD-6016 surrounding weather
              designations (e.g. NO STATEMENT, BETTER TO NORTH, BETTER TO EAST, BETTER TO
              SOUTH, BETTER TO WEST).

          temperature: The measurement of air temperature in degrees C.

          visibility: Visual distance in meters.

          vshear: The change in wind speed between two different altitudes divided by the vertical
              distance between them, in units of 1/sec.

          weather_amp: Amplifies the actual weather being reported. Intended as, but not constrained
              to, MIL-STD-6016 weather amplification designations (e.g. NO STATEMENT, NO
              SCATTERED BROKEN MEDIUM CLOUD, SCATTERED BROKEN MEDIUM CLOUDS, GUSTY WINDS AT
              SERVICE, FOG IN VALLEYS, HIGHER TERRAIN OBSCURED, SURFACE CONDITIONS VARIABLE,
              SURFACE WIND NE, SURFACE WIND SE, SURFACE WIND SW, SURFACE WIND NW, PRESENCE OF
              CUMULONIMBUS).

          weather_desc: Used in conjunction with actWeather and weatherInt. Intended as, but not
              constrained to, MIL-STD-6016 actual weather descriptor (e.g. NO STATEMENT,
              SHALLOW, PATCHES, LOW DRIFTING, BLOWING, SHOWERS, THUNDERSTORMS, SUPERCOOLED).

          weather_id: Identifier of the weather over target, which should remain the same on
              subsequent Weather Over Target records.

          weather_int: Weather Intensity. Used in conjunction with actWeather and weatherDesc. Intended
              as, but not constrained to, MIL-STD-6016 weather intensity (e.g. NO STATEMENT,
              LIGHT, MODERATE, HEAVY, IN VICINITY).

          wind_chill: The perceived temperature in degrees C.

          wind_cov: Covariance matrix, in knots and second based units. The array values represent
              the lower triangular half of the covariance matrix. The size of the covariance
              matrix is 2x2. The covariance elements are position dependent within the array
              with values ordered as follows:

              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;x&nbsp;&nbsp;&nbsp;&nbsp;y

              x&nbsp;&nbsp;&nbsp;&nbsp;1

              y&nbsp;&nbsp;&nbsp;&nbsp;2&nbsp;&nbsp;&nbsp;3

              The cov array should contain only the lower left triangle values from top left
              down to bottom right, in order.

          wind_dir: Direction the wind is blowing, in degrees clockwise from true north.

          wind_dir_avg: Average wind direction over a 1 minute period, in degrees clockwise from true
              north.

          wind_dir_peak: Wind direction corresponding to the peak wind speed during a 1 minute period, in
              degrees clockwise from true north.

          wind_dir_peak10: Wind direction corresponding to the peak wind speed during a 10 minute period,
              in degrees clockwise from true north.

          wind_gust: Expresses the max gust speed of the wind, in meters/second.

          wind_gust10: Expresses the max gust speed of the wind recorded in a 10 minute period, in
              meters/second.

          wind_spd: Expresses the speed of the wind in meters/second.

          wind_spd_avg: Average wind speed over a 1 minute period, in meters/second.

          wind_var: Boolean describing whether or not the wind direction and/or speed is variable.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/udl/weatherreport",
            body=maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "lat": lat,
                    "lon": lon,
                    "ob_time": ob_time,
                    "report_type": report_type,
                    "source": source,
                    "id": id,
                    "act_weather": act_weather,
                    "agjson": agjson,
                    "alt": alt,
                    "andims": andims,
                    "area": area,
                    "asrid": asrid,
                    "atext": atext,
                    "atype": atype,
                    "bar_press": bar_press,
                    "cc_event": cc_event,
                    "cloud_cover": cloud_cover,
                    "cloud_hght": cloud_hght,
                    "contrail_hght_lower": contrail_hght_lower,
                    "contrail_hght_upper": contrail_hght_upper,
                    "data_level": data_level,
                    "dew_point": dew_point,
                    "dif_rad": dif_rad,
                    "dir_dev": dir_dev,
                    "en_route_weather": en_route_weather,
                    "external_id": external_id,
                    "external_location_id": external_location_id,
                    "forecast_end_time": forecast_end_time,
                    "forecast_start_time": forecast_start_time,
                    "geo_potential_alt": geo_potential_alt,
                    "hshear": hshear,
                    "icao": icao,
                    "icing_lower_limit": icing_lower_limit,
                    "icing_upper_limit": icing_upper_limit,
                    "id_airfield": id_airfield,
                    "id_ground_imagery": id_ground_imagery,
                    "id_sensor": id_sensor,
                    "id_site": id_site,
                    "index_refraction": index_refraction,
                    "origin": origin,
                    "orig_sensor_id": orig_sensor_id,
                    "precip_rate": precip_rate,
                    "qnh": qnh,
                    "rad_vel": rad_vel,
                    "rad_vel_beam1": rad_vel_beam1,
                    "rad_vel_beam2": rad_vel_beam2,
                    "rad_vel_beam3": rad_vel_beam3,
                    "rad_vel_beam4": rad_vel_beam4,
                    "rad_vel_beam5": rad_vel_beam5,
                    "rain_hour": rain_hour,
                    "raw_metar": raw_metar,
                    "raw_taf": raw_taf,
                    "ref_rad": ref_rad,
                    "rel_humidity": rel_humidity,
                    "senalt": senalt,
                    "senlat": senlat,
                    "senlon": senlon,
                    "soil_moisture": soil_moisture,
                    "soil_temp": soil_temp,
                    "solar_rad": solar_rad,
                    "src_ids": src_ids,
                    "src_typs": src_typs,
                    "surrounding_weather": surrounding_weather,
                    "temperature": temperature,
                    "visibility": visibility,
                    "vshear": vshear,
                    "weather_amp": weather_amp,
                    "weather_desc": weather_desc,
                    "weather_id": weather_id,
                    "weather_int": weather_int,
                    "wind_chill": wind_chill,
                    "wind_cov": wind_cov,
                    "wind_dir": wind_dir,
                    "wind_dir_avg": wind_dir_avg,
                    "wind_dir_peak": wind_dir_peak,
                    "wind_dir_peak10": wind_dir_peak10,
                    "wind_gust": wind_gust,
                    "wind_gust10": wind_gust10,
                    "wind_spd": wind_spd,
                    "wind_spd_avg": wind_spd_avg,
                    "wind_var": wind_var,
                },
                weather_report_create_params.WeatherReportCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        *,
        ob_time: Union[str, datetime],
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncOffsetPage[WeatherReportListResponse]:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          ob_time: Datetime when a weather observation was made or forecast was issued in ISO 8601
              UTC datetime format with microsecond precision. (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/weatherreport",
            page=SyncOffsetPage[WeatherReportListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "ob_time": ob_time,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    weather_report_list_params.WeatherReportListParams,
                ),
            ),
            model=WeatherReportListResponse,
        )

    def count(
        self,
        *,
        ob_time: Union[str, datetime],
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
          ob_time: Datetime when a weather observation was made or forecast was issued in ISO 8601
              UTC datetime format with microsecond precision. (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return self._get(
            "/udl/weatherreport/count",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "ob_time": ob_time,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    weather_report_count_params.WeatherReportCountParams,
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
    ) -> WeatherReportFull:
        """
        Service operation to get a single WeatherReport by its unique ID passed as a
        path parameter.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/udl/weatherreport/{id}",
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
                    weather_report_get_params.WeatherReportGetParams,
                ),
            ),
            cast_to=WeatherReportFull,
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
            "/udl/weatherreport/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def tuple(
        self,
        *,
        columns: str,
        ob_time: Union[str, datetime],
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WeatherReportTupleResponse:
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

          ob_time: Datetime when a weather observation was made or forecast was issued in ISO 8601
              UTC datetime format with microsecond precision. (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/udl/weatherreport/tuple",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "columns": columns,
                        "ob_time": ob_time,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    weather_report_tuple_params.WeatherReportTupleParams,
                ),
            ),
            cast_to=WeatherReportTupleResponse,
        )

    def unvalidated_publish(
        self,
        *,
        body: Iterable[weather_report_unvalidated_publish_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a list of WeatherReports as a POST body and ingest
        into the database. This operation is intended to be used for automated feeds
        into UDL. A specific role is required to perform this service operation. Please
        contact the UDL team for assistance.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/filedrop/udl-weatherreport",
            body=maybe_transform(body, Iterable[weather_report_unvalidated_publish_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncWeatherReportResource(AsyncAPIResource):
    @cached_property
    def history(self) -> AsyncHistoryResource:
        return AsyncHistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncWeatherReportResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncWeatherReportResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWeatherReportResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncWeatherReportResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        lat: float,
        lon: float,
        ob_time: Union[str, datetime],
        report_type: str,
        source: str,
        id: str | NotGiven = NOT_GIVEN,
        act_weather: str | NotGiven = NOT_GIVEN,
        agjson: str | NotGiven = NOT_GIVEN,
        alt: float | NotGiven = NOT_GIVEN,
        andims: int | NotGiven = NOT_GIVEN,
        area: str | NotGiven = NOT_GIVEN,
        asrid: int | NotGiven = NOT_GIVEN,
        atext: str | NotGiven = NOT_GIVEN,
        atype: str | NotGiven = NOT_GIVEN,
        bar_press: float | NotGiven = NOT_GIVEN,
        cc_event: bool | NotGiven = NOT_GIVEN,
        cloud_cover: List[str] | NotGiven = NOT_GIVEN,
        cloud_hght: Iterable[float] | NotGiven = NOT_GIVEN,
        contrail_hght_lower: float | NotGiven = NOT_GIVEN,
        contrail_hght_upper: float | NotGiven = NOT_GIVEN,
        data_level: str | NotGiven = NOT_GIVEN,
        dew_point: float | NotGiven = NOT_GIVEN,
        dif_rad: float | NotGiven = NOT_GIVEN,
        dir_dev: float | NotGiven = NOT_GIVEN,
        en_route_weather: str | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        external_location_id: str | NotGiven = NOT_GIVEN,
        forecast_end_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        forecast_start_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        geo_potential_alt: float | NotGiven = NOT_GIVEN,
        hshear: float | NotGiven = NOT_GIVEN,
        icao: str | NotGiven = NOT_GIVEN,
        icing_lower_limit: float | NotGiven = NOT_GIVEN,
        icing_upper_limit: float | NotGiven = NOT_GIVEN,
        id_airfield: str | NotGiven = NOT_GIVEN,
        id_ground_imagery: str | NotGiven = NOT_GIVEN,
        id_sensor: str | NotGiven = NOT_GIVEN,
        id_site: str | NotGiven = NOT_GIVEN,
        index_refraction: float | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        orig_sensor_id: str | NotGiven = NOT_GIVEN,
        precip_rate: float | NotGiven = NOT_GIVEN,
        qnh: float | NotGiven = NOT_GIVEN,
        rad_vel: float | NotGiven = NOT_GIVEN,
        rad_vel_beam1: float | NotGiven = NOT_GIVEN,
        rad_vel_beam2: float | NotGiven = NOT_GIVEN,
        rad_vel_beam3: float | NotGiven = NOT_GIVEN,
        rad_vel_beam4: float | NotGiven = NOT_GIVEN,
        rad_vel_beam5: float | NotGiven = NOT_GIVEN,
        rain_hour: float | NotGiven = NOT_GIVEN,
        raw_metar: str | NotGiven = NOT_GIVEN,
        raw_taf: str | NotGiven = NOT_GIVEN,
        ref_rad: float | NotGiven = NOT_GIVEN,
        rel_humidity: float | NotGiven = NOT_GIVEN,
        senalt: float | NotGiven = NOT_GIVEN,
        senlat: float | NotGiven = NOT_GIVEN,
        senlon: float | NotGiven = NOT_GIVEN,
        soil_moisture: float | NotGiven = NOT_GIVEN,
        soil_temp: float | NotGiven = NOT_GIVEN,
        solar_rad: float | NotGiven = NOT_GIVEN,
        src_ids: List[str] | NotGiven = NOT_GIVEN,
        src_typs: List[str] | NotGiven = NOT_GIVEN,
        surrounding_weather: str | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        visibility: float | NotGiven = NOT_GIVEN,
        vshear: float | NotGiven = NOT_GIVEN,
        weather_amp: str | NotGiven = NOT_GIVEN,
        weather_desc: str | NotGiven = NOT_GIVEN,
        weather_id: str | NotGiven = NOT_GIVEN,
        weather_int: str | NotGiven = NOT_GIVEN,
        wind_chill: float | NotGiven = NOT_GIVEN,
        wind_cov: Iterable[float] | NotGiven = NOT_GIVEN,
        wind_dir: float | NotGiven = NOT_GIVEN,
        wind_dir_avg: float | NotGiven = NOT_GIVEN,
        wind_dir_peak: float | NotGiven = NOT_GIVEN,
        wind_dir_peak10: float | NotGiven = NOT_GIVEN,
        wind_gust: float | NotGiven = NOT_GIVEN,
        wind_gust10: float | NotGiven = NOT_GIVEN,
        wind_spd: float | NotGiven = NOT_GIVEN,
        wind_spd_avg: float | NotGiven = NOT_GIVEN,
        wind_var: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single WeatherReport as a POST body and ingest into
        the database. A specific role is required to perform this service operation.
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

          lat: The central WGS-84 latitude of the weather report, in degrees. -90 to 90 degrees
              (negative values south of equator).

          lon: The central WGS-84 longitude of the weather report, in degrees. -180 to 180
              degrees (negative values west of Prime Meridian).

          ob_time: Datetime when a weather observation was made or forecast was issued in ISO 8601
              UTC datetime format with microsecond precision.

          report_type: Identifies the type of weather report (e.g. OBSERVATION, FORECAST, etc.).

          source: Source of the data.

          id: Unique identifier of the record, auto-generated by the system.

          act_weather: Describes the actual weather at position. Intended as, but not constrained to,
              MIL-STD-6016 actual weather (e.g. NO STATEMENT, NO SIGNIFICANT WEATHER, DRIZZLE,
              RAIN, SNOW, SNOW GRAINS, DIAMOND DUST, ICE PELLETS, HAIL, SMALL HAIL, MIST, FOG,
              SMOKE, VOLCANIC ASH, WIDESPREAD DUST, SAND, HAZE, WELL DEVELOPED DUST, SQUALLS,
              FUNNEL CLOUDS, SANDSTORM, DUSTSTORM, LOW CLOUDS, CLOUDY, GROUND FOG, DUST, HEAVY
              RAIN, THUNDERSTORMS AWT, HEAVY THUNDERSTORMS, HURRICANE TYPHOON CYCLONE,
              TROPICAL STORM, TORNADO, HIGH WINDS, LIGHTNING, FREEZING DRIZZLE, FREEZING RAIN,
              HEAVY SNOW, ICING, SNOW OR RAIN AND SNOW MIXED, SHOWERS, CLEAR).

          agjson: Geographical region or polygon (lat/lon pairs), as depicted by the GeoJSON
              representation of the geometry/geography, of the image as projected on the
              ground. GeoJSON Reference: https://geojson.org/. Ignored if included with a POST
              or PUT request that also specifies a valid 'area' or 'atext' field.

          alt: Point height above ellipsoid (WGS-84), in meters.

          andims: Number of dimensions of the geometry depicted by region.

          area: Optional geographical region or polygon (lat/lon pairs) of the area surrounding
              the point of interest as projected on the ground.

          asrid: Geographical spatial_ref_sys for region.

          atext: Geographical region or polygon (lon/lat pairs), as depicted by the Well-Known
              Text representation of the geometry/geography, of the image as projected on the
              ground. WKT reference: https://www.opengeospatial.org/standards/wkt-crs. Ignored
              if included with a POST or PUT request that also specifies a valid 'area' field.

          atype: Type of region as projected on the ground.

          bar_press: The measurement of air pressure in the atmosphere in kilopascals.

          cc_event: Flag indicating detection of a cloud-to-cloud lightning event.

          cloud_cover: Array of cloud cover descriptions - each element can be maximum of 16 characters
              long. Intended as, but not constrained to, MIL-STD-6016 cloud cover designations
              (e.g. SKY CLEAR, SCATTERED, BROKEN, OVERCAST, SKY OBSCURED). Each element of the
              array corresponds to the elements in the cloudHght array specified respectively.

          cloud_hght: Array of cloud base heights in meters described by the cloudHght array. Each
              element of the array corresponds to the elements in the cloudCover array
              specified respectively.

          contrail_hght_lower: Reports the lowest altitude at which contrails are occurring, in meters.

          contrail_hght_upper: Reports the highest altitude at which contrails are occurring, in meters.

          data_level: Specific pressures or heights where measurements are taken, labeled as either
              MANDATORY or SIGNIFICANT levels. Mandatory levels are at particular pressures at
              geopotential heights. Significant levels are at particular geometric heights.

          dew_point: The temperature at which air is saturated with water vapor, in degrees C.

          dif_rad: The amount of radiation that reaches earth's surface after being scattered by
              the atmosphere, in Watts per square meter.

          dir_dev: The difference in wind direction recorded over a period of time, in degrees.

          en_route_weather: Describes the flight conditions in route to the target (NO STATEMENT, MAINLY
              IFR, MAINLY VFR, THUNDERSTORMS).

              MAINLY IFR:&nbsp;&nbsp;Predominantly Instrument Flight Rules.

              MAINLY VFR:&nbsp;&nbsp;Predominantly Visual Flight Rules.

              THUNDERSTORMS:&nbsp;&nbsp;Thunderstorms expected in route.

          external_id: Optional observation or forecast ID from external systems. This field has no
              meaning within UDL and is provided as a convenience for systems that require
              tracking of an internal system generated ID.

          external_location_id: Optional location ID from external systems. This field has no meaning within UDL
              and is provided as a convenience for systems that require tracking of an
              internal system generated ID.

          forecast_end_time: Valid end time of a weather forecast in ISO 8601 UTC datetime format with
              millisecond precision.

          forecast_start_time: Valid start time of a weather forecast in ISO 8601 UTC datetime format with
              millisecond precision.

          geo_potential_alt: Altitude of a pressure surface in the atmosphere above mean sea level, in
              meters.

          hshear: The change in wind speed between two different lateral positions at a given
              altitude divided by the horizontal distance between them, in units of 1/sec.

          icao: The International Civil Aviation Organization (ICAO) code of the airfield
              associated with this weather report.

          icing_lower_limit: Reports the lowest altitude at which icing or freezing rain is occurring, in
              meters.

          icing_upper_limit: Reports the highest altitude at which icing or freezing rain is occurring, in
              meters.

          id_airfield: Identifier of the Airfield associated with this weather report.

          id_ground_imagery: Identifier of the ground imagery associated for this weather over target report.

          id_sensor: Unique identifier of the sensor making the weather measurement.

          id_site: Identifier of the Site that is associated with this weather report.

          index_refraction: An indication of how much the atmosphere refracts light.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          orig_sensor_id: Optional identifier provided by the record source. This may be an internal
              identifier and not necessarily a valid sensor ID.

          precip_rate: The speed at which water is being applied to a specific area in millimeters per
              hour.

          qnh: Altimeter set to read zero at mean sea level in kilopascals.

          rad_vel: Average radial velocity of wind as measured by radar with multi-beam
              configurations. Radial velocity is the component of wind velocity moving
              directly toward or away from a sensor's radar beam, in meters per second. Values
              can either be positive (wind is moving away from the radar) or negative (wind is
              moving toward the radar).

          rad_vel_beam1: Component of wind velocity moving directly toward or away from radar beam 1, in
              meters per second. Radial velocity values can either be positive (wind is moving
              away from the radar) or negative (wind is moving toward the radar). The beam
              number designation is defined by the data source.

          rad_vel_beam2: Component of wind velocity moving directly toward or away from radar beam 2, in
              meters per second. Radial velocity values can either be positive (wind is moving
              away from the radar) or negative (wind is moving toward the radar). The beam
              number designation is defined by the data source.

          rad_vel_beam3: Component of wind velocity moving directly toward or away from radar beam 3, in
              meters per second. Radial velocity values can either be positive (wind is moving
              away from the radar) or negative (wind is moving toward the radar). The beam
              number designation is defined by the data source.

          rad_vel_beam4: Component of wind velocity moving directly toward or away from radar beam 4, in
              meters per second. Radial velocity values can either be positive (wind is moving
              away from the radar) or negative (wind is moving toward the radar). The beam
              number designation is defined by the data source.

          rad_vel_beam5: Component of wind velocity moving directly toward or away from radar beam 5, in
              meters per second. Radial velocity values can either be positive (wind is moving
              away from the radar) or negative (wind is moving toward the radar). The beam
              number designation is defined by the data source.

          rain_hour: The amount of rain that has fallen in the past hour, in centimeters.

          raw_metar: The Raw Meteorological Aerodrome Report (METAR) string.

          raw_taf: Terminal Aerodrome Forecast (TAF) containing detailed weather predictions for a
              specific airport or aerodrome.

          ref_rad: The amount of radiation that changes direction as a function of atmospheric
              density, in Watts per square meter.

          rel_humidity: The percentage of water vapor in the atmosphere.

          senalt: Sensor altitude at obTime in km. This includes pilot reports or other means of
              weather observation.

          senlat: Sensor WGS84 latitude at obTime in degrees. -90 to 90 degrees (negative values
              south of equator). This includes pilot reports or other means of weather
              observation.

          senlon: Sensor WGS84 longitude at obTime in degrees. -180 to 180 degrees (negative
              values west of Prime Meridian). This includes pilot reports or other means of
              weather observation.

          soil_moisture: The volumetric percentage of soil water contained in a given volume of soil.

          soil_temp: The measurement of soil temperature in degrees C.

          solar_rad: The power per unit area received from the Sun in the form of electromagnetic
              radiation as measured in the wavelength range of the measuring instrument. The
              solar irradiance is measured in watt per square meter (W/m2).

          src_ids: Array of UUID(s) of the UDL data record(s) that are related to this
              WeatherReport record. See the associated 'srcTyps' array for the specific types
              of data, positionally corresponding to the UUIDs in this array. The 'srcTyps'
              and 'srcIds' arrays must match in size. See the corresponding srcTyps array
              element for the data type of the UUID and use the appropriate API operation to
              retrieve that object.

          src_typs: Array of UDL record types (SENSOR, WEATHERDATA) that are related to this
              WeatherReport record. See the associated 'srcIds' array for the record UUIDs,
              positionally corresponding to the record types in this array. The 'srcTyps' and
              'srcIds' arrays must match in size.

          surrounding_weather: Describes in which direction (if any) that better weather conditions exist.
              Intended as, but not constrained to, MIL-STD-6016 surrounding weather
              designations (e.g. NO STATEMENT, BETTER TO NORTH, BETTER TO EAST, BETTER TO
              SOUTH, BETTER TO WEST).

          temperature: The measurement of air temperature in degrees C.

          visibility: Visual distance in meters.

          vshear: The change in wind speed between two different altitudes divided by the vertical
              distance between them, in units of 1/sec.

          weather_amp: Amplifies the actual weather being reported. Intended as, but not constrained
              to, MIL-STD-6016 weather amplification designations (e.g. NO STATEMENT, NO
              SCATTERED BROKEN MEDIUM CLOUD, SCATTERED BROKEN MEDIUM CLOUDS, GUSTY WINDS AT
              SERVICE, FOG IN VALLEYS, HIGHER TERRAIN OBSCURED, SURFACE CONDITIONS VARIABLE,
              SURFACE WIND NE, SURFACE WIND SE, SURFACE WIND SW, SURFACE WIND NW, PRESENCE OF
              CUMULONIMBUS).

          weather_desc: Used in conjunction with actWeather and weatherInt. Intended as, but not
              constrained to, MIL-STD-6016 actual weather descriptor (e.g. NO STATEMENT,
              SHALLOW, PATCHES, LOW DRIFTING, BLOWING, SHOWERS, THUNDERSTORMS, SUPERCOOLED).

          weather_id: Identifier of the weather over target, which should remain the same on
              subsequent Weather Over Target records.

          weather_int: Weather Intensity. Used in conjunction with actWeather and weatherDesc. Intended
              as, but not constrained to, MIL-STD-6016 weather intensity (e.g. NO STATEMENT,
              LIGHT, MODERATE, HEAVY, IN VICINITY).

          wind_chill: The perceived temperature in degrees C.

          wind_cov: Covariance matrix, in knots and second based units. The array values represent
              the lower triangular half of the covariance matrix. The size of the covariance
              matrix is 2x2. The covariance elements are position dependent within the array
              with values ordered as follows:

              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;x&nbsp;&nbsp;&nbsp;&nbsp;y

              x&nbsp;&nbsp;&nbsp;&nbsp;1

              y&nbsp;&nbsp;&nbsp;&nbsp;2&nbsp;&nbsp;&nbsp;3

              The cov array should contain only the lower left triangle values from top left
              down to bottom right, in order.

          wind_dir: Direction the wind is blowing, in degrees clockwise from true north.

          wind_dir_avg: Average wind direction over a 1 minute period, in degrees clockwise from true
              north.

          wind_dir_peak: Wind direction corresponding to the peak wind speed during a 1 minute period, in
              degrees clockwise from true north.

          wind_dir_peak10: Wind direction corresponding to the peak wind speed during a 10 minute period,
              in degrees clockwise from true north.

          wind_gust: Expresses the max gust speed of the wind, in meters/second.

          wind_gust10: Expresses the max gust speed of the wind recorded in a 10 minute period, in
              meters/second.

          wind_spd: Expresses the speed of the wind in meters/second.

          wind_spd_avg: Average wind speed over a 1 minute period, in meters/second.

          wind_var: Boolean describing whether or not the wind direction and/or speed is variable.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/udl/weatherreport",
            body=await async_maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "lat": lat,
                    "lon": lon,
                    "ob_time": ob_time,
                    "report_type": report_type,
                    "source": source,
                    "id": id,
                    "act_weather": act_weather,
                    "agjson": agjson,
                    "alt": alt,
                    "andims": andims,
                    "area": area,
                    "asrid": asrid,
                    "atext": atext,
                    "atype": atype,
                    "bar_press": bar_press,
                    "cc_event": cc_event,
                    "cloud_cover": cloud_cover,
                    "cloud_hght": cloud_hght,
                    "contrail_hght_lower": contrail_hght_lower,
                    "contrail_hght_upper": contrail_hght_upper,
                    "data_level": data_level,
                    "dew_point": dew_point,
                    "dif_rad": dif_rad,
                    "dir_dev": dir_dev,
                    "en_route_weather": en_route_weather,
                    "external_id": external_id,
                    "external_location_id": external_location_id,
                    "forecast_end_time": forecast_end_time,
                    "forecast_start_time": forecast_start_time,
                    "geo_potential_alt": geo_potential_alt,
                    "hshear": hshear,
                    "icao": icao,
                    "icing_lower_limit": icing_lower_limit,
                    "icing_upper_limit": icing_upper_limit,
                    "id_airfield": id_airfield,
                    "id_ground_imagery": id_ground_imagery,
                    "id_sensor": id_sensor,
                    "id_site": id_site,
                    "index_refraction": index_refraction,
                    "origin": origin,
                    "orig_sensor_id": orig_sensor_id,
                    "precip_rate": precip_rate,
                    "qnh": qnh,
                    "rad_vel": rad_vel,
                    "rad_vel_beam1": rad_vel_beam1,
                    "rad_vel_beam2": rad_vel_beam2,
                    "rad_vel_beam3": rad_vel_beam3,
                    "rad_vel_beam4": rad_vel_beam4,
                    "rad_vel_beam5": rad_vel_beam5,
                    "rain_hour": rain_hour,
                    "raw_metar": raw_metar,
                    "raw_taf": raw_taf,
                    "ref_rad": ref_rad,
                    "rel_humidity": rel_humidity,
                    "senalt": senalt,
                    "senlat": senlat,
                    "senlon": senlon,
                    "soil_moisture": soil_moisture,
                    "soil_temp": soil_temp,
                    "solar_rad": solar_rad,
                    "src_ids": src_ids,
                    "src_typs": src_typs,
                    "surrounding_weather": surrounding_weather,
                    "temperature": temperature,
                    "visibility": visibility,
                    "vshear": vshear,
                    "weather_amp": weather_amp,
                    "weather_desc": weather_desc,
                    "weather_id": weather_id,
                    "weather_int": weather_int,
                    "wind_chill": wind_chill,
                    "wind_cov": wind_cov,
                    "wind_dir": wind_dir,
                    "wind_dir_avg": wind_dir_avg,
                    "wind_dir_peak": wind_dir_peak,
                    "wind_dir_peak10": wind_dir_peak10,
                    "wind_gust": wind_gust,
                    "wind_gust10": wind_gust10,
                    "wind_spd": wind_spd,
                    "wind_spd_avg": wind_spd_avg,
                    "wind_var": wind_var,
                },
                weather_report_create_params.WeatherReportCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        *,
        ob_time: Union[str, datetime],
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[WeatherReportListResponse, AsyncOffsetPage[WeatherReportListResponse]]:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          ob_time: Datetime when a weather observation was made or forecast was issued in ISO 8601
              UTC datetime format with microsecond precision. (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/weatherreport",
            page=AsyncOffsetPage[WeatherReportListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "ob_time": ob_time,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    weather_report_list_params.WeatherReportListParams,
                ),
            ),
            model=WeatherReportListResponse,
        )

    async def count(
        self,
        *,
        ob_time: Union[str, datetime],
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
          ob_time: Datetime when a weather observation was made or forecast was issued in ISO 8601
              UTC datetime format with microsecond precision. (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return await self._get(
            "/udl/weatherreport/count",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "ob_time": ob_time,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    weather_report_count_params.WeatherReportCountParams,
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
    ) -> WeatherReportFull:
        """
        Service operation to get a single WeatherReport by its unique ID passed as a
        path parameter.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/udl/weatherreport/{id}",
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
                    weather_report_get_params.WeatherReportGetParams,
                ),
            ),
            cast_to=WeatherReportFull,
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
            "/udl/weatherreport/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def tuple(
        self,
        *,
        columns: str,
        ob_time: Union[str, datetime],
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WeatherReportTupleResponse:
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

          ob_time: Datetime when a weather observation was made or forecast was issued in ISO 8601
              UTC datetime format with microsecond precision. (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/udl/weatherreport/tuple",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "columns": columns,
                        "ob_time": ob_time,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    weather_report_tuple_params.WeatherReportTupleParams,
                ),
            ),
            cast_to=WeatherReportTupleResponse,
        )

    async def unvalidated_publish(
        self,
        *,
        body: Iterable[weather_report_unvalidated_publish_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a list of WeatherReports as a POST body and ingest
        into the database. This operation is intended to be used for automated feeds
        into UDL. A specific role is required to perform this service operation. Please
        contact the UDL team for assistance.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/filedrop/udl-weatherreport",
            body=await async_maybe_transform(body, Iterable[weather_report_unvalidated_publish_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class WeatherReportResourceWithRawResponse:
    def __init__(self, weather_report: WeatherReportResource) -> None:
        self._weather_report = weather_report

        self.create = to_raw_response_wrapper(
            weather_report.create,
        )
        self.list = to_raw_response_wrapper(
            weather_report.list,
        )
        self.count = to_raw_response_wrapper(
            weather_report.count,
        )
        self.get = to_raw_response_wrapper(
            weather_report.get,
        )
        self.queryhelp = to_raw_response_wrapper(
            weather_report.queryhelp,
        )
        self.tuple = to_raw_response_wrapper(
            weather_report.tuple,
        )
        self.unvalidated_publish = to_raw_response_wrapper(
            weather_report.unvalidated_publish,
        )

    @cached_property
    def history(self) -> HistoryResourceWithRawResponse:
        return HistoryResourceWithRawResponse(self._weather_report.history)


class AsyncWeatherReportResourceWithRawResponse:
    def __init__(self, weather_report: AsyncWeatherReportResource) -> None:
        self._weather_report = weather_report

        self.create = async_to_raw_response_wrapper(
            weather_report.create,
        )
        self.list = async_to_raw_response_wrapper(
            weather_report.list,
        )
        self.count = async_to_raw_response_wrapper(
            weather_report.count,
        )
        self.get = async_to_raw_response_wrapper(
            weather_report.get,
        )
        self.queryhelp = async_to_raw_response_wrapper(
            weather_report.queryhelp,
        )
        self.tuple = async_to_raw_response_wrapper(
            weather_report.tuple,
        )
        self.unvalidated_publish = async_to_raw_response_wrapper(
            weather_report.unvalidated_publish,
        )

    @cached_property
    def history(self) -> AsyncHistoryResourceWithRawResponse:
        return AsyncHistoryResourceWithRawResponse(self._weather_report.history)


class WeatherReportResourceWithStreamingResponse:
    def __init__(self, weather_report: WeatherReportResource) -> None:
        self._weather_report = weather_report

        self.create = to_streamed_response_wrapper(
            weather_report.create,
        )
        self.list = to_streamed_response_wrapper(
            weather_report.list,
        )
        self.count = to_streamed_response_wrapper(
            weather_report.count,
        )
        self.get = to_streamed_response_wrapper(
            weather_report.get,
        )
        self.queryhelp = to_streamed_response_wrapper(
            weather_report.queryhelp,
        )
        self.tuple = to_streamed_response_wrapper(
            weather_report.tuple,
        )
        self.unvalidated_publish = to_streamed_response_wrapper(
            weather_report.unvalidated_publish,
        )

    @cached_property
    def history(self) -> HistoryResourceWithStreamingResponse:
        return HistoryResourceWithStreamingResponse(self._weather_report.history)


class AsyncWeatherReportResourceWithStreamingResponse:
    def __init__(self, weather_report: AsyncWeatherReportResource) -> None:
        self._weather_report = weather_report

        self.create = async_to_streamed_response_wrapper(
            weather_report.create,
        )
        self.list = async_to_streamed_response_wrapper(
            weather_report.list,
        )
        self.count = async_to_streamed_response_wrapper(
            weather_report.count,
        )
        self.get = async_to_streamed_response_wrapper(
            weather_report.get,
        )
        self.queryhelp = async_to_streamed_response_wrapper(
            weather_report.queryhelp,
        )
        self.tuple = async_to_streamed_response_wrapper(
            weather_report.tuple,
        )
        self.unvalidated_publish = async_to_streamed_response_wrapper(
            weather_report.unvalidated_publish,
        )

    @cached_property
    def history(self) -> AsyncHistoryResourceWithStreamingResponse:
        return AsyncHistoryResourceWithStreamingResponse(self._weather_report.history)
