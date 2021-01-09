# -*- coding: utf-8 -*-from __future__ import unicode_literals
from django.shortcuts import render,redirect
from django.http  import HttpResponse
from .models import Image,Category,Location
# Create your views here.

def image(request):
    image = Image.objects.all()
    image_location = Location.objects.all
    return render(request, 'photos.html', {'image': image})


def search_results(request):
    if 'category' in request.GET and request.GET["category"]:
        category = request.GET.get("category")
        searched_images = Image.search_by_category(category)
        message = f"{category}"
        print('searched.........',searched_images)
        return render(request, 'search.html', {"message": message, "images": searched_images})
    else:
        message = "Sorry! You haven't searched for any image"
        return render(request, 'search.html', {"message": message})


def location(request, location):
    images_by_location = Image.filter_by_location(location)
    print(images)
    return render(request, 'location.html', {'location_images': images_by_location})  