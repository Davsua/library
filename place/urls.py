from .views import BookViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("books", BookViewSet)
router.register("books/<string:title>", BookViewSet)


urlpatterns = router.urls
