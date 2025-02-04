from django.db import models

# Create your models here.

JOB_TYPE = (
    ('full time','full time'),
    ('part time','part time'),
)

class Job(models.Model):
    title = models.CharField(max_length=100)
    #location
    job_type = models.CharField(max_length=30 , choices=JOB_TYPE)
    description = models.TextField(max_length=1000)
    published_at = models.DateField(auto_now=True)