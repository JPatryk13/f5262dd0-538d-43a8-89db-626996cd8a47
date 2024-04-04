from rest_framework.routers import DefaultRouter

from .views import BookViewSet, EditionViewSet, AuthorViewSet

router = DefaultRouter()
router.register(r"books", BookViewSet, basename="books")
router.register(r"editions", EditionViewSet, basename="editions")
router.register(r"authors", AuthorViewSet, basename="authors")
urlpatterns = router.urls
