# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *
from django.conf import settings

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
    (r'^octavo/admin/(.*)', admin.site.root),
    (r'^octavo/$', 'index'),
    (r'^octavo/book/add/$', 'add_book'),
)

urlpatterns += patterns('django.views.static',
    (r'^octavo/media/gfx/(?P<path>.*)$', 'serve', {'document_root': ('%s/%s' % (settings.MEDIA_ROOT, 'gfx'))}),
    (r'^octavo/media/css/(?P<path>.*)$', 'serve', {'document_root': ('%s/%s' % (settings.MEDIA_ROOT, 'css'))}),
    (r'^octavo/media/js/(?P<path>.*)$', 'serve', {'document_root': ('%s/%s' % (settings.MEDIA_ROOT, 'js'))}),
    (r'^octavo/media/data/(?P<path>.*)$', 'serve', {'document_root': ('%s/%s' % (settings.MEDIA_ROOT, 'data'))}),
)
