from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from router.chat import router
from router.health import router as health_router



app = FastAPI(title="OpenRouter Service")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
app.include_router(health_router)

