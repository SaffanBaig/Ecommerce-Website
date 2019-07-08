from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page),
    path('about', views.about_page),
    path('contact', views.contact_page),
    path('login', views.login_page),
    path('register',views.register_page)
]