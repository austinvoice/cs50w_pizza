from django.urls import path

from . import views
#
app_name = 'pizza';
app_name = 'orders';
app_name = 'order';
#
urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
]
