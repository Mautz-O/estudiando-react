from pydantic import BaseModel


class ChatCreate(BaseModel):
    usuario_id: str
    titulo: str


class ChatResponse(BaseModel):
    id: str
    usuario_id: str
    titulo: str
    fecha_creacion: str


# Compatibilidad con nombres anteriores del proyecto
chatCreate = ChatCreate
chatResponse = ChatResponse
