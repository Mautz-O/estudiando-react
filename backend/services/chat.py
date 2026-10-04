from datetime import datetime, timezone

from schemas.chat import ChatCreate, ChatResponse
from base_de_datos.database import chats_collection



def create_chat(chat: ChatCreate) -> ChatResponse:
    documento = {
            "usuario_id" : chat.usuario_id,
            "titulo"     : chat.titulo,
            "fecha_creacion" : datetime.now(timezone.utc).isoformat()
    
}
    
    
    resultado = chats_collection.insert_one(documento)
    
    
    
    return ChatResponse(
        id=str(resultado.insert_id),
        usuario_id=chat.usuario_id,
        titulo=chat.titulo,
        fecha_creacion=documento["fecha_creacion"]
    )