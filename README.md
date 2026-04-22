# ENAE Vet API

Implementacion minima de API FastAPI para el ticket `ENAE-9` (`VET-7`).

## Requisitos
- Python 3.11+ recomendado
- pip

## Instalacion
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Arranque local
```bash
uvicorn app.main:app --reload
```

## Endpoints incluidos
- `GET /health`: verificacion de salud del servicio.
- `POST /chat/test`: endpoint de chat placeholder con modelos Pydantic.

## Documentacion Swagger
- URL local: `http://127.0.0.1:8000/docs`

## Ejemplo rapido
```bash
curl -X POST "http://127.0.0.1:8000/chat/test" ^
  -H "Content-Type: application/json" ^
  -d "{\"message\":\"hola\"}"
```
