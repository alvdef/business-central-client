from __future__ import annotations

from pathlib import Path
from typing import Protocol

import msal

from business_central_client.config import BusinessCentralConfig
from business_central_client.errors import BusinessCentralAuthError


class TokenProvider(Protocol):
    """Callable token provider used by the runtime HTTP client."""

    def get_token(self) -> str:
        """Return a bearer token without the ``Bearer`` prefix."""


class StaticTokenProvider:
    """Small test/integration helper for callers that manage OAuth elsewhere."""

    def __init__(self, token: str) -> None:
        self._token = token

    def get_token(self) -> str:
        return self._token


class CertificateTokenProvider:
    """Microsoft Entra client credentials provider backed by a PEM certificate."""

    def __init__(self, config: BusinessCentralConfig) -> None:
        if config.certificate_path is None:
            raise BusinessCentralAuthError("certificate_path is required for certificate auth")
        if not config.certificate_thumbprint:
            raise BusinessCentralAuthError(
                "certificate_thumbprint is required for certificate auth"
            )

        certificate_path = Path(config.certificate_path)
        private_key = certificate_path.read_text(encoding="utf-8")

        self._scope = [config.scope]
        self._client = msal.ConfidentialClientApplication(
            client_id=config.client_id,
            authority=config.authority,
            client_credential={
                "thumbprint": config.certificate_thumbprint,
                "private_key": private_key,
            },
        )

    def get_token(self) -> str:
        result = self._client.acquire_token_silent(self._scope, account=None)
        if not result:
            result = self._client.acquire_token_for_client(scopes=self._scope)

        access_token = result.get("access_token")
        if access_token:
            return access_token

        error = result.get("error_description") or result.get("error") or "unknown auth error"
        raise BusinessCentralAuthError(f"Failed to acquire Business Central token: {error}")
