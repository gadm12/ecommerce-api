from decimal import Decimal
from django.db import models
from django.core import validators
from .validators import name_format_validate


# Create your models here.
class Item(models.Model):
    class Category(models.TextChoices):
        ELECTRONICS = "electronics", "Electronics"
        BOOK = "book", "Book"
        OTHER = "other", "Other"

    category = models.CharField(
        max_length=50,
        choices=Category.choices,
    )
    
    name: str = models.CharField(
        max_length=100,
        validators=[name_format_validate],
    )

    price: float = models.DecimalField(
        decimal_places=2,
        max_digits=10,
        validators=[
            validators.MinValueValidator(Decimal("0.01"))
        ],
    )

    def __str__(self):
        return (
            f"< { self.name} | ${self.price} | {self.category} >"
        )
