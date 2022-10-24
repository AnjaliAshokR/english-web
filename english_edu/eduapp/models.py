from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='product', blank=True)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    stock=models.IntegerField()
    available=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}'.format(self.name)