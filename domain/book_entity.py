# book_entity.py

from dataclasses import dataclass
from datetime import datetime, date
from typing import Optional

@dataclass
class Book:
    id: Optional[int]
    title: str
    subtitle: Optional[str]
    author: str
    link: Optional[str]
    status: str
    trigger: Optional[str]
    rating: Optional[int]
    completed_date: Optional[date]
    book_type: Optional[str]
    created_at: datetime
    updated_at: datetime
    cover_image: Optional[str]
    memo: Optional[str]
