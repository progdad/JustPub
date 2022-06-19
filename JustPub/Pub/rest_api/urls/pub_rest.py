from rest_framework.routers import SimpleRouter

from Pub.rest_api.views import CategoryModelView, DishesTypeModelView, DishModelView


router = SimpleRouter()

router.register(r"categories", CategoryModelView)
router.register(r"dishes-types", DishesTypeModelView)
router.register(r"dishes", DishModelView)

rest_endpoints = router.urls
