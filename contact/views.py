from django.shortcuts import render

# from django.contrib.auth.models import User,auth
# from django.contrib import messages
# from django.contrib.auth.decorators import login_required
# @login_required(login_url='login')
def contactpage(request):
    return render(request,'contact.html')
