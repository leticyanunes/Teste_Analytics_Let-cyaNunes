CREATE DATABASE case_vendas;
USE case_vendas;

CREATE TABLE vendas (
    ID INT,
    Data DATE,
    Produto VARCHAR(100),
    Categoria VARCHAR(100),
    Quantidade INT,
    Preco DECIMAL(10,2)
);

LOAD DATA INFILE "C:/ProgramData/MySQL/MySQL Server 9.3/Uploads/data_clean.csv"
INTO TABLE vendas
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

SELECT 
    Produto,
    Categoria,
    SUM(Quantidade * Preco) AS Total_Vendas
FROM vendas
GROUP BY Produto, Categoria
ORDER BY Total_Vendas DESC;

SELECT 
    Produto,
    SUM(Quantidade * Preco) AS Total_Junho
FROM vendas
WHERE MONTH(Data) = 6 AND YEAR(Data) = 2023
GROUP BY Produto
ORDER BY Total_Junho ASC
LIMIT 1;

