import time
import json
import mysql.connector
from confluent_kafka import SerializingProducer
from confluent_kafka.schema_registry import SchemaRegistryClient
from confluent_kafka.schema_registry.avro import AvroSerializer
from confluent_kafka.serialization import StringSerializer

# ==========================
# Kafka Cluster Config
# ==========================
kafka_config = {
    'bootstrap.servers': 'pkc-921jm.us-east-2.aws.confluent.cloud:9092',
    'sasl.mechanisms': 'PLAIN',
    'security.protocol': 'SASL_SSL',
    'sasl.username': 'NNWXRAN5YAXWEVRA',
    'sasl.password': 'cflt/OcwaZxL8pEUHGBFiKS/rlsh57DqnZ+9QBbandZAiaQX/ut02YVSc1PNeZ+w'
}

# ==========================
# Schema Registry Config
# ==========================
schema_registry_conf = {
    'url': 'https://psrc-4x6n5v3.us-east-2.aws.confluent.cloud',
    'basic.auth.user.info': '{}:{}'.format(
        'RIBBIXSS7EXWTQVP',
        'cflt25TVs1PyTyqdTWfIAxt9+YBRz8tohs7FgDc6qUNNxB4kekILLEAFHYCB5T1A'
    )
}
schema_registry_client = SchemaRegistryClient(schema_registry_conf)

# ==========================
# Load latest schema from Schema Registry
# ==========================
subject_name = 'product-value'  # Value schema subject
schema_str = schema_registry_client.get_latest_version(subject_name).schema.schema_str

# ==========================
# Serializer Setup
# ==========================
key_serializer = StringSerializer('utf_8')
avro_serializer = AvroSerializer(schema_registry_client, schema_str)

# ==========================
# Delivery Report Callback
# ==========================
def delivery_report(err, msg):
    if err is not None:
        print(f"Delivery failed for record {msg.key()}: {err}")
    else:
        print(f"Record {msg.key()} successfully produced to {msg.topic()} [{msg.partition()}] at offset {msg.offset()}")

# ==========================
# Producer Setup
# ==========================
producer = SerializingProducer({
    **kafka_config,
    'key.serializer': key_serializer,
    'value.serializer': avro_serializer
})

# ==========================
# Load Last Checkpoint
# ==========================
try:
    with open('config.json') as f:
        config_data = json.load(f)
        last_read_timestamp = config_data.get('last_read_timestamp', '1900-01-01 00:00:00')
except FileNotFoundError:
    last_read_timestamp = '1900-01-01 00:00:00'

print(f"Last checkpoint: {last_read_timestamp}")

# ==========================
# MySQL Connection
# ==========================
connection = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='VeGiTo@2206',
    database='assignment_db'
)
cursor = connection.cursor(dictionary=True)

# ==========================
# Fetch Incremental Data
# ==========================
query = f"SELECT * FROM product WHERE last_updated > '{last_read_timestamp}'"
cursor.execute(query)
rows = cursor.fetchall()

print(f"Found {len(rows)} new rows since {last_read_timestamp}")

# ==========================
# Produce to Kafka
# ==========================
for row in rows:
    # Apply transformation: uppercase the product name
    if row.get('name'):
        row['name'] = row['name'].upper()

    # Produce record
    producer.produce(
        topic='product',
        key=str(row['id']),  # Kafka key as string
        value=row,
        on_delivery=delivery_report
    )

producer.flush()

# ==========================
# Update Checkpoint
# ==========================
cursor.execute("SELECT MAX(last_updated) as max_ts FROM product")
result = cursor.fetchone()

if result and result['max_ts']:
    new_checkpoint = result['max_ts'].strftime("%Y-%m-%d %H:%M:%S")
    with open('config.json', 'w') as f:
        json.dump({"last_read_timestamp": new_checkpoint}, f)
    print(f"Updated checkpoint to: {new_checkpoint}")

# ==========================
# Cleanup
# ==========================
cursor.close()
connection.close()
print("Data successfully published to Kafka")