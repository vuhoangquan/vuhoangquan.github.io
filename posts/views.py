from django.shortcuts import render
from django.http import JsonResponse
from django.urls import reverse
from .models import Post, Author, Category, SubCategory

from itertools import chain

# Create your views here.
def index(request):
    return render(request, "posts/index.html", {
        "posts":Post.objects.all(),
        "categories":Category.objects.all(),
        "sub_categories":SubCategory.objects.all()
    })

def post(request, post_id):
    post = Post.objects.get(id=post_id)
    categories = Category.objects.filter(posts = post).all()
    
    return render(request, "posts/post.html", {
        "post":post,
        "categories_tag": categories,
        "categories":Category.objects.all(),
        "sub_categories":SubCategory.objects.all()
    })

categories1 = [] 
sub_categories1 = []

def author(request, author_id):
    author = Author.objects.get(id=author_id)
    posts = Post.objects.filter(author=author).all()
    for post in posts:
        category = post.post_categories.all()
        categories1.append(category)
    for category in categories1:
        sub_categories1.append(category)
    
    # catefories1 = get_all_categories(author)
    # categories1 = posts[1].post_categories.all()
    # sub_categories = categories.main_categories.all()
    # sub_categories = categories1[1].main_categories.all()
    
    return render(request, "posts/author.html", {
        "author":author,
        "posts":posts,
        "categories_tag": categories1[0],
        "sub_categories_tag": sub_categories1[0],
        "categories":Category.objects.all(),
        "sub_categories":SubCategory.objects.all()
    })
    
    
    
    
# def thumbnail(request, post_id):
#       return render(request, )

#     # Get start and end points
#     # start = int(request.GET.get("start") or 0)
#     # end = int(request.GET.get("end") or (start + 9))

#     # # Generate list of posts
#     data = ["test"]
#     # for i in range(start, end ):
#     #     data.append(f"Post #{ i }: ")

#     # Artificially delay speed of response
#     # time.sleep(1)

#     # Return list of posts
#     return JsonResponse({
#         "posts": data
#     })