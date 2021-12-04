from django.db import models

# Create your models here.
class Index(models.Model):
    corr=models.CharField(max_length=7)
    neg=models.CharField(max_length=7)
    form1=models.FileField(default='')
    form2=models.FileField(default='')
