from django.db import models
from user.models import User


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.customer.username
    
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    # item = models.ForeignKey('Books yoki Courses', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    
