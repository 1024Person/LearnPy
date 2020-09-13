from django.db import models


# Create your models here.
class Pizza(models.Model):
    name = models.CharField(max_length=20)  # 披萨的名字

    def __str__(self):
        return self.name


class Topping(models.Model):
    burden = models.TextField()  # 配料
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)

    def __str__(self):
        if len(self.burden) < 20:
            return self.burden
        else:
            return self.burden + '...'
