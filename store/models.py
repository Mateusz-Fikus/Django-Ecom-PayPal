from django.db import models



class Items(models.Model):
    name = models.CharField(max_length=20, null=False, blank=False)
    desc = models.TextField()
    price = models.IntegerField(null=False, blank=False)
    stock = models.IntegerField(null=False, blank=False)
    image = models.ImageField(upload_to="product_pictures")
