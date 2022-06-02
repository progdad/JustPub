from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from Pub.models import Category, DishesType, Dish
from .serializers import (
    CategoryListSerializer,   CategoryRetrieveSerializer,   CategoryCreateUpdateSerializer,
    DishesTypeListSerializer, DishesTypeRetrieveSerializer, DishesTypeCreateUpdateSerializer,
    DishListSerializer,       DishRetrieveSerializer,       DishCreateUpdateSerializer
)


class BaseViewMixin(ModelViewSet):
    lookup_field = "slug"
    queryset = None
    get_list_serializer = None
    get_retrieve_serializer = None
    post_create_update_serializer = None

    def get_serializer_class(self, *args, **kwargs):
        if self.action == "list":
            return self.get_list_serializer
        elif self.action in ["retrieve", "destroy"]:
            return self.get_retrieve_serializer
        elif self.action in ["create", "update", "partial_update"]:
            return self.post_create_update_serializer

    def retrieve(self, request, slug=None, **kwargs):
        model_instance = get_object_or_404(self.queryset, slug=slug)
        serializer = self.get_retrieve_serializer(model_instance, context={'request': request})
        return Response(serializer.data)


class CategoryModelView(BaseViewMixin):
    queryset = Category.objects.all()
    get_list_serializer = CategoryListSerializer
    get_retrieve_serializer = CategoryRetrieveSerializer
    post_create_update_serializer = CategoryCreateUpdateSerializer


class DishesTypeModelView(BaseViewMixin):
    queryset = DishesType.objects.all()
    get_list_serializer = DishesTypeListSerializer
    get_retrieve_serializer = DishesTypeRetrieveSerializer
    post_create_update_serializer = DishesTypeCreateUpdateSerializer


class DishModelView(BaseViewMixin):
    queryset = Dish.objects.all()
    get_list_serializer = DishListSerializer
    get_retrieve_serializer = DishRetrieveSerializer
    post_create_update_serializer = DishCreateUpdateSerializer
