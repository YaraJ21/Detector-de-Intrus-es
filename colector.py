
# COLECTOR DE DADOS REAIS


import pandas as pd
import random


# CARREGA DATASET


dataset = pd.read_csv("dataset_completo.csv")

# Remove espaços extras dos nomes das colunas
dataset.columns = dataset.columns.str.strip()



# FUNÇÃO RESPONSÁVEL POR GERAR DADOS


def gerar_dados():

    # Escolhe linha aleatória
    linha = dataset.sample().iloc[0]

    # Cria dicionário
    dados = {

        "requisições":
            int(linha["Total Fwd Packets"]),

        "duração":
            int(linha["Flow Duration"]),

        "pacotes_retorno":
            int(linha["Total Backward Packets"]),

        "label":
            linha["Label"]
    }

    return dados