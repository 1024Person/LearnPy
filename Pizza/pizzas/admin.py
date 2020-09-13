from django.contrib import admin
from pizzas.models import Pizza, Topping

# Register your models here.
# 注册披散模型
admin.site.register(Pizza)
# 注册原料模型
admin.site.register(Topping)
