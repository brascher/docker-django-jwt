from rest_framework.views import exception_handler

def mycatalog_exception_handler(exc, context):
    """
    Custom exception handler for MyCatalog apps
    """

    response = exception_handler(exc, context)
    handlers = {
        "MethodNotAllowed": handle_no_method_error
    }

    exception_class = exc.__class__.__name__

    if exception_class in handlers:
        return handlers[exception_class](exc, context, response)

    return response


def handle_no_method_error(exc, context, response):
    """
    Handle the MethodNotAllowed exception
    """

    response.data = {
        "error": "The service you requested is not available"
    }

    return response
