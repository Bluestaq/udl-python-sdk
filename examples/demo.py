from datetime import datetime, timezone

import rich
from unifieddatalibrary import Unifieddatalibrary

client = Unifieddatalibrary(
    base_url="https://test.unifieddatalibrary.com"
)

elsets = client.elsets.list(
    epoch=datetime(2018, 1, 1, 16, 0, 0, 123456, tzinfo=timezone.utc),
)
rich.print(elsets)
assert isinstance(elsets[0].epoch, datetime)
