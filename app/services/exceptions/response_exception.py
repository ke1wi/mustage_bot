from typing import Any, Dict, List, Optional

from pydantic import BaseModel


class ErrorDetail(BaseModel):
    type: str
    loc: List[str]
    msg: str
    input: Optional[str]
    ctx: Optional[Dict[str, Any]]  # Змінено: ctx може бути словником або None


class ResponseError(BaseModel):
    detail: List[ErrorDetail]


class ResponseException(Exception):
    def __init__(self, detail: List[ErrorDetail]):
        self.detail = detail
        self.message = "; ".join([f"{e.msg} (Input: {e.input})" for e in self.detail])
        super().__init__(self.message)

    @classmethod
    def from_json(cls, error_response) -> "ResponseException":
        response_error = ResponseError.model_validate(error_response)
        return cls(detail=response_error.detail)
