from fastapi import APIRouter, status
from modules.IA_services import conectar_openrouter
from schemas.chat import OpenRouterRequest, OpenRouterResponse
from base_de_datos.database import chats_collection




router = APIRouter()

@router.post(
    "/chat/message",
    response_model=OpenRouterResponse,
    status_code=status.HTTP_200_OK
)

def chat(mensaje: OpenRouterRequest):

    # mensaje del usuario
    mensaje_db = {
        "rol": "user",
        "contenido": mensaje.message
    }

    chats_collection.insert_one(mensaje_db)

    # respuesta de la IA
    respuesta = conectar_openrouter(
        message=mensaje.message,
        model=mensaje.model
    )

    respuesta_db = {
        "rol": "assistant",
        "contenido": respuesta["answer"]
    }

    chats_collection.insert_one(respuesta_db)

    return respuesta
    