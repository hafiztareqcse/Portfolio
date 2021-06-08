from django.db import models


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

