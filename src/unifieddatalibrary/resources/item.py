# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from datetime import date, datetime
from typing_extensions import Literal

import httpx

from ..types import (
    item_get_params,
    item_list_params,
    item_count_params,
    item_tuple_params,
    item_create_params,
    item_update_params,
    item_unvalidated_publish_params,
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
from ..types.item_get_response import ItemGetResponse
from ..types.item_list_response import ItemListResponse
from ..types.item_tuple_response import ItemTupleResponse
from ..types.item_queryhelp_response import ItemQueryhelpResponse

__all__ = ["ItemResource", "AsyncItemResource"]


class ItemResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ItemResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return ItemResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ItemResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return ItemResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        scan_code: str,
        source: str,
        type: str,
        id: str | NotGiven = NOT_GIVEN,
        acc_sys_keys: List[str] | NotGiven = NOT_GIVEN,
        acc_sys_notes: str | NotGiven = NOT_GIVEN,
        acc_system: str | NotGiven = NOT_GIVEN,
        acc_sys_values: List[str] | NotGiven = NOT_GIVEN,
        airdrop: bool | NotGiven = NOT_GIVEN,
        alt_data_format: str | NotGiven = NOT_GIVEN,
        cargo_type: str | NotGiven = NOT_GIVEN,
        centerline_offset: float | NotGiven = NOT_GIVEN,
        cg: float | NotGiven = NOT_GIVEN,
        commodity_code: str | NotGiven = NOT_GIVEN,
        commodity_sys: str | NotGiven = NOT_GIVEN,
        container: bool | NotGiven = NOT_GIVEN,
        departure: str | NotGiven = NOT_GIVEN,
        destination: str | NotGiven = NOT_GIVEN,
        dv_code: str | NotGiven = NOT_GIVEN,
        fs: float | NotGiven = NOT_GIVEN,
        haz_codes: Iterable[float] | NotGiven = NOT_GIVEN,
        height: float | NotGiven = NOT_GIVEN,
        id_air_load_plan: str | NotGiven = NOT_GIVEN,
        item_contains: List[str] | NotGiven = NOT_GIVEN,
        keys: List[str] | NotGiven = NOT_GIVEN,
        last_arr_date: Union[str, date] | NotGiven = NOT_GIVEN,
        length: float | NotGiven = NOT_GIVEN,
        moment: float | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        net_exp_wt: float | NotGiven = NOT_GIVEN,
        notes: str | NotGiven = NOT_GIVEN,
        num_pallet_pos: int | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        product_code: str | NotGiven = NOT_GIVEN,
        product_sys: str | NotGiven = NOT_GIVEN,
        receiving_branch: str | NotGiven = NOT_GIVEN,
        receiving_unit: str | NotGiven = NOT_GIVEN,
        sc_gen_tool: str | NotGiven = NOT_GIVEN,
        tcn: str | NotGiven = NOT_GIVEN,
        uln: str | NotGiven = NOT_GIVEN,
        values: List[str] | NotGiven = NOT_GIVEN,
        volume: float | NotGiven = NOT_GIVEN,
        weight: float | NotGiven = NOT_GIVEN,
        weight_ts: Union[str, datetime] | NotGiven = NOT_GIVEN,
        width: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single item record as a POST body and ingest into
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

          scan_code: The tracking identifier of an item or person. May be similar in representation
              of a barcode or UPC. If no scanCode or tracking number equivalent is available,
              'NONE' should be used.

          source: Source of the data.

          type: The item type of this record (e.g. EQUIPMENT, CARGO, PASSENGER).

          id: Unique identifier of the record, auto-generated by the system if not provided on
              create operations.

          acc_sys_keys: Array of keys that may be associated to the accepting system data. The entries
              in this array must correspond to the position index in accSysValues array. This
              array must be the same length as accSysValues.

          acc_sys_notes: Additional data required to find this item in the accepting system.

          acc_system: Name of the system that accepted this item from a customer. Where a user or
              application could go look for additional information.

          acc_sys_values: Array of values for the keys that may be associated to the accepting system
              data. The entries in this array must correspond to the position index in
              accSysKeys array. This array must be the same length as accSysKeys.

          airdrop: Flag indicating this item is planned to be airdropped. Applicable for cargo and
              passenger item types only.

          alt_data_format: Name of the additional data format so downstream consuming applications can know
              how to parse it. Typically includes the source system name and the format name.

          cargo_type: The type of cargo (e.g. PALLET, ROLLING STOCK, LOOSE, OTHER). Applicable for
              cargo item types only.

          centerline_offset: How far left or right of centerline is the item in meters. Applicable for cargo
              and passenger item types only.

          cg: Center of gravity position of the item, measured from the item's front datum, in
              centimeters.

          commodity_code: The classification code of the commodity or group of commodities.

          commodity_sys: The classification system denoting the commodity code, commodityCode (e.g. AIR,
              WATER, NMFC, UFC, STCC, DODUNQ, etc.).

          container: Flag indicating this item acts as a container and contains additional items.

          departure: The departure code or location where this item has left or is leaving.

          destination: The destination of the item, typically an ICAO or port code. Applicable for
              cargo and passenger item types only.

          dv_code: United States Distinguished Visitor Code, only applicable to people.

          fs: The fuselage station of the item measured from the reference datum, in
              centimeters. Applicable for cargo and passenger item types only.

          haz_codes: Array of UN hazard classes or division codes that apply to this item.

          height: Height of the cargo in meters. Applicable for cargo item types only.

          id_air_load_plan: The UDL ID of the air load plan this item is associated with.

          item_contains: Array of tracking identifiers that are contained within this item.

          keys: Array of keys that may be associated to this item. The entries in this array
              must correspond to the position index in the values array. This array must be
              the same length as values..

          last_arr_date: The latest acceptable arrival date of the item at the destination, in ISO 8601
              date-only format (e.g. YYYY-MM-DD).

          length: Length of the cargo in meters. Applicable for cargo item types only.

          moment: Moment of the item in Newton-meters. Applicable for equipment and cargo item
              types only.

          name: Name of the item. Applicable for equipment and cargo item types only.

          net_exp_wt: Net explosive weight of the item, in kilograms.

          notes: Optional notes or comments about this item.

          num_pallet_pos: Number of pallet positions or equivalent on the aircraft, ship, or conveyance
              equipment that this item occupies.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          product_code: The code denoting the type of material item.

          product_sys: The assigning system that denotes the type of material item, productCode (e.g.
              NSN-national stock number, NDC-national drug code, MPN-manufacturer part number,
              etc.).

          receiving_branch: The military branch receiving this item.

          receiving_unit: The name of the unit receiving this item.

          sc_gen_tool: The algorithm name or standard that generated the scanCode (e.g. UPC-A, EAN-13,
              GTIN, SSCC, bID, JAN, etc.).

          tcn: Transportation Control Number of the cargo. Applicable for cargo item types
              only.

          uln: The unit line number of this item.

          values: Array of values for the keys that may be associated to this tracked item. The
              entries in this array must correspond to the position index in the keys array.
              This array must be the same length as keys.

          volume: The volume of the item, in cubic meters. Applicable for cargo item types only.

          weight: Weight of the item in kilograms (if item is a passenger, include on-person
              bags).

          weight_ts: Timestamp when the weight was taken, in ISO 8601 UTC format with millisecond
              precision.

          width: Width of the cargo in meters. Applicable for cargo item types only.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/udl/item",
            body=maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "scan_code": scan_code,
                    "source": source,
                    "type": type,
                    "id": id,
                    "acc_sys_keys": acc_sys_keys,
                    "acc_sys_notes": acc_sys_notes,
                    "acc_system": acc_system,
                    "acc_sys_values": acc_sys_values,
                    "airdrop": airdrop,
                    "alt_data_format": alt_data_format,
                    "cargo_type": cargo_type,
                    "centerline_offset": centerline_offset,
                    "cg": cg,
                    "commodity_code": commodity_code,
                    "commodity_sys": commodity_sys,
                    "container": container,
                    "departure": departure,
                    "destination": destination,
                    "dv_code": dv_code,
                    "fs": fs,
                    "haz_codes": haz_codes,
                    "height": height,
                    "id_air_load_plan": id_air_load_plan,
                    "item_contains": item_contains,
                    "keys": keys,
                    "last_arr_date": last_arr_date,
                    "length": length,
                    "moment": moment,
                    "name": name,
                    "net_exp_wt": net_exp_wt,
                    "notes": notes,
                    "num_pallet_pos": num_pallet_pos,
                    "origin": origin,
                    "product_code": product_code,
                    "product_sys": product_sys,
                    "receiving_branch": receiving_branch,
                    "receiving_unit": receiving_unit,
                    "sc_gen_tool": sc_gen_tool,
                    "tcn": tcn,
                    "uln": uln,
                    "values": values,
                    "volume": volume,
                    "weight": weight,
                    "weight_ts": weight_ts,
                    "width": width,
                },
                item_create_params.ItemCreateParams,
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
        scan_code: str,
        source: str,
        type: str,
        body_id: str | NotGiven = NOT_GIVEN,
        acc_sys_keys: List[str] | NotGiven = NOT_GIVEN,
        acc_sys_notes: str | NotGiven = NOT_GIVEN,
        acc_system: str | NotGiven = NOT_GIVEN,
        acc_sys_values: List[str] | NotGiven = NOT_GIVEN,
        airdrop: bool | NotGiven = NOT_GIVEN,
        alt_data_format: str | NotGiven = NOT_GIVEN,
        cargo_type: str | NotGiven = NOT_GIVEN,
        centerline_offset: float | NotGiven = NOT_GIVEN,
        cg: float | NotGiven = NOT_GIVEN,
        commodity_code: str | NotGiven = NOT_GIVEN,
        commodity_sys: str | NotGiven = NOT_GIVEN,
        container: bool | NotGiven = NOT_GIVEN,
        departure: str | NotGiven = NOT_GIVEN,
        destination: str | NotGiven = NOT_GIVEN,
        dv_code: str | NotGiven = NOT_GIVEN,
        fs: float | NotGiven = NOT_GIVEN,
        haz_codes: Iterable[float] | NotGiven = NOT_GIVEN,
        height: float | NotGiven = NOT_GIVEN,
        id_air_load_plan: str | NotGiven = NOT_GIVEN,
        item_contains: List[str] | NotGiven = NOT_GIVEN,
        keys: List[str] | NotGiven = NOT_GIVEN,
        last_arr_date: Union[str, date] | NotGiven = NOT_GIVEN,
        length: float | NotGiven = NOT_GIVEN,
        moment: float | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        net_exp_wt: float | NotGiven = NOT_GIVEN,
        notes: str | NotGiven = NOT_GIVEN,
        num_pallet_pos: int | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        product_code: str | NotGiven = NOT_GIVEN,
        product_sys: str | NotGiven = NOT_GIVEN,
        receiving_branch: str | NotGiven = NOT_GIVEN,
        receiving_unit: str | NotGiven = NOT_GIVEN,
        sc_gen_tool: str | NotGiven = NOT_GIVEN,
        tcn: str | NotGiven = NOT_GIVEN,
        uln: str | NotGiven = NOT_GIVEN,
        values: List[str] | NotGiven = NOT_GIVEN,
        volume: float | NotGiven = NOT_GIVEN,
        weight: float | NotGiven = NOT_GIVEN,
        weight_ts: Union[str, datetime] | NotGiven = NOT_GIVEN,
        width: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Service operation to update a single Item.

        An Item can be cargo, equipment, or a
        passenger. A specific role is required to perform this service operation. Please
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

          scan_code: The tracking identifier of an item or person. May be similar in representation
              of a barcode or UPC. If no scanCode or tracking number equivalent is available,
              'NONE' should be used.

          source: Source of the data.

          type: The item type of this record (e.g. EQUIPMENT, CARGO, PASSENGER).

          body_id: Unique identifier of the record, auto-generated by the system if not provided on
              create operations.

          acc_sys_keys: Array of keys that may be associated to the accepting system data. The entries
              in this array must correspond to the position index in accSysValues array. This
              array must be the same length as accSysValues.

          acc_sys_notes: Additional data required to find this item in the accepting system.

          acc_system: Name of the system that accepted this item from a customer. Where a user or
              application could go look for additional information.

          acc_sys_values: Array of values for the keys that may be associated to the accepting system
              data. The entries in this array must correspond to the position index in
              accSysKeys array. This array must be the same length as accSysKeys.

          airdrop: Flag indicating this item is planned to be airdropped. Applicable for cargo and
              passenger item types only.

          alt_data_format: Name of the additional data format so downstream consuming applications can know
              how to parse it. Typically includes the source system name and the format name.

          cargo_type: The type of cargo (e.g. PALLET, ROLLING STOCK, LOOSE, OTHER). Applicable for
              cargo item types only.

          centerline_offset: How far left or right of centerline is the item in meters. Applicable for cargo
              and passenger item types only.

          cg: Center of gravity position of the item, measured from the item's front datum, in
              centimeters.

          commodity_code: The classification code of the commodity or group of commodities.

          commodity_sys: The classification system denoting the commodity code, commodityCode (e.g. AIR,
              WATER, NMFC, UFC, STCC, DODUNQ, etc.).

          container: Flag indicating this item acts as a container and contains additional items.

          departure: The departure code or location where this item has left or is leaving.

          destination: The destination of the item, typically an ICAO or port code. Applicable for
              cargo and passenger item types only.

          dv_code: United States Distinguished Visitor Code, only applicable to people.

          fs: The fuselage station of the item measured from the reference datum, in
              centimeters. Applicable for cargo and passenger item types only.

          haz_codes: Array of UN hazard classes or division codes that apply to this item.

          height: Height of the cargo in meters. Applicable for cargo item types only.

          id_air_load_plan: The UDL ID of the air load plan this item is associated with.

          item_contains: Array of tracking identifiers that are contained within this item.

          keys: Array of keys that may be associated to this item. The entries in this array
              must correspond to the position index in the values array. This array must be
              the same length as values..

          last_arr_date: The latest acceptable arrival date of the item at the destination, in ISO 8601
              date-only format (e.g. YYYY-MM-DD).

          length: Length of the cargo in meters. Applicable for cargo item types only.

          moment: Moment of the item in Newton-meters. Applicable for equipment and cargo item
              types only.

          name: Name of the item. Applicable for equipment and cargo item types only.

          net_exp_wt: Net explosive weight of the item, in kilograms.

          notes: Optional notes or comments about this item.

          num_pallet_pos: Number of pallet positions or equivalent on the aircraft, ship, or conveyance
              equipment that this item occupies.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          product_code: The code denoting the type of material item.

          product_sys: The assigning system that denotes the type of material item, productCode (e.g.
              NSN-national stock number, NDC-national drug code, MPN-manufacturer part number,
              etc.).

          receiving_branch: The military branch receiving this item.

          receiving_unit: The name of the unit receiving this item.

          sc_gen_tool: The algorithm name or standard that generated the scanCode (e.g. UPC-A, EAN-13,
              GTIN, SSCC, bID, JAN, etc.).

          tcn: Transportation Control Number of the cargo. Applicable for cargo item types
              only.

          uln: The unit line number of this item.

          values: Array of values for the keys that may be associated to this tracked item. The
              entries in this array must correspond to the position index in the keys array.
              This array must be the same length as keys.

          volume: The volume of the item, in cubic meters. Applicable for cargo item types only.

          weight: Weight of the item in kilograms (if item is a passenger, include on-person
              bags).

          weight_ts: Timestamp when the weight was taken, in ISO 8601 UTC format with millisecond
              precision.

          width: Width of the cargo in meters. Applicable for cargo item types only.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            f"/udl/item/{path_id}",
            body=maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "scan_code": scan_code,
                    "source": source,
                    "type": type,
                    "body_id": body_id,
                    "acc_sys_keys": acc_sys_keys,
                    "acc_sys_notes": acc_sys_notes,
                    "acc_system": acc_system,
                    "acc_sys_values": acc_sys_values,
                    "airdrop": airdrop,
                    "alt_data_format": alt_data_format,
                    "cargo_type": cargo_type,
                    "centerline_offset": centerline_offset,
                    "cg": cg,
                    "commodity_code": commodity_code,
                    "commodity_sys": commodity_sys,
                    "container": container,
                    "departure": departure,
                    "destination": destination,
                    "dv_code": dv_code,
                    "fs": fs,
                    "haz_codes": haz_codes,
                    "height": height,
                    "id_air_load_plan": id_air_load_plan,
                    "item_contains": item_contains,
                    "keys": keys,
                    "last_arr_date": last_arr_date,
                    "length": length,
                    "moment": moment,
                    "name": name,
                    "net_exp_wt": net_exp_wt,
                    "notes": notes,
                    "num_pallet_pos": num_pallet_pos,
                    "origin": origin,
                    "product_code": product_code,
                    "product_sys": product_sys,
                    "receiving_branch": receiving_branch,
                    "receiving_unit": receiving_unit,
                    "sc_gen_tool": sc_gen_tool,
                    "tcn": tcn,
                    "uln": uln,
                    "values": values,
                    "volume": volume,
                    "weight": weight,
                    "weight_ts": weight_ts,
                    "width": width,
                },
                item_update_params.ItemUpdateParams,
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
    ) -> SyncOffsetPage[ItemListResponse]:
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
            "/udl/item",
            page=SyncOffsetPage[ItemListResponse],
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
                    item_list_params.ItemListParams,
                ),
            ),
            model=ItemListResponse,
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
        Service operation to delete a item record specified by the passed ID path
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
            f"/udl/item/{id}",
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
            "/udl/item/count",
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
                    item_count_params.ItemCountParams,
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
    ) -> ItemGetResponse:
        """
        Service operation to get a single item record by its unique ID passed as a path
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
            f"/udl/item/{id}",
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
                    item_get_params.ItemGetParams,
                ),
            ),
            cast_to=ItemGetResponse,
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
    ) -> ItemQueryhelpResponse:
        """
        Service operation to provide detailed information on available dynamic query
        parameters for a particular data type.
        """
        return self._get(
            "/udl/item/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ItemQueryhelpResponse,
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
    ) -> ItemTupleResponse:
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
            "/udl/item/tuple",
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
                    item_tuple_params.ItemTupleParams,
                ),
            ),
            cast_to=ItemTupleResponse,
        )

    def unvalidated_publish(
        self,
        *,
        body: Iterable[item_unvalidated_publish_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take multiple item records as a POST body and ingest into
        the database. This operation is intended to be used for automated feeds into
        UDL. A specific role is required to perform this service operation. Please
        contact the UDL team for assistance.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/filedrop/udl-item",
            body=maybe_transform(body, Iterable[item_unvalidated_publish_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncItemResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncItemResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncItemResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncItemResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncItemResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        scan_code: str,
        source: str,
        type: str,
        id: str | NotGiven = NOT_GIVEN,
        acc_sys_keys: List[str] | NotGiven = NOT_GIVEN,
        acc_sys_notes: str | NotGiven = NOT_GIVEN,
        acc_system: str | NotGiven = NOT_GIVEN,
        acc_sys_values: List[str] | NotGiven = NOT_GIVEN,
        airdrop: bool | NotGiven = NOT_GIVEN,
        alt_data_format: str | NotGiven = NOT_GIVEN,
        cargo_type: str | NotGiven = NOT_GIVEN,
        centerline_offset: float | NotGiven = NOT_GIVEN,
        cg: float | NotGiven = NOT_GIVEN,
        commodity_code: str | NotGiven = NOT_GIVEN,
        commodity_sys: str | NotGiven = NOT_GIVEN,
        container: bool | NotGiven = NOT_GIVEN,
        departure: str | NotGiven = NOT_GIVEN,
        destination: str | NotGiven = NOT_GIVEN,
        dv_code: str | NotGiven = NOT_GIVEN,
        fs: float | NotGiven = NOT_GIVEN,
        haz_codes: Iterable[float] | NotGiven = NOT_GIVEN,
        height: float | NotGiven = NOT_GIVEN,
        id_air_load_plan: str | NotGiven = NOT_GIVEN,
        item_contains: List[str] | NotGiven = NOT_GIVEN,
        keys: List[str] | NotGiven = NOT_GIVEN,
        last_arr_date: Union[str, date] | NotGiven = NOT_GIVEN,
        length: float | NotGiven = NOT_GIVEN,
        moment: float | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        net_exp_wt: float | NotGiven = NOT_GIVEN,
        notes: str | NotGiven = NOT_GIVEN,
        num_pallet_pos: int | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        product_code: str | NotGiven = NOT_GIVEN,
        product_sys: str | NotGiven = NOT_GIVEN,
        receiving_branch: str | NotGiven = NOT_GIVEN,
        receiving_unit: str | NotGiven = NOT_GIVEN,
        sc_gen_tool: str | NotGiven = NOT_GIVEN,
        tcn: str | NotGiven = NOT_GIVEN,
        uln: str | NotGiven = NOT_GIVEN,
        values: List[str] | NotGiven = NOT_GIVEN,
        volume: float | NotGiven = NOT_GIVEN,
        weight: float | NotGiven = NOT_GIVEN,
        weight_ts: Union[str, datetime] | NotGiven = NOT_GIVEN,
        width: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single item record as a POST body and ingest into
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

          scan_code: The tracking identifier of an item or person. May be similar in representation
              of a barcode or UPC. If no scanCode or tracking number equivalent is available,
              'NONE' should be used.

          source: Source of the data.

          type: The item type of this record (e.g. EQUIPMENT, CARGO, PASSENGER).

          id: Unique identifier of the record, auto-generated by the system if not provided on
              create operations.

          acc_sys_keys: Array of keys that may be associated to the accepting system data. The entries
              in this array must correspond to the position index in accSysValues array. This
              array must be the same length as accSysValues.

          acc_sys_notes: Additional data required to find this item in the accepting system.

          acc_system: Name of the system that accepted this item from a customer. Where a user or
              application could go look for additional information.

          acc_sys_values: Array of values for the keys that may be associated to the accepting system
              data. The entries in this array must correspond to the position index in
              accSysKeys array. This array must be the same length as accSysKeys.

          airdrop: Flag indicating this item is planned to be airdropped. Applicable for cargo and
              passenger item types only.

          alt_data_format: Name of the additional data format so downstream consuming applications can know
              how to parse it. Typically includes the source system name and the format name.

          cargo_type: The type of cargo (e.g. PALLET, ROLLING STOCK, LOOSE, OTHER). Applicable for
              cargo item types only.

          centerline_offset: How far left or right of centerline is the item in meters. Applicable for cargo
              and passenger item types only.

          cg: Center of gravity position of the item, measured from the item's front datum, in
              centimeters.

          commodity_code: The classification code of the commodity or group of commodities.

          commodity_sys: The classification system denoting the commodity code, commodityCode (e.g. AIR,
              WATER, NMFC, UFC, STCC, DODUNQ, etc.).

          container: Flag indicating this item acts as a container and contains additional items.

          departure: The departure code or location where this item has left or is leaving.

          destination: The destination of the item, typically an ICAO or port code. Applicable for
              cargo and passenger item types only.

          dv_code: United States Distinguished Visitor Code, only applicable to people.

          fs: The fuselage station of the item measured from the reference datum, in
              centimeters. Applicable for cargo and passenger item types only.

          haz_codes: Array of UN hazard classes or division codes that apply to this item.

          height: Height of the cargo in meters. Applicable for cargo item types only.

          id_air_load_plan: The UDL ID of the air load plan this item is associated with.

          item_contains: Array of tracking identifiers that are contained within this item.

          keys: Array of keys that may be associated to this item. The entries in this array
              must correspond to the position index in the values array. This array must be
              the same length as values..

          last_arr_date: The latest acceptable arrival date of the item at the destination, in ISO 8601
              date-only format (e.g. YYYY-MM-DD).

          length: Length of the cargo in meters. Applicable for cargo item types only.

          moment: Moment of the item in Newton-meters. Applicable for equipment and cargo item
              types only.

          name: Name of the item. Applicable for equipment and cargo item types only.

          net_exp_wt: Net explosive weight of the item, in kilograms.

          notes: Optional notes or comments about this item.

          num_pallet_pos: Number of pallet positions or equivalent on the aircraft, ship, or conveyance
              equipment that this item occupies.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          product_code: The code denoting the type of material item.

          product_sys: The assigning system that denotes the type of material item, productCode (e.g.
              NSN-national stock number, NDC-national drug code, MPN-manufacturer part number,
              etc.).

          receiving_branch: The military branch receiving this item.

          receiving_unit: The name of the unit receiving this item.

          sc_gen_tool: The algorithm name or standard that generated the scanCode (e.g. UPC-A, EAN-13,
              GTIN, SSCC, bID, JAN, etc.).

          tcn: Transportation Control Number of the cargo. Applicable for cargo item types
              only.

          uln: The unit line number of this item.

          values: Array of values for the keys that may be associated to this tracked item. The
              entries in this array must correspond to the position index in the keys array.
              This array must be the same length as keys.

          volume: The volume of the item, in cubic meters. Applicable for cargo item types only.

          weight: Weight of the item in kilograms (if item is a passenger, include on-person
              bags).

          weight_ts: Timestamp when the weight was taken, in ISO 8601 UTC format with millisecond
              precision.

          width: Width of the cargo in meters. Applicable for cargo item types only.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/udl/item",
            body=await async_maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "scan_code": scan_code,
                    "source": source,
                    "type": type,
                    "id": id,
                    "acc_sys_keys": acc_sys_keys,
                    "acc_sys_notes": acc_sys_notes,
                    "acc_system": acc_system,
                    "acc_sys_values": acc_sys_values,
                    "airdrop": airdrop,
                    "alt_data_format": alt_data_format,
                    "cargo_type": cargo_type,
                    "centerline_offset": centerline_offset,
                    "cg": cg,
                    "commodity_code": commodity_code,
                    "commodity_sys": commodity_sys,
                    "container": container,
                    "departure": departure,
                    "destination": destination,
                    "dv_code": dv_code,
                    "fs": fs,
                    "haz_codes": haz_codes,
                    "height": height,
                    "id_air_load_plan": id_air_load_plan,
                    "item_contains": item_contains,
                    "keys": keys,
                    "last_arr_date": last_arr_date,
                    "length": length,
                    "moment": moment,
                    "name": name,
                    "net_exp_wt": net_exp_wt,
                    "notes": notes,
                    "num_pallet_pos": num_pallet_pos,
                    "origin": origin,
                    "product_code": product_code,
                    "product_sys": product_sys,
                    "receiving_branch": receiving_branch,
                    "receiving_unit": receiving_unit,
                    "sc_gen_tool": sc_gen_tool,
                    "tcn": tcn,
                    "uln": uln,
                    "values": values,
                    "volume": volume,
                    "weight": weight,
                    "weight_ts": weight_ts,
                    "width": width,
                },
                item_create_params.ItemCreateParams,
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
        scan_code: str,
        source: str,
        type: str,
        body_id: str | NotGiven = NOT_GIVEN,
        acc_sys_keys: List[str] | NotGiven = NOT_GIVEN,
        acc_sys_notes: str | NotGiven = NOT_GIVEN,
        acc_system: str | NotGiven = NOT_GIVEN,
        acc_sys_values: List[str] | NotGiven = NOT_GIVEN,
        airdrop: bool | NotGiven = NOT_GIVEN,
        alt_data_format: str | NotGiven = NOT_GIVEN,
        cargo_type: str | NotGiven = NOT_GIVEN,
        centerline_offset: float | NotGiven = NOT_GIVEN,
        cg: float | NotGiven = NOT_GIVEN,
        commodity_code: str | NotGiven = NOT_GIVEN,
        commodity_sys: str | NotGiven = NOT_GIVEN,
        container: bool | NotGiven = NOT_GIVEN,
        departure: str | NotGiven = NOT_GIVEN,
        destination: str | NotGiven = NOT_GIVEN,
        dv_code: str | NotGiven = NOT_GIVEN,
        fs: float | NotGiven = NOT_GIVEN,
        haz_codes: Iterable[float] | NotGiven = NOT_GIVEN,
        height: float | NotGiven = NOT_GIVEN,
        id_air_load_plan: str | NotGiven = NOT_GIVEN,
        item_contains: List[str] | NotGiven = NOT_GIVEN,
        keys: List[str] | NotGiven = NOT_GIVEN,
        last_arr_date: Union[str, date] | NotGiven = NOT_GIVEN,
        length: float | NotGiven = NOT_GIVEN,
        moment: float | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        net_exp_wt: float | NotGiven = NOT_GIVEN,
        notes: str | NotGiven = NOT_GIVEN,
        num_pallet_pos: int | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        product_code: str | NotGiven = NOT_GIVEN,
        product_sys: str | NotGiven = NOT_GIVEN,
        receiving_branch: str | NotGiven = NOT_GIVEN,
        receiving_unit: str | NotGiven = NOT_GIVEN,
        sc_gen_tool: str | NotGiven = NOT_GIVEN,
        tcn: str | NotGiven = NOT_GIVEN,
        uln: str | NotGiven = NOT_GIVEN,
        values: List[str] | NotGiven = NOT_GIVEN,
        volume: float | NotGiven = NOT_GIVEN,
        weight: float | NotGiven = NOT_GIVEN,
        weight_ts: Union[str, datetime] | NotGiven = NOT_GIVEN,
        width: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Service operation to update a single Item.

        An Item can be cargo, equipment, or a
        passenger. A specific role is required to perform this service operation. Please
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

          scan_code: The tracking identifier of an item or person. May be similar in representation
              of a barcode or UPC. If no scanCode or tracking number equivalent is available,
              'NONE' should be used.

          source: Source of the data.

          type: The item type of this record (e.g. EQUIPMENT, CARGO, PASSENGER).

          body_id: Unique identifier of the record, auto-generated by the system if not provided on
              create operations.

          acc_sys_keys: Array of keys that may be associated to the accepting system data. The entries
              in this array must correspond to the position index in accSysValues array. This
              array must be the same length as accSysValues.

          acc_sys_notes: Additional data required to find this item in the accepting system.

          acc_system: Name of the system that accepted this item from a customer. Where a user or
              application could go look for additional information.

          acc_sys_values: Array of values for the keys that may be associated to the accepting system
              data. The entries in this array must correspond to the position index in
              accSysKeys array. This array must be the same length as accSysKeys.

          airdrop: Flag indicating this item is planned to be airdropped. Applicable for cargo and
              passenger item types only.

          alt_data_format: Name of the additional data format so downstream consuming applications can know
              how to parse it. Typically includes the source system name and the format name.

          cargo_type: The type of cargo (e.g. PALLET, ROLLING STOCK, LOOSE, OTHER). Applicable for
              cargo item types only.

          centerline_offset: How far left or right of centerline is the item in meters. Applicable for cargo
              and passenger item types only.

          cg: Center of gravity position of the item, measured from the item's front datum, in
              centimeters.

          commodity_code: The classification code of the commodity or group of commodities.

          commodity_sys: The classification system denoting the commodity code, commodityCode (e.g. AIR,
              WATER, NMFC, UFC, STCC, DODUNQ, etc.).

          container: Flag indicating this item acts as a container and contains additional items.

          departure: The departure code or location where this item has left or is leaving.

          destination: The destination of the item, typically an ICAO or port code. Applicable for
              cargo and passenger item types only.

          dv_code: United States Distinguished Visitor Code, only applicable to people.

          fs: The fuselage station of the item measured from the reference datum, in
              centimeters. Applicable for cargo and passenger item types only.

          haz_codes: Array of UN hazard classes or division codes that apply to this item.

          height: Height of the cargo in meters. Applicable for cargo item types only.

          id_air_load_plan: The UDL ID of the air load plan this item is associated with.

          item_contains: Array of tracking identifiers that are contained within this item.

          keys: Array of keys that may be associated to this item. The entries in this array
              must correspond to the position index in the values array. This array must be
              the same length as values..

          last_arr_date: The latest acceptable arrival date of the item at the destination, in ISO 8601
              date-only format (e.g. YYYY-MM-DD).

          length: Length of the cargo in meters. Applicable for cargo item types only.

          moment: Moment of the item in Newton-meters. Applicable for equipment and cargo item
              types only.

          name: Name of the item. Applicable for equipment and cargo item types only.

          net_exp_wt: Net explosive weight of the item, in kilograms.

          notes: Optional notes or comments about this item.

          num_pallet_pos: Number of pallet positions or equivalent on the aircraft, ship, or conveyance
              equipment that this item occupies.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          product_code: The code denoting the type of material item.

          product_sys: The assigning system that denotes the type of material item, productCode (e.g.
              NSN-national stock number, NDC-national drug code, MPN-manufacturer part number,
              etc.).

          receiving_branch: The military branch receiving this item.

          receiving_unit: The name of the unit receiving this item.

          sc_gen_tool: The algorithm name or standard that generated the scanCode (e.g. UPC-A, EAN-13,
              GTIN, SSCC, bID, JAN, etc.).

          tcn: Transportation Control Number of the cargo. Applicable for cargo item types
              only.

          uln: The unit line number of this item.

          values: Array of values for the keys that may be associated to this tracked item. The
              entries in this array must correspond to the position index in the keys array.
              This array must be the same length as keys.

          volume: The volume of the item, in cubic meters. Applicable for cargo item types only.

          weight: Weight of the item in kilograms (if item is a passenger, include on-person
              bags).

          weight_ts: Timestamp when the weight was taken, in ISO 8601 UTC format with millisecond
              precision.

          width: Width of the cargo in meters. Applicable for cargo item types only.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            f"/udl/item/{path_id}",
            body=await async_maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "scan_code": scan_code,
                    "source": source,
                    "type": type,
                    "body_id": body_id,
                    "acc_sys_keys": acc_sys_keys,
                    "acc_sys_notes": acc_sys_notes,
                    "acc_system": acc_system,
                    "acc_sys_values": acc_sys_values,
                    "airdrop": airdrop,
                    "alt_data_format": alt_data_format,
                    "cargo_type": cargo_type,
                    "centerline_offset": centerline_offset,
                    "cg": cg,
                    "commodity_code": commodity_code,
                    "commodity_sys": commodity_sys,
                    "container": container,
                    "departure": departure,
                    "destination": destination,
                    "dv_code": dv_code,
                    "fs": fs,
                    "haz_codes": haz_codes,
                    "height": height,
                    "id_air_load_plan": id_air_load_plan,
                    "item_contains": item_contains,
                    "keys": keys,
                    "last_arr_date": last_arr_date,
                    "length": length,
                    "moment": moment,
                    "name": name,
                    "net_exp_wt": net_exp_wt,
                    "notes": notes,
                    "num_pallet_pos": num_pallet_pos,
                    "origin": origin,
                    "product_code": product_code,
                    "product_sys": product_sys,
                    "receiving_branch": receiving_branch,
                    "receiving_unit": receiving_unit,
                    "sc_gen_tool": sc_gen_tool,
                    "tcn": tcn,
                    "uln": uln,
                    "values": values,
                    "volume": volume,
                    "weight": weight,
                    "weight_ts": weight_ts,
                    "width": width,
                },
                item_update_params.ItemUpdateParams,
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
    ) -> AsyncPaginator[ItemListResponse, AsyncOffsetPage[ItemListResponse]]:
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
            "/udl/item",
            page=AsyncOffsetPage[ItemListResponse],
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
                    item_list_params.ItemListParams,
                ),
            ),
            model=ItemListResponse,
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
        Service operation to delete a item record specified by the passed ID path
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
            f"/udl/item/{id}",
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
            "/udl/item/count",
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
                    item_count_params.ItemCountParams,
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
    ) -> ItemGetResponse:
        """
        Service operation to get a single item record by its unique ID passed as a path
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
            f"/udl/item/{id}",
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
                    item_get_params.ItemGetParams,
                ),
            ),
            cast_to=ItemGetResponse,
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
    ) -> ItemQueryhelpResponse:
        """
        Service operation to provide detailed information on available dynamic query
        parameters for a particular data type.
        """
        return await self._get(
            "/udl/item/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ItemQueryhelpResponse,
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
    ) -> ItemTupleResponse:
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
            "/udl/item/tuple",
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
                    item_tuple_params.ItemTupleParams,
                ),
            ),
            cast_to=ItemTupleResponse,
        )

    async def unvalidated_publish(
        self,
        *,
        body: Iterable[item_unvalidated_publish_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take multiple item records as a POST body and ingest into
        the database. This operation is intended to be used for automated feeds into
        UDL. A specific role is required to perform this service operation. Please
        contact the UDL team for assistance.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/filedrop/udl-item",
            body=await async_maybe_transform(body, Iterable[item_unvalidated_publish_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class ItemResourceWithRawResponse:
    def __init__(self, item: ItemResource) -> None:
        self._item = item

        self.create = to_raw_response_wrapper(
            item.create,
        )
        self.update = to_raw_response_wrapper(
            item.update,
        )
        self.list = to_raw_response_wrapper(
            item.list,
        )
        self.delete = to_raw_response_wrapper(
            item.delete,
        )
        self.count = to_raw_response_wrapper(
            item.count,
        )
        self.get = to_raw_response_wrapper(
            item.get,
        )
        self.queryhelp = to_raw_response_wrapper(
            item.queryhelp,
        )
        self.tuple = to_raw_response_wrapper(
            item.tuple,
        )
        self.unvalidated_publish = to_raw_response_wrapper(
            item.unvalidated_publish,
        )


class AsyncItemResourceWithRawResponse:
    def __init__(self, item: AsyncItemResource) -> None:
        self._item = item

        self.create = async_to_raw_response_wrapper(
            item.create,
        )
        self.update = async_to_raw_response_wrapper(
            item.update,
        )
        self.list = async_to_raw_response_wrapper(
            item.list,
        )
        self.delete = async_to_raw_response_wrapper(
            item.delete,
        )
        self.count = async_to_raw_response_wrapper(
            item.count,
        )
        self.get = async_to_raw_response_wrapper(
            item.get,
        )
        self.queryhelp = async_to_raw_response_wrapper(
            item.queryhelp,
        )
        self.tuple = async_to_raw_response_wrapper(
            item.tuple,
        )
        self.unvalidated_publish = async_to_raw_response_wrapper(
            item.unvalidated_publish,
        )


class ItemResourceWithStreamingResponse:
    def __init__(self, item: ItemResource) -> None:
        self._item = item

        self.create = to_streamed_response_wrapper(
            item.create,
        )
        self.update = to_streamed_response_wrapper(
            item.update,
        )
        self.list = to_streamed_response_wrapper(
            item.list,
        )
        self.delete = to_streamed_response_wrapper(
            item.delete,
        )
        self.count = to_streamed_response_wrapper(
            item.count,
        )
        self.get = to_streamed_response_wrapper(
            item.get,
        )
        self.queryhelp = to_streamed_response_wrapper(
            item.queryhelp,
        )
        self.tuple = to_streamed_response_wrapper(
            item.tuple,
        )
        self.unvalidated_publish = to_streamed_response_wrapper(
            item.unvalidated_publish,
        )


class AsyncItemResourceWithStreamingResponse:
    def __init__(self, item: AsyncItemResource) -> None:
        self._item = item

        self.create = async_to_streamed_response_wrapper(
            item.create,
        )
        self.update = async_to_streamed_response_wrapper(
            item.update,
        )
        self.list = async_to_streamed_response_wrapper(
            item.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            item.delete,
        )
        self.count = async_to_streamed_response_wrapper(
            item.count,
        )
        self.get = async_to_streamed_response_wrapper(
            item.get,
        )
        self.queryhelp = async_to_streamed_response_wrapper(
            item.queryhelp,
        )
        self.tuple = async_to_streamed_response_wrapper(
            item.tuple,
        )
        self.unvalidated_publish = async_to_streamed_response_wrapper(
            item.unvalidated_publish,
        )
