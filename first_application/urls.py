from django.urls import path
from.import views

urlpatterns = [
    #path('view',views.app),
    path('', views.app_new, name='index'),
    path('home', views.home, name= "home"),
    path('about', views.about, name= "about"),
    path('contact',views.contact, name="contact"),
    path('form', views.form, name="form"),
    path('list1', views.list1, name="list1"),
    path('edit/<pk>', views.edit_item, name='edit'),           #PK it creates id
    path('delete/<pk>', views.delete_item, name='delete'),
    
]