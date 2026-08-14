#This is Url File 
from django.urls import path
from . import views
urlpatterns=[path('', views.landing_view, name='landing'),
    path('login/', views.login_action, name='login'),
    path('logout/', views.logout_action, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),

]