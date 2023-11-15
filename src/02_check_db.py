# checks to see if the database is populated with the data from the previous step
import sys
sys.path.append('..')
from utils import getCQLSession, getCQLKeyspace
from config import table_name

session = getCQLSession()
keyspace = getCQLKeyspace()

cqlSelect = f'SELECT * FROM {keyspace}.{table_name} LIMIT 3;'  # (Not a production-optimized query ...)
rows = session.execute(cqlSelect)

for row_i, row in enumerate(rows):
    print(f'\nRow {row_i}:')
    # depending on the cassIO version, the underlying Cassandra table can have different structure ...
    try:
        # you are using the new cassIO 0.1.0+ : congratulations :)
        print(f'    row_id:            {row.row_id}')
        print(f'    vector:            {str(row.vector)[:64]} ...')
        print(f'    body_blob:         {row.body_blob[:64]} ...')
        print(f'    metadata_s:        {row.metadata_s}')        
    except AttributeError:
        # Please upgrade your cassIO to the latest version ...
        print(f'    document_id:      {row.document_id}')
        print(f'    embedding_vector: {str(row.embedding_vector)[:64]} ...')
        print(f'    document:         {row.document[:64]} ...')
        print(f'    metadata_blob:    {row.metadata_blob}')

print('\n...')
