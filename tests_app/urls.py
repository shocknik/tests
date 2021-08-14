from django.urls import path, include


from . import views

app_name = 'tests_app'
urlpatterns = [
    path('', views.f_list, name='test_list'),
    path('category/<int:pk>', views.f_list, name='test_by_category'),
    path('tests/<int:pk>', views.test_detail, name='test_detail'),
]
