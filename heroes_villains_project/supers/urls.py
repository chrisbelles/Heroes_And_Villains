from django.urls import path
from . import views

urlpatterns = [
    path('', views.super_list),
    path('<int:pk>/', views.super_detail),
]

# from django.contrib import admin
# from django.urls import path, include


# urlpatterns = [
#      path('admin/', admin.site.urls),
#      path('api/supers/', include('supers.urls')),
#  ]
