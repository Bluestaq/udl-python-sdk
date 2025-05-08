# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from datetime import datetime
from typing_extensions import Literal

import httpx

from .history import (
    HistoryResource,
    AsyncHistoryResource,
    HistoryResourceWithRawResponse,
    AsyncHistoryResourceWithRawResponse,
    HistoryResourceWithStreamingResponse,
    AsyncHistoryResourceWithStreamingResponse,
)
from ...._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....pagination import SyncOffsetPage, AsyncOffsetPage
from ...._base_client import AsyncPaginator, make_request_options
from ....types.observations import (
    rf_observation_get_params,
    rf_observation_list_params,
    rf_observation_count_params,
    rf_observation_tuple_params,
    rf_observation_create_params,
    rf_observation_create_bulk_params,
    rf_observation_unvalidated_publish_params,
)
from ....types.observations.rf_observation_get_response import RfObservationGetResponse
from ....types.observations.rf_observation_list_response import RfObservationListResponse
from ....types.observations.rf_observation_tuple_response import RfObservationTupleResponse

__all__ = ["RfObservationResource", "AsyncRfObservationResource"]


class RfObservationResource(SyncAPIResource):
    @cached_property
    def history(self) -> HistoryResource:
        return HistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> RfObservationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return RfObservationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RfObservationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return RfObservationResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        ob_time: Union[str, datetime],
        source: str,
        type: str,
        id: str | NotGiven = NOT_GIVEN,
        antenna_name: str | NotGiven = NOT_GIVEN,
        azimuth: float | NotGiven = NOT_GIVEN,
        azimuth_measured: bool | NotGiven = NOT_GIVEN,
        azimuth_rate: float | NotGiven = NOT_GIVEN,
        azimuth_unc: float | NotGiven = NOT_GIVEN,
        bandwidth: float | NotGiven = NOT_GIVEN,
        baud_rate: float | NotGiven = NOT_GIVEN,
        baud_rates: Iterable[float] | NotGiven = NOT_GIVEN,
        bit_error_rate: float | NotGiven = NOT_GIVEN,
        carrier_standard: str | NotGiven = NOT_GIVEN,
        channel: int | NotGiven = NOT_GIVEN,
        chip_rates: Iterable[float] | NotGiven = NOT_GIVEN,
        code_fills: List[str] | NotGiven = NOT_GIVEN,
        code_lengths: Iterable[float] | NotGiven = NOT_GIVEN,
        code_taps: List[str] | NotGiven = NOT_GIVEN,
        collection_mode: str | NotGiven = NOT_GIVEN,
        confidence: float | NotGiven = NOT_GIVEN,
        confidences: Iterable[float] | NotGiven = NOT_GIVEN,
        constellation_x_points: Iterable[float] | NotGiven = NOT_GIVEN,
        constellation_y_points: Iterable[float] | NotGiven = NOT_GIVEN,
        descriptor: str | NotGiven = NOT_GIVEN,
        detection_status: str | NotGiven = NOT_GIVEN,
        detection_statuses: List[str] | NotGiven = NOT_GIVEN,
        eirp: float | NotGiven = NOT_GIVEN,
        elevation: float | NotGiven = NOT_GIVEN,
        elevation_measured: bool | NotGiven = NOT_GIVEN,
        elevation_rate: float | NotGiven = NOT_GIVEN,
        elevation_unc: float | NotGiven = NOT_GIVEN,
        elnot: str | NotGiven = NOT_GIVEN,
        end_frequency: float | NotGiven = NOT_GIVEN,
        frequencies: Iterable[float] | NotGiven = NOT_GIVEN,
        frequency: float | NotGiven = NOT_GIVEN,
        frequency_shift: float | NotGiven = NOT_GIVEN,
        id_sensor: str | NotGiven = NOT_GIVEN,
        incoming: bool | NotGiven = NOT_GIVEN,
        inner_coding_rate: int | NotGiven = NOT_GIVEN,
        max_psd: float | NotGiven = NOT_GIVEN,
        min_psd: float | NotGiven = NOT_GIVEN,
        modulation: str | NotGiven = NOT_GIVEN,
        noise_pwr_density: float | NotGiven = NOT_GIVEN,
        nominal_bandwidth: float | NotGiven = NOT_GIVEN,
        nominal_eirp: float | NotGiven = NOT_GIVEN,
        nominal_frequency: float | NotGiven = NOT_GIVEN,
        nominal_power_over_noise: float | NotGiven = NOT_GIVEN,
        nominal_snr: float | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        orig_object_id: str | NotGiven = NOT_GIVEN,
        orig_sensor_id: str | NotGiven = NOT_GIVEN,
        outer_coding_rate: int | NotGiven = NOT_GIVEN,
        peak: bool | NotGiven = NOT_GIVEN,
        pgri: float | NotGiven = NOT_GIVEN,
        pn_orders: Iterable[int] | NotGiven = NOT_GIVEN,
        polarity: float | NotGiven = NOT_GIVEN,
        polarity_type: Literal["H", "V", "R", "L"] | NotGiven = NOT_GIVEN,
        power_over_noise: float | NotGiven = NOT_GIVEN,
        powers: Iterable[float] | NotGiven = NOT_GIVEN,
        range: float | NotGiven = NOT_GIVEN,
        range_measured: bool | NotGiven = NOT_GIVEN,
        range_rate: float | NotGiven = NOT_GIVEN,
        range_rate_measured: bool | NotGiven = NOT_GIVEN,
        range_rate_unc: float | NotGiven = NOT_GIVEN,
        range_unc: float | NotGiven = NOT_GIVEN,
        raw_file_uri: str | NotGiven = NOT_GIVEN,
        reference_level: float | NotGiven = NOT_GIVEN,
        relative_carrier_power: float | NotGiven = NOT_GIVEN,
        relative_noise_floor: float | NotGiven = NOT_GIVEN,
        resolution_bandwidth: float | NotGiven = NOT_GIVEN,
        sat_no: int | NotGiven = NOT_GIVEN,
        senalt: float | NotGiven = NOT_GIVEN,
        senlat: float | NotGiven = NOT_GIVEN,
        senlon: float | NotGiven = NOT_GIVEN,
        signal_ids: List[str] | NotGiven = NOT_GIVEN,
        snr: float | NotGiven = NOT_GIVEN,
        snrs: Iterable[float] | NotGiven = NOT_GIVEN,
        spectrum_analyzer_power: float | NotGiven = NOT_GIVEN,
        start_frequency: float | NotGiven = NOT_GIVEN,
        switch_point: int | NotGiven = NOT_GIVEN,
        symbol_to_noise_ratio: float | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        task_id: str | NotGiven = NOT_GIVEN,
        telemetry_ids: List[str] | NotGiven = NOT_GIVEN,
        track_id: str | NotGiven = NOT_GIVEN,
        track_range: float | NotGiven = NOT_GIVEN,
        transaction_id: str | NotGiven = NOT_GIVEN,
        transmit_filter_roll_off: float | NotGiven = NOT_GIVEN,
        transmit_filter_type: str | NotGiven = NOT_GIVEN,
        transponder: str | NotGiven = NOT_GIVEN,
        uct: bool | NotGiven = NOT_GIVEN,
        url: str | NotGiven = NOT_GIVEN,
        video_bandwidth: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single RF observation as a POST body and ingest into
        the database. This operation is not intended to be used for automated feeds into
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

          ob_time: Ob detection time in ISO 8601 UTC with microsecond precision.

          source: Source of the data.

          type: Type of RF ob (e.g. RF, RF-SOSI, PSD, RFI, SPOOF, etc).

          id: Unique identifier of the record, auto-generated by the system.

          antenna_name: Antenna name of the RFObservation record.

          azimuth: azimuth angle in degrees and J2000 coordinate frame.

          azimuth_measured: Optional flag indicating whether the azimuth value is measured (true) or
              computed (false). If null, consumers may consult the data provider for
              information regarding whether the corresponding value is computed or measured.

          azimuth_rate: Rate of change of the azimuth in degrees per second.

          azimuth_unc: One sigma uncertainty in the azimuth angle measurement, in degrees.

          bandwidth: Measured bandwidth in Hz.

          baud_rate: Baud rate is the number of symbol changes, waveform changes, or signaling
              events, across the transmission medium per second.

          baud_rates: Array of measured signal baud rates.

          bit_error_rate: The ratio of bit errors per number of received bits.

          carrier_standard: Carrier standard (e.g. DVB-S2, 802.11g, etc.).

          channel: Channel of the RFObservation record.

          chip_rates: Array of chipRates.

          code_fills: Array of code fills.

          code_lengths: Array of code lengths.

          code_taps: Array of code taps.

          collection_mode: Collection mode (e.g. SURVEY, SPOT_SEARCH, NEIGHBORHOOD_WATCH, DIRECTED_SEARCH,
              MANUAL, etc).

          confidence: Confidence in the signal and its measurements and characterization.

          confidences: Array of measurement confidences.

          constellation_x_points: Array of individual x-coordinates for demodulated signal constellation. This
              array should correspond with the same-sized array of constellationYPoints.

          constellation_y_points: Array of individual y-coordinates for demodulated signal constellation. This
              array should correspond with the same-sized array of constellationXPoints.

          descriptor: Optional source-provided and searchable metadata or descriptor of the data.

          detection_status: Detection status (e.g. DETECTED, CARRIER_ACQUIRING, CARRIER_DETECTED,
              NOT_DETECTED, etc).

          detection_statuses: Array of detection statuses (e.g. DETECTED, CARRIER_DETECTED, NOT_DETECTED) for
              each measured signal.

          eirp: Measured Equivalent Isotopically Radiated Power in dBW.

          elevation: elevation in degrees and J2000 coordinate frame.

          elevation_measured: Optional flag indicating whether the elevation value is measured (true) or
              computed (false). If null, consumers may consult the data provider for
              information regarding whether the corresponding value is computed or measured.

          elevation_rate: Rate of change of the elevation in degrees per second.

          elevation_unc: One sigma uncertainty in the elevation angle measurement, in degrees.

          elnot: ELINT notation.

          end_frequency: End carrier frequency in Hz.

          frequencies: Array of individual PSD frequencies of the signal in Hz. This array should
              correspond with the same-sized array of powers.

          frequency: Center carrier frequency in Hz.

          frequency_shift: Frequency Shift of the RFObservation record.

          id_sensor: Unique identifier of the reporting sensor.

          incoming: True if the signal is incoming, false if outgoing.

          inner_coding_rate: Inner forward error correction rate: 0 = Auto, 1 = 1/2, 2 = 2/3, 3 = 3/4, 4 =
              5/6, 5 = 7/8, 6 = 8/9, 7 = 3/5, 8 = 4/5, 9 = 9/10, 15 = None.

          max_psd: Maximum measured PSD value of the trace in dBW.

          min_psd: Minimum measured PSD value of the trace in dBW.

          modulation: Transponder modulation (e.g. Auto, QPSK, 8PSK, etc).

          noise_pwr_density: Noise power density, in dBW-Hz.

          nominal_bandwidth: Expected bandwidth in Hz.

          nominal_eirp: Expected Equivalent Isotopically Radiated Power in dBW.

          nominal_frequency: Nominal or expected center carrier frequency in Hz.

          nominal_power_over_noise: Expected carrier power over noise (dBW/Hz).

          nominal_snr: Nominal or expected signal to noise ratio, in dB.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          orig_object_id: Optional identifier provided by observation source to indicate the target
              onorbit object of this observation. This may be an internal identifier and not
              necessarily a valid satellite number.

          orig_sensor_id: Optional identifier provided by observation source to indicate the sensor
              identifier which produced this observation. This may be an internal identifier
              and not necessarily a valid sensor ID.

          outer_coding_rate: Outer forward error correction rate: 0 = Auto, 1 = 1/2, 2 = 2/3, 3 = 3/4, 4 =
              5/6, 5 = 7/8, 6 = 8/9, 7 = 3/5, 8 = 4/5, 9 = 9/10, 15 = None.

          peak: Peak of the RFObservation record.

          pgri: A pulse group repetition interval (PGRI) is a pulse train in which there are
              groups of closely spaced pulses separated by much longer times between these
              pulse groups.

          pn_orders: Array of pnOrder.

          polarity: The antenna pointing dependent polarizer angle, in degrees.

          polarity_type: Transponder polarization e.g. H - (Horizontally Polarized) Perpendicular to
              Earth's surface, V - (Vertically Polarized) Parallel to Earth's surface, L -
              (Left Hand Circularly Polarized) Rotating left relative to the earth's surface,
              R - (Right Hand Circularly Polarized) Rotating right relative to the earth's
              surface.

          power_over_noise: Measured carrier power over noise (dBW/Hz).

          powers: Array of individual measured PSD powers of the signal in dBW. This array should
              correspond with the same-sized array of frequencies.

          range: Target range in km.

          range_measured: Optional flag indicating whether the range value is measured (true) or computed
              (false). If null, consumers may consult the data provider for information
              regarding whether the corresponding value is computed or measured.

          range_rate: Rate of change of the range in km/sec.

          range_rate_measured: Optional flag indicating whether the rangeRate value is measured (true) or
              computed (false). If null, consumers may consult the data provider for
              information regarding whether the corresponding value is computed or measured.

          range_rate_unc: One sigma uncertainty in the range rate measurement, in kilometers/second.

          range_unc: One sigma uncertainty in the range measurement, in kilometers.

          raw_file_uri: Optional URI location in the document repository of the raw file parsed by the
              system to produce this record. To download the raw file, prepend
              https://udl-hostname/scs/download?id= to this value.

          reference_level: Reference signal level, in dBW.

          relative_carrier_power: Measured power of the center carrier frequency in dBW.

          relative_noise_floor: The measure of the signal created from the sum of all the noise sources and
              unwanted signals within the measurement system, in dBW.

          resolution_bandwidth: Resolution bandwidth in Hz.

          sat_no: Satellite/Catalog number of the target on-orbit object.

          senalt: Sensor altitude at obTime (if mobile/onorbit) in km. If null, can be obtained
              from sensor info.

          senlat: Sensor WGS84 latitude at obTime (if mobile/onorbit) in degrees. If null, can be
              obtained from sensor info. -90 to 90 degrees (negative values south of equator).

          senlon: Sensor WGS84 longitude at obTime (if mobile/onorbit) in degrees. If null, can be
              obtained from sensor info. -180 to 180 degrees (negative values west of Prime
              Meridian).

          signal_ids: Array of optional source provided identifiers of the measurements/signals.

          snr: Signal to noise ratio, in dB.

          snrs: Array of signal to noise ratios of the signals, in dB.

          spectrum_analyzer_power: Measured spectrum analyzer power of the center carrier frequency in dBW.

          start_frequency: Start carrier frequency in Hz.

          switch_point: Switch Point of the RFObservation record.

          symbol_to_noise_ratio: Symbol to noise ratio, in dB.

          tags: Optional array of provider/source specific tags for this data, where each
              element is no longer than 32 characters, used for implementing data owner
              conditional access controls to restrict access to the data. Should be left null
              by data providers unless conditional access controls are coordinated with the
              UDL team.

          task_id: Optional identifier to indicate the specific tasking which produced this
              observation.

          telemetry_ids: Array of optional source provided telemetry identifiers of the
              measurements/signals.

          track_id: Optional identifier of the track to which this observation belongs.

          track_range: Target track or apparent range in km.

          transaction_id: Optional identifier to track a commercial or marketplace transaction executed to
              produce this data.

          transmit_filter_roll_off: Transmit pulse shaping filter roll-off value.

          transmit_filter_type: Transmit pulse shaping filter typ (e.g. RRC).

          transponder: Optional identifier provided by observation source to indicate the transponder
              used for this measurement.

          uct: Boolean indicating this observation is part of an uncorrelated track or was
              unable to be correlated to a known object. This flag should only be set to true
              by data providers after an attempt to correlate to an on-orbit object was made
              and failed. If unable to correlate, the 'origObjectId' field may be populated
              with an internal data provider specific identifier.

          url: Optional URL containing additional information on this observation.

          video_bandwidth: Video bandwidth in Hz.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/udl/rfobservation",
            body=maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "ob_time": ob_time,
                    "source": source,
                    "type": type,
                    "id": id,
                    "antenna_name": antenna_name,
                    "azimuth": azimuth,
                    "azimuth_measured": azimuth_measured,
                    "azimuth_rate": azimuth_rate,
                    "azimuth_unc": azimuth_unc,
                    "bandwidth": bandwidth,
                    "baud_rate": baud_rate,
                    "baud_rates": baud_rates,
                    "bit_error_rate": bit_error_rate,
                    "carrier_standard": carrier_standard,
                    "channel": channel,
                    "chip_rates": chip_rates,
                    "code_fills": code_fills,
                    "code_lengths": code_lengths,
                    "code_taps": code_taps,
                    "collection_mode": collection_mode,
                    "confidence": confidence,
                    "confidences": confidences,
                    "constellation_x_points": constellation_x_points,
                    "constellation_y_points": constellation_y_points,
                    "descriptor": descriptor,
                    "detection_status": detection_status,
                    "detection_statuses": detection_statuses,
                    "eirp": eirp,
                    "elevation": elevation,
                    "elevation_measured": elevation_measured,
                    "elevation_rate": elevation_rate,
                    "elevation_unc": elevation_unc,
                    "elnot": elnot,
                    "end_frequency": end_frequency,
                    "frequencies": frequencies,
                    "frequency": frequency,
                    "frequency_shift": frequency_shift,
                    "id_sensor": id_sensor,
                    "incoming": incoming,
                    "inner_coding_rate": inner_coding_rate,
                    "max_psd": max_psd,
                    "min_psd": min_psd,
                    "modulation": modulation,
                    "noise_pwr_density": noise_pwr_density,
                    "nominal_bandwidth": nominal_bandwidth,
                    "nominal_eirp": nominal_eirp,
                    "nominal_frequency": nominal_frequency,
                    "nominal_power_over_noise": nominal_power_over_noise,
                    "nominal_snr": nominal_snr,
                    "origin": origin,
                    "orig_object_id": orig_object_id,
                    "orig_sensor_id": orig_sensor_id,
                    "outer_coding_rate": outer_coding_rate,
                    "peak": peak,
                    "pgri": pgri,
                    "pn_orders": pn_orders,
                    "polarity": polarity,
                    "polarity_type": polarity_type,
                    "power_over_noise": power_over_noise,
                    "powers": powers,
                    "range": range,
                    "range_measured": range_measured,
                    "range_rate": range_rate,
                    "range_rate_measured": range_rate_measured,
                    "range_rate_unc": range_rate_unc,
                    "range_unc": range_unc,
                    "raw_file_uri": raw_file_uri,
                    "reference_level": reference_level,
                    "relative_carrier_power": relative_carrier_power,
                    "relative_noise_floor": relative_noise_floor,
                    "resolution_bandwidth": resolution_bandwidth,
                    "sat_no": sat_no,
                    "senalt": senalt,
                    "senlat": senlat,
                    "senlon": senlon,
                    "signal_ids": signal_ids,
                    "snr": snr,
                    "snrs": snrs,
                    "spectrum_analyzer_power": spectrum_analyzer_power,
                    "start_frequency": start_frequency,
                    "switch_point": switch_point,
                    "symbol_to_noise_ratio": symbol_to_noise_ratio,
                    "tags": tags,
                    "task_id": task_id,
                    "telemetry_ids": telemetry_ids,
                    "track_id": track_id,
                    "track_range": track_range,
                    "transaction_id": transaction_id,
                    "transmit_filter_roll_off": transmit_filter_roll_off,
                    "transmit_filter_type": transmit_filter_type,
                    "transponder": transponder,
                    "uct": uct,
                    "url": url,
                    "video_bandwidth": video_bandwidth,
                },
                rf_observation_create_params.RfObservationCreateParams,
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
    ) -> SyncOffsetPage[RfObservationListResponse]:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          ob_time: Ob detection time in ISO 8601 UTC with microsecond precision.
              (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/rfobservation",
            page=SyncOffsetPage[RfObservationListResponse],
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
                    rf_observation_list_params.RfObservationListParams,
                ),
            ),
            model=RfObservationListResponse,
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
          ob_time: Ob detection time in ISO 8601 UTC with microsecond precision.
              (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return self._get(
            "/udl/rfobservation/count",
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
                    rf_observation_count_params.RfObservationCountParams,
                ),
            ),
            cast_to=str,
        )

    def create_bulk(
        self,
        *,
        body: Iterable[rf_observation_create_bulk_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation intended for initial integration only, to take a list of RF
        observations as a POST body and ingest into the database. This operation is not
        intended to be used for automated feeds into UDL. Data providers should contact
        the UDL team for specific role assignments and for instructions on setting up a
        permanent feed through an alternate mechanism.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/udl/rfobservation/createBulk",
            body=maybe_transform(body, Iterable[rf_observation_create_bulk_params.Body]),
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
    ) -> RfObservationGetResponse:
        """
        Service operation to get a single RF observation by its unique ID passed as a
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
            f"/udl/rfobservation/{id}",
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
                    rf_observation_get_params.RfObservationGetParams,
                ),
            ),
            cast_to=RfObservationGetResponse,
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
            "/udl/rfobservation/queryhelp",
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
    ) -> RfObservationTupleResponse:
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

          ob_time: Ob detection time in ISO 8601 UTC with microsecond precision.
              (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/udl/rfobservation/tuple",
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
                    rf_observation_tuple_params.RfObservationTupleParams,
                ),
            ),
            cast_to=RfObservationTupleResponse,
        )

    def unvalidated_publish(
        self,
        *,
        body: Iterable[rf_observation_unvalidated_publish_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take multiple RF observations as a POST body and ingest
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
            "/filedrop/udl-rf",
            body=maybe_transform(body, Iterable[rf_observation_unvalidated_publish_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncRfObservationResource(AsyncAPIResource):
    @cached_property
    def history(self) -> AsyncHistoryResource:
        return AsyncHistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncRfObservationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncRfObservationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRfObservationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncRfObservationResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        ob_time: Union[str, datetime],
        source: str,
        type: str,
        id: str | NotGiven = NOT_GIVEN,
        antenna_name: str | NotGiven = NOT_GIVEN,
        azimuth: float | NotGiven = NOT_GIVEN,
        azimuth_measured: bool | NotGiven = NOT_GIVEN,
        azimuth_rate: float | NotGiven = NOT_GIVEN,
        azimuth_unc: float | NotGiven = NOT_GIVEN,
        bandwidth: float | NotGiven = NOT_GIVEN,
        baud_rate: float | NotGiven = NOT_GIVEN,
        baud_rates: Iterable[float] | NotGiven = NOT_GIVEN,
        bit_error_rate: float | NotGiven = NOT_GIVEN,
        carrier_standard: str | NotGiven = NOT_GIVEN,
        channel: int | NotGiven = NOT_GIVEN,
        chip_rates: Iterable[float] | NotGiven = NOT_GIVEN,
        code_fills: List[str] | NotGiven = NOT_GIVEN,
        code_lengths: Iterable[float] | NotGiven = NOT_GIVEN,
        code_taps: List[str] | NotGiven = NOT_GIVEN,
        collection_mode: str | NotGiven = NOT_GIVEN,
        confidence: float | NotGiven = NOT_GIVEN,
        confidences: Iterable[float] | NotGiven = NOT_GIVEN,
        constellation_x_points: Iterable[float] | NotGiven = NOT_GIVEN,
        constellation_y_points: Iterable[float] | NotGiven = NOT_GIVEN,
        descriptor: str | NotGiven = NOT_GIVEN,
        detection_status: str | NotGiven = NOT_GIVEN,
        detection_statuses: List[str] | NotGiven = NOT_GIVEN,
        eirp: float | NotGiven = NOT_GIVEN,
        elevation: float | NotGiven = NOT_GIVEN,
        elevation_measured: bool | NotGiven = NOT_GIVEN,
        elevation_rate: float | NotGiven = NOT_GIVEN,
        elevation_unc: float | NotGiven = NOT_GIVEN,
        elnot: str | NotGiven = NOT_GIVEN,
        end_frequency: float | NotGiven = NOT_GIVEN,
        frequencies: Iterable[float] | NotGiven = NOT_GIVEN,
        frequency: float | NotGiven = NOT_GIVEN,
        frequency_shift: float | NotGiven = NOT_GIVEN,
        id_sensor: str | NotGiven = NOT_GIVEN,
        incoming: bool | NotGiven = NOT_GIVEN,
        inner_coding_rate: int | NotGiven = NOT_GIVEN,
        max_psd: float | NotGiven = NOT_GIVEN,
        min_psd: float | NotGiven = NOT_GIVEN,
        modulation: str | NotGiven = NOT_GIVEN,
        noise_pwr_density: float | NotGiven = NOT_GIVEN,
        nominal_bandwidth: float | NotGiven = NOT_GIVEN,
        nominal_eirp: float | NotGiven = NOT_GIVEN,
        nominal_frequency: float | NotGiven = NOT_GIVEN,
        nominal_power_over_noise: float | NotGiven = NOT_GIVEN,
        nominal_snr: float | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        orig_object_id: str | NotGiven = NOT_GIVEN,
        orig_sensor_id: str | NotGiven = NOT_GIVEN,
        outer_coding_rate: int | NotGiven = NOT_GIVEN,
        peak: bool | NotGiven = NOT_GIVEN,
        pgri: float | NotGiven = NOT_GIVEN,
        pn_orders: Iterable[int] | NotGiven = NOT_GIVEN,
        polarity: float | NotGiven = NOT_GIVEN,
        polarity_type: Literal["H", "V", "R", "L"] | NotGiven = NOT_GIVEN,
        power_over_noise: float | NotGiven = NOT_GIVEN,
        powers: Iterable[float] | NotGiven = NOT_GIVEN,
        range: float | NotGiven = NOT_GIVEN,
        range_measured: bool | NotGiven = NOT_GIVEN,
        range_rate: float | NotGiven = NOT_GIVEN,
        range_rate_measured: bool | NotGiven = NOT_GIVEN,
        range_rate_unc: float | NotGiven = NOT_GIVEN,
        range_unc: float | NotGiven = NOT_GIVEN,
        raw_file_uri: str | NotGiven = NOT_GIVEN,
        reference_level: float | NotGiven = NOT_GIVEN,
        relative_carrier_power: float | NotGiven = NOT_GIVEN,
        relative_noise_floor: float | NotGiven = NOT_GIVEN,
        resolution_bandwidth: float | NotGiven = NOT_GIVEN,
        sat_no: int | NotGiven = NOT_GIVEN,
        senalt: float | NotGiven = NOT_GIVEN,
        senlat: float | NotGiven = NOT_GIVEN,
        senlon: float | NotGiven = NOT_GIVEN,
        signal_ids: List[str] | NotGiven = NOT_GIVEN,
        snr: float | NotGiven = NOT_GIVEN,
        snrs: Iterable[float] | NotGiven = NOT_GIVEN,
        spectrum_analyzer_power: float | NotGiven = NOT_GIVEN,
        start_frequency: float | NotGiven = NOT_GIVEN,
        switch_point: int | NotGiven = NOT_GIVEN,
        symbol_to_noise_ratio: float | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        task_id: str | NotGiven = NOT_GIVEN,
        telemetry_ids: List[str] | NotGiven = NOT_GIVEN,
        track_id: str | NotGiven = NOT_GIVEN,
        track_range: float | NotGiven = NOT_GIVEN,
        transaction_id: str | NotGiven = NOT_GIVEN,
        transmit_filter_roll_off: float | NotGiven = NOT_GIVEN,
        transmit_filter_type: str | NotGiven = NOT_GIVEN,
        transponder: str | NotGiven = NOT_GIVEN,
        uct: bool | NotGiven = NOT_GIVEN,
        url: str | NotGiven = NOT_GIVEN,
        video_bandwidth: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single RF observation as a POST body and ingest into
        the database. This operation is not intended to be used for automated feeds into
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

          ob_time: Ob detection time in ISO 8601 UTC with microsecond precision.

          source: Source of the data.

          type: Type of RF ob (e.g. RF, RF-SOSI, PSD, RFI, SPOOF, etc).

          id: Unique identifier of the record, auto-generated by the system.

          antenna_name: Antenna name of the RFObservation record.

          azimuth: azimuth angle in degrees and J2000 coordinate frame.

          azimuth_measured: Optional flag indicating whether the azimuth value is measured (true) or
              computed (false). If null, consumers may consult the data provider for
              information regarding whether the corresponding value is computed or measured.

          azimuth_rate: Rate of change of the azimuth in degrees per second.

          azimuth_unc: One sigma uncertainty in the azimuth angle measurement, in degrees.

          bandwidth: Measured bandwidth in Hz.

          baud_rate: Baud rate is the number of symbol changes, waveform changes, or signaling
              events, across the transmission medium per second.

          baud_rates: Array of measured signal baud rates.

          bit_error_rate: The ratio of bit errors per number of received bits.

          carrier_standard: Carrier standard (e.g. DVB-S2, 802.11g, etc.).

          channel: Channel of the RFObservation record.

          chip_rates: Array of chipRates.

          code_fills: Array of code fills.

          code_lengths: Array of code lengths.

          code_taps: Array of code taps.

          collection_mode: Collection mode (e.g. SURVEY, SPOT_SEARCH, NEIGHBORHOOD_WATCH, DIRECTED_SEARCH,
              MANUAL, etc).

          confidence: Confidence in the signal and its measurements and characterization.

          confidences: Array of measurement confidences.

          constellation_x_points: Array of individual x-coordinates for demodulated signal constellation. This
              array should correspond with the same-sized array of constellationYPoints.

          constellation_y_points: Array of individual y-coordinates for demodulated signal constellation. This
              array should correspond with the same-sized array of constellationXPoints.

          descriptor: Optional source-provided and searchable metadata or descriptor of the data.

          detection_status: Detection status (e.g. DETECTED, CARRIER_ACQUIRING, CARRIER_DETECTED,
              NOT_DETECTED, etc).

          detection_statuses: Array of detection statuses (e.g. DETECTED, CARRIER_DETECTED, NOT_DETECTED) for
              each measured signal.

          eirp: Measured Equivalent Isotopically Radiated Power in dBW.

          elevation: elevation in degrees and J2000 coordinate frame.

          elevation_measured: Optional flag indicating whether the elevation value is measured (true) or
              computed (false). If null, consumers may consult the data provider for
              information regarding whether the corresponding value is computed or measured.

          elevation_rate: Rate of change of the elevation in degrees per second.

          elevation_unc: One sigma uncertainty in the elevation angle measurement, in degrees.

          elnot: ELINT notation.

          end_frequency: End carrier frequency in Hz.

          frequencies: Array of individual PSD frequencies of the signal in Hz. This array should
              correspond with the same-sized array of powers.

          frequency: Center carrier frequency in Hz.

          frequency_shift: Frequency Shift of the RFObservation record.

          id_sensor: Unique identifier of the reporting sensor.

          incoming: True if the signal is incoming, false if outgoing.

          inner_coding_rate: Inner forward error correction rate: 0 = Auto, 1 = 1/2, 2 = 2/3, 3 = 3/4, 4 =
              5/6, 5 = 7/8, 6 = 8/9, 7 = 3/5, 8 = 4/5, 9 = 9/10, 15 = None.

          max_psd: Maximum measured PSD value of the trace in dBW.

          min_psd: Minimum measured PSD value of the trace in dBW.

          modulation: Transponder modulation (e.g. Auto, QPSK, 8PSK, etc).

          noise_pwr_density: Noise power density, in dBW-Hz.

          nominal_bandwidth: Expected bandwidth in Hz.

          nominal_eirp: Expected Equivalent Isotopically Radiated Power in dBW.

          nominal_frequency: Nominal or expected center carrier frequency in Hz.

          nominal_power_over_noise: Expected carrier power over noise (dBW/Hz).

          nominal_snr: Nominal or expected signal to noise ratio, in dB.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          orig_object_id: Optional identifier provided by observation source to indicate the target
              onorbit object of this observation. This may be an internal identifier and not
              necessarily a valid satellite number.

          orig_sensor_id: Optional identifier provided by observation source to indicate the sensor
              identifier which produced this observation. This may be an internal identifier
              and not necessarily a valid sensor ID.

          outer_coding_rate: Outer forward error correction rate: 0 = Auto, 1 = 1/2, 2 = 2/3, 3 = 3/4, 4 =
              5/6, 5 = 7/8, 6 = 8/9, 7 = 3/5, 8 = 4/5, 9 = 9/10, 15 = None.

          peak: Peak of the RFObservation record.

          pgri: A pulse group repetition interval (PGRI) is a pulse train in which there are
              groups of closely spaced pulses separated by much longer times between these
              pulse groups.

          pn_orders: Array of pnOrder.

          polarity: The antenna pointing dependent polarizer angle, in degrees.

          polarity_type: Transponder polarization e.g. H - (Horizontally Polarized) Perpendicular to
              Earth's surface, V - (Vertically Polarized) Parallel to Earth's surface, L -
              (Left Hand Circularly Polarized) Rotating left relative to the earth's surface,
              R - (Right Hand Circularly Polarized) Rotating right relative to the earth's
              surface.

          power_over_noise: Measured carrier power over noise (dBW/Hz).

          powers: Array of individual measured PSD powers of the signal in dBW. This array should
              correspond with the same-sized array of frequencies.

          range: Target range in km.

          range_measured: Optional flag indicating whether the range value is measured (true) or computed
              (false). If null, consumers may consult the data provider for information
              regarding whether the corresponding value is computed or measured.

          range_rate: Rate of change of the range in km/sec.

          range_rate_measured: Optional flag indicating whether the rangeRate value is measured (true) or
              computed (false). If null, consumers may consult the data provider for
              information regarding whether the corresponding value is computed or measured.

          range_rate_unc: One sigma uncertainty in the range rate measurement, in kilometers/second.

          range_unc: One sigma uncertainty in the range measurement, in kilometers.

          raw_file_uri: Optional URI location in the document repository of the raw file parsed by the
              system to produce this record. To download the raw file, prepend
              https://udl-hostname/scs/download?id= to this value.

          reference_level: Reference signal level, in dBW.

          relative_carrier_power: Measured power of the center carrier frequency in dBW.

          relative_noise_floor: The measure of the signal created from the sum of all the noise sources and
              unwanted signals within the measurement system, in dBW.

          resolution_bandwidth: Resolution bandwidth in Hz.

          sat_no: Satellite/Catalog number of the target on-orbit object.

          senalt: Sensor altitude at obTime (if mobile/onorbit) in km. If null, can be obtained
              from sensor info.

          senlat: Sensor WGS84 latitude at obTime (if mobile/onorbit) in degrees. If null, can be
              obtained from sensor info. -90 to 90 degrees (negative values south of equator).

          senlon: Sensor WGS84 longitude at obTime (if mobile/onorbit) in degrees. If null, can be
              obtained from sensor info. -180 to 180 degrees (negative values west of Prime
              Meridian).

          signal_ids: Array of optional source provided identifiers of the measurements/signals.

          snr: Signal to noise ratio, in dB.

          snrs: Array of signal to noise ratios of the signals, in dB.

          spectrum_analyzer_power: Measured spectrum analyzer power of the center carrier frequency in dBW.

          start_frequency: Start carrier frequency in Hz.

          switch_point: Switch Point of the RFObservation record.

          symbol_to_noise_ratio: Symbol to noise ratio, in dB.

          tags: Optional array of provider/source specific tags for this data, where each
              element is no longer than 32 characters, used for implementing data owner
              conditional access controls to restrict access to the data. Should be left null
              by data providers unless conditional access controls are coordinated with the
              UDL team.

          task_id: Optional identifier to indicate the specific tasking which produced this
              observation.

          telemetry_ids: Array of optional source provided telemetry identifiers of the
              measurements/signals.

          track_id: Optional identifier of the track to which this observation belongs.

          track_range: Target track or apparent range in km.

          transaction_id: Optional identifier to track a commercial or marketplace transaction executed to
              produce this data.

          transmit_filter_roll_off: Transmit pulse shaping filter roll-off value.

          transmit_filter_type: Transmit pulse shaping filter typ (e.g. RRC).

          transponder: Optional identifier provided by observation source to indicate the transponder
              used for this measurement.

          uct: Boolean indicating this observation is part of an uncorrelated track or was
              unable to be correlated to a known object. This flag should only be set to true
              by data providers after an attempt to correlate to an on-orbit object was made
              and failed. If unable to correlate, the 'origObjectId' field may be populated
              with an internal data provider specific identifier.

          url: Optional URL containing additional information on this observation.

          video_bandwidth: Video bandwidth in Hz.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/udl/rfobservation",
            body=await async_maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "ob_time": ob_time,
                    "source": source,
                    "type": type,
                    "id": id,
                    "antenna_name": antenna_name,
                    "azimuth": azimuth,
                    "azimuth_measured": azimuth_measured,
                    "azimuth_rate": azimuth_rate,
                    "azimuth_unc": azimuth_unc,
                    "bandwidth": bandwidth,
                    "baud_rate": baud_rate,
                    "baud_rates": baud_rates,
                    "bit_error_rate": bit_error_rate,
                    "carrier_standard": carrier_standard,
                    "channel": channel,
                    "chip_rates": chip_rates,
                    "code_fills": code_fills,
                    "code_lengths": code_lengths,
                    "code_taps": code_taps,
                    "collection_mode": collection_mode,
                    "confidence": confidence,
                    "confidences": confidences,
                    "constellation_x_points": constellation_x_points,
                    "constellation_y_points": constellation_y_points,
                    "descriptor": descriptor,
                    "detection_status": detection_status,
                    "detection_statuses": detection_statuses,
                    "eirp": eirp,
                    "elevation": elevation,
                    "elevation_measured": elevation_measured,
                    "elevation_rate": elevation_rate,
                    "elevation_unc": elevation_unc,
                    "elnot": elnot,
                    "end_frequency": end_frequency,
                    "frequencies": frequencies,
                    "frequency": frequency,
                    "frequency_shift": frequency_shift,
                    "id_sensor": id_sensor,
                    "incoming": incoming,
                    "inner_coding_rate": inner_coding_rate,
                    "max_psd": max_psd,
                    "min_psd": min_psd,
                    "modulation": modulation,
                    "noise_pwr_density": noise_pwr_density,
                    "nominal_bandwidth": nominal_bandwidth,
                    "nominal_eirp": nominal_eirp,
                    "nominal_frequency": nominal_frequency,
                    "nominal_power_over_noise": nominal_power_over_noise,
                    "nominal_snr": nominal_snr,
                    "origin": origin,
                    "orig_object_id": orig_object_id,
                    "orig_sensor_id": orig_sensor_id,
                    "outer_coding_rate": outer_coding_rate,
                    "peak": peak,
                    "pgri": pgri,
                    "pn_orders": pn_orders,
                    "polarity": polarity,
                    "polarity_type": polarity_type,
                    "power_over_noise": power_over_noise,
                    "powers": powers,
                    "range": range,
                    "range_measured": range_measured,
                    "range_rate": range_rate,
                    "range_rate_measured": range_rate_measured,
                    "range_rate_unc": range_rate_unc,
                    "range_unc": range_unc,
                    "raw_file_uri": raw_file_uri,
                    "reference_level": reference_level,
                    "relative_carrier_power": relative_carrier_power,
                    "relative_noise_floor": relative_noise_floor,
                    "resolution_bandwidth": resolution_bandwidth,
                    "sat_no": sat_no,
                    "senalt": senalt,
                    "senlat": senlat,
                    "senlon": senlon,
                    "signal_ids": signal_ids,
                    "snr": snr,
                    "snrs": snrs,
                    "spectrum_analyzer_power": spectrum_analyzer_power,
                    "start_frequency": start_frequency,
                    "switch_point": switch_point,
                    "symbol_to_noise_ratio": symbol_to_noise_ratio,
                    "tags": tags,
                    "task_id": task_id,
                    "telemetry_ids": telemetry_ids,
                    "track_id": track_id,
                    "track_range": track_range,
                    "transaction_id": transaction_id,
                    "transmit_filter_roll_off": transmit_filter_roll_off,
                    "transmit_filter_type": transmit_filter_type,
                    "transponder": transponder,
                    "uct": uct,
                    "url": url,
                    "video_bandwidth": video_bandwidth,
                },
                rf_observation_create_params.RfObservationCreateParams,
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
    ) -> AsyncPaginator[RfObservationListResponse, AsyncOffsetPage[RfObservationListResponse]]:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          ob_time: Ob detection time in ISO 8601 UTC with microsecond precision.
              (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/rfobservation",
            page=AsyncOffsetPage[RfObservationListResponse],
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
                    rf_observation_list_params.RfObservationListParams,
                ),
            ),
            model=RfObservationListResponse,
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
          ob_time: Ob detection time in ISO 8601 UTC with microsecond precision.
              (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return await self._get(
            "/udl/rfobservation/count",
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
                    rf_observation_count_params.RfObservationCountParams,
                ),
            ),
            cast_to=str,
        )

    async def create_bulk(
        self,
        *,
        body: Iterable[rf_observation_create_bulk_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation intended for initial integration only, to take a list of RF
        observations as a POST body and ingest into the database. This operation is not
        intended to be used for automated feeds into UDL. Data providers should contact
        the UDL team for specific role assignments and for instructions on setting up a
        permanent feed through an alternate mechanism.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/udl/rfobservation/createBulk",
            body=await async_maybe_transform(body, Iterable[rf_observation_create_bulk_params.Body]),
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
    ) -> RfObservationGetResponse:
        """
        Service operation to get a single RF observation by its unique ID passed as a
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
            f"/udl/rfobservation/{id}",
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
                    rf_observation_get_params.RfObservationGetParams,
                ),
            ),
            cast_to=RfObservationGetResponse,
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
            "/udl/rfobservation/queryhelp",
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
    ) -> RfObservationTupleResponse:
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

          ob_time: Ob detection time in ISO 8601 UTC with microsecond precision.
              (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/udl/rfobservation/tuple",
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
                    rf_observation_tuple_params.RfObservationTupleParams,
                ),
            ),
            cast_to=RfObservationTupleResponse,
        )

    async def unvalidated_publish(
        self,
        *,
        body: Iterable[rf_observation_unvalidated_publish_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take multiple RF observations as a POST body and ingest
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
            "/filedrop/udl-rf",
            body=await async_maybe_transform(body, Iterable[rf_observation_unvalidated_publish_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class RfObservationResourceWithRawResponse:
    def __init__(self, rf_observation: RfObservationResource) -> None:
        self._rf_observation = rf_observation

        self.create = to_raw_response_wrapper(
            rf_observation.create,
        )
        self.list = to_raw_response_wrapper(
            rf_observation.list,
        )
        self.count = to_raw_response_wrapper(
            rf_observation.count,
        )
        self.create_bulk = to_raw_response_wrapper(
            rf_observation.create_bulk,
        )
        self.get = to_raw_response_wrapper(
            rf_observation.get,
        )
        self.queryhelp = to_raw_response_wrapper(
            rf_observation.queryhelp,
        )
        self.tuple = to_raw_response_wrapper(
            rf_observation.tuple,
        )
        self.unvalidated_publish = to_raw_response_wrapper(
            rf_observation.unvalidated_publish,
        )

    @cached_property
    def history(self) -> HistoryResourceWithRawResponse:
        return HistoryResourceWithRawResponse(self._rf_observation.history)


class AsyncRfObservationResourceWithRawResponse:
    def __init__(self, rf_observation: AsyncRfObservationResource) -> None:
        self._rf_observation = rf_observation

        self.create = async_to_raw_response_wrapper(
            rf_observation.create,
        )
        self.list = async_to_raw_response_wrapper(
            rf_observation.list,
        )
        self.count = async_to_raw_response_wrapper(
            rf_observation.count,
        )
        self.create_bulk = async_to_raw_response_wrapper(
            rf_observation.create_bulk,
        )
        self.get = async_to_raw_response_wrapper(
            rf_observation.get,
        )
        self.queryhelp = async_to_raw_response_wrapper(
            rf_observation.queryhelp,
        )
        self.tuple = async_to_raw_response_wrapper(
            rf_observation.tuple,
        )
        self.unvalidated_publish = async_to_raw_response_wrapper(
            rf_observation.unvalidated_publish,
        )

    @cached_property
    def history(self) -> AsyncHistoryResourceWithRawResponse:
        return AsyncHistoryResourceWithRawResponse(self._rf_observation.history)


class RfObservationResourceWithStreamingResponse:
    def __init__(self, rf_observation: RfObservationResource) -> None:
        self._rf_observation = rf_observation

        self.create = to_streamed_response_wrapper(
            rf_observation.create,
        )
        self.list = to_streamed_response_wrapper(
            rf_observation.list,
        )
        self.count = to_streamed_response_wrapper(
            rf_observation.count,
        )
        self.create_bulk = to_streamed_response_wrapper(
            rf_observation.create_bulk,
        )
        self.get = to_streamed_response_wrapper(
            rf_observation.get,
        )
        self.queryhelp = to_streamed_response_wrapper(
            rf_observation.queryhelp,
        )
        self.tuple = to_streamed_response_wrapper(
            rf_observation.tuple,
        )
        self.unvalidated_publish = to_streamed_response_wrapper(
            rf_observation.unvalidated_publish,
        )

    @cached_property
    def history(self) -> HistoryResourceWithStreamingResponse:
        return HistoryResourceWithStreamingResponse(self._rf_observation.history)


class AsyncRfObservationResourceWithStreamingResponse:
    def __init__(self, rf_observation: AsyncRfObservationResource) -> None:
        self._rf_observation = rf_observation

        self.create = async_to_streamed_response_wrapper(
            rf_observation.create,
        )
        self.list = async_to_streamed_response_wrapper(
            rf_observation.list,
        )
        self.count = async_to_streamed_response_wrapper(
            rf_observation.count,
        )
        self.create_bulk = async_to_streamed_response_wrapper(
            rf_observation.create_bulk,
        )
        self.get = async_to_streamed_response_wrapper(
            rf_observation.get,
        )
        self.queryhelp = async_to_streamed_response_wrapper(
            rf_observation.queryhelp,
        )
        self.tuple = async_to_streamed_response_wrapper(
            rf_observation.tuple,
        )
        self.unvalidated_publish = async_to_streamed_response_wrapper(
            rf_observation.unvalidated_publish,
        )

    @cached_property
    def history(self) -> AsyncHistoryResourceWithStreamingResponse:
        return AsyncHistoryResourceWithStreamingResponse(self._rf_observation.history)
