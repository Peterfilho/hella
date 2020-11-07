from django.contrib import admin
from django.urls import path, include
from core import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contato', views.contact, name='contact'),
    path('produto', views.product, name='product'),
    path('produtos/', include(('catalog.urls'), namespace='catalog')),
    path('admin/', admin.site.urls),
]
