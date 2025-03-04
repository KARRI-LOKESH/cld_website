from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('', views.index, name='index'),
    path('administration/', views.administration, name='administration'),
    path('admissions/', views.admissions, name='admissions'),
    path('departments/', views.departments, name='departments'),
    path('placements/', views.placements, name='placements'),
    path('research/', views.research, name='research'),
    path('amenities/', views.amenities, name='amenities'),
    path('activities/', views.activities, name='activities'),
    path('contact/', views.contact, name='contact'),
]