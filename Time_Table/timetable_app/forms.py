from django import forms
from .models import TimetableEntry, ClassGroup, Subject, Teacher

DAYS_OF_WEEK = [
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
    ('Saturday', 'Saturday'),
    ('Sunday', 'Sunday'),
]

PERIOD_CHOICES = [(i, f'Period {i}') for i in range(1, 9)]  # 1 to 8

class TimetableEntryForm(forms.ModelForm):
    day = forms.ChoiceField(choices=DAYS_OF_WEEK)
    period = forms.ChoiceField(choices=PERIOD_CHOICES)

    class Meta:
        model = TimetableEntry
        fields = ['class_group', 'subject', 'teacher', 'day', 'period']

class ClassGroupForm(forms.ModelForm):
    class Meta:
        model = ClassGroup
        fields = ['name']

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['name', 'hours_per_week']

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['name', 'subjects']
        widgets = {
            'subjects': forms.CheckboxSelectMultiple
        }