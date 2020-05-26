from django.db import models
from django.utils import timezone
from django.urls import reverse
import random

default_image_urls = [
    "https://images.pexels.com/photos/147411/italy-mountains-dawn-daybreak-147411.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=94",
    "https://images.pexels.com/photos/462024/pexels-photo-462024.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940",
    "https://images.pexels.com/photos/417054/pexels-photo-417054.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940",
    "https://images.pexels.com/photos/196667/pexels-photo-196667.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940",
    "https://images.pexels.com/photos/507410/pexels-photo-507410.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940",
    "https://images.pexels.com/photos/981781/pexels-photo-981781.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940",
    "https://images.pexels.com/photos/981781/pexels-photo-981781.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940",
    "https://images.pexels.com/photos/4261797/pexels-photo-4261797.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940",
    "https://images.pexels.com/photos/3989821/pexels-photo-3989821.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940",
    "https://images.pexels.com/photos/461198/pexels-photo-461198.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940",
    "https://images.pexels.com/photos/1640772/pexels-photo-1640772.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940",
    "https://images.pexels.com/photos/1640774/pexels-photo-1640774.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940",
    "https://images.pexels.com/photos/2664216/pexels-photo-2664216.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940",
    "https://images.pexels.com/photos/2081166/pexels-photo-2081166.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940",
]

def choice():
    return random.choice(default_image_urls)

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete= models.CASCADE,)
    title = models.CharField(max_length=200)
    banner_image_url = models.URLField(help_text="Provide a banner image for your post", default=choice)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    publish_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.publish_date = timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved_comment=True)

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk':self.pk})

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete= models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse('post_list')

    def __str__(self):
        return self.text
