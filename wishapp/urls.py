from django.conf.urls import url
from . import views

""" URLとViewファンクションの関連付け """
urlpatterns = [
    url(r'^Machine/$', views.machine_list, name='machine_list'),
    url(r'^Machine/add/$', views.machine_add, name='machine_add'),
]
