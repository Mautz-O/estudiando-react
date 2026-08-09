from fastapi import APIRouter, status
from backend.schemas.chat import ChatCreate, ChatResponse
from uuid import uuid4

router = APIRouter()


@router.post("/chat", response_model=ChatResponse, status_code=status.HTTP_201_CREATED)
async def create_chat(chat: ChatCreate):
    return {
        "id": "chat-001",
        "usuario_id": chat.usuario_id,
        "titulo": chat.titulo,
        "fecha_creacion": "2026-08-09T00:00:00Z",
    }

