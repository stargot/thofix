from django.urls import path
from thoughts import views

urlpatterns = [
    path('', views.ThoughtsList.as_view(), name="main"),
    path('add/', views.AddThought.as_view()),
]
