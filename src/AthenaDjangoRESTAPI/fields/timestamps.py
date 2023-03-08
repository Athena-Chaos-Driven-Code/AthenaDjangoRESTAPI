# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import re
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy

# Athena Packages

# Local Imports

# ----------------------------------------------------------------------------------------------------------------------
# - Support Code -
# ----------------------------------------------------------------------------------------------------------------------
re_timestamp:re.Pattern = re.compile(
    r"^((\d{4,})|(-\d{4,})|(\+0000))-((0[0-9])|(1[0-2]))-([0-2][0-9]|3[0-1])(T(([0-1][0-9])|(2[0-4])):([0-5][0-9]):([0-5][0-9]))?$"
)
re_duration:re.Pattern = re.compile(
    r"^P(\d+Y)?((1[0-2]|[1-9])M)?((3[01]|[12][0-9]|[1-9])D)?(T(((2[0-4]|1[0-9]|[1-9])H)?)((([1-5]?[0-9])M)?)((([1-5]?[0-9])S)?))?$"
)

def validate_timestamp(value:str) -> None:
    """
    Validates the inserted argument as a timestamp
    Raises a ValidationError if the value doesn't adhere to the ISO 8601 format
    """
    if isinstance(value, str) and re_timestamp.match(value):
        return None

    raise ValidationError(gettext_lazy(f'{value} is not able to be defined as a timestamp in the ISO 8601 format'))

def validate_duration(value:str) -> None:
    """
    Validates the inserted argument as a duration
    Raises a ValidationError if the value doesn't adhere to the ISO 8601 format
    """
    if isinstance(value, str) and re_duration.match(value):
        return None

    raise ValidationError(gettext_lazy(f'{value} is not able to be defined as a duration in the ISO 8601 format'))

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class ISO8601_Timestamp(models.CharField):
    empty_strings_allowed = False
    default_validators = [validate_timestamp]

class ISO8601_Duration(models.CharField):
    empty_strings_allowed = False
    default_validators = [validate_duration]