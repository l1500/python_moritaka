from django.urls import path
from . import views


app_name = 'myapp'

urlpatterns = [
    path('/hello', views.hello, name='hello'),
    path('home/', views.home, name='home'),

]