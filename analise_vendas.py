import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../data/vendas.csv')
df['data'] = pd.to_datetime(df['data'])
df['faturamento'] = df['valor'] * df['quantidade']

print(' VISÃO GERAL')
print(df.head(), '\n')

print(' Faturamento total:')
print(df['faturamento'].sum(), '\n')

print(' Faturamento por categoria:')
print(df.groupby('categoria')['faturamento'].sum(), '\n')

produto_top = df.groupby('produto')['quantidade'].sum().idxmax()
print(f' Produto mais vendido: {produto_top}')

df.groupby('categoria')['faturamento'].sum().plot(kind='bar')
plt.title('Faturamento por Categoria')
plt.xlabel('Categoria')
plt.ylabel('Faturamento (R$)')
plt.tight_layout()
plt.show()
