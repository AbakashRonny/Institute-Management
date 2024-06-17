from django.urls import path
from . import views

urlpatterns=[
    path('base/',views.base),
    path('home/',views.home,name='home'),
    path('course/',views.course,name='course'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('blog/',views.blog,name='blog'),
    path('about/',views.about,name='about')
]