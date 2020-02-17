from . import views
from django.urls import path
urlpatterns = [
       path("", views.AboutView.as_view(), name="about"),
       path("order/", views.CreateOrderView.as_view(), name="order_new"),
       path("order/finish/", views.FinishView.as_view(),name = "finish"),
       path("orderlist/",views.OrderListView.as_view(), name="order_list"),
       path("ordrlist/<int:pk>", views.OrderDetailedView.as_view(), name="order_list_detail"),
]