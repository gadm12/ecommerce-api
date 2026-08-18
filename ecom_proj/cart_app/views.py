from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .models import Cart, Cart_item
from .serializers import CartSerializer, Cart_itemSerializer




class Cart_manager(APIView):
   

    def post(self, request):
        cart = get_object_or_404(Cart, client=request.user)
        item_id = request.data.get("item_id")
        quantity = request.data.get("quantity", 1)
        cart_item = cart.add_item(item_id, quantity)
        return Response(
            Cart_itemSerializer(cart_item).data,
            status=status.HTTP_201_CREATED,
        )

    def get(self, request):
        cart, _ = Cart.objects.get_or_create(client=request.user)
        return Response(CartSerializer(cart).data)

    def put(self, request, method, cart_item_id):
        cart_item = get_object_or_404(Cart_item, id=cart_item_id)
        if method == "add":
            cart_item.quantity += 1
            cart_item.save()
        elif method == "sub":
            cart_item.quantity -= 1
            if cart_item.quantity <= 0:
                cart_item.delete()
            else:
                cart_item.save()
        return Response(status=status.HTTP_200_OK)

    def delete(self, request, cart_item_id):
        cart_item = get_object_or_404(Cart_item, id=cart_item_id)
        cart_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
