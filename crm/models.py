from django.db import models

# Create your models here.
class Order(models.Model):
    order_dt = models.DateTimeField(auto_now=True)
    order_name = models.CharField(max_length=50, verbose_name='имя')
    order_phone = models.CharField(max_length=50, verbose_name='телефон')

    def __str__(self):
        return self.order_name

    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'

