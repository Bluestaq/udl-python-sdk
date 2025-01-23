# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import udl_skyimagery_create_params
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

__all__ = ["UdlSkyimageryResource", "AsyncUdlSkyimageryResource"]


class UdlSkyimageryResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UdlSkyimageryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/unifieddatalibrary-python#accessing-raw-response-data-eg-headers
        """
        return UdlSkyimageryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UdlSkyimageryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/unifieddatalibrary-python#with_streaming_response
        """
        return UdlSkyimageryResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        exp_start_time: Union[str, datetime],
        image_type: str,
        source: str,
        id: str | NotGiven = NOT_GIVEN,
        annotation_key: str | NotGiven = NOT_GIVEN,
        calibration_key: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        eo_observations: Iterable[udl_skyimagery_create_params.EoObservation] | NotGiven = NOT_GIVEN,
        exp_end_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        filename: str | NotGiven = NOT_GIVEN,
        filesize: int | NotGiven = NOT_GIVEN,
        frame_fov_height: float | NotGiven = NOT_GIVEN,
        frame_fov_width: float | NotGiven = NOT_GIVEN,
        frame_height_pixels: int | NotGiven = NOT_GIVEN,
        frame_width_pixels: int | NotGiven = NOT_GIVEN,
        id_attitude_set: str | NotGiven = NOT_GIVEN,
        id_sensor: str | NotGiven = NOT_GIVEN,
        id_soi_set: str | NotGiven = NOT_GIVEN,
        image_set_id: str | NotGiven = NOT_GIVEN,
        image_set_length: int | NotGiven = NOT_GIVEN,
        image_source_info: str | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        orig_object_id: str | NotGiven = NOT_GIVEN,
        orig_sensor_id: str | NotGiven = NOT_GIVEN,
        pixel_bit_depth: int | NotGiven = NOT_GIVEN,
        pixel_fov_height: float | NotGiven = NOT_GIVEN,
        pixel_fov_width: float | NotGiven = NOT_GIVEN,
        sat_no: int | NotGiven = NOT_GIVEN,
        senalt: float | NotGiven = NOT_GIVEN,
        senlat: float | NotGiven = NOT_GIVEN,
        senlon: float | NotGiven = NOT_GIVEN,
        sen_quat: Iterable[float] | NotGiven = NOT_GIVEN,
        sen_quat_dot: Iterable[float] | NotGiven = NOT_GIVEN,
        senx: float | NotGiven = NOT_GIVEN,
        seny: float | NotGiven = NOT_GIVEN,
        senz: float | NotGiven = NOT_GIVEN,
        sequence_id: int | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        top_left_start_az: float | NotGiven = NOT_GIVEN,
        top_left_start_el: float | NotGiven = NOT_GIVEN,
        top_left_stop_az: float | NotGiven = NOT_GIVEN,
        top_left_stop_el: float | NotGiven = NOT_GIVEN,
        transaction_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """This service operation requires a zip file in the body of the POST request.

        The
        zip file must contains exactly two files. 1) A json file with any file name that
        ends in .json e.g. MyFitsFile.json The contents of the json file must be valid
        according to the schema for SkyImagery. 2) A binary image file. This can be png,
        jpeg or fits/eossa file. e.g. MyFitsFile.fits. The metadata and image files will
        be stored and associated with each other allowing queries of the data retrieval
        of the binary images. This operation is intended to be used for automated feeds
        into UDL. A specific role is required to perform this service operation. Please
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

          exp_start_time: Start time of the exposure, in ISO 8601 UTC format with microsecond precision.

          image_type: The type of image associated with this record (e.g. FITS, EOSSA, EOCHIP).

          source: Source of the data.

          id: Unique identifier of the record, auto-generated by the system.

          annotation_key: Reference to an annotation document associated with this image.

          calibration_key: Reference to a calibration document associated with this image.

          description: Optional name/description associated with this image.

          eo_observations: Collection of linked EOObservations.

          exp_end_time: End time of the exposure, in ISO 8601 UTC format with microsecond precision.

          filename: Name of the uploaded image file.

          filesize: Size of the image file, in bytes.

          frame_fov_height: Field Of View frame height, in degrees.

          frame_fov_width: Field Of View frame width, in degrees.

          frame_height_pixels: Frame height of the image, in number of pixels.

          frame_width_pixels: Frame width of the image, in number of pixels.

          id_attitude_set: Optional identifier of the AttitudeSet data record describing the orientation of
              an object body.

          id_sensor: Unique identifier of the reporting sensor.

          id_soi_set: Optional unique identifier of the SOI Observation Set associated with this
              image.

          image_set_id: The user-defined set ID of a sequence of images.

          image_set_length: The number of images in an image set.

          image_source_info: String that uniquely identifies the data source.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          orig_object_id: Optional identifier provided by the imaging source to indicate the target
              onorbit object of this image. This may be an internal identifier and not
              necessarily a valid satellite number.

          orig_sensor_id: Optional identifier provided by the imaging source to indicate the sensor
              identifier which produced this image. This may be an internal identifier and not
              necessarily a valid sensor ID.

          pixel_bit_depth: Bit depth of the image, in number of pixels.

          pixel_fov_height: Field Of View pixel height, in degrees.

          pixel_fov_width: Field Of View pixel width, in degrees.

          sat_no: Catalog number of the target on-orbit object.

          senalt: Sensor altitude at exposure start epoch, in km. If null, can be obtained from
              sensor info.

          senlat: Sensor latitude at exposure start epoch, in degrees. If null, can be obtained
              from sensor info. -90 to 90 degrees (negative values south of equator).

          senlon: Sensor longitude at exposure start epoch, in degrees. If null, can be obtained
              from sensor info. -180 to 180 degrees (negative values west of Prime Meridian).

          sen_quat: The quaternion describing the rotation of the body-fixed frame used for this
              system into the local geodetic frame, at exposure start epoch (expStartTime).
              The array element order convention is scalar component first, followed by the
              three vector components. For a vector u in the body-fixed frame, the
              corresponding vector u' in the geodetic frame should satisfy u' = quq\\**, where q
              is this quaternion.

          sen_quat_dot: The derivative of the quaternion describing the rotation of the body-fixed frame
              used for this system into the local geodetic frame, exposure start epoch
              (expStartTime). The array element order convention is scalar component first,
              followed by the three vector components. For a vector u in the body-fixed frame,
              the corresponding vector u' in the geodetic frame should satisfy u' = quq\\**,
              where q is this quaternion.

          senx: Sensor x position at exposure start epoch, in km (if mobile/onorbit) in J2000
              coordinate frame.

          seny: Sensor y position at exposure start epoch, in km (if mobile/onorbit) in J2000
              coordinate frame.

          senz: Sensor z position at exposure start epoch, in km (if mobile/onorbit) in J2000
              coordinate frame.

          sequence_id: The sequence ID of an image within an image set.

          tags: Optional array of provider/source specific tags for this data, where each
              element is no longer than 32 characters, used for implementing data owner
              conditional access controls to restrict access to the data. Should be left null
              by data providers unless conditional access controls are coordinated with the
              UDL team.

          top_left_start_az: The telescope pointing azimuth, in degrees, at the exposure start epoch.

          top_left_start_el: The telescope pointing elevation, in degrees, at the exposure start epoch.

          top_left_stop_az: The telescope pointing azimuth, in degrees, at the exposure stop epoch.

          top_left_stop_el: The telescope pointing elevation, in degrees, at the exposure stop epoch.

          transaction_id: Optional identifier to track a commercial or marketplace transaction executed to
              produce this data.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/filedrop/udl-skyimagery",
            body=maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "exp_start_time": exp_start_time,
                    "image_type": image_type,
                    "source": source,
                    "id": id,
                    "annotation_key": annotation_key,
                    "calibration_key": calibration_key,
                    "description": description,
                    "eo_observations": eo_observations,
                    "exp_end_time": exp_end_time,
                    "filename": filename,
                    "filesize": filesize,
                    "frame_fov_height": frame_fov_height,
                    "frame_fov_width": frame_fov_width,
                    "frame_height_pixels": frame_height_pixels,
                    "frame_width_pixels": frame_width_pixels,
                    "id_attitude_set": id_attitude_set,
                    "id_sensor": id_sensor,
                    "id_soi_set": id_soi_set,
                    "image_set_id": image_set_id,
                    "image_set_length": image_set_length,
                    "image_source_info": image_source_info,
                    "origin": origin,
                    "orig_object_id": orig_object_id,
                    "orig_sensor_id": orig_sensor_id,
                    "pixel_bit_depth": pixel_bit_depth,
                    "pixel_fov_height": pixel_fov_height,
                    "pixel_fov_width": pixel_fov_width,
                    "sat_no": sat_no,
                    "senalt": senalt,
                    "senlat": senlat,
                    "senlon": senlon,
                    "sen_quat": sen_quat,
                    "sen_quat_dot": sen_quat_dot,
                    "senx": senx,
                    "seny": seny,
                    "senz": senz,
                    "sequence_id": sequence_id,
                    "tags": tags,
                    "top_left_start_az": top_left_start_az,
                    "top_left_start_el": top_left_start_el,
                    "top_left_stop_az": top_left_stop_az,
                    "top_left_stop_el": top_left_stop_el,
                    "transaction_id": transaction_id,
                },
                udl_skyimagery_create_params.UdlSkyimageryCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncUdlSkyimageryResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUdlSkyimageryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/unifieddatalibrary-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUdlSkyimageryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUdlSkyimageryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/unifieddatalibrary-python#with_streaming_response
        """
        return AsyncUdlSkyimageryResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        exp_start_time: Union[str, datetime],
        image_type: str,
        source: str,
        id: str | NotGiven = NOT_GIVEN,
        annotation_key: str | NotGiven = NOT_GIVEN,
        calibration_key: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        eo_observations: Iterable[udl_skyimagery_create_params.EoObservation] | NotGiven = NOT_GIVEN,
        exp_end_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        filename: str | NotGiven = NOT_GIVEN,
        filesize: int | NotGiven = NOT_GIVEN,
        frame_fov_height: float | NotGiven = NOT_GIVEN,
        frame_fov_width: float | NotGiven = NOT_GIVEN,
        frame_height_pixels: int | NotGiven = NOT_GIVEN,
        frame_width_pixels: int | NotGiven = NOT_GIVEN,
        id_attitude_set: str | NotGiven = NOT_GIVEN,
        id_sensor: str | NotGiven = NOT_GIVEN,
        id_soi_set: str | NotGiven = NOT_GIVEN,
        image_set_id: str | NotGiven = NOT_GIVEN,
        image_set_length: int | NotGiven = NOT_GIVEN,
        image_source_info: str | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        orig_object_id: str | NotGiven = NOT_GIVEN,
        orig_sensor_id: str | NotGiven = NOT_GIVEN,
        pixel_bit_depth: int | NotGiven = NOT_GIVEN,
        pixel_fov_height: float | NotGiven = NOT_GIVEN,
        pixel_fov_width: float | NotGiven = NOT_GIVEN,
        sat_no: int | NotGiven = NOT_GIVEN,
        senalt: float | NotGiven = NOT_GIVEN,
        senlat: float | NotGiven = NOT_GIVEN,
        senlon: float | NotGiven = NOT_GIVEN,
        sen_quat: Iterable[float] | NotGiven = NOT_GIVEN,
        sen_quat_dot: Iterable[float] | NotGiven = NOT_GIVEN,
        senx: float | NotGiven = NOT_GIVEN,
        seny: float | NotGiven = NOT_GIVEN,
        senz: float | NotGiven = NOT_GIVEN,
        sequence_id: int | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        top_left_start_az: float | NotGiven = NOT_GIVEN,
        top_left_start_el: float | NotGiven = NOT_GIVEN,
        top_left_stop_az: float | NotGiven = NOT_GIVEN,
        top_left_stop_el: float | NotGiven = NOT_GIVEN,
        transaction_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """This service operation requires a zip file in the body of the POST request.

        The
        zip file must contains exactly two files. 1) A json file with any file name that
        ends in .json e.g. MyFitsFile.json The contents of the json file must be valid
        according to the schema for SkyImagery. 2) A binary image file. This can be png,
        jpeg or fits/eossa file. e.g. MyFitsFile.fits. The metadata and image files will
        be stored and associated with each other allowing queries of the data retrieval
        of the binary images. This operation is intended to be used for automated feeds
        into UDL. A specific role is required to perform this service operation. Please
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

          exp_start_time: Start time of the exposure, in ISO 8601 UTC format with microsecond precision.

          image_type: The type of image associated with this record (e.g. FITS, EOSSA, EOCHIP).

          source: Source of the data.

          id: Unique identifier of the record, auto-generated by the system.

          annotation_key: Reference to an annotation document associated with this image.

          calibration_key: Reference to a calibration document associated with this image.

          description: Optional name/description associated with this image.

          eo_observations: Collection of linked EOObservations.

          exp_end_time: End time of the exposure, in ISO 8601 UTC format with microsecond precision.

          filename: Name of the uploaded image file.

          filesize: Size of the image file, in bytes.

          frame_fov_height: Field Of View frame height, in degrees.

          frame_fov_width: Field Of View frame width, in degrees.

          frame_height_pixels: Frame height of the image, in number of pixels.

          frame_width_pixels: Frame width of the image, in number of pixels.

          id_attitude_set: Optional identifier of the AttitudeSet data record describing the orientation of
              an object body.

          id_sensor: Unique identifier of the reporting sensor.

          id_soi_set: Optional unique identifier of the SOI Observation Set associated with this
              image.

          image_set_id: The user-defined set ID of a sequence of images.

          image_set_length: The number of images in an image set.

          image_source_info: String that uniquely identifies the data source.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          orig_object_id: Optional identifier provided by the imaging source to indicate the target
              onorbit object of this image. This may be an internal identifier and not
              necessarily a valid satellite number.

          orig_sensor_id: Optional identifier provided by the imaging source to indicate the sensor
              identifier which produced this image. This may be an internal identifier and not
              necessarily a valid sensor ID.

          pixel_bit_depth: Bit depth of the image, in number of pixels.

          pixel_fov_height: Field Of View pixel height, in degrees.

          pixel_fov_width: Field Of View pixel width, in degrees.

          sat_no: Catalog number of the target on-orbit object.

          senalt: Sensor altitude at exposure start epoch, in km. If null, can be obtained from
              sensor info.

          senlat: Sensor latitude at exposure start epoch, in degrees. If null, can be obtained
              from sensor info. -90 to 90 degrees (negative values south of equator).

          senlon: Sensor longitude at exposure start epoch, in degrees. If null, can be obtained
              from sensor info. -180 to 180 degrees (negative values west of Prime Meridian).

          sen_quat: The quaternion describing the rotation of the body-fixed frame used for this
              system into the local geodetic frame, at exposure start epoch (expStartTime).
              The array element order convention is scalar component first, followed by the
              three vector components. For a vector u in the body-fixed frame, the
              corresponding vector u' in the geodetic frame should satisfy u' = quq\\**, where q
              is this quaternion.

          sen_quat_dot: The derivative of the quaternion describing the rotation of the body-fixed frame
              used for this system into the local geodetic frame, exposure start epoch
              (expStartTime). The array element order convention is scalar component first,
              followed by the three vector components. For a vector u in the body-fixed frame,
              the corresponding vector u' in the geodetic frame should satisfy u' = quq\\**,
              where q is this quaternion.

          senx: Sensor x position at exposure start epoch, in km (if mobile/onorbit) in J2000
              coordinate frame.

          seny: Sensor y position at exposure start epoch, in km (if mobile/onorbit) in J2000
              coordinate frame.

          senz: Sensor z position at exposure start epoch, in km (if mobile/onorbit) in J2000
              coordinate frame.

          sequence_id: The sequence ID of an image within an image set.

          tags: Optional array of provider/source specific tags for this data, where each
              element is no longer than 32 characters, used for implementing data owner
              conditional access controls to restrict access to the data. Should be left null
              by data providers unless conditional access controls are coordinated with the
              UDL team.

          top_left_start_az: The telescope pointing azimuth, in degrees, at the exposure start epoch.

          top_left_start_el: The telescope pointing elevation, in degrees, at the exposure start epoch.

          top_left_stop_az: The telescope pointing azimuth, in degrees, at the exposure stop epoch.

          top_left_stop_el: The telescope pointing elevation, in degrees, at the exposure stop epoch.

          transaction_id: Optional identifier to track a commercial or marketplace transaction executed to
              produce this data.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/filedrop/udl-skyimagery",
            body=await async_maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "exp_start_time": exp_start_time,
                    "image_type": image_type,
                    "source": source,
                    "id": id,
                    "annotation_key": annotation_key,
                    "calibration_key": calibration_key,
                    "description": description,
                    "eo_observations": eo_observations,
                    "exp_end_time": exp_end_time,
                    "filename": filename,
                    "filesize": filesize,
                    "frame_fov_height": frame_fov_height,
                    "frame_fov_width": frame_fov_width,
                    "frame_height_pixels": frame_height_pixels,
                    "frame_width_pixels": frame_width_pixels,
                    "id_attitude_set": id_attitude_set,
                    "id_sensor": id_sensor,
                    "id_soi_set": id_soi_set,
                    "image_set_id": image_set_id,
                    "image_set_length": image_set_length,
                    "image_source_info": image_source_info,
                    "origin": origin,
                    "orig_object_id": orig_object_id,
                    "orig_sensor_id": orig_sensor_id,
                    "pixel_bit_depth": pixel_bit_depth,
                    "pixel_fov_height": pixel_fov_height,
                    "pixel_fov_width": pixel_fov_width,
                    "sat_no": sat_no,
                    "senalt": senalt,
                    "senlat": senlat,
                    "senlon": senlon,
                    "sen_quat": sen_quat,
                    "sen_quat_dot": sen_quat_dot,
                    "senx": senx,
                    "seny": seny,
                    "senz": senz,
                    "sequence_id": sequence_id,
                    "tags": tags,
                    "top_left_start_az": top_left_start_az,
                    "top_left_start_el": top_left_start_el,
                    "top_left_stop_az": top_left_stop_az,
                    "top_left_stop_el": top_left_stop_el,
                    "transaction_id": transaction_id,
                },
                udl_skyimagery_create_params.UdlSkyimageryCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class UdlSkyimageryResourceWithRawResponse:
    def __init__(self, udl_skyimagery: UdlSkyimageryResource) -> None:
        self._udl_skyimagery = udl_skyimagery

        self.create = to_raw_response_wrapper(
            udl_skyimagery.create,
        )


class AsyncUdlSkyimageryResourceWithRawResponse:
    def __init__(self, udl_skyimagery: AsyncUdlSkyimageryResource) -> None:
        self._udl_skyimagery = udl_skyimagery

        self.create = async_to_raw_response_wrapper(
            udl_skyimagery.create,
        )


class UdlSkyimageryResourceWithStreamingResponse:
    def __init__(self, udl_skyimagery: UdlSkyimageryResource) -> None:
        self._udl_skyimagery = udl_skyimagery

        self.create = to_streamed_response_wrapper(
            udl_skyimagery.create,
        )


class AsyncUdlSkyimageryResourceWithStreamingResponse:
    def __init__(self, udl_skyimagery: AsyncUdlSkyimageryResource) -> None:
        self._udl_skyimagery = udl_skyimagery

        self.create = async_to_streamed_response_wrapper(
            udl_skyimagery.create,
        )
