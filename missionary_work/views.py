from django.shortcuts import render

def home(request):
    """View for the home page"""
    return render(request, 'missionary_work/home.html')

def about(request):
    """View for the about page"""
    return render(request, 'missionary_work/about.html')

def missionary_work(request):
    """View for the missionary work page"""
    return render(request, 'missionary_work/missionary_work.html')

def latest_mission(request):
    """View for the latest mission page"""
    return render(request, 'missionary_work/latest_mission.html')

def media(request):
    """View for the media page"""
    return render(request, 'missionary_work/media.html')

def contact(request):
    """View for the contact page"""
    return render(request, 'missionary_work/contact.html')

# Website Guide Views
def website_guide(request):
    """View for the main website guide page"""
    return render(request, 'missionary_work/website_guide.html')

def website_guide_part1(request):
    """View for website guide part 1: Introduction and Overview"""
    return render(request, 'missionary_work/website_guide_part1.html')

def website_guide_part2(request):
    """View for website guide part 2: Website Features and Pages"""
    return render(request, 'missionary_work/website_guide_part2.html')

def website_guide_part3(request):
    """View for website guide part 3: Media Resources and Involvement"""
    return render(request, 'missionary_work/website_guide_part3.html')

def website_guide_part4(request):
    """View for website guide part 4: Contact Information"""
    return render(request, 'missionary_work/website_guide_part4.html')
