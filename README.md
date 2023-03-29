Projeto de Análise de Vendas
Este projeto consiste em analisar as vendas de uma loja fictícia utilizando uma base de dados em MySQL. O objetivo é obter insights a partir dos dados e apresentar visualizações gráficas dos resultados.

Funcionalidades
O script Python desenvolvido para este projeto realiza as seguintes tarefas:

Conexão com o banco de dados MySQL;
Consulta dos dados de vendas por produto, cliente e região;
Criação de gráficos de barras e de pizza para as informações obtidas;
Exportação dos resultados em arquivos de texto.
Tecnologias utilizadas
As principais tecnologias utilizadas neste projeto foram:

MySQL: para armazenar a base de dados de vendas;
Python: para realizar as consultas e criar as visualizações gráficas;
Pandas: biblioteca para manipulação e análise de dados;
Matplotlib e Seaborn: bibliotecas para criação de gráficos.
Instalação
Para executar o script deste projeto, você precisará instalar as seguintes bibliotecas do Python através do gerenciador de pacotes pip:

mysql-connector-python
pandas
matplotlib
seaborn

Utilização
Antes de executar o script, certifique-se de que o servidor MySQL esteja rodando e que o banco de dados banco_vendas esteja criado. Caso contrário, crie o banco de dados e importe o arquivo banco_vendas.sql para criar as tabelas e inserir os dados de exemplo.


Por fim, execute o arquivo app.py para gerar as visualizações gráficas e exportar os resultados em arquivos de texto.

Arquivos
Este projeto contém os seguintes arquivos:

app.py: script principal para consulta e visualização dos dados de vendas;

banco_vendas.sql: arquivo SQL para criação do banco de dados e inserção de dados de exemplo;
vendas_por_produto.png: imagem do gráfico de barras das vendas por produto;
vendas_por_cliente.png: imagem do gráfico de barras das vendas por cliente;
vendas_por_regiao.png: imagem do gráfico de pizza das vendas por região;
vendas_por_produto.txt: arquivo de texto com a tabela das vendas por produto;
vendas_por_cliente.txt: arquivo de texto com a tabela das vendas por cliente;
vendas_por_regiao.txt: arquivo de texto com a tabela das vendas por região;
README.md: este arquivo com a documentação do projeto.
Autor
Este projeto foi desenvolvido por Carlos Alberto Witzler Filho. Sinta-se livre para entrar em contato para qualquer sugestão ou dúvida!
