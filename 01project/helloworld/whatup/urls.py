from django.urls import path

from . import views

urlpatterns = [
    path('', views.frontPageView, name='front'),
]