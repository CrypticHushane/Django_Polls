from django.contrib import admin
from .models import Choice, Profile, Question

# Register your models here.
admin.site.register(Profile)
admin.site.register(Question)
admin.site.register(Choice)