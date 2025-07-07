from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.


class ClassGroup(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=100)
    hours_per_week = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    subjects = models.ManyToManyField(Subject, related_name='teachers')

    def __str__(self):
        return self.name

class TimetableEntry(models.Model):
    class_group = models.ForeignKey(ClassGroup, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    day = models.CharField(max_length=10)  
    period = models.PositiveIntegerField() 

    class Meta:
        unique_together = ('teacher', 'day', 'period')  

    def clean(self):
        
        clash = TimetableEntry.objects.filter(
            teacher=self.teacher,
            day=self.day,
            period=self.period
        ).exclude(pk=self.pk)
        if clash.exists():
            raise ValidationError(
                f"Teacher {self.teacher} already has a class at {self.day} period {self.period}."
            )
     
        group_clash = TimetableEntry.objects.filter(
            class_group=self.class_group,
            day=self.day,
            period=self.period
        ).exclude(pk=self.pk)
        if group_clash.exists():
            raise ValidationError(
                f"Class group {self.class_group} already has a lesson at {self.day} period {self.period}."
            )

    def __str__(self):
        return f"{self.class_group} - {self.subject} - {self.teacher} ({self.day} P{self.period})"