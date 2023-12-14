from django.http import HttpResponse
from django.conf import settings
import traceback
import requests
from django.conf import settings

TELEGRAM_ERROR_LOG_URL = "https://api.telegram.org/5140507968:AAF1KS9oSe92-LkKM1o67C2EZ20H5eM7ET0/sendMessage?chat_id=<CHAT_ID>&text="

class ErrorHandlerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
        if not settings.DEBUG:
            if exception:
                # Format your message here
                message = "{url}\n\n{error}\n\n````{tb}````".format(
                    url=request.build_absolute_uri(),
                    error=repr(exception),
                    tb=traceback.format_exc(),
                )
                # Do now whatever with this message
                try:
                    requests.post(settings.TELEGRAM_ERROR_LOG_URL + message[:4000])
                except:
                    pass
            raise exception
