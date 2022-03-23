from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name='home'),
    path('about',views.about, name='about'),
    path('blogs',views.blogs, name='blogs'),
    path('contact',views.contact, name='contact'),
]
