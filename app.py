import mysql.connector
import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import seaborn as sns

# Faz a conexão com o banco de dados
cnx = mysql.connector.connect(user='Seu_user', password='Sua_Senha', host='127.0.0.1', database='banco_vendas')

# Query para obter as vendas por produto
query_vendas_produto = """
SELECT nome_produto, SUM(quantidade) AS total_vendido, SUM(total) AS receita_total
FROM vendas
GROUP BY nome_produto
"""

# Query para obter as vendas por cliente
query_vendas_cliente = """
SELECT id_cliente, SUM(quantidade) AS total_vendido, SUM(total) AS receita_total
FROM vendas
GROUP BY id_cliente
"""

# Query para obter as vendas por região
query_vendas_regiao = """
SELECT CASE
    WHEN id_cliente IN (1,2,3) THEN 'Sul'
    WHEN id_cliente IN (4,5,6) THEN 'Sudeste'
    WHEN id_cliente IN (7,8,9) THEN 'Nordeste'
    ELSE 'Outros'
END AS regiao,
SUM(quantidade) AS total_vendido,
SUM(total) AS receita_total
FROM vendas
GROUP BY regiao
"""

# Executa as queries e armazena os resultados em dataframes do Pandas
df_vendas_produto = pd.read_sql(query_vendas_produto, con=cnx)
df_vendas_cliente = pd.read_sql(query_vendas_cliente, con=cnx)
df_vendas_regiao = pd.read_sql(query_vendas_regiao, con=cnx)

# Gráfico de barras das vendas por produto
plt.figure(figsize=(8,6))
sns.barplot(x='nome_produto', y='total_vendido', data=df_vendas_produto)
plt.title('Vendas por Produto')
plt.xlabel('Produto')
plt.ylabel('Quantidade Vendida')
plt.savefig('vendas_por_produto.png')

# Gráfico de barras das vendas por cliente
plt.figure(figsize=(8,6))
sns.barplot(x='id_cliente', y='total_vendido', data=df_vendas_cliente)
plt.title('Vendas por Cliente')
plt.xlabel('ID do Cliente')
plt.ylabel('Quantidade Vendida')
plt.savefig('vendas_por_cliente.png')

# Gráfico de pizza das vendas por região
plt.figure(figsize=(8,6))
sns.set_palette('pastel')
plt.pie(df_vendas_regiao['total_vendido'], labels=df_vendas_regiao['regiao'], autopct='%1.1f%%', startangle=90)
plt.title('Vendas por Região')
plt.axis('equal')
plt.savefig('vendas_por_regiao.png')

# exibe todos os gráficos de uma só vez
plt.show()


# Tabela com as vendas por produto
with open('vendas_por_produto.txt', 'w') as f:
    f.write('Vendas por Produto:\n')
    f.write(df_vendas_produto.to_string())

# Tabela com as vendas por cliente
with open('vendas_por_cliente.txt', 'w') as f:
    f.write('Vendas por Cliente:\n')
    f.write(df_vendas_cliente.to_string())

# Tabela com as vendas por região
with open('vendas_por_regiao.txt', 'w') as f:
    f.write('Vendas por Região:\n')
    f.write(df_vendas_regiao.to_string())



# Fecha a conexão com o banco de dados
cnx.close()