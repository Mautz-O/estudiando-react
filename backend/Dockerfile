
#Obtiene una imagen que ya tiene Python
FROM python:3.12-slim

#carpeta de trabajo dentro del contenedor.
WORKDIR  /app

#Copia las dependencias del backend.
COPY requirements.txt ./

#Instala FastAPI, Uvicorn, Pydantic, etc.
RUN pip install --no-cache-dir -r requirements.txt

#Copia todo el contenido de backend/ al contenedor.
COPY . .

# puerto en el que se ejecutará la aplicación.
EXPOSE 5173

#indica qué programa debe arrancar cuando se ejecute el contenedor.
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]


