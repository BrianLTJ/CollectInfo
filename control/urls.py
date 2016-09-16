from django.conf.urls import url
from control import views

urlpatterns = [
    url(r'^$', views.list_index, name='index'),
    url(r'^/login$', views.login_index, name='login'),
]

