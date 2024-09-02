from django.db import models

# Create your models here.
#sheets -- in excel
#models-- in the form of tables
# class Post(models.Model):
#     sno = models.AutoField(primary_key=True)
#     title = models.CharField(max_length=300)
#     author = models.CharField(max_length=20)
#     slug = models.CharField(max_length=130)
#     timeStamp = models.DateTimeField(blank=True)
#     content = models.TextField()

#     def __str__(self):
#         return self.title + ' by ' + self.author

from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from pickle import TRUE
from django.utils.timezone import now


class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=300)
    author = models.CharField(max_length=20)
    slug = models.SlugField(max_length=130, unique=True, blank=True)
    timeStamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def save(self, *args, **kwargs):
        # Generate the slug from the title if it is not already set
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.title} by {self.author}'
    
class blogComment(models.Model):
    sno=models.AutoField(primary_key=True)
    comment = models.TextField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    parent=models.ForeignKey('self', on_delete=models.CASCADE, null=TRUE)
    timestamp= models.DateTimeField(default=now)



  
