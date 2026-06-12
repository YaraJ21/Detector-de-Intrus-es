#Data: 24/05/2026

#Data: 11/06/2026 :Novos features sao adicionados ao modelo 

#Modelo de Ineligencia Artificial 

import pandas as pd
import numpy as np
import joblib

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report

from features_modelo import FEATURES  #Importa os features que o modelo ira aprender 


#Carregamento do DataSet

dataset= pd.read_csv("dataset_completo.csv")
dataset.columns= dataset.columns.str.strip()




#============Selecao de Features==================================================================================================================#
X= dataset[FEATURES]
 
y= dataset["Label"]

# LIMPEZA DOS DADOS

X= X.replace([np.inf, -np.inf], np.nan) #Substitui valores infinitos por NaN

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

modelo = RandomForestClassifier(
    n_estimators=100,
    random_state=42 
    )

modelo.fit(X_treino, y_treino)

print("Modelo treinado com sucesso.")

# TESTE DO MODELO

previsoes = modelo.predict(X_teste)

precisao = accuracy_score(y_teste, previsoes)

print("Precisão:", precisao)

print("\n=== RELATÓRIO COMPLETO ===")
print(classification_report(y_teste, previsoes))

#Guardar modelo treinado
joblib.dump(modelo, "modelo_treinado.pkl")
print("Modelo guardado com sucesso")

#Data: 25/05/2026

joblib.dump(encoder, "encoder.pkl")
print("Modelo guardado com sucesso")