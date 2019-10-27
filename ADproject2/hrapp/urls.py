from django.urls import path,include
from . import views

urlpatterns = [
    path('create/', views.employee_signup, name='create' ),
    path('modify/<int:pk>', views.employee_page_modify, name='modify' ),

]
