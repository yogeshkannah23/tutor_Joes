from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=150,null=False,blank=False)
    image = models.URLField(max_length=300,null=False,blank=False)
    description = models.TextField(max_length=500)
    status = models.BooleanField(default=False,help_text="0-show,1-hidden")
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=150,null=False,blank=False)
    vendor = models.CharField(max_length=150,null=False,blank=False)
    product_image = models.URLField(max_length=300,null=False,blank=False)
    quantity = models.IntegerField(null=False,blank=False)
    original_price = models.FloatField(null=False,blank=False)
    selling_price = models.FloatField(null=False,blank=False)
    description = models.TextField(max_length=500)
    status = models.BooleanField(default=False,help_text="0-show,1-hidden")
    trending = models.BooleanField(default=False,help_text="0-default,1-trending")
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return self.name
