# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AltitudeBlocksIngestParam"]


class AltitudeBlocksIngestParam(TypedDict, total=False):
    altitude_sequence_id: Annotated[str, PropertyInfo(alias="altitudeSequenceId")]
    """Sequencing field for the altitude block."""

    lower_altitude: Annotated[float, PropertyInfo(alias="lowerAltitude")]
    """Lowest altitude of the track route altitude block above mean sea level in feet."""

    upper_altitude: Annotated[float, PropertyInfo(alias="upperAltitude")]
    """
    Highest altitude of the track route altitude block above mean sea level in feet.
    """
