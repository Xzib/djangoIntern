from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView, LogoutView
from django.views import View


# Create your views here.
class CustomLoginView(LoginView):
    template_name = 'registration/login.html'


class HomeView(View):
    def get(self, request):
        user = request.user
        return render(request, "dashboard/home.html",{'user':user})
    
class DashboardView(View):
    def get(self, request):
        user= request.user
        return render(request, "backend/dashboard.html", {'user':user})
