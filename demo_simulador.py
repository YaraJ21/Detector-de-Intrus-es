import json
import time
import random

estados = [
    {
        "10.10.0.10": ("node01", "ACTIVE", "BENIGN"),
        "10.10.0.11": ("node02", "ACTIVE", "BENIGN"),
        "10.10.0.12": ("node03", "ACTIVE", "BENIGN")
    },
    {
        "10.10.0.10": ("node01", "ACTIVE", "BENIGN"),
        "10.10.0.11": ("node02", "ACTIVE", "BENIGN"),
        "10.10.0.12": ("node03", "ACTIVE", "BENIGN")
    },
    {
        "10.10.0.10": ("node01", "ACTIVE", "BENIGN"),
        "10.10.0.11": ("node02", "ACTIVE", "PortScan"),
        "10.10.0.12": ("node03", "ACTIVE", "BENIGN")
    },
    {
        "10.10.0.10": ("node01", "ACTIVE", "BENIGN"),
        "10.10.0.11": ("node02", "ACTIVE", "PortScan"),
        "10.10.0.12": ("node03", "ACTIVE", "BENIGN")
    },
    {
        "10.10.0.10": ("node01", "ACTIVE", "BENIGN"),
        "10.10.0.11": ("node02", "ACTIVE", "DDoS"),
        "10.10.0.12": ("node03", "ACTIVE", "BENIGN")
    },
    {
        "10.10.0.10": ("node01", "ACTIVE", "BENIGN"),
        "10.10.0.11": ("node02", "ACTIVE", "DDoS"),
        "10.10.0.12": ("node03", "ACTIVE", "BENIGN")
    },
    {
        "10.10.0.10": ("node01", "ACTIVE", "BENIGN"),
        "10.10.0.11": ("node02", "ACTIVE", "BENIGN"),
        "10.10.0.12": ("node03", "ACTIVE", "BENIGN")
    }
]

pacotes = {
    "10.10.0.10": 120,
    "10.10.0.11": 180,
    "10.10.0.12": 100
}

while True:

    for estado_atual in estados:

        dados = {}

        for ip, (nome, status, prediction) in estado_atual.items():

            pacotes[ip] += random.randint(5, 25)

            dados[ip] = {
                "name": nome,
                "status": status,
                "prediction": prediction,
                "packets": pacotes[ip],
                "activity_score": pacotes[ip],
                "last_seen": time.strftime("%H:%M:%S")
            }

        with open("state_exemplo.json", "w", encoding="utf-8") as ficheiro:
            json.dump(dados, ficheiro, indent=4, ensure_ascii=False)

        print(">>> ESTADO DA DEMO ATUALIZADO")
        print(dados)

        time.sleep(3)