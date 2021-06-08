from django.db import models
from django.forms import ModelForm, TextInput, EmailInput

# Create your models here.

class Personal(models.Model):
    name = models.CharField(max_length=30, blank=True)
    profession = models.CharField(max_length=30, blank=True)
    details = models.CharField(max_length=400, blank=True)
    phone = models.CharField(max_length=10, blank=True)
    email = models.CharField(max_length=30, blank=True)
    image = models.ImageField(blank=True, upload_to='me')
    about_image = models.ImageField(blank=True, upload_to='me')
    facebook = models.CharField(max_length=50, blank=True)
    linkedin = models.CharField(max_length=50, blank=True)
    twitter = models.CharField(max_length=50, blank=True)
    instagram = models.CharField(max_length=50, blank=True)
    github = models.CharField(max_length=50, blank=True)
    youtube = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=30, blank=True)
    experience = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.name


class Education(models.Model):
    degree = models.CharField(max_length=30, blank=True)
    institute = models.CharField(max_length=50, blank=True)
    sector = models.CharField(max_length=50, blank=True)
    started_at = models.CharField(max_length=30, blank=True)
    ended_at = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.degree


class Experience(models.Model):
    role = models.CharField(max_length=50, blank=True)
    company = models.CharField(max_length=50, blank=True)
    describe = models.CharField(max_length=100, blank=True)
    started_at = models.CharField(max_length=30, blank=True)
    ended_at = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.company

class ContactMessage(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Read', 'Read'),
        ('Closed', 'Closed'),
    )
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=50)
    subject = models.CharField(max_length=200, blank=True)
    message = models.TextField()
    status = models.CharField(max_length=40, choices=STATUS, default='New')
    ip = models.CharField(max_length=100, blank=True, null=True)
    note = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ContactForm(ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': TextInput(attrs={'placeholder': 'Your Name'}),
            'email': EmailInput(attrs={'placeholder': 'Your Email'}),
            'subject': TextInput(attrs={'placeholder': 'Subject'}),
            'message': TextInput(attrs={'placeholder': 'Write Message'}),
        }