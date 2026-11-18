from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('projects/', views.projects, name='projects'),
    path('contact/', views.contact, name='contact'),
    path('form/' , views.form , name='form'),  
    path('data/' , views.data , name="data"),
    path('confirm/', views.confirm_person, name='confirm_person'),
    path('update/<int:id>/', views.update_person, name='update_person'),
    path('delete/<int:id>/', views.delete_person, name='delete_person'),
]