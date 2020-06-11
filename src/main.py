from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import motor.motor_asyncio
import json

class Item(BaseModel):
    item_id: int
    item_name: str
    description: str = None

app = FastAPI()

@app.on_event("startup")
async def app_startup():
    """
    Do tasks related to app initialization.
    """
    # This if fact does nothing its just an example.
    client = motor.motor_asyncio.AsyncIOMotorClient()
    db = client['test_database']

# client = motor.motor_asyncio.AsyncIOMotorClient()
# db = client['test_database']
# collection = db['test_collection']



@app.post("/items/")
async def insert_one(todo_item: Item):
    # todo_item = json.load(todo_item)
    # document = {'key': 'value'}
    result = await db.todo_item.insert_one(todo_item.dict())
    return {"message": " item inserted successfully"}
    # print('result %s' % repr(result.inserted_id))

@app.get("/items/{item_id}")
async def do_find_one():
    document = await db.test_collection.find_one({'item_id': item_id})
    return {"item": document}


    # pprint.pprint(document)

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}



# if __name__ == '__main__':
#     uvicorn.run(app, host='0.0.0.0',port=8000)