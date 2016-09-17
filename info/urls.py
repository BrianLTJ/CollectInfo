from django.conf.urls import url
from info import views
urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^info/add$', views.add_handler, name='add_handler'),

    url(r'^edit$', views.edit_index, name='edit'),
    url(r'^edit/save$', views.edit_handler, name='edit_handler'),
]
