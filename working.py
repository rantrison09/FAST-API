import fastapi
from fastapi import FastAPI, Path,Query,HTTPException, status
from typing import Optional
from pydantic import BaseModel

app= FastAPI()
class Item(BaseModel):
    name:str
    price: float
    brand: Optional[str]=None

class UpdateItem(BaseModel):
    name: Optional[str]=None
    price: Optional[float]=None
    brand: Optional[str]=None
inventory = {}
@app.get("/get-item/{item_id}")
def get_item(item_id: int = Path(..., description='Id of the item you would like to view')):
    return inventory[item_id]

@app.get('/get-by-name/{item_id}')
def get_item(*, item_id: int, name: Optional[str]= None , test:int):
    for item_id in inventory:
        if inventory[item_id].name == name:
        # if inventory[item_id]["name"].upper() == name.upper():
            return inventory[item_id]
    raise HTTPException (status_code=status.HTTP_404_NOT_FOUND , detail="Item ID not found ")
#request body

@app.post('/create-item/{item_id}')
def create_item(item_id: int ,item:Item):
    if item_id in inventory:
        raise HTTPException (status_code=400, detail="Item ID already exisits ")
    
    
    inventory[item_id] = item
    # inventory[item_id] = {'name': item.name, "brand":item.brand, "price": item.price}
    return inventory[item_id]
    
@app.put('/update-item{item_id}')
def update_item(item_id:int, item: UpdateItem):
    if item_id not in inventory:
        raise HTTPException (status_code=404, detail="Item ID does not exisits ")
    
    if item.name != None:
        inventory[item_id].name = item.name
    if item.price != None:
        inventory[item_id].name = item.price
    if item.brand != None:
        inventory[item_id].name = item.brand
    return inventory[item_id]
    
@app.delete('/delete-item')
def delete_item (item_id:int = Query(..., description="the id of the item delete")):
    if item_id not in inventory:
        raise HTTPException (status_code=404, detail="Item ID does not exisits ")
        #return{"Error":"ID does not exisit"}
    del inventory [item_id]
    return{"Sucess": "Item Deleted"}