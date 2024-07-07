from django.db import models

from users.models import User
from goods.models import Products


class CartQueryset(models.QuerySet):

    def total_price(self):
        return sum(cart.product_price() for cart in self)

    def total_quantity(self):
        if self:
            return sum(cart.quantity for cart in self)
        return 0


class Cart(models.Model):

    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
        blank=True,
        null=True,
    )
    product = models.ForeignKey(
        to=Products, 
        on_delete=models.CASCADE, 
        verbose_name="Товар"
    )
    session_key = models.CharField(max_length=32, blank=True, null=True)
    quantity = models.SmallIntegerField(default=0, verbose_name="Количество")
    created_timestamp = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата добавления"
    )

    objects = CartQueryset().as_manager()

    class Meta:
        db_table = "cart"
        verbose_name = "Корзина"
        verbose_name_plural = "Корзина"

    def product_price(self):
        return round(self.product.sell_price() * self.quantity)

    def __str__(self):
        if self.user:
            return f"Корзина пользователя {self.user.username} | Товар {self.product.name} | Количество {self.quantity}"
        return f"Корзина неавторизованного  пользователя | Товар {self.product.name} | Количество {self.quantity}"