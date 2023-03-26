from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

class Category(MPTTModel):
  name = models.CharField(max_length=200, unique=True)
  parent = TreeForeignKey('self', on_delete=models.PROTECT, null=True, blank=True)
  
  
  class MPTTMeta():
    order_insertion_by = ['name']
    verbose_name_plural = 'Categories'
    
  
  def __str__(self):
    return self.name


class Post(models.Model):
  name = models.CharField(max_length=200)
  description = models.TextField(blank=True)
  weight_in_tons = models.IntegerField(blank=True, null=True)
  amount = models.IntegerField(blank=False)
  category = TreeForeignKey('Category', on_delete=models.SET_NULL, null=True)
  location = models.CharField(max_length=200)
  remark = models.TextField(blank=True)
  

  
  def __str__(self):
    return self.name
  