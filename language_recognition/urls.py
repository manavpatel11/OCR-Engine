from django.contrib import admin
from django.urls import path,include
from . import *
from registration import views
from capture import  views as vs
from homepage import views as hview
from django.contrib.auth.views import LoginView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('homepage.urls'),name = 'homepage'),
    path('scan',include('recognition_app.urls')),
    path('report',include('report.urls'),name='report'),
    path('contact',include('contact.urls'),name='contact'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('homepage',hview.home2,name="home2"),
    path('capture',vs.hm,name='capture'),
    path('save-image/', vs.save_image, name='save_image'),
    path('cimg',vs.cimg,name="cimg"),
    path('matchacc',vs.match_accuracy,name="matchacc")
    # path('history',include('history.urls')),
    # path('history',include('history.urls')),
]
