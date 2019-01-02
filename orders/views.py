from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

from .models import Category

# Create your views here.
def index(request):
    return HttpResponse("Project 3: TODO")

# class IndexView(generic.ListView):
#     template_name = 'orders/index.html'
#     context_object_name = 'category_list'
#
#     def get_queryset(self):
#         """Return categories."""
#         return Category.objects.all()
