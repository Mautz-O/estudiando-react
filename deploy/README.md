# Proyecto React + FastAPI + MongoDB

Este proyecto se despliega con tres archivos Docker Compose separados:

- Frontend React: puerto 5173
- Backend FastAPI: puerto 8000
- MongoDB: puerto 27017


## Servicios

### Frontend
- URL: http://localhost:5173

### Backend
- URL: http://localhost:8000
- Documentación Swagger: http://localhost:8000/docs

### Base de datos
- MongoDB: mongodb://localhost:27017
- Base de datos: appdb

## Iniciar la base de datos

```bash
docker compose -f deploy/database-compose.yml up -d
```

## Iniciar el backend

```bash
docker compose -f deploy/backend-compose.yml up -d
```

## Iniciar el frontend

```bash
docker compose -f deploy/frontend-compose.yml up -d
```

## Ver logs

```bash
docker compose -f deploy/database-compose.yml logs -f

```

## Detener servicios

```bash
docker compose -f deploy/frontend-compose.yml down

```

## Reiniciar todo

```bash
docker compose -f deploy/database-compose.yml down -v


docker compose -f deploy/database-compose.yml up -d

```

## Nota
Si tu backend está en otra carpeta distinta a `../backend`, ajusta la ruta del volumen en `backend-compose.yml`.
Si tu frontend usa otra estructura de proyecto o un puerto diferente, cambia los valores en `frontend-compose.yml`.