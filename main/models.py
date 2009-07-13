# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Book(models.Model):
    
    ORDER_IN_PROGRESS = 1
    IN_REVIEW = 2
    WAITING_FOR_RETURN = 3
    AVAILABLE = 4
    RESERVED = 5
    ON_LOAN = 6
    UNAVAILABLE = 7
    
    BOOK_STATUSES = (
        (ORDER_IN_PROGRESS, _(u'realizacja zamówienia')),
        (IN_REVIEW, _(u'u recenzenta')),
        (WAITING_FOR_RETURN, _(u'oczekiwanie na zwrot')),
        (AVAILABLE, _(u'na półce')),
        (RESERVED, _(u'oczekiwanie na odbiór')),
        (ON_LOAN, _(u'wypożyczona')),
        (UNAVAILABLE, _(u'niedostępna')),
    )
    
    name = models.CharField(max_length=128, verbose_name=_('name'))
    link = models.URLField(verbose_name=_('link to book'), help_text=_('must be from manning.com'))
    status = models.PositiveSmallIntegerField(verbose_name=_('status'), choices=BOOK_STATUSES, default=1, help_text=_('book status'))
    creation_date = models.DateTimeField(verbose_name=_('creation date'), auto_now_add=True)
    
    def __unicode__(self):
        return self.name
