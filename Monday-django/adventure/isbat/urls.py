from django.urls import path
from isbat import views
from isbat.views import indexpage

urlpatterns=[
    path('',views.indexpage,name='home'),
    path('signup',views.usersignup),
]