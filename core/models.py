from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length = 50, )
    mobile = models.CharField(max_length = 15, null=True,blank=True)

    def __str__(self):
        return self.name