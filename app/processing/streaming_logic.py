"""
Streaming Logic Module

- Implements simple window-based aggregation
- Computes average latency over a fixed-size window
- Designed as a baseline for streaming behavior analysis

Current Version:
- Tumbling window (count-based, not time-based)
- No overlap between windows
- Stateless between windows (buffer cleared after aggregation)

Future Extensions:
- Sliding window
- Time-based windowing (event time vs processing time)
- Advanced metrics (p95, variance)
"""


class WindowAggregator:
    def __init__(self, window_size=10):
        """
        Initialize window aggregator

        Args:
            window_size (int): Number of events per aggregation window
        """
        self.window_size = window_size
        self.buffer = []

    def add(self, value):
        """
        Add a new value to the window

        When buffer reaches window_size:
        - Compute average
        - Reset buffer (tumbling window behavior)

        Args:
            value (float): latency value

        Returns:
            float | None:
                - average latency if window is full
                - None otherwise
        """
        # Skip invalid values
        if value is None:
            return None

        self.buffer.append(value)

        # Trigger aggregation when window is full
        if len(self.buffer) >= self.window_size:
            avg = sum(self.buffer) / self.window_size

            # Reset buffer → tumbling window
            self.buffer.clear()

            return avg

        return None
