from django.contrib import admin
from django.urls import path,include
from Bandlabapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', include('Bandlabapp.urls')),
]
