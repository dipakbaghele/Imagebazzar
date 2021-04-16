from django.http import HttpResponse
from django.shortcuts import render
from Imagebazzarapp.models import *


def show_design_page(request ):
    cats=Category.objects.all()
    images = Images.objects.all()
    data = {
        'images': images,
        'cats':cats
    }

    return render(request,"design.html", data)


def show_category_page(request,cid):

    cats=Category.objects.all()

    cat=Category.objects.get(pk=cid)
    print(cat)
    images = Images.objects.all()
    data = {
        'images': images,
        'cats':cats
    }

    return render(request,"design.html", data)




"""def design(request):
    return redirect('/design')"""



