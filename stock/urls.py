from django.urls import path, include
from . import views


app_name = 'stock'

urlpatterns = [
    path('create/', views.SupplyCreateView.as_view(), name="create"),
    path('restock/<int:pk>', views.add_supply, name="restock"),
    path('send/', views.send_supply_to_tasks, name="send"),
    path("update/<int:pk>", views.SupplyUpdateView.as_view(), name="update"),
    path('list', views.SupplyListView.as_view(), name="supply-list"),
]
