# 'path' in Django maps a URL pattern to a view function.
from django.urls import path
# from current directory importing views
from . import views

urlpatterns = [
    path('members/', views.members, name='members'),
]