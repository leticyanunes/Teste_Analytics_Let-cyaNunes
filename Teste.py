import pandas as pd
import random
from datetime import datetime, timedelta

# Produtos e suas categorias
produtos = {
    "Notebook": "Eletronicos",
    "Celular": "Eletronicos",
    "Tablet": "Eletronicos",
    "Monitor": "Eletronicos",
    "Fone": "Acessorios",
    "Teclado": "Acessorios",
    "Cadeira Gamer": "Moveis",
    "Mesa Escritorio": "Moveis"
}

dados = []

# Gerar 50 registros
for i in range(50):
    # Gerar data aleatória em 2023
    data = datetime(2023, 1, 1) + timedelta(days=random.randint(0, 364))

    # Escolher produto aleatório
    produto = random.choice(list(produtos.keys()))

    # Pegar categoria correspondente
    categoria = produtos[produto]

    # Gerar quantidade e preço
    quantidade = random.randint(1, 15)
    preco = random.randint(200, 5000)

    dados.append([i + 1, data, produto, categoria, quantidade, preco])

# Criar DataFrame
df = pd.DataFrame(dados, columns=["ID", "Data", "Produto", "Categoria", "Quantidade", "Preco"])

# Criar erro proposital para limpeza
df.loc[0, "Preco"] = None
df = pd.concat([df, df.iloc[[1]]])

# Tratar valor faltante
df["Preco"] = df["Preco"].fillna(0)

# Remover duplicatas
df = df.drop_duplicates()

# Converter data
df["Data"] = pd.to_datetime(df["Data"])

# Dataset limpo
df.to_csv("data_clean.csv", index=False)

df = pd.read_csv("data_clean.csv")

print(df)
