from django.db import models
#import cloudinary 
from cloudinary.models import CloudinaryField




# Create your models here.
class Post(models.Model):
    class Meta(object):
        db_table = 'post'
    name = models.CharField(
        'name', blank=False, null=False, max_length=20, db_index=True, default='Richie'
    )
    hobbie = models.CharField(
        'hobbie', blank=True, null=True, max_length=140, db_index=True
    )
    image = CloudinaryField(
        'image', blank=True, db_index=True

    )
    created_at = models.DateTimeField(
        'created_at', blank=True, auto_now_add=True
    )
    likecount=models.IntegerField(
        'like_count',default=0,null=True, blank=True

    )

