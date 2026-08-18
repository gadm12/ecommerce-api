from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import Item, ItemSerializer
from cart_app.models import Cart, Cart_item
from rest_framework import status


# Create your views here.
class All_items(APIView):
    def get(self, request):
        return Response(
            ItemSerializer(
                Item.objects.all(),
                many=True,
            ).data
        )

    def post(self, request):
        serializer = ItemSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED,
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )


class An_item(APIView):
    def get(self, request, item_id):
        item = get_object_or_404(Item, id=item_id)
        return Response(ItemSerializer(item).data)

    def get(self, request, item_id):
        item = get_object_or_404(Item, id=item_id)
        return Response(ItemSerializer(item).data)

    def post(self, request, item_id):
        item = get_object_or_404(Item, id=item_id)
        cart, _ = Cart.objects.get_or_create(client=request.user)
        cart.add_item(item.id, quantity=1)
        return Response(
            f"{item.name} has been added to your cart",
            status=status.HTTP_201_CREATED,
        )

    def delete(self, request, item_id):
        item = get_object_or_404(
            Item,
            id=item_id,
        )

        item.delete()

        return Response(
            status=status.HTTP_204_NO_CONTENT,
        )


class Item_by_category(APIView):
    def get(self, request, category):
        items = Item.objects.filter(category__iexact=category)
        return Response(ItemSerializer(items, many=True).data)
