from django.contrib import admin

from onlineapp.models import Persons,MembershipsBase,AvailableLanguages

admin.site.register(Persons)
admin.site.register(MembershipsBase)
admin.site.register(AvailableLanguages)
