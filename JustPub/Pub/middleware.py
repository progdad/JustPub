from django.shortcuts import redirect

# Server can be accessed on any of the next urls: "/", "/rest-api/" or "/rest-api/v1/" url,
# but server must redirect users from these urls because there is no UI-implementation for these endpoints.


class RedirectMiddleware:
    def __init__(self, get_response):
        self._get_response = get_response

    def __call__(self, request):
        reqpath = request.path if request.path.endswith("/") else f"{request.path}/"
        if (reqpath == "/") or (reqpath == "/rest-api/") or (reqpath == "/rest-api/v1/"):
            if request.user.is_authenticated:
                return redirect("home-docs")
            return redirect("user_auth")
        return self._get_response(request)
