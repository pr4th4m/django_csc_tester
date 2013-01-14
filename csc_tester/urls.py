#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-

# django imports
from django.conf.urls import patterns, include, url

# project imports

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

# initial params for views
home_dict = {
    'template': 'csc/base.html',
    'form': '',
    'model': '',
    'success': '',
    'extra': ''
}

urlpatterns = patterns('',
                       # Examples:
                       url(r'^$', 'django_csc_tester.views.home', home_dict, name='home'),

                       # Uncomment the admin/doc line below to enable admin documentation:
                       url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

                       # Uncomment the next line to enable the admin:
                       url(r'^admin/', include(admin.site.urls)),
                       )
