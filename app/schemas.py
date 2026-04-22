from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    message: str = Field(min_length=1, description="Mensaje de entrada del usuario.")


class ChatResponse(BaseModel):
    reply: str
