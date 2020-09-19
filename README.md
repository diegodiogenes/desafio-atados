# Resolução Atados

Este projeto trata da solução para o desafio de Back-end da Atadados, uma API para cadastro de voluntários e ações sociais.

- Linguagem escolhida: [**Python**](https://www.python.org/);
- Framework back-end: [**Django**](https://www.djangoproject.com/);
- Framework api: [**Django Rest Framework**](https://www.django-rest-framework.org/);
- Banco de dados: [**Postgres**](https://www.postgresql.org/).

## Setup

Para iniciar o projeto, é necessário que tenha instalado em sua máquina o [Docker](https://docs.docker.com/engine/install/) e o [Docker Compose](https://docs.docker.com/compose/install/)

Tendo feito a instação anterior, basta rodar o seguinte comando na raiz do projeto:

```shell script
docker-compose up -d --build
```

### Realizando testes

Para testar se o setup foi concluído com êxito, utilize o comando:

```shell script
./bin/tests.sh
```

### Criando um usuário administrador

Para criar um usuário administrador pode ser utilizado:

```shell script
./bin/create_admin.sh
```

### Dados iniciais do sistema

Para adicionar dados iniciais ao sistema, pode ser utilizado o seguinte comando:

```shell script
./bin/load_data.sh
```

Será criado um usuário administrador e dois usuários default com senha test1234.

## Rotas

Foram criados um total de 10 rotas, sendo elas:
- Auth
  - Login: `[POST] /api-token-auth`
- Usuários
  - Listar: `[GET] /users`
  - Registrar: `[POST] /users`
  - Atualizar: `[PUT] /users/:id`
  - Ver: `[PUT] /users/:id`
  - Apagar: `[DELETE] /users/:id`
- Ações
  - Listar: `[GET] /actions`
  - Registrar: `[POST] /actions`
  - Atualizar: `[PUT] /actions/:id`
  - Ver: `[PUT] /actions/:id`
  - Apagar: `[DELETE] /actions/:id`
