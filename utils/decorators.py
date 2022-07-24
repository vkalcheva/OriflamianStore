from functools import wraps

from flask import request
from werkzeug.exceptions import BadRequest, Forbidden

from managers.auth import auth


def validate_schema(schema_name):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            schema = schema_name()
            errors = schema.validate(request.get_json())
            if errors:
                raise BadRequest(f"Invalid fields {errors}")
            return f(*args, **kwargs)
        return decorated_function
    return decorator


def permission_required(permission):
    def wrapper(func):
        def decorated_func(*args, **kwargs):
            user = auth.current_user()
            if not user.role == permission:
                raise Forbidden("You do not have access to this resource")
            return func(*args, **kwargs)
        return decorated_func
    return wrapper
