from typing import List, Optional
from datetime import date

from pydantic import BaseModel


class CardBase(BaseModel):
    name: str
    stack_id: int
    quality: int
    prev_easiness: float
    prev_interval: int
    prev_repetitions: int
    prev_review_date: date


class CardBaseOptional(BaseModel):
    name: Optional[str]
    stack_id: Optional[int]
    quality: Optional[int]
    prev_easiness: Optional[float]
    prev_interval: Optional[int]
    prev_repetitions: Optional[int]
    prev_review_date: Optional[date]


class CardCreate(CardBase):
    pass


class CardCreateFirstReview(BaseModel):
    name: str
    stack_id: int
    quality: int


class CardOptionalAttrs(CardBaseOptional):
    pass


class CardReview(CardBaseOptional):
    quality: int
    prev_review_date: Optional[date]


class Card(CardBase):
    id: int
    easiness: float
    interval: int
    repetitions: int
    review_date: date

    class Config:
        orm_mode = True
