from django.db import models
from django.utils import timezone #To get UTC time. For this to work USE_TZ should be set True
#otherwise it will get localtime
from django.urls import reverse #for get_absolute_url method to obtain url after processing model(RECHECK)

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)#Try other options for cascade
    title = models.CharField(max_length=200)
    text = models.TextField()
    creation_date = models.DateTimeField(default=timezone.now)
    publishion_date = models.DateTimeField(blank=True, null=True)#Its not necessary to publish post it
    #has been created

    def publish(self):
        self.publishion_date = timezone.now()
        self.save()

    def approve_comment(self):
        return self.comments.filter(approved_comment=True)

    def get_absolute_url(self):#Tells what to do when Post object has been created.
        return reverse('post_detail', kwargs={'pk':self.pk})#Here 'post_detail' is view name and kwargs
        #is context_dictionary

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    text = models.TextField()
    creation_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):#Who will approve comments?
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse('post_list')
    def __str__(self):
        return self.text
