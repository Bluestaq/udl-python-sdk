import rich

from unifieddatalibrary import Unifieddatalibrary

client = Unifieddatalibrary(base_url="https://test.unifieddatalibrary.com")

topics = client.secure_messaging.list_topics()

rich.print("List of topics:")
rich.print(topics)

offset = client.secure_messaging.get_latest_offset(topics[0].topic or "no_topic") or -1
rich.print("Latest offset for topic '{}':".format(topics[0].topic or "no_topic"))
rich.print(offset)

pages = client.secure_messaging.get_messages(
    offset=offset, topic=topics[0].topic or "no_topic", max_results=100
).iter_pages()
rich.print("Messages in topic '{}':".format(topics[0].topic or "no_topic"))
for page in pages:
    rich.print(page)
    for message in page:
        rich.print(f"Message: {message}")
