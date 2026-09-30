import json


def ler_estado():
    """Lê o estado dos nós a partir do ficheiro JSON."""

    try:
        with open("state_exemplo.json", "r", encoding="utf-8") as ficheiro:
            return json.load(ficheiro)

    except FileNotFoundError:
        print("Ficheiro de estado não encontrado.")
        return {}

    except json.JSONDecodeError:
        print("Erro: o ficheiro de estado não contém JSON válido.")
        return {}


def obter_no(ip):
    """Obtém os dados de um nó através do seu IP."""

    estado = ler_estado()
    return estado.get(ip)

def obter_nos_para_interface():
    """Converte o estado do backend para o formato usado pela interface."""

    estado = ler_estado()

    nos = {}

    for ip, dados in estado.items():
        nome = dados["name"].upper().replace("NODE", "NODE ")

        nos[nome] = {
            "ip": ip,
            "estado": {
                "ACTIVE": "ACTIVO",
                "INACTIVE": "INACTIVO"
            }.get(dados["status"], dados["status"]),
            "predicao": dados["prediction"],
            "pacotes": dados["packets"],
            "actividade": dados["activity_score"],
            "ultima_actividade": dados["last_seen"]
        }

    return nos