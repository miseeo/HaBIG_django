from rest_framework import routers
from .views import EventsViewSet, imgViewSet, PhotosViewSet, GPSViewSet, StudyViewSet
from django.urls import path, include


router = routers.DefaultRouter()
router.register(r'events', EventsViewSet)
router.register(r'img', imgViewSet)
router.register(r'photos', PhotosViewSet)
router.register(r'GPS', GPSViewSet)
router.register(r'Study', StudyViewSet)


urlpatterns = [
    path('', include(router.urls))
]
