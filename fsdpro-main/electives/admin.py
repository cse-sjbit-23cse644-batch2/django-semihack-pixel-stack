from django.contrib import admin
from .models import *
from .models import Result

admin.site.register(Result)
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Question)
admin.site.register(TestResult)
admin.site.register(Eligibility)
admin.site.register(Preference)