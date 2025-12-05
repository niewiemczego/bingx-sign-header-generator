import json
from dataclasses import dataclass, field
from datetime import datetime
from hashlib import sha256
from typing import Any
from uuid import uuid4

DEFAULT_APP_VERSION = "5.3.17"


@dataclass
class BingxSignHeader:
    """
    The `BingxSignHeader` class is a data class that represents the data required to generate the sign header.
    It contains the following attributes:
    - `timestamp`: The timestamp in milliseconds.
    - `trace_id`: The trace ID which is a unique identifier for the request. Basically u can do it with uuid.
    - `device_id`: The device ID which is a unique identifier for the device. Basically u can do it with uuid.
    - `platform_id`: The platform ID which is a unique identifier for the platform. Default value is "30".
    - `app_version`: The version of the application.
    - `request_payload`: The payload of the request.
    """

    timestamp: int = field(default_factory=lambda: int(datetime.now().timestamp() * 1000))
    trace_id: str = field(default_factory=lambda: str(uuid4()))
    device_id: str = field(default_factory=lambda: str(uuid4()))
    platform_id: str = field(default="30")
    app_version: str = field(default=DEFAULT_APP_VERSION)
    request_payload: dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        # Sort the request payload by key to ensure consistent order for the sign header generation
        self.request_payload = dict(sorted(self.request_payload.items()))

    def generate_value(self) -> str:
        encryption_content = self._generate_encryption_content()
        return self._generate_sign(encryption_content)

    def _generate_encryption_content(self) -> str:
        default_base_value = "95d65c73dc5c4370ae9018fb7f2eab69"
        payload_json = json.dumps(self.request_payload, separators=(",", ":"))

        return f"{default_base_value}{self.timestamp}{self.trace_id}{self.device_id}{self.platform_id}{self.app_version}{payload_json}"

    def _generate_sign(self, encryption_content: str) -> str:
        return sha256(encryption_content.encode("utf-8")).hexdigest().upper()
