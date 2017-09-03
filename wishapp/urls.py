from django.conf.urls import url
from . import views

""" URLとViewファンクションの関連付け """
urlpatterns = [
    url(r'^Machinery/$', views.machinery_list, name='machinery_list'),
    url(r'^Machinery/add/$', views.machinery_add, name='machinery_add'),
#    url(r'^$', views.post_list),
]
