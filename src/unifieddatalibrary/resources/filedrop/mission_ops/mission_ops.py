# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from .personnel_recovery import (
    PersonnelRecoveryResource,
    AsyncPersonnelRecoveryResource,
    PersonnelRecoveryResourceWithRawResponse,
    AsyncPersonnelRecoveryResourceWithRawResponse,
    PersonnelRecoveryResourceWithStreamingResponse,
    AsyncPersonnelRecoveryResourceWithStreamingResponse,
)

__all__ = ["MissionOpsResource", "AsyncMissionOpsResource"]


class MissionOpsResource(SyncAPIResource):
    @cached_property
    def personnel_recovery(self) -> PersonnelRecoveryResource:
        return PersonnelRecoveryResource(self._client)

    @cached_property
    def with_raw_response(self) -> MissionOpsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/unifieddatalibrary-python#accessing-raw-response-data-eg-headers
        """
        return MissionOpsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MissionOpsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/unifieddatalibrary-python#with_streaming_response
        """
        return MissionOpsResourceWithStreamingResponse(self)


class AsyncMissionOpsResource(AsyncAPIResource):
    @cached_property
    def personnel_recovery(self) -> AsyncPersonnelRecoveryResource:
        return AsyncPersonnelRecoveryResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncMissionOpsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/unifieddatalibrary-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMissionOpsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMissionOpsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/unifieddatalibrary-python#with_streaming_response
        """
        return AsyncMissionOpsResourceWithStreamingResponse(self)


class MissionOpsResourceWithRawResponse:
    def __init__(self, mission_ops: MissionOpsResource) -> None:
        self._mission_ops = mission_ops

    @cached_property
    def personnel_recovery(self) -> PersonnelRecoveryResourceWithRawResponse:
        return PersonnelRecoveryResourceWithRawResponse(self._mission_ops.personnel_recovery)


class AsyncMissionOpsResourceWithRawResponse:
    def __init__(self, mission_ops: AsyncMissionOpsResource) -> None:
        self._mission_ops = mission_ops

    @cached_property
    def personnel_recovery(self) -> AsyncPersonnelRecoveryResourceWithRawResponse:
        return AsyncPersonnelRecoveryResourceWithRawResponse(self._mission_ops.personnel_recovery)


class MissionOpsResourceWithStreamingResponse:
    def __init__(self, mission_ops: MissionOpsResource) -> None:
        self._mission_ops = mission_ops

    @cached_property
    def personnel_recovery(self) -> PersonnelRecoveryResourceWithStreamingResponse:
        return PersonnelRecoveryResourceWithStreamingResponse(self._mission_ops.personnel_recovery)


class AsyncMissionOpsResourceWithStreamingResponse:
    def __init__(self, mission_ops: AsyncMissionOpsResource) -> None:
        self._mission_ops = mission_ops

    @cached_property
    def personnel_recovery(self) -> AsyncPersonnelRecoveryResourceWithStreamingResponse:
        return AsyncPersonnelRecoveryResourceWithStreamingResponse(self._mission_ops.personnel_recovery)
