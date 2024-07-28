from django.urls import path
from. import views

urlpatterns=[
    path('',views.home),
    path('home/',views.home),
    path('about/',views.about),
    path('contactus/',views.contactus),
    path('adminlogin/',views.adminlogin),
    path('courses/',views.course),
    path('placement/',views.placement),
    path('recuiters/',views.recuiter),
    path('registration/',views.registration),
    path('gallery/',views.imagegallery),
    path('faculty/',views.faculty),




]