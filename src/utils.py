from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import os
from dotenv import load_dotenv
load_dotenv()

ASTRA_DB_APPLICATION_TOKEN = os.getenv('ASTRA_DB_APPLICATION_TOKEN')
ASTRA_DB_KEYSPACE = os.getenv('ASTRA_DB_KEYSPACE')
ASTRA_DB_SECURE_BUNDLE_PATH = os.getenv('ASTRA_DB_SECURE_BUNDLE_PATH')
OPENAI_API_KEY=os.getenv('OPENAI_API_KEY')

def getCQLSession():
    cluster = Cluster(
        cloud={
            "secure_connect_bundle": ASTRA_DB_SECURE_BUNDLE_PATH,
        },
        auth_provider=PlainTextAuthProvider(
            "token",
            ASTRA_DB_APPLICATION_TOKEN,
        ),
    )
    astraSession = cluster.connect()
    return astraSession

def getCQLKeyspace():
    return ASTRA_DB_KEYSPACE
