#!/bin/sh

# Verificar se o parâmetro foi passado
if [ "$1" = "up" ]; then
    # Permitir que o docker se conecte com o servidor X11, somente se a permissão ainda não existir
    if ! xhost | grep -q 'local:docker'; then
        xhost +local:docker
    fi

    docker compose up -d

elif [ "$1" = "down" ]; then
    # Parar e remover containers com o docker compose
    docker compose down

elif [ "$1" = "app" ]; then
    docker compose start app

elif [ "$1" = "database" ]; then
    docker compose start database

elif [ "$1" = "build" ]; then
    docker compose down
    docker compose up -d --build

else
    # Mensagem de erro caso o parâmetro seja inválido
    echo "Uso: $0 {up|down}"
    exit 1
fi
