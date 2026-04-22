from fastapi import FastAPI

from app.schemas import ChatRequest, ChatResponse

app = FastAPI(
    title="ENAE Vet API",
    version="0.1.0",
    description="API minima FastAPI para ENAE-9.",
)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/chat/test", response_model=ChatResponse)
def chat_test(payload: ChatRequest) -> ChatResponse:
    return ChatResponse(reply=f"placeholder: {payload.message}")
