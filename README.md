# Proyecto PostgreSQL en Docker

Este proyecto configura una base de datos PostgreSQL en Docker.

## Requisitos
- Docker

## Pasos para iniciar
1. Ejecutar el contenedor:
   ```bash
   docker run --name contenedor_plan_de_carrera -e POSTGRES_USER=aleira -e POSTGRES_PASSWORD=shifta20 -e POSTGRES_DB=sql_dev -p 5432:5432 -v C:/postgres_data:/var/lib/postgresql/data -d postgres
