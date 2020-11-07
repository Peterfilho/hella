from django.urls import path, re_path
from . import views

app_name='catalog'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    re_path(r'^(?P<slug>[\w-]+)/$', views.category, name='category'),
]
