# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic.edit import FormView

from .forms import SignupForm
from django.shortcuts import render

# Create your views here.
class SignupFormView(FormView):
    form_class = SignupForm

    template_name = "signup_form.html"
    success_url = "/thanks/"
