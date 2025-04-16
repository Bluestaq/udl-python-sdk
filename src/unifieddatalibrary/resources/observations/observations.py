# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .swir import (
    SwirResource,
    AsyncSwirResource,
    SwirResourceWithRawResponse,
    AsyncSwirResourceWithRawResponse,
    SwirResourceWithStreamingResponse,
    AsyncSwirResourceWithStreamingResponse,
)
from .ecpsdr import (
    EcpsdrResource,
    AsyncEcpsdrResource,
    EcpsdrResourceWithRawResponse,
    AsyncEcpsdrResourceWithRawResponse,
    EcpsdrResourceWithStreamingResponse,
    AsyncEcpsdrResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .monoradar.monoradar import (
    MonoradarResource,
    AsyncMonoradarResource,
    MonoradarResourceWithRawResponse,
    AsyncMonoradarResourceWithRawResponse,
    MonoradarResourceWithStreamingResponse,
    AsyncMonoradarResourceWithStreamingResponse,
)
from .rfobservation.rfobservation import (
    RfobservationResource,
    AsyncRfobservationResource,
    RfobservationResourceWithRawResponse,
    AsyncRfobservationResourceWithRawResponse,
    RfobservationResourceWithStreamingResponse,
    AsyncRfobservationResourceWithStreamingResponse,
)
from .radarobservation.radarobservation import (
    RadarobservationResource,
    AsyncRadarobservationResource,
    RadarobservationResourceWithRawResponse,
    AsyncRadarobservationResourceWithRawResponse,
    RadarobservationResourceWithStreamingResponse,
    AsyncRadarobservationResourceWithStreamingResponse,
)

__all__ = ["ObservationsResource", "AsyncObservationsResource"]


class ObservationsResource(SyncAPIResource):
    @cached_property
    def ecpsdr(self) -> EcpsdrResource:
        return EcpsdrResource(self._client)

    @cached_property
    def monoradar(self) -> MonoradarResource:
        return MonoradarResource(self._client)

    @cached_property
    def swir(self) -> SwirResource:
        return SwirResource(self._client)

    @cached_property
    def radarobservation(self) -> RadarobservationResource:
        return RadarobservationResource(self._client)

    @cached_property
    def rfobservation(self) -> RfobservationResource:
        return RfobservationResource(self._client)

    @cached_property
    def with_raw_response(self) -> ObservationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/rsivilli-bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return ObservationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ObservationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/rsivilli-bluestaq/udl-python-sdk#with_streaming_response
        """
        return ObservationsResourceWithStreamingResponse(self)


class AsyncObservationsResource(AsyncAPIResource):
    @cached_property
    def ecpsdr(self) -> AsyncEcpsdrResource:
        return AsyncEcpsdrResource(self._client)

    @cached_property
    def monoradar(self) -> AsyncMonoradarResource:
        return AsyncMonoradarResource(self._client)

    @cached_property
    def swir(self) -> AsyncSwirResource:
        return AsyncSwirResource(self._client)

    @cached_property
    def radarobservation(self) -> AsyncRadarobservationResource:
        return AsyncRadarobservationResource(self._client)

    @cached_property
    def rfobservation(self) -> AsyncRfobservationResource:
        return AsyncRfobservationResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncObservationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/rsivilli-bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncObservationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncObservationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/rsivilli-bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncObservationsResourceWithStreamingResponse(self)


class ObservationsResourceWithRawResponse:
    def __init__(self, observations: ObservationsResource) -> None:
        self._observations = observations

    @cached_property
    def ecpsdr(self) -> EcpsdrResourceWithRawResponse:
        return EcpsdrResourceWithRawResponse(self._observations.ecpsdr)

    @cached_property
    def monoradar(self) -> MonoradarResourceWithRawResponse:
        return MonoradarResourceWithRawResponse(self._observations.monoradar)

    @cached_property
    def swir(self) -> SwirResourceWithRawResponse:
        return SwirResourceWithRawResponse(self._observations.swir)

    @cached_property
    def radarobservation(self) -> RadarobservationResourceWithRawResponse:
        return RadarobservationResourceWithRawResponse(self._observations.radarobservation)

    @cached_property
    def rfobservation(self) -> RfobservationResourceWithRawResponse:
        return RfobservationResourceWithRawResponse(self._observations.rfobservation)


class AsyncObservationsResourceWithRawResponse:
    def __init__(self, observations: AsyncObservationsResource) -> None:
        self._observations = observations

    @cached_property
    def ecpsdr(self) -> AsyncEcpsdrResourceWithRawResponse:
        return AsyncEcpsdrResourceWithRawResponse(self._observations.ecpsdr)

    @cached_property
    def monoradar(self) -> AsyncMonoradarResourceWithRawResponse:
        return AsyncMonoradarResourceWithRawResponse(self._observations.monoradar)

    @cached_property
    def swir(self) -> AsyncSwirResourceWithRawResponse:
        return AsyncSwirResourceWithRawResponse(self._observations.swir)

    @cached_property
    def radarobservation(self) -> AsyncRadarobservationResourceWithRawResponse:
        return AsyncRadarobservationResourceWithRawResponse(self._observations.radarobservation)

    @cached_property
    def rfobservation(self) -> AsyncRfobservationResourceWithRawResponse:
        return AsyncRfobservationResourceWithRawResponse(self._observations.rfobservation)


class ObservationsResourceWithStreamingResponse:
    def __init__(self, observations: ObservationsResource) -> None:
        self._observations = observations

    @cached_property
    def ecpsdr(self) -> EcpsdrResourceWithStreamingResponse:
        return EcpsdrResourceWithStreamingResponse(self._observations.ecpsdr)

    @cached_property
    def monoradar(self) -> MonoradarResourceWithStreamingResponse:
        return MonoradarResourceWithStreamingResponse(self._observations.monoradar)

    @cached_property
    def swir(self) -> SwirResourceWithStreamingResponse:
        return SwirResourceWithStreamingResponse(self._observations.swir)

    @cached_property
    def radarobservation(self) -> RadarobservationResourceWithStreamingResponse:
        return RadarobservationResourceWithStreamingResponse(self._observations.radarobservation)

    @cached_property
    def rfobservation(self) -> RfobservationResourceWithStreamingResponse:
        return RfobservationResourceWithStreamingResponse(self._observations.rfobservation)


class AsyncObservationsResourceWithStreamingResponse:
    def __init__(self, observations: AsyncObservationsResource) -> None:
        self._observations = observations

    @cached_property
    def ecpsdr(self) -> AsyncEcpsdrResourceWithStreamingResponse:
        return AsyncEcpsdrResourceWithStreamingResponse(self._observations.ecpsdr)

    @cached_property
    def monoradar(self) -> AsyncMonoradarResourceWithStreamingResponse:
        return AsyncMonoradarResourceWithStreamingResponse(self._observations.monoradar)

    @cached_property
    def swir(self) -> AsyncSwirResourceWithStreamingResponse:
        return AsyncSwirResourceWithStreamingResponse(self._observations.swir)

    @cached_property
    def radarobservation(self) -> AsyncRadarobservationResourceWithStreamingResponse:
        return AsyncRadarobservationResourceWithStreamingResponse(self._observations.radarobservation)

    @cached_property
    def rfobservation(self) -> AsyncRfobservationResourceWithStreamingResponse:
        return AsyncRfobservationResourceWithStreamingResponse(self._observations.rfobservation)
