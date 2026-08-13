from enum import unique

from django.db import models

# Create your models here.
week_days=[
    ('MON', 'Monday'),
    ('TUE', 'Tuesday'),
    ('WED', 'Wednesday'),
    ('THU', 'Thursday'),
    ('FRI', 'Friday'),
    ('SAT', 'Saturday'),
    ('SUN', 'Sunday'),
]



class StudentState(models.Model):
    name = models.CharField(default='Student',max_length = 255,primary_key=True)
    topics = models.CharField(null=True,blank=True,default='none',max_length = 255)
    mastery = models.DecimalField(null=True,blank=True,max_digits=5,decimal_places=4)
    av_time = models.IntegerField(default=0)#type:ignore
    join_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.name



class Availability(models.Model):
    student = models.ForeignKey(StudentState, on_delete=models.CASCADE, related_name='availabilities')
    day = models.CharField(max_length=3, choices=week_days)
    hours_free = models.PositiveIntegerField()

    class Meta:
        unique_together = ('student','day')

    def __str__(self):
        return f"{self.student.name} - {self.day} ({self.hours_free}h)"
