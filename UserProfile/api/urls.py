from rest_framework.routers import DefaultRouter
from ..views import FormViewSet


router = DefaultRouter()
router.register(r'', FormViewSet, basename='UserProfile')
urlpatterns = router.urls