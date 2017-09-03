from django.conf.urls import url
from . import views

""" URLとViewファンクションの関連付け """
urlpatterns = [
    url(r'^machine_list/$', views.machine_list, name='machine_list'),
    url(r'^machine/add/$', views.machine_add, name='machine_add'),
    url(r'^machine/edit/$', views.machine_edit, name='machine_edit'),
    url(r'^machine/delete/$', views.machine_delete, name='machine_delete'),
    url(r'^borrowed_list/$', views.borrowed_list, name='borrowed_list'),
    url(r'^borrowed/add/$', views.borrowed_add, name='borrowed_add'),
]
