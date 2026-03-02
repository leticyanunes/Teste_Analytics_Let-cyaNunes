import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

df = pd.read_csv("data_clean.csv")

# Criar coluna de total de venda
df["Total_Venda"] = df["Quantidade"] * df["Preco"]

# Total por produto
total_por_produto = df.groupby("Produto")["Total_Venda"].sum()

print("Total de vendas por produto:")
print(total_por_produto)

# Produto com maior venda
produto_top = total_por_produto.idxmax()

print("\nProduto com maior total de vendas:")
print(produto_top)

# Para analisar mensalmente
# Criar coluna de mês
df["Data"] = pd.to_datetime(df["Data"])
df["Mes"] = df["Data"].dt.month

# Agrupar por mês
vendas_mensais = df.groupby("Mes")["Total_Venda"].sum()

print(vendas_mensais)

import matplotlib.pyplot as plt

plt.figure()
plt.plot(vendas_mensais.index, vendas_mensais.values)
plt.xlabel("Mes")
plt.ylabel("Total de Vendas")
plt.title("Tendencia de Vendas em 2023")
plt.show()