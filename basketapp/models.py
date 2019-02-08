from django.db import models
from django.conf import settings
from mainapp.models import Product

class Basket(models.Model):
    _cost: float
    _total_quantity: int
    _total_price: int

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='basket')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='кол-во', default=0)
    add_datetime = models.DateTimeField(verbose_name='дата добавления', auto_now_add=True)


    @property
    def total_quantity(self):
        return sum([_.quantity for _ in Basket.objects.filter(user=self.user)])

    # @vars
    @property
    def product_price(self):
        return self.product.price * self.quantity

    @property
    def total_price(self):
        return sum([_.product_price for _ in Basket.objects.filter(user=self.user)])