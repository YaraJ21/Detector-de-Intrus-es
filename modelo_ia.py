#Data: 24/05/2026

#Modelo de Ineligencia Artificial 

import pandas as pd
import numpy as np
import joblib

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

#Carregamento do DataSet

dataset= pd.read_csv("C:/Users/ACER/OneDrive/Desktop/isdb/2026/1_Semestre/Seguranca de Sistemas/Detector-de-Intrus-es/dataset_completo.csv")
dataset.columns= dataset.columns.str.strip()

X= dataset[[
    "Total Fwd Packets",
    "Flow Duration",
    "Total Backward Packets"
]]
 
y= dataset["Label"]

# LIMPEZA DOS DADOS

x= X.replace([np.inf, -np.inf], np.nan)

valid_rows = X.notna().all(axis=1)

X = X[valid_rows]
y = y[valid_rows]

# CONVERTER LABELS PARA NÚMEROS

encoder = LabelEncoder()

y_codificado = encoder.fit_transform(y)

# DIVISÃO DE TREINO E TESTE

X_treino, X_teste, y_treino, y_teste = train_test_split(
    X,
    y_codificado,
    test_size=0.2,
    random_state=42
)

# TREINAMENTO DO MODELO

print("A treinar modelo...")

modelo = RandomForestClassifier(n_estimators=10)

modelo.fit(X_treino, y_treino)

print("Modelo treinado com sucesso.")

# TESTE DO MODELO

previsoes = modelo.predict(X_teste)

precisao = accuracy_score(y_teste, previsoes)

print("Precisão:", precisao)

#Guardar modelo treinado
joblib.dump(modelo, "modelo_treinado.pkl")
print("Modelo guardado com sucesso")

#Data: 25/05/2026

joblib.dump(encoder, "encoder.pkl")
print("Modelo guardado com sucesso")