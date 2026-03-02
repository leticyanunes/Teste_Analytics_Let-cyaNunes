# Teste_Analytics_LeticyaFranca

Este repositório contém a entrega do teste para Estagiário de Analytics na Quod. Os scripts Python estão na pasta "python/". O arquivo "TESTE.py" cria e limpa o dataset de vendas, que é salvo como "data_clean.csv". O arquivo "TESTE.2.py" realiza análises e gera gráficos de tendência de vendas ao longo do ano. As consultas SQL estão em "sql/consultas_sql.sql" e o relatório de insights está em "relatorio_insights.pdf".  

Para executar os scripts Python, é necessário ter Python 3.x e as bibliotecas pandas, datatime, random e matplotlib. Instale usando: pip install pandas datatime matplotlib random. Execute primeiro "python python/TESTE.py" para gerar o dataset limpo. Depois execute "python python/TESTE.2.py" para gerar análises e gráficos.  

As consultas SQL podem ser executadas em qualquer ferramenta MySQL compatível. Crie o banco de dados, carregue o arquivo "data_clean.csv" na tabela de vendas e execute as consultas presentes no arquivo "sql/consultas_sql.sql".  

Observação: o dataset foi simulado para o período de 01/01/2023 a 31/12/2023. Por isso, os resultados das consultas SQL sobre junho foram analisados com base em 2023, mesmo que o enunciado mencione 2024.  

O relatório de insights apresenta os produtos com maior e menor venda, padrões de vendas ao longo do ano e sugestões de ações baseadas nos dados.
