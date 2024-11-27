from django.shortcuts import render

def home(request):
    return render(request, "home.html")

def download(request):
    return render(request, "download.html")