from django.http import HttpResponse


def index(request):
    return HttpResponse('<h1>¡Hola Mundo! Saludos desde Santa Marta.</h1>')


def your_ip(request):
    ip = request.META.get('REMOTE_ADDR')
    return HttpResponse(f'<h1>Hola, tu ip es: {ip}</h1>')