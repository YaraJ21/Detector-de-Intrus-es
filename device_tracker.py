
# device_tracker.py

from collections import defaultdict
from datetime import datetime

# Nós conhecidos da rede CyberShield
KNOWN_DEVICES = {
    "10.10.0.10": "node01",
    "10.10.0.11": "node02",
    "10.10.0.12": "node03"
}

devices = defaultdict(lambda: {
    "name": "UNKNOWN",
    "packets": 0,
    "last_seen": None,
    "status": "INACTIVE",
    "activity_score": 0,
    "prediction": "UNKNOWN"
})


# Inicializa os nós conhecidos
for ip, name in KNOWN_DEVICES.items():
    devices[ip]["name"] = name


def update_device(ip, status):
    devices[ip]["packets"] += 1
    devices[ip]["last_seen"] = datetime.now()
    devices[ip]["status"] = status
    devices[ip]["activity_score"] += 1

    if ip in KNOWN_DEVICES:
        devices[ip]["name"] = KNOWN_DEVICES[ip]


def update_prediction(ip, prediction):
    devices[ip]["prediction"] = prediction


def decay_devices():
    """Marca dispositivos como inactivos se não houver tráfego recente."""
    now = datetime.now()

    for ip, data in devices.items():
        if data["last_seen"] is None:
            continue

        seconds = (now - data["last_seen"]).total_seconds()

        if seconds > 10:
            data["status"] = "INACTIVE"


def get_devices():
    return devices

