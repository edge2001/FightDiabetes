from django.contrib import admin

# Register your models here.
from user.models import UserInfo, datum, PatientInfo
admin.site.register(UserInfo)
admin.site.register(datum)
admin.site.register(PatientInfo)
