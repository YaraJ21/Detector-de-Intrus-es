#data: 25/05/2026

# Detector Inteligente com IA
import joblib
import pandas as pd

# Carregar modelo treinado
modelo = joblib.load("modelo_treinado.pkl")
encoder= joblib.load("encoder.pkl")

# Função de previsão
def prever_ataque(dados):

    # Criar tabela com os dados recebidos
    entrada = pd.DataFrame([dados])

    # Fazer previsão
    previsao = modelo.predict(entrada)
    ataque= encoder.inverse_transform(previsao)

    return ataque[0]

dados_teste= {
    "Total Fwd Packets": 2,
    "Flow Duration": 3,
    "Total Backward Packets": 0
}

resultado= prever_ataque(dados_teste)

print("Resultado previsto: ", resultado)