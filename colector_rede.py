#Data: 25/05/2026

#CAPTURA DE TRÁFEGO EM TEMPO REAL

from scapy.all import sniff
import time

# Variáveis globais
pacotes = 0
inicio = time.time()


# FUNÇÃO EXECUTADA A CADA PACOTE
def analisar_pacote(packet):

    global pacotes

    pacotes += 1


# FUNÇÃO PARA OBTER DADOS DA REDE
def obter_dados_rede():

    global pacotes
    global inicio

    # Reinicia contagem
    pacotes = 0

    inicio = time.time()

    # Captura pacotes durante 5 segundos
    sniff(
        prn=analisar_pacote,
        timeout=5,
        store=False
    )

    duracao = time.time() - inicio

    dados = {

        "requisições": pacotes,
        "duração": int(duracao),
        "pacotes_retorno": int(pacotes * 0.3)
    }

    return dados