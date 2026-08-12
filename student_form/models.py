from django.db import models

# Create your models here.
class StudentState(models.Model):
    s_name = models.CharField(default='Student',max_length = 255,error_messages='Enter Your Name Again')
    s_topics = models.CharField(null=True,blank=True,default='none',max_length = 255)
    s_mastery = models.FloatField(null=True,blank=True,verbose_name='Mastery')
    s_av_time = models.IntegerField(help_text='Enter Available Time to Study per day(hours)',
        error_messages='Enter Available Time to Study per day(hours)')
