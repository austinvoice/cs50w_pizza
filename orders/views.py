from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

from .models import Category, Type

# Create your views here.

def index(request):
    # Create list of categories for home page orders
    category_list = Category.objects.order_by('-pk').reverse()[:8]
    context = {'category_list': category_list}
    return render(request, 'orders/index.html', context)

def detail(request, category_id):
    try:
        category=Category.objects.get(pk=category_id)
    except Category.DoesNotExist:
        raise Http404("Category does not exist.")
    return render(request, 'orders/detail.html', {'category': category})

def order(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    try:
        selected_type = category.type_set.get(pk=request.POST['type'])
    except (KeyError, Type.DoesNotExist):
        # Redisplay the order form.
        return render(request, 'orders/detail.html', {
            'category': category,
            'error_message': "You didn't select a choice.",
            })
    else:
        selected_type.orders += 1
        selected_type.save()
        # Return HttpResponseRedirect after POST data to keep
        # from posting twice.
        return HttpResponseRedirect(reverse('results', args=(category.id,)))

# def detail(request, category_id):
#     category = get_object_or_404(Category, pk=category_id)
#     return render(request, 'orders/detail.html', {'category': category})

def results(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    return render(request, 'orders/results.html', {'category': category})


# class IndexView(generic.ListView):
#     template_name = 'orders/index.html'
#     context_object_name = 'category_list'
#
#     def get_queryset(self):
#         """Return the full set of categories"""
#         return Category.objects.order_by('-pk').reverse()[:8]
#         # category_list = Category.objects.all()
#         # output = ', '.join([q.category_text for q in category_list])
#         # return HttpResponse(output)
#
# class DetailView(generic.DetailView):
#     model = Category
#     template_name = 'orders/detail.html'
#
# class ResultsView(generic.DetailView):
#     model = Category
#     template_name = 'orders/results.html'

# Raise 404 if page does not exist

# # TODO:
    # 1. Add toppings
    # 2. Enable login
    # 3. Show total order
    # 4. Migrate to generic views
    # 5. Fix namespace issues
    # 6. Add checkout
    # 7. Migrate DB to postgres
    # 8. Migrate site to AWS
    # 9. Add s/l options
