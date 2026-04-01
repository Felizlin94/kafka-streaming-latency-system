# Kafka Streaming Latency System

## Overview
This project implements an end-to-end streaming pipeline using Kafka to measure, analyze, and visualize message latency.

The system simulates real-time data ingestion and evaluates latency behavior under continuous streaming and fault conditions.

---

## Architecture

<img width="1000" height="585.9" alt="architecture" src="https://github.com/user-attachments/assets/db288482-a89d-493e-8492-7e1130f0451a" />

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
<img width="1000" height="500" alt="latency_plot" src="https://github.com/user-attachments/assets/eaac701c-3492-43d5-8024-0bd008b2e7b0" />

### Latency Distribution
<img width="800" height="500" alt="latency_histogram" src="https://github.com/user-attachments/assets/ac10aeb5-c08c-46cb-89bb-e9b57f676b8c" />

---

## How to Run

Bash:
1. docker-compose up --build
2. python scripts/plot_latency.py 

---



## Output

<img width="781" height="318" alt="results" src="https://github.com/user-attachments/assets/8809954a-e3c2-4679-a3b5-eae57f8a61d5" />

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



