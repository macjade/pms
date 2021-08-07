from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
    path('get-code/<code>', views.GetRX.as_view(), name="code"),
]