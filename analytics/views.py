from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(
        request=request,
        template_name='index.html'
    )


def your_ip(request):
    ip = request.META.get('REMOTE_ADDR')
    return render(
        request=request,
        template_name='ip.html',
        context={
            'ip_view': ip
        }
    )