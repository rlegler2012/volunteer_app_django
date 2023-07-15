from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('professionals/', views.ProfessionalList.as_view(), name="professional_list"),
    path('professionals/new', views.ProfessionalCreate.as_view(), name="professional_create")
]

# path('professionals/<int:pk>/', views.ProfessionalDetail.as_view(), name="professional_detail"),
    # path('professionals/<int:pk>/update',
    #      views.ProfessionalUpdate.as_view(), name="professional_update"),
    # path('professionals/<int:pk>/delete',views.ProfessionalDelete.as_view(), name="professional_delete"),