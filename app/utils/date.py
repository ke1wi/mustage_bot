from datetime import date, datetime


def parse_date(input_date: str) -> date:
    return datetime.strptime(input_date, "%d.%m.%Y").date()


def check_date(input_date: str) -> str | None:
    try:
        datetime.strptime(input_date, "%d.%m.%Y").date()
        return input_date
    except ValueError:
        return None


def date_for_user(input_date: str) -> str:
    return datetime.strptime(input_date, "%Y-%m-%d").strftime("%d.%m.%Y")
