from bson.objectid import ObjectId
from config.config import DB
from fastapi import APIRouter, Depends, HTTPException
from typing import List
import logging

from .models import Item, ItemOnDB



todo_router = APIRouter()


def validate_object_id(id_: str):
    _id = ObjectId(id_)

    return _id


async def _get_item_or_404(id_: str):
    _id = validate_object_id(id_)
    item = await DB.item.find_one({"_id": _id})
    if item:
        return item
    else:
        raise HTTPException(status_code=404, detail="item not found")


def fix_item_id(item):
    item["id_"] = str(item["_id"])
    return item


@todo_router.get("/",response_model=List[ItemOnDB])
async def get_all_items(limit: int = 10):
    """
    Gets all items.
 
    """
  
    items_cursor = DB.item.find()
   
    items = await items_cursor.to_list(length=limit)
    return list(map(fix_item_id, items))



@todo_router.post("/")
async def add_item(item: Item):
    """
    add item
  
    """
    item_op = await DB.item.insert_one(item.dict())

    return {"message": "item succesfully inserted"}



@todo_router.delete("/{id_}",response_model=dict)
async def delete_item_by_id(id_: str):
    """
    Get one item by ID.
   
    """
    item_op = await DB.item.delete_one({"_id": ObjectId(id_)})
    if item_op.deleted_count:
        return {"status": f"deleted count: {item_op.deleted_count}"}


@todo_router.put( "/{id_}", dependencies=[Depends(validate_object_id), Depends(_get_item_or_404)],response_model=ItemOnDB)
async def update_item(id_: str, item_data: Item):
    """
    Update a Item by ID
    """
    item_op = await DB.item.update_one(
        {"_id": ObjectId(id_)}, {"$set": item_data.dict()}
    )
    if item_op.modified_count:
        return await _get_item_or_404(id_)
    else:
        raise HTTPException(status_code=304)
