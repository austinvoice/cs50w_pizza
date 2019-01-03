from django.urls import path

from . import views
#
app_name = 'orders';
#
urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:category_id>/order/', views.order, name='order'),
]
