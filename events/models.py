from django.db import models
import qrcode
from io import BytesIO
from django.core.files.base import ContentFile
from PIL import Image
from django.contrib.postgres.fields import ArrayField
import os
# import torch
# import torch.nn as nn

# Create your models here.


class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    qr_code = models.ImageField(blank=True, upload_to='qrcodes/')
    date = models.DateField()

    def __str__(self):
        return str(self.name)

    def save(self, *arg, **kwargs):
        if not self.qr_code:
            qrcode_img = qrcode.make(self.name)
            canvas = Image.new('RGB', (qrcode_img.pixel_size,
                               qrcode_img.pixel_size), 'white')
            canvas.paste(qrcode_img)
            fname = f'qr_code-{self.name}.png'
            buffer = BytesIO()
            canvas.save(buffer, 'PNG')
            self.qr_code.save(fname, ContentFile(
                buffer.getvalue()), save=False)

        super().save(*arg, **kwargs)


class Selectedhabit(models.Model):
    user = models.IntegerField(),
    selecthabit = models.CharField(max_length=1000),


class img(models.Model):
    imgname = models.CharField(max_length=200, default='')
    imge = models.CharField(max_length=1000, default='')

    def __str__(self):
        return str(self.name)

    def save(self, *arg, **kwargs):
        super().save(*arg, **kwargs)


class Photos(models.Model):
    photo = models.ImageField(blank=True, upload_to='user_img/')

    def save(self, *arg, **kwargs):
        super().save(*arg, **kwargs)

class GPS(models.Model):
    lat = models.FloatField()
    long = models.FloatField()

class Study(models.Model):
    lat = models.FloatField()
    long = models.FloatField()
    
# class MyModel(nn.Module):
#     predict = models.CharField(max_length=200, default='')
    
#     def load_model():
#         model = MyModel()
#         model.load_state_dict(torch.load('../best.pt'))
#         model.eval()
#         return model

