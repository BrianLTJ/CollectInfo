from django.conf.urls import url
from info import views
urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^info/add$', views.add_handler, name='add_handler'),
]
