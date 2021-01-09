# -*- coding: utf-8 -*-from __future__ import unicode_literals
from django.shortcuts import render,redirect
from django.http  import HttpResponse
from .models import Image,Category,Location
# Create your views here.

def image(request):
    image = Image.objects.all()
    image_location = Location.objects.all
    return render(request, 'photos.html', {'image': image})
