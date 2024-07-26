from django.contrib import admin

# Register your models here.

from .models import Profile, Publication, HonersAndAwards, ResearchInterests, Skill, Message

admin.site.register(Profile)
admin.site.register(Publication)
admin.site.register(HonersAndAwards)
admin.site.register(ResearchInterests)
admin.site.register(Skill)
admin.site.register(Message)