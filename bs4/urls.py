from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('aboutus/',views.aboutus,name='aboutus'),
    path('test/',views.test,name='test'),
    path('contactus/',views.contactus,name='contactus')

]