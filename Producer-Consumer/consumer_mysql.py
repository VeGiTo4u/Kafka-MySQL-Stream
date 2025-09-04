import json
import socket
import sys
from confluent_kafka import DeserializingConsumer
from confluent_kafka.schema_registry import SchemaRegistryClient
from confluent_kafka.schema_registry.avro import AvroDeserializer
from confluent_kafka.serialization import StringDeserializer

# ==========================
# Get Consumer Number from Arguments
# ==========================
if len(sys.argv) != 2:
    print("Usage: python consumer.py <consumer_number>")
    sys.exit(1)

consumer_number = sys.argv[1]
output_file = f"consumer{consumer_number}.json"

# ==========================
# Kafka Cluster Config
# ==========================
kafka_config = {
    'bootstrap.servers': 'pkc-921jm.us-east-2.aws.confluent.cloud:9092',
    'security.protocol': 'SASL_SSL',
    'sasl.mechanisms': 'PLAIN',
    'sasl.username': 'NNWXRAN5YAXWEVRA',
    'sasl.password': 'cflt/OcwaZxL8pEUHGBFiKS/rlsh57DqnZ+9QBbandZAiaQX/ut02YVSc1PNeZ+w',
    'group.id': 'product-consumer-group',  
    'auto.offset.reset': 'earliest'
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
# Load Avro Schema for Value
# ==========================
subject_name = 'product-value'
schema_str = schema_registry_client.get_latest_version(subject_name).schema.schema_str

# ==========================
# Deserializer Setup
# ==========================
key_deserializer = StringDeserializer('utf_8')
avro_deserializer = AvroDeserializer(schema_registry_client, schema_str)

# ==========================
# Consumer Setup
# ==========================
consumer = DeserializingConsumer({
    **kafka_config,
    'key.deserializer': key_deserializer,
    'value.deserializer': avro_deserializer
})

consumer.subscribe(['product'])

print(f"Writing messages to {output_file}")

# ==========================
# Consume Loop
# ==========================
try:
    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue

        if msg.error():
            print(f"Consumer error: {msg.error()}")
            continue

        key = msg.key()
        value = msg.value()

        print(f"Received message: key={key}, value={value}")

        with open(output_file, 'a') as f:
            f.write(json.dumps(value, default=str) + '\n')

except KeyboardInterrupt:
    print("Stopping consumer...")

finally:
    consumer.close()
    print("Consumer closed.")