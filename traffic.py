import urllib.request
import time

TARGETS = [
    "http://10.10.0.11:8000",
    "http://10.10.0.12:8000"
]

while True:
    for target in TARGETS:
        try:
            urllib.request.urlopen(target, timeout=2)
            print(f"Tráfego enviado para {target}")
        except Exception as e:
            print(f"Erro: {e}")

    time.sleep(2)