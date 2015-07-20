from django.conf.urls import include, url
from django.contrib import admin
admin.autodiscover()

from django.contrib.auth.views import login, logout

from .views import here, math, welcome, index, register
from restaurants.views import menu, list_restaurants, comment


urlpatterns = [
    url('^index/$', index),
    url(r'^accounts/login/$', login),
    url(r'^accounts/logout/$', logout),
    url(r'^accounts/register/$', register),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^here/$', here),
    url(r'^(\d{1,2})/math/(\d{1,2})/$', math),
    url(r'^menu/$', menu),
    url(r'^welcome/$', welcome),
    url(r'^restaurants_list/$', list_restaurants),
    url(r'^comment/(\d{1,5})/$', comment),
]
