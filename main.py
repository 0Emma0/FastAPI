from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
def read_root():
    return {"Root": "Hello Root"}

@app.get("/hello")
def read_root():
    return {"Path": "Hello Path"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/calc")
def calc(operator_1: float, operator_2: float):
    return {"suma": operator_1 + operator_2}