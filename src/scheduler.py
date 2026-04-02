import json
from datetime import datetime, timedelta

def load_price_curve(path):
    """Load a simple JSON price curve."""
    with open(path, "r") as f:
        raw = json.load(f)

    curve = []
    for entry in raw:
        curve.append({
            "time": datetime.fromisoformat(entry["time"]),
            "price": float(entry["price"])
        })
    return curve


def estimate_cost(start_time, duration_hours, price_curve, power_kw=0.15):
    """
    Estimate cost of running a print starting at start_time.
    Assumes constant power draw (0.15 kW = 150W).
    """
    end_time = start_time + timedelta(hours=duration_hours)
    total_cost = 0.0

    for entry in price_curve:
        t = entry["time"]
        if start_time <= t < end_time:
            total_cost += power_kw * entry["price"]

    return total_cost


def find_cheapest_start(duration_hours, deadline, price_curve):
    """
    Step backwards from deadline in 30-minute increments
    and find the cheapest possible start time that finishes before the deadline.
    """
    best_start = None
    best_cost = float("inf")
    duration = timedelta(hours=duration_hours)

    # Search backwards 48 hours (96 half-hour steps)
    for i in range(96):
        candidate_start = deadline - timedelta(minutes=30 * i)

        # Skip impossible start times
        if candidate_start + duration > deadline:
            continue

        cost = estimate_cost(candidate_start, duration_hours, price_curve)

        if cost < best_cost:
            best_cost = cost
            best_start = candidate_start

    return best_start, best_cost
