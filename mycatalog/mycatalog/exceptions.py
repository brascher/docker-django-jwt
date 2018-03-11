from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import exception_handler

from myauth.views import LoginView

def mycatalog_exception_handler(exc, context):
    """
    Custom exception handler for MyCatalog apps
    """

    response = exception_handler(exc, context)
    handlers = {
        "MethodNotAllowed": handle_no_method_error,
        "ValidationError": validation_error,
        "DoesNotExist": does_not_exist_error,
    }

    exception_class = exc.__class__.__name__

    if exception_class in handlers:
        return handlers[exception_class](exc, context, response)

    return response


def handle_no_method_error(exc, context, response):
    """
    Handle the MethodNotAllowed exception.
    """

    response.data = {
        "error": "The service you requested is not available"
    }

    return response

def validation_error(exc, context, response):
    """
    Handle the ValidationError exception. If the validation error occurred 
    during Login, we want to update the status to 401.
    """

    if isinstance(context["view"], LoginView):
        response.status_code = status.HTTP_401_UNAUTHORIZED

    response.data = {
        "error": exc.detail
    }

    return response

def does_not_exist_error(exc, context, response):
    """
    Handle the DoesNotExist exception.
    """

    response = Response()
    response.status_code = status.HTTP_404_NOT_FOUND
    response.data = {
        "error": "We cannot find the item you are looking for."
    }

    return response