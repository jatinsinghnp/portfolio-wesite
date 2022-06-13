from django.contrib import admin
from .models import PersonalInfo, PersonalDetailInfo, Skill, Education, MyPortFolio,ContactUs,Blog

# Register your models here.

admin.site.register(PersonalInfo)
admin.site.register(PersonalDetailInfo)
admin.site.register(Skill)
admin.site.register(Education)
admin.site.register(MyPortFolio)
admin.site.register(ContactUs)
admin.site.register(Blog)
