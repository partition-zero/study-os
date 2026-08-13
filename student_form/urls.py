#This is Url File 
from django.urls import path
from . import views
urlpatterns=[path(' ',views.home_page,name='home'),
    path('form/',views.register_student, name='register-student'),
    path('register/', views.register_student, name='register-student'),
    path('<str:pk>/availability/add/', views.add_availability, name='add-availability'),
    path('<str:pk>/schedule/', views.student_schedule, name='student-schedule'),

]