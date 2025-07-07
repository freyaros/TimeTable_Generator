from django.contrib import admin
from .models import ClassGroup, Subject, Teacher, TimetableEntry

admin.site.register(ClassGroup)
admin.site.register(Subject)
admin.site.register(Teacher)
admin.site.register(TimetableEntry)
