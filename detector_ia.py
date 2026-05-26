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
    entrada = pd.DataFrame([{
    "Total Fwd Packets": dados["requisições"],
    "Flow Duration": dados["duração"],
    "Total Backward Packets": dados["pacotes_retorno"]
    }])

    # Fazer previsão
    previsao = modelo.predict(entrada)
    ataque= encoder.inverse_transform(previsao)

    return ataque[0]

if __name__ == "__main__":
    dados_teste= {
     "requisições": 2,
    "duração": 3,
    "pacotes_retorno": 0
    }
    
    resultado= prever_ataque(dados_teste)

    

    print("Resultado previsto: ", resultado)

