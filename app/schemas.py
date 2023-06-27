from uuid import UUID

from pydantic import BaseModel


class TextEntryBase(BaseModel):
    text: str


class TextEntryCreate(TextEntryBase):
    pass


class TextEntryInDB(TextEntryBase):
    uuid: UUID

    class Config:
        orm_mode = True


class TextEntryUpdate(TextEntryBase):
    pass
