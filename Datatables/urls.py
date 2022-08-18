from django.contrib import admin
from django.urls import path
from App import views   

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('json/', views.inventory_json, name='inventory_json'),
]
