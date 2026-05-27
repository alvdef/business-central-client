from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass, field
from pathlib import Path

DEFAULT_SCOPE = "https://api.businesscentral.dynamics.com/.default"


@dataclass(frozen=True, slots=True)
class BusinessCentralConfig:
    """Configuration for Microsoft Dynamics 365 Business Central API access.

    The default authentication mode uses Microsoft Entra client credentials with
    a PEM certificate/private key, handled by :class:`CertificateTokenProvider`.
    """

    tenant_id: str
    client_id: str
    certificate_path: str | Path | None = None
    certificate_thumbprint: str | None = None
    authority_host: str = "https://login.microsoftonline.com"
    scope: str = DEFAULT_SCOPE
    environment: str = "production"
    api_version: str = "v2.0"
    timeout_seconds: float = 30.0
    default_company_id: str | None = None
    extra_headers: Mapping[str, str] = field(default_factory=dict)

    @property
    def authority(self) -> str:
        return f"{self.authority_host.rstrip('/')}/{self.tenant_id}"

    @property
    def base_url(self) -> str:
        environment = self.environment.strip("/")
        version = self.api_version.strip("/")
        return f"https://api.businesscentral.dynamics.com/{version}/{environment}/api/v2.0"
