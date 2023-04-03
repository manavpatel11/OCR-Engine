from django.shortcuts import render

from django.contrib.auth.decorators import login_required
@login_required(login_url='login')

def home(request):
    value = request.session.get('key', None)
    print(value)
    return render(request,'index.html')


def home2(request):
    value = request.session.get('key', None)
    print(value)
    return render(request,'index.html')