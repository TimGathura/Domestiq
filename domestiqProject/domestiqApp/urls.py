# domestiqApp/urls.py
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    #Absolute paths/urls to each template/html file
    path('', views.index, name='index'),
    path('client_signup/', views.client_signup, name='client_signup'),
    path('worker_signup/', views.worker_signup, name='worker_signup'),
    # Log out
    path('logout/', views.log_out, name='logout'),
    path('login/', views.log_in, name='login'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('search/', views.search, name='search'),
    path('contact/', views.contact, name='contact'),
    path('success/', views.success, name='success'),
    path('client_dash/', views.clientdash, name='client_dash'),
    path('worker_dash/', views.workerdash, name='worker_dash'),
    path('admin_dash/', views.admindash, name='admin_dash'),

    #Registration forms urls pointing to view functions
    # path('client_signup2/', views.client_registration, name='client_registration'),
    # path('worker_signup2/', views.worker_registration, name='worker_registration'),

    #Query URLs
    # path('client_dash/', views.client_name, name='client_name'),
    # Add other app-specific URLs as needed




]
