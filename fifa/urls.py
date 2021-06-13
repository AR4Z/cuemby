from django.urls import path

from fifa import views


urls = [
    path('team', views.TeamAPIView.as_view(), name='team'),
    path('players', views.PlayerAPIView.as_view(), name='player'),
]
