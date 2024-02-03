from django.db import models

# Create your models here.

class MobilePhone(models.Model):

    brand=models.CharField(max_length=100)
    model=models.CharField(max_length=50)
    description=models.TextField()
    price=models.FloatField()
    date_created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.brand

    class Meta:
        ordering=['brand']

class Demo (models.Model):
    photo= models.ImageField()
    file= models.FileField()
