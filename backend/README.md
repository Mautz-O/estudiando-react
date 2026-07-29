# Backend (FastAPI)

Este directorio contiene una API minimal construida con FastAPI destinada a servir datos al frontend React.

Requisitos
- Python 3.10+
- `pip`

Instalación rápida
```bash
pip install fastapi uvicorn
```

Ejecutar en desarrollo
```bash
uvicorn modules.hello:app --reload --app-dir backend --host 127.0.0.1 --port 8000
```

Endpoint principal
- `GET /hello` → devuelve JSON: `{ "message": "hola mundo" }`
  - URL local: `http://127.0.0.1:8000/hello`

CORS
- La aplicación ya incluye CORS configurado para permitir peticiones desde los servidores de desarrollo comunes de React:
  - `http://localhost:5173` (Vite)
  - `http://localhost:3000` (Create React App)
- Si despliegas en producción, actualiza `allow_origins` con el dominio de frontend y evita usar `"*"`.

Ejemplo de consumo desde React
```js
fetch('http://127.0.0.1:8000/hello')
  .then(res => res.json())
  .then(data => console.log(data));
```

Notas
- Para entornos reproducibles, puedes crear un `requirements.txt` con:
  ```text
  fastapi
  uvicorn
  ```
- Ajusta el puerto y host en el comando `uvicorn` si ya tienes servicios en esos puertos.
