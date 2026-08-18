from django.urls import path
from .views import Cart_manager

urlpatterns = [
    path("cart/", Cart_manager.as_view(), name="cart"),
    path(
        "cart/method/<str:method>/cart_item/<int:cart_item_id>/",
        Cart_manager.as_view(),
        name="cart_item_quantity",
    ),
    path(
        "cart/<int:cart_item_id>/",
        Cart_manager.as_view(),
        name="delete_item",
    ),
]
