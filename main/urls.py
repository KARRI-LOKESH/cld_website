from django.urls import path
from . import views
from .views import student_signup, student_login,verify_otp,StudentData,dashboard

urlpatterns = [
    path('home/', views.home, name='home'),
    path('index/', views.index, name='index'),
    path('signup/', student_signup, name='student_signup'),
    path('login/', student_login, name='student_login'),
    path("verify_otp/", verify_otp, name="verify_otp"),
    path('administration/', views.administration, name='administration'),
    path('admissions/', views.admissions, name='admissions'),
    path('departments/', views.departments, name='departments'),
    path('placements/', views.placements, name='placements'),
    path('research/', views.research, name='research'),
    path('amenities/', views.amenities, name='amenities'),
    path('activities/', views.activities, name='activities'),
    path('contact/', views.contact, name='contact'),
    path('studentData/',StudentData.as_view()),
    path('studentData/<int:pk>',StudentData.as_view()),
    path("dashboard/", dashboard, name="dashboard"),
    path("logout/", views.student_logout, name="student_logout"), 
]