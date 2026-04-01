"""
Consumer Service

- Consumes streaming events from Kafka
- Computes end-to-end latency (event time → processing time)
- Logs latency to CSV for offline analysis
- Performs window-based aggregation on latency metrics
- Simulates fault scenarios (consumer crash)

Design Notes:
- Uses tumbling window aggregation (fixed-size window)
- Includes fault injection to observe system behavior under instability
- Auto-commit enabled for simplicity (not for strict reliability experiments)
"""

from kafka import KafkaConsumer
import json
import time
import random

from app.utils.latency import calculate_latency, log_latency, init_csv
from app.processing.streaming_logic import WindowAggregator


TOPIC = "test-topic"
BOOTSTRAP_SERVERS = "kafka:9092"


# Initialize CSV file for latency logging
init_csv()


# Initialize streaming aggregation component
aggregator = WindowAggregator(window_size=10)


# Initialize Kafka consumer with retry logic
while True:
    try:
        consumer = KafkaConsumer(
            TOPIC,
            bootstrap_servers=BOOTSTRAP_SERVERS,
            value_deserializer=lambda x: json.loads(x.decode("utf-8")),
            auto_offset_reset="earliest",
            group_id="latency-group",
            enable_auto_commit=True,
            consumer_timeout_ms=1000,  # prevent blocking forever
        )
        print("Kafka connected!")
        break
    except Exception as e:
        print(f"Waiting for Kafka... ({e})")
        time.sleep(3)


# Main streaming consumption loop
while True:
    try:
        for msg in consumer:
            try:
                receive_time = time.time()
                event_time = msg.value["timestamp"]

                # Compute latency correctly
                latency = calculate_latency(event_time, receive_time)

                print(f"Received: {msg.value} | Latency: {latency:.6f}")

                # Log to CSV
                log_latency(event_time, receive_time, latency)

                # Window aggregation
                avg_latency = aggregator.add(latency)
                if avg_latency is not None:
                    print(
                        f"Window Avg Latency (last {aggregator.window_size}): {avg_latency:.6f}"
                    )

                # Fault injection
                if random.random() < 0.1:
                    raise Exception("Simulated Consumer Crash")

            except Exception as e:
                print(f"Processing error: {e}")
                time.sleep(2)

    except Exception as e:
        print(f"Consumer loop error: {e}")
        time.sleep(3)
