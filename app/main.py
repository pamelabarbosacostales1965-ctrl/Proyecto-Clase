from fastapi import FastAPI
from pydantic import BaseModel

from app.calculator import sum, resta, multiply

app = FastAPI()

class OperationRequest(BaseModel):
    a: int
    b: int

@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "Calculator API is running"}


@app.post("/suma")
def suma_endpoint(payload: OperationRequest) -> dict[str, int]:
    return {"result": sum(payload.a, payload.b)}


@app.post("/resta")
def resta_endpoint(payload: OperationRequest) -> dict[str, int]:
    return {"result": resta(payload.a, payload.b)}


@app.post("/multiplicacion")
def multiplicacion_endpoint(payload: OperationRequest) -> dict[str, int]:
    return {"result": multiply(payload.a, payload.b)}