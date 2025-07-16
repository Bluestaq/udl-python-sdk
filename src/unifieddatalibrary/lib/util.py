from datetime import datetime, timezone

from .common import UDL_DATETIME_FORMAT


def sanitize_datetime(val: datetime) -> str:
    """Takes a datetime argument val and returns the same datetime converted to UTC.
    If tzinfo is not set, assumes local time in conversion."""

    if val.tzinfo is None:
        # Assume the input is in the local timezone
        local_tz = datetime.now().astimezone().tzinfo  # Get the local timezone
        val = val.replace(tzinfo=local_tz)

    # Convert to UTC

    tmp = val.astimezone(timezone.utc)
    return tmp.strftime(UDL_DATETIME_FORMAT)
