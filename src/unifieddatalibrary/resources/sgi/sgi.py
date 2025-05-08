# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from datetime import datetime
from typing_extensions import Literal

import httpx

from ...types import (
    sgi_get_params,
    sgi_list_params,
    sgi_count_params,
    sgi_tuple_params,
    sgi_create_params,
    sgi_update_params,
    sgi_create_bulk_params,
    sgi_unvalidated_publish_params,
    sgi_get_data_by_effective_as_of_date_params,
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
from ...types.sgi_get_response import SgiGetResponse
from ...types.sgi_list_response import SgiListResponse
from ...types.sgi_tuple_response import SgiTupleResponse
from ...types.sgi_get_data_by_effective_as_of_date_response import SgiGetDataByEffectiveAsOfDateResponse

__all__ = ["SgiResource", "AsyncSgiResource"]


class SgiResource(SyncAPIResource):
    @cached_property
    def history(self) -> HistoryResource:
        return HistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> SgiResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return SgiResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SgiResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return SgiResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        effective_date: Union[str, datetime],
        sgi_date: Union[str, datetime],
        source: str,
        id: str | NotGiven = NOT_GIVEN,
        analyzer_attenuation: float | NotGiven = NOT_GIVEN,
        ap: float | NotGiven = NOT_GIVEN,
        ap_duration: int | NotGiven = NOT_GIVEN,
        coeff_degree: Iterable[int] | NotGiven = NOT_GIVEN,
        coeff_order: Iterable[int] | NotGiven = NOT_GIVEN,
        ctce: Iterable[float] | NotGiven = NOT_GIVEN,
        ctci: Iterable[float] | NotGiven = NOT_GIVEN,
        dst: float | NotGiven = NOT_GIVEN,
        dtc: float | NotGiven = NOT_GIVEN,
        e10: float | NotGiven = NOT_GIVEN,
        e54: float | NotGiven = NOT_GIVEN,
        f10: float | NotGiven = NOT_GIVEN,
        f10_high: float | NotGiven = NOT_GIVEN,
        f10_low: float | NotGiven = NOT_GIVEN,
        f54: float | NotGiven = NOT_GIVEN,
        f81: float | NotGiven = NOT_GIVEN,
        frequencies: Iterable[float] | NotGiven = NOT_GIVEN,
        gamma: int | NotGiven = NOT_GIVEN,
        id_sensor: str | NotGiven = NOT_GIVEN,
        k_index: int | NotGiven = NOT_GIVEN,
        kp: float | NotGiven = NOT_GIVEN,
        kp_duration: int | NotGiven = NOT_GIVEN,
        m10: float | NotGiven = NOT_GIVEN,
        m54: float | NotGiven = NOT_GIVEN,
        mode: int | NotGiven = NOT_GIVEN,
        norm_factor: float | NotGiven = NOT_GIVEN,
        observed_baseline: Iterable[int] | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        orig_sensor_id: str | NotGiven = NOT_GIVEN,
        powers: Iterable[float] | NotGiven = NOT_GIVEN,
        precedence: Literal["O", "P", "R", "Y", "Z"] | NotGiven = NOT_GIVEN,
        raw_file_uri: str | NotGiven = NOT_GIVEN,
        rb_duration: int | NotGiven = NOT_GIVEN,
        rb_index: float | NotGiven = NOT_GIVEN,
        rb_region_code: int | NotGiven = NOT_GIVEN,
        s10: float | NotGiven = NOT_GIVEN,
        s54: float | NotGiven = NOT_GIVEN,
        state: Literal["I", "N", "P"] | NotGiven = NOT_GIVEN,
        station_name: str | NotGiven = NOT_GIVEN,
        stce: Iterable[float] | NotGiven = NOT_GIVEN,
        stci: Iterable[float] | NotGiven = NOT_GIVEN,
        sunspot_num: float | NotGiven = NOT_GIVEN,
        sunspot_num_high: float | NotGiven = NOT_GIVEN,
        sunspot_num_low: float | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        transaction_id: str | NotGiven = NOT_GIVEN,
        type: str | NotGiven = NOT_GIVEN,
        y10: float | NotGiven = NOT_GIVEN,
        y54: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single SGI record as a POST body and ingest into the
        database. A specific role is required to perform this service operation. Please
        contact the UDL team for assistance.

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

          effective_date: ISO8601 UTC Time the data was received and processed from the source. Typically
              a source provides data for a date window with each transmission including past,
              present, and future predicted values.

          sgi_date: ISO8601 UTC Time of the index value. This could be a past, current, or future
              predicted value. Note: sgiDate defines the start time of the time window for
              this data record.

          source: Source of the data.

          id: Unique identifier of the record, auto-generated by the system.

          analyzer_attenuation: Signal analyzer's input attenuation level, in decibels. Attenuation is a setting
              on the hardware that measures the power of a signal.

          ap: Ap is the planetary geomagnetic 2 nT index (00-21 UT) for the timespan specified
              in apDuration. If apDuration is null, a 3 hour duration should be assumed.

          ap_duration: The time, in hours, for which the Ap index value is valid. If null, a span of 3
              hours is assumed.

          coeff_degree: Array containing the degree of the temperature coefficients. The coeffDegree and
              coeffOrder arrays must be the same length.

          coeff_order: Array containing the order of the temperature coefficients. The coeffDegree and
              coeffOrder arrays must be the same length.

          ctce: Array containing the cosine spherical-harmonic coefficients for Exospheric
              temperature (DTC) difference. Each array element corresponds to the positional
              index of the coeffDegree and coeffOrder arrays.

          ctci: Array containing the cosine spherical-harmonic coefficients for Inflection
              temperature (DTX) difference. Each array element corresponds to the positional
              index of the coeffDegree and coeffOrder arrays.

          dst: Disturbance Storm Time geomagnetic index in nT.

          dtc: delta exospheric temperature correction in units of K.

          e10: Extreme Ultraviolet (EUV) proxy, E10.7, in x10-22 Watts per meter squared per
              Hertz, is the integrated solar EUV energy flux at the top of atmosphere and
              normalized to solar flux units.

          e54: E54 (E10-Bar), in x10-22 Watts per meter squared per Hertz, uses the past
              54-days E10 values to determine the E10 average.

          f10: Daily solar 10.7 cm radio flux in x10-22 Watts per meter squared per Hertz.

          f10_high: Daily F10.7 index - high range, in x10-22 Watts per meter squared per Hertz.
              This field usually applies to forecast values, based on the consensus of the
              Solar Cycle 24 Prediction Panel.

          f10_low: Daily F10.7 index - low range, in x10-22 Watts per meter squared per Hertz. This
              field usually applies to forecast values, based on the consensus of the Solar
              Cycle 24 Prediction Panel.

          f54: 54 day solar 10.7 cm radio flux in x10-22 Watts per meter squared per Hertz.

          f81: 81 day solar 10.7 cm radio flux in x10-22 Watts per meter squared per Hertz.

          frequencies: Array of individual power spectral density (PSD) frequencies of the signal, in
              megahertz. This array should correspond with the same-sized array of powers.

          gamma: The maximum measured gamma deflection during the kpDuration timespan. If
              kpDuration is null, a 3 hour duration should be assumed.

          id_sensor: Unique identifier of the reporting sensor.

          k_index: The maximum measured K-Index at the associated station during the kpDuration
              timespan. The K-Index is a unitless measure (0 - 9) of the deviation in the
              Earth's magnetic field from normal at the station geographic location, with 0
              indicating the absence of geomagnetic disturbance, and 9 indicating the most
              significant disturbance. If kpDuration is null, a 3 hour duration should be
              assumed.

          kp: The Planetary K-index (Kp) over the kpDuration timespan. The Kp-Index is the
              average K-Index for the entire Earth, utilizing a unitless scale (0-9, in
              incremenets of 1/3), with 0 indicating the absence of geomagnetic disturbance,
              and 9 indicating the most significant disturbance. If kpDuration is null, a 3
              hour duration should be assumed.

          kp_duration: The time, in hours, over which the K, Kp, and/or gamma index values are
              measured. If null, a span of 3 hours is assumed.

          m10: Daily M10.7 index for 100-110 km heating of O2 by solar photosphere. 160 nm SRC
              emissions in x10-22 Watts per meter squared per Hertz.

          m54: 54 day M10.7 index for 100-110 km heating of O2 by solar photosphere. 160 nm SRC
              emissions in x10-22 Watts per meter squared per Hertz.

          mode: The transmitted DCA mode of the record (1-3).

          norm_factor: The normalization factor that has already been applied to the index value prior
              to record ingest. Typically used to normalize the index value to a particular
              interval. Units of the normalization factor may vary depending on the provider
              of this data (REACH, POES, CEASE3, etc.).

          observed_baseline: Observed baseline values of the frequencies specified in the frequencies field,
              in solar flux units. The baseline values will be used to help detect abnormal
              readings from the sun that might indicate a flare or other solar activity.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          orig_sensor_id: Optional identifier provided by the reporting source to indicate the sensor
              identifier which produced this data. This may be an internal identifier and not
              necessarily a valid sensor ID.

          powers: Array of individual power spectral density (PSD) powers of the signal, in watts.
              This array should correspond with the same-sized array of frequencies.

          precedence: The precedence of data in this record (O = Immediate, P = Priority, R = Routine,
              Y = Emergency, Z = Flash).

          raw_file_uri: Optional URI location in the document repository of the raw file parsed by the
              system to produce this record. To download the raw file, prepend
              https://udl-hostname/scs/download?id= to this value.

          rb_duration: The timespan over which the associated radiation belt index is factored. If
              rbDuration is null, a 24 hour duration should be assumed. Note: rbDuration
              defines the length of the time window for this data record. The time window
              start time is defined by sgiDate, and the time window end time is defined by
              sgiDate plus rbDuration.

          rb_index: The value of the radiation belt index. This is the ratio of current intensity of
              a radiation belt to long-term average value. It's long-term average should be
              close to 1. Depending on the type of belt sensor, this ratio may measure Flux
              (number of particles / (cm^2 sec energy solid-angle)), dose rate (rad per
              second), or relative counts of particles per time (counts per second). The index
              value may also be normalized, the normalization value typically represents an
              average of the sensor measurements taken within a region over a given time
              interval. See the normFactor field for the specific normalization factor, if
              provided.

          rb_region_code: Region code for the associated radiation belt index. This is the code associated
              with the corresponding radiation belt location. See the provider card for
              reference to specific region code definitions.

          s10: Daily S10.7 index for >200 km heating of O by solar chromosphere. 28.4-30.4 nm
              emissions in x10-22 Watts per meter squared per Hertz.

          s54: 54 day S10.7 index for >200 km heating of O by solar chromosphere. 28.4-30.4 nm
              emissions in x10-22 Watts per meter squared per Hertz.

          state: State indicating Issued (I), Nowcast (N), or Predicted (P) values for this
              record.

          station_name: The name/location of the station that collected the geomagnetic data for this
              record.

          stce: Array containing the sine spherical-harmonic coefficients for Exospheric
              temperature (DTC) difference. Each array element corresponds to the positional
              index of the coeffDegree and coeffOrder arrays.

          stci: Array containing the sine spherical harmonic coefficients for Inflection
              temperature (DTX) difference. Each array element corresponds to the positional
              index of the coeffDegree and coeffOrder arrays.

          sunspot_num: Daily sunspot number.

          sunspot_num_high: Daily sunspot number - high range. This field usually applies to forecast
              values, based on the consensus of the Solar Cycle 24 Prediction Panel.

          sunspot_num_low: Daily sunspot number - low range. This field usually applies to forecast values,
              based on the consensus of the Solar Cycle 24 Prediction Panel.

          tags: Optional array of provider/source specific tags for this data, where each
              element is no longer than 32 characters, used for implementing data owner
              conditional access controls to restrict access to the data. Should be left null
              by data providers unless conditional access controls are coordinated with the
              UDL team.

          transaction_id: Optional identifier to track a commercial or marketplace transaction executed to
              produce this data.

          type: The type of data contained in this record (e.g. HASDM, JBH09, K-Index, PSD-dB,
              RBI, RFI-SFU, etc).

          y10: Daily Y10.7 index for 85-90 km heating of N2, O2, H2O, NO by solar coronal.
              0.1-0.8 nm and Lya 121 nm emissions in x10-22 Watts per meter squared per Hertz.

          y54: 54 day Y10.7 index for 85-90 km heating of N2, O2, H2O, NO by solar coronal.
              0.1-0.8 nm and Lya 121 nm emissions in x10-22 Watts per meter squared per Hertz.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/udl/sgi",
            body=maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "effective_date": effective_date,
                    "sgi_date": sgi_date,
                    "source": source,
                    "id": id,
                    "analyzer_attenuation": analyzer_attenuation,
                    "ap": ap,
                    "ap_duration": ap_duration,
                    "coeff_degree": coeff_degree,
                    "coeff_order": coeff_order,
                    "ctce": ctce,
                    "ctci": ctci,
                    "dst": dst,
                    "dtc": dtc,
                    "e10": e10,
                    "e54": e54,
                    "f10": f10,
                    "f10_high": f10_high,
                    "f10_low": f10_low,
                    "f54": f54,
                    "f81": f81,
                    "frequencies": frequencies,
                    "gamma": gamma,
                    "id_sensor": id_sensor,
                    "k_index": k_index,
                    "kp": kp,
                    "kp_duration": kp_duration,
                    "m10": m10,
                    "m54": m54,
                    "mode": mode,
                    "norm_factor": norm_factor,
                    "observed_baseline": observed_baseline,
                    "origin": origin,
                    "orig_sensor_id": orig_sensor_id,
                    "powers": powers,
                    "precedence": precedence,
                    "raw_file_uri": raw_file_uri,
                    "rb_duration": rb_duration,
                    "rb_index": rb_index,
                    "rb_region_code": rb_region_code,
                    "s10": s10,
                    "s54": s54,
                    "state": state,
                    "station_name": station_name,
                    "stce": stce,
                    "stci": stci,
                    "sunspot_num": sunspot_num,
                    "sunspot_num_high": sunspot_num_high,
                    "sunspot_num_low": sunspot_num_low,
                    "tags": tags,
                    "transaction_id": transaction_id,
                    "type": type,
                    "y10": y10,
                    "y54": y54,
                },
                sgi_create_params.SgiCreateParams,
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
        effective_date: Union[str, datetime],
        sgi_date: Union[str, datetime],
        source: str,
        body_id: str | NotGiven = NOT_GIVEN,
        analyzer_attenuation: float | NotGiven = NOT_GIVEN,
        ap: float | NotGiven = NOT_GIVEN,
        ap_duration: int | NotGiven = NOT_GIVEN,
        coeff_degree: Iterable[int] | NotGiven = NOT_GIVEN,
        coeff_order: Iterable[int] | NotGiven = NOT_GIVEN,
        ctce: Iterable[float] | NotGiven = NOT_GIVEN,
        ctci: Iterable[float] | NotGiven = NOT_GIVEN,
        dst: float | NotGiven = NOT_GIVEN,
        dtc: float | NotGiven = NOT_GIVEN,
        e10: float | NotGiven = NOT_GIVEN,
        e54: float | NotGiven = NOT_GIVEN,
        f10: float | NotGiven = NOT_GIVEN,
        f10_high: float | NotGiven = NOT_GIVEN,
        f10_low: float | NotGiven = NOT_GIVEN,
        f54: float | NotGiven = NOT_GIVEN,
        f81: float | NotGiven = NOT_GIVEN,
        frequencies: Iterable[float] | NotGiven = NOT_GIVEN,
        gamma: int | NotGiven = NOT_GIVEN,
        id_sensor: str | NotGiven = NOT_GIVEN,
        k_index: int | NotGiven = NOT_GIVEN,
        kp: float | NotGiven = NOT_GIVEN,
        kp_duration: int | NotGiven = NOT_GIVEN,
        m10: float | NotGiven = NOT_GIVEN,
        m54: float | NotGiven = NOT_GIVEN,
        mode: int | NotGiven = NOT_GIVEN,
        norm_factor: float | NotGiven = NOT_GIVEN,
        observed_baseline: Iterable[int] | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        orig_sensor_id: str | NotGiven = NOT_GIVEN,
        powers: Iterable[float] | NotGiven = NOT_GIVEN,
        precedence: Literal["O", "P", "R", "Y", "Z"] | NotGiven = NOT_GIVEN,
        raw_file_uri: str | NotGiven = NOT_GIVEN,
        rb_duration: int | NotGiven = NOT_GIVEN,
        rb_index: float | NotGiven = NOT_GIVEN,
        rb_region_code: int | NotGiven = NOT_GIVEN,
        s10: float | NotGiven = NOT_GIVEN,
        s54: float | NotGiven = NOT_GIVEN,
        state: Literal["I", "N", "P"] | NotGiven = NOT_GIVEN,
        station_name: str | NotGiven = NOT_GIVEN,
        stce: Iterable[float] | NotGiven = NOT_GIVEN,
        stci: Iterable[float] | NotGiven = NOT_GIVEN,
        sunspot_num: float | NotGiven = NOT_GIVEN,
        sunspot_num_high: float | NotGiven = NOT_GIVEN,
        sunspot_num_low: float | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        transaction_id: str | NotGiven = NOT_GIVEN,
        type: str | NotGiven = NOT_GIVEN,
        y10: float | NotGiven = NOT_GIVEN,
        y54: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Service operation to update a single SGI record.

        A specific role is required to
        perform this service operation. Please contact the UDL team for assistance.

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

          effective_date: ISO8601 UTC Time the data was received and processed from the source. Typically
              a source provides data for a date window with each transmission including past,
              present, and future predicted values.

          sgi_date: ISO8601 UTC Time of the index value. This could be a past, current, or future
              predicted value. Note: sgiDate defines the start time of the time window for
              this data record.

          source: Source of the data.

          body_id: Unique identifier of the record, auto-generated by the system.

          analyzer_attenuation: Signal analyzer's input attenuation level, in decibels. Attenuation is a setting
              on the hardware that measures the power of a signal.

          ap: Ap is the planetary geomagnetic 2 nT index (00-21 UT) for the timespan specified
              in apDuration. If apDuration is null, a 3 hour duration should be assumed.

          ap_duration: The time, in hours, for which the Ap index value is valid. If null, a span of 3
              hours is assumed.

          coeff_degree: Array containing the degree of the temperature coefficients. The coeffDegree and
              coeffOrder arrays must be the same length.

          coeff_order: Array containing the order of the temperature coefficients. The coeffDegree and
              coeffOrder arrays must be the same length.

          ctce: Array containing the cosine spherical-harmonic coefficients for Exospheric
              temperature (DTC) difference. Each array element corresponds to the positional
              index of the coeffDegree and coeffOrder arrays.

          ctci: Array containing the cosine spherical-harmonic coefficients for Inflection
              temperature (DTX) difference. Each array element corresponds to the positional
              index of the coeffDegree and coeffOrder arrays.

          dst: Disturbance Storm Time geomagnetic index in nT.

          dtc: delta exospheric temperature correction in units of K.

          e10: Extreme Ultraviolet (EUV) proxy, E10.7, in x10-22 Watts per meter squared per
              Hertz, is the integrated solar EUV energy flux at the top of atmosphere and
              normalized to solar flux units.

          e54: E54 (E10-Bar), in x10-22 Watts per meter squared per Hertz, uses the past
              54-days E10 values to determine the E10 average.

          f10: Daily solar 10.7 cm radio flux in x10-22 Watts per meter squared per Hertz.

          f10_high: Daily F10.7 index - high range, in x10-22 Watts per meter squared per Hertz.
              This field usually applies to forecast values, based on the consensus of the
              Solar Cycle 24 Prediction Panel.

          f10_low: Daily F10.7 index - low range, in x10-22 Watts per meter squared per Hertz. This
              field usually applies to forecast values, based on the consensus of the Solar
              Cycle 24 Prediction Panel.

          f54: 54 day solar 10.7 cm radio flux in x10-22 Watts per meter squared per Hertz.

          f81: 81 day solar 10.7 cm radio flux in x10-22 Watts per meter squared per Hertz.

          frequencies: Array of individual power spectral density (PSD) frequencies of the signal, in
              megahertz. This array should correspond with the same-sized array of powers.

          gamma: The maximum measured gamma deflection during the kpDuration timespan. If
              kpDuration is null, a 3 hour duration should be assumed.

          id_sensor: Unique identifier of the reporting sensor.

          k_index: The maximum measured K-Index at the associated station during the kpDuration
              timespan. The K-Index is a unitless measure (0 - 9) of the deviation in the
              Earth's magnetic field from normal at the station geographic location, with 0
              indicating the absence of geomagnetic disturbance, and 9 indicating the most
              significant disturbance. If kpDuration is null, a 3 hour duration should be
              assumed.

          kp: The Planetary K-index (Kp) over the kpDuration timespan. The Kp-Index is the
              average K-Index for the entire Earth, utilizing a unitless scale (0-9, in
              incremenets of 1/3), with 0 indicating the absence of geomagnetic disturbance,
              and 9 indicating the most significant disturbance. If kpDuration is null, a 3
              hour duration should be assumed.

          kp_duration: The time, in hours, over which the K, Kp, and/or gamma index values are
              measured. If null, a span of 3 hours is assumed.

          m10: Daily M10.7 index for 100-110 km heating of O2 by solar photosphere. 160 nm SRC
              emissions in x10-22 Watts per meter squared per Hertz.

          m54: 54 day M10.7 index for 100-110 km heating of O2 by solar photosphere. 160 nm SRC
              emissions in x10-22 Watts per meter squared per Hertz.

          mode: The transmitted DCA mode of the record (1-3).

          norm_factor: The normalization factor that has already been applied to the index value prior
              to record ingest. Typically used to normalize the index value to a particular
              interval. Units of the normalization factor may vary depending on the provider
              of this data (REACH, POES, CEASE3, etc.).

          observed_baseline: Observed baseline values of the frequencies specified in the frequencies field,
              in solar flux units. The baseline values will be used to help detect abnormal
              readings from the sun that might indicate a flare or other solar activity.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          orig_sensor_id: Optional identifier provided by the reporting source to indicate the sensor
              identifier which produced this data. This may be an internal identifier and not
              necessarily a valid sensor ID.

          powers: Array of individual power spectral density (PSD) powers of the signal, in watts.
              This array should correspond with the same-sized array of frequencies.

          precedence: The precedence of data in this record (O = Immediate, P = Priority, R = Routine,
              Y = Emergency, Z = Flash).

          raw_file_uri: Optional URI location in the document repository of the raw file parsed by the
              system to produce this record. To download the raw file, prepend
              https://udl-hostname/scs/download?id= to this value.

          rb_duration: The timespan over which the associated radiation belt index is factored. If
              rbDuration is null, a 24 hour duration should be assumed. Note: rbDuration
              defines the length of the time window for this data record. The time window
              start time is defined by sgiDate, and the time window end time is defined by
              sgiDate plus rbDuration.

          rb_index: The value of the radiation belt index. This is the ratio of current intensity of
              a radiation belt to long-term average value. It's long-term average should be
              close to 1. Depending on the type of belt sensor, this ratio may measure Flux
              (number of particles / (cm^2 sec energy solid-angle)), dose rate (rad per
              second), or relative counts of particles per time (counts per second). The index
              value may also be normalized, the normalization value typically represents an
              average of the sensor measurements taken within a region over a given time
              interval. See the normFactor field for the specific normalization factor, if
              provided.

          rb_region_code: Region code for the associated radiation belt index. This is the code associated
              with the corresponding radiation belt location. See the provider card for
              reference to specific region code definitions.

          s10: Daily S10.7 index for >200 km heating of O by solar chromosphere. 28.4-30.4 nm
              emissions in x10-22 Watts per meter squared per Hertz.

          s54: 54 day S10.7 index for >200 km heating of O by solar chromosphere. 28.4-30.4 nm
              emissions in x10-22 Watts per meter squared per Hertz.

          state: State indicating Issued (I), Nowcast (N), or Predicted (P) values for this
              record.

          station_name: The name/location of the station that collected the geomagnetic data for this
              record.

          stce: Array containing the sine spherical-harmonic coefficients for Exospheric
              temperature (DTC) difference. Each array element corresponds to the positional
              index of the coeffDegree and coeffOrder arrays.

          stci: Array containing the sine spherical harmonic coefficients for Inflection
              temperature (DTX) difference. Each array element corresponds to the positional
              index of the coeffDegree and coeffOrder arrays.

          sunspot_num: Daily sunspot number.

          sunspot_num_high: Daily sunspot number - high range. This field usually applies to forecast
              values, based on the consensus of the Solar Cycle 24 Prediction Panel.

          sunspot_num_low: Daily sunspot number - low range. This field usually applies to forecast values,
              based on the consensus of the Solar Cycle 24 Prediction Panel.

          tags: Optional array of provider/source specific tags for this data, where each
              element is no longer than 32 characters, used for implementing data owner
              conditional access controls to restrict access to the data. Should be left null
              by data providers unless conditional access controls are coordinated with the
              UDL team.

          transaction_id: Optional identifier to track a commercial or marketplace transaction executed to
              produce this data.

          type: The type of data contained in this record (e.g. HASDM, JBH09, K-Index, PSD-dB,
              RBI, RFI-SFU, etc).

          y10: Daily Y10.7 index for 85-90 km heating of N2, O2, H2O, NO by solar coronal.
              0.1-0.8 nm and Lya 121 nm emissions in x10-22 Watts per meter squared per Hertz.

          y54: 54 day Y10.7 index for 85-90 km heating of N2, O2, H2O, NO by solar coronal.
              0.1-0.8 nm and Lya 121 nm emissions in x10-22 Watts per meter squared per Hertz.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            f"/udl/sgi/{path_id}",
            body=maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "effective_date": effective_date,
                    "sgi_date": sgi_date,
                    "source": source,
                    "body_id": body_id,
                    "analyzer_attenuation": analyzer_attenuation,
                    "ap": ap,
                    "ap_duration": ap_duration,
                    "coeff_degree": coeff_degree,
                    "coeff_order": coeff_order,
                    "ctce": ctce,
                    "ctci": ctci,
                    "dst": dst,
                    "dtc": dtc,
                    "e10": e10,
                    "e54": e54,
                    "f10": f10,
                    "f10_high": f10_high,
                    "f10_low": f10_low,
                    "f54": f54,
                    "f81": f81,
                    "frequencies": frequencies,
                    "gamma": gamma,
                    "id_sensor": id_sensor,
                    "k_index": k_index,
                    "kp": kp,
                    "kp_duration": kp_duration,
                    "m10": m10,
                    "m54": m54,
                    "mode": mode,
                    "norm_factor": norm_factor,
                    "observed_baseline": observed_baseline,
                    "origin": origin,
                    "orig_sensor_id": orig_sensor_id,
                    "powers": powers,
                    "precedence": precedence,
                    "raw_file_uri": raw_file_uri,
                    "rb_duration": rb_duration,
                    "rb_index": rb_index,
                    "rb_region_code": rb_region_code,
                    "s10": s10,
                    "s54": s54,
                    "state": state,
                    "station_name": station_name,
                    "stce": stce,
                    "stci": stci,
                    "sunspot_num": sunspot_num,
                    "sunspot_num_high": sunspot_num_high,
                    "sunspot_num_low": sunspot_num_low,
                    "tags": tags,
                    "transaction_id": transaction_id,
                    "type": type,
                    "y10": y10,
                    "y54": y54,
                },
                sgi_update_params.SgiUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        *,
        effective_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        sgi_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncOffsetPage[SgiListResponse]:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          effective_date: (One or more of fields 'effectiveDate, sgiDate' are required.) ISO8601 UTC Time
              the data was received and processed from the source. Typically a source provides
              solar data for a date window with each transmission including past, present, and
              future predicted values. (YYYY-MM-DDTHH:MM:SS.sssZ)

          sgi_date: (One or more of fields 'effectiveDate, sgiDate' are required.) ISO8601 UTC Time
              of the index value. This could be a past, current, or future predicted value.
              Note: sgiDate defines the start time of the time window for this data record.
              (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/sgi",
            page=SyncOffsetPage[SgiListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "effective_date": effective_date,
                        "first_result": first_result,
                        "max_results": max_results,
                        "sgi_date": sgi_date,
                    },
                    sgi_list_params.SgiListParams,
                ),
            ),
            model=SgiListResponse,
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
        Service operation to delete a SGI record specified by the passed ID path
        parameter. A specific role is required to perform this service operation. Please
        contact the UDL team for assistance.

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
            f"/udl/sgi/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def count(
        self,
        *,
        effective_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        sgi_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
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
          effective_date: (One or more of fields 'effectiveDate, sgiDate' are required.) ISO8601 UTC Time
              the data was received and processed from the source. Typically a source provides
              solar data for a date window with each transmission including past, present, and
              future predicted values. (YYYY-MM-DDTHH:MM:SS.sssZ)

          sgi_date: (One or more of fields 'effectiveDate, sgiDate' are required.) ISO8601 UTC Time
              of the index value. This could be a past, current, or future predicted value.
              Note: sgiDate defines the start time of the time window for this data record.
              (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return self._get(
            "/udl/sgi/count",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "effective_date": effective_date,
                        "first_result": first_result,
                        "max_results": max_results,
                        "sgi_date": sgi_date,
                    },
                    sgi_count_params.SgiCountParams,
                ),
            ),
            cast_to=str,
        )

    def create_bulk(
        self,
        *,
        body: Iterable[sgi_create_bulk_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation intended for initial integration only, to take a list of SGI
        as a POST body and ingest into the database. This operation is not intended to
        be used for automated feeds into UDL. Data providers should contact the UDL team
        for specific role assignments and for instructions on setting up a permanent
        feed through an alternate mechanism.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/udl/sgi/createBulk",
            body=maybe_transform(body, Iterable[sgi_create_bulk_params.Body]),
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
    ) -> SgiGetResponse:
        """
        Service operation to get a single SGI record by its unique ID passed as a path
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
            f"/udl/sgi/{id}",
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
                    sgi_get_params.SgiGetParams,
                ),
            ),
            cast_to=SgiGetResponse,
        )

    def get_data_by_effective_as_of_date(
        self,
        *,
        effective_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        sgi_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SgiGetDataByEffectiveAsOfDateResponse:
        """
        Service to return matching SGI records as of the effective date.

        Args:
          effective_date: (One or more of fields 'effectiveDate, sgiDate' are required.) ISO8601 UTC Time
              the data was received and processed from the source. Typically a source provides
              solar data for a date window with each transmission including past, present, and
              future predicted values. (YYYY-MM-DDTHH:MM:SS.sssZ)

          sgi_date: (One or more of fields 'effectiveDate, sgiDate' are required.) ISO8601 UTC Time
              of the index value. This could be a past, current, or future predicted value.
              Note: sgiDate defines the start time of the time window for this data record.
              (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/udl/sgi/getSGIDataByEffectiveAsOfDate",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "effective_date": effective_date,
                        "first_result": first_result,
                        "max_results": max_results,
                        "sgi_date": sgi_date,
                    },
                    sgi_get_data_by_effective_as_of_date_params.SgiGetDataByEffectiveAsOfDateParams,
                ),
            ),
            cast_to=SgiGetDataByEffectiveAsOfDateResponse,
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
            "/udl/sgi/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def tuple(
        self,
        *,
        columns: str,
        effective_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        sgi_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SgiTupleResponse:
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

          effective_date: (One or more of fields 'effectiveDate, sgiDate' are required.) ISO8601 UTC Time
              the data was received and processed from the source. Typically a source provides
              solar data for a date window with each transmission including past, present, and
              future predicted values. (YYYY-MM-DDTHH:MM:SS.sssZ)

          sgi_date: (One or more of fields 'effectiveDate, sgiDate' are required.) ISO8601 UTC Time
              of the index value. This could be a past, current, or future predicted value.
              Note: sgiDate defines the start time of the time window for this data record.
              (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/udl/sgi/tuple",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "columns": columns,
                        "effective_date": effective_date,
                        "first_result": first_result,
                        "max_results": max_results,
                        "sgi_date": sgi_date,
                    },
                    sgi_tuple_params.SgiTupleParams,
                ),
            ),
            cast_to=SgiTupleResponse,
        )

    def unvalidated_publish(
        self,
        *,
        body: Iterable[sgi_unvalidated_publish_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take multiple SGI as a POST body and ingest into the
        database. This operation is intended to be used for automated feeds into UDL. A
        specific role is required to perform this service operation. Please contact the
        UDL team for assistance.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/filedrop/udl-sgi",
            body=maybe_transform(body, Iterable[sgi_unvalidated_publish_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncSgiResource(AsyncAPIResource):
    @cached_property
    def history(self) -> AsyncHistoryResource:
        return AsyncHistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSgiResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncSgiResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSgiResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncSgiResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        effective_date: Union[str, datetime],
        sgi_date: Union[str, datetime],
        source: str,
        id: str | NotGiven = NOT_GIVEN,
        analyzer_attenuation: float | NotGiven = NOT_GIVEN,
        ap: float | NotGiven = NOT_GIVEN,
        ap_duration: int | NotGiven = NOT_GIVEN,
        coeff_degree: Iterable[int] | NotGiven = NOT_GIVEN,
        coeff_order: Iterable[int] | NotGiven = NOT_GIVEN,
        ctce: Iterable[float] | NotGiven = NOT_GIVEN,
        ctci: Iterable[float] | NotGiven = NOT_GIVEN,
        dst: float | NotGiven = NOT_GIVEN,
        dtc: float | NotGiven = NOT_GIVEN,
        e10: float | NotGiven = NOT_GIVEN,
        e54: float | NotGiven = NOT_GIVEN,
        f10: float | NotGiven = NOT_GIVEN,
        f10_high: float | NotGiven = NOT_GIVEN,
        f10_low: float | NotGiven = NOT_GIVEN,
        f54: float | NotGiven = NOT_GIVEN,
        f81: float | NotGiven = NOT_GIVEN,
        frequencies: Iterable[float] | NotGiven = NOT_GIVEN,
        gamma: int | NotGiven = NOT_GIVEN,
        id_sensor: str | NotGiven = NOT_GIVEN,
        k_index: int | NotGiven = NOT_GIVEN,
        kp: float | NotGiven = NOT_GIVEN,
        kp_duration: int | NotGiven = NOT_GIVEN,
        m10: float | NotGiven = NOT_GIVEN,
        m54: float | NotGiven = NOT_GIVEN,
        mode: int | NotGiven = NOT_GIVEN,
        norm_factor: float | NotGiven = NOT_GIVEN,
        observed_baseline: Iterable[int] | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        orig_sensor_id: str | NotGiven = NOT_GIVEN,
        powers: Iterable[float] | NotGiven = NOT_GIVEN,
        precedence: Literal["O", "P", "R", "Y", "Z"] | NotGiven = NOT_GIVEN,
        raw_file_uri: str | NotGiven = NOT_GIVEN,
        rb_duration: int | NotGiven = NOT_GIVEN,
        rb_index: float | NotGiven = NOT_GIVEN,
        rb_region_code: int | NotGiven = NOT_GIVEN,
        s10: float | NotGiven = NOT_GIVEN,
        s54: float | NotGiven = NOT_GIVEN,
        state: Literal["I", "N", "P"] | NotGiven = NOT_GIVEN,
        station_name: str | NotGiven = NOT_GIVEN,
        stce: Iterable[float] | NotGiven = NOT_GIVEN,
        stci: Iterable[float] | NotGiven = NOT_GIVEN,
        sunspot_num: float | NotGiven = NOT_GIVEN,
        sunspot_num_high: float | NotGiven = NOT_GIVEN,
        sunspot_num_low: float | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        transaction_id: str | NotGiven = NOT_GIVEN,
        type: str | NotGiven = NOT_GIVEN,
        y10: float | NotGiven = NOT_GIVEN,
        y54: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single SGI record as a POST body and ingest into the
        database. A specific role is required to perform this service operation. Please
        contact the UDL team for assistance.

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

          effective_date: ISO8601 UTC Time the data was received and processed from the source. Typically
              a source provides data for a date window with each transmission including past,
              present, and future predicted values.

          sgi_date: ISO8601 UTC Time of the index value. This could be a past, current, or future
              predicted value. Note: sgiDate defines the start time of the time window for
              this data record.

          source: Source of the data.

          id: Unique identifier of the record, auto-generated by the system.

          analyzer_attenuation: Signal analyzer's input attenuation level, in decibels. Attenuation is a setting
              on the hardware that measures the power of a signal.

          ap: Ap is the planetary geomagnetic 2 nT index (00-21 UT) for the timespan specified
              in apDuration. If apDuration is null, a 3 hour duration should be assumed.

          ap_duration: The time, in hours, for which the Ap index value is valid. If null, a span of 3
              hours is assumed.

          coeff_degree: Array containing the degree of the temperature coefficients. The coeffDegree and
              coeffOrder arrays must be the same length.

          coeff_order: Array containing the order of the temperature coefficients. The coeffDegree and
              coeffOrder arrays must be the same length.

          ctce: Array containing the cosine spherical-harmonic coefficients for Exospheric
              temperature (DTC) difference. Each array element corresponds to the positional
              index of the coeffDegree and coeffOrder arrays.

          ctci: Array containing the cosine spherical-harmonic coefficients for Inflection
              temperature (DTX) difference. Each array element corresponds to the positional
              index of the coeffDegree and coeffOrder arrays.

          dst: Disturbance Storm Time geomagnetic index in nT.

          dtc: delta exospheric temperature correction in units of K.

          e10: Extreme Ultraviolet (EUV) proxy, E10.7, in x10-22 Watts per meter squared per
              Hertz, is the integrated solar EUV energy flux at the top of atmosphere and
              normalized to solar flux units.

          e54: E54 (E10-Bar), in x10-22 Watts per meter squared per Hertz, uses the past
              54-days E10 values to determine the E10 average.

          f10: Daily solar 10.7 cm radio flux in x10-22 Watts per meter squared per Hertz.

          f10_high: Daily F10.7 index - high range, in x10-22 Watts per meter squared per Hertz.
              This field usually applies to forecast values, based on the consensus of the
              Solar Cycle 24 Prediction Panel.

          f10_low: Daily F10.7 index - low range, in x10-22 Watts per meter squared per Hertz. This
              field usually applies to forecast values, based on the consensus of the Solar
              Cycle 24 Prediction Panel.

          f54: 54 day solar 10.7 cm radio flux in x10-22 Watts per meter squared per Hertz.

          f81: 81 day solar 10.7 cm radio flux in x10-22 Watts per meter squared per Hertz.

          frequencies: Array of individual power spectral density (PSD) frequencies of the signal, in
              megahertz. This array should correspond with the same-sized array of powers.

          gamma: The maximum measured gamma deflection during the kpDuration timespan. If
              kpDuration is null, a 3 hour duration should be assumed.

          id_sensor: Unique identifier of the reporting sensor.

          k_index: The maximum measured K-Index at the associated station during the kpDuration
              timespan. The K-Index is a unitless measure (0 - 9) of the deviation in the
              Earth's magnetic field from normal at the station geographic location, with 0
              indicating the absence of geomagnetic disturbance, and 9 indicating the most
              significant disturbance. If kpDuration is null, a 3 hour duration should be
              assumed.

          kp: The Planetary K-index (Kp) over the kpDuration timespan. The Kp-Index is the
              average K-Index for the entire Earth, utilizing a unitless scale (0-9, in
              incremenets of 1/3), with 0 indicating the absence of geomagnetic disturbance,
              and 9 indicating the most significant disturbance. If kpDuration is null, a 3
              hour duration should be assumed.

          kp_duration: The time, in hours, over which the K, Kp, and/or gamma index values are
              measured. If null, a span of 3 hours is assumed.

          m10: Daily M10.7 index for 100-110 km heating of O2 by solar photosphere. 160 nm SRC
              emissions in x10-22 Watts per meter squared per Hertz.

          m54: 54 day M10.7 index for 100-110 km heating of O2 by solar photosphere. 160 nm SRC
              emissions in x10-22 Watts per meter squared per Hertz.

          mode: The transmitted DCA mode of the record (1-3).

          norm_factor: The normalization factor that has already been applied to the index value prior
              to record ingest. Typically used to normalize the index value to a particular
              interval. Units of the normalization factor may vary depending on the provider
              of this data (REACH, POES, CEASE3, etc.).

          observed_baseline: Observed baseline values of the frequencies specified in the frequencies field,
              in solar flux units. The baseline values will be used to help detect abnormal
              readings from the sun that might indicate a flare or other solar activity.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          orig_sensor_id: Optional identifier provided by the reporting source to indicate the sensor
              identifier which produced this data. This may be an internal identifier and not
              necessarily a valid sensor ID.

          powers: Array of individual power spectral density (PSD) powers of the signal, in watts.
              This array should correspond with the same-sized array of frequencies.

          precedence: The precedence of data in this record (O = Immediate, P = Priority, R = Routine,
              Y = Emergency, Z = Flash).

          raw_file_uri: Optional URI location in the document repository of the raw file parsed by the
              system to produce this record. To download the raw file, prepend
              https://udl-hostname/scs/download?id= to this value.

          rb_duration: The timespan over which the associated radiation belt index is factored. If
              rbDuration is null, a 24 hour duration should be assumed. Note: rbDuration
              defines the length of the time window for this data record. The time window
              start time is defined by sgiDate, and the time window end time is defined by
              sgiDate plus rbDuration.

          rb_index: The value of the radiation belt index. This is the ratio of current intensity of
              a radiation belt to long-term average value. It's long-term average should be
              close to 1. Depending on the type of belt sensor, this ratio may measure Flux
              (number of particles / (cm^2 sec energy solid-angle)), dose rate (rad per
              second), or relative counts of particles per time (counts per second). The index
              value may also be normalized, the normalization value typically represents an
              average of the sensor measurements taken within a region over a given time
              interval. See the normFactor field for the specific normalization factor, if
              provided.

          rb_region_code: Region code for the associated radiation belt index. This is the code associated
              with the corresponding radiation belt location. See the provider card for
              reference to specific region code definitions.

          s10: Daily S10.7 index for >200 km heating of O by solar chromosphere. 28.4-30.4 nm
              emissions in x10-22 Watts per meter squared per Hertz.

          s54: 54 day S10.7 index for >200 km heating of O by solar chromosphere. 28.4-30.4 nm
              emissions in x10-22 Watts per meter squared per Hertz.

          state: State indicating Issued (I), Nowcast (N), or Predicted (P) values for this
              record.

          station_name: The name/location of the station that collected the geomagnetic data for this
              record.

          stce: Array containing the sine spherical-harmonic coefficients for Exospheric
              temperature (DTC) difference. Each array element corresponds to the positional
              index of the coeffDegree and coeffOrder arrays.

          stci: Array containing the sine spherical harmonic coefficients for Inflection
              temperature (DTX) difference. Each array element corresponds to the positional
              index of the coeffDegree and coeffOrder arrays.

          sunspot_num: Daily sunspot number.

          sunspot_num_high: Daily sunspot number - high range. This field usually applies to forecast
              values, based on the consensus of the Solar Cycle 24 Prediction Panel.

          sunspot_num_low: Daily sunspot number - low range. This field usually applies to forecast values,
              based on the consensus of the Solar Cycle 24 Prediction Panel.

          tags: Optional array of provider/source specific tags for this data, where each
              element is no longer than 32 characters, used for implementing data owner
              conditional access controls to restrict access to the data. Should be left null
              by data providers unless conditional access controls are coordinated with the
              UDL team.

          transaction_id: Optional identifier to track a commercial or marketplace transaction executed to
              produce this data.

          type: The type of data contained in this record (e.g. HASDM, JBH09, K-Index, PSD-dB,
              RBI, RFI-SFU, etc).

          y10: Daily Y10.7 index for 85-90 km heating of N2, O2, H2O, NO by solar coronal.
              0.1-0.8 nm and Lya 121 nm emissions in x10-22 Watts per meter squared per Hertz.

          y54: 54 day Y10.7 index for 85-90 km heating of N2, O2, H2O, NO by solar coronal.
              0.1-0.8 nm and Lya 121 nm emissions in x10-22 Watts per meter squared per Hertz.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/udl/sgi",
            body=await async_maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "effective_date": effective_date,
                    "sgi_date": sgi_date,
                    "source": source,
                    "id": id,
                    "analyzer_attenuation": analyzer_attenuation,
                    "ap": ap,
                    "ap_duration": ap_duration,
                    "coeff_degree": coeff_degree,
                    "coeff_order": coeff_order,
                    "ctce": ctce,
                    "ctci": ctci,
                    "dst": dst,
                    "dtc": dtc,
                    "e10": e10,
                    "e54": e54,
                    "f10": f10,
                    "f10_high": f10_high,
                    "f10_low": f10_low,
                    "f54": f54,
                    "f81": f81,
                    "frequencies": frequencies,
                    "gamma": gamma,
                    "id_sensor": id_sensor,
                    "k_index": k_index,
                    "kp": kp,
                    "kp_duration": kp_duration,
                    "m10": m10,
                    "m54": m54,
                    "mode": mode,
                    "norm_factor": norm_factor,
                    "observed_baseline": observed_baseline,
                    "origin": origin,
                    "orig_sensor_id": orig_sensor_id,
                    "powers": powers,
                    "precedence": precedence,
                    "raw_file_uri": raw_file_uri,
                    "rb_duration": rb_duration,
                    "rb_index": rb_index,
                    "rb_region_code": rb_region_code,
                    "s10": s10,
                    "s54": s54,
                    "state": state,
                    "station_name": station_name,
                    "stce": stce,
                    "stci": stci,
                    "sunspot_num": sunspot_num,
                    "sunspot_num_high": sunspot_num_high,
                    "sunspot_num_low": sunspot_num_low,
                    "tags": tags,
                    "transaction_id": transaction_id,
                    "type": type,
                    "y10": y10,
                    "y54": y54,
                },
                sgi_create_params.SgiCreateParams,
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
        effective_date: Union[str, datetime],
        sgi_date: Union[str, datetime],
        source: str,
        body_id: str | NotGiven = NOT_GIVEN,
        analyzer_attenuation: float | NotGiven = NOT_GIVEN,
        ap: float | NotGiven = NOT_GIVEN,
        ap_duration: int | NotGiven = NOT_GIVEN,
        coeff_degree: Iterable[int] | NotGiven = NOT_GIVEN,
        coeff_order: Iterable[int] | NotGiven = NOT_GIVEN,
        ctce: Iterable[float] | NotGiven = NOT_GIVEN,
        ctci: Iterable[float] | NotGiven = NOT_GIVEN,
        dst: float | NotGiven = NOT_GIVEN,
        dtc: float | NotGiven = NOT_GIVEN,
        e10: float | NotGiven = NOT_GIVEN,
        e54: float | NotGiven = NOT_GIVEN,
        f10: float | NotGiven = NOT_GIVEN,
        f10_high: float | NotGiven = NOT_GIVEN,
        f10_low: float | NotGiven = NOT_GIVEN,
        f54: float | NotGiven = NOT_GIVEN,
        f81: float | NotGiven = NOT_GIVEN,
        frequencies: Iterable[float] | NotGiven = NOT_GIVEN,
        gamma: int | NotGiven = NOT_GIVEN,
        id_sensor: str | NotGiven = NOT_GIVEN,
        k_index: int | NotGiven = NOT_GIVEN,
        kp: float | NotGiven = NOT_GIVEN,
        kp_duration: int | NotGiven = NOT_GIVEN,
        m10: float | NotGiven = NOT_GIVEN,
        m54: float | NotGiven = NOT_GIVEN,
        mode: int | NotGiven = NOT_GIVEN,
        norm_factor: float | NotGiven = NOT_GIVEN,
        observed_baseline: Iterable[int] | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        orig_sensor_id: str | NotGiven = NOT_GIVEN,
        powers: Iterable[float] | NotGiven = NOT_GIVEN,
        precedence: Literal["O", "P", "R", "Y", "Z"] | NotGiven = NOT_GIVEN,
        raw_file_uri: str | NotGiven = NOT_GIVEN,
        rb_duration: int | NotGiven = NOT_GIVEN,
        rb_index: float | NotGiven = NOT_GIVEN,
        rb_region_code: int | NotGiven = NOT_GIVEN,
        s10: float | NotGiven = NOT_GIVEN,
        s54: float | NotGiven = NOT_GIVEN,
        state: Literal["I", "N", "P"] | NotGiven = NOT_GIVEN,
        station_name: str | NotGiven = NOT_GIVEN,
        stce: Iterable[float] | NotGiven = NOT_GIVEN,
        stci: Iterable[float] | NotGiven = NOT_GIVEN,
        sunspot_num: float | NotGiven = NOT_GIVEN,
        sunspot_num_high: float | NotGiven = NOT_GIVEN,
        sunspot_num_low: float | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        transaction_id: str | NotGiven = NOT_GIVEN,
        type: str | NotGiven = NOT_GIVEN,
        y10: float | NotGiven = NOT_GIVEN,
        y54: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Service operation to update a single SGI record.

        A specific role is required to
        perform this service operation. Please contact the UDL team for assistance.

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

          effective_date: ISO8601 UTC Time the data was received and processed from the source. Typically
              a source provides data for a date window with each transmission including past,
              present, and future predicted values.

          sgi_date: ISO8601 UTC Time of the index value. This could be a past, current, or future
              predicted value. Note: sgiDate defines the start time of the time window for
              this data record.

          source: Source of the data.

          body_id: Unique identifier of the record, auto-generated by the system.

          analyzer_attenuation: Signal analyzer's input attenuation level, in decibels. Attenuation is a setting
              on the hardware that measures the power of a signal.

          ap: Ap is the planetary geomagnetic 2 nT index (00-21 UT) for the timespan specified
              in apDuration. If apDuration is null, a 3 hour duration should be assumed.

          ap_duration: The time, in hours, for which the Ap index value is valid. If null, a span of 3
              hours is assumed.

          coeff_degree: Array containing the degree of the temperature coefficients. The coeffDegree and
              coeffOrder arrays must be the same length.

          coeff_order: Array containing the order of the temperature coefficients. The coeffDegree and
              coeffOrder arrays must be the same length.

          ctce: Array containing the cosine spherical-harmonic coefficients for Exospheric
              temperature (DTC) difference. Each array element corresponds to the positional
              index of the coeffDegree and coeffOrder arrays.

          ctci: Array containing the cosine spherical-harmonic coefficients for Inflection
              temperature (DTX) difference. Each array element corresponds to the positional
              index of the coeffDegree and coeffOrder arrays.

          dst: Disturbance Storm Time geomagnetic index in nT.

          dtc: delta exospheric temperature correction in units of K.

          e10: Extreme Ultraviolet (EUV) proxy, E10.7, in x10-22 Watts per meter squared per
              Hertz, is the integrated solar EUV energy flux at the top of atmosphere and
              normalized to solar flux units.

          e54: E54 (E10-Bar), in x10-22 Watts per meter squared per Hertz, uses the past
              54-days E10 values to determine the E10 average.

          f10: Daily solar 10.7 cm radio flux in x10-22 Watts per meter squared per Hertz.

          f10_high: Daily F10.7 index - high range, in x10-22 Watts per meter squared per Hertz.
              This field usually applies to forecast values, based on the consensus of the
              Solar Cycle 24 Prediction Panel.

          f10_low: Daily F10.7 index - low range, in x10-22 Watts per meter squared per Hertz. This
              field usually applies to forecast values, based on the consensus of the Solar
              Cycle 24 Prediction Panel.

          f54: 54 day solar 10.7 cm radio flux in x10-22 Watts per meter squared per Hertz.

          f81: 81 day solar 10.7 cm radio flux in x10-22 Watts per meter squared per Hertz.

          frequencies: Array of individual power spectral density (PSD) frequencies of the signal, in
              megahertz. This array should correspond with the same-sized array of powers.

          gamma: The maximum measured gamma deflection during the kpDuration timespan. If
              kpDuration is null, a 3 hour duration should be assumed.

          id_sensor: Unique identifier of the reporting sensor.

          k_index: The maximum measured K-Index at the associated station during the kpDuration
              timespan. The K-Index is a unitless measure (0 - 9) of the deviation in the
              Earth's magnetic field from normal at the station geographic location, with 0
              indicating the absence of geomagnetic disturbance, and 9 indicating the most
              significant disturbance. If kpDuration is null, a 3 hour duration should be
              assumed.

          kp: The Planetary K-index (Kp) over the kpDuration timespan. The Kp-Index is the
              average K-Index for the entire Earth, utilizing a unitless scale (0-9, in
              incremenets of 1/3), with 0 indicating the absence of geomagnetic disturbance,
              and 9 indicating the most significant disturbance. If kpDuration is null, a 3
              hour duration should be assumed.

          kp_duration: The time, in hours, over which the K, Kp, and/or gamma index values are
              measured. If null, a span of 3 hours is assumed.

          m10: Daily M10.7 index for 100-110 km heating of O2 by solar photosphere. 160 nm SRC
              emissions in x10-22 Watts per meter squared per Hertz.

          m54: 54 day M10.7 index for 100-110 km heating of O2 by solar photosphere. 160 nm SRC
              emissions in x10-22 Watts per meter squared per Hertz.

          mode: The transmitted DCA mode of the record (1-3).

          norm_factor: The normalization factor that has already been applied to the index value prior
              to record ingest. Typically used to normalize the index value to a particular
              interval. Units of the normalization factor may vary depending on the provider
              of this data (REACH, POES, CEASE3, etc.).

          observed_baseline: Observed baseline values of the frequencies specified in the frequencies field,
              in solar flux units. The baseline values will be used to help detect abnormal
              readings from the sun that might indicate a flare or other solar activity.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          orig_sensor_id: Optional identifier provided by the reporting source to indicate the sensor
              identifier which produced this data. This may be an internal identifier and not
              necessarily a valid sensor ID.

          powers: Array of individual power spectral density (PSD) powers of the signal, in watts.
              This array should correspond with the same-sized array of frequencies.

          precedence: The precedence of data in this record (O = Immediate, P = Priority, R = Routine,
              Y = Emergency, Z = Flash).

          raw_file_uri: Optional URI location in the document repository of the raw file parsed by the
              system to produce this record. To download the raw file, prepend
              https://udl-hostname/scs/download?id= to this value.

          rb_duration: The timespan over which the associated radiation belt index is factored. If
              rbDuration is null, a 24 hour duration should be assumed. Note: rbDuration
              defines the length of the time window for this data record. The time window
              start time is defined by sgiDate, and the time window end time is defined by
              sgiDate plus rbDuration.

          rb_index: The value of the radiation belt index. This is the ratio of current intensity of
              a radiation belt to long-term average value. It's long-term average should be
              close to 1. Depending on the type of belt sensor, this ratio may measure Flux
              (number of particles / (cm^2 sec energy solid-angle)), dose rate (rad per
              second), or relative counts of particles per time (counts per second). The index
              value may also be normalized, the normalization value typically represents an
              average of the sensor measurements taken within a region over a given time
              interval. See the normFactor field for the specific normalization factor, if
              provided.

          rb_region_code: Region code for the associated radiation belt index. This is the code associated
              with the corresponding radiation belt location. See the provider card for
              reference to specific region code definitions.

          s10: Daily S10.7 index for >200 km heating of O by solar chromosphere. 28.4-30.4 nm
              emissions in x10-22 Watts per meter squared per Hertz.

          s54: 54 day S10.7 index for >200 km heating of O by solar chromosphere. 28.4-30.4 nm
              emissions in x10-22 Watts per meter squared per Hertz.

          state: State indicating Issued (I), Nowcast (N), or Predicted (P) values for this
              record.

          station_name: The name/location of the station that collected the geomagnetic data for this
              record.

          stce: Array containing the sine spherical-harmonic coefficients for Exospheric
              temperature (DTC) difference. Each array element corresponds to the positional
              index of the coeffDegree and coeffOrder arrays.

          stci: Array containing the sine spherical harmonic coefficients for Inflection
              temperature (DTX) difference. Each array element corresponds to the positional
              index of the coeffDegree and coeffOrder arrays.

          sunspot_num: Daily sunspot number.

          sunspot_num_high: Daily sunspot number - high range. This field usually applies to forecast
              values, based on the consensus of the Solar Cycle 24 Prediction Panel.

          sunspot_num_low: Daily sunspot number - low range. This field usually applies to forecast values,
              based on the consensus of the Solar Cycle 24 Prediction Panel.

          tags: Optional array of provider/source specific tags for this data, where each
              element is no longer than 32 characters, used for implementing data owner
              conditional access controls to restrict access to the data. Should be left null
              by data providers unless conditional access controls are coordinated with the
              UDL team.

          transaction_id: Optional identifier to track a commercial or marketplace transaction executed to
              produce this data.

          type: The type of data contained in this record (e.g. HASDM, JBH09, K-Index, PSD-dB,
              RBI, RFI-SFU, etc).

          y10: Daily Y10.7 index for 85-90 km heating of N2, O2, H2O, NO by solar coronal.
              0.1-0.8 nm and Lya 121 nm emissions in x10-22 Watts per meter squared per Hertz.

          y54: 54 day Y10.7 index for 85-90 km heating of N2, O2, H2O, NO by solar coronal.
              0.1-0.8 nm and Lya 121 nm emissions in x10-22 Watts per meter squared per Hertz.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            f"/udl/sgi/{path_id}",
            body=await async_maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "effective_date": effective_date,
                    "sgi_date": sgi_date,
                    "source": source,
                    "body_id": body_id,
                    "analyzer_attenuation": analyzer_attenuation,
                    "ap": ap,
                    "ap_duration": ap_duration,
                    "coeff_degree": coeff_degree,
                    "coeff_order": coeff_order,
                    "ctce": ctce,
                    "ctci": ctci,
                    "dst": dst,
                    "dtc": dtc,
                    "e10": e10,
                    "e54": e54,
                    "f10": f10,
                    "f10_high": f10_high,
                    "f10_low": f10_low,
                    "f54": f54,
                    "f81": f81,
                    "frequencies": frequencies,
                    "gamma": gamma,
                    "id_sensor": id_sensor,
                    "k_index": k_index,
                    "kp": kp,
                    "kp_duration": kp_duration,
                    "m10": m10,
                    "m54": m54,
                    "mode": mode,
                    "norm_factor": norm_factor,
                    "observed_baseline": observed_baseline,
                    "origin": origin,
                    "orig_sensor_id": orig_sensor_id,
                    "powers": powers,
                    "precedence": precedence,
                    "raw_file_uri": raw_file_uri,
                    "rb_duration": rb_duration,
                    "rb_index": rb_index,
                    "rb_region_code": rb_region_code,
                    "s10": s10,
                    "s54": s54,
                    "state": state,
                    "station_name": station_name,
                    "stce": stce,
                    "stci": stci,
                    "sunspot_num": sunspot_num,
                    "sunspot_num_high": sunspot_num_high,
                    "sunspot_num_low": sunspot_num_low,
                    "tags": tags,
                    "transaction_id": transaction_id,
                    "type": type,
                    "y10": y10,
                    "y54": y54,
                },
                sgi_update_params.SgiUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        *,
        effective_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        sgi_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[SgiListResponse, AsyncOffsetPage[SgiListResponse]]:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          effective_date: (One or more of fields 'effectiveDate, sgiDate' are required.) ISO8601 UTC Time
              the data was received and processed from the source. Typically a source provides
              solar data for a date window with each transmission including past, present, and
              future predicted values. (YYYY-MM-DDTHH:MM:SS.sssZ)

          sgi_date: (One or more of fields 'effectiveDate, sgiDate' are required.) ISO8601 UTC Time
              of the index value. This could be a past, current, or future predicted value.
              Note: sgiDate defines the start time of the time window for this data record.
              (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/sgi",
            page=AsyncOffsetPage[SgiListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "effective_date": effective_date,
                        "first_result": first_result,
                        "max_results": max_results,
                        "sgi_date": sgi_date,
                    },
                    sgi_list_params.SgiListParams,
                ),
            ),
            model=SgiListResponse,
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
        Service operation to delete a SGI record specified by the passed ID path
        parameter. A specific role is required to perform this service operation. Please
        contact the UDL team for assistance.

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
            f"/udl/sgi/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def count(
        self,
        *,
        effective_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        sgi_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
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
          effective_date: (One or more of fields 'effectiveDate, sgiDate' are required.) ISO8601 UTC Time
              the data was received and processed from the source. Typically a source provides
              solar data for a date window with each transmission including past, present, and
              future predicted values. (YYYY-MM-DDTHH:MM:SS.sssZ)

          sgi_date: (One or more of fields 'effectiveDate, sgiDate' are required.) ISO8601 UTC Time
              of the index value. This could be a past, current, or future predicted value.
              Note: sgiDate defines the start time of the time window for this data record.
              (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return await self._get(
            "/udl/sgi/count",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "effective_date": effective_date,
                        "first_result": first_result,
                        "max_results": max_results,
                        "sgi_date": sgi_date,
                    },
                    sgi_count_params.SgiCountParams,
                ),
            ),
            cast_to=str,
        )

    async def create_bulk(
        self,
        *,
        body: Iterable[sgi_create_bulk_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation intended for initial integration only, to take a list of SGI
        as a POST body and ingest into the database. This operation is not intended to
        be used for automated feeds into UDL. Data providers should contact the UDL team
        for specific role assignments and for instructions on setting up a permanent
        feed through an alternate mechanism.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/udl/sgi/createBulk",
            body=await async_maybe_transform(body, Iterable[sgi_create_bulk_params.Body]),
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
    ) -> SgiGetResponse:
        """
        Service operation to get a single SGI record by its unique ID passed as a path
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
            f"/udl/sgi/{id}",
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
                    sgi_get_params.SgiGetParams,
                ),
            ),
            cast_to=SgiGetResponse,
        )

    async def get_data_by_effective_as_of_date(
        self,
        *,
        effective_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        sgi_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SgiGetDataByEffectiveAsOfDateResponse:
        """
        Service to return matching SGI records as of the effective date.

        Args:
          effective_date: (One or more of fields 'effectiveDate, sgiDate' are required.) ISO8601 UTC Time
              the data was received and processed from the source. Typically a source provides
              solar data for a date window with each transmission including past, present, and
              future predicted values. (YYYY-MM-DDTHH:MM:SS.sssZ)

          sgi_date: (One or more of fields 'effectiveDate, sgiDate' are required.) ISO8601 UTC Time
              of the index value. This could be a past, current, or future predicted value.
              Note: sgiDate defines the start time of the time window for this data record.
              (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/udl/sgi/getSGIDataByEffectiveAsOfDate",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "effective_date": effective_date,
                        "first_result": first_result,
                        "max_results": max_results,
                        "sgi_date": sgi_date,
                    },
                    sgi_get_data_by_effective_as_of_date_params.SgiGetDataByEffectiveAsOfDateParams,
                ),
            ),
            cast_to=SgiGetDataByEffectiveAsOfDateResponse,
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
            "/udl/sgi/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def tuple(
        self,
        *,
        columns: str,
        effective_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        sgi_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SgiTupleResponse:
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

          effective_date: (One or more of fields 'effectiveDate, sgiDate' are required.) ISO8601 UTC Time
              the data was received and processed from the source. Typically a source provides
              solar data for a date window with each transmission including past, present, and
              future predicted values. (YYYY-MM-DDTHH:MM:SS.sssZ)

          sgi_date: (One or more of fields 'effectiveDate, sgiDate' are required.) ISO8601 UTC Time
              of the index value. This could be a past, current, or future predicted value.
              Note: sgiDate defines the start time of the time window for this data record.
              (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/udl/sgi/tuple",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "columns": columns,
                        "effective_date": effective_date,
                        "first_result": first_result,
                        "max_results": max_results,
                        "sgi_date": sgi_date,
                    },
                    sgi_tuple_params.SgiTupleParams,
                ),
            ),
            cast_to=SgiTupleResponse,
        )

    async def unvalidated_publish(
        self,
        *,
        body: Iterable[sgi_unvalidated_publish_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take multiple SGI as a POST body and ingest into the
        database. This operation is intended to be used for automated feeds into UDL. A
        specific role is required to perform this service operation. Please contact the
        UDL team for assistance.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/filedrop/udl-sgi",
            body=await async_maybe_transform(body, Iterable[sgi_unvalidated_publish_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class SgiResourceWithRawResponse:
    def __init__(self, sgi: SgiResource) -> None:
        self._sgi = sgi

        self.create = to_raw_response_wrapper(
            sgi.create,
        )
        self.update = to_raw_response_wrapper(
            sgi.update,
        )
        self.list = to_raw_response_wrapper(
            sgi.list,
        )
        self.delete = to_raw_response_wrapper(
            sgi.delete,
        )
        self.count = to_raw_response_wrapper(
            sgi.count,
        )
        self.create_bulk = to_raw_response_wrapper(
            sgi.create_bulk,
        )
        self.get = to_raw_response_wrapper(
            sgi.get,
        )
        self.get_data_by_effective_as_of_date = to_raw_response_wrapper(
            sgi.get_data_by_effective_as_of_date,
        )
        self.queryhelp = to_raw_response_wrapper(
            sgi.queryhelp,
        )
        self.tuple = to_raw_response_wrapper(
            sgi.tuple,
        )
        self.unvalidated_publish = to_raw_response_wrapper(
            sgi.unvalidated_publish,
        )

    @cached_property
    def history(self) -> HistoryResourceWithRawResponse:
        return HistoryResourceWithRawResponse(self._sgi.history)


class AsyncSgiResourceWithRawResponse:
    def __init__(self, sgi: AsyncSgiResource) -> None:
        self._sgi = sgi

        self.create = async_to_raw_response_wrapper(
            sgi.create,
        )
        self.update = async_to_raw_response_wrapper(
            sgi.update,
        )
        self.list = async_to_raw_response_wrapper(
            sgi.list,
        )
        self.delete = async_to_raw_response_wrapper(
            sgi.delete,
        )
        self.count = async_to_raw_response_wrapper(
            sgi.count,
        )
        self.create_bulk = async_to_raw_response_wrapper(
            sgi.create_bulk,
        )
        self.get = async_to_raw_response_wrapper(
            sgi.get,
        )
        self.get_data_by_effective_as_of_date = async_to_raw_response_wrapper(
            sgi.get_data_by_effective_as_of_date,
        )
        self.queryhelp = async_to_raw_response_wrapper(
            sgi.queryhelp,
        )
        self.tuple = async_to_raw_response_wrapper(
            sgi.tuple,
        )
        self.unvalidated_publish = async_to_raw_response_wrapper(
            sgi.unvalidated_publish,
        )

    @cached_property
    def history(self) -> AsyncHistoryResourceWithRawResponse:
        return AsyncHistoryResourceWithRawResponse(self._sgi.history)


class SgiResourceWithStreamingResponse:
    def __init__(self, sgi: SgiResource) -> None:
        self._sgi = sgi

        self.create = to_streamed_response_wrapper(
            sgi.create,
        )
        self.update = to_streamed_response_wrapper(
            sgi.update,
        )
        self.list = to_streamed_response_wrapper(
            sgi.list,
        )
        self.delete = to_streamed_response_wrapper(
            sgi.delete,
        )
        self.count = to_streamed_response_wrapper(
            sgi.count,
        )
        self.create_bulk = to_streamed_response_wrapper(
            sgi.create_bulk,
        )
        self.get = to_streamed_response_wrapper(
            sgi.get,
        )
        self.get_data_by_effective_as_of_date = to_streamed_response_wrapper(
            sgi.get_data_by_effective_as_of_date,
        )
        self.queryhelp = to_streamed_response_wrapper(
            sgi.queryhelp,
        )
        self.tuple = to_streamed_response_wrapper(
            sgi.tuple,
        )
        self.unvalidated_publish = to_streamed_response_wrapper(
            sgi.unvalidated_publish,
        )

    @cached_property
    def history(self) -> HistoryResourceWithStreamingResponse:
        return HistoryResourceWithStreamingResponse(self._sgi.history)


class AsyncSgiResourceWithStreamingResponse:
    def __init__(self, sgi: AsyncSgiResource) -> None:
        self._sgi = sgi

        self.create = async_to_streamed_response_wrapper(
            sgi.create,
        )
        self.update = async_to_streamed_response_wrapper(
            sgi.update,
        )
        self.list = async_to_streamed_response_wrapper(
            sgi.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            sgi.delete,
        )
        self.count = async_to_streamed_response_wrapper(
            sgi.count,
        )
        self.create_bulk = async_to_streamed_response_wrapper(
            sgi.create_bulk,
        )
        self.get = async_to_streamed_response_wrapper(
            sgi.get,
        )
        self.get_data_by_effective_as_of_date = async_to_streamed_response_wrapper(
            sgi.get_data_by_effective_as_of_date,
        )
        self.queryhelp = async_to_streamed_response_wrapper(
            sgi.queryhelp,
        )
        self.tuple = async_to_streamed_response_wrapper(
            sgi.tuple,
        )
        self.unvalidated_publish = async_to_streamed_response_wrapper(
            sgi.unvalidated_publish,
        )

    @cached_property
    def history(self) -> AsyncHistoryResourceWithStreamingResponse:
        return AsyncHistoryResourceWithStreamingResponse(self._sgi.history)
