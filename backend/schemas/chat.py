from pydantic import BaseModel




# Definición de los modelos de datos para la API de chat
class ChatCreate(BaseModel):
    usuario_id: str
    titulo: str

# Definición del modelo de respuesta para la API de chat
class ChatResponse(BaseModel):
    id: str
    usuario_id: str
    titulo: str
    fecha_creacion: str

# Definición del modelo de solicitud para la API de OpenRouter
class OpenRouterRequest(BaseModel):
    message: str
    #api_key: str | None = None
    model: str = "openai/gpt-4o-mini"

#respuesta del LLM
class OpenRouterResponse(BaseModel):
    answer: str
    model: str


# Compatibilidad con nombres anteriores del proyecto
chatCreate = ChatCreate
chatResponse = ChatResponse
