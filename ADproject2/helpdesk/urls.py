from django.urls import path,include
from . import views

urlpatterns = [
    path('assign/', views.inventory_page, name='assign' ),
    path('assign/<int:pk>', views.inventory_page_modify, name='assign_edit' ),

]
