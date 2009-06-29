# -*- coding: utf-8 -*-
from django import forms
from django.contrib import admin
from django.conf import settings
from django.utils.translation import ugettext as _


from octavo.main import models as octavo_models


class BookForm(forms.ModelForm):
    
    class Meta:
        model = octavo_models.Book 
        fields = ('name', 'link')
