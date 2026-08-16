from fastapi import APIRouter, status
from schemas.chat import ChatCreate, ChatResponse
from services.chat import create_chat





router = APIRouter()

 # Genera un UUID único para cada chat creado

@router.post("/chat", response_model=ChatResponse, status_code=status.HTTP_201_CREATED)
async def create_chat_endpoint(chat: ChatCreate):
    return create_chat(chat)