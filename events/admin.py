from django.contrib import admin
from .models import Event,img,GPS,Study

# Register your models here.

admin.site.register(Event)
admin.site.register(img)
admin.site.register(GPS)
admin.site.register(Study)