from types import TracebackType
from typing import Optional, Type

from httpx import URL, AsyncClient
from pydantic import AnyUrl

from app.settings import settings


class BaseAPI:
    _url: AnyUrl = settings.API_URL
    _path: str = ""
    _base_url: Optional[URL] = None

    def __init__(self) -> None:
        self._session = AsyncClient(base_url=self.base_url)

    @property
    def base_url(self) -> URL:
        if self._base_url is None:
            self._base_url = URL(f"{self._url}")

        return self._base_url

    @property
    def path(self) -> str:
        return self.base_url.path + self._path

    async def __aenter__(self):  # type: ignore
        return self

    async def __aexit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional[TracebackType],
    ) -> None:
        await self.close()

    async def close(self) -> None:
        await self._session.aclose()
