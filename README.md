# CRUD com Python e Docker

Este repositório contém uma aplicação configurada para ser executada dentro de contêineres Docker usando o Docker Compose. Abaixo estão os passos para subir e descer os contêineres de forma simples utilizando o script `init.sh`.

## Pré-requisitos

Antes de iniciar o projeto, certifique-se de ter as seguintes ferramentas instaladas em sua máquina:

- [Docker](https://www.docker.com/get-started) (versão 20.x ou superior)
- [Docker Compose](https://docs.docker.com/compose/) (versão 2.29 ou superior)

## Subindo o projeto

Para poder **executar** o script, adicione a permissão de execução:

```bash
chmod +x ./init.sh
```

Para **subir** o projeto e iniciar os contêineres, execute o seguinte comando:

```bash
./init.sh up
```

Para **descer** o projeto e parar os contêineres, execute o seguinte comando:

```bash
./init.sh down
```