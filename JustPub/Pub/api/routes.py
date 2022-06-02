from rest_framework.routers import SimpleRouter

from .views import CategoryModelView, DishesTypeModelView, DishModelView


router = SimpleRouter()

router.register(r"categories", CategoryModelView)
router.register(r"dishes-types", DishesTypeModelView)
router.register(r"dishes", DishModelView)


urlpatterns = router.urls
