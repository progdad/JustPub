from rest_framework.fields import SerializerMethodField
from rest_framework.relations import HyperlinkedIdentityField
from rest_framework.serializers import CharField

from Pub.models import DishesType, Dish
from Pub.rest_api.serializers.base_serializer_mixin import BaseSerializerMixin
from Pub.rest_api.serializers.dishes_serializers import DishListSerializer


class DishesTypeListSerializer(BaseSerializerMixin):
    category = CharField(source="category.name")
    url = HyperlinkedIdentityField(view_name="dishestype-detail", lookup_field="slug")

    class Meta:
        model = DishesType
        fields = ["name", "url", "category"]


class DishesTypeRetrieveSerializer(BaseSerializerMixin):
    category = CharField(source="category.name")
    dishes = SerializerMethodField()

    def get_dishes(self, dishes_type):
        all_current_dishes_type_dishes = Dish.objects.filter(type_of_food=dishes_type)
        serializer = DishListSerializer(
            all_current_dishes_type_dishes,
            many=True, read_only=True,
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
