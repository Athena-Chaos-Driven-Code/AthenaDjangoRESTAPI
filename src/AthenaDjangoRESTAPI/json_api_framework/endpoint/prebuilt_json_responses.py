# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from django.http import JsonResponse

# Athena Packages

# Local Imports
from sol_lib.json_api_framework.endpoint.api_response import ApiResponse
from sol_lib.json_api_framework.endpoint.status_codes import ErrorServer, ErrorClient

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
BAD_REQUEST: JsonResponse = JsonResponse(
    (response := ApiResponse(errors=["Bad Request"], status=ErrorClient.BAD_REQUEST)).to_dict(),
    status=response.status
)
ENDPOINT_NOT_FOUND: JsonResponse = JsonResponse(
    (response := ApiResponse(errors=["Endpoint Not Found"], status=ErrorClient.NOT_FOUND)).to_dict(),
    status=response.status
)
NOT_ACCEPTABLE_JSON: JsonResponse = JsonResponse(
    (response := ApiResponse(errors=["JSON was not in acceptable format"], status=ErrorClient.NOT_ACCEPTABLE)).to_dict(),
    status=response.status
)

SERVER_ERROR: JsonResponse = JsonResponse(
    (response := ApiResponse(errors=["Internal Server Error"], status=ErrorServer.INTERNAL)).to_dict(),
    status=response.status
)

