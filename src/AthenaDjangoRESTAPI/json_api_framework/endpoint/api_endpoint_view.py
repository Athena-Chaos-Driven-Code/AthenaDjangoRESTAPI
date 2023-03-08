# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

# Athena Packages

# Local Imports

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from django.core.handlers.wsgi import HttpRequest
from django.http import JsonResponse
from django.views import View

# Athena Packages

# Local Imports
from sol_lib.json_api_framework.endpoint.api_endpoint import api_endpoint
from sol_lib.json_api_framework.endpoint.prebuilt_json_responses import ENDPOINT_NOT_FOUND

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class ApiEndpointView(View):
    @api_endpoint
    def get(self, request:HttpRequest) -> JsonResponse:
        if request.user.is_authenticated:
            return self.get_authenticated(request)
        else:
            return self.get_anonymous(request)

    def get_authenticated(self, request:HttpRequest) -> JsonResponse:
        return ENDPOINT_NOT_FOUND

    def get_anonymous(self, request:HttpRequest) -> JsonResponse:
        return ENDPOINT_NOT_FOUND