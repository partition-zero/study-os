#This is Url File 
from django.urls import path
from . import views
urlpatterns=[path('form/',views.init_form)
]