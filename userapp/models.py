from django.db import models

# Create your models here.
class user_reg(models .Model):
    Name=models.CharField(max_length=50)
    Email=models.CharField(max_length=50)
    Phone=models.CharField(max_length=50)
    Password=models.CharField(max_length=50)

    def __str__(self):
        return self.Name