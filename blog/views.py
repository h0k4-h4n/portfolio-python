from django.shortcuts import render, get_object_or_404
from .models import Blog
# Create your views here.

def allblogs(request):
    blog = Blog.objects.all()
    return render(request, 'blog/allblogs.html', {'blog': blog})

def detail(request, blog_id):
    detailblog = Blog.objects.get(pk=blog_id)
    print("detailblog")
    return render(request, 'blog/detail.html', {'blog': detailblog})