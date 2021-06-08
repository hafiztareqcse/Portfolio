from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from MyApp.models import Personal, Skill, Education, Experience, ContactForm, ContactMessage


# Create your views here.
def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = ContactMessage()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE ADDR')
            data.save()
            return HttpResponseRedirect(reverse('MyApp:home'))
    form = ContactForm
    personal = Personal.objects.get(id=1)
    skill = Skill.objects.all()
    education = Education.objects.all()
    experience = Experience.objects.all()
    context = {'personal': personal,
               'skill': skill,
               'education': education,
               'experience': experience,
               'form': form
               }
    return render(request, 'home.html', context)
