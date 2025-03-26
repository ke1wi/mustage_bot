from datetime import date as _date
from uuid import UUID

from app.services.base_api import BaseAPI
from app.services.exceptions.response_exception import ResponseException
from app.services.types.expense import (
    DatesResponse,
    ExpenseCreate,
    ExpensesResponse,
    ExpenseTextResponse,
    ExpenseUpdate,
    FileResponse,
)


class ExpenseAPI(BaseAPI):
    _path = "/expenses"

    async def add_expense(self, data: ExpenseCreate) -> ExpenseTextResponse:
        """Додає нову витрату для користувача."""
        response = await self._session.post(
            f"{self._path}", json=data.model_dump(mode="json", by_alias=True)
        )
        json = response.json()
        if response.status_code == 200:
            return ExpenseTextResponse.model_validate(json)
        raise ResponseException.from_json(json)

    async def get_expenses(self, user_id: int) -> ExpensesResponse:
        """Отримує список витрат користувача."""
        response = await self._session.get(f"{self._path}/{user_id}")
        json = response.json()
        if response.status_code == 200:
            return ExpensesResponse.model_validate(json)
        raise ResponseException.from_json(json)

    async def get_expenses_by_date(self, date: _date, user_id: int) -> ExpensesResponse:
        """Отримує витрати за дату."""
        response = await self._session.get(
            f"{self._path}/by_date?date={date}&user_id={user_id}"
        )
        json = response.json()
        if response.status_code == 200:
            return ExpensesResponse.model_validate(json)
        raise ResponseException.from_json(json)

    async def get_report(self, start_date: _date, end_date: _date, user_id: int):
        response = await self._session.get(
            f"{self._path}/get_report",
            params={"start_date": start_date, "end_date": end_date, "user_id": user_id},
        )
        if response.status_code == 200:
            file_content = response.read()
            return FileResponse(filename="expenses_report.xlsx", content=file_content)
        raise ResponseException.from_json(response.json())

    async def update_expense(
        self, expense_id: UUID, data: ExpenseUpdate
    ) -> ExpenseTextResponse:
        """Оновлює витрату за її ID."""
        response = await self._session.put(
            f"{self._path}/{expense_id}",
            json=data.model_dump(mode="json", by_alias=True),
        )
        json = response.json()
        if response.status_code == 200:
            return ExpenseTextResponse.model_validate(json)
        raise ResponseException.from_json(json)

    async def delete_expense(self, expense_id: UUID) -> ExpenseTextResponse:
        """Видаляє витрату за її ID."""
        response = await self._session.delete(f"{self._path}/{expense_id}")
        json = response.json()
        if response.status_code == 200:
            return ExpenseTextResponse.model_validate(json)
        print(json)

    async def get_expenses_dates(self, user_id: int) -> DatesResponse:
        """Отримує всі унікальні дати витрат для користувача."""
        response = await self._session.get(
            f"{self._path}/dates", params={"user_id": user_id}
        )
        json = response.json()
        if response.status_code == 200:
            return DatesResponse.model_validate(json)
        raise ResponseException.from_json(json)
