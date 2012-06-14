from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'circ_proj.views.home', name='home'),
    # url(r'^circ_proj/', include('circ_proj.foo.urls')),

    url(r'^accounts/', include('bootstrap_registration.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', include('emprestimo.urls')),

)

urlpatterns += patterns('',
    url(r'', include('test_client.urls')),
)

