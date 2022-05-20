from main.cache import cache


class CheckTokenMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if "Authorization" in request.headers and "Bearer" in request.headers["Authorization"]:
            access_token = request.headers["Authorization"].split()[1]
            if cache.exists(access_token):
                request.META["HTTP_AUTHORIZATION"] = "Bearer xyz"
        response = self.get_response(request)
        return response
