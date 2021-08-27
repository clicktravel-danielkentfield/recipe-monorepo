from django.db import models


class Recipe(models.Model):
    """Recipe object"""
    name = models.CharField(max_length=10)
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    """Ingredient object"""
    name = models.CharField(max_length=10)
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name
