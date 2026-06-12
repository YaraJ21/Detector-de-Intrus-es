# device_tracker.py

from collections import defaultdict
from datetime import datetime

devices = defaultdict(lambda:{
    "packets": 0,
    "last_seen": None,
    "status": "UNKNOWN",
    "activity_score": 0})


def update_device(ip, status):
    devices[ip]["packets"] += 1
    devices[ip]["last_seen"] = datetime.now()
    devices[ip]["status"] = status
    devices[ip]["activity_score"]+=1

def decay_devices():
    """Marks devices inactive if no recent packets"""
    now = datetime.now()

    for ip, data in devices.items():
        if data["last_seen"] is None:
            continue

        seconds = (now - data["last_seen"]).total_seconds()

        if seconds > 10:
            data["status"] = "INACTIVE"


def get_devices():
    return devices