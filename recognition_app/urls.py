from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.scanhompage,name="scan"),
    path('/result',views.recogntion,name="recogntion")
]
