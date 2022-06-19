from rest_framework.viewsets import ModelViewSet

from Pub.models import Category, DishesType, Dish
from Pub.rest_api.serializers import (
    CategoryListSerializer,   CategoryRetrieveSerializer,   CategoryCreateUpdateSerializer,
    DishesTypeListSerializer, DishesTypeRetrieveSerializer, DishesTypeCreateUpdateSerializer,
    DishListSerializer,       DishRetrieveSerializer,       DishCreateUpdateSerializer
)


class BaseViewClass(ModelViewSet):
    """
    list:
        Return all "{model_name}" model instances.

    create:
        Create a new "{model_name}" model instance.

    retrieve:
        Return single "{model_name}" model instance.

    delete:
        Delete "{model_name}" model instance.

    update:
        Update "{model_name}" model instance.
    """

    lookup_field = "slug"
    queryset = None
    get_list_serializer = None
    get_retrieve_serializer = None
    post_create_update_serializer = None
    # Redefine allowed HTTP methods to disallow "OPTIONS", "HEAD", "PATCH" and other unneeded methods.
    http_method_names = ['get', 'post', 'put', 'delete']

    def get_serializer_class(self, *args, **kwargs):
        if self.action == "list":
            return self.get_list_serializer
        elif self.action in ["retrieve", "destroy"]:
            return self.get_retrieve_serializer
        elif self.action in ["create", "update"]:
            return self.post_create_update_serializer


class CategoryModelView(BaseViewClass):
    __doc__ = BaseViewClass.__doc__.format(model_name="Category")

    queryset = Category.objects.all()
    get_list_serializer = CategoryListSerializer
    get_retrieve_serializer = CategoryRetrieveSerializer
    post_create_update_serializer = CategoryCreateUpdateSerializer


class DishesTypeModelView(BaseViewClass):
    __doc__ = BaseViewClass.__doc__.format(model_name="DishesType")

    queryset = DishesType.objects.all()
    get_list_serializer = DishesTypeListSerializer
    get_retrieve_serializer = DishesTypeRetrieveSerializer
    post_create_update_serializer = DishesTypeCreateUpdateSerializer


class DishModelView(BaseViewClass):
    __doc__ = BaseViewClass.__doc__.format(model_name="Dish")

    queryset = Dish.objects.all()
    get_list_serializer = DishListSerializer
    get_retrieve_serializer = DishRetrieveSerializer
    post_create_update_serializer = DishCreateUpdateSerializer
