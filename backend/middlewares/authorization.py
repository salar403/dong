from django.utils.deprecation import MiddlewareMixin
from backend.services.login_manager import validate_token


class CustomAuthorization(MiddlewareMixin):
    def process_request(self, request):
        token = request.COOKIES.get("Bearer", None)
        if not token:
            return
        else:
            session = validate_token(token=token)
            if not session:
                return
            request.admin = session.admin
            request.session_obj = session
