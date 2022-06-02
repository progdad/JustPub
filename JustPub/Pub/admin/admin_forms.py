from django.core.exceptions import ValidationError
from django.forms import ModelForm

from Pub.models import Category, DishesType, Dish


class BaseAdminForm(ModelForm):
    def clean_name(self):
        name = self.cleaned_data["name"]
        if not name.replace(" ", "").replace("-", "").isalnum():
            raise ValidationError(
                "'name' field may contain only letters, numbers, dashes and spaces. Change it, please !"
            )
        return name


class CategoryAdminForm(BaseAdminForm):
    class Meta:
        model = Category
        fields = "__all__"


class DishesTypeAdminForm(BaseAdminForm):
    class Meta:
        model = DishesType
        fields = "__all__"


class DishAdminForm(BaseAdminForm):
    class Meta:
        model = Dish
        fields = "__all__"
