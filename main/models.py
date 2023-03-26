from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Item(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    imgLink = models.CharField(max_length=1000)
    name = models.CharField(max_length=100)
    descr = models.TextField()
    price = models.CharField(max_length=50)
    rating = models.DecimalField(decimal_places=1, max_digits=50000)

class Cart(models.Model):
    title = models.CharField(max_length=50)
    imgLink = models.CharField(max_length=1000)
    name = models.CharField(max_length=100)
    descr = models.TextField()
    price = models.CharField(max_length=50)
    rating = models.DecimalField(decimal_places=1, max_digits=50000)


