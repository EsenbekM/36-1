from django.contrib import admin

from user.models import Profile, SMSCodes

admin.site.register(Profile)
admin.site.register(SMSCodes)