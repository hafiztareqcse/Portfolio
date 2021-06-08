from django.shortcuts import render
from MyApp.models import Personal, Skill, Education, Experience


# Create your views here.
def home(request):
    personal = Personal.objects.get(id=1)
    skill = Skill.objects.all()
    education = Education.objects.all()
    experience = Experience.objects.all()
    context = {'personal': personal,
               'skill': skill,
               'education': education,
               'experience': experience,
               }
    return render(request, 'home.html', context)
