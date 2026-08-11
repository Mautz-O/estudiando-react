from fastapi import APIRouter, status
from backend.schemas.chat import ChatCreate, ChatResponse
from backend.services.chat import create_chat


router = APIRouter()

 # Genera un UUID único para cada chat creado

@router.post("/chat", response_model=ChatResponse, status_code=status.HTTP_201_CREATED)
async def create_chat_endpoint(chat: ChatCreate):
    return create_chat(chat)