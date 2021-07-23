from django.urls import path

from . import views

app_name = 'tests_app'
urlpatterns = [
    path('', views.test_list, name='test_list'),
]