from django.db import models
from django.core import validators

# from .validators import validators
from item_app.models import Item
from user_app.models import Client


# Create your models here.
class Cart(models.Model):

    client = models.OneToOneField(
        to=Client, on_delete=models.CASCADE, related_name="cart"
    )

    def add_item(self, cart_item_id, quantity=1):
        item = Item.objects.get(id=cart_item_id)
        cart_item, created = Cart_item.objects.get_or_create(
            cart=self, item=item, defaults={"quantity": quantity}
        )
        if not created:
            cart_item.quantity += quantity
            cart_item.save()
        return cart_item

    def remove_item(self, cart_item_id):
        if not self.cart_items.exists():
            raise Exception("The cart is empty")
        Cart_item.objects.filter(
            cart=self, cart_item_id=cart_item_id
        ).delete()

    def remove_all_items(self):
        if not self.cart_items.exists():
            raise Exception("The cart is empty")
        self.cart_items.all().delete()


class Cart_item(models.Model):

    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        related_name="cart_items",
    )

    item = models.ForeignKey(
        Item,
        on_delete=models.CASCADE,
        related_name="cart_item",
    )
    quantity: int = models.PositiveIntegerField(default=1)
