from datetime import date
from typing import List, Optional, Union
from uuid import UUID

from app.services.types.base import Base


class ExpenseCreate(Base):
    name: str
    date: date
    amount_uah: float
    user_id: int


class ExpenseItem(ExpenseCreate):
    id: Union[UUID, str]


class ExpensesResponse(Base):
    expenses: List[ExpenseItem]


class DatesResponse(Base):
    dates: List[str]


class FileResponse(Base):
    filename: str
    content: Optional[bytes] = None


class ExpenseUpdate(Base):
    name: Optional[str]
    date: Optional[date]
    amount_uah: Optional[float]


class ExpenseTextResponse(Base):
    message: str
    expense_id: Optional[str] = None
