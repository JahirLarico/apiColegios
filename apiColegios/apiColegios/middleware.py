from django.middleware.csrf import CsrfViewMiddleware

class DisableCSRFMiddleware(CsrfViewMiddleware):
    def process_view(self, request, callback, callback_args, callback_kwargs):
        if request.path.startswith('/admin'):
            return None  # No se aplica la protección CSRF en la ruta de administración
        return super().process_view(request, callback, callback_args, callback_kwargs)
