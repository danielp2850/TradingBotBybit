from cassandra.cluster import Cluster
from cassandra.query import SimpleStatement
import datetime

# Connect to the cluster
cluster = Cluster(['127.0.0.1'])  # Replace with your ScyllaDB IP address
session = cluster.connect('time_series')

# Insert data
def insert_data(device_id, timestamp, value):
    query = """
    INSERT INTO data (device_id, timestamp, value)
    VALUES (%s, %s, %s)
    """
    session.execute(query, (device_id, timestamp, value))

# Query data
def query_data(device_id, start_time, end_time):
    query = SimpleStatement("""
    SELECT * FROM data
    WHERE device_id = %s AND timestamp >= %s AND timestamp <= %s
    """)
    rows = session.execute(query, (device_id, start_time, end_time))
    for row in rows:
        print(row)

# Example usage
if __name__ == "__main__":
    # Insert example data
    insert_data('device_1', datetime.datetime.now(), 23.5)

    # Query data for the last minute
    one_minute_ago = datetime.datetime.now() - datetime.timedelta(minutes=1)
    query_data('device_1', one_minute_ago, datetime.datetime.now())
