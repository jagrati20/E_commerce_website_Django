from django.db import models

class Product(models.Model):
    prod_title=models.CharField(max_length=100)
    prod_image=models.ImageField(upload_to='product_img',null=True)
    prod_price=models.DecimalField(decimal_places=2,max_digits=10000)
    prod_category=models.ForeignKey('Category',on_delete=models.CASCADE)
    prod_desc=models.TextField(blank=True,null=True)

    def __self__(self):
        return self

class Category(models.Model):
    category_name=models.CharField(max_length=100)
    category_desc=models.TextField(blank=True,null=True)

    def __self__(self):
        return self