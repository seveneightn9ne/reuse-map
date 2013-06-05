from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

import emails.views
import mitmap.views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^email_download', emails.views.email_download, name='email_download'),
    url(r'^list_urls', mitmap.views.list_urls, name='list_urls'),

    # Examples:
    # url(r'^$', 'reuse_map.views.home', name='home'),
    # url(r'^reuse_map/', include('reuse_map.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()
