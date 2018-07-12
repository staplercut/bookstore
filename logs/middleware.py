from django.utils.deprecation import MiddlewareMixin
from logs.models import HttpRequestsLog
from django.utils import timezone


class HttpRequestsTrackingMiddleware(MiddlewareMixin):

    def pretty_request(self, request):
        headers = ''
        for header, value in request.META.items():
            if not header.startswith('HTTP'):
                continue
            header = '-'.join([h.capitalize() for h in header[5:].lower().split('_')])
            headers += '{}: {}\n'.format(header, value)

        return (
            '{method} HTTP/1.1\n'
            'Content-Length: {content_length}\n'
            'Content-Type: {content_type}\n'
            '{headers}\n'
            '{body}'
        ).format(
            method=request.method,
            content_length=request.META['CONTENT_LENGTH'],
            content_type=request.META['CONTENT_TYPE'],
            headers=headers,
            body=request.body,
        )

    def process_request(self, request):
        user = request.user if request.user.is_authenticated else None
        req = HttpRequestsLog(user=user, http_requests=self.pretty_request(request), date=timezone.now())
        req.save()
        return None
