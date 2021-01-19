from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect
from django.template.loader import render_to_string
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout


from .models import Post, Author, Category, SubCategory
from itertools import chain

# Create your views here.
def index(request):
    cate_news = Category.objects.get(name="news")
    news_posts = Post.objects.filter(categories=cate_news)
    cate_business = Category.objects.get(name="Business")
    business_posts = Post.objects.filter(categories=cate_business)
    
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
        "news_posts": news_posts,
        "business_posts": business_posts,
    })
    
def post(request, post_id):
    post = Post.objects.get(id=post_id)
    categories = Category.objects.filter(post_categories = post)
    
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

# categories1 = [] 
# sub_categories1 = []

def author(request, author_id):
    author = Author.objects.get(id=author_id)
    posts = Post.objects.filter(author=author)
    categorys =Category.objects.filter(post_categories__in=posts)
    sub_categorys =SubCategory.objects.filter(categories__in=categorys)

    
    return render(request, "posts/author.html", {
        "author":author,
        "posts":posts,
        "categories_tag": categorys,
        "sub_categories_tag": sub_categorys,
        "categories":Category.objects.all(),
        "sub_categories":SubCategory.objects.all()
    })
    
def category(request, category_id):
    category = Category.objects.get(id=category_id)
    posts = Post.objects.filter(categories=category)
    sub_categories = SubCategory.objects.filter(categories=category)
    
    return render(request, "posts/category.html", {
        "posts":posts,
        "category":category,
        "sub_categories_tag": sub_categories
    })
    
def aboutus(request):
    tag_cate = Category.objects.all()
    tag_subcate = SubCategory.objects.all()
    
    return render(request, "posts/aboutus.html",{
        "categories": tag_cate,
        "subcategories": tag_subcate,
    })
    
def login_view(request):
    if request.method == "POST":
        # Accessing username and password from form data
        username = request.POST["username"]
        password = request.POST["password"]
        # Check of username and password are correct, returning User object if so
        user = authenticate(request, username=username, password=password)
        # If user object is returned, log in and route to index page:
        if user:
            login(request,user)
            return HttpResponseRedirect(reverse("admin:index"))
        # Otherwise, return login page again with new context
        else:
            return render(request,"posts/index.html", {
                "message": "Invalid Credentials"
            })
    return render(request,"posts/index.html")
    
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