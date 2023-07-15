from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('professionals/', views.ProfessionalList.as_view(), name="professional_list"),
    path('locations/', views.LocationList.as_view(), name="location_list")
]


