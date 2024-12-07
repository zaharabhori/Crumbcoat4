from django.shortcuts import render
from website.storage_backends import S3PrivateMediaStorage

#from .models import images
# Create your views here.
def home(request):
    return(render(request, "home.html"))

def gallery(request):
    #imgs = images.objects.all().order_by('id')
    storage = S3PrivateMediaStorage()
    file_name = 'pics/cake21.jpg'
    signed_url = storage.get_s3_signed_url(file_name)
    return(render(request, "gallery.html", {'signed_url': signed_url}))
    #return(render(request, "aboutus.html")) #temporarily 

def menu(request):
    return(render(request, "menu.html"))

def aboutus(request):
    return(render(request, "aboutus.html"))

def data_view(request,types):
    #imgs = images.objects.all().order_by('id')
    #return(render(request, "gallery.html",{'imgs': imgs, 'type':types}))
    return(render(request, "aboutus.html")) #temporarily 
