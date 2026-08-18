from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from item_app.serializers import ItemSerializer
from .models import Cart, Cart_item


class Cart_itemSerializer(ModelSerializer):
    item = ItemSerializer(read_only=True)

    class Meta:
        model = Cart_item
        fields = ["id", "item", "quantity"]


class CartSerializer(ModelSerializer):
    cart_items = Cart_itemSerializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ["cart_items", "total_price"]
        

    def get_total_price(self, obj):
        total = 0

        for ci in obj.cart_items.all():
            total += ci.item.price * ci.quantity
        return float(round(total, 2))
