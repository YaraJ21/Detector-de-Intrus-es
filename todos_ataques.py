import pandas as pd
import glob

# Procura todos os CSVs da pasta archive
arquivos = glob.glob("archive/*.csv")

# Lista para guardar datasets
lista_datasets = []

# Lê cada CSV
for arquivo in arquivos:

    print(f"Lendo: {arquivo}")

    df = pd.read_csv(arquivo)

    lista_datasets.append(df)

# Junta tudo
dataset_final = pd.concat(lista_datasets)

# Guarda dataset final
dataset_final.to_csv("dataset_completo.csv", index=False)

print("Dataset completo criado com sucesso!")