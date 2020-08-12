from django.shortcuts import render
from .models import images
# Create your views here.
def home(request):
    return(render(request, "home.html"))

def gallery(request):
    imgs = images.objects.all().order_by('id')
    return(render(request, "gallery.html", {'imgs':imgs}))

def menu(request):
    return(render(request, "menu.html"))

def aboutus(request):
    return(render(request, "aboutus.html"))

def data_view(request,types):
    imgs = images.objects.all().order_by('id')
    return(render(request, "gallery.html",{'imgs': imgs, 'type':types}))
