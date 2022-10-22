from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from taggit.managers import TaggableManager
# Create your models here.
class CustomManager(models.Manager):
	def get_queryset(self):
		return super().get_queryset().filter(status='published')

class Post(models.Model):
	tags=TaggableManager()
	STATUS_CHOICE=(('draft',"Draft"),('published','Published'))
	# draft, published -> for application
	# Draft, Published -> for User
	title=models.CharField(max_length=200)
	slug=models.SlugField(max_length=50,unique_for_date='publish')
	author=models.ForeignKey(User,related_name='blog_posts',on_delete=models.CASCADE)
	body=models.TextField()
	publish=models.DateTimeField(default=timezone.now)
	created=models.DateTimeField(auto_now_add=True)
	updated=models.DateTimeField(auto_now=True)
	status=models.CharField(max_length=20,choices=STATUS_CHOICE,default='draft')
	objects=CustomManager()
	class Meta:
		ordering=('-publish',) # single value tuple should end with comma

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("post_detail",args=[self.publish.year,self.publish.strftime('%m'),self.publish.strftime('%d'),self.slug])


class Comment(models.Model):
	name=models.CharField(max_length=50,default="")
	post=models.ForeignKey(Post,related_name="comments",on_delete=models.CASCADE)
	email=models.EmailField()
	body=models.TextField(default="")
	created=models.DateTimeField(auto_now_add=True)
	updated=models.DateTimeField(auto_now=True)
	active=models.BooleanField(default=True)
	class Meta:
		ordering=('created',)

		def __str__(self):
			return 'Commented by {0} on {1}'.format(self.name,self.post)