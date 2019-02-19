from django.urls import path

from . import views

# DIFFERENT PATHS
urlpatterns = [
    path('', views.index, name='index'),
    path('music/', views.music, name='index'),

# FOR CHALLENGE
    path('Masego', views.masego, name='index'),
    path('JorjaSmith', views.jorjaSmith, name='index'),
    path('Galimatias', views.galimatias, name='index'),

]