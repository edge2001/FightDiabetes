from django.contrib import admin

# Register your models here.
from user.models import UserInfo, datum, PatientInfo,EmailPro
admin.site.register(UserInfo)
admin.site.register(datum)
admin.site.register(PatientInfo)
admin.site.register(EmailPro)