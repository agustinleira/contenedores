# Proyecto PostgreSQL en Docker

Este proyecto configura una base de datos PostgreSQL en Docker utilizando Docker Compose para facilitar la ejecución y persistencia de datos.

## Requisitos
- Docker
- Docker Compose

## Configuración

El proyecto contiene:
- Un archivo `docker-compose.yml` que define el servicio PostgreSQL, configurando el usuario, contraseña, y base de datos.
- Un archivo `.sql` con los comandos para crear e insertar datos en una tabla de ejemplo.

## Pasos para iniciar

1. Clona el repositorio:
   En Gitbash
   git clone https://github.com/agustinleira/contenedores.git
   cd contenedores


## Levantar los servicios
docker-compose up -d

## Apagar los servicios
docker-compose down
