from rest_framework import viewsets
from ..models import Event, img, Photos, GPS, Study
from .serializers import EventModelSerializer, imgModelSerializer, PhotosModelSerializer, GPSModelSerializer, StudyModelSerializer
# SelectedhabitModelSerializer
from django.http.response import HttpResponse


class EventsViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventModelSerializer


class imgViewSet(viewsets.ModelViewSet):
    queryset = img.objects.all()
    serializer_class = imgModelSerializer


class PhotosViewSet(viewsets.ModelViewSet):
    queryset = Photos.objects.all()
    serializer_class = PhotosModelSerializer

class GPSViewSet(viewsets.ModelViewSet):
    queryset = GPS.objects.all()
    serializer_class = GPSModelSerializer
    
class StudyViewSet(viewsets.ModelViewSet):
    queryset = Study.objects.all()
    serializer_class = StudyModelSerializer
