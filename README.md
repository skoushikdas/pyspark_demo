Real-Time Interaction Pipeline

Python 3.8+

PySpark

Confluent Kafka

MongoDB

Pandas

pymongo

openpyxl

Install dependencies:

bash
Copy
Edit
pip install pyspark pandas pymongo openpyxl

Example:

json
Copy
Edit
{
  "generator": {
    "speed_multiplier": 100.0,
    "time_interval": 0.01
  },
  "kafka": {
    "bootstrap.servers": "localhost:9092",
    "security.protocol": "SASL_SSL",
    "sasl.mechanism": "PLAIN",
    "sasl.username": "user",
    "sasl.password": "password",
    "topic": "kafka_test",
    "acks": "1",
    "batch.num.messages": "1000",
    "compression.type": "snappy"
  },
  "mongodb": {
    "uri": "mongodb://localhost:27017",
    "database": "interaction_logs",
    "collection": "aggregated_metrics"
  },
  "dashboard": {
    "output_dir": "./output_reports"
  }
}

1. Run Kafka Data Generator
Simulates real-time interaction data into Kafka.

python producer_runner.py

2. Start the PySpark Kafka Consumer
Consumes the Kafka stream, performs real-time aggregations, and writes results into MongoDB.

python kafka_consumer_runner.py

3. Run Dashboard Generator
Pulls data from MongoDB and exports daily Excel files for monitoring.

python dashboard_runner.py

Output files are stored in the output_reports/ folder, with filenames in the format dashboard_metrics_YYYY-MM-DD.xlsx.