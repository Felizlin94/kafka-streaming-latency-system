# Kafka Streaming Latency System

## Overview
This project implements an end-to-end streaming pipeline using Kafka to measure, analyze, and visualize message latency.

The system simulates real-time data ingestion and evaluates latency behavior under continuous streaming and fault conditions.

---

## Architecture

Producer  →  Kafka  →  Consumer
                          ↓
                   Latency Logger
                          ↓
                 Streaming Aggregator
                          ↓
                  Visualization Layer

---

## Features

- End-to-end latency measurement
- Window-based streaming aggregation
- Fault simulation (consumer crash)
- Latency visualization (time series + distribution)
- Dockerized deployment

---

## Tech Stack

- Python
- Apache Kafka
- Docker / Docker Compose
- Matplotlib

---

## Current Status (v0.1) 

- Basic Kafka streaming pipeline
- End-to-end latency measurement
- CSV logging and visualization

---

## How It Works

1. Producer sends timestamped messages to Kafka.
2. Consumer receives messages and computes latency
3. Latency is calculated as: 
    latency = receive_time - event_time
4. Latency is logged into CSV  
5. Streaming aggregation computes window averages  
6. Visualization scripts generate plots  


---

## Results

### Latency Over Time
![Latency Plot](results/latency_plot.png)

### Latency Distribution
![Histogram](results/latency_histogram.png)

---

## How to Run

```bash
docker-compose up --build

python scripts/plot_latency.py  (For generate plots:)

---



## Output

results/
 ├── latency_log.csv
 ├── latency_plot.png
 └── latency_histogram.png 

---


## Key Insights
Kafka shows strong steady-state latency performance
Initial backlog significantly impacts early latency
System exhibits realistic latency spikes under load/fault conditions

---

## Future Work
Multi-consumer scaling
Throughput vs latency trade-off analysis
Integration with real financial data streams
Advanced fault injection scenarios

---



