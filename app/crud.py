from app.crud_base import CRUDBase
from app.db import TextEntry
from app.schemas import TextEntryCreate, TextEntryUpdate


class CRUDTextEntry(CRUDBase[TextEntry, TextEntryCreate, TextEntryUpdate]):
    pass


crud_text_entry = CRUDTextEntry(TextEntry)
