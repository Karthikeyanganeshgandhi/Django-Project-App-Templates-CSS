from django.urls import path
from . import views

urlpatterns=[
    path('hellopage/',views.hellopage,name='hellopage'),
]