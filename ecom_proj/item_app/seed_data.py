from item_app.models import Item

red_bull = Item.objects.create(
    category="drinks", name="Red Bull", price="3.50"
)

coke = Item.objects.create(
    category="Drinks", name="coke", price="1.50"
)

item = Item(category="drinks", name="Red Bull", price="3.50")
item.full_clean()   
item.save()

print("Created successfully!")
# pm shell < item_app/seed_data.py
