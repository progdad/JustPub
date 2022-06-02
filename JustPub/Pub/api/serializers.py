from rest_framework.exceptions import ValidationError
from rest_framework.fields import SerializerMethodField
from rest_framework.relations import HyperlinkedIdentityField, StringRelatedField
from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer, CharField

from Pub.models import Category, DishesType, Dish


class BaseSerializerMixin(ModelSerializer):
    @staticmethod
    def validate_name(name):
        if not name.replace(" ", "").replace("-", "").isalnum():
            raise ValidationError(
                "'name' field may contain only letters, numbers, dashes and spaces. Change it, please !"
            )
        return name


#
# DISH SERIALIZERS
#


class DishListSerializer(BaseSerializerMixin):
    url = HyperlinkedIdentityField(view_name="dish-detail", lookup_field="slug")

    class Meta:
        model = Dish
        fields = ["name", "url"]


class DishRetrieveSerializer(BaseSerializerMixin):
    type_of_food = CharField(source="type_of_food.name")

    class Meta:
        model = Dish
        fields = ["type_of_food", "id", "name", "description", "prices"]


class DishCreateUpdateSerializer(BaseSerializerMixin):
    @staticmethod
    def validate_prices(prices):
        if not prices:
            raise ValidationError(
                "'prices' JSONField of 'Dish' model can't be the NoneType object. Input the valid JSON data !"
            )
        return prices

    class Meta:
        model = Dish
        fields = ["name", "type_of_food", "description", "prices"]


#
# DISHES_TYPES SERIALIZERS
#


class DishesTypeListSerializer(BaseSerializerMixin):
    url = HyperlinkedIdentityField(view_name="dishestype-detail", lookup_field="slug")

    class Meta:
        model = DishesType
        fields = ["name", "url"]


class DishesTypeRetrieveSerializer(BaseSerializerMixin):
    category = CharField(source="category.name")
    dishes = SerializerMethodField()

    def get_dishes(self, dishes_type):
        all_current_dishes_type_dishes = Dish.objects.filter(type_of_food=dishes_type)
        serializer = DishListSerializer(
            all_current_dishes_type_dishes, many=True,
            context=self.context
        )
        return serializer.data

    class Meta:
        model = DishesType
        fields = ["category", "id", "name", "dishes"]


class DishesTypeCreateUpdateSerializer(BaseSerializerMixin):
    class Meta:
        model = DishesType
        fields = ["name", "category"]


#
# CATEGORIES SERIALIZERS
#


class CategoryListSerializer(BaseSerializerMixin):
    url = HyperlinkedIdentityField(view_name="category-detail", lookup_field="slug")

    class Meta:
        model = Category
        fields = ["name", "url"]


class CategoryRetrieveSerializer(BaseSerializerMixin):
    dishes_types = SerializerMethodField()

    def get_dishes_types(self, category):
        all_current_category_dishes_types = DishesType.objects.filter(category=category)
        serializer = DishesTypeListSerializer(
            all_current_category_dishes_types, many=True,
            context=self.context
        )
        return serializer.data

    class Meta:
        model = Category
        fields = ["id", "name", "dishes_types"]


class CategoryCreateUpdateSerializer(BaseSerializerMixin):
    class Meta:
        model = Category
        fields = ["name"]
