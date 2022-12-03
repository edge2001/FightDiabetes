from django.contrib import admin

# Register your models here.
from .models import UserInfo, PatientInfo, datum, Sports_record
admin.site.register(UserInfo)
admin.site.register(PatientInfo)
admin.site.register(datum)
admin.site.register(Sports_record)