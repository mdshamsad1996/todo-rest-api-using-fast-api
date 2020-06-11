from pydantic import BaseModel

class Item(BaseModel):
    item_id: int
    item_name: str
    description: str = None

class ItemOnDB(Item):
    """[summary]
    Actual model used at DB level
    [description]
    Extends:
        PetBase
    Adds `_id` field.
    Variables:
        id_: str {[ObjectId]} -- [id at DB]
    """
    id_: str