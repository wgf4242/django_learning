from django.db import models


class Topping(models.Model):
    name = models.CharField(max_length=30)

class Pizza(models.Model):
    name = models.CharField(max_length=50)
    toppings = models.ManyToManyField(Topping)

    def __str__(self):              # __unicode__ on Python 2
        return "%s (%s)" % (
            self.name,
            ", ".join(topping.name for topping in self.toppings.all()),
        )


class Restaurant(models.Model):
    pizzas = models.ManyToManyField(Pizza, related_name='restaurants')
    best_pizza = models.ForeignKey(Pizza, related_name='championed_by')

class Country(models.Model):
    name = models.CharField(max_length=30)

class City(models.Model):
    name = models.CharField(max_length=30)
    country = models.ForeignKey(Country)
    population = models.PositiveIntegerField()