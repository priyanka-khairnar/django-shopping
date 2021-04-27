from django.db import models

# Create your models here.
class Brands(models.Model):
    brand_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.brand_name


class WebPage(models.Model):
    brand = models.ForeignKey(Brands, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name


class AccessRecord(models.Model):
    webpage = models.ForeignKey(WebPage, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return str(self.date)

