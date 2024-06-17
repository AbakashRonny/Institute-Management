from django.urls import path
from . import views

urlpatterns=[
    path('base/',views.base),
    path('home/',views.home,name='home'),
    path('course/',views.course,name='course'),
    path('signup/',views.signup_view,name='signup'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('blog/',views.blog,name='blog'),
    path('about/',views.about,name='about'),
]