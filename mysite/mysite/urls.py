from django.conf.urls import include, url
from django.contrib import admin
admin.autodiscover()

from django.contrib.auth.views import login, logout

from . import views
import restaurants.views


urlpatterns = [
    url(r'^accounts/login/$', login),
    url(r'^accounts/logout/$', logout),
    url(r'^admin/', include(admin.site.urls)),

    url('^index/$', views.index),
    url(r'^accounts/register/$', views.register),
    url(r'^here/$', views.HereView.as_view()),
    url(r'^(\d{1,2})/math/(\d{1,2})/$', views.math),
    url(r'^welcome/$', views.welcome),

    url(r'^menu/$', restaurants.views.menu),
    url(r'^restaurants_list/$', restaurants.views.list_restaurants),
    url(r'^comment/(\d{1,5})/$', restaurants.views.comment),
]
