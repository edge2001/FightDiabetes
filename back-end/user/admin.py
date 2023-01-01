from django.contrib import admin
# Register your models here.
from user.models import (EmailPro, Medicine_record, PatientInfo, Sports_record,
                         UserInfo, datum)

admin.site.register(UserInfo)
admin.site.register(datum)
admin.site.register(PatientInfo)
admin.site.register(EmailPro)
admin.site.register(Sports_record)
admin.site.register(Medicine_record)
