# Kafka-MySQL-Stream
A Kafka-to-MySQL streaming pipeline that ingests data incrementally (based on last-read timestamp), publishes it to Kafka, and consumes it through 5 parallel consumer instances. Each consumer writes its own JSON file while ensuring no duplicate records are processed.
