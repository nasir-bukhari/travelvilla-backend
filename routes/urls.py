from rest_framework import routers
from django.urls import path, include
from . import views
from .views import find_nearest_station

# router = routers.DefaultRouter()
# router.register(r'', views.RoutesViewSet)
urlpatterns = [
    # path('', include(router.urls)),
    path('nearest_station/', find_nearest_station, name="find_nearest_station")
]
