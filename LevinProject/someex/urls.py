from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('FAQ', views.FAQ, name='FAQ'),
    path('Emperor', views.Emperor, name='Emperor'),
    path('Vader', views.Vader, name='Vader'),
    path('Tarkin', views.Tarkin, name='Tarkin'),

]
