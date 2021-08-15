from django.urls import path, include

from . import views

app_name = 'cables'
urlpatterns = [
    path('', views.cab_list, name='cab_list'),
    path('category/<int:pk>', views.cab_list, name='cab_by_category'),

]
