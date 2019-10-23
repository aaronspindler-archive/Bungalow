from rest_framework.routers import SimpleRouter

from .views import HouseViewSet

urlpatterns = [
]
router = SimpleRouter()
router.register('houses', HouseViewSet, base_name='houses')
urlpatterns += router.urls
