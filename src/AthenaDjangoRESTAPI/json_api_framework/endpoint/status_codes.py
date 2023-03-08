# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import enum

# Athena Packages

# Local Imports

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class Information(enum.IntEnum):  #1xx
    CONTINUE = 100
    SWITCH_PROTOCOL = 101

class Successful(enum.IntEnum):  #2xx
    OK = 200
    CREATED = 201
    ACCEPTED = 202
    NO_AUTH_INFO = 203
    NO_CONTENT = 204
    RESET_CONTENT = 205
    PARTIAL_CONTENT = 206

class Redirection(enum.IntEnum):  #3xx
    MULTIPLE_CHOICE = 300
    MOVED_PERMANENTLY = 301
    FOUND = 302
    SEE_OTHER = 303
    NOT_MODIFIED = 304

class ErrorClient(enum.IntEnum):  #4xx
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    NOT_FOUND = 404
    NOT_ALLOWED = 405
    NOT_ACCEPTABLE = 406
    PROXY_AUTH = 407
    REQUEST_TIMEOUT = 408
    CONFLICT = 409
    GONE = 410
    LENGTH_REQUIRED = 411
    PRECONDITION_FAILED = 412
    ENTITY_TOO_LARGE = 413
    URI_TOO_LONG = 414
    UNSUPPORTED_MEDIA = 415
    RANGE_NOT_SATISFIED = 416
    EXCEPTION_FAILED = 417
    TEAPOT = 418

class ErrorServer(enum.IntEnum):  #5xx
    INTERNAL = 500
    NOT_IMPLEMENTED = 501
    BAD_GATEWAY = 502
    SERVICE_UNAVAILABLE = 503
    GATEWAY_TIMEOUT = 504

STATUS_CODES = Information | Successful | Redirection | ErrorClient | ErrorServer