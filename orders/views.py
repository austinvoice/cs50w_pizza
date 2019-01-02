from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

from .models import Category, Type

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'orders/index.html'

    def get_queryset(self):
        """Return the full set of categories"""
        return Category.objects.all()

class DetailView(generic.DetailView):
    template_name = 'orders/detail.html'

    def get_queryset(self):
        """Return the full set of categories"""
        return Category.objects.all()

class ResultsView(generic.DetailView):
    template_name = 'orders/results.html'

    def get_queryset(self):
        """Return the full set of categories"""
        return Category.objects.all()


# def detail(request, category_id):
#     try:
#         category = Category.objects.get(pk=category_id)
#     except Category.DoesNotExist:
#         raise Http404("Category does not exist.")
#     return render(request, 'orders/detail.html', {category': category})


# def index(request):
#     return HttpResponse("Project 3: TODO")

# class IndexView(generic.ListView):
#     template_name = 'orders/index.html'
#     context_object_name = 'category_list'
#
#     def get_queryset(self):
#         """Return categories."""
#         return Category.objects.all()
