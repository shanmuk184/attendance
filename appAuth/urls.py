from django.conf.urls import url
from .views import register, loginView, logoutView, HelloView
urlpatterns = [
    url(r'^login', loginView, name='login'),
    url(r'^register', register, name='register'),
    url(r'^logout', logoutView, name='logout'),
    url(r'^hello', HelloView, name='hello')
]