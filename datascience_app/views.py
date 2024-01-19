from django.shortcuts import redirect, render


def home(request):
    return render(request, 'index.html')

def dashboard_view(request):
    return render(request, 'dashboard.html')

def application_view(request):
    return render(request, 'applications.html')

def learning_view(request):
    return render(request, 'learning.html')
