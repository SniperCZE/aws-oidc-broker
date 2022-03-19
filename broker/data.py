from dataclasses import dataclass, field
from typing import Optional


@dataclass
class KeyCloakOpenIdconfig:
    """keycloak openid config"""

    KEYCLOAK_CLIENT_ID: str
    KEYCLOAK_ISSUER: str
    KEYCLOAK_CLIENT_SECRET: Optional[str] = field(default_factory=str)
    APP_SECRET: Optional[str] = field(default_factory=str)
    TITLE: Optional[str] = field(default_factory=str)

    def __post_init__(self):
        if self.KEYCLOAK_ISSUER[-1] == "/":
            self.KEYCLOAK_ISSUER = self.KEYCLOAK_ISSUER[:-1]

        self.KEYCLOAK_WELL_KNOWN = (
            f"{self.KEYCLOAK_ISSUER}/.well-known/openid-configuration"
        )


@dataclass
class AwsManage:
    console: str = field(default_factory=str)
    cli: dict = field(default_factory=dict)
    expired_token: bool = field(default_factory=bool)
