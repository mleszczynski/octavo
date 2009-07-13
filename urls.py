# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from django.conf import settings

from octavo import admin

handler500 = 'octavo.main.views.handler500'
handler404 = 'octavo.main.views.handler404'


urlpatterns = patterns('octavo.main.views',
    (r'^octavo/admin/(.*)', admin.site.root),
    (r'^octavo/$', 'index'),
    (r'^octavo/books/$', 'books'),
    (r'^octavo/book/(?P<book_id>\d+)/$', 'book'), 
    (r'^octavo/book/add/$', 'book_add'),   
)

urlpatterns += patterns('django.views.static',
    (r'^octavo/media/gfx/(?P<path>.*)$', 'serve', {'document_root': ('%s/%s' % (settings.MEDIA_ROOT, 'gfx'))}),
    (r'^octavo/media/css/(?P<path>.*)$', 'serve', {'document_root': ('%s/%s' % (settings.MEDIA_ROOT, 'css'))}),
    (r'^octavo/media/js/(?P<path>.*)$', 'serve', {'document_root': ('%s/%s' % (settings.MEDIA_ROOT, 'js'))}),
    (r'^octavo/media/data/(?P<path>.*)$', 'serve', {'document_root': ('%s/%s' % (settings.MEDIA_ROOT, 'data'))}),
)
