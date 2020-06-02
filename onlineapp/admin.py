from django.contrib import admin

from onlineapp.models import Persons,MembershipsBase,AvailableLanguages,CountryCodes

admin.site.register(Persons)
admin.site.register(MembershipsBase)
admin.site.register(AvailableLanguages)
admin.site.register(CountryCodes)
