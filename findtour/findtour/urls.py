"""findtour URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

# APP - index
from index.views import index_view
from index.views import private_tour_view
from index.views import private_tour_handler
from index.views import form_test
from index.views import form_test_handler
from index.views import about_view

# APP - sights
from sights.views import sight_detail
from sights.views import sight_list
from sights.views import area_list as sight_area_list
from sights.views import area_detail as sight_area_detail

# APP - map
from map.views import baidu_map
from map.views import gg_map

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    # sights
    url(r'^sights/$', sight_list, name='sight_list'),
    url(r'^sights/(?P<sight_slug>[\w\W]+)$', sight_detail, name='sight_detail'),
    url(r'^area/$', sight_area_list, name='sight_area_list'),
    url(r'^area/(?P<area_name>[\w\W]+)$', sight_area_detail, name='sight_area_detail'),

    # index
    url(r'^$', index_view, name='index'),
    url(r'^about/$', about_view, name='aboutview'),
    url(r'^private_tour/$', private_tour_view, name='privatetour'),
    url(r'^private_tour_handler/$', private_tour_handler, name='privatetourhandler'),
    url(r'^form_test/$', form_test, name='test'),
    url(r'^form_test_handler/$', form_test_handler, name='testhandler'),

    # map
    url(r'^map/baidu$', baidu_map, name='baidu_map'),
    url(r'^map/gg$', gg_map, name='gg_map'),

]
