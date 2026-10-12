from django.db import models

class foodorder(models.Model):
    customer_name = models.CharField(max_length=255)
    food_item = models.CharField(max_length=255)
    quantity = models.IntegerField()
    price = models.IntegerField()
    is_delivered = models.BooleanField(default=False)

    def __str__(self):
        return f"Order {self.id} - {self.customer_name}"
        
