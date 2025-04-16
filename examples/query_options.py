


from unifieddatalibrary import Client
from unifieddatalibrary.types.elset_abridged import ElsetAbridged
from unifieddatalibrary.lib.query_field_names import Query as QueryFieldNames 
from unifieddatalibrary.lib.model_based_query import Query as QueryClass
from unifieddatalibrary.lib.util import sanitize_datetime
from datetime import datetime, timedelta
import rich



client = Client(

    base_url="https://test.unifieddatalibrary.com"
)


# Using Query Field Name Help
query = QueryFieldNames(ElsetAbridged).field("sat_no").eq(25544).field("epoch").gte(datetime.now()- timedelta(minutes=60))
response = client.elsets.list(epoch=query.to_params()["epoch"])

rich.print(response)
rich.print(client.elsets.current.list())


# Using Query Class helper
query_class = QueryClass(ElsetAbridged).sat_no_eq('25544')
response = client.elsets.current.list(extra_query=query_class.to_params())
rich.print(response)

# Creating and listing notifications without Query Helper

client.notification.create(
    classification_marking="U",
    data_mode="TEST",
    msg_body=dict(name="bob", val=2),
    msg_type="Dummy",
    source="Test"
)

notifications= client.notification.list(created_at=f">{sanitize_datetime(datetime.now()- timedelta(minutes=30))}")
rich.print(notifications)



