import psutil
import csv
import time
import os
from datetime import datetime

# File path
DATA_DIR = os.path.join("..", "data")
CSV_FILE = os.path.join(DATA_DIR, "system_data.csv")


def create_csv_if_not_exists():
    """
    Creates CSV file with headers if it does not exist.
    """
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["timestamp", "cpu", "ram", "disk"])


def collect_system_data(interval=5):
    """
    Collects CPU, RAM, and Disk usage at fixed intervals.
    """
    create_csv_if_not_exists()
    print("📊 System monitoring started... (Press CTRL+C to stop)")

    while True:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cpu = psutil.cpu_percent(interval=1)
        ram = psutil.virtual_memory().percent
        disk = psutil.disk_usage("/").percent

        with open(CSV_FILE, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([timestamp, cpu, ram, disk])

        print(f"{timestamp} | CPU: {cpu}% | RAM: {ram}% | Disk: {disk}%")
        time.sleep(interval)


if __name__ == "__main__":
    collect_system_data()
