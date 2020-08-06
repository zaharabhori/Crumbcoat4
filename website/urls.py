from django.urls import path, re_path
from . import views

urlpatterns =[
    path('', views.home,name='home'),
    path('menu', views.menu, name='menu'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('gallery', views.gallery, name='gallery'),
    re_path('^filter-gallery/(?P<types>[a-z]+)?',views.data_view,name="filter-gallery"),

]