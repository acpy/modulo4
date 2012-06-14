from django.conf.urls import patterns, include, url

from .views import *

urlpatterns = patterns('',
    # Examples:
    url(r'^$', HomeView.as_view(), name='home'),
    # url(r'^circ_proj/', include('circ_proj.foo.urls')),

)
