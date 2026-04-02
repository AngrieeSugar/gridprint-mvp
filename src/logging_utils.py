import csv
from datetime import datetime

def log_run(print_type, start, end, kwh, quality, path="data/energy_log.csv"):
    """Append a single print run to the energy log."""
    header = ["timestamp", "print_type", "start", "end", "kwh", "quality"]

    try:
        exists = open(path, "r")
        exists.close()
        file_exists = True
    except FileNotFoundError:
        file_exists = False

    with open(path, "a", newline="") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(header)

        writer.writerow([
            datetime.now().isoformat(),
            print_type,
            start,
            end,
            kwh,
            quality
        ])
