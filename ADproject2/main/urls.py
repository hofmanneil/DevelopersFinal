from django.urls import path,include
from . import views

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('search/', views.search, name='search'),
    path('', views.index, name='index'),

]
