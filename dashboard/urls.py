from django.urls import path
from . import views

app_name = "dashboard"

urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
    path('addrx/', views.AddRxView.as_view(), name="add-rx"),
]