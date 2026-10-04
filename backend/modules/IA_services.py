
import os
from dotenv import load_dotenv
import httpx
from fastapi import HTTPException


load_dotenv()


def conectar_openrouter(
    message: str,
    model: str = "openrouter/free"
):

    # Obtener API key desde variables de entorno
    api_key = os.getenv("OPENROUTER_API_KEY")

    # Validar que la API key esté disponible
    if not api_key:
        raise HTTPException(
            status_code=400,
            detail="Falta la API key de OpenRouter."
        )

    # URL del endpoint de chat completions de OpenRouter
    url = "https://openrouter.ai/api/v1/chat/completions"

    # Headers para autenticación y configuración de la solicitud
    headers = {
        "Authorization": f"Bearer {api_key}",  # Token de autenticación
        "Content-Type": "application/json",     # Tipo de contenido
        "HTTP-Referer": "http://localhost:5173",  # Referencia del cliente (frontend)
        "X-Title": "My React Router App",       # Título de la aplicación
    }

    # Payload (cuerpo) de la solicitud
    payload = {
        "model": model,  # Modelo de IA a utilizar
        "messages": [
            {"role": "user", "content": message}  # Mensaje del usuario
        ],
    }

    try:
        # Realizar solicitud POST a OpenRouter con timeout de 60 segundos
        response = httpx.post(
            url,
            headers=headers,
            json=payload,
            timeout=60.0
        )

        # Lanzar excepción si el status HTTP indica error (4xx, 5xx)
        response.raise_for_status()

        # Parsear respuesta JSON
        data = response.json()
        # Extraer el contenido de la primera opción de respuesta
        answer = data["choices"][0]["message"]["content"]

        # Retornar respuesta con modelo utilizado
        return {
            "answer": answer,
            "model": model
        }

    except httpx.HTTPStatusError as exc:
        # Manejar errores HTTP específicos
        raise HTTPException(
            status_code=exc.response.status_code,
            detail=exc.response.text
        ) from exc

    except Exception as exc:
        # Manejar otros errores inesperados
        raise HTTPException(
            status_code=500,
            detail=str(exc)
        ) from exc


    


