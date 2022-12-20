from django.contrib import admin

# Register your models here.
from user.models import UserInfo, datum, PatientInfo,EmailPro,Sports_record,Medicine_record
admin.site.register(UserInfo)
admin.site.register(datum)
admin.site.register(PatientInfo)
admin.site.register(EmailPro)
admin.site.register(Sports_record)
admin.site.register(Medicine_record)
