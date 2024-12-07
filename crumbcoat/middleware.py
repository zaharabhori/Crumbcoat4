from django.conf import settings
from django.http import HttpResponseRedirect

class ForceHttpMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if we're in production (not in DEBUG mode)
        if not request.is_secure() and not settings.DEBUG:
            # Redirect to HTTP only if not secure in production
            return HttpResponseRedirect(request.build_absolute_uri(request.get_full_path()).replace("https://", "http://"))
        
        # Otherwise, proceed as usual
        response = self.get_response(request)
        return response
