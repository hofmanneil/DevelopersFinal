from django.urls import path,include
from . import views

urlpatterns = [
    path('machines/', views.machine_page, name='machines' ),
    path('machines/<int:pk>', views.machine_page_modify, name='machines_edit' ),
    



    # path('assign/<int:pk>', views.inventory_page_modify, name='assign_edit' ),

]
