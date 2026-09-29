#data: 25/05/2026
#data: 11/06/2026: Update das Features de dettecao 

# Detector Inteligente com IA
import joblib
import pandas as pd

from features_modelo import FEATURES
from colector_rede import obter_dados_rede
from device_tracker import update_prediction

# Carregar modelo treinado
modelo = joblib.load("modelo_treinado.pkl")
encoder= joblib.load("encoder.pkl")

# ============================
# FUNÇÃO DE PREVISÃO
# ============================

def prever_ataque(dados):
    #Recebe as features de um único IP e devolve a classificação prevista.
    row= {}
     
    for feature in FEATURES:
        row[feature]= dados.get(feature,0)

    # Cria DataFrame com TODAS as features esperadas pelo modelo
    entrada = pd.DataFrame([row])[FEATURES]

    previsao = modelo.predict(entrada)

    # Converte número → label original (ex: BENIGN, DDoS)
    ataque = encoder.inverse_transform(previsao)
    return ataque[0]

def prever_multiplos_ataques(dados_multiplos_ips):
    resultados = {}

    for ip, features in dados_multiplos_ips.items():
        resultado = prever_ataque(features)

        resultados[ip] = resultado

        # Guarda a previsão no tracker do dispositivo
        update_prediction(ip, resultado)

    return resultados


    

# ============================
# TESTE LOCAL
# ============================

if __name__ == "__main__":

   while True:
        print("\nCapturando tráfego por IP...")

        dados = obter_dados_rede()

        resultados = prever_multiplos_ataques(dados)

        for ip, result in resultados.items():
            print(f"\nIP: {ip}")
            print("Resultado:", result)