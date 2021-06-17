from django.contrib import admin

# Register your models here.
from .models import  bhyhospital,vasaihospital,vaccinename,vmain,noti

admin.site.register(bhyhospital)
admin.site.register(vasaihospital)
admin.site.register(vaccinename)
admin.site.register(vmain)
admin.site.register(noti)