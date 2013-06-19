from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

import emails.views
import mitmap.views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # User Facing
    url(r'^map$', 'mitmap.views.map', name='map'),
    url(r'^google_map$', 'mitmap.views.google_map', name='google_map'),

    # API
    url(r'^API/reuse_object$', 'reuse.views.reuse_object', name='reuse_object'),

    # Examples:
    # url(r'^$', 'reuse_map.views.home', name='home'),
    # url(r'^reuse_map/', include('reuse_map.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()
