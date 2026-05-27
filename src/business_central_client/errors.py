from __future__ import annotations

from typing import Any


class BusinessCentralAuthError(RuntimeError):
    """Raised when acquiring an access token fails."""


class BusinessCentralAPIError(RuntimeError):
    """Raised when Business Central returns a non-successful HTTP response."""

    def __init__(
        self,
        message: str,
        *,
        status_code: int | None = None,
        response_body: Any = None,
        request_id: str | None = None,
    ) -> None:
        super().__init__(message)
        self.status_code = status_code
        self.response_body = response_body
        self.request_id = request_id
