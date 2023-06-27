from sqlalchemy.orm import Session

from app.db import TextEntry
from app.exceptions import ItemNotFound
from app.schemas import TextEntryBase, TextEntryInDB
from app.crud import crud_text_entry


class TextEntryService:
    @staticmethod
    def create_all(entries: list[TextEntryBase], db: Session):
        res_entries = []
        for entry in entries:
            res_entries.append(crud_text_entry.create(db=db, obj_in=entry))
        return res_entries

    @staticmethod
    def get_all(db: Session) -> list[TextEntry]:
        return crud_text_entry.get_all(db=db)

    @staticmethod
    def get_one(uuid: str, db: Session) -> TextEntry:
        return crud_text_entry.get(db=db, uuid=uuid)

    @staticmethod
    def get_by_count(count: int, db: Session) -> list[TextEntry]:
        items: list[TextEntry] = crud_text_entry.get_multi(db=db, skip=0, limit=count)
        return items

    @staticmethod
    def delete_by_uuid(uuid: str, db: Session) -> TextEntry:
        item = text_entry_service.get_one(uuid, db)
        if item is None:
            raise ItemNotFound
        return crud_text_entry.remove(db=db, uuid=uuid)


text_entry_service = TextEntryService()
