#Data: 25/05/2026

# ============================================
# Data: 12/06/2026
# ============================================
# CYBERSHIELD AI - COLETOR DE TRÁFEGO IDS
#
# ALTERAÇÕES IMPORTANTES NESTA VERSÃO:
# - Migração de estatísticas globais → PER-IP
# - Suporte a múltiplos dispositivos simultâneos
# - Preparação de features compatíveis com treino ML
# - Base para deteção individual por host
# ============================================


#CAPTURA DE TRÁFEGO EM TEMPO REAL

from scapy.all import sniff
import time

from rede_config import INTERFACE

from scapy.layers.inet import TCP

from features_modelo import FEATURES

from scapy.layers.inet import IP

from device_tracker import update_device

import statistics

from collections import defaultdict


# ============================================
# ESTRUTURA PRINCIPAL (PER-IP STATE)
# ============================================

devices = defaultdict(lambda: {
    "packets": 0,
    "bytes": 0,
    "lengths": [],
    "syn": 0,
    "ack": 0,
    "rst": 0,
    "last_seen": None,
    "status": "UNKNOWN",
    "prediction": "UNKNOWN"
})

#=============================================================
# FUNÇÃO EXECUTADA A CADA PACOTE=======================================================
def analisar_pacote(packet):
    if not packet.haslayer(IP):
        return

    ip = packet[IP].src
    tamanho = len(packet)

    # Atualização base do device
    dev = devices[ip]
    dev["packets"] += 1
    dev["bytes"] += tamanho
    dev["lengths"].append(tamanho)
    dev["last_seen"] = time.strftime("%H:%M:%S")
    
    update_device(ip, "ACTIVE")


    # ========================================
    # EXTRAÇÃO DE FLAGS TCP
    # ========================================

    if packet.haslayer(TCP):
        flags = packet[TCP].flags

        if flags & 0x02:
            dev["syn"] += 1

        if flags & 0x10:
            dev["ack"] += 1

        if flags & 0x04:
            dev["rst"] += 1


# ============================================
# CONSTRUÇÃO DE FEATURES POR IP
# ============================================

def build_features(dev, duration):

    lengths = dev["lengths"]

    if lengths:
        mean_len = statistics.mean(lengths)
        std_len = statistics.stdev(lengths) if len(lengths) > 1 else 0
    else:
        mean_len = 0
        std_len = 0

    return {
        "Flow Duration": duration,
        "Total Fwd Packets": dev["packets"],
        "Total Backward Packets": int(dev["packets"] * 0.3),

        "Flow Bytes/s": dev["bytes"] / duration if duration > 0 else 0,
        "Flow Packets/s": dev["packets"] / duration if duration > 0 else 0,

        "Fwd Packet Length Mean": mean_len,
        "Bwd Packet Length Mean": mean_len,

        "Packet Length Mean": mean_len,
        "Packet Length Std": std_len,

        "SYN Flag Count": dev["syn"],
        "ACK Flag Count": dev["ack"],
        "RST Flag Count": dev["rst"]
    }

# ============================================
# FUNÇÃO PARA OBTER DADOS DA REDE
# ============================================

def obter_dados_rede():

    global devices
    
     # Reset temporário de janela (3 segundos)
    start = time.time()

    # Limpa estado antigo (window-based IDS)
    devices.clear()

    # Captura pacotes durante 5 segundos
    sniff(
        prn=analisar_pacote,
        timeout=10,
        store=False,
        iface= INTERFACE
    )

    duracao = time.time() - start

    features_por_ip = {}

    for ip, dev in devices.items():

        features_por_ip[ip] = {
            key: build_features(dev, duracao).get(key, 0)
            for key in FEATURES
        }

    return features_por_ip





if __name__ == "__main__":

        print("📡 Capturando tráfego por IP...")

        dados = obter_dados_rede()

        for ip, features in dados.items():
            print("\nIP:", ip)
            print(features)