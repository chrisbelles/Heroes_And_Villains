from django.urls import path
from super_types import views


urlpatterns = [
    path('', views.superType_list),
    path('<int:pk>/', views.superType_detail),
]