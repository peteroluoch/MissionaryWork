from django.shortcuts import render

def home(request):
    """View for the home page"""
    return render(request, 'home.html')

def about(request):
    """View for the about page"""
    return render(request, 'about.html')

def missionary_work(request):
    """View for the missionary work page"""
    return render(request, 'missionary_work.html')

def latest_mission(request):
    """View for the latest mission page"""
    return render(request, 'latest_mission.html')

def media(request):
    """View for the media page"""
    return render(request, 'media.html')

def contact(request):
    """View for the contact page"""
    return render(request, 'contact.html')
