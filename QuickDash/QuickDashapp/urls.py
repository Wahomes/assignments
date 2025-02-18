from django.contrib import admin
from django.urls import path,include
from QuickDashapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('QuickDashapp.urls')),
]