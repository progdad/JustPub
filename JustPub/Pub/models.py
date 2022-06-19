from django.db import models
from django.utils.text import slugify


class BaseModelClass(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(blank=True, null=True, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        abstract = True


class Category(BaseModelClass):
    class Meta:
        ordering = ["name"]
        verbose_name_plural = "1. Food Categories"

    def __str__(self):
        return self.name


class DishesType(BaseModelClass):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        ordering = ["category", "name"]
        verbose_name_plural = "2. Types Of Dishes"

    def __str__(self):
        return f"{self.category} - {self.name}"


class Dish(BaseModelClass):
    type_of_food = models.ForeignKey(DishesType, on_delete=models.CASCADE)
    description = models.CharField(max_length=1000)
    prices = models.JSONField()

    class Meta:
        ordering = ["type_of_food", "name"]
        verbose_name_plural = "3. Dishes"

    def __str__(self):
        return f"{self.type_of_food} - {self.name}"
