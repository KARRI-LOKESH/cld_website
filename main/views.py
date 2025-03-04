
from django.shortcuts import render

def home(request):
    return render(request, 'main/index.html')

def index(request):
    return render(request, 'main/index.html')

def administration(request):
    return render(request, 'main/administration.html')

def admissions(request):
    return render(request, 'main/admissions.html')

def departments(request):
    return render(request, 'main/departments.html')

def placements(request):
    return render(request, 'main/placements.html')

def research(request):
    return render(request, 'main/research.html')

def amenities(request):
    return render(request, 'main/amenities.html')

def activities(request):
    return render(request, 'main/activities.html')

def contact(request):
    return render(request, 'main/contact.html')
