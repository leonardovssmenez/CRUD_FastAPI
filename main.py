from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional,List
from database import SessionLocal
import models
 

app = FastAPI()

class Item(BaseModel): #serializador
    id: int
    name: str
    description:str
    price:int
    on_offer:bool

class Config:
    orm_mode=True

db=SessionLocal()

@app.get("/itens",response_models=List[Item],status_code=200)
def get_all_itens():
    itens=db.query(models.item),all()

    return itens

@app.get("/item/{item_id}")
def get_an_item(item_id:int):
    pass

@app.post("/itens")
def create_an_item():
    pass

@app.put("/item/{item_id}")
def update_an_item(item_id:int):
    pass

@app.delete("/item/{item_id}")
def delete_an_item(item_id:int):
    pass