from django.shortcuts import render
from logs.models import HttpRequestsLog, BookChangeLogs
from django.core import serializers


def showlastten(request):
    last_ten = HttpRequestsLog.objects.all().order_by('-id')[:10]

    return render(request, 'logs/showlastten.html', {'last_ten': last_ten})


def showbooklog(request):
    #book_log = BookChangeLogs.objects.all().values().order_by('-id')[:10]
    book_log = serializers.serialize("python", BookChangeLogs.objects.all())

    return render(request, 'logs/showbooklog.html', {'book_log': book_log})
