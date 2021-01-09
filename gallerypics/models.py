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
