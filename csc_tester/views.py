#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-

# python/django imports


# project imports
from django.template import RequestContext
from django.shortcuts import render_to_response


def home(request, template=None, form=None, model=None, success=None, extra=None):
    """ Function to display memories dashboard  """
    context = {}

    if request.method == 'GET':
        pass

    if request.method == 'POST':
        pass

    return render_to_response(template, context, RequestContext(request))
