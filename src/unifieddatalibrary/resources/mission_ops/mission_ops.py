# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .effect_requests import (
    EffectRequestsResource,
    AsyncEffectRequestsResource,
    EffectRequestsResourceWithRawResponse,
    AsyncEffectRequestsResourceWithRawResponse,
    EffectRequestsResourceWithStreamingResponse,
    AsyncEffectRequestsResourceWithStreamingResponse,
)
from .personnelrecovery.personnelrecovery import (
    PersonnelrecoveryResource,
    AsyncPersonnelrecoveryResource,
    PersonnelrecoveryResourceWithRawResponse,
    AsyncPersonnelrecoveryResourceWithRawResponse,
    PersonnelrecoveryResourceWithStreamingResponse,
    AsyncPersonnelrecoveryResourceWithStreamingResponse,
)

__all__ = ["MissionOpsResource", "AsyncMissionOpsResource"]


class MissionOpsResource(SyncAPIResource):
    @cached_property
    def effect_requests(self) -> EffectRequestsResource:
        return EffectRequestsResource(self._client)

    @cached_property
    def personnelrecovery(self) -> PersonnelrecoveryResource:
        return PersonnelrecoveryResource(self._client)

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
    def effect_requests(self) -> AsyncEffectRequestsResource:
        return AsyncEffectRequestsResource(self._client)

    @cached_property
    def personnelrecovery(self) -> AsyncPersonnelrecoveryResource:
        return AsyncPersonnelrecoveryResource(self._client)

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
    def effect_requests(self) -> EffectRequestsResourceWithRawResponse:
        return EffectRequestsResourceWithRawResponse(self._mission_ops.effect_requests)

    @cached_property
    def personnelrecovery(self) -> PersonnelrecoveryResourceWithRawResponse:
        return PersonnelrecoveryResourceWithRawResponse(self._mission_ops.personnelrecovery)


class AsyncMissionOpsResourceWithRawResponse:
    def __init__(self, mission_ops: AsyncMissionOpsResource) -> None:
        self._mission_ops = mission_ops

    @cached_property
    def effect_requests(self) -> AsyncEffectRequestsResourceWithRawResponse:
        return AsyncEffectRequestsResourceWithRawResponse(self._mission_ops.effect_requests)

    @cached_property
    def personnelrecovery(self) -> AsyncPersonnelrecoveryResourceWithRawResponse:
        return AsyncPersonnelrecoveryResourceWithRawResponse(self._mission_ops.personnelrecovery)


class MissionOpsResourceWithStreamingResponse:
    def __init__(self, mission_ops: MissionOpsResource) -> None:
        self._mission_ops = mission_ops

    @cached_property
    def effect_requests(self) -> EffectRequestsResourceWithStreamingResponse:
        return EffectRequestsResourceWithStreamingResponse(self._mission_ops.effect_requests)

    @cached_property
    def personnelrecovery(self) -> PersonnelrecoveryResourceWithStreamingResponse:
        return PersonnelrecoveryResourceWithStreamingResponse(self._mission_ops.personnelrecovery)


class AsyncMissionOpsResourceWithStreamingResponse:
    def __init__(self, mission_ops: AsyncMissionOpsResource) -> None:
        self._mission_ops = mission_ops

    @cached_property
    def effect_requests(self) -> AsyncEffectRequestsResourceWithStreamingResponse:
        return AsyncEffectRequestsResourceWithStreamingResponse(self._mission_ops.effect_requests)

    @cached_property
    def personnelrecovery(self) -> AsyncPersonnelrecoveryResourceWithStreamingResponse:
        return AsyncPersonnelrecoveryResourceWithStreamingResponse(self._mission_ops.personnelrecovery)
