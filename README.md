# api-predicao-ataque-cardiaco

## Descrição: Esta API contém views utilizando ModelViewSet que é capaz de realizer o CRUD (Create, Read, Update, Delete) completo com poucas linhas, com código limpo e eficiente, além de usar SimpleRouter nas rotas, tornando as urls mais padronizadas. A rede neural original em códigos não está presente neste repositório, ela apenas foi carregada a partir de um json contendo a sua estrutura e outro arquivo contendo os pesos. A rede neural utiliza recursos do Deep Learning (Aprendizado profundo) e foi a primeira que fiz sozinho. Caso obtenha interesse no código da rede neural, basta entrar em contao comigo, aqui está meu linkedin: https://www.linkedin.com/in/higor-ribeiro-araujo-892008211/.

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
