from rest_framework.fields import SerializerMethodField
from rest_framework.relations import HyperlinkedIdentityField

from Pub.models import Category, DishesType
from Pub.rest_api.serializers.base_serializer_mixin import BaseSerializerMixin
from Pub.rest_api.serializers.dishestype_serializers import DishesTypeListSerializer


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
            all_current_category_dishes_types,
            many=True, read_only=True,
            context=self.context,
        )
        return serializer.data

    class Meta:
        model = Category
        fields = ["id", "name", "dishes_types"]


class CategoryCreateUpdateSerializer(BaseSerializerMixin):
    class Meta:
        model = Category
        fields = ["name"]
