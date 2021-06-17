from django.urls import path

from . import views


urlpatterns = [
    path('', views.go_to_admin, name='current_datetime'),
]
