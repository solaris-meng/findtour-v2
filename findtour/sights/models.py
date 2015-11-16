from django.db import models

# Create your models here.
class Area(models.Model):
    name = models.CharField(max_length=32, default='none')
    slug = models.CharField(max_length=32, default='none')
    main_pic = models.CharField(max_length=32, default='none')
    description = models.TextField(max_length=256,default='none')

    def __str__(self):
        return self.name

class Sight(models.Model):
    area = models.ForeignKey(Area)

    name = models.CharField(max_length=32, default='none')
    slug = models.CharField(max_length=32, default='none')

    # description
    description = models.TextField(max_length=2048,default='none')
    wiki = models.CharField(max_length=128, default='none')

    # information
    city = models.CharField(max_length=32, default='none')
    ticket = models.CharField(max_length=32, default='none')
    opentime = models.CharField(max_length=32, default='none')
    timeforvisit = models.CharField(max_length=32, default='none')

    # review
    review = models.TextField(max_length=1024,default='none')

    # tips
    tips = models.TextField(max_length=1024,default='none')

    #photos
    photos = models.TextField(max_length=1024,default='none')

    main_pic = models.CharField(max_length=32, default='none')
    main_pic_small = models.CharField(max_length=32, default='none')

    def __str__(self):
        return self.name

    def get_review_item(self):
        reviews = self.review
        rv = reviews.split('\r')
        return rv
    def get_tips_item(self):
        tip = self.tips
        rv = tip.split('\r')
        return rv
    def get_photos_item(self):
        photos = self.photos
        rv = photos.split('\r')
        return rv
