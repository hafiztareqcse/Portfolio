from django.contrib import admin
from MyApp.models import Personal, Skill, Education, Experience
# Register your models here.

admin.site.register(Personal)
admin.site.register(Skill)
admin.site.register(Education)
admin.site.register(Experience)