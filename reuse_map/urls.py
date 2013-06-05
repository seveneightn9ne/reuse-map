from django.conf.urls import patterns, include, url
import emails.views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^email_download', emails.views.email_download, name='email_download')

    # Examples:
    # url(r'^$', 'reuse_map.views.home', name='home'),
    # url(r'^reuse_map/', include('reuse_map.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
