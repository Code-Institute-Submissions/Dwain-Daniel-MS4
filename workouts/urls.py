from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_workouts, name='workouts'),
    path('<int:workouts_id>/', views.workouts_detail, name='workouts_detail'),
    path('add/', views.add_workouts, name='add_workouts'),
]
