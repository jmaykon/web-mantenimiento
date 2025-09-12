from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def dashboard_admin(request):
    return render(request, "adminapp/dashboard_admin.html")