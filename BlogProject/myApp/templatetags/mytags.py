from django import template
from myApp.models import Post
from django.db.models import Count
register=template.Library() # default template tag = total_posts
@register.simple_tag
def total_posts():
	return Post.objects.count()

@register.inclusion_tag('myApp/latest_post.html')
def show_latest_posts(count=3):
	latest_post=Post.objects.order_by('-publish')[:count]
	# collect the posts based on latest poublished date w.r.t. specified count
	return {'latest_post':latest_post}

@register.simple_tag
def get_most_commented_post(count=2):
	return Post.objects.annotate(total_comments=Count('comments')).order_by('-total_comments')[:count]

@register.simple_tag()
def all_post():
	return Post.objects.all()