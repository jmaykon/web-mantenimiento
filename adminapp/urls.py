from django.urls import path
from . import views


app_name = "adminapp"   # 👈 necesario para usar adminapp:dashboard_admin


urlpatterns = [
    path("dashboard/", views.dashboard_admin, name="dashboard_admin"),  # 👈 este name
]

