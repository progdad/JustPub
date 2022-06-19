from rest_framework.exceptions import ValidationError
from rest_framework.relations import HyperlinkedIdentityField
from rest_framework.serializers import CharField

from Pub.models import Dish
from Pub.rest_api.serializers.base_class import BaseSerializerClass


class DishListSerializer(BaseSerializerClass):
    type_of_food = CharField(source="type_of_food.name")
    url = HyperlinkedIdentityField(view_name="dish-detail", lookup_field="slug")

    class Meta:
        model = Dish
        fields = ["name", "url", "type_of_food"]


class DishRetrieveSerializer(BaseSerializerClass):
    type_of_food = CharField(source="type_of_food.name")

    class Meta:
        model = Dish
        fields = ["type_of_food", "id", "name", "description", "prices"]


class DishCreateUpdateSerializer(BaseSerializerClass):
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
