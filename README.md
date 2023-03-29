Projeto de Análise de Vendas
Este projeto consiste em analisar as vendas de uma loja fictícia utilizando uma base de dados em MySQL. O objetivo é obter insights a partir dos dados e apresentar visualizações gráficas dos resultados.

Funcionalidades
O script Python desenvolvido para este projeto realiza as seguintes tarefas:

Conexão com o banco de dados MySQL;<br>
Consulta dos dados de vendas por produto, cliente e região;<br>
Criação de gráficos de barras e de pizza para as informações obtidas;<br>
Exportação dos resultados em arquivos de texto.<br>
Tecnologias utilizadas
As principais tecnologias utilizadas neste projeto foram:

MySQL: para armazenar a base de dados de vendas;<br>
Python: para realizar as consultas e criar as visualizações gráficas;<br>
Pandas: biblioteca para manipulação e análise de dados;<br>
Matplotlib e Seaborn: bibliotecas para criação de gráficos.<br>
Instalação
Para executar o script deste projeto, você precisará instalar as seguintes bibliotecas do Python através do gerenciador de pacotes pip:

mysql-connector-python
pandas
matplotlib
seaborn

Utilização
Antes de executar o script, certifique-se de que o servidor MySQL esteja rodando e que o banco de dados banco_vendas esteja criado. Caso contrário, crie o banco de dados e importe o arquivo banco_vendas.sql para criar as tabelas e inserir os dados de exemplo.


Por fim, execute o arquivo app.py para gerar as visualizações gráficas e exportar os resultados em arquivos de texto.

Você pode ajustar o tamanho dos gráficos e a quantidade de colunas exibidas nos resultados facilmente, alterando os parâmetros no código conforme a sua necessidade.
O código permite que você execute comandos SQL dentro da IDE no próprio arquivo python, então provavelmente você não encontrará problemas em escalar a aplicação.

Arquivos
Este projeto contém os seguintes arquivos:

app.py: script principal para consulta e visualização dos dados de vendas;<br>
banco_vendas.sql: arquivo SQL para criação do banco de dados e inserção de dados de exemplo;<br>
vendas_por_produto.png: imagem do gráfico de barras das vendas por produto;<br>
vendas_por_cliente.png: imagem do gráfico de barras das vendas por cliente;<br>
vendas_por_regiao.png: imagem do gráfico de pizza das vendas por região;<br>
vendas_por_produto.txt: arquivo de texto com a tabela das vendas por produto;<br>
vendas_por_cliente.txt: arquivo de texto com a tabela das vendas por cliente;<br>
vendas_por_regiao.txt: arquivo de texto com a tabela das vendas por região;<br>
README.md: este arquivo com a documentação do projeto.
Autor
Este projeto foi desenvolvido por Carlos Alberto Witzler Filho. Sinta-se livre para entrar em contato para qualquer sugestão ou dúvida!
