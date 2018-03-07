from django.contrib.auth import user_logged_in
from django.dispatch import receiver
from django.utils import timezone

from mycatalog.loggers import MyCatalogLogger

@receiver(user_logged_in)
def log_user_login_success(sender, user, request, **kwargs):
    
    logger = MyCatalogLogger()

    try:
        user_agent_info = request.META.get("HTTP_USER_AGENT", "unknown")
        logger.log_info_msg("%s logged in at %s from %s using %s browser" % (user.email,
                                                                             timezone.now(),
                                                                             get_client_ip(request),
                                                                             user_agent_info))
    except Exception as exc:
        logger.log_error_msg("user_logged_in issue, request: %s, exception: %s" % (request, exc))

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