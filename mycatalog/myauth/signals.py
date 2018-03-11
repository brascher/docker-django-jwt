import logging

from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver, Signal
from django.utils import timezone

# Custom Signals
token_created = Signal(providing_args=["request", "user"])
missing_credentials = Signal(providing_args=["request", "user"])
invalid_credentials = Signal(providing_args=["request", "user"])
inactive_user = Signal(providing_args=["request", "user"])
invalid_token = Signal(providing_args=["request"])
missing_user = Signal(providing_args=["request"])

LOGGER_NAME = "myauth"
logger = logging.getLogger(LOGGER_NAME)

@receiver(token_created)
def log_token_created(sender, request, user, **kwargs):

    try:
        user_agent_info = request.META.get("HTTP_USER_AGENT", "unknown")
        msg = "Token issued to {} from {} using {} browser" \
              .format(user.get("email", "unknown"),
                      get_client_ip(request),
                      user_agent_info)
        logger.info(msg)
    except Exception as exc:
        logger.error("log_token_created issue, request: %s, exception: %s" % (request, exc))

@receiver(missing_credentials)
def log_missing_credentials(sender, request, user, **kwargs):

    try:
        user_agent_info = request.META.get("HTTP_USER_AGENT", "unknown")
        msg = "Attempted token request from user {} missing credentials, from {} using {} browser" \
              .format(user.get("email", "unknown"),
                      get_client_ip(request),
                      user_agent_info)
        logger.info(msg)
    except Exception as exc:
        logger.error("log_invalid_credentials issue, request: %s, exception: %s" % (request, exc))

@receiver(invalid_credentials)
def log_invalid_credentials(sender, request, user, **kwargs):
    
    try:
        user_agent_info = request.META.get("HTTP_USER_AGENT", "unknown")
        msg = "Invalid credentials from user {} in token request from {} using {} browser" \
              .format(user.get("email", "unknown"),
                      get_client_ip(request),
                      user_agent_info)
        
        logger.info(msg)
    except Exception as exc:
        logger.error("log_invalid_credentials issue, request: %s, exception: %s" % (request, exc))

@receiver(inactive_user)
def log_inactive_user(sender, request, user, **kwargs):
    
    try:
        user_agent_info = request.META.get("HTTP_USER_AGENT", "unknown")
        msg = "Inactive user {} attempted token request from {} using {} browser" \
              .format(user.get("email", "unknown"),
                      get_client_ip(request),
                      user_agent_info)
        
        logger.info(msg)
    except Exception as exc:
        logger.error("log_invalid_credentials issue, request: %s, exception: %s" % (request, exc))

@receiver(invalid_token)
def log_invalid_token(sender, request, user, **kwargs):
    
    try:
        user_agent_info = request.META.get("HTTP_USER_AGENT", "unknown")
        msg = "Invalid token request from {} using {} browser" \
              .format(get_client_ip(request),
                      user_agent_info)
        
        logger.info(msg)
    except Exception as exc:
        logger.error("log_invalid_token issue, request: %s, exception: %s" % (request, exc))

@receiver(missing_user)
def log_missing_user(sender, request, user, **kwargs):

    try:
        user_agent_info = request.META.get("HTTP_USER_AGENT", "unknown")
        msg = "Invalid token request from missing user, from {} using {} browser" \
              .format(get_client_ip(request),
                      user_agent_info)
        logger.info(msg)
    except Exception as exc:
        logger.error("log_missing_user issue, request: %s, exception: %s" % (request, exc))

def get_client_ip(request):
    """
    Helper function to retrieve IP address from request
    """

    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")

    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0]
    else:
        ip = request.META.get("REMOTE_ADDR")

    return ip