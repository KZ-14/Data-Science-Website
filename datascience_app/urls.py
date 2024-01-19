from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('application/', views.application_view, name='app'),
    path('learning/', views.learning_view, name='learning'),
    

]

