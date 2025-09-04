# Kafka to MySQL Stream

Welcome to the Kafka to MySQL Stream Project repository! 🚀
This project demonstrates a real-time streaming pipeline from MySQL → Kafka → JSON outputs, with incremental loading and parallel consumers. Designed as a portfolio project, it highlights practical data engineering concepts like streaming ingestion, consumer parallelism, and duplicate prevention.

⸻

# 🏗️ **Data Architecture**

**The architecture follows a Producer–Broker–Consumer flow:**

1.	MySQL (Source): Data is loaded into MySQL tables.
2.	Kafka Producer: Reads MySQL data and publishes only incremental records based on the last-read timestamp.
3.	Kafka Broker: Manages the published data streams.
4.	Kafka Consumers (5 Instances): Consume messages in parallel and write separate JSON files (consumer1.json, consumer2.json, etc.).

# **📖 Project Overview**

**This project involves:**
	1.	Incremental Data Ingestion: Load new records from MySQL into Kafka without duplicates.
	2.	Streaming Pipeline: Leverage Kafka for distributing messages across multiple consumers.
	3.	Parallel Consumers: Run 5 consumer instances under a consumer group, each writing to its own JSON file.
	4.	Scalable Architecture: The consumer group can be expanded or reduced depending on workload.

	•	Apache Kafka
	•	Real-time Data Streaming
	•	MySQL Data Integration
	•	Parallel Processing with Consumer Groups
	•	JSON-based Data Outputs

⸻

# **Tech Stack** 
	•	Apache Kafka – Distributed message streaming platform
	•	MySQL/MySQL Workbench – Relational database for source data
	•	Python / Java – For Kafka producer & consumers
	•	JSON – Output format for processed messages

⸻

# **Project Workflow**

**Objective - Build a real-time pipeline that streams MySQL data to Kafka and outputs JSON files through multiple consumers with incremental loading.**

Workflow Steps

	1.	Load Data into MySQL – Insert records into MySQL database tables.
	2.	Producer – Reads new records (greater than last timestamp) and publishes them into a Kafka topic.
	3.	Kafka Broker – Distributes data to consumers.
	4.	Consumers – 5 parallel instances consume the messages and each writes its own JSON file.
	5.	Output – Clean, duplicate-free JSON files per consumer instance.

⸻

# **📂 Repository Structure**

```
kafka-mysql-stream/
|
├── Producer-Cosumer/
|       ├── consumer.py        
│   	└── producer.py

├── Avro Schema
├── README.md               # Project documentation
├── LICENSE                 # License information
├── System Guide
```

# **Key Learning Outcomes**
	•	Setting up a Kafka producer connected to MySQL
	•	Using timestamps for incremental loading and duplicate prevention
	•	Understanding Kafka consumer groups and partition assignment
	•	Implementing parallel consumers writing to JSON files

⸻

# **Future Improvements**
	•	🐳 Add Docker setup for seamless environment configuration
	•	📑 Implement schema validation for JSON output files
	•	📊 Extend with real-time dashboards using Kafka + Spark/Flink
	•	🗄️ Push consumer JSON outputs into a NoSQL store like MongoDB

⸻

# **🛡️ License**

This project is licensed under the MIT License. You are free to use, modify, and share this project with proper attribution.

⸻

# **🌟 About Me**

Hi there! I’m Krrish Sethiya. I’m a 3rd Year Grad at Medicaps University, Indore, currently upskilling myself in Data Engineering and Streaming Technologies.
