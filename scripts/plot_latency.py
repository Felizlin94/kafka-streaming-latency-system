"""
Latency Visualization Script

- Loads latency data from CSV logs
- Generates:
    1. Time-series plot (raw + moving average)
    2. Latency distribution histogram

Purpose:
- Provide offline analysis of streaming system performance
- Help identify latency trends, spikes, and distribution characteristics

Design Notes:
- Supports both header-based and raw CSV formats
- Moving average used to smooth noisy latency signals
"""

import csv
import os
import matplotlib.pyplot as plt


CSV_FILE = "results/latency_log.csv"
OUTPUT_DIR = "results"


def load_latencies():
    latencies = []

    if not os.path.exists(CSV_FILE):
        raise FileNotFoundError("CSV file not found")

    with open(CSV_FILE, "r") as f:
        first_line = f.readline()
        f.seek(0)

        if "latency" in first_line:
            reader = csv.DictReader(f)

            for row in reader:
                try:
                    latencies.append(float(row["latency"]))
                except Exception:
                    continue
        else:
            reader = csv.reader(f)

            for row in reader:
                try:
                    latencies.append(float(row[2]))
                except Exception:
                    continue

    return latencies


def moving_average(data, window=10):
    if len(data) < window:
        return data

    smoothed = []

    for i in range(len(data)):
        start = max(0, i - window + 1)
        smoothed.append(sum(data[start : i + 1]) / (i - start + 1))

    return smoothed


def plot_latency(latencies):
    smooth = moving_average(latencies, window=10)

    plt.figure(figsize=(10, 5))

    plt.plot(latencies, alpha=0.4, label="Raw Latency")
    plt.plot(smooth, linewidth=2, label="Smoothed (MA)")

    plt.title("Kafka Latency Over Time")
    plt.xlabel("Message Index")
    plt.ylabel("Latency (seconds)")
    plt.legend()
    plt.grid()

    path = os.path.join(OUTPUT_DIR, "latency_plot.png")
    plt.savefig(path)

    print(f"Saved: {path}")

    plt.close()


def plot_histogram(latencies):
    plt.figure(figsize=(8, 5))

    plt.hist(latencies, bins=30)

    plt.title("Latency Distribution")
    plt.xlabel("Latency (seconds)")
    plt.ylabel("Frequency")
    plt.grid()

    path = os.path.join(OUTPUT_DIR, "latency_histogram.png")
    plt.savefig(path)

    print(f"Saved: {path}")

    plt.close()


if __name__ == "__main__":
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    latencies = load_latencies()

    print("Loaded latency points:", len(latencies))

    if len(latencies) == 0:
        print("No data found. Check consumer or Docker volume.")
        exit()

    print(f"Min latency: {min(latencies):.6f}s")
    print(f"Max latency: {max(latencies):.6f}s")

    plot_latency(latencies)
    plot_histogram(latencies)

    print("Plotting complete")
