from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_login, name='login'),   # login page
    path('home/', views.course_list, name='home'),
    path('course/<int:course_id>/', views.course_detail, name='course_detail'),
    path('test/<int:course_id>/', views.take_test, name='take_test'),
]