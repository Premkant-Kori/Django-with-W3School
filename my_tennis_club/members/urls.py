# 'path' in Django maps a URL pattern to a view function.
from django.urls import path
# from current directory importing views
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('members/', views.members, name='members'),
    path('members/details/<int:id>', views.details, name='details'),
    path('testing/', views.testing, name='testing'),  
]