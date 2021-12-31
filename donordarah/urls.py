from django.urls import path

from donordarah import views

app_name = 'donorpage'

urlpatterns = [
    path('', views.donorPage, name='donorpage'),
    path('layananpage/', views.layananPage, name='layananpage'),
    path('form/', views.formPage, name='form'),
    path('outputform/', views.hasilFormPage, name='outputform'),
    path('json', views.flutter, name= 'json'),
]