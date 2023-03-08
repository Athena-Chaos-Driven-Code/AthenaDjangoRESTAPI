# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any

# Athena Packages

# Local Imports
from sol_lib.json_api_framework.endpoint.status_codes import STATUS_CODES, ErrorServer

# ----------------------------------------------------------------------------------------------------------------------
# - Support Code -
# ----------------------------------------------------------------------------------------------------------------------
RESULT = "result"
ERRORS = "errors"

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
@dataclass(slots=True)
class ApiResponse:
    result:Any = None
    errors:list = field(default_factory=list)
    status:STATUS_CODES = ErrorServer.INTERNAL

    def to_dict(self) -> dict:
        data = {RESULT: self.result,}
        if self.errors:
            data[ERRORS] = self.errors

        return data
