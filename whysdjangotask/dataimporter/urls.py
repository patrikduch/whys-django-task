from django.urls import path
from . import views

urlpatterns = [
    path('import/', views.import_data, name='import_data'),
    path('detail/<str:model_name>/', views.detail_model_list, name='detail_model_list'),
    path('detail/<str:model_name>/<int:pk>/', views.detail_model_data, name='detail_model_data'),
]