from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime
import os

User=get_user_model() #curruntly authenticated user

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    bio = models.TextField(blank=True)
    profileimg = models.ImageField(upload_to='profile_images' ,null=True, blank=True)
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return str(self.user)

def rename_post_image(instance, filename):
    ext = filename.split('.')[-1]
    # generate a new unique name for the file
    filename = f'{uuid.uuid4()}.{ext}'
    # return the new filename including the path where it will be saved
    return os.path.join('post_images', filename)        
        
class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.CharField(max_length=100)
    image = models.ImageField(upload_to=rename_post_image)
    caption = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)
    no_of_likes = models.IntegerField(default=0)

    def __str__(self):
        return self.user  


class LikePost(models.Model):
    post_id = models.CharField(max_length=500)
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username

class FollowersCount(models.Model):
    follower = models.CharField(max_length=100)
    user = models.CharField(max_length=100)

    def __str__(self):
        return self.user        
