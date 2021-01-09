# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import cloudinary
from cloudinary.models import CloudinaryField

# Create your models here.
class Image(models.Model):
    name =models.CharField(max_length = 30)
    image_description = models.TextField()
    image_location = models.ForeignKey('Location', on_delete=models.SET_NULL, default = '', null=True)
    image_category = models.ForeignKey('Category', on_delete=models.CASCADE, default='')
    image = CloudinaryField('image')


    def delete_image(self):
        self.save()


    @classmethod
    def search_by_category(cls, image_category):
        images = cls.objects.filter(image_category__category_name__icontains=image_category)
        return images


    def save_image(self):
        self.save()

    def __str__(self):
        return self.name

class Location(models.Model):
    location_name = models.CharField(max_length = 30)

    def __str__(self):
        return self.location_name


    def delete_location_name(self):
        self.delete() 
        
class Category(models.Model):
    category_name = models.CharField(max_length = 30) 

    
    def __str__(self):
        return self.category_name  


    def delete_category_name(self):
        self.delete()         

def update_image(self, Name=None, category=None):
        self.name = Name if Name else self.Name
        self.image_category = category if category else self.image_category 
        self.save()