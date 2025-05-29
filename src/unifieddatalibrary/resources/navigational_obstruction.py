# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from datetime import date
from typing_extensions import Literal

import httpx

from ..types import (
    navigational_obstruction_get_params,
    navigational_obstruction_list_params,
    navigational_obstruction_count_params,
    navigational_obstruction_tuple_params,
    navigational_obstruction_create_params,
    navigational_obstruction_update_params,
    navigational_obstruction_create_bulk_params,
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
from ..types.navigational_obstruction_get_response import NavigationalObstructionGetResponse
from ..types.navigational_obstruction_list_response import NavigationalObstructionListResponse
from ..types.navigational_obstruction_tuple_response import NavigationalObstructionTupleResponse
from ..types.navigational_obstruction_queryhelp_response import NavigationalObstructionQueryhelpResponse

__all__ = ["NavigationalObstructionResource", "AsyncNavigationalObstructionResource"]


class NavigationalObstructionResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> NavigationalObstructionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return NavigationalObstructionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NavigationalObstructionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return NavigationalObstructionResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        classification_marking: str,
        cycle_date: Union[str, date],
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        obstacle_id: str,
        obstacle_type: str,
        source: str,
        id: str | NotGiven = NOT_GIVEN,
        act_del_code: str | NotGiven = NOT_GIVEN,
        airac_cycle: int | NotGiven = NOT_GIVEN,
        base_airac_cycle: int | NotGiven = NOT_GIVEN,
        baseline_cutoff_date: Union[str, date] | NotGiven = NOT_GIVEN,
        bound_ne_lat: float | NotGiven = NOT_GIVEN,
        bound_ne_lon: float | NotGiven = NOT_GIVEN,
        bound_sw_lat: float | NotGiven = NOT_GIVEN,
        bound_sw_lon: float | NotGiven = NOT_GIVEN,
        country_code: str | NotGiven = NOT_GIVEN,
        cutoff_date: Union[str, date] | NotGiven = NOT_GIVEN,
        data_set_remarks: str | NotGiven = NOT_GIVEN,
        deleting_org: str | NotGiven = NOT_GIVEN,
        deriving_org: str | NotGiven = NOT_GIVEN,
        directivity_code: int | NotGiven = NOT_GIVEN,
        elevation: float | NotGiven = NOT_GIVEN,
        elevation_acc: float | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        facc: str | NotGiven = NOT_GIVEN,
        feature_code: str | NotGiven = NOT_GIVEN,
        feature_description: str | NotGiven = NOT_GIVEN,
        feature_name: str | NotGiven = NOT_GIVEN,
        feature_type: str | NotGiven = NOT_GIVEN,
        height_agl: float | NotGiven = NOT_GIVEN,
        height_agl_acc: float | NotGiven = NOT_GIVEN,
        height_msl: float | NotGiven = NOT_GIVEN,
        height_msl_acc: float | NotGiven = NOT_GIVEN,
        horiz_acc: float | NotGiven = NOT_GIVEN,
        horiz_datum_code: str | NotGiven = NOT_GIVEN,
        init_record_date: Union[str, date] | NotGiven = NOT_GIVEN,
        keys: List[str] | NotGiven = NOT_GIVEN,
        lighting_code: str | NotGiven = NOT_GIVEN,
        line_ne_lat: float | NotGiven = NOT_GIVEN,
        line_ne_lon: float | NotGiven = NOT_GIVEN,
        lines_filename: str | NotGiven = NOT_GIVEN,
        line_sw_lat: float | NotGiven = NOT_GIVEN,
        line_sw_lon: float | NotGiven = NOT_GIVEN,
        min_height_agl: float | NotGiven = NOT_GIVEN,
        mult_obs: str | NotGiven = NOT_GIVEN,
        next_cycle_date: Union[str, date] | NotGiven = NOT_GIVEN,
        num_lines: int | NotGiven = NOT_GIVEN,
        num_obs: int | NotGiven = NOT_GIVEN,
        num_points: int | NotGiven = NOT_GIVEN,
        obstacle_remarks: str | NotGiven = NOT_GIVEN,
        orig_id: str | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        owner_country_code: str | NotGiven = NOT_GIVEN,
        point_lat: float | NotGiven = NOT_GIVEN,
        point_lon: float | NotGiven = NOT_GIVEN,
        points_filename: str | NotGiven = NOT_GIVEN,
        process_code: str | NotGiven = NOT_GIVEN,
        producer: str | NotGiven = NOT_GIVEN,
        province_code: str | NotGiven = NOT_GIVEN,
        quality: str | NotGiven = NOT_GIVEN,
        rev_date: Union[str, date] | NotGiven = NOT_GIVEN,
        seg_end_point: int | NotGiven = NOT_GIVEN,
        seg_num: int | NotGiven = NOT_GIVEN,
        seg_start_point: int | NotGiven = NOT_GIVEN,
        source_date: Union[str, date] | NotGiven = NOT_GIVEN,
        surface_mat_code: str | NotGiven = NOT_GIVEN,
        transaction_code: str | NotGiven = NOT_GIVEN,
        validation_code: int | NotGiven = NOT_GIVEN,
        values: List[str] | NotGiven = NOT_GIVEN,
        vectors_filename: str | NotGiven = NOT_GIVEN,
        wac: str | NotGiven = NOT_GIVEN,
        wac_innr: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single navigational obstruction record as a POST
        body and ingest into the database. A specific role is required to perform this
        service operation. Please contact the UDL team for assistance.

        Args:
          classification_marking: Classification marking of the data in IC/CAPCO Portion-marked format.

          cycle_date: Start date of this obstruction data set's currency, in ISO 8601 date-only
              format.

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

          obstacle_id: The ID of this obstacle.

          obstacle_type: Type of obstacle (e.g. P for point, V for vector, L for line).

          source: Source of the data.

          id: Unique identifier of the record, auto-generated by the system.

          act_del_code: Indicates if this obstacle record is Active (A) or Deleted (D).

          airac_cycle: The Aeronautical Information Regulation and Control (AIRAC) cycle of this
              obstruction data set. The format is YYNN where YY is the last two digits of the
              year and NN is the cycle number.

          base_airac_cycle: The baseline Aeronautical Information Regulation and Control (AIRAC) cycle for
              change sets only. The format is YYNN where YY is the last two digits of the year
              and NN is the cycle number.

          baseline_cutoff_date: Earliest record date possible in this obstruction data set (not the earliest
              data item), in ISO 8601 date-only format (e.g. YYYY-MM-DD). If null, this data
              set is assumed to be a full data pull of holdings until the cutoffDate. If this
              field is populated, this data set only contains updates since the last baseline
              data set.

          bound_ne_lat: WGS-84 latitude of the northeastern boundary for obstructions contained in this
              data set, in degrees. -90 to 90 degrees (negative values south of equator).

          bound_ne_lon: WGS-84 longitude of the northeastern boundary for obstructions contained in this
              data set, in degrees. -180 to 180 degrees (negative values west of Prime
              Meridian).

          bound_sw_lat: WGS-84 latitude of the southwestern boundary for obstructions contained in this
              data set, in degrees. -90 to 90 degrees (negative values south of equator).

          bound_sw_lon: WGS-84 longitude of the southwestern boundary for obstructions contained in this
              data set, in degrees. -180 to 180 degrees (negative values west of Prime
              Meridian).

          country_code: The DoD Standard Country Code designator for the country issuing the diplomatic
              clearance. This field will be set to "OTHR" if the source value does not match a
              UDL Country code value (ISO-3166-ALPHA-2).

          cutoff_date: Latest record date possible in this obstruction data set (not the most recent
              data item), in ISO 8601 date-only format (e.g. YYYY-MM-DD).

          data_set_remarks: Remarks concerning this obstruction's data set.

          deleting_org: The organization that deleted this obstacle record.

          deriving_org: The organization that entered obstacle data other than the producer.

          directivity_code: The side or sides of this obstruction feature which produces the greatest
              reflectivity potential.

          elevation: The elevation at the point obstacle's location in feet.

          elevation_acc: The difference between the assigned elevation of this point and its true
              elevation, in feet.

          external_id: Optional obstacle ID from external systems. This field has no meaning within UDL
              and is provided as a convenience for systems that require tracking of an
              internal system generated ID.

          facc: FACC (Feature and Attribute Coding Catalog) is a five-character code for
              encoding real-world entities and objects. The first letter of the code is an
              alphabetic value from "A" to "Z" which will map to a feature category. The
              second character will map to a subcategory. Characters three to five are numeric
              and range from 000 to 999. This value will provide a unit feature type
              identification within the categories.

          feature_code: Identifying code for the type of this point obstacle.

          feature_description: Description of this obstacle, corresponding to the FACC (Feature and Attribute
              Coding Catalog) value.

          feature_name: Type name of point obstacle.

          feature_type: Identifying code for the type of this point obstacle.

          height_agl: The height Above Ground Level (AGL) of the point obstacle in feet.

          height_agl_acc: The accuracy of the height Above Ground Level (AGL) value for this point
              obstacle, in feet.

          height_msl: The height Above Mean Sea Level (AMSL) of the point obstacle in feet.

          height_msl_acc: The accuracy of the height Above Mean Sea Level (AMSL) value for this point
              obstacle in feet.

          horiz_acc: The difference between the recorded horizontal coordinates of this point
              obstacle and its true position, in feet.

          horiz_datum_code: Code representing the mathematical model of Earth used to calculate coordinates
              for this obstacle (e.g. WGS-84, U for undetermined, etc.). US Forces use the
              World Geodetic System 1984 (WGS-84), but also use maps by allied countries with
              local datums.

          init_record_date: Date this obstacle was initially added to the data set, in ISO 8601 date-only
              format (ex. YYYY-MM-DD).

          keys: This field provides an array of keys that can be added to any obstruction
              feature to provide information that is not already supported. The entries in
              this array must correspond to the position index in the values array. This array
              must be the same length as values.

          lighting_code: Code specifying if this obstacle is lit (e.g. Y = Yes, N = No, U = Unknown).

          line_ne_lat: WGS-84 latitude of the northeastern point of the line, in degrees. -90 to 90
              degrees (negative values south of equator).

          line_ne_lon: WGS-84 longitude of the northeastern point of the line, in degrees. -180 to 180
              degrees (negative values west of Prime Meridian).

          lines_filename: The name of the line file associated with this obstruction data set.

          line_sw_lat: WGS-84 latitude of the southwestern point of the line, in degrees. -90 to 90
              degrees (negative values south of equator).

          line_sw_lon: WGS-84 longitude of the southwestern point of the line, in degrees. -180 to 180
              degrees (negative values west of Prime Meridian).

          min_height_agl: The minimum height Above Ground Level (AGL) of the shortest obstruction
              contained in this data set, in feet.

          mult_obs: Indicates if the feature has multiple obstructions (e.g. S = Single, M =
              Multiple, U = Undetermined).

          next_cycle_date: The date after which this obstruction data set’s currency is stale and should be
              refreshed, in ISO 8601 date-only format (e.g. YYYY-MM-DD).

          num_lines: The number of line features associated with this obstruction data set.

          num_obs: Indicates the number of obstructions associated with a feature.

          num_points: The number of point features associated with this obstruction data set.

          obstacle_remarks: Remarks regarding this obstacle.

          orig_id: The original ID for this obstacle.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          owner_country_code: The DoD Standard Country Code designator for the country or political entity
              that owns the data set associated with this obstruction. This field will be set
              to "OTHR" if the source value does not match a UDL Country code value
              (ISO-3166-ALPHA-2).

          point_lat: WGS-84 latitude of this point obstacle, in degrees. -90 to 90 degrees (negative
              values south of equator).

          point_lon: WGS-84 longitude of this point obstacle, in degrees. -180 to 180 degrees
              (negative values west of Prime Meridian).

          points_filename: The name of the point file associated with this obstruction data set.

          process_code: Code denoting the action, review, or process that updated this obstacle.

          producer: Name of the agency that produced this obstruction data set.

          province_code: The Federal Information Processing Standards (FIPS) state/province numeric code
              of this obstacle's location.

          quality: When horizontal and/or vertical accuracy requirements cannot be met because of
              inadequate source material, this code indicates the quality of the data.

          rev_date: Date this obstacle data was revised, in ISO 8601 date-only format (ex.
              YYYY-MM-DD).

          seg_end_point: ID of the end point of a line segment.

          seg_num: Identifies the sequence number of a line segment.

          seg_start_point: ID of the starting point of a line segment.

          source_date: Source date of this obstacle data, in ISO 8601 date-only format (ex.
              YYYY-MM-DD).

          surface_mat_code: The surface material composition code of this point obstacle.

          transaction_code: The transaction type/code for this obstacle (e.g. "D", "N", "R", "S", "V", "X").

          validation_code: Method used to confirm the existence of this obstacle.

          values: This field provides an array of values that can be added to any obstruction
              feature to provide information that is not already supported. The entries in
              this array must correspond to the position index in the keys array. This array
              must be the same length as keys.

          vectors_filename: The name of the vector file associated with this obstruction data set.

          wac: The World Aeronautical Chart (WAC) identifier for the area in which this
              obstacle is located.

          wac_innr: This obstacle's World Area Code installation number (WAC-INNR).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/udl/navigationalobstruction",
            body=maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "cycle_date": cycle_date,
                    "data_mode": data_mode,
                    "obstacle_id": obstacle_id,
                    "obstacle_type": obstacle_type,
                    "source": source,
                    "id": id,
                    "act_del_code": act_del_code,
                    "airac_cycle": airac_cycle,
                    "base_airac_cycle": base_airac_cycle,
                    "baseline_cutoff_date": baseline_cutoff_date,
                    "bound_ne_lat": bound_ne_lat,
                    "bound_ne_lon": bound_ne_lon,
                    "bound_sw_lat": bound_sw_lat,
                    "bound_sw_lon": bound_sw_lon,
                    "country_code": country_code,
                    "cutoff_date": cutoff_date,
                    "data_set_remarks": data_set_remarks,
                    "deleting_org": deleting_org,
                    "deriving_org": deriving_org,
                    "directivity_code": directivity_code,
                    "elevation": elevation,
                    "elevation_acc": elevation_acc,
                    "external_id": external_id,
                    "facc": facc,
                    "feature_code": feature_code,
                    "feature_description": feature_description,
                    "feature_name": feature_name,
                    "feature_type": feature_type,
                    "height_agl": height_agl,
                    "height_agl_acc": height_agl_acc,
                    "height_msl": height_msl,
                    "height_msl_acc": height_msl_acc,
                    "horiz_acc": horiz_acc,
                    "horiz_datum_code": horiz_datum_code,
                    "init_record_date": init_record_date,
                    "keys": keys,
                    "lighting_code": lighting_code,
                    "line_ne_lat": line_ne_lat,
                    "line_ne_lon": line_ne_lon,
                    "lines_filename": lines_filename,
                    "line_sw_lat": line_sw_lat,
                    "line_sw_lon": line_sw_lon,
                    "min_height_agl": min_height_agl,
                    "mult_obs": mult_obs,
                    "next_cycle_date": next_cycle_date,
                    "num_lines": num_lines,
                    "num_obs": num_obs,
                    "num_points": num_points,
                    "obstacle_remarks": obstacle_remarks,
                    "orig_id": orig_id,
                    "origin": origin,
                    "owner_country_code": owner_country_code,
                    "point_lat": point_lat,
                    "point_lon": point_lon,
                    "points_filename": points_filename,
                    "process_code": process_code,
                    "producer": producer,
                    "province_code": province_code,
                    "quality": quality,
                    "rev_date": rev_date,
                    "seg_end_point": seg_end_point,
                    "seg_num": seg_num,
                    "seg_start_point": seg_start_point,
                    "source_date": source_date,
                    "surface_mat_code": surface_mat_code,
                    "transaction_code": transaction_code,
                    "validation_code": validation_code,
                    "values": values,
                    "vectors_filename": vectors_filename,
                    "wac": wac,
                    "wac_innr": wac_innr,
                },
                navigational_obstruction_create_params.NavigationalObstructionCreateParams,
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
        cycle_date: Union[str, date],
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        obstacle_id: str,
        obstacle_type: str,
        source: str,
        body_id: str | NotGiven = NOT_GIVEN,
        act_del_code: str | NotGiven = NOT_GIVEN,
        airac_cycle: int | NotGiven = NOT_GIVEN,
        base_airac_cycle: int | NotGiven = NOT_GIVEN,
        baseline_cutoff_date: Union[str, date] | NotGiven = NOT_GIVEN,
        bound_ne_lat: float | NotGiven = NOT_GIVEN,
        bound_ne_lon: float | NotGiven = NOT_GIVEN,
        bound_sw_lat: float | NotGiven = NOT_GIVEN,
        bound_sw_lon: float | NotGiven = NOT_GIVEN,
        country_code: str | NotGiven = NOT_GIVEN,
        cutoff_date: Union[str, date] | NotGiven = NOT_GIVEN,
        data_set_remarks: str | NotGiven = NOT_GIVEN,
        deleting_org: str | NotGiven = NOT_GIVEN,
        deriving_org: str | NotGiven = NOT_GIVEN,
        directivity_code: int | NotGiven = NOT_GIVEN,
        elevation: float | NotGiven = NOT_GIVEN,
        elevation_acc: float | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        facc: str | NotGiven = NOT_GIVEN,
        feature_code: str | NotGiven = NOT_GIVEN,
        feature_description: str | NotGiven = NOT_GIVEN,
        feature_name: str | NotGiven = NOT_GIVEN,
        feature_type: str | NotGiven = NOT_GIVEN,
        height_agl: float | NotGiven = NOT_GIVEN,
        height_agl_acc: float | NotGiven = NOT_GIVEN,
        height_msl: float | NotGiven = NOT_GIVEN,
        height_msl_acc: float | NotGiven = NOT_GIVEN,
        horiz_acc: float | NotGiven = NOT_GIVEN,
        horiz_datum_code: str | NotGiven = NOT_GIVEN,
        init_record_date: Union[str, date] | NotGiven = NOT_GIVEN,
        keys: List[str] | NotGiven = NOT_GIVEN,
        lighting_code: str | NotGiven = NOT_GIVEN,
        line_ne_lat: float | NotGiven = NOT_GIVEN,
        line_ne_lon: float | NotGiven = NOT_GIVEN,
        lines_filename: str | NotGiven = NOT_GIVEN,
        line_sw_lat: float | NotGiven = NOT_GIVEN,
        line_sw_lon: float | NotGiven = NOT_GIVEN,
        min_height_agl: float | NotGiven = NOT_GIVEN,
        mult_obs: str | NotGiven = NOT_GIVEN,
        next_cycle_date: Union[str, date] | NotGiven = NOT_GIVEN,
        num_lines: int | NotGiven = NOT_GIVEN,
        num_obs: int | NotGiven = NOT_GIVEN,
        num_points: int | NotGiven = NOT_GIVEN,
        obstacle_remarks: str | NotGiven = NOT_GIVEN,
        orig_id: str | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        owner_country_code: str | NotGiven = NOT_GIVEN,
        point_lat: float | NotGiven = NOT_GIVEN,
        point_lon: float | NotGiven = NOT_GIVEN,
        points_filename: str | NotGiven = NOT_GIVEN,
        process_code: str | NotGiven = NOT_GIVEN,
        producer: str | NotGiven = NOT_GIVEN,
        province_code: str | NotGiven = NOT_GIVEN,
        quality: str | NotGiven = NOT_GIVEN,
        rev_date: Union[str, date] | NotGiven = NOT_GIVEN,
        seg_end_point: int | NotGiven = NOT_GIVEN,
        seg_num: int | NotGiven = NOT_GIVEN,
        seg_start_point: int | NotGiven = NOT_GIVEN,
        source_date: Union[str, date] | NotGiven = NOT_GIVEN,
        surface_mat_code: str | NotGiven = NOT_GIVEN,
        transaction_code: str | NotGiven = NOT_GIVEN,
        validation_code: int | NotGiven = NOT_GIVEN,
        values: List[str] | NotGiven = NOT_GIVEN,
        vectors_filename: str | NotGiven = NOT_GIVEN,
        wac: str | NotGiven = NOT_GIVEN,
        wac_innr: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Service operation to update a single navigational obstruction record.

        A specific
        role is required to perform this service operation. Please contact the UDL team
        for assistance.

        Args:
          classification_marking: Classification marking of the data in IC/CAPCO Portion-marked format.

          cycle_date: Start date of this obstruction data set's currency, in ISO 8601 date-only
              format.

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

          obstacle_id: The ID of this obstacle.

          obstacle_type: Type of obstacle (e.g. P for point, V for vector, L for line).

          source: Source of the data.

          body_id: Unique identifier of the record, auto-generated by the system.

          act_del_code: Indicates if this obstacle record is Active (A) or Deleted (D).

          airac_cycle: The Aeronautical Information Regulation and Control (AIRAC) cycle of this
              obstruction data set. The format is YYNN where YY is the last two digits of the
              year and NN is the cycle number.

          base_airac_cycle: The baseline Aeronautical Information Regulation and Control (AIRAC) cycle for
              change sets only. The format is YYNN where YY is the last two digits of the year
              and NN is the cycle number.

          baseline_cutoff_date: Earliest record date possible in this obstruction data set (not the earliest
              data item), in ISO 8601 date-only format (e.g. YYYY-MM-DD). If null, this data
              set is assumed to be a full data pull of holdings until the cutoffDate. If this
              field is populated, this data set only contains updates since the last baseline
              data set.

          bound_ne_lat: WGS-84 latitude of the northeastern boundary for obstructions contained in this
              data set, in degrees. -90 to 90 degrees (negative values south of equator).

          bound_ne_lon: WGS-84 longitude of the northeastern boundary for obstructions contained in this
              data set, in degrees. -180 to 180 degrees (negative values west of Prime
              Meridian).

          bound_sw_lat: WGS-84 latitude of the southwestern boundary for obstructions contained in this
              data set, in degrees. -90 to 90 degrees (negative values south of equator).

          bound_sw_lon: WGS-84 longitude of the southwestern boundary for obstructions contained in this
              data set, in degrees. -180 to 180 degrees (negative values west of Prime
              Meridian).

          country_code: The DoD Standard Country Code designator for the country issuing the diplomatic
              clearance. This field will be set to "OTHR" if the source value does not match a
              UDL Country code value (ISO-3166-ALPHA-2).

          cutoff_date: Latest record date possible in this obstruction data set (not the most recent
              data item), in ISO 8601 date-only format (e.g. YYYY-MM-DD).

          data_set_remarks: Remarks concerning this obstruction's data set.

          deleting_org: The organization that deleted this obstacle record.

          deriving_org: The organization that entered obstacle data other than the producer.

          directivity_code: The side or sides of this obstruction feature which produces the greatest
              reflectivity potential.

          elevation: The elevation at the point obstacle's location in feet.

          elevation_acc: The difference between the assigned elevation of this point and its true
              elevation, in feet.

          external_id: Optional obstacle ID from external systems. This field has no meaning within UDL
              and is provided as a convenience for systems that require tracking of an
              internal system generated ID.

          facc: FACC (Feature and Attribute Coding Catalog) is a five-character code for
              encoding real-world entities and objects. The first letter of the code is an
              alphabetic value from "A" to "Z" which will map to a feature category. The
              second character will map to a subcategory. Characters three to five are numeric
              and range from 000 to 999. This value will provide a unit feature type
              identification within the categories.

          feature_code: Identifying code for the type of this point obstacle.

          feature_description: Description of this obstacle, corresponding to the FACC (Feature and Attribute
              Coding Catalog) value.

          feature_name: Type name of point obstacle.

          feature_type: Identifying code for the type of this point obstacle.

          height_agl: The height Above Ground Level (AGL) of the point obstacle in feet.

          height_agl_acc: The accuracy of the height Above Ground Level (AGL) value for this point
              obstacle, in feet.

          height_msl: The height Above Mean Sea Level (AMSL) of the point obstacle in feet.

          height_msl_acc: The accuracy of the height Above Mean Sea Level (AMSL) value for this point
              obstacle in feet.

          horiz_acc: The difference between the recorded horizontal coordinates of this point
              obstacle and its true position, in feet.

          horiz_datum_code: Code representing the mathematical model of Earth used to calculate coordinates
              for this obstacle (e.g. WGS-84, U for undetermined, etc.). US Forces use the
              World Geodetic System 1984 (WGS-84), but also use maps by allied countries with
              local datums.

          init_record_date: Date this obstacle was initially added to the data set, in ISO 8601 date-only
              format (ex. YYYY-MM-DD).

          keys: This field provides an array of keys that can be added to any obstruction
              feature to provide information that is not already supported. The entries in
              this array must correspond to the position index in the values array. This array
              must be the same length as values.

          lighting_code: Code specifying if this obstacle is lit (e.g. Y = Yes, N = No, U = Unknown).

          line_ne_lat: WGS-84 latitude of the northeastern point of the line, in degrees. -90 to 90
              degrees (negative values south of equator).

          line_ne_lon: WGS-84 longitude of the northeastern point of the line, in degrees. -180 to 180
              degrees (negative values west of Prime Meridian).

          lines_filename: The name of the line file associated with this obstruction data set.

          line_sw_lat: WGS-84 latitude of the southwestern point of the line, in degrees. -90 to 90
              degrees (negative values south of equator).

          line_sw_lon: WGS-84 longitude of the southwestern point of the line, in degrees. -180 to 180
              degrees (negative values west of Prime Meridian).

          min_height_agl: The minimum height Above Ground Level (AGL) of the shortest obstruction
              contained in this data set, in feet.

          mult_obs: Indicates if the feature has multiple obstructions (e.g. S = Single, M =
              Multiple, U = Undetermined).

          next_cycle_date: The date after which this obstruction data set’s currency is stale and should be
              refreshed, in ISO 8601 date-only format (e.g. YYYY-MM-DD).

          num_lines: The number of line features associated with this obstruction data set.

          num_obs: Indicates the number of obstructions associated with a feature.

          num_points: The number of point features associated with this obstruction data set.

          obstacle_remarks: Remarks regarding this obstacle.

          orig_id: The original ID for this obstacle.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          owner_country_code: The DoD Standard Country Code designator for the country or political entity
              that owns the data set associated with this obstruction. This field will be set
              to "OTHR" if the source value does not match a UDL Country code value
              (ISO-3166-ALPHA-2).

          point_lat: WGS-84 latitude of this point obstacle, in degrees. -90 to 90 degrees (negative
              values south of equator).

          point_lon: WGS-84 longitude of this point obstacle, in degrees. -180 to 180 degrees
              (negative values west of Prime Meridian).

          points_filename: The name of the point file associated with this obstruction data set.

          process_code: Code denoting the action, review, or process that updated this obstacle.

          producer: Name of the agency that produced this obstruction data set.

          province_code: The Federal Information Processing Standards (FIPS) state/province numeric code
              of this obstacle's location.

          quality: When horizontal and/or vertical accuracy requirements cannot be met because of
              inadequate source material, this code indicates the quality of the data.

          rev_date: Date this obstacle data was revised, in ISO 8601 date-only format (ex.
              YYYY-MM-DD).

          seg_end_point: ID of the end point of a line segment.

          seg_num: Identifies the sequence number of a line segment.

          seg_start_point: ID of the starting point of a line segment.

          source_date: Source date of this obstacle data, in ISO 8601 date-only format (ex.
              YYYY-MM-DD).

          surface_mat_code: The surface material composition code of this point obstacle.

          transaction_code: The transaction type/code for this obstacle (e.g. "D", "N", "R", "S", "V", "X").

          validation_code: Method used to confirm the existence of this obstacle.

          values: This field provides an array of values that can be added to any obstruction
              feature to provide information that is not already supported. The entries in
              this array must correspond to the position index in the keys array. This array
              must be the same length as keys.

          vectors_filename: The name of the vector file associated with this obstruction data set.

          wac: The World Aeronautical Chart (WAC) identifier for the area in which this
              obstacle is located.

          wac_innr: This obstacle's World Area Code installation number (WAC-INNR).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            f"/udl/navigationalobstruction/{path_id}",
            body=maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "cycle_date": cycle_date,
                    "data_mode": data_mode,
                    "obstacle_id": obstacle_id,
                    "obstacle_type": obstacle_type,
                    "source": source,
                    "body_id": body_id,
                    "act_del_code": act_del_code,
                    "airac_cycle": airac_cycle,
                    "base_airac_cycle": base_airac_cycle,
                    "baseline_cutoff_date": baseline_cutoff_date,
                    "bound_ne_lat": bound_ne_lat,
                    "bound_ne_lon": bound_ne_lon,
                    "bound_sw_lat": bound_sw_lat,
                    "bound_sw_lon": bound_sw_lon,
                    "country_code": country_code,
                    "cutoff_date": cutoff_date,
                    "data_set_remarks": data_set_remarks,
                    "deleting_org": deleting_org,
                    "deriving_org": deriving_org,
                    "directivity_code": directivity_code,
                    "elevation": elevation,
                    "elevation_acc": elevation_acc,
                    "external_id": external_id,
                    "facc": facc,
                    "feature_code": feature_code,
                    "feature_description": feature_description,
                    "feature_name": feature_name,
                    "feature_type": feature_type,
                    "height_agl": height_agl,
                    "height_agl_acc": height_agl_acc,
                    "height_msl": height_msl,
                    "height_msl_acc": height_msl_acc,
                    "horiz_acc": horiz_acc,
                    "horiz_datum_code": horiz_datum_code,
                    "init_record_date": init_record_date,
                    "keys": keys,
                    "lighting_code": lighting_code,
                    "line_ne_lat": line_ne_lat,
                    "line_ne_lon": line_ne_lon,
                    "lines_filename": lines_filename,
                    "line_sw_lat": line_sw_lat,
                    "line_sw_lon": line_sw_lon,
                    "min_height_agl": min_height_agl,
                    "mult_obs": mult_obs,
                    "next_cycle_date": next_cycle_date,
                    "num_lines": num_lines,
                    "num_obs": num_obs,
                    "num_points": num_points,
                    "obstacle_remarks": obstacle_remarks,
                    "orig_id": orig_id,
                    "origin": origin,
                    "owner_country_code": owner_country_code,
                    "point_lat": point_lat,
                    "point_lon": point_lon,
                    "points_filename": points_filename,
                    "process_code": process_code,
                    "producer": producer,
                    "province_code": province_code,
                    "quality": quality,
                    "rev_date": rev_date,
                    "seg_end_point": seg_end_point,
                    "seg_num": seg_num,
                    "seg_start_point": seg_start_point,
                    "source_date": source_date,
                    "surface_mat_code": surface_mat_code,
                    "transaction_code": transaction_code,
                    "validation_code": validation_code,
                    "values": values,
                    "vectors_filename": vectors_filename,
                    "wac": wac,
                    "wac_innr": wac_innr,
                },
                navigational_obstruction_update_params.NavigationalObstructionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        *,
        cycle_date: Union[str, date] | NotGiven = NOT_GIVEN,
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        obstacle_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncOffsetPage[NavigationalObstructionListResponse]:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          cycle_date: (One or more of fields 'cycleDate, obstacleId' are required.) Start date of this
              obstruction data set's currency, in ISO 8601 date-only format. (YYYY-MM-DD)

          obstacle_id: (One or more of fields 'cycleDate, obstacleId' are required.) The ID of this
              obstacle.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/navigationalobstruction",
            page=SyncOffsetPage[NavigationalObstructionListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cycle_date": cycle_date,
                        "first_result": first_result,
                        "max_results": max_results,
                        "obstacle_id": obstacle_id,
                    },
                    navigational_obstruction_list_params.NavigationalObstructionListParams,
                ),
            ),
            model=NavigationalObstructionListResponse,
        )

    def count(
        self,
        *,
        cycle_date: Union[str, date] | NotGiven = NOT_GIVEN,
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        obstacle_id: str | NotGiven = NOT_GIVEN,
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
          cycle_date: (One or more of fields 'cycleDate, obstacleId' are required.) Start date of this
              obstruction data set's currency, in ISO 8601 date-only format. (YYYY-MM-DD)

          obstacle_id: (One or more of fields 'cycleDate, obstacleId' are required.) The ID of this
              obstacle.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return self._get(
            "/udl/navigationalobstruction/count",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cycle_date": cycle_date,
                        "first_result": first_result,
                        "max_results": max_results,
                        "obstacle_id": obstacle_id,
                    },
                    navigational_obstruction_count_params.NavigationalObstructionCountParams,
                ),
            ),
            cast_to=str,
        )

    def create_bulk(
        self,
        *,
        body: Iterable[navigational_obstruction_create_bulk_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation intended for initial integration only, to take a list of
        navigational obstruction records as a POST body and ingest into the database.
        This operation is not intended to be used for automated feeds into UDL. Data
        providers should contact the UDL team for specific role assignments and for
        instructions on setting up a permanent feed through an alternate mechanism.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/udl/navigationalobstruction/createBulk",
            body=maybe_transform(body, Iterable[navigational_obstruction_create_bulk_params.Body]),
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
    ) -> NavigationalObstructionGetResponse:
        """
        Service operation to get a single navigational obstruction record by its unique
        ID passed as a path parameter.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/udl/navigationalobstruction/{id}",
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
                    navigational_obstruction_get_params.NavigationalObstructionGetParams,
                ),
            ),
            cast_to=NavigationalObstructionGetResponse,
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
    ) -> NavigationalObstructionQueryhelpResponse:
        """
        Service operation to provide detailed information on available dynamic query
        parameters for a particular data type.
        """
        return self._get(
            "/udl/navigationalobstruction/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NavigationalObstructionQueryhelpResponse,
        )

    def tuple(
        self,
        *,
        columns: str,
        cycle_date: Union[str, date] | NotGiven = NOT_GIVEN,
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        obstacle_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NavigationalObstructionTupleResponse:
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

          cycle_date: (One or more of fields 'cycleDate, obstacleId' are required.) Start date of this
              obstruction data set's currency, in ISO 8601 date-only format. (YYYY-MM-DD)

          obstacle_id: (One or more of fields 'cycleDate, obstacleId' are required.) The ID of this
              obstacle.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/udl/navigationalobstruction/tuple",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "columns": columns,
                        "cycle_date": cycle_date,
                        "first_result": first_result,
                        "max_results": max_results,
                        "obstacle_id": obstacle_id,
                    },
                    navigational_obstruction_tuple_params.NavigationalObstructionTupleParams,
                ),
            ),
            cast_to=NavigationalObstructionTupleResponse,
        )


class AsyncNavigationalObstructionResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncNavigationalObstructionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncNavigationalObstructionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNavigationalObstructionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncNavigationalObstructionResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        classification_marking: str,
        cycle_date: Union[str, date],
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        obstacle_id: str,
        obstacle_type: str,
        source: str,
        id: str | NotGiven = NOT_GIVEN,
        act_del_code: str | NotGiven = NOT_GIVEN,
        airac_cycle: int | NotGiven = NOT_GIVEN,
        base_airac_cycle: int | NotGiven = NOT_GIVEN,
        baseline_cutoff_date: Union[str, date] | NotGiven = NOT_GIVEN,
        bound_ne_lat: float | NotGiven = NOT_GIVEN,
        bound_ne_lon: float | NotGiven = NOT_GIVEN,
        bound_sw_lat: float | NotGiven = NOT_GIVEN,
        bound_sw_lon: float | NotGiven = NOT_GIVEN,
        country_code: str | NotGiven = NOT_GIVEN,
        cutoff_date: Union[str, date] | NotGiven = NOT_GIVEN,
        data_set_remarks: str | NotGiven = NOT_GIVEN,
        deleting_org: str | NotGiven = NOT_GIVEN,
        deriving_org: str | NotGiven = NOT_GIVEN,
        directivity_code: int | NotGiven = NOT_GIVEN,
        elevation: float | NotGiven = NOT_GIVEN,
        elevation_acc: float | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        facc: str | NotGiven = NOT_GIVEN,
        feature_code: str | NotGiven = NOT_GIVEN,
        feature_description: str | NotGiven = NOT_GIVEN,
        feature_name: str | NotGiven = NOT_GIVEN,
        feature_type: str | NotGiven = NOT_GIVEN,
        height_agl: float | NotGiven = NOT_GIVEN,
        height_agl_acc: float | NotGiven = NOT_GIVEN,
        height_msl: float | NotGiven = NOT_GIVEN,
        height_msl_acc: float | NotGiven = NOT_GIVEN,
        horiz_acc: float | NotGiven = NOT_GIVEN,
        horiz_datum_code: str | NotGiven = NOT_GIVEN,
        init_record_date: Union[str, date] | NotGiven = NOT_GIVEN,
        keys: List[str] | NotGiven = NOT_GIVEN,
        lighting_code: str | NotGiven = NOT_GIVEN,
        line_ne_lat: float | NotGiven = NOT_GIVEN,
        line_ne_lon: float | NotGiven = NOT_GIVEN,
        lines_filename: str | NotGiven = NOT_GIVEN,
        line_sw_lat: float | NotGiven = NOT_GIVEN,
        line_sw_lon: float | NotGiven = NOT_GIVEN,
        min_height_agl: float | NotGiven = NOT_GIVEN,
        mult_obs: str | NotGiven = NOT_GIVEN,
        next_cycle_date: Union[str, date] | NotGiven = NOT_GIVEN,
        num_lines: int | NotGiven = NOT_GIVEN,
        num_obs: int | NotGiven = NOT_GIVEN,
        num_points: int | NotGiven = NOT_GIVEN,
        obstacle_remarks: str | NotGiven = NOT_GIVEN,
        orig_id: str | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        owner_country_code: str | NotGiven = NOT_GIVEN,
        point_lat: float | NotGiven = NOT_GIVEN,
        point_lon: float | NotGiven = NOT_GIVEN,
        points_filename: str | NotGiven = NOT_GIVEN,
        process_code: str | NotGiven = NOT_GIVEN,
        producer: str | NotGiven = NOT_GIVEN,
        province_code: str | NotGiven = NOT_GIVEN,
        quality: str | NotGiven = NOT_GIVEN,
        rev_date: Union[str, date] | NotGiven = NOT_GIVEN,
        seg_end_point: int | NotGiven = NOT_GIVEN,
        seg_num: int | NotGiven = NOT_GIVEN,
        seg_start_point: int | NotGiven = NOT_GIVEN,
        source_date: Union[str, date] | NotGiven = NOT_GIVEN,
        surface_mat_code: str | NotGiven = NOT_GIVEN,
        transaction_code: str | NotGiven = NOT_GIVEN,
        validation_code: int | NotGiven = NOT_GIVEN,
        values: List[str] | NotGiven = NOT_GIVEN,
        vectors_filename: str | NotGiven = NOT_GIVEN,
        wac: str | NotGiven = NOT_GIVEN,
        wac_innr: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single navigational obstruction record as a POST
        body and ingest into the database. A specific role is required to perform this
        service operation. Please contact the UDL team for assistance.

        Args:
          classification_marking: Classification marking of the data in IC/CAPCO Portion-marked format.

          cycle_date: Start date of this obstruction data set's currency, in ISO 8601 date-only
              format.

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

          obstacle_id: The ID of this obstacle.

          obstacle_type: Type of obstacle (e.g. P for point, V for vector, L for line).

          source: Source of the data.

          id: Unique identifier of the record, auto-generated by the system.

          act_del_code: Indicates if this obstacle record is Active (A) or Deleted (D).

          airac_cycle: The Aeronautical Information Regulation and Control (AIRAC) cycle of this
              obstruction data set. The format is YYNN where YY is the last two digits of the
              year and NN is the cycle number.

          base_airac_cycle: The baseline Aeronautical Information Regulation and Control (AIRAC) cycle for
              change sets only. The format is YYNN where YY is the last two digits of the year
              and NN is the cycle number.

          baseline_cutoff_date: Earliest record date possible in this obstruction data set (not the earliest
              data item), in ISO 8601 date-only format (e.g. YYYY-MM-DD). If null, this data
              set is assumed to be a full data pull of holdings until the cutoffDate. If this
              field is populated, this data set only contains updates since the last baseline
              data set.

          bound_ne_lat: WGS-84 latitude of the northeastern boundary for obstructions contained in this
              data set, in degrees. -90 to 90 degrees (negative values south of equator).

          bound_ne_lon: WGS-84 longitude of the northeastern boundary for obstructions contained in this
              data set, in degrees. -180 to 180 degrees (negative values west of Prime
              Meridian).

          bound_sw_lat: WGS-84 latitude of the southwestern boundary for obstructions contained in this
              data set, in degrees. -90 to 90 degrees (negative values south of equator).

          bound_sw_lon: WGS-84 longitude of the southwestern boundary for obstructions contained in this
              data set, in degrees. -180 to 180 degrees (negative values west of Prime
              Meridian).

          country_code: The DoD Standard Country Code designator for the country issuing the diplomatic
              clearance. This field will be set to "OTHR" if the source value does not match a
              UDL Country code value (ISO-3166-ALPHA-2).

          cutoff_date: Latest record date possible in this obstruction data set (not the most recent
              data item), in ISO 8601 date-only format (e.g. YYYY-MM-DD).

          data_set_remarks: Remarks concerning this obstruction's data set.

          deleting_org: The organization that deleted this obstacle record.

          deriving_org: The organization that entered obstacle data other than the producer.

          directivity_code: The side or sides of this obstruction feature which produces the greatest
              reflectivity potential.

          elevation: The elevation at the point obstacle's location in feet.

          elevation_acc: The difference between the assigned elevation of this point and its true
              elevation, in feet.

          external_id: Optional obstacle ID from external systems. This field has no meaning within UDL
              and is provided as a convenience for systems that require tracking of an
              internal system generated ID.

          facc: FACC (Feature and Attribute Coding Catalog) is a five-character code for
              encoding real-world entities and objects. The first letter of the code is an
              alphabetic value from "A" to "Z" which will map to a feature category. The
              second character will map to a subcategory. Characters three to five are numeric
              and range from 000 to 999. This value will provide a unit feature type
              identification within the categories.

          feature_code: Identifying code for the type of this point obstacle.

          feature_description: Description of this obstacle, corresponding to the FACC (Feature and Attribute
              Coding Catalog) value.

          feature_name: Type name of point obstacle.

          feature_type: Identifying code for the type of this point obstacle.

          height_agl: The height Above Ground Level (AGL) of the point obstacle in feet.

          height_agl_acc: The accuracy of the height Above Ground Level (AGL) value for this point
              obstacle, in feet.

          height_msl: The height Above Mean Sea Level (AMSL) of the point obstacle in feet.

          height_msl_acc: The accuracy of the height Above Mean Sea Level (AMSL) value for this point
              obstacle in feet.

          horiz_acc: The difference between the recorded horizontal coordinates of this point
              obstacle and its true position, in feet.

          horiz_datum_code: Code representing the mathematical model of Earth used to calculate coordinates
              for this obstacle (e.g. WGS-84, U for undetermined, etc.). US Forces use the
              World Geodetic System 1984 (WGS-84), but also use maps by allied countries with
              local datums.

          init_record_date: Date this obstacle was initially added to the data set, in ISO 8601 date-only
              format (ex. YYYY-MM-DD).

          keys: This field provides an array of keys that can be added to any obstruction
              feature to provide information that is not already supported. The entries in
              this array must correspond to the position index in the values array. This array
              must be the same length as values.

          lighting_code: Code specifying if this obstacle is lit (e.g. Y = Yes, N = No, U = Unknown).

          line_ne_lat: WGS-84 latitude of the northeastern point of the line, in degrees. -90 to 90
              degrees (negative values south of equator).

          line_ne_lon: WGS-84 longitude of the northeastern point of the line, in degrees. -180 to 180
              degrees (negative values west of Prime Meridian).

          lines_filename: The name of the line file associated with this obstruction data set.

          line_sw_lat: WGS-84 latitude of the southwestern point of the line, in degrees. -90 to 90
              degrees (negative values south of equator).

          line_sw_lon: WGS-84 longitude of the southwestern point of the line, in degrees. -180 to 180
              degrees (negative values west of Prime Meridian).

          min_height_agl: The minimum height Above Ground Level (AGL) of the shortest obstruction
              contained in this data set, in feet.

          mult_obs: Indicates if the feature has multiple obstructions (e.g. S = Single, M =
              Multiple, U = Undetermined).

          next_cycle_date: The date after which this obstruction data set’s currency is stale and should be
              refreshed, in ISO 8601 date-only format (e.g. YYYY-MM-DD).

          num_lines: The number of line features associated with this obstruction data set.

          num_obs: Indicates the number of obstructions associated with a feature.

          num_points: The number of point features associated with this obstruction data set.

          obstacle_remarks: Remarks regarding this obstacle.

          orig_id: The original ID for this obstacle.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          owner_country_code: The DoD Standard Country Code designator for the country or political entity
              that owns the data set associated with this obstruction. This field will be set
              to "OTHR" if the source value does not match a UDL Country code value
              (ISO-3166-ALPHA-2).

          point_lat: WGS-84 latitude of this point obstacle, in degrees. -90 to 90 degrees (negative
              values south of equator).

          point_lon: WGS-84 longitude of this point obstacle, in degrees. -180 to 180 degrees
              (negative values west of Prime Meridian).

          points_filename: The name of the point file associated with this obstruction data set.

          process_code: Code denoting the action, review, or process that updated this obstacle.

          producer: Name of the agency that produced this obstruction data set.

          province_code: The Federal Information Processing Standards (FIPS) state/province numeric code
              of this obstacle's location.

          quality: When horizontal and/or vertical accuracy requirements cannot be met because of
              inadequate source material, this code indicates the quality of the data.

          rev_date: Date this obstacle data was revised, in ISO 8601 date-only format (ex.
              YYYY-MM-DD).

          seg_end_point: ID of the end point of a line segment.

          seg_num: Identifies the sequence number of a line segment.

          seg_start_point: ID of the starting point of a line segment.

          source_date: Source date of this obstacle data, in ISO 8601 date-only format (ex.
              YYYY-MM-DD).

          surface_mat_code: The surface material composition code of this point obstacle.

          transaction_code: The transaction type/code for this obstacle (e.g. "D", "N", "R", "S", "V", "X").

          validation_code: Method used to confirm the existence of this obstacle.

          values: This field provides an array of values that can be added to any obstruction
              feature to provide information that is not already supported. The entries in
              this array must correspond to the position index in the keys array. This array
              must be the same length as keys.

          vectors_filename: The name of the vector file associated with this obstruction data set.

          wac: The World Aeronautical Chart (WAC) identifier for the area in which this
              obstacle is located.

          wac_innr: This obstacle's World Area Code installation number (WAC-INNR).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/udl/navigationalobstruction",
            body=await async_maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "cycle_date": cycle_date,
                    "data_mode": data_mode,
                    "obstacle_id": obstacle_id,
                    "obstacle_type": obstacle_type,
                    "source": source,
                    "id": id,
                    "act_del_code": act_del_code,
                    "airac_cycle": airac_cycle,
                    "base_airac_cycle": base_airac_cycle,
                    "baseline_cutoff_date": baseline_cutoff_date,
                    "bound_ne_lat": bound_ne_lat,
                    "bound_ne_lon": bound_ne_lon,
                    "bound_sw_lat": bound_sw_lat,
                    "bound_sw_lon": bound_sw_lon,
                    "country_code": country_code,
                    "cutoff_date": cutoff_date,
                    "data_set_remarks": data_set_remarks,
                    "deleting_org": deleting_org,
                    "deriving_org": deriving_org,
                    "directivity_code": directivity_code,
                    "elevation": elevation,
                    "elevation_acc": elevation_acc,
                    "external_id": external_id,
                    "facc": facc,
                    "feature_code": feature_code,
                    "feature_description": feature_description,
                    "feature_name": feature_name,
                    "feature_type": feature_type,
                    "height_agl": height_agl,
                    "height_agl_acc": height_agl_acc,
                    "height_msl": height_msl,
                    "height_msl_acc": height_msl_acc,
                    "horiz_acc": horiz_acc,
                    "horiz_datum_code": horiz_datum_code,
                    "init_record_date": init_record_date,
                    "keys": keys,
                    "lighting_code": lighting_code,
                    "line_ne_lat": line_ne_lat,
                    "line_ne_lon": line_ne_lon,
                    "lines_filename": lines_filename,
                    "line_sw_lat": line_sw_lat,
                    "line_sw_lon": line_sw_lon,
                    "min_height_agl": min_height_agl,
                    "mult_obs": mult_obs,
                    "next_cycle_date": next_cycle_date,
                    "num_lines": num_lines,
                    "num_obs": num_obs,
                    "num_points": num_points,
                    "obstacle_remarks": obstacle_remarks,
                    "orig_id": orig_id,
                    "origin": origin,
                    "owner_country_code": owner_country_code,
                    "point_lat": point_lat,
                    "point_lon": point_lon,
                    "points_filename": points_filename,
                    "process_code": process_code,
                    "producer": producer,
                    "province_code": province_code,
                    "quality": quality,
                    "rev_date": rev_date,
                    "seg_end_point": seg_end_point,
                    "seg_num": seg_num,
                    "seg_start_point": seg_start_point,
                    "source_date": source_date,
                    "surface_mat_code": surface_mat_code,
                    "transaction_code": transaction_code,
                    "validation_code": validation_code,
                    "values": values,
                    "vectors_filename": vectors_filename,
                    "wac": wac,
                    "wac_innr": wac_innr,
                },
                navigational_obstruction_create_params.NavigationalObstructionCreateParams,
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
        cycle_date: Union[str, date],
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        obstacle_id: str,
        obstacle_type: str,
        source: str,
        body_id: str | NotGiven = NOT_GIVEN,
        act_del_code: str | NotGiven = NOT_GIVEN,
        airac_cycle: int | NotGiven = NOT_GIVEN,
        base_airac_cycle: int | NotGiven = NOT_GIVEN,
        baseline_cutoff_date: Union[str, date] | NotGiven = NOT_GIVEN,
        bound_ne_lat: float | NotGiven = NOT_GIVEN,
        bound_ne_lon: float | NotGiven = NOT_GIVEN,
        bound_sw_lat: float | NotGiven = NOT_GIVEN,
        bound_sw_lon: float | NotGiven = NOT_GIVEN,
        country_code: str | NotGiven = NOT_GIVEN,
        cutoff_date: Union[str, date] | NotGiven = NOT_GIVEN,
        data_set_remarks: str | NotGiven = NOT_GIVEN,
        deleting_org: str | NotGiven = NOT_GIVEN,
        deriving_org: str | NotGiven = NOT_GIVEN,
        directivity_code: int | NotGiven = NOT_GIVEN,
        elevation: float | NotGiven = NOT_GIVEN,
        elevation_acc: float | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        facc: str | NotGiven = NOT_GIVEN,
        feature_code: str | NotGiven = NOT_GIVEN,
        feature_description: str | NotGiven = NOT_GIVEN,
        feature_name: str | NotGiven = NOT_GIVEN,
        feature_type: str | NotGiven = NOT_GIVEN,
        height_agl: float | NotGiven = NOT_GIVEN,
        height_agl_acc: float | NotGiven = NOT_GIVEN,
        height_msl: float | NotGiven = NOT_GIVEN,
        height_msl_acc: float | NotGiven = NOT_GIVEN,
        horiz_acc: float | NotGiven = NOT_GIVEN,
        horiz_datum_code: str | NotGiven = NOT_GIVEN,
        init_record_date: Union[str, date] | NotGiven = NOT_GIVEN,
        keys: List[str] | NotGiven = NOT_GIVEN,
        lighting_code: str | NotGiven = NOT_GIVEN,
        line_ne_lat: float | NotGiven = NOT_GIVEN,
        line_ne_lon: float | NotGiven = NOT_GIVEN,
        lines_filename: str | NotGiven = NOT_GIVEN,
        line_sw_lat: float | NotGiven = NOT_GIVEN,
        line_sw_lon: float | NotGiven = NOT_GIVEN,
        min_height_agl: float | NotGiven = NOT_GIVEN,
        mult_obs: str | NotGiven = NOT_GIVEN,
        next_cycle_date: Union[str, date] | NotGiven = NOT_GIVEN,
        num_lines: int | NotGiven = NOT_GIVEN,
        num_obs: int | NotGiven = NOT_GIVEN,
        num_points: int | NotGiven = NOT_GIVEN,
        obstacle_remarks: str | NotGiven = NOT_GIVEN,
        orig_id: str | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        owner_country_code: str | NotGiven = NOT_GIVEN,
        point_lat: float | NotGiven = NOT_GIVEN,
        point_lon: float | NotGiven = NOT_GIVEN,
        points_filename: str | NotGiven = NOT_GIVEN,
        process_code: str | NotGiven = NOT_GIVEN,
        producer: str | NotGiven = NOT_GIVEN,
        province_code: str | NotGiven = NOT_GIVEN,
        quality: str | NotGiven = NOT_GIVEN,
        rev_date: Union[str, date] | NotGiven = NOT_GIVEN,
        seg_end_point: int | NotGiven = NOT_GIVEN,
        seg_num: int | NotGiven = NOT_GIVEN,
        seg_start_point: int | NotGiven = NOT_GIVEN,
        source_date: Union[str, date] | NotGiven = NOT_GIVEN,
        surface_mat_code: str | NotGiven = NOT_GIVEN,
        transaction_code: str | NotGiven = NOT_GIVEN,
        validation_code: int | NotGiven = NOT_GIVEN,
        values: List[str] | NotGiven = NOT_GIVEN,
        vectors_filename: str | NotGiven = NOT_GIVEN,
        wac: str | NotGiven = NOT_GIVEN,
        wac_innr: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Service operation to update a single navigational obstruction record.

        A specific
        role is required to perform this service operation. Please contact the UDL team
        for assistance.

        Args:
          classification_marking: Classification marking of the data in IC/CAPCO Portion-marked format.

          cycle_date: Start date of this obstruction data set's currency, in ISO 8601 date-only
              format.

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

          obstacle_id: The ID of this obstacle.

          obstacle_type: Type of obstacle (e.g. P for point, V for vector, L for line).

          source: Source of the data.

          body_id: Unique identifier of the record, auto-generated by the system.

          act_del_code: Indicates if this obstacle record is Active (A) or Deleted (D).

          airac_cycle: The Aeronautical Information Regulation and Control (AIRAC) cycle of this
              obstruction data set. The format is YYNN where YY is the last two digits of the
              year and NN is the cycle number.

          base_airac_cycle: The baseline Aeronautical Information Regulation and Control (AIRAC) cycle for
              change sets only. The format is YYNN where YY is the last two digits of the year
              and NN is the cycle number.

          baseline_cutoff_date: Earliest record date possible in this obstruction data set (not the earliest
              data item), in ISO 8601 date-only format (e.g. YYYY-MM-DD). If null, this data
              set is assumed to be a full data pull of holdings until the cutoffDate. If this
              field is populated, this data set only contains updates since the last baseline
              data set.

          bound_ne_lat: WGS-84 latitude of the northeastern boundary for obstructions contained in this
              data set, in degrees. -90 to 90 degrees (negative values south of equator).

          bound_ne_lon: WGS-84 longitude of the northeastern boundary for obstructions contained in this
              data set, in degrees. -180 to 180 degrees (negative values west of Prime
              Meridian).

          bound_sw_lat: WGS-84 latitude of the southwestern boundary for obstructions contained in this
              data set, in degrees. -90 to 90 degrees (negative values south of equator).

          bound_sw_lon: WGS-84 longitude of the southwestern boundary for obstructions contained in this
              data set, in degrees. -180 to 180 degrees (negative values west of Prime
              Meridian).

          country_code: The DoD Standard Country Code designator for the country issuing the diplomatic
              clearance. This field will be set to "OTHR" if the source value does not match a
              UDL Country code value (ISO-3166-ALPHA-2).

          cutoff_date: Latest record date possible in this obstruction data set (not the most recent
              data item), in ISO 8601 date-only format (e.g. YYYY-MM-DD).

          data_set_remarks: Remarks concerning this obstruction's data set.

          deleting_org: The organization that deleted this obstacle record.

          deriving_org: The organization that entered obstacle data other than the producer.

          directivity_code: The side or sides of this obstruction feature which produces the greatest
              reflectivity potential.

          elevation: The elevation at the point obstacle's location in feet.

          elevation_acc: The difference between the assigned elevation of this point and its true
              elevation, in feet.

          external_id: Optional obstacle ID from external systems. This field has no meaning within UDL
              and is provided as a convenience for systems that require tracking of an
              internal system generated ID.

          facc: FACC (Feature and Attribute Coding Catalog) is a five-character code for
              encoding real-world entities and objects. The first letter of the code is an
              alphabetic value from "A" to "Z" which will map to a feature category. The
              second character will map to a subcategory. Characters three to five are numeric
              and range from 000 to 999. This value will provide a unit feature type
              identification within the categories.

          feature_code: Identifying code for the type of this point obstacle.

          feature_description: Description of this obstacle, corresponding to the FACC (Feature and Attribute
              Coding Catalog) value.

          feature_name: Type name of point obstacle.

          feature_type: Identifying code for the type of this point obstacle.

          height_agl: The height Above Ground Level (AGL) of the point obstacle in feet.

          height_agl_acc: The accuracy of the height Above Ground Level (AGL) value for this point
              obstacle, in feet.

          height_msl: The height Above Mean Sea Level (AMSL) of the point obstacle in feet.

          height_msl_acc: The accuracy of the height Above Mean Sea Level (AMSL) value for this point
              obstacle in feet.

          horiz_acc: The difference between the recorded horizontal coordinates of this point
              obstacle and its true position, in feet.

          horiz_datum_code: Code representing the mathematical model of Earth used to calculate coordinates
              for this obstacle (e.g. WGS-84, U for undetermined, etc.). US Forces use the
              World Geodetic System 1984 (WGS-84), but also use maps by allied countries with
              local datums.

          init_record_date: Date this obstacle was initially added to the data set, in ISO 8601 date-only
              format (ex. YYYY-MM-DD).

          keys: This field provides an array of keys that can be added to any obstruction
              feature to provide information that is not already supported. The entries in
              this array must correspond to the position index in the values array. This array
              must be the same length as values.

          lighting_code: Code specifying if this obstacle is lit (e.g. Y = Yes, N = No, U = Unknown).

          line_ne_lat: WGS-84 latitude of the northeastern point of the line, in degrees. -90 to 90
              degrees (negative values south of equator).

          line_ne_lon: WGS-84 longitude of the northeastern point of the line, in degrees. -180 to 180
              degrees (negative values west of Prime Meridian).

          lines_filename: The name of the line file associated with this obstruction data set.

          line_sw_lat: WGS-84 latitude of the southwestern point of the line, in degrees. -90 to 90
              degrees (negative values south of equator).

          line_sw_lon: WGS-84 longitude of the southwestern point of the line, in degrees. -180 to 180
              degrees (negative values west of Prime Meridian).

          min_height_agl: The minimum height Above Ground Level (AGL) of the shortest obstruction
              contained in this data set, in feet.

          mult_obs: Indicates if the feature has multiple obstructions (e.g. S = Single, M =
              Multiple, U = Undetermined).

          next_cycle_date: The date after which this obstruction data set’s currency is stale and should be
              refreshed, in ISO 8601 date-only format (e.g. YYYY-MM-DD).

          num_lines: The number of line features associated with this obstruction data set.

          num_obs: Indicates the number of obstructions associated with a feature.

          num_points: The number of point features associated with this obstruction data set.

          obstacle_remarks: Remarks regarding this obstacle.

          orig_id: The original ID for this obstacle.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          owner_country_code: The DoD Standard Country Code designator for the country or political entity
              that owns the data set associated with this obstruction. This field will be set
              to "OTHR" if the source value does not match a UDL Country code value
              (ISO-3166-ALPHA-2).

          point_lat: WGS-84 latitude of this point obstacle, in degrees. -90 to 90 degrees (negative
              values south of equator).

          point_lon: WGS-84 longitude of this point obstacle, in degrees. -180 to 180 degrees
              (negative values west of Prime Meridian).

          points_filename: The name of the point file associated with this obstruction data set.

          process_code: Code denoting the action, review, or process that updated this obstacle.

          producer: Name of the agency that produced this obstruction data set.

          province_code: The Federal Information Processing Standards (FIPS) state/province numeric code
              of this obstacle's location.

          quality: When horizontal and/or vertical accuracy requirements cannot be met because of
              inadequate source material, this code indicates the quality of the data.

          rev_date: Date this obstacle data was revised, in ISO 8601 date-only format (ex.
              YYYY-MM-DD).

          seg_end_point: ID of the end point of a line segment.

          seg_num: Identifies the sequence number of a line segment.

          seg_start_point: ID of the starting point of a line segment.

          source_date: Source date of this obstacle data, in ISO 8601 date-only format (ex.
              YYYY-MM-DD).

          surface_mat_code: The surface material composition code of this point obstacle.

          transaction_code: The transaction type/code for this obstacle (e.g. "D", "N", "R", "S", "V", "X").

          validation_code: Method used to confirm the existence of this obstacle.

          values: This field provides an array of values that can be added to any obstruction
              feature to provide information that is not already supported. The entries in
              this array must correspond to the position index in the keys array. This array
              must be the same length as keys.

          vectors_filename: The name of the vector file associated with this obstruction data set.

          wac: The World Aeronautical Chart (WAC) identifier for the area in which this
              obstacle is located.

          wac_innr: This obstacle's World Area Code installation number (WAC-INNR).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            f"/udl/navigationalobstruction/{path_id}",
            body=await async_maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "cycle_date": cycle_date,
                    "data_mode": data_mode,
                    "obstacle_id": obstacle_id,
                    "obstacle_type": obstacle_type,
                    "source": source,
                    "body_id": body_id,
                    "act_del_code": act_del_code,
                    "airac_cycle": airac_cycle,
                    "base_airac_cycle": base_airac_cycle,
                    "baseline_cutoff_date": baseline_cutoff_date,
                    "bound_ne_lat": bound_ne_lat,
                    "bound_ne_lon": bound_ne_lon,
                    "bound_sw_lat": bound_sw_lat,
                    "bound_sw_lon": bound_sw_lon,
                    "country_code": country_code,
                    "cutoff_date": cutoff_date,
                    "data_set_remarks": data_set_remarks,
                    "deleting_org": deleting_org,
                    "deriving_org": deriving_org,
                    "directivity_code": directivity_code,
                    "elevation": elevation,
                    "elevation_acc": elevation_acc,
                    "external_id": external_id,
                    "facc": facc,
                    "feature_code": feature_code,
                    "feature_description": feature_description,
                    "feature_name": feature_name,
                    "feature_type": feature_type,
                    "height_agl": height_agl,
                    "height_agl_acc": height_agl_acc,
                    "height_msl": height_msl,
                    "height_msl_acc": height_msl_acc,
                    "horiz_acc": horiz_acc,
                    "horiz_datum_code": horiz_datum_code,
                    "init_record_date": init_record_date,
                    "keys": keys,
                    "lighting_code": lighting_code,
                    "line_ne_lat": line_ne_lat,
                    "line_ne_lon": line_ne_lon,
                    "lines_filename": lines_filename,
                    "line_sw_lat": line_sw_lat,
                    "line_sw_lon": line_sw_lon,
                    "min_height_agl": min_height_agl,
                    "mult_obs": mult_obs,
                    "next_cycle_date": next_cycle_date,
                    "num_lines": num_lines,
                    "num_obs": num_obs,
                    "num_points": num_points,
                    "obstacle_remarks": obstacle_remarks,
                    "orig_id": orig_id,
                    "origin": origin,
                    "owner_country_code": owner_country_code,
                    "point_lat": point_lat,
                    "point_lon": point_lon,
                    "points_filename": points_filename,
                    "process_code": process_code,
                    "producer": producer,
                    "province_code": province_code,
                    "quality": quality,
                    "rev_date": rev_date,
                    "seg_end_point": seg_end_point,
                    "seg_num": seg_num,
                    "seg_start_point": seg_start_point,
                    "source_date": source_date,
                    "surface_mat_code": surface_mat_code,
                    "transaction_code": transaction_code,
                    "validation_code": validation_code,
                    "values": values,
                    "vectors_filename": vectors_filename,
                    "wac": wac,
                    "wac_innr": wac_innr,
                },
                navigational_obstruction_update_params.NavigationalObstructionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        *,
        cycle_date: Union[str, date] | NotGiven = NOT_GIVEN,
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        obstacle_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[NavigationalObstructionListResponse, AsyncOffsetPage[NavigationalObstructionListResponse]]:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          cycle_date: (One or more of fields 'cycleDate, obstacleId' are required.) Start date of this
              obstruction data set's currency, in ISO 8601 date-only format. (YYYY-MM-DD)

          obstacle_id: (One or more of fields 'cycleDate, obstacleId' are required.) The ID of this
              obstacle.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/navigationalobstruction",
            page=AsyncOffsetPage[NavigationalObstructionListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cycle_date": cycle_date,
                        "first_result": first_result,
                        "max_results": max_results,
                        "obstacle_id": obstacle_id,
                    },
                    navigational_obstruction_list_params.NavigationalObstructionListParams,
                ),
            ),
            model=NavigationalObstructionListResponse,
        )

    async def count(
        self,
        *,
        cycle_date: Union[str, date] | NotGiven = NOT_GIVEN,
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        obstacle_id: str | NotGiven = NOT_GIVEN,
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
          cycle_date: (One or more of fields 'cycleDate, obstacleId' are required.) Start date of this
              obstruction data set's currency, in ISO 8601 date-only format. (YYYY-MM-DD)

          obstacle_id: (One or more of fields 'cycleDate, obstacleId' are required.) The ID of this
              obstacle.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return await self._get(
            "/udl/navigationalobstruction/count",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cycle_date": cycle_date,
                        "first_result": first_result,
                        "max_results": max_results,
                        "obstacle_id": obstacle_id,
                    },
                    navigational_obstruction_count_params.NavigationalObstructionCountParams,
                ),
            ),
            cast_to=str,
        )

    async def create_bulk(
        self,
        *,
        body: Iterable[navigational_obstruction_create_bulk_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation intended for initial integration only, to take a list of
        navigational obstruction records as a POST body and ingest into the database.
        This operation is not intended to be used for automated feeds into UDL. Data
        providers should contact the UDL team for specific role assignments and for
        instructions on setting up a permanent feed through an alternate mechanism.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/udl/navigationalobstruction/createBulk",
            body=await async_maybe_transform(body, Iterable[navigational_obstruction_create_bulk_params.Body]),
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
    ) -> NavigationalObstructionGetResponse:
        """
        Service operation to get a single navigational obstruction record by its unique
        ID passed as a path parameter.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/udl/navigationalobstruction/{id}",
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
                    navigational_obstruction_get_params.NavigationalObstructionGetParams,
                ),
            ),
            cast_to=NavigationalObstructionGetResponse,
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
    ) -> NavigationalObstructionQueryhelpResponse:
        """
        Service operation to provide detailed information on available dynamic query
        parameters for a particular data type.
        """
        return await self._get(
            "/udl/navigationalobstruction/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NavigationalObstructionQueryhelpResponse,
        )

    async def tuple(
        self,
        *,
        columns: str,
        cycle_date: Union[str, date] | NotGiven = NOT_GIVEN,
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        obstacle_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NavigationalObstructionTupleResponse:
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

          cycle_date: (One or more of fields 'cycleDate, obstacleId' are required.) Start date of this
              obstruction data set's currency, in ISO 8601 date-only format. (YYYY-MM-DD)

          obstacle_id: (One or more of fields 'cycleDate, obstacleId' are required.) The ID of this
              obstacle.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/udl/navigationalobstruction/tuple",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "columns": columns,
                        "cycle_date": cycle_date,
                        "first_result": first_result,
                        "max_results": max_results,
                        "obstacle_id": obstacle_id,
                    },
                    navigational_obstruction_tuple_params.NavigationalObstructionTupleParams,
                ),
            ),
            cast_to=NavigationalObstructionTupleResponse,
        )


class NavigationalObstructionResourceWithRawResponse:
    def __init__(self, navigational_obstruction: NavigationalObstructionResource) -> None:
        self._navigational_obstruction = navigational_obstruction

        self.create = to_raw_response_wrapper(
            navigational_obstruction.create,
        )
        self.update = to_raw_response_wrapper(
            navigational_obstruction.update,
        )
        self.list = to_raw_response_wrapper(
            navigational_obstruction.list,
        )
        self.count = to_raw_response_wrapper(
            navigational_obstruction.count,
        )
        self.create_bulk = to_raw_response_wrapper(
            navigational_obstruction.create_bulk,
        )
        self.get = to_raw_response_wrapper(
            navigational_obstruction.get,
        )
        self.queryhelp = to_raw_response_wrapper(
            navigational_obstruction.queryhelp,
        )
        self.tuple = to_raw_response_wrapper(
            navigational_obstruction.tuple,
        )


class AsyncNavigationalObstructionResourceWithRawResponse:
    def __init__(self, navigational_obstruction: AsyncNavigationalObstructionResource) -> None:
        self._navigational_obstruction = navigational_obstruction

        self.create = async_to_raw_response_wrapper(
            navigational_obstruction.create,
        )
        self.update = async_to_raw_response_wrapper(
            navigational_obstruction.update,
        )
        self.list = async_to_raw_response_wrapper(
            navigational_obstruction.list,
        )
        self.count = async_to_raw_response_wrapper(
            navigational_obstruction.count,
        )
        self.create_bulk = async_to_raw_response_wrapper(
            navigational_obstruction.create_bulk,
        )
        self.get = async_to_raw_response_wrapper(
            navigational_obstruction.get,
        )
        self.queryhelp = async_to_raw_response_wrapper(
            navigational_obstruction.queryhelp,
        )
        self.tuple = async_to_raw_response_wrapper(
            navigational_obstruction.tuple,
        )


class NavigationalObstructionResourceWithStreamingResponse:
    def __init__(self, navigational_obstruction: NavigationalObstructionResource) -> None:
        self._navigational_obstruction = navigational_obstruction

        self.create = to_streamed_response_wrapper(
            navigational_obstruction.create,
        )
        self.update = to_streamed_response_wrapper(
            navigational_obstruction.update,
        )
        self.list = to_streamed_response_wrapper(
            navigational_obstruction.list,
        )
        self.count = to_streamed_response_wrapper(
            navigational_obstruction.count,
        )
        self.create_bulk = to_streamed_response_wrapper(
            navigational_obstruction.create_bulk,
        )
        self.get = to_streamed_response_wrapper(
            navigational_obstruction.get,
        )
        self.queryhelp = to_streamed_response_wrapper(
            navigational_obstruction.queryhelp,
        )
        self.tuple = to_streamed_response_wrapper(
            navigational_obstruction.tuple,
        )


class AsyncNavigationalObstructionResourceWithStreamingResponse:
    def __init__(self, navigational_obstruction: AsyncNavigationalObstructionResource) -> None:
        self._navigational_obstruction = navigational_obstruction

        self.create = async_to_streamed_response_wrapper(
            navigational_obstruction.create,
        )
        self.update = async_to_streamed_response_wrapper(
            navigational_obstruction.update,
        )
        self.list = async_to_streamed_response_wrapper(
            navigational_obstruction.list,
        )
        self.count = async_to_streamed_response_wrapper(
            navigational_obstruction.count,
        )
        self.create_bulk = async_to_streamed_response_wrapper(
            navigational_obstruction.create_bulk,
        )
        self.get = async_to_streamed_response_wrapper(
            navigational_obstruction.get,
        )
        self.queryhelp = async_to_streamed_response_wrapper(
            navigational_obstruction.queryhelp,
        )
        self.tuple = async_to_streamed_response_wrapper(
            navigational_obstruction.tuple,
        )
