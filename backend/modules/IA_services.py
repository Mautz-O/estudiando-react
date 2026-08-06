import os
from dotenv import load_dotenv
import httpx
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="OpenRouter Service")


# Allow the frontend dev servers (Vite/CRA) to access the API
origins = [
    "http://localhost:5173",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class OpenRouterRequest(BaseModel):
    message: str
    #api_key: str | None = None
    model: str = "openai/gpt-4o-mini"

load_dotenv()

def conectar_openrouter(message: str, api_key: str | None = None, model: str = "openai/gpt-4o-mini"):
    api_key = api_key or os.getenv("OPENROUTER_API_KEY")
    print("API KEY cargada:", bool(api_key))
    print("API KEY cargada:", bool(api_key))
    print("Longitud:", len(api_key) if api_key else 0)
    print("Header creado:", bool(f"Bearer {api_key}"))
    if not api_key:
        raise HTTPException(status_code=400, detail="Falta la API key de OpenRouter.")
        
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost:5173",
        "X-Title": "My React Router App",
    }
    payload = {
        "model": model,
        "messages": [
            {"role": "user", "content": message}
        ],
        "stream": True
    }
    print("Header creado:", bool(headers["Authorization"]))
    print("Directorio actual:", os.getcwd())
    print("API key desde entorno:", bool(os.getenv("OPENROUTER_API_KEY")))
   

def conectar_openrouter(
    message: str,
    model: str = "openrouter/free"
):
    api_key = os.getenv("OPENROUTER_API_KEY")

    if not api_key:
        raise HTTPException(
            status_code=400,
            detail="Falta la API key de OpenRouter."
        )

    print("API KEY cargada:", bool(api_key))
    print("Longitud:", len(api_key))

    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost:5173",
        "X-Title": "My React Router App",
    }

    payload = {
        "model": model,
        "messages": [
            {"role": "user", "content": message}
        ],
    }

    try:
        response = httpx.post(
            url,
            headers=headers,
            json=payload,
            timeout=60.0
        )

        response.raise_for_status()

        data = response.json()
        answer = data["choices"][0]["message"]["content"]

        return {
            "answer": answer,
            "model": model
        }

    except httpx.HTTPStatusError as exc:
        raise HTTPException(
            status_code=exc.response.status_code,
            detail=exc.response.text
        ) from exc

    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=str(exc)
        ) from exc

@app.post("/openrouter")
def openrouter_endpoint(request: OpenRouterRequest):
    return conectar_openrouter(
        message=request.message,
        #api_key=request.api_key,
        model=request.model,
    )


@app.get("/health")
def health():
    return {"status": "ok"}
