from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('about/', views.about, name = 'about'),
    path('searchresults/', views.searchresults, name = 'searchresults'),
    path('privacy/', views.privacy, name = 'privacy'),
]