from fastapi import APIRouter
from schemas import ItemCreate, ItemResponse

router = APIRouter(
    prefix="/items",
    tags=["items"]
)

fake_db = []

@router.get("/", response_model=list[ItemResponse])
def get_items():
    return fake_db

@router.post("/", response_model=ItemResponse)
def create_item(item: ItemCreate):
    new_item = item.dict()
    new_item["id"] = len(fake_db) + 1
    fake_db.append(new_item)
    return new_item

