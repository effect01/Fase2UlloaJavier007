
from django.urls import path
from . import views 

urlpatterns = [
    path('contact/', views.contact, name='Booklary-contact'),
    path('register/', views.register, name='Booklary-register'),
    path('', views.index, name='Booklary-index'),
    path('home/', views.home, name='Booklary-home'),
    path('library/', views.library, name='Booklary-library'),
    path('about/', views.about, name='Booklary-about'),

]
