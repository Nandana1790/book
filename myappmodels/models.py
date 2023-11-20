from django.db import models

# Create your models here.
class Books(models.Model):
    name=models.CharField(max_length=200)
    price=models.PositiveIntegerField()
    author=models.CharField(max_length=200)
    genre=models.CharField(max_length=200)
    cover_pic=models.ImageField(upload_to="images",null=True,blank=True)
    Published_date=models.DateField(null=True,blank=True)


    def __str__(self):
        return self.name
        