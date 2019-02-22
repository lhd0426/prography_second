from django.shortcuts import render
from blog.models import Blog

# Create your views here.
def index(request):
	blogs = Blog.objects.all()
	pageId = request.GET.get('id')
	text = request.GET.get('text')
	return render(request, 'blog/index.html', {'blogs': blogs, 'title': pageId, 'text': text})