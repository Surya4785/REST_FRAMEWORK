from django.shortcuts import render

def home_view(request):
    return render(request, 'base.html')

def frontend_view(request):
    return render(request, 'frontend.html')