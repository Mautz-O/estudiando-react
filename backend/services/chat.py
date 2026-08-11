from datetime import datetime, timezone

from schemas.chat import ChatCreate, ChatResponse
from uuid import uuid4


def create_chat(chat: ChatCreate) -> ChatResponse:
    return ChatResponse(
        id=str(uuid4()),
        usuario_id=chat.usuario_id,
        titulo=chat.titulo,
        fecha_creacion=datetime.now(timezone.utc).isoformat()
    )