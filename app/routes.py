from sqlalchemy.orm import Session

from fastapi import APIRouter, Depends, HTTPException
from app.db import get_db
from app.exceptions import ItemNotFound
from app.schemas import TextEntryBase, TextEntryInDB, TextEntryCreate
from app.service import text_entry_service

router = APIRouter(prefix="/text", tags=["text"])


@router.post("/new", response_model=list[TextEntryInDB])
async def create_entry(entries: list[TextEntryCreate], db: Session = Depends(get_db)):
    return text_entry_service.create_all(entries, db)


@router.get("/all", response_model=list[TextEntryInDB])
async def get_all_entries(db: Session = Depends(get_db)):
    return text_entry_service.get_all(db)


@router.get("/{uuid}", response_model=TextEntryInDB)
async def read_entry(uuid: str, db: Session = Depends(get_db)):
    item = text_entry_service.get_one(uuid, db)

    if item is None:
        raise HTTPException(status_code=404, detail="Entry not found")
    return item


@router.get("/{count}", response_model=list[TextEntryInDB])
async def get_entries(count: int, db: Session = Depends(get_db)):
    items = text_entry_service.get_by_count(count, db)
    return items


@router.delete("/{uuid}", status_code=200)
async def delete_entry(uuid: str, db: Session = Depends(get_db)):
    try:
        text_entry_service.delete_by_uuid(uuid, db)
    except ItemNotFound:
        raise HTTPException(status_code=404, detail="Entry not found")
    return True
