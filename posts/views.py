from django.shortcuts import render
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.urls import reverse

from .models import Post, Author, Category, SubCategory

from itertools import chain

# Create your views here.
def index(request):
    url_parameter = request.GET.get("title")
    if url_parameter:
        searches = Post.objects.filter(title__icontains=url_parameter)
    
        if request.is_ajax():
            html = render_to_string(
                template_name="posts/partial_result.html", 
                context={"posts_returned": searches}
            )
            data_dict = {"html_from_view": html}
            return JsonResponse(data=data_dict, safe=False)
    else:
        searches = Post.objects.all()
        
    return render(request, "posts/index.html", {
        "posts":Post.objects.all(),
        "categories":Category.objects.all(),
        "sub_categories":SubCategory.objects.all(),
    })
    
def post(request, post_id):
    post = Post.objects.get(id=post_id)
    categories = Category.objects.filter(posts = post).all()
    
    url_parameter = request.GET.get("title")
    if url_parameter:
        searches = Post.objects.filter(title__icontains=url_parameter)
    
        if request.is_ajax():
            html = render_to_string(
                template_name="posts/partial_result.html", 
                context={"posts_returned": searches}
            )
            data_dict = {"html_from_view": html}
            return JsonResponse(data=data_dict, safe=False)
    else:
        searches = Post.objects.all()
    
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
    
def aboutus(request):
    tag_cate = Category.objects.all()
    tag_subcate = SubCategory.objects.all()
    
    return render(request, "posts/aboutus.html",{
        "categories": tag_cate,
        "subcategories": tag_subcate,
    })
    
# def search(request):
#     ctx={}
    # search?post=<sth_post>&author=<sth_author>
    # post_url   = request.GET.get("post")
    # author_url = request.GET.get("author")
    # posts_returned = Post.object.filter(title__icontains=post_url)
    # author_returned= Author.objects.filter(name__icontains=author_url)
    # ctx["posts"] = post_returned
    # ctx["authors"] = author_returned

    # if request.is_ajax():
    #     html = render_to_string(
    #         template_name="partial_result.html", 
    #         context={"posts_returned": posts_returned,"author_returned":author_returned}
    #     )
    #     data_dict = {"html_from_view": html}
    #     return JsonResponse(data=data_dict, safe=False)

    # return render(request, "search.html", context=ctx)
    # return JsonResponse({
    #     "post_search": posts_returned,
    #     "author_search": author_returned,
    # })
    
    
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