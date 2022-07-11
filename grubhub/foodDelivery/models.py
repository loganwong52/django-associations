from django.db import models

# A user has many orders
# An order belongs to a user
#### Order has a Many-to-One FK 'user' to User 'order'

# A restaurant has many orders
# An order belongs to a restaurant
#### Order has a Many-to-One FK 'restaurant' to Restaurant 'order'

# An order has many order_food_items
# An order_food_item belongs to an order
#### OrderFoodItem has a One-to-Many FK 'order' to Order 'order_food_item'

# A food item has many order_food_items
# An order_food_item belongs to a food_item
#### OrderFoodItem has a One-to-Many FK 'food_item' to FoodItem 'order_food_item'

# And finally if you have set up your associations correctly a user should have many food items through orders. See the final test.
#### Order has a Many-to-Many FK 'food_items' through OrderFoodItems, OFI is a Join Table


class User(models.Model):
    name = models.CharField(max_length=20, default="")

class Restaurant(models.Model):
    restaurant_name = models.CharField(max_length=50, default="")

class FoodItem(models.Model):
    food_name = models.CharField(max_length=20, default="")

    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders", null=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="orders", null=True)
    food_items = models.ManyToManyField(FoodItem, related_name="orders", through="OrderFoodItem")

# Join table for Order, User(?) and FoodItem
class OrderFoodItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="order_food_items", null=True)
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE, related_name="order_food_items", null=True)


