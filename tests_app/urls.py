from django.urls import path


from . import views

app_name = 'tests_app'
urlpatterns = [
    path('', views.f_list, name='test_list'),
    path('<int:pk>/', views.f_list, name='test_by_category')
]
