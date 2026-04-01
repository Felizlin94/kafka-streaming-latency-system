"""
Producer Service

- Continuously generates timestamped events
- Sends messages to Kafka topic for downstream processing
- Simulates real-time data ingestion in a streaming system

Design Notes:
- Includes retry logic to handle Kafka container startup delay
- Emits one event per second (configurable rate)
"""

from kafka import KafkaProducer
import json
import time

KAFKA_SERVER = "kafka:9092"
TOPIC = "test-topic"


# Initialize Kafka producer with retry loop
while True:
    try:
        producer = KafkaProducer(
            bootstrap_servers=KAFKA_SERVER,
            value_serializer=lambda v: json.dumps(v).encode("utf-8"),
            acks="all",
            retries=5,
        )
        print("Kafka connected!")
        break
    except Exception as e:
        print(f"Waiting for Kafka... ({e})")
        time.sleep(3)


# Main event loop
while True:
    data = {"timestamp": time.time()}

    producer.send(TOPIC, data)
    producer.flush()  # force send for accurate latency measurement

    print("Sent:", data)

    time.sleep(1)
