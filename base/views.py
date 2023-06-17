from django.shortcuts import render

from . import models

# Create your views here.
def home(request, user_id):
    user = models.User.objects.filter(id=user_id).first()
    experiences = models.Experiences.objects.filter(user=user)
    
    context = {
        'user' : user,
        'experiences': experiences
    }
    return render(request, 'base/index.html', context)

def portfolio_details(request):
    
    context = {
        
    }
    
    return render(request, 'base/portfolio-details.html', context)
