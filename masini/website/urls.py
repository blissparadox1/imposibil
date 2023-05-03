
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home , name="home"),
    path('car-list-fullWidth.html', views.list1 , name="list"),
    path('contact.html', views.contact , name="contact"),
]
