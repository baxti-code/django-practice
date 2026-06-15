from django.urls import path
from .views import home, about, contact, user, post

urlpatterns = [
    path('', home, name="home"),
    path('about/', about, name="about"),
    path('contact/', contact, name="contact"),
    path('user/<str:username>/', user, name="user"),
    path('post/<int:pnumber>/', post, name="post")
]