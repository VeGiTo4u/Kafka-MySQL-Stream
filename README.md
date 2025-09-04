**Kafka to MySQL Stream**

This project demonstrates a Kafka-to-MySQL streaming pipeline with incremental loading and parallel consumers writing JSON outputs. It showcases how to integrate Kafka producers, consumers, and MySQL while ensuring data consistency and parallelism.

Project Overview
	•	Data is first loaded into MySQL.
	•	A Kafka producer publishes data from MySQL into a Kafka topic.
	•	A Kafka consumer group with 5 instances consumes the messages.
	•	Each consumer writes its own JSON file (for example, consumer1.json, consumer2.json, etc.).
	•	Incremental loading ensures that only records greater than the last-read timestamp are published to Kafka, avoiding duplicates.

This simulates a real-world data pipeline where data ingestion, message streaming, and storage/output are automated and consistent.

Features
	•	MySQL → Kafka → JSON streaming flow
	•	Incremental loading (no duplicate records)
	•	5 parallel consumers writing independent JSON files
	•	Scalable consumer group (can increase or decrease instances)
	•	Timestamp-based checkpointing for consistent ingestion

Tech Stack
	•	Apache Kafka – Message streaming platform
	•	MySQL – Relational database for source data
	•	Python / Java (for producer and consumers)
	•	JSON – Output format for consumer writes

How It Works
	1.	Data is loaded into MySQL tables.
	2.	The producer script reads from MySQL, checks the last-read timestamp, and publishes only new records to a Kafka topic.
	3.	Kafka consumers (5 instances under the same consumer group) consume the messages.
	4.	Kafka distributes partitions among them, and each consumer writes messages into its own JSON file.
	5.	Example output files: consumer1.json, consumer2.json, consumer3.json, consumer4.json, consumer5.json.

Project Structure
	•	producer – Code for MySQL to Kafka publishing
	•	consumers – Code for Kafka to JSON writing
	•	config – Config files for Kafka and MySQL
	•	sample_data – Example MySQL data
	•	output – JSON outputs from consumers
	•	README.md – Project documentation

Key Learning Outcomes
	•	Setting up incremental streaming pipelines
	•	Preventing duplicates with timestamp-based incremental loading
	•	Understanding Kafka consumer groups and load distribution
	•	Writing streaming data into structured JSON outputs

Future Improvements
	•	Add Docker setup for easier environment configuration
	•	Implement schema validation for JSON files
	•	Extend pipeline with real-time dashboards using Kafka + Spark/Flink
	•	Push JSON outputs into a NoSQL store like MongoDB

License

This project is open-source and available under the MIT License.
