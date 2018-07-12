from django.db import models
from django.conf import settings

# Create your models here.


class HttpRequestsLog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    http_requests = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.http_requests


class BookChangeLogs(models.Model):
    model_id = models.BigIntegerField(null=False, blank=True)
    field = models.CharField(max_length=16, null=False, blank=True)
    data = models.TextField(null=False, blank=True)
    action = models.CharField(max_length=16, null=False, blank=True)  # saved or deleted
    timestamp = models.DateTimeField(null=False, blank=True)

    # def __str__(self):
    #     return 'id: %s\n field: %s\n data: %s\n action: %s\n timestamp: %s' % (self.model_id, self.field, self.data, self.action, self.timestamp)