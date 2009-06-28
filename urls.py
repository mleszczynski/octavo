# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *

from octavo import admin

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

handler500 = 'octavo.main.views.handler500'
handler404 = 'octavo.main.views.handler404'


urlpatterns = patterns('octavo.main.views',
    # Example:
    # (r'^octavo/', include('octavo.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/(.*)', admin.site.root),
    (r'^octavo/$', 'index'),
)
#
#urlpatterns += patterns('',
#   
#    (r'^admin/(.*)', admin.site.root),
#)
