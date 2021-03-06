from django.http import HttpResponse
from django.shortcuts import render, redirect

# form
from analytics.forms import TestUserForm


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


def test_user(request):
    if request.method == 'POST':
        form = TestUserForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TestUserForm()

    return render(
        request=request,
        template_name='test_user.html',
        context={
            'form': form
        }
    )