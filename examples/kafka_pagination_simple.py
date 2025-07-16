import rich

from unifieddatalibrary import Unifieddatalibrary

client = Unifieddatalibrary(base_url="https://dev.unifieddatalibrary.com")

# find a topic with messages in it
topic = "eop"

# start at 0 for now
offset = 0
pages = client.secure_messaging.get_messages(offset=offset, topic=topic, max_results=100).iter_pages()
rich.print("Messages in topic '{}':".format(topic))
for page in pages:
    rich.print(f"Page with {len(page.items)} items:")
