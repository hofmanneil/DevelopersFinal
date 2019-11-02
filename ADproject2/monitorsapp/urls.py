from django.urls import path,include
from . import views

urlpatterns = [
    path('monitors/', views.monitors_page, name='monitor' ),
    # path('monitors/<int:pk>', views.monitors_page_modify, name='monitors_edit' ),
]
