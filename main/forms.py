# -*- coding: utf-8 -*-
from django import forms
from django.contrib import admin
from django.conf import settings
from django.utils.translation import ugettext as _


from octavo.main import models as octavo_models

class BookAdminForm(forms.ModelForm):
    
    def clean_link(self):
        if self.cleaned_data['link']:
            link = self.cleaned_data['link']
            if link.find('manning.com') == -1:
                raise forms.ValidationError, _('Link is not from manning.com')
        return self.cleaned_data['link']
    
    def clean(self):
        return self.cleaned_data
    
class BookAdmin(admin.ModelAdmin):
    form = BookAdminForm
    list_display = (
        'name', 'status',  
    )    
    list_filter = ('status',)
    search_fields = ('name',)
    list_per_page = 2


class BookAddForm(forms.ModelForm):
    
    class Meta:
        model = octavo_models.Book 
        fields = ('name', 'link')
