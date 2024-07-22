# api-predicao-ataque-cardiaco

## Descrição: Esta API contém views utilizando ModelViewSet que é capaz de realizer o CRUD (Create, Read, Update, Delete) completo em poucas linhas, com código limpo e eficiente, além de usar SimpleRouter nas rotas, tornando as urls mais padronizadas. A rede neural original em códigos não está presente neste repositório, ela apenas foi carregada a partir de um json contendo a sua estrutura e outro arquivo contendo os pesos. A rede neural utiliza recursos do Deep Learning (Aprendizado profundo) e foi a primeira que fiz sozinho. A rede neural foi treinada com dataset obtido no Kaggle e por não possuir muitas linhas de dados (tem 303 linhas e 14 colunas) não foi tão eficiente para o treinamento com a precisão chegando em torno dos 88%, porém, sendo apenas um projeto teste, foi bem produtivo. A base de dados para registros da API é apenas um SQLite simples e será guardado localmente, se quiser utilizar outro banco de dados pode conectar nas settings da API. Caso obtenha interesse no código da rede neural, basta entrar em contao comigo, aqui está meu linkedin: https://www.linkedin.com/in/higor-ribeiro-araujo-892008211/.

## Execução:

### Você pode executar de dois modos: por máquina virtual ou por docker.
### No ambiente Windows, basta seguir os seguintes passos no terminal:
#### 1- criar uma venv:
#### python -m venv venv
#### 2- executar a venv:
#### ./venv/scripts/activate
#### 3- python manage.py runserver
#### obs: Não irei fazer passos para outros OS. Caso tenha problemas, pesquise na internet ou consulte alguma IA.
### Ainda em ambiente windows, agora para o docker, basta digitar o seguinte comando no terminal:
#### docker compose up
#### Se quiser executar em segundo plano: docker compose up -d

### Você pode abrir o swagger do projeto no navegador, pela rota: api/schema/swagger-ui/
### Utilizando o swagger, faça o registro do paciente em "users" e posteriormente pode realizar a consulta do mesmo em "possibility_attack"
### Para registrar o usuário basta:
#### {
  ####  "name": "Higor",
  ####  "cpf": "888.888.888-99"
#### }
#### Obs: O cpf será utilizado apenas para identificar o paciente e diferenciá-lo dos demais, portanto não necessita ser o dado real.
### Já para a consulta, é necessário mais dados e detalhes, por exemplo:
#### {
  #### "age": 22,
  #### "sex": 1,
  #### "cp": 1,
  #### "trtbps": 110,
  #### "chol": 130,
  #### "fbs": 0,
  #### "restecg": 0,
  #### "thalachh": 150,
  #### "exng": 0,
  #### "oldpeak": 2.1,
  #### "slp": 1,
  #### "caa": 2,
  #### "thall": 3,
  #### "user_id": 1
#### }
