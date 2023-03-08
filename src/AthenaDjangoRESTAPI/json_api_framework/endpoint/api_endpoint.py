# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from django.db import transaction
from django.http import JsonResponse, HttpRequest
from django.views import View
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from typing import Callable
import functools
from django.core import exceptions as DjangoExceptions

# Athena Packages

# Local Imports
from sol_lib.json_api_framework.endpoint.prebuilt_json_responses import BAD_REQUEST, SERVER_ERROR
from sol_lib.json_api_framework.endpoint.api_response import ApiResponse

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
def api_endpoint(fnc:Callable):
    @functools.wraps(fnc)
    def wrapper(obj:View, request:HttpRequest, *args, **kwargs) -> JsonResponse:
        try:
            with transaction.atomic():
                # Authenticate user
                user:User = authenticate(
                    request=request,
                    username=request.headers["username"],
                    password=request.headers["password"]
                )

                print(user.get_all_permissions(), "---------------------------------")

                # Execute function
                result = fnc(obj, request, *args, **kwargs)

                #
                match result:
                    case ApiResponse():
                        return result.to_dict()

                    case JsonResponse():
                        return result

                    case _:
                        return SERVER_ERROR

        except DjangoExceptions.ValidationError:
            return BAD_REQUEST

        except DjangoExceptions.ObjectDoesNotExist:
            return BAD_REQUEST

    return wrapper