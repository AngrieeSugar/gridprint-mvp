import argparse
from datetime import datetime
from scheduler import load_price_curve, find_cheapest_start, estimate_cost

def main():
    parser = argparse.ArgumentParser(description="GridPrint MVP Scheduler")
    parser.add_argument("--duration-hours", type=float, required=True)
    parser.add_argument("--deadline", type=str, required=True)
    parser.add_argument("--prices", type=str, required=True)

    args = parser.parse_args()

    duration = args.duration_hours
    deadline = datetime.fromisoformat(args.deadline)
    price_curve = load_price_curve(args.prices)

    best_start, best_cost = find_cheapest_start(duration, deadline, price_curve)

    # Cost if starting right now
    now = datetime.now()
    cost_now = estimate_cost(now, duration, price_curve)

    print("\n=== GridPrint MVP Scheduler ===")
    print(f"Print duration: {duration} hours")
    print(f"Deadline: {deadline}")
    print(f"\nRecommended start time: {best_start}")
    print(f"Estimated cost (recommended): ${best_cost:.2f}")
    print(f"Estimated cost (start now):   ${cost_now:.2f}")
    print(f"Savings: ${cost_now - best_cost:.2f}\n")

if __name__ == "__main__":
    main()
