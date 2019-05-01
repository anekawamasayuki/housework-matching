from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

from .models import Housework


class IndexView(generic.ListView):
    model = Housework
    template_name = 'housework_matching/index.html'


class DetailView(generic.DetailView):
    model = Housework
    template_name = 'housework_matching/detail.html'


def accept(request, housework_id):
    pass


def done(request, housework_id):
    pass
