from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = "posts"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:post_id>", views.post, name="post"),
    path("author/<int:author_id>", views.author, name="author"),
    path("aboutus/", views.aboutus, name="aboutus"),
    # path("search/", views.search, name="search")
    # path("static/post.<int:post_id>/thumbnail.url", views.thumbnail, name="thumbnail"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
