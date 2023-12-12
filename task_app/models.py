from django.db import models

# Create your models here.
class Status(models.TextChoices):
    UNSTARTED='u', "Not yet started"
    ONGOING='o', 'Ongoing'
    FINISHED='f','Finished'

class Task(models.Model):
    name=models.CharField(verbose_name="Task name",max_length=65,unique=True)
    t_date=models.DateField(verbose_name="Date")
    status=models.CharField(verbose_name="Task status", max_length=1,choices=Status.choices) #my status defined under status will come to this

    def __str__(self):
        return self.name