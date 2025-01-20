# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from datetime import datetime

import httpx

from ..types import udl_sigact_text_create_params
from .._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options

__all__ = ["UdlSigactTextResource", "AsyncUdlSigactTextResource"]


class UdlSigactTextResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UdlSigactTextResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/unifieddatalibrary-python#accessing-raw-response-data-eg-headers
        """
        return UdlSigactTextResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UdlSigactTextResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/unifieddatalibrary-python#with_streaming_response
        """
        return UdlSigactTextResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        classification_marking: str,
        data_mode: str,
        report_date: Union[str, datetime],
        source: str,
        id: str | NotGiven = NOT_GIVEN,
        accuracy: int | NotGiven = NOT_GIVEN,
        actors: List[str] | NotGiven = NOT_GIVEN,
        agjson: str | NotGiven = NOT_GIVEN,
        andims: int | NotGiven = NOT_GIVEN,
        area: str | NotGiven = NOT_GIVEN,
        asrid: int | NotGiven = NOT_GIVEN,
        atext: str | NotGiven = NOT_GIVEN,
        atype: str | NotGiven = NOT_GIVEN,
        avg_tone: float | NotGiven = NOT_GIVEN,
        cameo_base_code: str | NotGiven = NOT_GIVEN,
        cameo_code: str | NotGiven = NOT_GIVEN,
        cameo_root_code: str | NotGiven = NOT_GIVEN,
        checksum_value: str | NotGiven = NOT_GIVEN,
        city: str | NotGiven = NOT_GIVEN,
        civ_abd: int | NotGiven = NOT_GIVEN,
        civ_det: int | NotGiven = NOT_GIVEN,
        civ_kia: int | NotGiven = NOT_GIVEN,
        civ_wound: int | NotGiven = NOT_GIVEN,
        clarity: int | NotGiven = NOT_GIVEN,
        coal_abd: int | NotGiven = NOT_GIVEN,
        coal_det: int | NotGiven = NOT_GIVEN,
        coal_kia: int | NotGiven = NOT_GIVEN,
        coal_wound: int | NotGiven = NOT_GIVEN,
        complex_attack: bool | NotGiven = NOT_GIVEN,
        confidence: int | NotGiven = NOT_GIVEN,
        country_code: str | NotGiven = NOT_GIVEN,
        created_at: Union[str, datetime] | NotGiven = NOT_GIVEN,
        created_by: str | NotGiven = NOT_GIVEN,
        district: str | NotGiven = NOT_GIVEN,
        document_filename: str | NotGiven = NOT_GIVEN,
        document_source: str | NotGiven = NOT_GIVEN,
        enemy_abd: int | NotGiven = NOT_GIVEN,
        enemy_det: int | NotGiven = NOT_GIVEN,
        enemy_kia: int | NotGiven = NOT_GIVEN,
        event_description: str | NotGiven = NOT_GIVEN,
        event_end: Union[str, datetime] | NotGiven = NOT_GIVEN,
        event_start: Union[str, datetime] | NotGiven = NOT_GIVEN,
        event_type: str | NotGiven = NOT_GIVEN,
        filesize: int | NotGiven = NOT_GIVEN,
        friendly_abd: int | NotGiven = NOT_GIVEN,
        friendly_det: int | NotGiven = NOT_GIVEN,
        friendly_kia: int | NotGiven = NOT_GIVEN,
        friendly_wound: int | NotGiven = NOT_GIVEN,
        goldstein: float | NotGiven = NOT_GIVEN,
        has_attachment: bool | NotGiven = NOT_GIVEN,
        host_nat_abd: int | NotGiven = NOT_GIVEN,
        host_nat_det: int | NotGiven = NOT_GIVEN,
        host_nat_kia: int | NotGiven = NOT_GIVEN,
        host_nat_wound: int | NotGiven = NOT_GIVEN,
        id_number: str | NotGiven = NOT_GIVEN,
        lat: float | NotGiven = NOT_GIVEN,
        lon: float | NotGiven = NOT_GIVEN,
        milgrid: str | NotGiven = NOT_GIVEN,
        notes: str | NotGiven = NOT_GIVEN,
        num_articles: int | NotGiven = NOT_GIVEN,
        num_mentions: int | NotGiven = NOT_GIVEN,
        num_sources: int | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        orig_network: str | NotGiven = NOT_GIVEN,
        province: str | NotGiven = NOT_GIVEN,
        related_docs: Iterable[udl_sigact_text_create_params.RelatedDoc] | NotGiven = NOT_GIVEN,
        rep_unit: str | NotGiven = NOT_GIVEN,
        rep_unit_activity: str | NotGiven = NOT_GIVEN,
        rep_unit_type: str | NotGiven = NOT_GIVEN,
        side_a_abd: int | NotGiven = NOT_GIVEN,
        side_a_det: int | NotGiven = NOT_GIVEN,
        side_akia: int | NotGiven = NOT_GIVEN,
        side_a_wound: int | NotGiven = NOT_GIVEN,
        side_b_abd: int | NotGiven = NOT_GIVEN,
        side_b_det: int | NotGiven = NOT_GIVEN,
        side_bkia: int | NotGiven = NOT_GIVEN,
        side_b_wound: int | NotGiven = NOT_GIVEN,
        source_language: str | NotGiven = NOT_GIVEN,
        source_url: str | NotGiven = NOT_GIVEN,
        summary: str | NotGiven = NOT_GIVEN,
        target: str | NotGiven = NOT_GIVEN,
        theater: str | NotGiven = NOT_GIVEN,
        type_of_attack: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        The sigact-txt service allows for contribution of large text that exceeds the
        limits of the sigact.eventDescription field (4096 characters). This service
        operation requires a zip file in the body of the POST request. The zip file must
        contain exactly two files. <h3> 1) A json file with any file name that ends in
        .json e.g. MyDataFile.json. The contents of the json file must be valid
        according to the schema for sigact. 2) A txt file of the text encoded in UTF-8.
        </h3> The sigact metadata and text file will be stored and associated with each
        other allowing queries of the data retrieval of the text. This operation is
        intended to be used for automated feeds into UDL. A specific role is required to
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

          report_date: Date of the report or filing.

          source: Source of the data.

          id: Unique identifier of the record, auto-generated by the system.

          accuracy: Estimate of the accuracy that this event occurred as described/reported.

          actors: A list of one or more actors involved in the event.

          agjson: Geographical region or polygon (lat/lon pairs), as depicted by the GeoJSON
              representation of the geometry/geography, of the image as projected on the
              ground. GeoJSON Reference: https://geojson.org/. Ignored if included with a POST
              or PUT request that also specifies a valid 'area' or 'atext' field.

          andims: Number of dimensions of the geometry depicted by region.

          area: Optional geographical region or polygon (lat/lon pairs) of the area surrounding
              the point of interest as projected on the ground.

          asrid: Geographical spatial_ref_sys for region.

          atext: Geographical region or polygon (lon/lat pairs), as depicted by the Well-Known
              Text representation of the geometry/geography, of the image as projected on the
              ground. WKT reference: https://www.opengeospatial.org/standards/wkt-crs. Ignored
              if included with a POST or PUT request that also specifies a valid 'area' field.

          atype: Type of region as projected on the ground.

          avg_tone: This is the average tone of all documents containing one or more mentions of
              this event during the 15 minute update in which it was first seen. The score
              ranges from -100 (extremely negative) to +100 (extremely positive). Common
              values range between -10 and +10, with 0 indicating neutral.

          cameo_base_code: CAMEO event codes are defined in a three-level taxonomy. For events at level
              three in the taxonomy, this yields its level two leaf root node. For example,
              code 0251 (Appeal for easing of administrative sanctions) would yield an
              EventBaseCode of 025 (Appeal to yield). This makes it possible to aggregate
              events at various resolutions of specificity. For events at levels two or one,
              this field will be set to EventCode.

          cameo_code: This is the raw CAMEO action code describing the action that Actor1 performed
              upon Actor2. Additional information about Cameo Codes can be obtained from the
              GDELT project documentation here:
              https://www.gdeltproject.org/data.html#documentation.

          cameo_root_code: Similar to EventBaseCode, this defines the root-level category the event code
              falls under. For example, code 0251 (Appeal for easing of administrative
              sanctions) has a root code of 02 (Appeal). This makes it possible to aggregate
              events at various resolutions of specificity. For events at levels two or one,
              this field will be set to EventCode.

          checksum_value: MD5 value of the file. The ingest/create operation will automatically generate
              the value.

          city: The city in or near which this event occurred.

          civ_abd: Number of civilians abducted in the activity.

          civ_det: Number of civilians detained in the activity.

          civ_kia: Number of civilians killed in the activity.

          civ_wound: Number of civilians wounded in the activity.

          clarity: 1 (high) for events where the reporting allows the coder to identify the event
              in full. That is, events where the individual happening is described by the
              original source in a sufficiently detailed way as to identify individual
              incidents, i.e. separate activities of fighting in a single location:

              2 (lower) for events where an aggregation of information was already made by the
              source material that is impossible to undo in the coding process. Such events
              are described by the original source only as aggregates (totals) of multiple
              separate activities of fighting spanning over a longer period than a single,
              clearly defined day.

          coal_abd: Number of coalition members abducted in the activity.

          coal_det: Number of coalition members detained in the activity.

          coal_kia: Number of coalition members killed in the activity.

          coal_wound: Number of coalition members wounded in the activity.

          complex_attack: Flag indicating that this attack was of a complex or coordinated nature.

          confidence: Estimate of the confidence that this event occurred.

          country_code: The country code. This value is typically the ISO 3166 Alpha-2 two-character
              country code, however it can also represent various consortiums that do not
              appear in the ISO document. The code must correspond to an existing country in
              the UDL�s country API. Call udl/country/{code} to get any associated FIPS code,
              ISO Alpha-3 code, or alternate code values that exist for the specified country
              code.

          created_at: Time the row was created in the database, auto-populated by the system, example
              = 2018-01-01T16:00:00.123Z.

          created_by: Application user who created the row in the database, auto-populated by the
              system.

          district: The district in which this event occurred.

          document_filename: The filename of the document or report.

          document_source: The source of the document or report.

          enemy_abd: Number of enemy combatants abducted in the activity.

          enemy_det: Number of enemy combatants detained in the activity.

          enemy_kia: Number of enemy combatants killed in the activity.

          event_description: A description of the event.

          event_end: The approximate end time of the event, in ISO 8601 UTC format.

          event_start: The approximate start time of the event, in ISO 8601 UTC format.

          event_type: The type of event (e.g. Military, Natural, Political, Social, etc.).

          filesize: Size of the associated text file. Units in bytes. If filesize is provided
              without an associated file, it defaults to 0.

          friendly_abd: Number of friendlies abducted in the activity.

          friendly_det: Number of friendlies in the activity.

          friendly_kia: Number of friendlies killed in the activity.

          friendly_wound: Number of friendlies wounded in the activity.

          goldstein: Each CAMEO event code is assigned a numeric score from -10 to +10, capturing the
              theoretical potential impact that type of event will have on the stability of a
              country. This is known as the Goldstein Scale. NOTE: this score is based on the
              type of event, not the specifics of the actual event record being recorded thus
              two riots, one with 10 people and one with 10,000, will both receive the same
              Goldstein score. This can be aggregated to various levels of time resolution to
              yield an approximation of the stability of a location over time.

          has_attachment: Flag indicating this SigAct record has an associated txt file stored in the UDL.
              Retrieve the txt file by using the GET/udl/sigact/getFile/{id} where id is the
              same as the SigAct record id. The maximum file size for this service is
              10,000,000 bytes (10MB). Files exceeding the maximum size will be rejected.

          host_nat_abd: Number of Host Nation members abducted in the activity.

          host_nat_det: Number of Host Nation members detained in the activity.

          host_nat_kia: Number of Host Nation members killed in the activity.

          host_nat_wound: Number of Host Nation members wounded in the activity.

          id_number: Unique identifier assigned to each event record that uniquely identifies it in
              the master dataset. This ID is provided for convenience of mapping to external
              systems.

          lat: WGS-84 centroid latitude of the event location, in degrees. -90 to 90 degrees
              (negative values south of equator).

          lon: WGS-84 centroid longitude of the event location, in degrees. -180 to 180 degrees
              (negative values west of Prime Meridian).

          milgrid: The Military Grid Reference System is the geocoordinate standard used by NATO
              militaries for locating points on Earth. The MGRS is derived from the Universal
              Transverse Mercator (UTM) grid system and the Universal Polar Stereographic
              (UPS) grid system, but uses a different labeling convention. The MGRS is used as
              geocode for the entire Earth. Example of an milgrid coordinate, or grid
              reference, would be 4QFJ12345678, which consists of three parts:

              &nbsp;&nbsp;4Q (grid zone designator, GZD)

              &nbsp;&nbsp;FJ (the 100,000-meter square identifier)

              &nbsp;&nbsp;12345678 (numerical location; easting is 1234 and northing is 5678,
              in this case specifying a location with 10 m resolution).

          notes: Notes related to the documents or event.

          num_articles: This is the total number of source documents containing one or more mentions of
              this event during the 15 minute update in which it was first seen. This can be
              used as a method of assessing the importance of an event: the more discussion of
              that event, the more likely it is to be significant.

          num_mentions: This is the total number of mentions of this event across all source documents
              during the 15 minute update in which it was first seen. Multiple references to
              an event within a single document also contribute to this count. This can be
              used as a method of assessing the importance of an event: the more discussion of
              that event, the more likely it is to be significant.

          num_sources: This is the total number of information sources containing one or more mentions
              of this event during the 15 minute update in which it was first seen. This can
              be used as a method of assessing the importance of an event: the more discussion
              of that event, the more likely it is to be significant.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          orig_network: The originating source network on which this record was created, auto-populated
              by the system.

          province: The province in which this event occurred.

          related_docs: Related document ids.

          rep_unit: The reporting unit.

          rep_unit_activity: The activity the unit was engaged in.

          rep_unit_type: The reporting unit type.

          side_a_abd: Number of side A members abducted in the activity.

          side_a_det: Number of side A members detained in the activity.

          side_akia: Number of side A members killed in the activity.

          side_a_wound: Number of side A members wounded in the activity.

          side_b_abd: Number of side B members abducted in the activity.

          side_b_det: Number of side B members detained in the activity.

          side_bkia: Number of side B members killed in the activity.

          side_b_wound: Number of side B members wounded in the activity.

          source_language: The source language of the significant event using the ISO 639-3, 3 character
              code definition.

          source_url: This field records the URL or citation of the first news report it found this
              event in. In most cases this is the first report it saw the article in, but due
              to the timing and flow of news reports through the processing pipeline, this may
              not always be the very first report, but is at least in the first few reports.

          summary: A summary of the event.

          target: The name of the target. The target may be an individual, an entity, or a
              country/region.

          theater: Area in which important military events occur or are progressing. A theater can
              include the entirety of the airspace, land and sea area that is or that may
              potentially become involved in war operations.

          type_of_attack: The mode of this attack or event (e.g. Direct Fire, IED Explosion, etc.).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/filedrop/udl-sigact-text",
            body=maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "report_date": report_date,
                    "source": source,
                    "id": id,
                    "accuracy": accuracy,
                    "actors": actors,
                    "agjson": agjson,
                    "andims": andims,
                    "area": area,
                    "asrid": asrid,
                    "atext": atext,
                    "atype": atype,
                    "avg_tone": avg_tone,
                    "cameo_base_code": cameo_base_code,
                    "cameo_code": cameo_code,
                    "cameo_root_code": cameo_root_code,
                    "checksum_value": checksum_value,
                    "city": city,
                    "civ_abd": civ_abd,
                    "civ_det": civ_det,
                    "civ_kia": civ_kia,
                    "civ_wound": civ_wound,
                    "clarity": clarity,
                    "coal_abd": coal_abd,
                    "coal_det": coal_det,
                    "coal_kia": coal_kia,
                    "coal_wound": coal_wound,
                    "complex_attack": complex_attack,
                    "confidence": confidence,
                    "country_code": country_code,
                    "created_at": created_at,
                    "created_by": created_by,
                    "district": district,
                    "document_filename": document_filename,
                    "document_source": document_source,
                    "enemy_abd": enemy_abd,
                    "enemy_det": enemy_det,
                    "enemy_kia": enemy_kia,
                    "event_description": event_description,
                    "event_end": event_end,
                    "event_start": event_start,
                    "event_type": event_type,
                    "filesize": filesize,
                    "friendly_abd": friendly_abd,
                    "friendly_det": friendly_det,
                    "friendly_kia": friendly_kia,
                    "friendly_wound": friendly_wound,
                    "goldstein": goldstein,
                    "has_attachment": has_attachment,
                    "host_nat_abd": host_nat_abd,
                    "host_nat_det": host_nat_det,
                    "host_nat_kia": host_nat_kia,
                    "host_nat_wound": host_nat_wound,
                    "id_number": id_number,
                    "lat": lat,
                    "lon": lon,
                    "milgrid": milgrid,
                    "notes": notes,
                    "num_articles": num_articles,
                    "num_mentions": num_mentions,
                    "num_sources": num_sources,
                    "origin": origin,
                    "orig_network": orig_network,
                    "province": province,
                    "related_docs": related_docs,
                    "rep_unit": rep_unit,
                    "rep_unit_activity": rep_unit_activity,
                    "rep_unit_type": rep_unit_type,
                    "side_a_abd": side_a_abd,
                    "side_a_det": side_a_det,
                    "side_akia": side_akia,
                    "side_a_wound": side_a_wound,
                    "side_b_abd": side_b_abd,
                    "side_b_det": side_b_det,
                    "side_bkia": side_bkia,
                    "side_b_wound": side_b_wound,
                    "source_language": source_language,
                    "source_url": source_url,
                    "summary": summary,
                    "target": target,
                    "theater": theater,
                    "type_of_attack": type_of_attack,
                },
                udl_sigact_text_create_params.UdlSigactTextCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncUdlSigactTextResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUdlSigactTextResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/unifieddatalibrary-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUdlSigactTextResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUdlSigactTextResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/unifieddatalibrary-python#with_streaming_response
        """
        return AsyncUdlSigactTextResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        classification_marking: str,
        data_mode: str,
        report_date: Union[str, datetime],
        source: str,
        id: str | NotGiven = NOT_GIVEN,
        accuracy: int | NotGiven = NOT_GIVEN,
        actors: List[str] | NotGiven = NOT_GIVEN,
        agjson: str | NotGiven = NOT_GIVEN,
        andims: int | NotGiven = NOT_GIVEN,
        area: str | NotGiven = NOT_GIVEN,
        asrid: int | NotGiven = NOT_GIVEN,
        atext: str | NotGiven = NOT_GIVEN,
        atype: str | NotGiven = NOT_GIVEN,
        avg_tone: float | NotGiven = NOT_GIVEN,
        cameo_base_code: str | NotGiven = NOT_GIVEN,
        cameo_code: str | NotGiven = NOT_GIVEN,
        cameo_root_code: str | NotGiven = NOT_GIVEN,
        checksum_value: str | NotGiven = NOT_GIVEN,
        city: str | NotGiven = NOT_GIVEN,
        civ_abd: int | NotGiven = NOT_GIVEN,
        civ_det: int | NotGiven = NOT_GIVEN,
        civ_kia: int | NotGiven = NOT_GIVEN,
        civ_wound: int | NotGiven = NOT_GIVEN,
        clarity: int | NotGiven = NOT_GIVEN,
        coal_abd: int | NotGiven = NOT_GIVEN,
        coal_det: int | NotGiven = NOT_GIVEN,
        coal_kia: int | NotGiven = NOT_GIVEN,
        coal_wound: int | NotGiven = NOT_GIVEN,
        complex_attack: bool | NotGiven = NOT_GIVEN,
        confidence: int | NotGiven = NOT_GIVEN,
        country_code: str | NotGiven = NOT_GIVEN,
        created_at: Union[str, datetime] | NotGiven = NOT_GIVEN,
        created_by: str | NotGiven = NOT_GIVEN,
        district: str | NotGiven = NOT_GIVEN,
        document_filename: str | NotGiven = NOT_GIVEN,
        document_source: str | NotGiven = NOT_GIVEN,
        enemy_abd: int | NotGiven = NOT_GIVEN,
        enemy_det: int | NotGiven = NOT_GIVEN,
        enemy_kia: int | NotGiven = NOT_GIVEN,
        event_description: str | NotGiven = NOT_GIVEN,
        event_end: Union[str, datetime] | NotGiven = NOT_GIVEN,
        event_start: Union[str, datetime] | NotGiven = NOT_GIVEN,
        event_type: str | NotGiven = NOT_GIVEN,
        filesize: int | NotGiven = NOT_GIVEN,
        friendly_abd: int | NotGiven = NOT_GIVEN,
        friendly_det: int | NotGiven = NOT_GIVEN,
        friendly_kia: int | NotGiven = NOT_GIVEN,
        friendly_wound: int | NotGiven = NOT_GIVEN,
        goldstein: float | NotGiven = NOT_GIVEN,
        has_attachment: bool | NotGiven = NOT_GIVEN,
        host_nat_abd: int | NotGiven = NOT_GIVEN,
        host_nat_det: int | NotGiven = NOT_GIVEN,
        host_nat_kia: int | NotGiven = NOT_GIVEN,
        host_nat_wound: int | NotGiven = NOT_GIVEN,
        id_number: str | NotGiven = NOT_GIVEN,
        lat: float | NotGiven = NOT_GIVEN,
        lon: float | NotGiven = NOT_GIVEN,
        milgrid: str | NotGiven = NOT_GIVEN,
        notes: str | NotGiven = NOT_GIVEN,
        num_articles: int | NotGiven = NOT_GIVEN,
        num_mentions: int | NotGiven = NOT_GIVEN,
        num_sources: int | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        orig_network: str | NotGiven = NOT_GIVEN,
        province: str | NotGiven = NOT_GIVEN,
        related_docs: Iterable[udl_sigact_text_create_params.RelatedDoc] | NotGiven = NOT_GIVEN,
        rep_unit: str | NotGiven = NOT_GIVEN,
        rep_unit_activity: str | NotGiven = NOT_GIVEN,
        rep_unit_type: str | NotGiven = NOT_GIVEN,
        side_a_abd: int | NotGiven = NOT_GIVEN,
        side_a_det: int | NotGiven = NOT_GIVEN,
        side_akia: int | NotGiven = NOT_GIVEN,
        side_a_wound: int | NotGiven = NOT_GIVEN,
        side_b_abd: int | NotGiven = NOT_GIVEN,
        side_b_det: int | NotGiven = NOT_GIVEN,
        side_bkia: int | NotGiven = NOT_GIVEN,
        side_b_wound: int | NotGiven = NOT_GIVEN,
        source_language: str | NotGiven = NOT_GIVEN,
        source_url: str | NotGiven = NOT_GIVEN,
        summary: str | NotGiven = NOT_GIVEN,
        target: str | NotGiven = NOT_GIVEN,
        theater: str | NotGiven = NOT_GIVEN,
        type_of_attack: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        The sigact-txt service allows for contribution of large text that exceeds the
        limits of the sigact.eventDescription field (4096 characters). This service
        operation requires a zip file in the body of the POST request. The zip file must
        contain exactly two files. <h3> 1) A json file with any file name that ends in
        .json e.g. MyDataFile.json. The contents of the json file must be valid
        according to the schema for sigact. 2) A txt file of the text encoded in UTF-8.
        </h3> The sigact metadata and text file will be stored and associated with each
        other allowing queries of the data retrieval of the text. This operation is
        intended to be used for automated feeds into UDL. A specific role is required to
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

          report_date: Date of the report or filing.

          source: Source of the data.

          id: Unique identifier of the record, auto-generated by the system.

          accuracy: Estimate of the accuracy that this event occurred as described/reported.

          actors: A list of one or more actors involved in the event.

          agjson: Geographical region or polygon (lat/lon pairs), as depicted by the GeoJSON
              representation of the geometry/geography, of the image as projected on the
              ground. GeoJSON Reference: https://geojson.org/. Ignored if included with a POST
              or PUT request that also specifies a valid 'area' or 'atext' field.

          andims: Number of dimensions of the geometry depicted by region.

          area: Optional geographical region or polygon (lat/lon pairs) of the area surrounding
              the point of interest as projected on the ground.

          asrid: Geographical spatial_ref_sys for region.

          atext: Geographical region or polygon (lon/lat pairs), as depicted by the Well-Known
              Text representation of the geometry/geography, of the image as projected on the
              ground. WKT reference: https://www.opengeospatial.org/standards/wkt-crs. Ignored
              if included with a POST or PUT request that also specifies a valid 'area' field.

          atype: Type of region as projected on the ground.

          avg_tone: This is the average tone of all documents containing one or more mentions of
              this event during the 15 minute update in which it was first seen. The score
              ranges from -100 (extremely negative) to +100 (extremely positive). Common
              values range between -10 and +10, with 0 indicating neutral.

          cameo_base_code: CAMEO event codes are defined in a three-level taxonomy. For events at level
              three in the taxonomy, this yields its level two leaf root node. For example,
              code 0251 (Appeal for easing of administrative sanctions) would yield an
              EventBaseCode of 025 (Appeal to yield). This makes it possible to aggregate
              events at various resolutions of specificity. For events at levels two or one,
              this field will be set to EventCode.

          cameo_code: This is the raw CAMEO action code describing the action that Actor1 performed
              upon Actor2. Additional information about Cameo Codes can be obtained from the
              GDELT project documentation here:
              https://www.gdeltproject.org/data.html#documentation.

          cameo_root_code: Similar to EventBaseCode, this defines the root-level category the event code
              falls under. For example, code 0251 (Appeal for easing of administrative
              sanctions) has a root code of 02 (Appeal). This makes it possible to aggregate
              events at various resolutions of specificity. For events at levels two or one,
              this field will be set to EventCode.

          checksum_value: MD5 value of the file. The ingest/create operation will automatically generate
              the value.

          city: The city in or near which this event occurred.

          civ_abd: Number of civilians abducted in the activity.

          civ_det: Number of civilians detained in the activity.

          civ_kia: Number of civilians killed in the activity.

          civ_wound: Number of civilians wounded in the activity.

          clarity: 1 (high) for events where the reporting allows the coder to identify the event
              in full. That is, events where the individual happening is described by the
              original source in a sufficiently detailed way as to identify individual
              incidents, i.e. separate activities of fighting in a single location:

              2 (lower) for events where an aggregation of information was already made by the
              source material that is impossible to undo in the coding process. Such events
              are described by the original source only as aggregates (totals) of multiple
              separate activities of fighting spanning over a longer period than a single,
              clearly defined day.

          coal_abd: Number of coalition members abducted in the activity.

          coal_det: Number of coalition members detained in the activity.

          coal_kia: Number of coalition members killed in the activity.

          coal_wound: Number of coalition members wounded in the activity.

          complex_attack: Flag indicating that this attack was of a complex or coordinated nature.

          confidence: Estimate of the confidence that this event occurred.

          country_code: The country code. This value is typically the ISO 3166 Alpha-2 two-character
              country code, however it can also represent various consortiums that do not
              appear in the ISO document. The code must correspond to an existing country in
              the UDL�s country API. Call udl/country/{code} to get any associated FIPS code,
              ISO Alpha-3 code, or alternate code values that exist for the specified country
              code.

          created_at: Time the row was created in the database, auto-populated by the system, example
              = 2018-01-01T16:00:00.123Z.

          created_by: Application user who created the row in the database, auto-populated by the
              system.

          district: The district in which this event occurred.

          document_filename: The filename of the document or report.

          document_source: The source of the document or report.

          enemy_abd: Number of enemy combatants abducted in the activity.

          enemy_det: Number of enemy combatants detained in the activity.

          enemy_kia: Number of enemy combatants killed in the activity.

          event_description: A description of the event.

          event_end: The approximate end time of the event, in ISO 8601 UTC format.

          event_start: The approximate start time of the event, in ISO 8601 UTC format.

          event_type: The type of event (e.g. Military, Natural, Political, Social, etc.).

          filesize: Size of the associated text file. Units in bytes. If filesize is provided
              without an associated file, it defaults to 0.

          friendly_abd: Number of friendlies abducted in the activity.

          friendly_det: Number of friendlies in the activity.

          friendly_kia: Number of friendlies killed in the activity.

          friendly_wound: Number of friendlies wounded in the activity.

          goldstein: Each CAMEO event code is assigned a numeric score from -10 to +10, capturing the
              theoretical potential impact that type of event will have on the stability of a
              country. This is known as the Goldstein Scale. NOTE: this score is based on the
              type of event, not the specifics of the actual event record being recorded thus
              two riots, one with 10 people and one with 10,000, will both receive the same
              Goldstein score. This can be aggregated to various levels of time resolution to
              yield an approximation of the stability of a location over time.

          has_attachment: Flag indicating this SigAct record has an associated txt file stored in the UDL.
              Retrieve the txt file by using the GET/udl/sigact/getFile/{id} where id is the
              same as the SigAct record id. The maximum file size for this service is
              10,000,000 bytes (10MB). Files exceeding the maximum size will be rejected.

          host_nat_abd: Number of Host Nation members abducted in the activity.

          host_nat_det: Number of Host Nation members detained in the activity.

          host_nat_kia: Number of Host Nation members killed in the activity.

          host_nat_wound: Number of Host Nation members wounded in the activity.

          id_number: Unique identifier assigned to each event record that uniquely identifies it in
              the master dataset. This ID is provided for convenience of mapping to external
              systems.

          lat: WGS-84 centroid latitude of the event location, in degrees. -90 to 90 degrees
              (negative values south of equator).

          lon: WGS-84 centroid longitude of the event location, in degrees. -180 to 180 degrees
              (negative values west of Prime Meridian).

          milgrid: The Military Grid Reference System is the geocoordinate standard used by NATO
              militaries for locating points on Earth. The MGRS is derived from the Universal
              Transverse Mercator (UTM) grid system and the Universal Polar Stereographic
              (UPS) grid system, but uses a different labeling convention. The MGRS is used as
              geocode for the entire Earth. Example of an milgrid coordinate, or grid
              reference, would be 4QFJ12345678, which consists of three parts:

              &nbsp;&nbsp;4Q (grid zone designator, GZD)

              &nbsp;&nbsp;FJ (the 100,000-meter square identifier)

              &nbsp;&nbsp;12345678 (numerical location; easting is 1234 and northing is 5678,
              in this case specifying a location with 10 m resolution).

          notes: Notes related to the documents or event.

          num_articles: This is the total number of source documents containing one or more mentions of
              this event during the 15 minute update in which it was first seen. This can be
              used as a method of assessing the importance of an event: the more discussion of
              that event, the more likely it is to be significant.

          num_mentions: This is the total number of mentions of this event across all source documents
              during the 15 minute update in which it was first seen. Multiple references to
              an event within a single document also contribute to this count. This can be
              used as a method of assessing the importance of an event: the more discussion of
              that event, the more likely it is to be significant.

          num_sources: This is the total number of information sources containing one or more mentions
              of this event during the 15 minute update in which it was first seen. This can
              be used as a method of assessing the importance of an event: the more discussion
              of that event, the more likely it is to be significant.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          orig_network: The originating source network on which this record was created, auto-populated
              by the system.

          province: The province in which this event occurred.

          related_docs: Related document ids.

          rep_unit: The reporting unit.

          rep_unit_activity: The activity the unit was engaged in.

          rep_unit_type: The reporting unit type.

          side_a_abd: Number of side A members abducted in the activity.

          side_a_det: Number of side A members detained in the activity.

          side_akia: Number of side A members killed in the activity.

          side_a_wound: Number of side A members wounded in the activity.

          side_b_abd: Number of side B members abducted in the activity.

          side_b_det: Number of side B members detained in the activity.

          side_bkia: Number of side B members killed in the activity.

          side_b_wound: Number of side B members wounded in the activity.

          source_language: The source language of the significant event using the ISO 639-3, 3 character
              code definition.

          source_url: This field records the URL or citation of the first news report it found this
              event in. In most cases this is the first report it saw the article in, but due
              to the timing and flow of news reports through the processing pipeline, this may
              not always be the very first report, but is at least in the first few reports.

          summary: A summary of the event.

          target: The name of the target. The target may be an individual, an entity, or a
              country/region.

          theater: Area in which important military events occur or are progressing. A theater can
              include the entirety of the airspace, land and sea area that is or that may
              potentially become involved in war operations.

          type_of_attack: The mode of this attack or event (e.g. Direct Fire, IED Explosion, etc.).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/filedrop/udl-sigact-text",
            body=await async_maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "report_date": report_date,
                    "source": source,
                    "id": id,
                    "accuracy": accuracy,
                    "actors": actors,
                    "agjson": agjson,
                    "andims": andims,
                    "area": area,
                    "asrid": asrid,
                    "atext": atext,
                    "atype": atype,
                    "avg_tone": avg_tone,
                    "cameo_base_code": cameo_base_code,
                    "cameo_code": cameo_code,
                    "cameo_root_code": cameo_root_code,
                    "checksum_value": checksum_value,
                    "city": city,
                    "civ_abd": civ_abd,
                    "civ_det": civ_det,
                    "civ_kia": civ_kia,
                    "civ_wound": civ_wound,
                    "clarity": clarity,
                    "coal_abd": coal_abd,
                    "coal_det": coal_det,
                    "coal_kia": coal_kia,
                    "coal_wound": coal_wound,
                    "complex_attack": complex_attack,
                    "confidence": confidence,
                    "country_code": country_code,
                    "created_at": created_at,
                    "created_by": created_by,
                    "district": district,
                    "document_filename": document_filename,
                    "document_source": document_source,
                    "enemy_abd": enemy_abd,
                    "enemy_det": enemy_det,
                    "enemy_kia": enemy_kia,
                    "event_description": event_description,
                    "event_end": event_end,
                    "event_start": event_start,
                    "event_type": event_type,
                    "filesize": filesize,
                    "friendly_abd": friendly_abd,
                    "friendly_det": friendly_det,
                    "friendly_kia": friendly_kia,
                    "friendly_wound": friendly_wound,
                    "goldstein": goldstein,
                    "has_attachment": has_attachment,
                    "host_nat_abd": host_nat_abd,
                    "host_nat_det": host_nat_det,
                    "host_nat_kia": host_nat_kia,
                    "host_nat_wound": host_nat_wound,
                    "id_number": id_number,
                    "lat": lat,
                    "lon": lon,
                    "milgrid": milgrid,
                    "notes": notes,
                    "num_articles": num_articles,
                    "num_mentions": num_mentions,
                    "num_sources": num_sources,
                    "origin": origin,
                    "orig_network": orig_network,
                    "province": province,
                    "related_docs": related_docs,
                    "rep_unit": rep_unit,
                    "rep_unit_activity": rep_unit_activity,
                    "rep_unit_type": rep_unit_type,
                    "side_a_abd": side_a_abd,
                    "side_a_det": side_a_det,
                    "side_akia": side_akia,
                    "side_a_wound": side_a_wound,
                    "side_b_abd": side_b_abd,
                    "side_b_det": side_b_det,
                    "side_bkia": side_bkia,
                    "side_b_wound": side_b_wound,
                    "source_language": source_language,
                    "source_url": source_url,
                    "summary": summary,
                    "target": target,
                    "theater": theater,
                    "type_of_attack": type_of_attack,
                },
                udl_sigact_text_create_params.UdlSigactTextCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class UdlSigactTextResourceWithRawResponse:
    def __init__(self, udl_sigact_text: UdlSigactTextResource) -> None:
        self._udl_sigact_text = udl_sigact_text

        self.create = to_raw_response_wrapper(
            udl_sigact_text.create,
        )


class AsyncUdlSigactTextResourceWithRawResponse:
    def __init__(self, udl_sigact_text: AsyncUdlSigactTextResource) -> None:
        self._udl_sigact_text = udl_sigact_text

        self.create = async_to_raw_response_wrapper(
            udl_sigact_text.create,
        )


class UdlSigactTextResourceWithStreamingResponse:
    def __init__(self, udl_sigact_text: UdlSigactTextResource) -> None:
        self._udl_sigact_text = udl_sigact_text

        self.create = to_streamed_response_wrapper(
            udl_sigact_text.create,
        )


class AsyncUdlSigactTextResourceWithStreamingResponse:
    def __init__(self, udl_sigact_text: AsyncUdlSigactTextResource) -> None:
        self._udl_sigact_text = udl_sigact_text

        self.create = async_to_streamed_response_wrapper(
            udl_sigact_text.create,
        )
