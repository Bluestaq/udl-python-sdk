import asyncio
from datetime import datetime, timedelta

from unifieddatalibrary import AsyncUnifieddatalibrary
from unifieddatalibrary.lib.util import sanitize_datetime

client = AsyncUnifieddatalibrary(base_url="https://test.unifieddatalibrary.com")


async def main() -> None:
    notifications = await client.notification.list(
        created_at=f">{sanitize_datetime(datetime.now() - timedelta(minutes=60 * 24))}"
    )
    print(notifications)


asyncio.run(main())
